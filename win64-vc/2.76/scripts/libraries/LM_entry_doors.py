import bpy
import fd
import math

from bpy.types import (Panel, 
                       Operator, 
                       PropertyGroup)

from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       BoolVectorProperty,
                       PointerProperty,
                       CollectionProperty,
                       EnumProperty)

HIDDEN_FOLDER_NAME = "_HIDDEN"
DOOR_LIBRARY_NAME = "Entry Door Assemblies"
DOOR_FRAME_CATEGORY_NAME = "Door Frames"
DOOR_PANEL_CATEGORY_NAME = "Door Panels"

DOOR_HANDLE_LIBRARY = "Hardware"
DOOR_HANDLE_CATEGORY = "Entry Door Handles"

class Global_Variables(PropertyGroup):
    Single_Panel_Width = FloatProperty(name="Door Single Panel Width",
                                       description="Default width for single panel entry doors",
                                       default=fd.inches(42.0),
                                       unit='LENGTH')    
    
    Double_Panel_Width = FloatProperty(name="Door Double Panel Width",
                                       description="Default width for double panel entry doors",
                                       default=fd.inches(78.0),
                                       unit='LENGTH')     
    
    Double_Panel_Width = FloatProperty(name="Door Double Panel Width",
                                       description="Default width for double panel entry doors",
                                       default=fd.inches(84.0),
                                       unit='LENGTH')  
    
    Door_Height = FloatProperty(name="Door Height",
                                       description="Default height for entry doors",
                                       default=fd.inches(83.0),
                                       unit='LENGTH')     
    
    Door_Depth = FloatProperty(name="Door Depth",
                                       description="Default depth for entry doors",
                                       default=fd.inches(6.0),
                                       unit='LENGTH')     
    
    Handle_Height = FloatProperty(name="Handle Height",
                                       description="Default handle height",
                                       default=fd.inches(37.0),
                                       unit='LENGTH')      

