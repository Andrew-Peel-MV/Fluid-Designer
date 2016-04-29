"""
Microvellum 
Columns
Stores the logic and product defs for columns
"""

import bpy
import fd
import math

HIDDEN_FOLDER_NAME = "_HIDDEN"
EXPOSED_CABINET_MATERIAL = ("Plastics","White Melamine")
UNEXPOSED_CABINET_MATERIAL = ("Wood","Wood Core","Particle Board")
SEMI_EXPOSED_CABINET_MATERIAL = ("Plastics","White Melamine")
PART_WITH_FRONT_EDGEBANDING = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Cut Parts","Part with Front Edgebanding")
CABINET_ASSEMBLY_LIB_NAME = "Cabinet Assemblies"
ASSEMBLY_LIBRARY_NAME = "Columns"
OBJECT_LIBRARY_NAME = "Osborne Wood Products"
OBJECT_CATEGORY_NAME = "Cabinet Molding"
        
#---------SPEC GROUP POINTERS
        
class Material_Pointers():
    
    Concealed_Surface = fd.Material_Pointer(UNEXPOSED_CABINET_MATERIAL)
    
    Exposed_Exterior_Surface = fd.Material_Pointer(EXPOSED_CABINET_MATERIAL)

    Semi_Exposed_Surface = fd.Material_Pointer(SEMI_EXPOSED_CABINET_MATERIAL)
    
    Exposed_Exterior_Edge = fd.Material_Pointer(EXPOSED_CABINET_MATERIAL)

class Cutpart_Pointers():
    
    Base_Side_FE = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                      core="Concealed_Surface",
                                      top="Semi_Exposed_Surface",
                                      bottom="Exposed_Exterior_Surface")
    
class Edgepart_Pointers():
    
    Cabinet_Body_Edges = fd.Edgepart_Pointer(thickness=fd.inches(.01),
                                             material="Exposed_Exterior_Edge")


#---------PRODUCT TEMPLATES

