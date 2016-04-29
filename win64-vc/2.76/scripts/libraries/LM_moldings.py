"""
Microvellum 
Moldings
Stores the UI and logic for the molding library
This script is responsible for how the auto extrude molding functionality works
and the functionality on how to save new modlings to the library
"""

import fd
import bpy
import os

HIDDEN_FOLDER_NAME = "_HIDDEN"
CROWN_CATEGORY_NAME = "Crown Molding Profiles"
BASE_CATEGORY_NAME = "Base Molding Profiles"
THUMBNAIL_FILE_NAME = "thumbnail.blend"

MOLDING_MATERIAL = ("Paint","Textured Wall Paint","Paint White")

preview_collections = {}

def get_thumbnail_path():
    return os.path.join(os.path.dirname(bpy.app.binary_path),THUMBNAIL_FILE_NAME)

def get_profile_directory():
    return os.path.join(fd.get_library_dir("objects"),HIDDEN_FOLDER_NAME)

# def get_crown_previews(self,context):
#     enum_items = []
#     
#     if context is None:
#         return enum_items
#     
#     icon_dir = os.path.join(get_profile_directory(),CROWN_CATEGORY_NAME)
#     
#     pcoll = preview_collections["crown"]
#     
#     if len(pcoll.my_previews) > 0:
#         return pcoll.my_previews
#     
#     update_enum_preview_from_dir(pcoll, icon_dir)    
#     
#     return pcoll.my_previews
# 
# def get_base_previews(self,context):
#     enum_items = []
#     
#     if context is None:
#         return enum_items
#     
#     icon_dir = os.path.join(get_profile_directory(),BASE_CATEGORY_NAME)
#     
#     pcoll = preview_collections["base"]
#     
#     if len(pcoll.my_previews) > 0:
#         return pcoll.my_previews
#     
#     update_enum_preview_from_dir(pcoll, icon_dir)
#     
#     return pcoll.my_previews

def update_enum_preview_from_dir(pcoll, icon_dir):
    enum_items = []
    pcoll.clear()
    
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
            enum_items.append((filename, filename, filename, thumb.icon_id, i))

    pcoll.my_previews = enum_items
    pcoll.my_previews_dir = icon_dir

def get_carcass_insert(product):
    new_list = []
    inserts = fd.get_insert_bp_list(product.obj_bp,new_list)
    for insert in inserts:
        if "Carcass Options" in insert.mv.PromptPage.COL_MainTab:
            carcass = fd.Assembly(insert)
            return carcass
        
def add_rectangle_molding(product,is_crown=True):
    carcass = get_carcass_insert(product)
    if carcass:
        width = product.obj_x.location.x
        depth = product.obj_y.location.y
        toe_kick_setback = carcass.get_prompt("Toe Kick Setback")
        left_fin_end = carcass.get_prompt("Left Fin End")
        right_fin_end = carcass.get_prompt("Right Fin End")
        left_side_wall_filler = carcass.get_prompt("Left Side Wall Filler")
        right_side_wall_filler = carcass.get_prompt("Right Side Wall Filler")
        setback = 0
        if toe_kick_setback and is_crown == False:
            setback = toe_kick_setback.value()
        
        points = []
        
        #LEFT
        if left_side_wall_filler.value() > 0:
            points.append((-left_side_wall_filler.value(),depth+setback,0))
        
        elif left_fin_end.value() == True:
            points.append((0,0,0))
            points.append((0,depth+setback,0))
        else:
            points.append((0,depth+setback,0))
            
        #RIGHT
        if right_side_wall_filler.value() > 0:
            points.append((width + right_side_wall_filler.value(),depth+setback,0))
        
        elif right_fin_end.value() == True:
            points.append((width,depth+setback,0))
            points.append((width,0,0))
        else:
            points.append((width,depth+setback,0))
        
        return points
    
def add_inside_molding(product,is_crown=True,is_notched=True):
    carcass = get_carcass_insert(product)
    width = product.obj_x.location.x
    depth = product.obj_y.location.y
    toe_kick_setback = carcass.get_prompt("Toe Kick Setback")
    left_fin_end = carcass.get_prompt("Left Fin End")
    right_fin_end = carcass.get_prompt("Right Fin End")
    left_side_wall_filler = carcass.get_prompt("Left Side Wall Filler")
    right_side_wall_filler = carcass.get_prompt("Right Side Wall Filler")
    cabinet_depth_left = carcass.get_prompt("Cabinet Depth Left")
    cabinet_depth_right = carcass.get_prompt("Cabinet Depth Right")

    setback = 0
    if toe_kick_setback and is_crown == False:
        setback = toe_kick_setback.value()
    
    points = []
    
    #LEFT
    if left_side_wall_filler.value() > 0:
        points.append((cabinet_depth_left.value()-setback,depth-left_side_wall_filler.value(),0))
    
    elif left_fin_end.value() == True:
        points.append((0,depth,0))
        points.append((cabinet_depth_left.value()-setback,depth,0))
    else:
        points.append((cabinet_depth_left.value()-setback,depth,0))
        
    #CENTER
    if is_notched:
        points.append((cabinet_depth_left.value()-setback,-cabinet_depth_right.value()+setback,0))
        
    #RIGHT
    if right_side_wall_filler.value() > 0:
        points.append((width + right_side_wall_filler.value(),-cabinet_depth_right.value()+setback,0))
    
    elif right_fin_end.value() == True:
        points.append((width,-cabinet_depth_right.value()+setback,0))
        points.append((width,0,0))
    else:
        points.append((width,-cabinet_depth_right.value()+setback,0))
    
    return points