class Entry_Door(fd.Library_Assembly):
    library_name = "Entry Doors"
    category_name = ""
    assembly_name = ""
    property_id = "cabinetlib.entry_door_prompts"
    type_assembly = "PRODUCT"
    mirror_z = False
    mirror_y = False
    width = 0
    height = 0
    depth = 0
    
    door_frame = ""
    door_panel = ""
    door_handle = ""
    double_door = False
    
    def draw(self):
        g = bpy.context.scene.lm_entry_doors
        self.create_assembly()
        
        if self.door_panel != "":
            self.add_tab(name='Main Options',tab_type='VISIBLE')
            self.add_prompt(name="Reverse Swing",prompt_type='CHECKBOX',value=False,tab_index=0)
            self.add_prompt(name="Door Rotation",prompt_type='ANGLE',value=0.0,tab_index=0)
            if self.double_door != True:
                self.add_prompt(name="Door Swing",prompt_type='COMBOBOX',items=["Left Swing","Right Swing"],value=False,tab_index=0)
        
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Door_Rotation = self.get_var('Door Rotation')
        Reverse_Swing = self.get_var("Reverse Swing")
        if self.double_door != True:
            Swing = self.get_var('Door Swing')

        door_frame = self.add_assembly((HIDDEN_FOLDER_NAME,DOOR_LIBRARY_NAME,DOOR_FRAME_CATEGORY_NAME,self.door_frame))
        door_frame.set_name("Door Frame")
        door_frame.x_dim('Width',[Width])
        door_frame.y_dim('Depth',[Depth])
        door_frame.z_dim('Height',[Height])        
        
        if self.door_panel != "":
            door_panel = self.add_assembly((HIDDEN_FOLDER_NAME,DOOR_LIBRARY_NAME,DOOR_PANEL_CATEGORY_NAME,self.door_panel))
            door_panel.set_name("Door Panel")
            if self.double_door != True:
                door_panel.x_loc('IF(Door_Swing==1,Width-INCH(3),INCH(3))',[Width, Swing])
                door_panel.y_loc('IF(Reverse_Swing,IF(Door_Swing==0,INCH(1.75),0),IF(Door_Swing==0,Depth,Depth-INCH(1.75)))',[Swing, Reverse_Swing, Depth])
                door_panel.z_rot('IF(Door_Swing==1,radians(180)+IF(Reverse_Swing,Door_Rotation,-Door_Rotation),IF(Reverse_Swing,-Door_Rotation,Door_Rotation))',
                                 [Door_Rotation, Swing, Reverse_Swing])
                
            else:
                door_panel.x_loc(value = fd.inches(3))
                door_panel.y_loc('Depth-IF(Reverse_Swing,INCH(4.25),INCH(0))',[Reverse_Swing, Depth])
                door_panel.z_rot('IF(Reverse_Swing,-Door_Rotation,Door_Rotation)',[Door_Rotation, Reverse_Swing])                
                
            door_panel.x_dim('Width-INCH(6)',[Width])
            door_panel.z_dim('Height-INCH(3.25)',[Height])

        if self.door_handle != "":
            door_handle = self.add_object((HIDDEN_FOLDER_NAME,DOOR_HANDLE_CATEGORY,self.door_handle))
            door_handle.obj.parent = door_panel.obj_bp
            door_handle.set_name("Door Handle")
            door_handle.x_loc('Width-INCH(9)',[Width])
            door_handle.y_loc(value = fd.inches(-0.875))
            door_handle.z_loc(value = g.Handle_Height)

        if self.double_door == True:
            door_panel.x_dim('(Width-INCH(6))*0.5',[Width])
            door_handle.x_loc('(Width*0.5)-INCH(6)',[Width])
        
            door_panel_right = self.add_assembly((HIDDEN_FOLDER_NAME,DOOR_LIBRARY_NAME,DOOR_PANEL_CATEGORY_NAME,self.door_panel))
            door_panel_right.set_name("Door Panel Right")
            door_panel_right.x_loc('Width-INCH(3)',[Width])
            door_panel_right.y_loc('Depth-INCH(1.75)-IF(Reverse_Swing,INCH(4.25),INCH(0))',[Reverse_Swing, Depth])
            door_panel_right.z_rot('radians(180)+IF(Reverse_Swing,Door_Rotation,-Door_Rotation)',[Door_Rotation, Reverse_Swing])
            door_panel_right.x_dim('(Width-INCH(6))*0.5',[Width])
            door_panel_right.z_dim('Height-INCH(3.25)',[Height])     
            
            Dpr_Width = door_panel_right.get_var('dim_x','Dpr_Width')
            
            door_handle_right = self.add_object((HIDDEN_FOLDER_NAME,DOOR_HANDLE_CATEGORY,self.door_handle))
            door_handle_right.set_name("Door Handle Right")
            door_handle_right.obj.parent = door_panel_right.obj_bp
            door_handle_right.x_loc('Dpr_Width-INCH(3)', [Dpr_Width])
            door_handle_right.y_loc(value = fd.inches(-0.875))
            door_handle_right.z_loc(value = g.Handle_Height)
                
        self.update()       
  