class Column(fd.Library_Assembly):
    library_name = "Columns"
    category_name = "Standard Columns"
    property_id = "cabnetlib.column_prompts"
    type_assembly = "PRODUCT"

    product_type = None

    object_name = ""
    height_above_floor = 0
    trim = None

    def draw(self):
        self.create_assembly()

        self.add_tab(name='Basic Column Options',tab_type='VISIBLE')
        self.add_tab(name='Formuls',tab_type='HIDDEN')
        self.add_prompt(name="Extend Left End",prompt_type='CHECKBOX',value=False,tab_index=0)
        self.add_prompt(name="Extend Right End",prompt_type='CHECKBOX',value=False,tab_index=0)
        self.add_prompt(name="Panel Depth",prompt_type='DISTANCE',value=fd.inches(4),tab_index=0)
        self.add_prompt(name="Part Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)

        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Extend_Left_End = self.get_var("Extend Left End")
        Extend_Right_End = self.get_var("Extend Right End")
        Panel_Depth = self.get_var("Panel Depth")
        Part_Thickness = self.get_var("Part Thickness")

        left_part = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        left_part.set_name("Left Part")
        left_part.x_loc(value = 0)
        left_part.y_loc('IF(Extend_Left_End,0,Depth+Panel_Depth)',[Extend_Left_End,Depth,Panel_Depth])
        left_part.z_loc(value = 0)
        left_part.x_rot(value = 0)
        left_part.y_rot(value = -90)
        left_part.z_rot(value = 0)
        left_part.x_dim('Height',[Height])
        left_part.y_dim('IF(Extend_Left_End,Depth,-Panel_Depth)',[Depth,Extend_Left_End,Panel_Depth])
        left_part.z_dim('-Part_Thickness',[Part_Thickness])
        left_part.cutpart('Base_Side_FE')
        left_part.edgebanding('Cabinet_Body_Edges',l1=True)

        right_part = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        right_part.set_name("Right Part")
        right_part.x_loc('Width',[Width])
        right_part.y_loc('IF(Extend_Right_End,0,Depth+Panel_Depth)',[Extend_Right_End,Depth,Panel_Depth])
        right_part.z_loc(value = 0)
        right_part.x_rot(value = 0)
        right_part.y_rot(value = -90)
        right_part.z_rot(value = 0)
        right_part.x_dim('Height',[Height])
        right_part.y_dim('IF(Extend_Right_End,Depth,-Panel_Depth)',[Depth,Extend_Right_End,Panel_Depth])
        right_part.z_dim('Part_Thickness',[Part_Thickness])
        right_part.cutpart('Base_Side_FE')
        right_part.edgebanding('Cabinet_Body_Edges',l1=True)

        front_part = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        front_part.set_name("Front Part")
        front_part.x_loc('Part_Thickness',[Part_Thickness])
        front_part.y_loc('Depth',[Depth])
        front_part.z_loc(value = 0)
        front_part.x_rot(value = 0)
        front_part.y_rot(value = -90)
        front_part.z_rot(value = -90)
        front_part.x_dim('Height',[Height])
        front_part.y_dim('Width-(Part_Thickness*2)',[Width,Part_Thickness])
        front_part.z_dim('Part_Thickness',[Part_Thickness])
        front_part.cutpart('Base_Side_FE')
        front_part.edgebanding('Cabinet_Body_Edges',l1=True)
        
        if self.object_name != "":
            deco_molding = self.add_object((OBJECT_LIBRARY_NAME,OBJECT_LIBRARY_NAME,self.object_name))
            deco_molding.set_name("Column_Trim")
            deco_molding.x_loc(value = 0)
            deco_molding.y_loc('Depth',[Depth])
            if self.product_type == "Upper":
                deco_molding.z_loc('Height',[Height])
            else:
                deco_molding.z_loc(value = 0)
            deco_molding.x_rot(value = 0)
            deco_molding.y_rot(value = 0)
            deco_molding.z_rot(value = 0)
            deco_molding.material("Exposed_Exterior_Surface")

        self.update()
       
class Angled_Column(fd.Library_Assembly):
    library_name = "Columns"
    category_name = "Angled Columns"
    property_id = "angled_columns.column_prompts"
    type_assembly = "PRODUCT"
    detail_piece = ""
    detail_type = ''
    orientation = ''

    product_type = None

    object_name = ""
    height_above_floor = 0
    trim = None

    def draw(self):  
        self.create_assembly()

        self.add_tab(name='Basic Column Options',tab_type='VISIBLE')
        self.add_prompt(name="Extend Left End",prompt_type='CHECKBOX',value=False,tab_index=0)
        self.add_prompt(name="Extend Right End",prompt_type='CHECKBOX',value=False,tab_index=0)
        self.add_prompt(name="Panel Depth",prompt_type='DISTANCE',value=fd.inches(4),tab_index=0)

        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')        
        
        detail = self.add_assembly((HIDDEN_FOLDER_NAME,CABINET_ASSEMBLY_LIB_NAME,ASSEMBLY_LIBRARY_NAME,self.detail_piece))
        detail.obj_bp.mv.name_object = self.assembly_name + " Column Style"
        detail.material("Exposed_Exterior_Surface")
        detail.y_rot(value = -90)              
        detail.y_loc("Depth+INCH(1.75)",[Depth])
        
        if self.orientation == 'LEFT':
            detail.z_rot(value = 90)
            detail.x_loc(value = fd.inches(1.75)) 
                       
            if self.detail_type == 'C':
                column = self.add_assembly((HIDDEN_FOLDER_NAME,CABINET_ASSEMBLY_LIB_NAME,ASSEMBLY_LIBRARY_NAME,"Column_C_Left"))

            elif self.detail_type == 'R':
                column = self.add_assembly((HIDDEN_FOLDER_NAME,CABINET_ASSEMBLY_LIB_NAME,ASSEMBLY_LIBRARY_NAME,"Column_R_Left"))
                
        elif self.orientation == 'RIGHT':
            detail.z_rot(value = 180)
            detail.x_loc(value = fd.inches(0.25))           
            
            if self.detail_type == 'C':
                column = self.add_assembly((HIDDEN_FOLDER_NAME,CABINET_ASSEMBLY_LIB_NAME,ASSEMBLY_LIBRARY_NAME,"Column_C_Right"))
                
            elif self.detail_type == 'R':
                column = self.add_assembly((HIDDEN_FOLDER_NAME,CABINET_ASSEMBLY_LIB_NAME,ASSEMBLY_LIBRARY_NAME,"Column_R_Right"))
            
        column.material("Exposed_Exterior_Surface")    
        column.x_dim('Width',[Width])
        column.y_dim('Depth',[Depth])       
        
        if self.product_type == 'UPPER':
            column.z_loc("Height",[Height])
            column.z_dim('-Height',[Height])
            detail.z_loc("Height",[Height])
            detail.x_dim("-Height",[Height])
            
        elif self.product_type == 'TALL':
            column.z_dim('Height',[Height])
            detail.x_dim("Height*0.5",[Height])
            detail2= self.add_assembly((HIDDEN_FOLDER_NAME,CABINET_ASSEMBLY_LIB_NAME,ASSEMBLY_LIBRARY_NAME,self.detail_piece))
            detail2.obj_bp.mv.name_object = self.assembly_name + " Column Style"
            detail2.material("Exposed_Exterior_Surface")
            detail2.y_loc("Depth+INCH(1.75)",[Depth])
            detail2.z_loc("Height*0.5",[Height])
            detail2.y_rot(value = -90)              
            detail2.x_dim("Height*0.5",[Height])
            
            if self.orientation == 'LEFT':
                detail2.z_rot(value = 90)
                detail2.x_loc(value = fd.inches(1.75))          
            elif self.orientation == 'RIGHT':
                detail2.z_rot(value = 180)
                detail2.x_loc(value = fd.inches(0.25))                        
            
        else:
            column.z_dim('Height',[Height])
            detail.x_dim("Height",[Height])  
            
        self.update()       
                
#---------PRODUCT: STARTER CABINETS

class PRODUCT_Base_Column(Column):
    
    def __init__(self):
        g = bpy.context.scene.lm_columns
        self.category_name = "Standard Columns"
        self.assembly_name = "Base Column"
        self.width = g.Default_Column_Width
        self.height = g.Base_Column_Height
        self.depth = g.Base_Column_Depth

class PRODUCT_Tall_Column(Column):
    
    def __init__(self):
        g = bpy.context.scene.lm_columns
        self.category_name = "Standard Columns"
        self.assembly_name = "Tall Column"
        self.width = g.Default_Column_Width
        self.height = g.Tall_Column_Height
        self.depth = g.Tall_Column_Depth
        
class PRODUCT_Upper_Column(Column):
    
    def __init__(self):
        g = bpy.context.scene.lm_columns
        self.category_name = "Standard Columns"
        self.assembly_name = "Upper Column"
        self.width = g.Default_Column_Width
        self.height = g.Upper_Column_Height
        self.depth = g.Upper_Column_Depth
        self.mirror_z = True
        self.height_above_floor = g.Height_Above_Floor
        
class PRODUCT_Base_Angled_Column_Left(Angled_Column):
    
    def __init__(self):
        g = bpy.context.scene.lm_columns
        g_styles = bpy.context.scene.lm_cabinet_closet_designer
        self.product_type = 'BASE'
        self.category_name = "Angled Columns"
        self.assembly_name = "Base Angled Column Left"
        self.detail_piece = g_styles.base_column_styles
        self.orientation = 'LEFT'
        self.detail_type = 'C'
        self.width = g.Default_Column_Width
        self.height = g.Base_Column_Height
        self.depth = g.Base_Column_Depth
        
class PRODUCT_Base_Angled_Column_Right(Angled_Column):
    
    def __init__(self):
        g = bpy.context.scene.lm_columns
        g_styles = bpy.context.scene.lm_cabinet_closet_designer
        self.product_type = 'BASE'
        self.category_name = "Angled Columns"
        self.assembly_name = "Base Angled Column Right"
        self.detail_piece = g_styles.base_column_styles
        self.orientation = 'RIGHT'
        self.detail_type = 'C'
        self.width = g.Default_Column_Width
        self.height = g.Base_Column_Height
        self.depth = g.Base_Column_Depth       

class PRODUCT_Tall_Angled_Column_Left(Angled_Column):
    
    def __init__(self):
        g = bpy.context.scene.lm_columns
        g_styles = bpy.context.scene.lm_cabinet_closet_designer
        self.product_type = 'TALL'
        self.category_name = "Angled Columns"
        self.assembly_name = "Tall Angled Column Left"
        self.detail_piece = g_styles.tall_column_styles
        self.orientation = 'LEFT'
        self.detail_type = 'C'
        self.width = g.Default_Column_Width
        self.height = g.Tall_Column_Height
        self.depth = g.Tall_Column_Depth
        
class PRODUCT_Tall_Angled_Column_Right(Angled_Column):
    
    def __init__(self):
        g = bpy.context.scene.lm_columns
        g_styles = bpy.context.scene.lm_cabinet_closet_designer
        self.product_type = 'TALL'
        self.category_name = "Angled Columns"
        self.assembly_name = "Tall Angled Column Right"
        self.detail_piece = g_styles.tall_column_styles
        self.orientation = 'RIGHT'
        self.detail_type = 'C'
        self.width = g.Default_Column_Width
        self.height = g.Tall_Column_Height
        self.depth = g.Tall_Column_Depth        
        
class PRODUCT_Upper_Angled_Column_Left(Angled_Column):
    
    def __init__(self):
        g = bpy.context.scene.lm_columns
        g_styles = bpy.context.scene.lm_cabinet_closet_designer
        self.product_type = 'UPPER'
        self.category_name = "Angled Columns"
        self.assembly_name = "Upper Angled Column Left"
        self.detail_piece = g_styles.upper_column_styles
        self.orientation = 'LEFT'
        self.detail_type = 'C'
        self.width = g.Default_Column_Width
        self.height = g.Upper_Column_Height
        self.depth = g.Upper_Column_Depth
        self.mirror_z = True
        self.height_above_floor = g.Height_Above_Floor
        
class PRODUCT_Upper_Angled_Column_Right(Angled_Column):
    
    def __init__(self):
        g = bpy.context.scene.lm_columns
        g_styles = bpy.context.scene.lm_cabinet_closet_designer
        self.product_type = 'UPPER'
        self.category_name = "Angled Columns"
        self.assembly_name = "Upper Angled Column Right"
        self.detail_piece = g_styles.upper_column_styles
        self.orientation = 'RIGHT'
        self.detail_type = 'C'
        self.width = g.Default_Column_Width
        self.height = g.Upper_Column_Height
        self.depth = g.Upper_Column_Depth
        self.mirror_z = True
        self.height_above_floor = g.Height_Above_Floor  
        
#---------USER INTERFACE

class PROMPTS_Column_Prompts(bpy.types.Operator):
    bl_idname = "cabnetlib.column_prompts"
    bl_label = "Column Prompts"
    bl_options = {'UNDO'}
    object_name = bpy.props.StringProperty(name="Object Name")

    width = bpy.props.FloatProperty(name="Width",unit='LENGTH',precision=4)
    height = bpy.props.FloatProperty(name="Height",unit='LENGTH',precision=4)
    depth = bpy.props.FloatProperty(name="Depth",unit='LENGTH',precision=4)

    product = None
    Left_End_Assembly = None
    Right_End_Assembly = None
    Standalone_Assembly = None
    Column_Detail_prompt = None
    
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

        self.product.obj_bp.location = self.product.obj_bp.location #refreshes drawing
        return True

    def execute(self, context):
        # This gets called when the OK button is clicked
        return {'FINISHED'}

    def invoke(self,context,event):
        # This gets called first and is used as an init call
        obj = context.scene.objects[self.object_name]
        obj_product_bp = fd.get_bp(obj,'PRODUCT')
        self.product = fd.Assembly(obj_product_bp)
        if self.product.obj_bp:
            self.depth = math.fabs(self.product.obj_y.location.y)
            self.height = math.fabs(self.product.obj_z.location.z)
            self.width = math.fabs(self.product.obj_x.location.x)
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=fd.get_prop_dialog_width(480))
    
    def draw_product_size(self,layout):
        box = layout.box()
        
        row = box.row()
        
        col = row.column(align=True)
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
            
        col = row.column(align=True)
        col.label("Location X:")
        col.label("Location Y:")
        col.label("Location Z:")
            
        col = row.column(align=True)
        col.prop(self.product.obj_bp,'location',text="")
        
        row = box.row()
        row.label('Rotation Z:')
        row.prop(self.product.obj_bp,'rotation_euler',index=2,text="")
            
    def object_has_driver(self,obj):
        if obj.animation_data:
            if len(obj.animation_data.drivers) > 0:
                return True

    def draw(self, context):
        layout = self.layout
        if self.product.obj_bp:
            if self.product.obj_bp.name in context.scene.objects:
                box = layout.box()

                split = box.split(percentage=.8)
                split.label(self.product.obj_bp.mv.name_object + " | " + self.product.obj_bp.cabinetlib.spec_group_name,icon='LATTICE_DATA')
                split.menu('MENU_Current_Cabinet_Menu',text="Menu",icon='DOWNARROW_HLT')

                Extend_Left_End = self.product.get_prompt("Extend Left End")
                Extend_Right_End = self.product.get_prompt("Extend Right End")
                Panel_Depth = self.product.get_prompt("Panel Depth")

                self.draw_product_size(box)
                col = box.column(align=True)
                col.label("Basic Column Options:")
                row = col.row()
                row.prop(Extend_Left_End,'CheckBoxValue',text="Extend Left End")
                row.prop(Extend_Right_End,'CheckBoxValue',text="Extend Right End")
                row = col.row()
                row.prop(Panel_Depth,'DistanceValue',text="Panel Depth")