def add_transition_molding(product,is_crown=True):
    carcass = get_carcass_insert(product)
    if carcass:
        width = product.obj_x.location.x
        toe_kick_setback = carcass.get_prompt("Toe Kick Setback")
        left_fin_end = carcass.get_prompt("Left Fin End")
        right_fin_end = carcass.get_prompt("Right Fin End")
        left_side_wall_filler = carcass.get_prompt("Left Side Wall Filler")
        right_side_wall_filler = carcass.get_prompt("Right Side Wall Filler")
        cabinet_depth_left = carcass.get_prompt("Cabinet Depth Left")
        cabinet_depth_right = carcass.get_prompt("Cabinet Depth Right")
        left_side_thickness = carcass.get_prompt("Left Side Thickness")
        right_side_thickness = carcass.get_prompt("Right Side Thickness")
        
        setback = 0
        if toe_kick_setback and is_crown == False:
            setback = toe_kick_setback.value()
        
        points = []
        
        #LEFT
        if left_side_wall_filler.value() > 0:
            points.append((-left_side_wall_filler.value(),-cabinet_depth_left.value()+setback,0))
            points.append((left_side_thickness.value(),-cabinet_depth_left.value()+setback,0))
            
        elif left_fin_end.value() == True:
            points.append((0,0,0))
            points.append((0,-cabinet_depth_left.value()+setback,0))
            points.append((left_side_thickness.value(),-cabinet_depth_left.value()+setback,0))
        else:
            points.append((0,-cabinet_depth_left.value()+setback,0))
            points.append((left_side_thickness.value(),-cabinet_depth_left.value()+setback,0))
            
        #RIGHT
        if right_side_wall_filler.value() > 0:
            points.append((width - right_side_thickness.value() + right_side_wall_filler.value(),-cabinet_depth_right.value()+setback,0))
            points.append((width + right_side_wall_filler.value(),-cabinet_depth_right.value()+setback,0))
        
        elif right_fin_end.value() == True:
            points.append((width - right_side_thickness.value() + right_side_wall_filler.value(),-cabinet_depth_right.value()+setback,0))
            points.append((width,-cabinet_depth_right.value()+setback,0))
            points.append((width,0,0))
        else:
            points.append((width - right_side_thickness.value() + right_side_wall_filler.value(),-cabinet_depth_right.value()+setback,0))
            points.append((width,-cabinet_depth_right.value()+setback,0))
        
        return points

class Material_Pointers():
    
    Cabinet_Moldings = fd.Material_Pointer(MOLDING_MATERIAL)

    Wall_Moldings = fd.Material_Pointer(MOLDING_MATERIAL)

class MENU_Molding_Library_Options(bpy.types.Menu):
    bl_label = "Molding Library Options"

    def draw(self, context):
        g = context.scene.lm_moldings
        layout = self.layout
        
        if g.Main_Tabs == 'BASE':
            lib_path = os.path.join(get_profile_directory(),BASE_CATEGORY_NAME)
            layout.operator("fd_general.open_browser_window",text="Open Library Location in Browser",icon='FILE_FOLDER').path = lib_path
            layout.operator('moldings.add_object_to_library',text="Save Object to Base Molding Library",icon='SAVE_COPY')
            layout.operator('moldings.delete_molding',text="Delete Molding",icon='X')
            
        if g.Main_Tabs == 'CROWN':
            lib_path = os.path.join(get_profile_directory(),CROWN_CATEGORY_NAME)
            layout.operator("fd_general.open_browser_window",text="Open Library Location in Browser",icon='FILE_FOLDER').path = lib_path
            layout.operator('moldings.add_object_to_library',text="Save Object to Crown Molding Library",icon='SAVE_COPY')
            layout.operator('moldings.delete_molding',text="Delete Molding",icon='X')                        
    
