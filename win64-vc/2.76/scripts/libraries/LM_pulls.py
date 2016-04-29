"""
Microvellum 
Pulls
Stores the UI and logic for the cabinet pull library
This script is responsible for the pull logic assembly and how to
save pulls to the library
"""

import bpy
import fd
import os

HIDDEN_FOLDER_NAME = "_HIDDEN"

METAL = ("Metals","Metals","Stainless Steel")

OBJECT_CATEGORY_NAME = "Cabinet Pulls"
THUMBNAIL_FILE_NAME = "thumbnail.blend"

preview_collections = {}

def get_cabinet_pull_category():
    return os.path.join(fd.get_library_dir("objects"),HIDDEN_FOLDER_NAME,OBJECT_CATEGORY_NAME)

def get_thumbnail_path():
    return os.path.join(os.path.dirname(bpy.app.binary_path),THUMBNAIL_FILE_NAME)

def enum_preview_from_dir(self,context):
    enum_items = []
    
    if context is None:
        return enum_items
    
    pcoll = preview_collections["main"]
    
    if len(pcoll.my_previews) > 0:
        return pcoll.my_previews
    
    update_enum_preview_from_dir(pcoll)
    
    return pcoll.my_previews    

def update_enum_preview_from_dir(pcoll):
    enum_items = []
    pcoll.clear()
    icon_dir = get_cabinet_pull_category()
    
    if icon_dir and os.path.exists(icon_dir):
        image_paths = []
        for fn in os.listdir(icon_dir):
            if fn.lower().endswith(".png"):
                image_paths.append(fn)

        for i, name in enumerate(image_paths):
            # generates a thumbnail preview for a file.
            filepath = os.path.join(icon_dir, name)
            thumb = pcoll.load(filepath, filepath, 'IMAGE')
            filename, ext = os.path.splitext(name)
            enum_items.append((filename, filename, filepath, thumb.icon_id, i))
            
    pcoll.my_previews = enum_items
    pcoll.my_previews_dir = icon_dir    

#---------SPEC GROUP POINTERS

class Material_Pointers():
    
    Pull_Finish = fd.Material_Pointer(METAL)

#---------FUNCTIONS

#---------ASSEMBLIES

class Standard_Pull(fd.Library_Assembly):
    
    library_name = "Cabinet Doors"
    type_assembly = "INSERT"
    property_id = "" #TODO: Create Prompts Page
    
    door_type = "" # Base, Tall, Upper, Sink, Suspended
    door_swing = "" # Left Swing, Right Swing, Double Door, Flip up

    def draw(self):
        g = bpy.context.scene.lm_pulls
        self.create_assembly()
        
        if self.door_type == "Base":
            pull_name = g.Base_Pull_Name
        if self.door_type == "Tall":
            pull_name = g.Tall_Pull_Name
        if self.door_type == "Upper":
            pull_name = g.Upper_Pull_Name
        if self.door_type == "Drawer":
            pull_name = g.Drawer_Pull_Name
        
        pull = self.add_object((HIDDEN_FOLDER_NAME,OBJECT_CATEGORY_NAME,pull_name))
        
        self.add_tab(name='Main Options',tab_type='VISIBLE')
        self.add_prompt(name="Pull Price",prompt_type='PRICE',value=0,tab_index=0)
        self.add_prompt(name="Hide",prompt_type='CHECKBOX',value=False,tab_index=0)
        self.add_prompt(name="Pull Length",prompt_type='DISTANCE',value=pull.obj.dimensions.x,tab_index=0)
        self.add_prompt(name="Pull X Location",prompt_type='DISTANCE',value=0,tab_index=0)
        self.add_prompt(name="Pull Z Location",prompt_type='DISTANCE',value=0,tab_index=0)
        self.add_prompt(name="Pull Rotation",prompt_type='ANGLE',value=0,tab_index=0)
        self.add_prompt(name="Pull Quantity",prompt_type='QUANTITY',value=1,tab_index=0)
        
        Width = self.get_var("dim_x","Width")
        Height = self.get_var("dim_z","Height")
        Depth = self.get_var("dim_y","Depth")
        Pull_X_Location = self.get_var("Pull X Location")
        Pull_Z_Location = self.get_var("Pull Z Location")
        Hide = self.get_var("Hide")
        
        pull.set_name(self.door_type + " Cabinet Pull")
        pull.x_loc('Width-Pull_Z_Location',[Width,Pull_Z_Location])
        pull.y_loc('Depth+IF(Depth<0,Pull_X_Location,-Pull_X_Location)',[Depth,Pull_X_Location,Pull_Z_Location])
        pull.z_loc('Height',[Height])
        pull.x_rot(value = -90)
        if self.door_swing == 'Left Swing':
            pull.z_rot(value = 180)
        pull.material("Pull_Finish")
        pull.hide('Hide',[Hide])
        
        self.update()
        