class PROMPTS_Angled_Column_Prompts(bpy.types.Operator):
    bl_idname = "angled_columns.column_prompts"
    bl_label = "Angled Column Prompts"
    bl_options = {'UNDO'}
    object_name = bpy.props.StringProperty(name="Object Name")

    width = bpy.props.FloatProperty(name="Width",unit='LENGTH',precision=4)
    height = bpy.props.FloatProperty(name="Height",unit='LENGTH',precision=4)
    depth = bpy.props.FloatProperty(name="Depth",unit='LENGTH',precision=4)

    product = None
    Left_End_Assembly = None
    Right_End_Assembly = None
    Standalone_Assembly = None
    Column_Detail_prompt = None
    
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

        self.product.obj_bp.location = self.product.obj_bp.location #refreshes drawing
        return True

    def execute(self, context):
        # This gets called when the OK button is clicked
        return {'FINISHED'}

    def invoke(self,context,event):
        # This gets called first and is used as an init call
        obj = context.scene.objects[self.object_name]
        obj_product_bp = fd.get_bp(obj,'PRODUCT')
        self.product = fd.Assembly(obj_product_bp)
        if self.product.obj_bp:
            self.depth = math.fabs(self.product.obj_y.location.y)
            self.height = math.fabs(self.product.obj_z.location.z)
            self.width = math.fabs(self.product.obj_x.location.x)
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=fd.get_prop_dialog_width(480))
    
    def draw_product_size(self,layout):
        box = layout.box()
        
        row = box.row()
        
        col = row.column(align=True)