class OPERATOR_Add_Object_To_Library(bpy.types.Operator):
    """ This will save the selected object to the molding library and create a thumbnail.
    """
    bl_idname = "moldings.add_object_to_library"
    bl_label = "Add Object to Molding Library"
    bl_description = "Save Object to Molding Library"
    
    molding_name = bpy.props.StringProperty(name="Molding Name")
    
    @classmethod
    def poll(self,context):
        if context.object:
            if context.object.type == 'CURVE' and context.mode == 'OBJECT':
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
        file.write("camera = bpy.context.scene.camera\n")
        file.write("camera.rotation_euler = (0,0,0)\n")
        file.write("for obj in data_to.objects:\n")
        file.write("    bpy.context.scene.objects.link(obj)\n")
        file.write("    obj.select = True\n")
        file.write("    obj.data.dimensions = '2D'\n")
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
        layout.prop(self,"molding_name")

    def execute(self,context):
        import subprocess
        g = context.scene.lm_moldings
        
        obj_molding = context.object
        obj_molding.name = self.molding_name
        
        if g.Main_Tabs == 'BASE':
            molding_cat = os.path.join(get_profile_directory(),BASE_CATEGORY_NAME)
            
        if g.Main_Tabs == 'CROWN':
            molding_cat = os.path.join(get_profile_directory(),CROWN_CATEGORY_NAME)
        
        if self.molding_name == "":
            self.report({'ERROR_INVALID_INPUT'},"Please Enter a Valid Molding Name!")
            return {'FINISHED'}             
        
        files = os.listdir(molding_cat)
        
        for file in files:
            filename, file_extension = os.path.splitext(file)
            if file_extension == ".blend":
                if filename == self.molding_name:
                    self.report({'ERROR_INVALID_INPUT'},"Molding Name: " + "\"" + self.molding_name + "\"" + " Already Exists in Library! \n Please Use a Different Name")
                    return {'FINISHED'}
        
        bpy.ops.wm.save_as_mainfile(filepath= bpy.app.tempdir + "\\" + self.molding_name + ".blend")
        
        save_script = self.save_to_lib(bpy.app.tempdir,self.molding_name + ".blend",self.molding_name,molding_cat)
        subprocess.call(bpy.app.binary_path + " -b --python " + save_script)
        
        thumbnail_script = self.create_tumbnail_script(bpy.app.tempdir,self.molding_name + ".blend",self.molding_name,molding_cat)
        subprocess.call(bpy.app.binary_path + ' "' + get_thumbnail_path() + '" -b --python "' + thumbnail_script + '"')
        
        if g.Main_Tabs == 'BASE':
            pcoll = preview_collections["base"]
            update_enum_preview_from_dir(pcoll,molding_cat)
        if g.Main_Tabs == 'CROWN':
            pcoll = preview_collections["crown"]
            update_enum_preview_from_dir(pcoll,molding_cat)
        
        return {'FINISHED'}    
    