#---------INTERFACES

class MENU_Pull_Library_Options(bpy.types.Menu):
    bl_label = "Pull Library Options"

    def draw(self, context):
        layout = self.layout
        lib_path = get_cabinet_pull_category()
        layout.operator("fd_general.open_browser_window",text="Open Library Location in Browser",icon='FILE_FOLDER').path = lib_path
        layout.operator('pulls.add_object_to_library',text="Save Object to Pull Library",icon='SAVE_COPY')

#---------OPERATORS

class OPERATOR_Add_Object_To_Library(bpy.types.Operator):
    """ This will save the selected object to the pull library and create a thumbnail.
    """
    bl_idname = "pulls.add_object_to_library"
    bl_label = "Add Object to Pull Library"
    bl_description = "Save object to cabinet pull library"
    
    pull_name = bpy.props.StringProperty(name="Pull Name")
    
    @classmethod
    def poll(self,context):
        if context.object:
            if context.object.type == 'MESH' and context.mode == 'OBJECT':
                return True
            else:
                return False
        else:
            return False

    def save_to_lib(self,source_dir,filename,object_name,save_path):
        file = open(os.path.join(source_dir,"s_temp.py"),'w')
        file.write("import bpy\n")
        file.write("with bpy.data.libraries.load(r'" + os.path.join(source_dir,filename) + "', False, True) as (data_from, data_to):\n")
        file.write("    for obj in data_from.objects:\n")
        file.write("        if obj == '" + object_name + "':\n")
        file.write("            data_to.objects = [obj]\n")
        file.write("            break\n")
        file.write("for obj in data_to.objects:\n")
        file.write("    bpy.context.scene.objects.link(obj)\n")
        file.write("    obj.select = True\n")
        file.write("bpy.ops.wm.save_as_mainfile(filepath= r'" + os.path.join(save_path,filename) + "')")
        file.close()
        return os.path.join(source_dir,'s_temp.py')
    
    def create_tumbnail_script(self,source_dir,filename,object_name,save_path):
        file = open(os.path.join(source_dir,"t_temp.py"),'w')
        file.write("import bpy\n")
        file.write("with bpy.data.libraries.load(r'" + os.path.join(source_dir,filename) + "', False, True) as (data_from, data_to):\n")
        file.write("    for obj in data_from.objects:\n")
        file.write("        if obj == '" + object_name + "':\n")
        file.write("            data_to.objects = [obj]\n")
        file.write("            break\n")
        file.write("for obj in data_to.objects:\n")
        file.write("    bpy.context.scene.objects.link(obj)\n")
        file.write("    obj.select = True\n")
        file.write("    bpy.context.scene.objects.active = obj\n")
        file.write("    bpy.ops.view3d.camera_to_view_selected()\n")
        file.write("    render = bpy.context.scene.render\n")
        file.write("    render.use_file_extension = True\n")
        file.write("    render.filepath = r'" + os.path.join(save_path,filename.replace(".blend","")) + "'\n")
        file.write("    bpy.ops.render.render(write_still=True)\n")
        file.close()
        return os.path.join(source_dir,'t_temp.py')
                
    def invoke(self,context,event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=fd.get_prop_dialog_width(400))

    def draw(self, context):
        layout = self.layout
        layout.prop(self,"pull_name")

    def execute(self,context):
        import subprocess

        obj_pull = context.object
        obj_pull.name = self.pull_name
        
        if self.pull_name == "":
            self.report({'ERROR_INVALID_INPUT'},"Please Enter a Valid Pull Name!")
            return {'FINISHED'}             
        
        files = os.listdir(get_cabinet_pull_category())
        
        for file in files:
            filename, file_extension = os.path.splitext(file)
            if file_extension == ".blend":
                if filename == self.pull_name:
                    self.report({'ERROR_INVALID_INPUT'},"Pull Name: " + "\"" + self.pull_name + "\"" + " Already Exists in Library! \n Please Use a Different Name")
                    return {'FINISHED'}
        
        bpy.ops.wm.save_as_mainfile(filepath= bpy.app.tempdir + "\\" + self.pull_name + ".blend")
        
        save_script = self.save_to_lib(bpy.app.tempdir,self.pull_name + ".blend",self.pull_name,get_cabinet_pull_category())
        subprocess.call(bpy.app.binary_path + " -b --python " + save_script)
        
        thumbnail_script = self.create_tumbnail_script(bpy.app.tempdir,self.pull_name + ".blend",self.pull_name,get_cabinet_pull_category())
        subprocess.call(bpy.app.binary_path + ' "' + get_thumbnail_path() + '" -b --python "' + thumbnail_script + '"')
        
        #refresh tumbnail previews
        pcoll = preview_collections["main"]
        update_enum_preview_from_dir(pcoll)
        
        return {'FINISHED'}