class PRODUCT_Entry_Door_Frame(Entry_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_entry_doors
        self.category_name = "Entry Doors"
        self.assembly_name = "Entry Door Frame"
        self.width = g.Single_Panel_Width
        self.height = g.Door_Height
        self.depth = g.Door_Depth
        
        self.door_frame = "Door_Frame"   
  
class PRODUCT_Entry_Door_Double_Panel(Entry_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_entry_doors
        self.category_name = "Entry Doors"
        self.assembly_name = "Entry Door Double Panel"
        self.width = g.Single_Panel_Width
        self.height = g.Door_Height
        self.depth = g.Door_Depth
        
        self.door_frame = "Door_Frame"
        self.door_panel = "Door_Panel_Double"
        self.door_handle = "Door_Handle"  
 
class PRODUCT_Entry_Door_Inset_Panel(Entry_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_entry_doors
        self.category_name = "Entry Doors"
        self.assembly_name = "Entry Door Inset Panel"
        self.width = g.Single_Panel_Width
        self.height = g.Door_Height
        self.depth = g.Door_Depth
        
        self.door_frame = "Door_Frame"
        self.door_panel = "Door_Panel_Inset"
        self.door_handle = "Door_Handle"   
 
class PRODUCT_Entry_Door_Glass_Panel(Entry_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_entry_doors
        self.category_name = "Entry Doors"
        self.assembly_name = "Entry Door Glass Panel"
        self.width = g.Single_Panel_Width
        self.height = g.Door_Height
        self.depth = g.Door_Depth
        
        self.door_frame = "Door_Frame"
        self.door_panel = "Door_Panel_Glass"
        self.door_handle = "Door_Handle"   
        
class PRODUCT_Entry_Door_Glass_Georgian_Panel(Entry_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_entry_doors
        self.category_name = "Entry Doors"
        self.assembly_name = "Entry Door Glass Georgian Panel"
        self.width = g.Single_Panel_Width
        self.height = g.Door_Height
        self.depth = g.Door_Depth
        
        self.door_frame = "Door_Frame"
        self.door_panel = "Door_Panel_Glass_Georgian"
        self.door_handle = "Door_Handle"         
        
class PRODUCT_Entry_Door_Glass_Border_Panel(Entry_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_entry_doors
        self.category_name = "Entry Doors"
        self.assembly_name = "Entry Door Glass Border Panel"
        self.width = g.Single_Panel_Width
        self.height = g.Door_Height
        self.depth = g.Door_Depth
        
        self.door_frame = "Door_Frame"
        self.door_panel = "Door_Panel_Glass_Marginal_Border"
        self.door_handle = "Door_Handle"          
        
class PRODUCT_Entry_Double_Door_Double_Panel(Entry_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_entry_doors
        self.category_name = "Entry Doors"
        self.assembly_name = "Entry Double Door Double Panel"
        self.width = g.Double_Panel_Width
        self.height = g.Door_Height
        self.depth = g.Door_Depth
        
        self.double_door = True
        self.door_frame = "Door_Frame"
        self.door_panel = "Door_Panel_Double"
        self.door_handle = "Door_Handle"         
        
class PRODUCT_Entry_Double_Door_Inset_Panel(Entry_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_entry_doors
        self.category_name = "Entry Doors"
        self.assembly_name = "Entry Double Door Inset Panel"
        self.width = g.Double_Panel_Width
        self.height = g.Door_Height
        self.depth = g.Door_Depth
        
        self.double_door = True
        self.door_frame = "Door_Frame"
        self.door_panel = "Door_Panel_Inset"
        self.door_handle = "Door_Handle"         
        
class PRODUCT_Entry_Double_Door_Glass_Panel(Entry_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_entry_doors
        self.category_name = "Entry Doors"
        self.assembly_name = "Entry Double Door Glass Panel"
        self.width = g.Double_Panel_Width
        self.height = g.Door_Height
        self.depth = g.Door_Depth
        
        self.double_door = True
        self.door_frame = "Door_Frame"
        self.door_panel = "Door_Panel_Glass"
        self.door_handle = "Door_Handle"        
        
class PRODUCT_Entry_Double_Door_Glass_Georgian_Panel(Entry_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_entry_doors
        self.category_name = "Entry Doors"
        self.assembly_name = "Entry Double Door Glass Georgian Panel"
        self.width = g.Double_Panel_Width
        self.height = g.Door_Height
        self.depth = g.Door_Depth
        
        self.double_door = True
        self.door_frame = "Door_Frame"
        self.door_panel = "Door_Panel_Glass_Georgian"
        self.door_handle = "Door_Handle"       
        
class PRODUCT_Entry_Double_Door_Glass_Border_Panel(Entry_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_entry_doors
        self.category_name = "Entry Doors"
        self.assembly_name = "Entry Double Door Glass Border Panel"
        self.width = g.Double_Panel_Width
        self.height = g.Door_Height
        self.depth = g.Door_Depth
        
        self.double_door = True
        self.door_frame = "Door_Frame"
        self.door_panel = "Door_Panel_Glass_Marginal_Border"
        self.door_handle = "Door_Handle"             
        
class PROMPTS_Entry_Door_Prompts(Operator):
    bl_idname = "cabinetlib.entry_door_prompts"
    bl_label = "Entry Door Prompts" 
    bl_options = {'UNDO'}
    
    object_name = StringProperty(name="Object Name")
    
    width = FloatProperty(name="Width",unit='LENGTH',precision=4)
    height = FloatProperty(name="Height",unit='LENGTH',precision=4)
    depth = FloatProperty(name="Depth",unit='LENGTH',precision=4)

    door_rotation = FloatProperty(name="Door Rotation",subtype='ANGLE',min=0,max=math.radians(110))
    
    door_swing = EnumProperty(name="Door Swing",items=[('Left Swing',"Left Swing","Left Swing"),
                                                       ('Right Swing',"Right Swing","Right Swing")])
    product = None
    
    open_door_prompt = None
    
    door_swing_prompt = None
    
    @classmethod
    def poll(cls, context):
        return True

    def check(self, context):
        self.product.obj_x.location.x = self.width
         
        if self.product.obj_bp.cabinetlib.mirror_y:
            self.product.obj_y.location.y = -self.depth
        else:
            self.product.obj_y.location.y = self.depth
         
        if self.product.obj_bp.cabinetlib.mirror_z:
            self.product.obj_z.location.z = -self.height
        else:
            self.product.obj_z.location.z = self.height
             
        if self.open_door_prompt:
            self.open_door_prompt.set_value(self.door_rotation)
            
        if self.door_swing_prompt:
            self.door_swing_prompt.set_value(self.door_swing)            
             
        self.product.obj_bp.location = self.product.obj_bp.location
        self.product.obj_bp.location = self.product.obj_bp.location
            
        return True

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self,context,event):
        obj = bpy.data.objects[self.object_name]
        obj_product_bp = fd.get_bp(obj,'PRODUCT')
        self.product = fd.Assembly(obj_product_bp)
        if self.product.obj_bp:
            self.depth = math.fabs(self.product.obj_y.location.y)
            self.height = math.fabs(self.product.obj_z.location.z)
            self.width = math.fabs(self.product.obj_x.location.x)
            
            try:
                self.open_door_prompt = self.product.get_prompt("Door Rotation")
                self.door_rotation = self.open_door_prompt.value() 
            except:
                pass
            
            try:
                self.door_swing_prompt = self.product.get_prompt("Door Swing")  
                self.door_swing = self.door_swing_prompt.value()         
            except:
                pass
                
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=fd.get_prop_dialog_width(480))

    def draw_product_size(self,layout):
        row = layout.row()
        box = row.box()
        col = box.column(align=True)

        row1 = col.row(align=True)
        if self.object_has_driver(self.product.obj_x):
            row1.label('Width: ' + str(fd.unit(math.fabs(self.product.obj_x.location.x))))
        else:
            row1.label('Width:')
            row1.prop(self,'width',text="")
            row1.prop(self.product.obj_x,'hide',text="")
        
        row1 = col.row(align=True)
        if self.object_has_driver(self.product.obj_z):
            row1.label('Height: ' + str(fd.unit(math.fabs(self.product.obj_z.location.z))))
        else:
            row1.label('Height:')
            row1.prop(self,'height',text="")
            row1.prop(self.product.obj_z,'hide',text="")
        
        row1 = col.row(align=True)
        if self.object_has_driver(self.product.obj_y):
            row1.label('Depth: ' + str(fd.unit(math.fabs(self.product.obj_y.location.y))))
        else:
            row1.label('Depth:')
            row1.prop(self,'depth',text="")
            row1.prop(self.product.obj_y,'hide',text="")
            
    def object_has_driver(self,obj):
        if obj.animation_data:
            if len(obj.animation_data.drivers) > 0:
                return True
            
    def draw_product_prompts(self,layout):

        if "Main Options" in self.product.obj_bp.mv.PromptPage.COL_MainTab:
            door_swing = self.product.get_prompt("Door Swing")
            reverse_swing = self.product.get_prompt("Reverse Swing")
            
            box = layout.box()
            col = box.column(align=True)
            col.label("Main Options:")
            row = col.row()
            row.label("Open Door")
            row.prop(self,'door_rotation',text="",slider=True)   
            if door_swing:
                col = box.column()
                row = col.row()                
                row.label("Door Swing")
                row.prop(self, 'door_swing',text="")
            col = box.column()
            row = col.row()                
            row.label("Reverse Swing")
            row.prop(reverse_swing,'CheckBoxValue',text="")            
    
    def draw_product_placment(self,layout):
        box = layout.box()
        row = box.row()
        row.label('Location:')
        row.prop(self.product.obj_bp,'location',index=0,text="")

        
    def draw(self, context):
        layout = self.layout
        if self.product.obj_bp:
            if self.product.obj_bp.name in context.scene.objects:
                box = layout.box()
                
                split = box.split(percentage=.8)
                split.label(self.product.obj_bp.mv.name_object + " | " + self.product.obj_bp.cabinetlib.spec_group_name,icon='LATTICE_DATA')
                split.menu('MENU_Current_Cabinet_Menu',text="Menu",icon='DOWNARROW_HLT')
                
                self.draw_product_size(box)
                self.draw_product_prompts(box)
                self.draw_product_placment(box)        
        
def register():
    bpy.utils.register_class(Global_Variables)
    bpy.types.Scene.lm_entry_doors = PointerProperty(type = Global_Variables)
    bpy.utils.register_class(PROMPTS_Entry_Door_Prompts)
    
def unregister():
    bpy.utils.unregister_class(Global_Variables)
    bpy.utils.unregister_class(PROMPTS_Entry_Door_Prompts)      
        