class OPERATOR_Place_Molding(bpy.types.Operator):
    """ This will be called when you drop a molding in the 3D viewport.
    """
    bl_idname = "moldings.place_molding"
    bl_label = "Place Molding"
    bl_description = "This will add a molding to the scene"
    bl_options = {'UNDO'}

    filepath = bpy.props.StringProperty(name="File Path")
    molding_type = bpy.props.StringProperty(name="Molding Type")

    profile = None
    extrusion = None
    product = None
    wall = None
    
    is_crown = False
    toe_kick_setback = 0
    left_fin_end = False
    right_fin_end = False
    left_cabinet_depth = 0
    right_cabinet_depth = 0
    left_filler = 0
    right_filler = 0
    
    def execute(self, context):
        return {'FINISHED'}

    def set_perspective(self,context):
        """ Raycasting only works in perspective mode
            This function makes sure the view is in perspective mode
        """
        if context.space_data.type == 'VIEW_3D':
            if not context.space_data.region_3d.is_perspective:
                bpy.ops.view3d.view_persportho()

    def create_extrusions(self):
        bpy.ops.curve.primitive_bezier_curve_add(enter_editmode=False)
        obj_curve = bpy.context.active_object
        obj_curve.data.show_handles = False
        obj_curve.data.bevel_object = self.profile
        obj_curve.location = (0,0,0)
        
        obj_curve.data.splines[0].bezier_points[0].co = (0,0,0)
        obj_curve.data.splines[0].bezier_points[1].co = (fd.inches(36),0,0)
        
        bpy.ops.object.editmode_toggle()
        bpy.ops.curve.select_all(action='SELECT')
        bpy.ops.curve.handle_type_set(type='VECTOR')
        bpy.ops.object.editmode_toggle()
        obj_curve.data.dimensions = '2D'
        self.extrusion = obj_curve

    def collect_prompts(self):
        new_list = []
        inserts = fd.get_insert_bp_list(self.product.obj_bp,new_list)
        left_fin_end = None
        right_fin_end = None
        left_cabinet_depth = None
        right_cabinet_depth = None
        toe_kick_setback = None
        left_filler = None
        right_filler = None
        for insert_bp in inserts:
            if "Carcass Options" in insert_bp.mv.PromptPage.COL_MainTab:
                insert = fd.Assembly(insert_bp)
                left_fin_end = insert.get_prompt("Left Fin End")
                right_fin_end = insert.get_prompt("Right Fin End")
                left_cabinet_depth = insert.get_prompt("Cabinet Depth Left")
                right_cabinet_depth = insert.get_prompt("Cabinet Depth Right")
                toe_kick_setback = insert.get_prompt("Toe Kick Setback")
                left_filler = insert.get_prompt("Left Filler Amount")
                right_filler = insert.get_prompt("Right Filler Amount")
                
        if left_fin_end:
            self.left_fin_end = left_fin_end.value()
        else:
            self.left_fin_end = False
            
        if right_fin_end:
            self.right_fin_end = right_fin_end.value()
        else:
            self.right_fin_end = False
            
        if left_cabinet_depth:
            self.left_cabinet_depth = left_cabinet_depth.value()
        else:
            self.left_cabinet_depth = 0
            
        if right_cabinet_depth:
            self.right_cabinet_depth = right_cabinet_depth.value()
        else:
            self.right_cabinet_depth = 0
            
        if toe_kick_setback:
            self.toe_kick_setback = toe_kick_setback.value()
        else:
            self.toe_kick_setback = 0
            
        if left_filler:
            self.left_filler = left_filler.value()
        else:
            self.left_filler = 0
            
        if right_filler:
            self.right_filler = right_filler.value()
        else:
            self.right_filler = 0
        
    def set_up_cabinet_extrusion(self):
        self.collect_prompts()

        #DETERMINE NUMBER OF POINTS IN SPLINE
        point_count = 2
        if self.left_cabinet_depth and self.right_cabinet_depth:
            point_count +=1
        
        if self.left_fin_end:
            point_count +=1
        
        if self.right_fin_end:
            point_count +=1
            
        #IF THE SPLINE DOESN'T HAVE THE CORRECT NUMBER OF POINTS REMOVE SPLINE AND CREATE NEW ONE
        if len(self.extrusion.data.splines[0].bezier_points) != point_count:
            self.extrusion.data.splines.clear()
            spline = self.extrusion.data.splines.new('BEZIER')
            spline.bezier_points.add(count=point_count-1)
            
        spline = self.extrusion.data.splines[0]
        for point in spline.bezier_points:
            point.handle_left_type = 'VECTOR'
            point.handle_right_type = 'VECTOR'
            
        #SET Z LOCATION
        product_depth = self.product.obj_y.location.y
        bpy.context.active_object.location.z = 0
        
        if self.is_crown and self.product.obj_z.location.z > 0:
            bpy.context.active_object.location.z = self.product.obj_z.location.z
            
        #BUILD SPLINE
        if self.left_cabinet_depth and self.right_cabinet_depth: #INSIDE CORNER CABINET
            
            if self.left_fin_end and not self.right_fin_end:
                spline.bezier_points[0].co = (0,product_depth,0)
                spline.bezier_points[1].co = (self.left_cabinet_depth-self.toe_kick_setback,product_depth,0)
                spline.bezier_points[2].co = (self.left_cabinet_depth-self.toe_kick_setback,-self.right_cabinet_depth+self.toe_kick_setback,0)
                spline.bezier_points[3].co = (self.product.obj_x.location.x,-self.right_cabinet_depth+self.toe_kick_setback,0)
            elif not self.left_fin_end and self.right_fin_end:
                spline.bezier_points[0].co = (self.left_cabinet_depth-self.toe_kick_setback,product_depth,0)
                spline.bezier_points[1].co = (self.left_cabinet_depth-self.toe_kick_setback,-self.right_cabinet_depth+self.toe_kick_setback,0)
                spline.bezier_points[2].co = (self.product.obj_x.location.x,-self.right_cabinet_depth+self.toe_kick_setback,0)
                spline.bezier_points[3].co = (self.product.obj_x.location.x,0,0)
            elif not self.left_fin_end and not self.right_fin_end:
                spline.bezier_points[0].co = (self.left_cabinet_depth-self.toe_kick_setback,product_depth,0)
                spline.bezier_points[1].co = (self.left_cabinet_depth-self.toe_kick_setback,-self.right_cabinet_depth+self.toe_kick_setback,0)
                spline.bezier_points[2].co = (self.product.obj_x.location.x,-self.right_cabinet_depth+self.toe_kick_setback,0)
            else:
                spline.bezier_points[0].co = (0,product_depth,0)
                spline.bezier_points[1].co = (self.left_cabinet_depth-self.toe_kick_setback,product_depth,0)
                spline.bezier_points[2].co = (self.left_cabinet_depth-self.toe_kick_setback,-self.right_cabinet_depth+self.toe_kick_setback,0)
                spline.bezier_points[3].co = (self.product.obj_x.location.x,-self.right_cabinet_depth+self.toe_kick_setback,0)
                spline.bezier_points[4].co = (self.product.obj_x.location.x,0,0)
        
        else: #STANDARD CABINET

            if self.is_crown:
                self.toe_kick_setback = 0

            if self.left_fin_end and not self.right_fin_end:
                spline.bezier_points[0].co = (-self.left_filler,0,0)
                spline.bezier_points[1].co = (-self.left_filler,product_depth+self.toe_kick_setback,0)
                spline.bezier_points[2].co = (self.product.obj_x.location.x+self.right_filler,product_depth+self.toe_kick_setback,0)
            elif not self.left_fin_end and self.right_fin_end:
                spline.bezier_points[0].co = (-self.left_filler,product_depth+self.toe_kick_setback,0)
                spline.bezier_points[1].co = (self.product.obj_x.location.x+self.right_filler,product_depth+self.toe_kick_setback,0)
                spline.bezier_points[2].co = (self.product.obj_x.location.x+self.right_filler,0,0)
            elif not self.left_fin_end and not self.right_fin_end:
                spline.bezier_points[0].co = (-self.left_filler,product_depth+self.toe_kick_setback,0)
                spline.bezier_points[1].co = (self.product.obj_x.location.x+self.right_filler,product_depth+self.toe_kick_setback,0)
            else:
                spline.bezier_points[0].co = (-self.left_filler,0,0)
                spline.bezier_points[1].co = (-self.left_filler,product_depth+self.toe_kick_setback,0)
                spline.bezier_points[2].co = (self.product.obj_x.location.x+self.right_filler,product_depth+self.toe_kick_setback,0)
                spline.bezier_points[3].co = (self.product.obj_x.location.x+self.right_filler,0,0)

    def set_up_wall_extrusion(self):
        spline = self.extrusion.data.splines[0]
        if len(self.extrusion.data.splines[0].bezier_points) != 2:
            self.extrusion.data.splines.clear()
            spline = self.extrusion.data.splines.new('BEZIER')
            spline.bezier_points.add(count=1)
            
        z_loc = 0
            
        if self.is_crown:
            z_loc += self.wall.obj_z.location.z - self.profile.dimensions[1]
            
        for point in spline.bezier_points:
            point.handle_left_type = 'VECTOR'
            point.handle_right_type = 'VECTOR'
            
        spline.bezier_points[0].co = (0,0,0)
        spline.bezier_points[1].co = (self.wall.obj_x.location.x,0,0)

    def get_profile(self):
        g = bpy.context.scene.lm_cabinet_closet_designer
        if self.molding_type == 'Base':
            self.profile = fd.get_object((HIDDEN_FOLDER_NAME,BASE_CATEGORY_NAME),object_name=g.base_moldings)
        else:
            self.is_crown = True
            self.profile = fd.get_object((HIDDEN_FOLDER_NAME,CROWN_CATEGORY_NAME),g.crown_moldings)

    def invoke(self,context,event):
        self.get_profile()
        self.create_extrusions()
        context.window.cursor_set('PAINT_BRUSH')
        self.set_perspective(context)
        context.scene.update() # THE SCENE MUST BE UPDATED FOR RAY CAST TO WORK
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def cancel_drop(self,context,event):
        bpy.ops.object.select_all(action='DESELECT')
        if self.extrusion:
            self.extrusion.select = True
            context.scene.objects.active = self.extrusion
            bpy.ops.object.delete()
        bpy.context.window.cursor_set('DEFAULT')
        return {'FINISHED'}
    
    def get_molding_material(self):
        spec_group = bpy.context.scene.cabinetlib.spec_groups[bpy.context.scene.cabinetlib.spec_group_index]
        bpy.ops.cabinetlib.sync_material_slots(object_name=self.extrusion.name)
        if self.product:
            pointer = spec_group.materials['Cabinet_Moldings']
            self.extrusion.cabinetlib.material_slots[0].pointer_name = pointer.name
            return fd.get_material((pointer.library_name,pointer.category_name), pointer.item_name)
        else:
            pointer = spec_group.materials['Wall_Moldings']
            self.extrusion.cabinetlib.material_slots[0].pointer_name = pointer.name
            return fd.get_material((pointer.library_name,pointer.category_name), pointer.item_name)
        
    def molding_drop(self,context,event):
        selected_point, selected_obj = fd.get_selection_point(context,event)
        obj_wall_bp = fd.get_wall_bp(selected_obj)
        obj_product_bp = fd.get_bp(selected_obj,'PRODUCT')
        if obj_product_bp:
            self.product = fd.Assembly(obj_product_bp)
            self.set_up_cabinet_extrusion()
            self.extrusion.parent = obj_product_bp

            if event.type == 'LEFTMOUSE' and event.value == 'PRESS':
                bpy.ops.fd_object.add_material_slot(object_name=self.extrusion.name)
                self.extrusion.material_slots[0].material = self.get_molding_material()
                if self.is_crown:
                    self.extrusion.mv.name_object = "Cabinet Crown Molding"
                else:
                    self.extrusion.mv.name_object = "Cabinet Base Molding"
                if not event.shift:
                    bpy.context.window.cursor_set('DEFAULT')
                    return {'FINISHED'}
                else:
                    self.create_extrusions()
        else:
            self.product = None
            if obj_wall_bp:
                self.wall = fd.Wall(obj_wall_bp)
                self.set_up_wall_extrusion()
                self.extrusion.parent = obj_wall_bp
                if self.is_crown:
                    self.extrusion.location.z = self.wall.obj_z.location.z - self.extrusion.dimensions.z
                else:
                    self.extrusion.location.z = 0
            if event.type == 'LEFTMOUSE' and event.value == 'PRESS':
                bpy.ops.fd_object.add_material_slot(object_name=self.extrusion.name)
                self.extrusion.material_slots[0].material = self.get_molding_material()
                if self.is_crown:
                    self.extrusion.mv.name_object = "Wall Crown Molding"
                else:
                    self.extrusion.mv.name_object = "Wall Base Molding"
                if not event.shift:
                    bpy.context.window.cursor_set('DEFAULT')
                    return {'FINISHED'}
                else:
                    self.create_extrusions()
                    
        if event.type == 'RIGHTMOUSE':
            pass
        return {'RUNNING_MODAL'}

    def modal(self, context, event):
        context.area.tag_redraw()
        context.window.cursor_set('PAINT_BRUSH')
        if event.type in {'MIDDLEMOUSE', 'WHEELUPMOUSE', 'WHEELDOWNMOUSE'}:
            return {'PASS_THROUGH'}
        
        if event.type in {'ESC'}:
            self.cancel_drop(context,event)
            return {'FINISHED'}
        
        return self.molding_drop(context,event)
        