class OPERATOR_Change_Pull(bpy.types.Operator):
    """ This will clear all the spec groups to save on file size.
    """
    bl_idname = "pulls.change_pull"
    bl_label = "Change Pull"
    bl_description = "This will all of the products with this global variable setting"
    bl_options = {'UNDO'}
    
    cabinet_type = bpy.props.StringProperty(name="Cabinet Type")
    pull_name = bpy.props.StringProperty(name="Pull Name")
    
    def execute(self, context):
        g = context.scene.lm_pulls
        if self.cabinet_type == "Base":
            g.Base_Pull_Name = self.pull_name
        if self.cabinet_type == "Tall":
            g.Tall_Pull_Name = self.pull_name
        if self.cabinet_type == "Upper":
            g.Upper_Pull_Name = self.pull_name
        if self.cabinet_type == "Drawer":
            g.Drawer_Pull_Name = self.pull_name
        return {'FINISHED'}

class OPERATOR_Update_Project(bpy.types.Operator):
    """ This will clear all the spec groups to save on file size.
    """
    bl_idname = "pulls.update_project"
    bl_label = "Change Pull"
    bl_description = "This will all of the products with this global variable setting"
    bl_options = {'UNDO'}
    
    cabinet_type = bpy.props.StringProperty(name = "Cabinet Type")

    def execute(self, context):
        g = context.scene.lm_pulls
        pulls = []
        for obj in context.scene.objects:
            if self.cabinet_type + " Cabinet Pull" in obj.mv.name_object:
                pulls.append(obj)
                
        if self.cabinet_type == "Base":
            pull_name = g.Base_Pull_Name
        if self.cabinet_type == "Tall":
            pull_name = g.Tall_Pull_Name
        if self.cabinet_type == "Upper":
            pull_name = g.Upper_Pull_Name
        if self.cabinet_type == "Drawer":
            pull_name = g.Drawer_Pull_Name
        
        for pull in pulls:
            pull_assembly = fd.Assembly(fd.get_assembly_bp(pull))
            pull_length = pull_assembly.get_prompt("Pull Length")
            new_pull = fd.get_object((HIDDEN_FOLDER_NAME,OBJECT_CATEGORY_NAME),pull_name)
            new_pull.mv.name_object = pull.mv.name_object
            new_pull.parent = pull.parent
            new_pull.location = pull.location
            new_pull.rotation_euler = pull.rotation_euler
            fd.assign_materials_from_pointers(new_pull)
            pull_length.set_value(new_pull.dimensions.x)
            fd.copy_drivers(pull,new_pull)
            
        fd.delete_obj_list(pulls)
        return {'FINISHED'}