#         row1 = col.row(align=True)
#         if self.object_has_driver(self.product.obj_x):
#             row1.label('Width: ' + str(fd.unit(math.fabs(self.product.obj_x.location.x))))
#         else:
#             row1.label('Width:')
#             row1.prop(self,'width',text="")
#             row1.prop(self.product.obj_x,'hide',text="")
        
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
            
        col = row.column(align=True)
        col.label("Location X:")
        col.label("Location Y:")
        col.label("Location Z:")
            
        col = row.column(align=True)
        col.prop(self.product.obj_bp,'location',text="")
        
        row = box.row()
        row.label('Rotation Z:')
        row.prop(self.product.obj_bp,'rotation_euler',index=2,text="")
            
    def object_has_driver(self,obj):
        if obj.animation_data:
            if len(obj.animation_data.drivers) > 0:
                return True

    def draw(self, context):
        layout = self.layout
        if self.product.obj_bp:
            if self.product.obj_bp.name in context.scene.objects:
                box = layout.box()

                split = box.split(percentage=.8)
                split.label(self.product.obj_bp.mv.name_object + " | " + self.product.obj_bp.cabinetlib.spec_group_name,icon='LATTICE_DATA')
                split.menu('MENU_Current_Cabinet_Menu',text="Menu",icon='DOWNARROW_HLT')

                self.draw_product_size(box)