class OPERATOR_Auto_Add_Molding(bpy.types.Operator):
    bl_idname = "moldings.auto_add_molding"
    bl_label = "Add Molding" 
    bl_options = {'UNDO'}

    molding_type = bpy.props.StringProperty(name="Molding Type")

    crown_profile = None
    base_profile = None
    
    tall_cabinet_switch = fd.inches(60)
    
    def get_profile(self):
        closet_g = bpy.context.scene.lm_closets
        g = bpy.context.scene.lm_cabinet_closet_designer
        if self.molding_type == 'Base':
            self.profile = fd.get_object((HIDDEN_FOLDER_NAME,BASE_CATEGORY_NAME),object_name=g.base_moldings)
            
        else:
            self.is_crown = True
            self.profile = fd.get_object((HIDDEN_FOLDER_NAME,CROWN_CATEGORY_NAME),g.crown_moldings)
            closet_g.Crown_Molding_Height = self.profile.dimensions.y
            closet_g.Crown_Molding_Depth = self.profile.dimensions.x
            
            bpy.ops.fd_prompts.update_all_prompts_in_scene(prompt_name="Crown Molding Depth",
                                                           prompt_type='DISTANCE',
                                                           float_value=closet_g.Crown_Molding_Depth)
            
            bpy.ops.fd_prompts.update_all_prompts_in_scene(prompt_name="Crown Molding Height",
                                                           prompt_type='DISTANCE',
                                                           float_value=closet_g.Crown_Molding_Height)
            
    def get_products(self):
        products = []
        for obj in bpy.context.visible_objects:
            if obj.mv.type == 'BPASSEMBLY' and obj.cabinetlib.type_group == 'PRODUCT':
                product = fd.Assembly(obj)
                products.append(product)
        return products
        
    def create_extrusion(self,points,is_crown=True,product=None):
        if self.profile is None:
            self.get_profile()
        
        bpy.ops.curve.primitive_bezier_curve_add(enter_editmode=False)
        obj_curve = bpy.context.active_object
        if is_crown:
            obj_curve.lm_moldings.is_crown_molding = True
        else:
            obj_curve.lm_moldings.is_base_molding = True
        obj_curve.data.splines.clear()
        spline = obj_curve.data.splines.new('BEZIER')
        spline.bezier_points.add(count=len(points) - 1)        
        obj_curve.data.show_handles = False
        obj_curve.data.bevel_object = self.profile
        obj_curve.cabinetlib.spec_group_index = product.obj_bp.cabinetlib.spec_group_index
        
        bpy.ops.fd_object.add_material_slot(object_name=obj_curve.name)
        bpy.ops.cabinetlib.sync_material_slots(object_name=obj_curve.name)
        obj_curve.cabinetlib.material_slots[0].pointer_name = "Cabinet_Moldings"

        obj_curve.location = (0,0,0)
        
        for i, point in enumerate(points):
            obj_curve.data.splines[0].bezier_points[i].co = point
        
        
        bpy.ops.object.editmode_toggle()
        bpy.ops.curve.select_all(action='SELECT')
        bpy.ops.curve.handle_type_set(type='VECTOR')
        bpy.ops.object.editmode_toggle()
        obj_curve.data.dimensions = '2D'
        fd.assign_materials_from_pointers(obj_curve)
        return obj_curve
        
    def add_closet_molding(self,product,is_crown=True):
        thickness = product.get_prompt("Panel Thickness")
        start_x = 0
        for i in range(1,10):
            points = []
            width = product.get_prompt("Opening " + str(i) + " Width")
            if width:
                next_width = product.get_prompt("Opening " + str(i + 1) + " Width")
                height = product.get_prompt("Opening " + str(i) + " Height")
                depth = product.get_prompt("Opening " + str(i) + " Depth")
                
                if i == 1: #FIRST
                    left_side_wall_filler = product.get_prompt("Left Side Wall Filler")
                    left_end_condition = product.get_prompt("Left End Condition")
                    next_height = product.get_prompt("Opening " + str(i + 1) + " Height")
                    next_depth = product.get_prompt("Opening " + str(i + 1) + " Depth")
                    
                    if left_side_wall_filler and left_side_wall_filler.value() > 0:
                        points.append((-left_side_wall_filler.value(),-depth.value(),0))
                    
                    else:
                    
                        if left_end_condition.value() == 'EP':
                            points.append((0,0,0))
                            points.append((0,-depth.value(),0))
                        else:
                            points.append((0,-depth.value(),0))
    
                    if (height.value() > next_height.value()) or (depth.value() > next_depth.value()):
                        left_side_thickness = product.get_prompt("Left Side Thickness")
                        start_x = width.value() + left_side_thickness.value() + thickness.value()
                        points.append((start_x,-depth.value(),0))
                        points.append((start_x,0,0))
                    else:
                        left_side_thickness = product.get_prompt("Left Side Thickness")
                        start_x = width.value() + left_side_thickness.value()
                        points.append((start_x,-depth.value(),0))
                    
                elif next_width: #MIDDLE
                    prev_height = product.get_prompt("Opening " + str(i - 1) + " Height")
                    prev_depth = product.get_prompt("Opening " + str(i - 1) + " Depth")
                    next_height = product.get_prompt("Opening " + str(i + 1) + " Height")
                    next_depth = product.get_prompt("Opening " + str(i + 1) + " Depth")
                    
                    if (height.value() > prev_height.value()) or (depth.value() > prev_depth.value()):
                        points.append((start_x,0,0))
                        points.append((start_x,-depth.value(),0))
                        start_x += thickness.value()
                    else:
                        points.append((start_x,-depth.value(),0))
                        start_x += thickness.value()
                    
                    if (height.value() > next_height.value()) or (depth.value() > next_depth.value()):
                        start_x += width.value() + thickness.value()
                        points.append((start_x,-depth.value(),0))
                        points.append((start_x,0,0))
                    else:
                        start_x += width.value()
                        points.append((start_x,-depth.value(),0))
                
                else: #LAST
                    right_side_wall_filler = product.get_prompt("Right Side Wall Filler")
                    right_end_condition = product.get_prompt("Right End Condition")
                    prev_height = product.get_prompt("Opening " + str(i - 1) + " Height")
                    prev_depth = product.get_prompt("Opening " + str(i - 1) + " Depth")
                    
                    if (height.value() > prev_height.value()) or (depth.value() > prev_depth.value()):
                        points.append((start_x,0,0))
                        points.append((start_x,-depth.value(),0))
                        start_x += thickness.value()
                    else:
                        points.append((start_x,-depth.value(),0))
                        start_x += thickness.value()
                    
                    if right_side_wall_filler and right_side_wall_filler.value() > 0:
                        start_x += width.value() + thickness.value() + right_side_wall_filler.value()
                        points.append((start_x,-depth.value(),0))
                    else:
                    
                        if right_end_condition.value() == 'EP':
                            start_x += width.value()
                            points.append((start_x,-depth.value(),0))
                            points.append((start_x,0,0))
                        else:
                            start_x += width.value() + thickness.value()
                            points.append((start_x,-depth.value(),0))
                    
                curve = self.create_extrusion(points,is_crown,product)
                curve.parent = product.obj_bp
                if is_crown:
                    curve.location.z = height.value()
    
    def clean_up_room(self):
        """ Removes all of the Dimensions and other objects
            That were added to the scene from this command
            We dont want multiple objects added on top of each other
            So we must clean up the scene before running this command 
        """
        is_crown = True if self.molding_type == 'Crown' else False
        objs = []
        for obj in bpy.data.objects:
            if is_crown:
                if obj.lm_moldings.is_crown_molding == True:
                    objs.append(obj)
            else:
                if obj.lm_moldings.is_base_molding == True:
                    objs.append(obj)
        fd.delete_obj_list(objs)

    def set_curve_location(self,product,curve,is_crown):
        curve.parent = product.obj_bp
        if is_crown:
            if product.obj_z.location.z < 0:
                curve.location.z = 0
            else:
                curve.location.z = product.obj_z.location.z

    def execute(self, context):
        self.clean_up_room()
        self.profile = None
        products = self.get_products()
        for product in products:
            shape = product.obj_bp.cabinetlib.product_shape
            is_crown = True if self.molding_type == 'Crown' else False
            
            if product.obj_z.location.z < 0 and is_crown == False:
                continue # Don't add base molding to upper cabinets
            elif product.obj_z.location.z < 0 and is_crown and product.obj_bp.location.z > fd.inches(50):
                pass #Add Crown to Upper Cabinets
            elif product.obj_z.location.z < self.tall_cabinet_switch and is_crown:
                continue # Don't add crown molding to base cabinets
            
            if shape == 'RECTANGLE':
                points = add_rectangle_molding(product,is_crown)
                if points:
                    curve = self.create_extrusion(points,is_crown,product)
                    self.set_curve_location(product,curve,is_crown)
                        
            if shape == 'INSIDE_NOTCH':
                points = add_inside_molding(product,is_crown,True)
                if points:
                    curve = self.create_extrusion(points,is_crown,product)
                    self.set_curve_location(product,curve,is_crown)
                
            if shape == 'INSIDE_DIAGONAL':
                points = add_inside_molding(product,is_crown,False)
                if points:
                    curve = self.create_extrusion(points,is_crown,product)
                    self.set_curve_location(product,curve,is_crown)
                
            if shape == 'OUTSIDE_DIAGONAL':
                pass #TODO
            
            if shape == 'OUTSIDE_RADIUS':
                pass #TODO
            
            if shape == 'TRANSITION':
                points = add_transition_molding(product,is_crown)
                if points:
                    curve = self.create_extrusion(points,is_crown,product)
                    self.set_curve_location(product,curve,is_crown)

            if shape == 'CUSTOM':
                self.add_closet_molding(product,True if self.molding_type == 'Crown' else False)

        return {'FINISHED'}
        