class PROPERTIES_Scene_Variables(bpy.types.PropertyGroup):

    Main_Tabs = bpy.props.EnumProperty(name="Main Tabs",
                                       items=[('BASE',"Base Cabinets",'Show the base cabinet pulls.'),
                                              ('TALL',"Tall Cabinets",'Show the tall cabinet pulls.'),
                                              ('UPPER',"Upper Cabinets",'Show the upper cabinet pulls.'),
                                              ('DRAWER',"Drawer Cabinets",'Show the drawer cabinet pulls.')])

    Base_Pull_Name = bpy.props.EnumProperty(name="Base Pull Name",items=enum_preview_from_dir)
    
    Tall_Pull_Name = bpy.props.EnumProperty(name="Tall Pull Name",items=enum_preview_from_dir)
    
    Upper_Pull_Name = bpy.props.EnumProperty(name="Upper Pull Name",items=enum_preview_from_dir)
    
    Drawer_Pull_Name = bpy.props.EnumProperty(name="Drawer Pull Name",items=enum_preview_from_dir)

    def draw(self,layout):
        box = layout.box()
        row = box.row(align=True)
        row.prop(self,"Main_Tabs",text="")
        row.menu('MENU_Pull_Library_Options',text="",icon='DOWNARROW_HLT')
        
        if self.Main_Tabs == 'BASE':
            row = box.row()
            row.prop(self,"Base_Pull_Name",text="")
            row = box.row()
            row.template_icon_view(self,"Base_Pull_Name")
            row = box.row()
            row.operator('pulls.update_project',text="Refresh Drawing",icon='FILE_REFRESH').cabinet_type = "Base"
        if self.Main_Tabs == 'TALL':
            row = box.row()
            row.prop(self,"Tall_Pull_Name",text="")
            row = box.row()
            row.template_icon_view(self,"Tall_Pull_Name")
            row = box.row()
            row.operator('pulls.update_project',text="Refresh Drawing",icon='FILE_REFRESH').cabinet_type = "Tall"
        if self.Main_Tabs == 'UPPER':
            row = box.row()
            row.prop(self,"Upper_Pull_Name",text="")
            row = box.row()
            row.template_icon_view(self,"Upper_Pull_Name")
            row = box.row()
            row.operator('pulls.update_project',text="Refresh Drawing",icon='FILE_REFRESH').cabinet_type = "Upper"
        if self.Main_Tabs == 'DRAWER':
            row = box.row()
            row.prop(self,"Drawer_Pull_Name",text="")
            row = box.row()
            row.template_icon_view(self,"Drawer_Pull_Name")
            row = box.row()
            row.operator('pulls.update_project',text="Refresh Drawing",icon='FILE_REFRESH').cabinet_type = "Drawer"


def register():
    bpy.utils.register_class(PROPERTIES_Scene_Variables)
    bpy.utils.register_class(OPERATOR_Update_Project)
    bpy.utils.register_class(OPERATOR_Change_Pull)
    bpy.utils.register_class(OPERATOR_Add_Object_To_Library)
    bpy.utils.register_class(MENU_Pull_Library_Options)

    bpy.types.Scene.lm_pulls = bpy.props.PointerProperty(type = PROPERTIES_Scene_Variables)

    pcoll = bpy.utils.previews.new()
    pcoll.my_previews_dir = ""
    pcoll.my_previews = ()

    preview_collections["main"] = pcoll
    
def unregister():
    bpy.utils.unregister_class(PROPERTIES_Scene_Variables)
    bpy.utils.unregister_class(OPERATOR_Update_Project)
    bpy.utils.unregister_class(OPERATOR_Change_Pull)
    bpy.utils.unregister_class(OPERATOR_Add_Object_To_Library)
    bpy.utils.unregister_class(MENU_Pull_Library_Options)