#                 col = box.column(align=True)
#                 col.label("Basic Column Options:")
#                 row = col.row()
                
class PROPERTIES_Scene_Variables(bpy.types.PropertyGroup):
    
    Default_Column_Width = bpy.props.FloatProperty(name="Default Column Width",
                                         description="Default width for columns",
                                         default=fd.inches(4),
                                         unit='LENGTH')
    
    Base_Column_Depth = bpy.props.FloatProperty(name="Base Column Depth",
                                      description="Default depth for base columns",
                                      default=fd.inches(23.0),
                                      unit='LENGTH')
    
    Tall_Column_Depth = bpy.props.FloatProperty(name="Tall Column Depth",
                                      description="Default depth for tall columns",
                                      default=fd.inches(25.0),
                                      unit='LENGTH')
    
    Upper_Column_Depth = bpy.props.FloatProperty(name="Upper Column Depth",
                                       description="Default depth for upper columns",
                                       default=fd.inches(12.0),
                                       unit='LENGTH')
    
    Base_Column_Height = bpy.props.FloatProperty(name="Base Column Height",
                                       description="Default height for base columns",
                                       default=fd.inches(34.0),
                                       unit='LENGTH')
    
    Tall_Column_Height = bpy.props.FloatProperty(name="Tall Column Height",
                                       description="Default height for tall columns",
                                       default=fd.inches(84.0),
                                       unit='LENGTH')
    
    Upper_Column_Height = bpy.props.FloatProperty(name="Upper Column Height",
                                        description="Default height for upper columns",
                                        default=fd.inches(34.0),
                                        unit='LENGTH')
    
    Height_Above_Floor = bpy.props.FloatProperty(name="Height Above Floor",
                                       description="Default height above floor for upper cabinets",
                                       default=fd.inches(84.0),
                                       unit='LENGTH')
    
    def draw(self,layout):
        box = layout.box()
        box.prop(self,'Default_Column_Width')
        col = box.column(align=True)
        col.prop(self,"Base_Column_Depth")
        col.prop(self,"Base_Column_Height")
        col = box.column(align=True)
        col.prop(self,"Tall_Column_Depth")
        col.prop(self,"Tall_Column_Height")
        col = box.column(align=True)
        col.prop(self,"Upper_Column_Depth")
        col.prop(self,"Upper_Column_Height")
        col.prop(self,"Height_Above_Floor")
                
def register():
    bpy.utils.register_class(PROPERTIES_Scene_Variables)
    bpy.types.Scene.lm_columns = bpy.props.PointerProperty(type = PROPERTIES_Scene_Variables)
    bpy.utils.register_class(PROMPTS_Column_Prompts)
    bpy.utils.register_class(PROMPTS_Angled_Column_Prompts)
    
def unregister():
    bpy.utils.unregister_class(PROPERTIES_Scene_Variables)
    bpy.utils.unregister_class(PROMPTS_Column_Prompts)
    bpy.utils.unregister_class(PROMPTS_Angled_Column_Prompts)
    