class OPERATOR_Delete_Molding(bpy.types.Operator):
    bl_idname = "moldings.delete_molding"
    bl_label = "Delete Molding" 
    bl_options = {'UNDO'}

    molding_type = bpy.props.StringProperty(name="Molding Type")

    def execute(self, context):
        is_crown = True if self.molding_type == 'Crown' else False
        objs = []
        for obj in context.scene.objects:
            if is_crown:
                if obj.lm_moldings.is_crown_molding == True:
                    objs.append(obj)
            else:
                if obj.lm_moldings.is_base_molding == True:
                    objs.append(obj)
        fd.delete_obj_list(objs)
        return {'FINISHED'}
        
class PROPERTIES_Scene_Variables(bpy.types.PropertyGroup):
    
    Main_Tabs = bpy.props.EnumProperty(name="Main Tabs",
                                       items=[('BASE',"Base Molding",'Show the available Base Molding.'),
                                              ('CROWN',"Crown Molding",'Show the available Crown Molding.')])
    
#     Crown_Molding = bpy.props.EnumProperty(name="Crown Molding",items=get_crown_previews)
#     
#     Base_Molding = bpy.props.EnumProperty(name="Base Molding",items=get_base_previews)
    
    def draw(self,layout):
        g = bpy.context.scene.lm_cabinet_closet_designer
        box = layout.box()
        row = box.row(align=True)
        row.prop(self,"Main_Tabs",expand=True)
        row.menu('MENU_Molding_Library_Options',text="",icon='DOWNARROW_HLT')
        
        if self.Main_Tabs == 'BASE':
            row = box.row()
            row.prop(g,"base_moldings",text="")
            row = box.row()
            #WORK
            row.template_icon_view(g,"base_moldings",show_labels=True)
            row = box.row()
            row.scale_y = 1.5
            row.operator('moldings.place_molding',text="Manual Place",icon='GREASEPENCIL').molding_type = "Base"
            row.operator('moldings.auto_add_molding',text="Auto Place",icon='GREASEPENCIL').molding_type = "Base"
            
        if self.Main_Tabs == 'CROWN':
            row = box.row()
            row.prop(g,"crown_moldings",text="")
            row = box.row()
            row.template_icon_view(g,"crown_moldings",show_labels=True)
            row = box.row()
            row.scale_y = 1.5
            row.operator('moldings.place_molding',text="Manual Place",icon='GREASEPENCIL').molding_type = "Crown"
            row.operator('moldings.auto_add_molding',text="Auto Place",icon='GREASEPENCIL').molding_type = "Crown"


class PROPERTIES_Object_Variables(bpy.types.PropertyGroup):
    
    is_crown_molding = bpy.props.BoolProperty(name="Is Crown Molding",
                                              description="Used to Delete Molding When Using Auto Add Molding Operator",
                                              default=False)
    
    is_base_molding = bpy.props.BoolProperty(name="Is Base Molding",
                                             description="Used to Delete Molding When Using Auto Add Molding Operator",
                                             default=False)

        
def register():
    bpy.utils.register_class(PROPERTIES_Scene_Variables)
    bpy.utils.register_class(PROPERTIES_Object_Variables)
    bpy.utils.register_class(MENU_Molding_Library_Options)
    bpy.utils.register_class(OPERATOR_Add_Object_To_Library)
    bpy.utils.register_class(OPERATOR_Place_Molding)
    bpy.utils.register_class(OPERATOR_Auto_Add_Molding)
    bpy.utils.register_class(OPERATOR_Delete_Molding)
    
    bpy.types.Scene.lm_moldings = bpy.props.PointerProperty(type = PROPERTIES_Scene_Variables)
    bpy.types.Object.lm_moldings = bpy.props.PointerProperty(type = PROPERTIES_Object_Variables)

    base_coll = bpy.utils.previews.new()
    base_coll.my_previews_dir = ""
    base_coll.my_previews = ()

    preview_collections["base"] = base_coll
    
    crown_coll = bpy.utils.previews.new()
    crown_coll.my_previews_dir = ""
    crown_coll.my_previews = ()

    preview_collections["crown"] = crown_coll
    
def unregister():
    bpy.utils.unregister_class(PROPERTIES_Scene_Variables)
    bpy.utils.unregister_class(PROPERTIES_Object_Variables)
    bpy.utils.unregister_class(MENU_Molding_Library_Options)
    bpy.utils.unregister_class(OPERATOR_Add_Object_To_Library)
    bpy.utils.unregister_class(OPERATOR_Place_Molding)
    bpy.utils.unregister_class(OPERATOR_Auto_Add_Molding)
    bpy.utils.unregister_class(OPERATOR_Delete_Molding)

