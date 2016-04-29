"""
Microvellum 
Cabinets
Stores the logic for the different types of cabinets available in the Face Frame and 
Frameless library. Only controls how the different inserts are combined to assemble a cabinet.
No construction or machining information is stored here.
TODO: Create Face Frame Transition, Create Face Frame Outside Corner
"""

import bpy
import fd
import math

HIDDEN_FOLDER_NAME = "_HIDDEN"

EXPOSED_CABINET_MATERIAL = ("Plastics","White Melamine")
UNEXPOSED_CABINET_MATERIAL = ("Wood","Wood Core","Particle Board")
SEMI_EXPOSED_CABINET_MATERIAL = ("Plastics","White Melamine")

MICROWAVE = (HIDDEN_FOLDER_NAME,"Appliances Assemblies","Microwaves","Conventional Microwave")
VENT = (HIDDEN_FOLDER_NAME,"Appliances Assemblies","Range Hoods","Wall Mounted Range Hood 01")
BLIND_PANEL = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Cut Parts","Part with Edgebanding")
FACE_FRAME = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Face Frames","Face Frame")
MID_RAIL = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Cut Parts","Part with Edgebanding")

class Material_Pointers():
    
    Exposed_Exterior_Surface = fd.Material_Pointer(EXPOSED_CABINET_MATERIAL)

    Semi_Exposed_Surface = fd.Material_Pointer(SEMI_EXPOSED_CABINET_MATERIAL)
    
    Exposed_Exterior_Edge = fd.Material_Pointer(EXPOSED_CABINET_MATERIAL)

    Concealed_Edge = fd.Material_Pointer(UNEXPOSED_CABINET_MATERIAL)

class Cutpart_Pointers():
    
    Blind_Panel = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                  core="Concealed_Surface",
                                  top="Semi_Exposed_Surface",
                                  bottom="Exposed_Exterior_Surface")

class Frameless_Standard(fd.Library_Assembly):
    """ Standard Frameless Cabinet
    """

    property_id = "cabinetlib.frameless_cabinet_prompts"
    type_assembly = "PRODUCT"

    """ Type:fd.Library_Assembly - The main carcass used """
    carcass = None
    
    """ Type:fd.Library_Assembly - Splitter insert to add to the cabinet """
    splitter = None
    
    """ Type:fd.Library_Assembly - Interior insert to add to the cabinet """
    interior = None
    
    """ Type:fd.Library_Assembly - Exterior insert to add to the cabinet """
    exterior = None
    
    """ Type:bool - This adds an empty opening to the carcass for starter products """
    add_empty_opening = False
    
    """ Type:bool - This adds a microwave below the cabinet. 
                        This is typically only used for upper cabinets """
    add_microwave = False
    
    """ Type:bool - This adds a vent below the cabinet. 
                        This is typically only used for upper cabinets """
    add_vent_hood = False
    
    def set_drivers_for_assembly(self,assembly):
        Width = self.carcass.get_var("dim_x",'Width')
        Height = self.carcass.get_var("dim_z",'Height')
        Depth = self.carcass.get_var("dim_y",'Depth')
        Left_Side_Thickness = self.carcass.get_var("Left Side Thickness")
        Right_Side_Thickness = self.carcass.get_var("Right Side Thickness")
        Top_Thickness = self.carcass.get_var("Top Thickness")
        Bottom_Thickness = self.carcass.get_var("Bottom Thickness")
        Top_Inset = self.carcass.get_var("Top Inset")
        Bottom_Inset = self.carcass.get_var("Bottom Inset")
        Back_Inset = self.carcass.get_var("Back Inset")
        
        assembly.x_loc('Left_Side_Thickness',[Left_Side_Thickness])
        assembly.y_loc('Depth',[Depth])
        if self.carcass.carcass_type in {"Base","Tall","Sink"}:
            assembly.z_loc('Bottom_Inset',[Bottom_Inset])
        if self.carcass.carcass_type in {"Upper","Suspended"}:
            self.mirror_z = True
            assembly.z_loc('Height+Bottom_Inset',[Height,Bottom_Inset])
        assembly.x_rot(value = 0)
        assembly.y_rot(value = 0)
        assembly.z_rot(value = 0)
        assembly.x_dim('Width-(Left_Side_Thickness+Right_Side_Thickness)',[Width,Left_Side_Thickness,Right_Side_Thickness])
        assembly.y_dim('fabs(Depth)-Back_Inset',[Depth,Back_Inset])
        assembly.z_dim('fabs(Height)-Bottom_Inset-Top_Inset',[Height,Bottom_Inset,Top_Inset])
        
        # ALLOW DOOR TO EXTEND TO TOP FOR VALANCE
        extend_top_amount = assembly.get_prompt("Extend Top Amount")
        valance_height_top = self.carcass.get_prompt("Valance Height Top")

        if extend_top_amount and valance_height_top:
            Valance_Height_Top = self.carcass.get_var("Valance Height Top")
            Door_Valance_Top = self.carcass.get_var("Door Valance Top")
            Top_Reveal = assembly.get_var("Top Reveal")
            
            assembly.prompt('Extend Top Amount','IF(AND(Door_Valance_Top,Valance_Height_Top>0),Valance_Height_Top+Top_Thickness-Top_Reveal,0)',[Valance_Height_Top,Door_Valance_Top,Top_Thickness,Top_Reveal])
            
        # ALLOW DOOR TO EXTEND TO BOTTOM FOR VALANCE
        extend_bottom_amount = assembly.get_prompt("Extend Bottom Amount")
        valance_height_bottom = self.carcass.get_prompt("Valance Height Bottom")
        
        if extend_bottom_amount and valance_height_bottom:
            Valance_Height_Bottom = self.carcass.get_var("Valance Height Bottom")
            Door_Valance_Bottom = self.carcass.get_var("Door Valance Bottom")
            Bottom_Reveal = assembly.get_var("Bottom Reveal")
            
            assembly.prompt('Extend Bottom Amount','IF(AND(Door_Valance_Bottom,Valance_Height_Bottom>0),Valance_Height_Bottom+Bottom_Thickness-Bottom_Reveal,0)',[Valance_Height_Bottom,Door_Valance_Bottom,Bottom_Thickness,Bottom_Reveal])
        
        # ALLOR DOOR TO EXTEND WHEN SUB FRONT IS FOUND
        sub_front_height = self.carcass.get_prompt("Sub Front Height")
        
        if extend_bottom_amount and sub_front_height:
            Sub_Front_Height = self.carcass.get_var("Sub Front Height")
            Top_Reveal = assembly.get_var("Top Reveal")
            
            assembly.prompt('Extend Top Amount','Sub_Front_Height-Top_Reveal',[Sub_Front_Height,Top_Reveal])
        
    def draw(self):
        self.create_assembly()
        
        Product_Width = self.get_var('dim_x','Product_Width')
        Product_Height = self.get_var('dim_z','Product_Height')
        Product_Depth = self.get_var('dim_y','Product_Depth')
        
        self.carcass.draw()
        self.carcass.obj_bp.parent = self.obj_bp
        self.carcass.x_loc(value = 0)
        self.carcass.y_loc(value = 0)
        self.carcass.z_loc(value = 0)
        self.carcass.x_rot(value = 0)
        self.carcass.y_rot(value = 0)
        self.carcass.z_rot(value = 0)
        self.carcass.x_dim('Product_Width',[Product_Width])
        self.carcass.y_dim('Product_Depth',[Product_Depth])
        self.carcass.z_dim('Product_Height',[Product_Height])

        vdim_x = fd.Dimension()
        vdim_x.parent(self.obj_bp)
        if self.mirror_z:
            vdim_x.start_z(value = fd.inches(5))
        else:
            vdim_x.start_z(value = -fd.inches(5))
        if self.carcass.carcass_type == 'Upper':
            vdim_x.start_y(value = fd.inches(8))
        else:
            vdim_x.start_y(value = fd.inches(3))
        vdim_x.end_x('Product_Width',[Product_Width])
        
        if self.splitter:
            self.splitter.draw()
            self.splitter.obj_bp.parent = self.obj_bp
            self.set_drivers_for_assembly(self.splitter)
            
        if self.interior:
            self.interior.draw()
            self.interior.obj_bp.parent = self.obj_bp
            self.set_drivers_for_assembly(self.interior)

        if self.exterior:
            self.exterior.draw()
            self.exterior.obj_bp.parent = self.obj_bp
            self.set_drivers_for_assembly(self.exterior)

        if self.add_empty_opening:
            opening = self.add_opening()
            opening.add_tab(name='Material Thickness',tab_type='HIDDEN')
            opening.add_prompt(name="Left Side Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
            opening.add_prompt(name="Right Side Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
            opening.add_prompt(name="Top Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
            opening.add_prompt(name="Bottom Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
            opening.add_prompt(name="Extend Top Amount",prompt_type='DISTANCE',value=fd.inches(0),tab_index=0)
            opening.add_prompt(name="Extend Bottom Amount",prompt_type='DISTANCE',value=fd.inches(0),tab_index=0)
            self.set_drivers_for_assembly(opening)
            
        if self.add_vent_hood:
            self.add_prompt(name="Vent Height",prompt_type='DISTANCE',value= fd.inches(14),tab_index=0,export=False)
            Vent_Height = self.get_var('Vent Height')
            vent = self.add_assembly(VENT)
            vent.set_name("Vent")
            vent.x_loc(value = 0)
            vent.y_loc(value = 0)
            vent.z_loc('Product_Height-Vent_Height',[Product_Height,Vent_Height])
            vent.x_dim('Product_Width',[Product_Width])
            vent.y_dim('Product_Depth',[Product_Depth])
            vent.z_dim('Vent_Height',[Vent_Height])
            
        if self.add_microwave:
            vent = self.add_assembly(MICROWAVE)
            vent.set_name("Microwave")
            vent.x_loc(value = 0)
            vent.y_loc(value = 0)
            vent.z_loc('Product_Height',[Product_Height])
            vent.x_dim('Product_Width',[Product_Width])
            vent.y_dim('Product_Depth',[Product_Depth])
            
        self.update()
        
class Frameless_Transition(fd.Library_Assembly):
    
    library_name = "Cabinets - Frameless"
    property_id = "cabinetlib.frameless_cabinet_prompts"
    type_assembly = "PRODUCT"
    product_shape = 'TRANSITION'
    
    carcass = None
    interior = None
    exterior = None
    
    def set_drivers_for_assembly(self,assembly):
        Width = self.carcass.get_var("dim_x",'Width')
        Height = self.carcass.get_var("dim_z",'Height')
        Depth = self.carcass.get_var("dim_y",'Depth')
        Left_Side_Thickness = self.carcass.get_var("Left Side Thickness")
        Right_Side_Thickness = self.carcass.get_var("Right Side Thickness")
        Top_Inset = self.carcass.get_var("Top Inset")
        Bottom_Inset = self.carcass.get_var("Bottom Inset")
        Back_Inset = self.carcass.get_var("Back Inset")
        
        assembly.x_loc('Left_Side_Thickness',[Left_Side_Thickness])
        assembly.y_loc('Depth',[Depth])
        if self.carcass.carcass_type in {"Base","Tall","Sink"}:
            assembly.z_loc('Bottom_Inset',[Bottom_Inset])
        if self.carcass.carcass_type in {"Upper","Suspended"}:
            self.mirror_z = True
            assembly.z_loc('Height+Bottom_Inset',[Height,Bottom_Inset])
        assembly.x_rot(value = 0)
        assembly.y_rot(value = 0)
        assembly.z_rot(value = 0)
        assembly.x_dim('Width-(Left_Side_Thickness+Right_Side_Thickness)',[Width,Left_Side_Thickness,Right_Side_Thickness])
        assembly.y_dim('fabs(Depth)-Back_Inset',[Depth,Back_Inset])
        assembly.z_dim('fabs(Height)-Bottom_Inset-Top_Inset',[Height,Bottom_Inset,Top_Inset])
        
    def add_doors(self):
        Width = self.carcass.get_var("dim_x",'Width')
        Height = self.carcass.get_var("dim_z",'Height')
        Depth = self.carcass.get_var("dim_y",'Depth')
        Top_Inset = self.carcass.get_var("Top Inset")
        Bottom_Inset = self.carcass.get_var("Bottom Inset")
        Cabinet_Depth_Left = self.carcass.get_var("Cabinet Depth Left")
        Cabinet_Depth_Right = self.carcass.get_var("Cabinet Depth Right")
        Left_Side_Thickness = self.carcass.get_var("Left Side Thickness")
        Right_Side_Thickness = self.carcass.get_var("Right Side Thickness")
        
        self.exterior.draw()
        self.exterior.obj_bp.parent = self.obj_bp
        self.exterior.x_loc('Left_Side_Thickness',[Left_Side_Thickness])
        self.exterior.y_loc('-Cabinet_Depth_Left',[Cabinet_Depth_Left])
        if self.carcass.carcass_type in {"Base","Tall"}:
            self.exterior.z_loc('Bottom_Inset',[Bottom_Inset])
        if self.carcass.carcass_type == "Upper":
            self.exterior.z_loc('Height+Bottom_Inset',[Height,Bottom_Inset])
        self.exterior.x_rot(value = 0)
        self.exterior.y_rot(value = 0)
        self.exterior.z_rot('atan((Cabinet_Depth_Left-Cabinet_Depth_Right)/(Width-Left_Side_Thickness-Right_Side_Thickness))',
                            [Left_Side_Thickness,Cabinet_Depth_Right,Width,Right_Side_Thickness,Cabinet_Depth_Left])
        self.exterior.x_dim('sqrt(((Cabinet_Depth_Left-Cabinet_Depth_Right)**2)+((Width-Left_Side_Thickness-Right_Side_Thickness)**2))',
                            [Left_Side_Thickness,Cabinet_Depth_Right,Width,Right_Side_Thickness,Cabinet_Depth_Left])
        self.exterior.y_dim('Depth+Cabinet_Depth_Right+Right_Side_Thickness',[Depth,Cabinet_Depth_Right,Right_Side_Thickness])
        self.exterior.z_dim('fabs(Height)-Bottom_Inset-Top_Inset',[Height,Bottom_Inset,Top_Inset])
        
    def draw(self):
        self.create_assembly()

        Product_Width = self.get_var('dim_x','Product_Width')
        Product_Height = self.get_var('dim_z','Product_Height')
        Product_Depth = self.get_var('dim_y','Product_Depth')
        
        self.carcass.draw()
        self.carcass.obj_bp.parent = self.obj_bp
        self.carcass.x_loc(value = 0)
        self.carcass.y_loc(value = 0)
        self.carcass.z_loc(value = 0)
        self.carcass.x_rot(value = 0)
        self.carcass.y_rot(value = 0)
        self.carcass.z_rot(value = 0)
        self.carcass.x_dim('Product_Width',[Product_Width])
        self.carcass.y_dim('Product_Depth',[Product_Depth])
        self.carcass.z_dim('Product_Height',[Product_Height])
        
        if self.exterior:
            self.add_doors()

        self.update()
        
class Frameless_Inside_Corner(fd.Library_Assembly):
    
    library_name = "Cabinets - Frameless"
    property_id = "cabinetlib.frameless_cabinet_prompts"
    type_assembly = "PRODUCT"
    placement_type = "Corner"

    carcass = None
    interior = None
    exterior = None
    
    def set_drivers_for_assembly(self,assembly):
        Width = self.carcass.get_var("dim_x",'Width')
        Height = self.carcass.get_var("dim_z",'Height')
        Depth = self.carcass.get_var("dim_y",'Depth')
        Left_Side_Thickness = self.carcass.get_var("Left Side Thickness")
        Right_Side_Thickness = self.carcass.get_var("Right Side Thickness")
        Top_Inset = self.carcass.get_var("Top Inset")
        Bottom_Inset = self.carcass.get_var("Bottom Inset")
        Back_Inset = self.carcass.get_var("Back Inset")
        
        assembly.x_loc('Left_Side_Thickness',[Left_Side_Thickness])
        assembly.y_loc('Depth',[Depth])
        if self.carcass.carcass_type in {"Base","Tall","Sink"}:
            assembly.z_loc('Bottom_Inset',[Bottom_Inset])
        if self.carcass.carcass_type in {"Upper","Suspended"}:
            self.mirror_z = True
            assembly.z_loc('Height+Bottom_Inset',[Height,Bottom_Inset])
        assembly.x_rot(value = 0)
        assembly.y_rot(value = 0)
        assembly.z_rot(value = 0)
        assembly.x_dim('Width-(Left_Side_Thickness+Right_Side_Thickness)',[Width,Left_Side_Thickness,Right_Side_Thickness])
        assembly.y_dim('fabs(Depth)-Back_Inset',[Depth,Back_Inset])
        assembly.z_dim('fabs(Height)-Bottom_Inset-Top_Inset',[Height,Bottom_Inset,Top_Inset])
        
    def add_pie_cut_doors(self):
        Width = self.carcass.get_var("dim_x",'Width')
        Height = self.carcass.get_var("dim_z",'Height')
        Depth = self.carcass.get_var("dim_y",'Depth')
        Top_Inset = self.carcass.get_var("Top Inset")
        Bottom_Inset = self.carcass.get_var("Bottom Inset")
        Cabinet_Depth_Left = self.carcass.get_var("Cabinet Depth Left")
        Cabinet_Depth_Right = self.carcass.get_var("Cabinet Depth Right")
        Left_Side_Thickness = self.carcass.get_var("Left Side Thickness")
        Right_Side_Thickness = self.carcass.get_var("Right Side Thickness")
        
        self.exterior.draw()
        self.exterior.obj_bp.parent = self.obj_bp
        self.exterior.x_loc('Cabinet_Depth_Left',[Cabinet_Depth_Left])
        self.exterior.y_loc('-Cabinet_Depth_Right',[Cabinet_Depth_Right])
        if self.carcass.carcass_type == "Base":
            self.exterior.z_loc('Bottom_Inset',[Bottom_Inset])
        if self.carcass.carcass_type == "Upper":
            self.exterior.z_loc('Height+Bottom_Inset',[Height,Bottom_Inset])
        self.exterior.x_rot(value = 0)
        self.exterior.y_rot(value = 0)
        self.exterior.z_rot(value = 0)
        self.exterior.x_dim('Width-Cabinet_Depth_Left-Left_Side_Thickness',[Width,Cabinet_Depth_Left,Left_Side_Thickness])
        self.exterior.y_dim('Depth+Cabinet_Depth_Right+Right_Side_Thickness',[Depth,Cabinet_Depth_Right,Right_Side_Thickness])
        self.exterior.z_dim('fabs(Height)-Bottom_Inset-Top_Inset',[Height,Bottom_Inset,Top_Inset])
        
    def add_diagonal_doors(self):
        Width = self.carcass.get_var("dim_x",'Width')
        Height = self.carcass.get_var("dim_z",'Height')
        Depth = self.carcass.get_var("dim_y",'Depth')
        Top_Inset = self.carcass.get_var("Top Inset")
        Bottom_Inset = self.carcass.get_var("Bottom Inset")
        Cabinet_Depth_Left = self.carcass.get_var("Cabinet Depth Left")
        Cabinet_Depth_Right = self.carcass.get_var("Cabinet Depth Right")
        Left_Side_Thickness = self.carcass.get_var("Left Side Thickness")
        Right_Side_Thickness = self.carcass.get_var("Right Side Thickness")
        
        self.exterior.draw()
        self.exterior.obj_bp.parent = self.obj_bp
        self.exterior.x_loc('Cabinet_Depth_Left',[Cabinet_Depth_Left])
        self.exterior.y_loc('Depth+Left_Side_Thickness',[Depth,Left_Side_Thickness])
        if self.carcass.carcass_type == "Base":
            self.exterior.z_loc('Bottom_Inset',[Bottom_Inset])
        if self.carcass.carcass_type == "Upper":
            self.exterior.z_loc('Height+Bottom_Inset',[Height,Bottom_Inset])
        self.exterior.x_rot(value = 0)
        self.exterior.y_rot(value = 0)
        self.exterior.z_rot('atan((fabs(Depth)-Left_Side_Thickness-Cabinet_Depth_Right)/(fabs(Width)-Right_Side_Thickness-Cabinet_Depth_Left))',[Depth,Left_Side_Thickness,Cabinet_Depth_Right,Width,Right_Side_Thickness,Cabinet_Depth_Left])
        self.exterior.x_dim('sqrt(((fabs(Depth)-Left_Side_Thickness-Cabinet_Depth_Right)**2)+((fabs(Width)-Right_Side_Thickness-Cabinet_Depth_Left)**2))',[Depth,Left_Side_Thickness,Cabinet_Depth_Right,Width,Right_Side_Thickness,Cabinet_Depth_Left])
        self.exterior.y_dim('Depth+Cabinet_Depth_Right+Right_Side_Thickness',[Depth,Cabinet_Depth_Right,Right_Side_Thickness])
        self.exterior.z_dim('fabs(Height)-Bottom_Inset-Top_Inset',[Height,Bottom_Inset,Top_Inset])
        
    def draw(self):
        self.create_assembly()

        Product_Width = self.get_var('dim_x','Product_Width')
        Product_Height = self.get_var('dim_z','Product_Height')
        Product_Depth = self.get_var('dim_y','Product_Depth')
        
        self.carcass.draw()
        self.carcass.obj_bp.parent = self.obj_bp
        self.carcass.x_loc(value = 0)
        self.carcass.y_loc(value = 0)
        self.carcass.z_loc(value = 0)
        self.carcass.x_rot(value = 0)
        self.carcass.y_rot(value = 0)
        self.carcass.z_rot(value = 0)
        self.carcass.x_dim('Product_Width',[Product_Width])
        self.carcass.y_dim('Product_Depth',[Product_Depth])
        self.carcass.z_dim('Product_Height',[Product_Height])
        
        if self.carcass.carcass_shape == 'Notched':
            self.product_shape = 'INSIDE_NOTCH'
            if self.exterior:
                self.add_pie_cut_doors()
        
        if self.carcass.carcass_shape == 'Diagonal':
            self.product_shape = 'INSIDE_DIAGONAL'
            if self.exterior:
                self.add_diagonal_doors()

        self.update()
        
class Frameless_Outside_Corner(fd.Library_Assembly):
    
    library_name = "Cabinets - Frameless"
    property_id = "cabinetlib.frameless_cabinet_prompts"
    type_assembly = "PRODUCT"
    placement_type = "Corner"

    carcass = None
    interior = None
    exterior = None
    
    def draw(self):
        self.create_assembly()

        Product_Height = self.get_var('dim_z','Product_Height')
        Product_Depth = self.get_var('dim_y','Product_Depth')
        
        self.carcass.draw()
        self.carcass.obj_bp.parent = self.obj_bp
        self.carcass.x_loc(value = 0)
        self.carcass.y_loc(value = 0)
        self.carcass.z_loc(value = 0)
        self.carcass.x_rot(value = 0)
        self.carcass.y_rot(value = 0)
        self.carcass.z_rot(value = 0)
        self.carcass.x_dim('fabs(Product_Depth)',[Product_Depth])
        self.carcass.y_dim('Product_Depth',[Product_Depth])
        self.carcass.z_dim('Product_Height',[Product_Height])
        
        if self.carcass.carcass_shape == 'Notched':
            self.product_shape = 'OUTSIDE_NOTCH'
            if self.exterior:
                pass #TODO
        
        if self.carcass.carcass_shape == 'Diagonal':
            self.product_shape = 'OUTSIDE_DIAGONAL'
            if self.exterior:
                pass #TODO
        
        self.update()
        
class Frameless_Blind_Corner(fd.Library_Assembly):
    
    library_name = "Cabinets - Frameless"
    property_id = "cabinetlib.frameless_cabinet_prompts"
    type_assembly = "PRODUCT"
    product_shape = "RECTANGLE"
    
    blind_side = "Left" # {Left, Right}
    
    carcass = None
    splitter = None
    interior = None
    exterior = None
    
    def draw(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.create_assembly()
        
        self.carcass.draw()
        self.carcass.obj_bp.parent = self.obj_bp

        self.add_tab(name='Blind Corner Options',tab_type='VISIBLE')
        self.add_tab(name='Formulas',tab_type='HIDDEN')
        if self.carcass.carcass_type == 'Base':
            self.add_prompt(name="Blind Panel Width",prompt_type='DISTANCE',value=g.Base_Cabinet_Depth,tab_index=0)
        if self.carcass.carcass_type == 'Tall':
            self.add_prompt(name="Blind Panel Width",prompt_type='DISTANCE',value=g.Tall_Cabinet_Depth,tab_index=0)
        if self.carcass.carcass_type == 'Upper':
            self.mirror_z = True
            self.add_prompt(name="Blind Panel Width",prompt_type='DISTANCE',value=g.Upper_Cabinet_Depth,tab_index=0)
        self.add_prompt(name="Blind Panel Reveal",prompt_type='DISTANCE',value=g.Blind_Panel_Reveal,tab_index=0)
        self.add_prompt(name="Inset Blind Panel",prompt_type='CHECKBOX',value=g.Inset_Blind_Panel,tab_index=0)
        self.add_prompt(name="Blind Panel Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        
        Product_Width = self.get_var('dim_x','Product_Width')
        Product_Height = self.get_var('dim_z','Product_Height')
        Product_Depth = self.get_var('dim_y','Product_Depth')
        Blind_Panel_Width = self.get_var('Blind Panel Width')
        Blind_Panel_Reveal = self.get_var('Blind Panel Reveal')
        Inset_Blind_Panel = self.get_var('Inset Blind Panel')
        Blind_Panel_Thickness = self.get_var('Blind Panel Thickness')
        Carcass_Width = self.carcass.get_var("dim_x",'Carcass_Width')
        Carcass_Depth = self.carcass.get_var("dim_y",'Carcass_Depth')
        Carcass_Height = self.carcass.get_var("dim_z",'Carcass_Height')
        Toe_Kick_Height = self.carcass.get_var("Toe Kick Height")
        Top_Thickness = self.carcass.get_var("Top Thickness")
        Bottom_Thickness = self.carcass.get_var("Bottom Thickness")
        Right_Side_Thickness = self.carcass.get_var("Right Side Thickness")
        Left_Side_Thickness = self.carcass.get_var("Left Side Thickness")
        Top_Inset = self.carcass.get_var("Top Inset",'Top_Inset')
        Bottom_Inset = self.carcass.get_var("Bottom Inset",'Bottom_Inset')
        Back_Inset = self.carcass.get_var("Back Inset",'Back_Inset')
        
        self.carcass.x_loc(value = 0)
        self.carcass.y_loc(value = 0)
        self.carcass.z_loc(value = 0)
        self.carcass.x_rot(value = 0)
        self.carcass.y_rot(value = 0)
        self.carcass.z_rot(value = 0)
        self.carcass.x_dim('Product_Width',[Product_Width])
        self.carcass.y_dim('Product_Depth',[Product_Depth])
        self.carcass.z_dim('Product_Height',[Product_Height])
        
        blind_panel = self.add_assembly(BLIND_PANEL)
        blind_panel.obj_bp.mv.name_object = "Blind Panel"
        if self.blind_side == "Left":
            blind_panel.x_loc('IF(Inset_Blind_Panel,Left_Side_Thickness,0)',[Inset_Blind_Panel,Left_Side_Thickness])
            blind_panel.y_dim('(Blind_Panel_Width+Blind_Panel_Reveal-IF(Inset_Blind_Panel,Left_Side_Thickness,0))*-1',[Blind_Panel_Width,Blind_Panel_Reveal,Inset_Blind_Panel,Left_Side_Thickness])
        if self.blind_side == "Right":
            blind_panel.x_loc('Carcass_Width-IF(Inset_Blind_Panel,Right_Side_Thickness,0)',[Carcass_Width,Inset_Blind_Panel,Right_Side_Thickness])
            blind_panel.y_dim('Blind_Panel_Width+Blind_Panel_Reveal-IF(Inset_Blind_Panel,Right_Side_Thickness,0)',[Blind_Panel_Width,Blind_Panel_Reveal,Right_Side_Thickness,Inset_Blind_Panel])
        blind_panel.y_loc('Carcass_Depth+IF(Inset_Blind_Panel,Blind_Panel_Thickness,0)',[Carcass_Depth,Inset_Blind_Panel,Blind_Panel_Thickness])
        if self.carcass.carcass_type in {"Base","Tall","Sink"}:
            blind_panel.z_loc('Toe_Kick_Height+IF(Inset_Blind_Panel,Bottom_Thickness,0)',[Toe_Kick_Height,Inset_Blind_Panel,Bottom_Thickness])
            blind_panel.x_dim('Carcass_Height-Toe_Kick_Height-IF(Inset_Blind_Panel,Top_Thickness+Bottom_Thickness,0)',[Carcass_Height,Toe_Kick_Height,Inset_Blind_Panel,Top_Thickness,Bottom_Thickness])
        if self.carcass.carcass_type in {"Upper","Suspended"}:
            blind_panel.z_loc('Carcass_Height+Bottom_Inset-IF(Inset_Blind_Panel,0,Bottom_Thickness)',[Carcass_Height,Bottom_Inset,Inset_Blind_Panel,Bottom_Thickness])
            blind_panel.x_dim('fabs(Carcass_Height)-Top_Inset-Bottom_Inset+IF(Inset_Blind_Panel,0,Top_Thickness+Bottom_Thickness)',[Carcass_Height,Top_Inset,Bottom_Inset,Inset_Blind_Panel,Top_Thickness,Bottom_Thickness])
        blind_panel.x_rot(value = 0)
        blind_panel.y_rot(value = -90)
        blind_panel.z_rot(value = 90)
        blind_panel.z_dim('Blind_Panel_Thickness',[Blind_Panel_Thickness])
        blind_panel.cutpart("Blind_Panel")
        
        if self.splitter:
            self.splitter.draw()
            self.splitter.obj_bp.parent = self.obj_bp
            if self.blind_side == "Left":
                self.splitter.x_loc('Blind_Panel_Width+Blind_Panel_Reveal',[Blind_Panel_Width,Blind_Panel_Reveal])
            if self.blind_side == "Right":
                self.splitter.x_loc('Left_Side_Thickness',[Left_Side_Thickness])
            self.splitter.y_loc('Carcass_Depth',[Carcass_Depth])
            if self.carcass.carcass_type in {"Base","Tall","Sink"}:
                self.splitter.z_loc('Bottom_Inset',[Bottom_Inset])
            if self.carcass.carcass_type in {"Upper","Suspended"}:
                self.splitter.z_loc('Carcass_Height+Bottom_Inset',[Carcass_Height,Bottom_Inset])
            self.splitter.x_rot(value = 0)
            self.splitter.y_rot(value = 0)
            self.splitter.z_rot(value = 0)
            if self.blind_side == "Left":
                self.splitter.x_dim('Carcass_Width-(Blind_Panel_Width+Blind_Panel_Reveal+Right_Side_Thickness)',[Carcass_Width,Blind_Panel_Width,Blind_Panel_Reveal,Right_Side_Thickness])
            else:
                self.splitter.x_dim('Carcass_Width-(Blind_Panel_Width+Blind_Panel_Reveal+Left_Side_Thickness)',[Carcass_Width,Blind_Panel_Width,Blind_Panel_Reveal,Left_Side_Thickness])
            self.splitter.y_dim('fabs(Carcass_Depth)-Back_Inset-IF(Inset_Blind_Panel,Blind_Panel_Thickness,0)',[Carcass_Depth,Back_Inset,Inset_Blind_Panel,Blind_Panel_Thickness])
            self.splitter.z_dim('fabs(Carcass_Height)-Bottom_Inset-Top_Inset',[Carcass_Height,Bottom_Inset,Top_Inset])
            
        if self.interior:
            self.interior.draw()
            self.interior.obj_bp.parent = self.obj_bp
            self.interior.x_loc('Left_Side_Thickness',[Left_Side_Thickness])
            self.interior.y_loc('Carcass_Depth+IF(Inset_Blind_Panel,Blind_Panel_Thickness,0)',[Carcass_Depth,Inset_Blind_Panel,Blind_Panel_Thickness])
            if self.carcass.carcass_type in {"Base","Tall","Sink"}:
                self.interior.z_loc('Bottom_Inset',[Bottom_Inset])
            if self.carcass.carcass_type in {"Upper","Suspended"}:
                self.interior.z_loc('Carcass_Height+Bottom_Inset',[Carcass_Height,Bottom_Inset])
            self.interior.x_rot(value = 0)
            self.interior.y_rot(value = 0)
            self.interior.z_rot(value = 0)
            self.interior.x_dim('Carcass_Width-(Left_Side_Thickness+Right_Side_Thickness)',[Carcass_Width,Left_Side_Thickness,Right_Side_Thickness])
            self.interior.y_dim('fabs(Carcass_Depth)-Back_Inset-IF(Inset_Blind_Panel,Blind_Panel_Thickness,0)',[Carcass_Depth,Back_Inset,Inset_Blind_Panel,Blind_Panel_Thickness])
            self.interior.z_dim('fabs(Carcass_Height)-Bottom_Inset-Top_Inset',[Carcass_Height,Bottom_Inset,Top_Inset])
            
        if self.exterior:
            self.exterior.draw()
            self.exterior.obj_bp.parent = self.obj_bp
            if self.blind_side == "Left":
                self.exterior.x_loc('Blind_Panel_Width+Blind_Panel_Reveal',[Blind_Panel_Width,Blind_Panel_Reveal])
            if self.blind_side == "Right":
                self.exterior.x_loc('Left_Side_Thickness',[Left_Side_Thickness])
            self.exterior.y_loc('Carcass_Depth',[Carcass_Depth])
            if self.carcass.carcass_type in {"Base","Tall","Sink"}:
                self.exterior.z_loc('Bottom_Inset',[Bottom_Inset])
            if self.carcass.carcass_type in {"Upper","Suspended"}:
                self.exterior.z_loc('Carcass_Height+Bottom_Inset',[Carcass_Height,Bottom_Inset])
            self.exterior.x_rot(value = 0)
            self.exterior.y_rot(value = 0)
            self.exterior.z_rot(value = 0)
            if self.blind_side == "Left":
                self.exterior.x_dim('Carcass_Width-(Blind_Panel_Width+Blind_Panel_Reveal+Right_Side_Thickness)',[Carcass_Width,Blind_Panel_Width,Blind_Panel_Reveal,Right_Side_Thickness])
            else:
                self.exterior.x_dim('Carcass_Width-(Blind_Panel_Width+Blind_Panel_Reveal+Left_Side_Thickness)',[Carcass_Width,Blind_Panel_Width,Blind_Panel_Reveal,Left_Side_Thickness])
            self.exterior.y_dim('fabs(Carcass_Depth)-Back_Inset-IF(Inset_Blind_Panel,Blind_Panel_Thickness,0)',[Carcass_Depth,Back_Inset,Inset_Blind_Panel,Blind_Panel_Thickness])
            self.exterior.z_dim('fabs(Carcass_Height)-Bottom_Inset-Top_Inset',[Carcass_Height,Bottom_Inset,Top_Inset])
            
        self.update()

class Face_Frame_Standard(fd.Library_Assembly):
    
    library_name = "Cabinets - Face Frame"
    property_id = "face_frame_cabients.cabinet_prompts"
    type_assembly = "PRODUCT"
    product_shape = "RECTANGLE"
    
    carcass = None
    splitter = None
    interior = None
    exterior = None
    
    add_empty_opening = False
    
    add_microwave = False
    add_vent_hood = False
    
    def set_drivers_for_assembly(self,assembly):
        Carcass_X = self.carcass.get_var("loc_x","Carcass_X")
        Left_Side_Thickness = self.carcass.get_var("Left Side Thickness")
        Right_Side_Thickness = self.carcass.get_var("Right Side Thickness")
        Top_Inset = self.carcass.get_var("Top Inset")
        Bottom_Inset = self.carcass.get_var("Bottom Inset")
        Back_Inset = self.carcass.get_var("Back Inset")
        Width = self.carcass.get_var("dim_x",'Width')
        Height = self.carcass.get_var("dim_z",'Height')
        Depth = self.carcass.get_var("dim_y",'Depth')
        
        assembly.x_loc('Carcass_X+Left_Side_Thickness',[Left_Side_Thickness,Carcass_X])
        assembly.y_loc('Depth',[Depth])
        if self.carcass.carcass_type in {"Base","Tall","Sink"}:
            assembly.z_loc('Bottom_Inset',[Bottom_Inset])
        if self.carcass.carcass_type in {"Upper","Suspended"}:
            self.mirror_z = True
            assembly.z_loc('Height+Bottom_Inset',[Height,Bottom_Inset])
        assembly.x_rot(value = 0)
        assembly.y_rot(value = 0)
        assembly.z_rot(value = 0)
        assembly.x_dim('Width-(Left_Side_Thickness+Right_Side_Thickness)',[Width,Left_Side_Thickness,Right_Side_Thickness])
        assembly.y_dim('fabs(Depth)-Back_Inset',[Depth,Back_Inset])
        assembly.z_dim('fabs(Height)-Bottom_Inset-Top_Inset',[Height,Bottom_Inset,Top_Inset])
        
    def draw(self):
        self.create_assembly()

        self.add_tab(name='Face Frame Options',tab_type='VISIBLE')
        self.add_tab(name='Formulas',tab_type='HIDDEN')
        self.add_prompt(name="Top Rail Width",prompt_type='DISTANCE',value=fd.inches(2),tab_index=0)
        self.add_prompt(name="Bottom Rail Width",prompt_type='DISTANCE',value=fd.inches(1.5),tab_index=0)
        self.add_prompt(name="Left Stile Width",prompt_type='DISTANCE',value=fd.inches(2),tab_index=0)
        self.add_prompt(name="Right Stile Width",prompt_type='DISTANCE',value=fd.inches(2),tab_index=0)
        
        self.carcass.draw()
        self.carcass.obj_bp.parent = self.obj_bp
        
        frame = self.add_assembly(FACE_FRAME)
        frame.set_name("Face Frame")
        
        Product_Width = self.get_var('dim_x','Product_Width')
        Product_Height = self.get_var('dim_z','Product_Height')
        Product_Depth = self.get_var('dim_y','Product_Depth')
        Top_Rail_Width = self.get_var("Top Rail Width")
        Bottom_Rail_Width = self.get_var("Bottom Rail Width")
        Left_Stile_Width = self.get_var("Left Stile Width")
        Right_Stile_Width = self.get_var("Right Stile Width")
        Frame_Thickness = frame.get_var("dim_y","Frame_Thickness")
        Left_Side_Thickness = self.carcass.get_var("Left Side Thickness")
        Right_Side_Thickness = self.carcass.get_var("Right Side Thickness")
        Top_Thickness = self.carcass.get_var("Top Thickness")
        Toe_Kick_Height = self.carcass.get_var("Toe Kick Height")
        Bottom_Thickness = self.carcass.get_var("Bottom Thickness")
        Left_Fin_End = self.carcass.get_var("Left Fin End")
        Right_Fin_End = self.carcass.get_var("Right Fin End")
        
        vdim_x = fd.Dimension()
        vdim_x.parent(self.obj_bp)
        if self.mirror_z:
            vdim_x.start_z(value = fd.inches(5))
        else:
            vdim_x.start_z(value = -fd.inches(5))
        if self.carcass.carcass_type == 'Upper':
            vdim_x.start_y(value = fd.inches(8))
        else:
            vdim_x.start_y(value = fd.inches(3))
        vdim_x.end_x('Product_Width',[Product_Width])
        
        self.carcass.x_loc('IF(Left_Fin_End,0,Left_Stile_Width-Left_Side_Thickness)',[Left_Fin_End,Left_Stile_Width,Left_Side_Thickness])
        self.carcass.y_loc(value = 0)
        self.carcass.z_loc(value = 0)
        self.carcass.x_rot(value = 0)
        self.carcass.y_rot(value = 0)
        self.carcass.z_rot(value = 0)
        self.carcass.x_dim('Product_Width-IF(Left_Fin_End,0,Left_Stile_Width-Left_Side_Thickness)-IF(Right_Fin_End,0,Right_Stile_Width-Right_Side_Thickness)',[Product_Width,Left_Fin_End,Right_Fin_End,Left_Stile_Width,Left_Side_Thickness,Right_Stile_Width,Right_Side_Thickness])
        self.carcass.y_dim('Product_Depth',[Product_Depth])
        self.carcass.z_dim('Product_Height',[Product_Height])
        
        frame.x_loc(value = 0)
        frame.y_loc('Product_Depth',[Product_Depth])
        if self.carcass.carcass_type in {"Base","Tall","Sink"}:
            frame.z_loc('Toe_Kick_Height-Bottom_Rail_Width+Bottom_Thickness',[Toe_Kick_Height,Bottom_Rail_Width,Bottom_Thickness])
        if self.carcass.carcass_type in {"Upper","Suspended"}:
            frame.z_loc('Product_Height-Bottom_Rail_Width+Bottom_Thickness',[Product_Height,Bottom_Rail_Width,Bottom_Thickness])
        frame.x_rot(value = 0)
        frame.y_rot(value = 0)
        frame.z_rot(value = 0)
        frame.x_dim('Product_Width',[Product_Width])
        frame.y_dim(value = fd.inches(-.75))
        if self.carcass.carcass_type in {"Base","Tall","Sink"}:
            frame.z_dim('Product_Height-Toe_Kick_Height+(Bottom_Rail_Width-Bottom_Thickness)',[Product_Height,Toe_Kick_Height,Bottom_Rail_Width,Bottom_Thickness])
        if self.carcass.carcass_type in {"Upper","Suspended"}:
            frame.z_dim('fabs(Product_Height)+(Bottom_Rail_Width-Bottom_Thickness)',[Product_Height,Bottom_Rail_Width,Bottom_Thickness])
        frame.prompt("Top Rail Width",'Top_Rail_Width',[Top_Rail_Width])
        frame.prompt("Bottom Rail Width",'Bottom_Rail_Width',[Bottom_Rail_Width])
        frame.prompt("Left Stile Width",'Left_Stile_Width',[Left_Stile_Width])
        frame.prompt("Right Stile Width",'Right_Stile_Width',[Right_Stile_Width])
        frame.material("Exposed_Exterior_Surface")
        
        if self.interior:
            self.interior.draw()
            self.interior.obj_bp.parent = self.obj_bp
            self.set_drivers_for_assembly(self.interior)

        if self.exterior:
            self.exterior.draw()
            self.exterior.obj_bp.parent = self.obj_bp
            self.set_drivers_for_assembly(self.exterior)
            self.exterior.prompt("Frame Thickness","fabs(Frame_Thickness)",[Frame_Thickness])
            self.exterior.prompt("Frame Left Gap","IF(Left_Fin_End,Left_Stile_Width-Left_Side_Thickness,0)",[Left_Fin_End,Left_Stile_Width,Left_Side_Thickness])
            self.exterior.prompt("Frame Right Gap","IF(Right_Fin_End,Right_Stile_Width-Right_Side_Thickness,0)",[Right_Fin_End,Right_Stile_Width,Right_Side_Thickness])
            self.exterior.prompt("Frame Top Gap","Top_Rail_Width-Top_Thickness",[Top_Rail_Width,Top_Thickness])
            self.exterior.prompt("Frame Bottom Gap",value = 0)

        if self.splitter:
            self.splitter.draw()
            self.splitter.obj_bp.parent = self.obj_bp
            self.set_drivers_for_assembly(self.splitter)
            self.splitter.prompt("Frame Thickness","fabs(Frame_Thickness)",[Frame_Thickness])
            self.splitter.prompt("Frame Left Gap","IF(Left_Fin_End,Left_Stile_Width-Left_Side_Thickness,0)",[Left_Fin_End,Left_Stile_Width,Left_Side_Thickness])
            self.splitter.prompt("Frame Right Gap","IF(Right_Fin_End,Right_Stile_Width-Right_Side_Thickness,0)",[Right_Fin_End,Right_Stile_Width,Right_Side_Thickness])
            self.splitter.prompt("Frame Top Gap","Top_Rail_Width-Top_Thickness",[Top_Rail_Width,Top_Thickness])
            self.splitter.prompt("Frame Bottom Gap",value = 0)

        if self.add_vent_hood:
            self.add_prompt(name="Vent Height",prompt_type='DISTANCE',value= fd.inches(14),tab_index=0,export=False)
            Vent_Height = self.get_var('Vent Height')
            vent = self.add_assembly(VENT)
            vent.set_name("Vent")
            vent.x_loc(value = 0)
            vent.y_loc(value = 0)
            vent.z_loc('Product_Height-Vent_Height',[Product_Height,Vent_Height])
            vent.x_dim('Product_Width',[Product_Width])
            vent.y_dim('Product_Depth',[Product_Depth])
            vent.z_dim('Vent_Height',[Vent_Height])
            
        if self.add_microwave:
            vent = self.add_assembly(MICROWAVE)
            vent.set_name("Microwave")
            vent.x_loc(value = 0)
            vent.y_loc(value = 0)
            vent.z_loc('Product_Height',[Product_Height])
            vent.x_dim('Product_Width',[Product_Width])
            vent.y_dim('Product_Depth',[Product_Depth])
            
        if self.add_empty_opening:
            opening = self.add_opening()
            opening.add_tab(name='Material Thickness',tab_type='HIDDEN')
            opening.add_prompt(name="Frame Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
            opening.add_prompt(name="Frame Left Gap",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
            opening.add_prompt(name="Frame Right Gap",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
            opening.add_prompt(name="Frame Top Gap",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
            opening.add_prompt(name="Frame Bottom Gap",prompt_type='DISTANCE',value=fd.inches(0),tab_index=0)
            
            Frame_Thickness = frame.get_var("dim_y","Frame_Thickness")
            opening.prompt("Frame Thickness","fabs(Frame_Thickness)",[Frame_Thickness])
            opening.prompt("Frame Left Gap","IF(Left_Fin_End,Left_Stile_Width-Left_Side_Thickness,0)",[Left_Fin_End,Left_Stile_Width,Left_Side_Thickness])
            opening.prompt("Frame Right Gap","IF(Right_Fin_End,Right_Stile_Width-Right_Side_Thickness,0)",[Right_Fin_End,Right_Stile_Width,Right_Side_Thickness])
            opening.prompt("Frame Top Gap","Top_Rail_Width-Top_Thickness",[Top_Rail_Width,Top_Thickness])
            opening.prompt("Frame Bottom Gap",value = 0)
            self.set_drivers_for_assembly(opening)
            
        self.update()

class Face_Frame_Blind_Corner(fd.Library_Assembly):
    
    library_name = "Cabinets - Face Frame"
    property_id = "face_frame_cabients.cabinet_prompts"
    type_assembly = "PRODUCT"
    product_shape = "RECTANGLE"
    
    carcass = None
    splitter = None
    interior = None
    exterior = None
    
    def set_drivers_for_assembly(self,assembly):
        Carcass_X = self.carcass.get_var("loc_x","Carcass_X")
        Left_Side_Thickness = self.carcass.get_var("Left Side Thickness",'Left_Side_Thickness')
        Right_Side_Thickness = self.carcass.get_var("Right Side Thickness",'Right_Side_Thickness')
        Top_Inset = self.carcass.get_var("Top Inset",'Top_Inset')
        Bottom_Inset = self.carcass.get_var("Bottom Inset",'Bottom_Inset')
        Back_Inset = self.carcass.get_var("Back Inset",'Back_Inset')
        Width = self.carcass.get_var("dim_x",'Width')
        Height = self.carcass.get_var("dim_z",'Height')
        Depth = self.carcass.get_var("dim_y",'Depth')
        
        assembly.x_loc('Carcass_X+Left_Side_Thickness',[Left_Side_Thickness,Carcass_X])
        assembly.y_loc('Depth',[Depth])
        if self.carcass.carcass_type in {"Base","Tall","Sink"}:
            assembly.z_loc('Bottom_Inset',[Bottom_Inset])
        if self.carcass.carcass_type in {"Upper","Suspended"}:
            self.mirror_z = True
            assembly.z_loc('Height+Bottom_Inset',[Height,Bottom_Inset])
        assembly.x_rot(value = 0)
        assembly.y_rot(value = 0)
        assembly.z_rot(value = 0)
        assembly.x_dim('Width-(Left_Side_Thickness+Right_Side_Thickness)',[Width,Left_Side_Thickness,Right_Side_Thickness])
        assembly.y_dim('fabs(Depth)-Back_Inset',[Depth,Back_Inset])
        assembly.z_dim('fabs(Height)-Bottom_Inset-Top_Inset',[Height,Bottom_Inset,Top_Inset])
        
    def draw(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.create_assembly()

        self.carcass.draw()
        self.carcass.obj_bp.parent = self.obj_bp

        self.add_tab(name='Face Frame Options',tab_type='VISIBLE')
        self.add_tab(name='Blind Panel Options',tab_type='VISIBLE')
        self.add_tab(name='Formulas',tab_type='HIDDEN')
        self.add_prompt(name="Top Rail Width",prompt_type='DISTANCE',value=fd.inches(2),tab_index=0)
        self.add_prompt(name="Bottom Rail Width",prompt_type='DISTANCE',value=fd.inches(1.5),tab_index=0)
        self.add_prompt(name="Left Stile Width",prompt_type='DISTANCE',value=fd.inches(2),tab_index=0)
        self.add_prompt(name="Right Stile Width",prompt_type='DISTANCE',value=fd.inches(2),tab_index=0)
        if self.carcass.carcass_type == 'Base':
            self.add_prompt(name="Blind Width",prompt_type='DISTANCE',value=g.Base_Cabinet_Depth + fd.inches(1),tab_index=1)
        if self.carcass.carcass_type == 'Tall':
            self.add_prompt(name="Blind Width",prompt_type='DISTANCE',value=g.Tall_Cabinet_Depth + fd.inches(1),tab_index=1)
        if self.carcass.carcass_type == 'Upper':
            self.add_prompt(name="Blind Width",prompt_type='DISTANCE',value=g.Upper_Cabinet_Depth + fd.inches(1),tab_index=1)
        self.add_prompt(name="Blind Panel Width",prompt_type='DISTANCE',value=fd.inches(6),tab_index=1)
        self.add_prompt(name="Blind Panel Reveal",prompt_type='DISTANCE',value=g.Blind_Panel_Reveal,tab_index=1)
        self.add_prompt(name="Inset Blind Panel",prompt_type='CHECKBOX',value=g.Inset_Blind_Panel,tab_index=1)
        self.add_prompt(name="Blind Panel Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=2)

        frame = self.add_assembly(FACE_FRAME)
        frame.set_name("Face Frame")
        
        Product_Width = self.get_var('dim_x','Product_Width')
        Product_Height = self.get_var('dim_z','Product_Height')
        Product_Depth = self.get_var('dim_y','Product_Depth')
        Top_Rail_Width = self.get_var("Top Rail Width")
        Bottom_Rail_Width = self.get_var("Bottom Rail Width")
        Left_Stile_Width = self.get_var("Left Stile Width")
        Right_Stile_Width = self.get_var("Right Stile Width")
        Blind_Panel_Width = self.get_var("Blind Panel Width")
        Blind_Panel_Reveal = self.get_var("Blind Panel Reveal")
        Blind_Width = self.get_var("Blind Width")
        
        Frame_Thickness = frame.get_var("dim_y","Frame_Thickness")
        Frame_Z_Loc = frame.get_var("loc_z",'Frame_Z_Loc')
        Frame_Y_Loc = frame.get_var("loc_y",'Frame_Y_Loc')
        Frame_Height = frame.get_var("dim_z","Frame_Height")

        Carcass_Depth = self.carcass.get_var("dim_y",'Carcass_Depth')
        Carcass_Height = self.carcass.get_var("dim_z",'Carcass_Height')
        Left_Side_Thickness = self.carcass.get_var("Left Side Thickness")
        Right_Side_Thickness = self.carcass.get_var("Right Side Thickness")
        Toe_Kick_Height = self.carcass.get_var("Toe Kick Height")
        Bottom_Thickness = self.carcass.get_var("Bottom Thickness")
        Bottom_Inset = self.carcass.get_var("Bottom Inset",'Bottom_Inset')
        Back_Inset = self.carcass.get_var("Back Inset",'Back_Inset')
        Left_Fin_End = self.carcass.get_var("Left Fin End")
        Right_Fin_End = self.carcass.get_var("Right Fin End")
        
        self.carcass.x_loc('IF(Left_Fin_End,0,Left_Stile_Width-Left_Side_Thickness)',[Left_Fin_End,Left_Stile_Width,Left_Side_Thickness])
        self.carcass.y_loc(value = 0)
        self.carcass.z_loc(value = 0)
        self.carcass.x_rot(value = 0)
        self.carcass.y_rot(value = 0)
        self.carcass.z_rot(value = 0)
        self.carcass.x_dim('Product_Width-IF(Left_Fin_End,0,Left_Stile_Width-Left_Side_Thickness)-IF(Right_Fin_End,0,Right_Stile_Width-Right_Side_Thickness)',[Product_Width,Left_Fin_End,Right_Fin_End,Left_Stile_Width,Left_Side_Thickness,Right_Stile_Width,Right_Side_Thickness])
        self.carcass.y_dim('Product_Depth',[Product_Depth])
        self.carcass.z_dim('Product_Height',[Product_Height])
        
        frame.x_loc(value = 0)
        frame.y_loc('Product_Depth',[Product_Depth])
        if self.carcass.carcass_type in {"Base","Tall","Sink"}:
            frame.z_loc('Toe_Kick_Height-Bottom_Rail_Width+Bottom_Thickness',[Toe_Kick_Height,Bottom_Rail_Width,Bottom_Thickness])
        if self.carcass.carcass_type in {"Upper","Suspended"}:
            frame.z_loc('Product_Height-Bottom_Rail_Width+Bottom_Thickness',[Product_Height,Bottom_Rail_Width,Bottom_Thickness])
        frame.x_rot(value = 0)
        frame.y_rot(value = 0)
        frame.z_rot(value = 0)
        frame.x_dim('Product_Width',[Product_Width])
        frame.y_dim(value = fd.inches(-.75))
        if self.carcass.carcass_type in {"Base","Tall","Sink"}:
            frame.z_dim('Product_Height-Toe_Kick_Height+(Bottom_Rail_Width-Bottom_Thickness)',[Product_Height,Toe_Kick_Height,Bottom_Rail_Width,Bottom_Thickness])
        if self.carcass.carcass_type in {"Upper","Suspended"}:
            frame.z_dim('fabs(Product_Height)+(Bottom_Rail_Width-Bottom_Thickness)',[Product_Height,Bottom_Rail_Width,Bottom_Thickness])
        frame.prompt("Top Rail Width",'Top_Rail_Width',[Top_Rail_Width])
        frame.prompt("Bottom Rail Width",'Bottom_Rail_Width',[Bottom_Rail_Width])
        frame.prompt("Left Stile Width",'Left_Stile_Width',[Left_Stile_Width])
        frame.prompt("Right Stile Width",'Right_Stile_Width',[Right_Stile_Width])
        frame.material("Exposed_Exterior_Surface")
        
        mid_rail = self.add_assembly(MID_RAIL)  
        mid_rail.set_name("Mid Rail")
        if self.blind_side == "Left":
            mid_rail.x_loc('Blind_Width+Blind_Panel_Reveal',[Blind_Width,Blind_Panel_Reveal])
        if self.blind_side == "Right":
            mid_rail.x_loc('Product_Width-(Blind_Width+Blind_Panel_Reveal-Blind_Panel_Width)',[Product_Width,Blind_Width,Blind_Panel_Width,Blind_Panel_Reveal])
        mid_rail.y_loc('Frame_Y_Loc',[Frame_Y_Loc])
        mid_rail.z_loc('Frame_Z_Loc+Bottom_Rail_Width',[Frame_Z_Loc,Bottom_Rail_Width])
        mid_rail.x_rot(value = 0)
        mid_rail.y_rot(value = -90)
        mid_rail.z_rot(value = 90)
        mid_rail.x_dim('Frame_Height-(Top_Rail_Width+Bottom_Rail_Width)',[Frame_Height,Top_Rail_Width,Bottom_Rail_Width])
        mid_rail.y_dim('Blind_Panel_Width',[Blind_Panel_Width])
        mid_rail.z_dim(value = fd.inches(.75))
        mid_rail.cutpart("Slab_Door")
        mid_rail.edgebanding('Door_Edges',l1 = True, w1 = True, l2 = True, w2 = True)
        
        if self.interior:
            self.interior.draw()
            self.interior.obj_bp.parent = self.obj_bp
            self.set_drivers_for_assembly(self.interior)
            
        if self.exterior:
            self.exterior.draw()
            self.exterior.obj_bp.parent = self.obj_bp
            if self.blind_side == "Left":
                self.exterior.x_loc('Blind_Width+Blind_Panel_Reveal',[Blind_Width,Blind_Panel_Reveal])
            else:
                self.exterior.x_loc('Left_Stile_Width',[Left_Stile_Width])
            self.exterior.y_loc('Carcass_Depth+Frame_Thickness',[Carcass_Depth,Frame_Thickness])
            if self.carcass.carcass_type in {"Base","Tall","Sink"}:
                self.exterior.z_loc('Frame_Z_Loc+Bottom_Rail_Width',[Frame_Z_Loc,Bottom_Rail_Width])
            if self.carcass.carcass_type in {"Upper","Suspended"}:
                self.exterior.z_loc('Carcass_Height+Bottom_Inset',[Carcass_Height,Bottom_Inset])
            self.exterior.x_rot(value = 0)
            self.exterior.y_rot(value = 0)
            self.exterior.z_rot(value = 0)
            if self.blind_side == "Left":
                self.exterior.x_dim('Product_Width-(Blind_Width+Blind_Panel_Reveal+Right_Stile_Width)',[Product_Width,Blind_Width,Blind_Panel_Reveal,Right_Stile_Width])
            else:
                self.exterior.x_dim('Product_Width-(Blind_Width+Blind_Panel_Reveal+Left_Stile_Width)',[Product_Width,Blind_Width,Blind_Panel_Reveal,Left_Stile_Width])
            self.exterior.y_dim('fabs(Carcass_Depth)-Back_Inset',[Carcass_Depth,Back_Inset])
            self.exterior.z_dim('Frame_Height-Top_Rail_Width-Bottom_Rail_Width',[Frame_Height,Top_Rail_Width,Bottom_Rail_Width])
            
        if self.splitter:
            self.splitter.draw()
            self.splitter.obj_bp.parent = self.obj_bp
            if self.blind_side == "Left":
                self.splitter.x_loc('Blind_Width+Blind_Panel_Reveal',[Blind_Width,Blind_Panel_Reveal])
            else:
                self.splitter.x_loc('Left_Stile_Width',[Left_Stile_Width])
            self.splitter.y_loc('Carcass_Depth+Frame_Thickness',[Carcass_Depth,Frame_Thickness])
            if self.carcass.carcass_type in {"Base","Tall","Sink"}:
                self.splitter.z_loc('Frame_Z_Loc+Bottom_Rail_Width',[Frame_Z_Loc,Bottom_Rail_Width])
            if self.carcass.carcass_type in {"Upper","Suspended"}:
                self.splitter.z_loc('Carcass_Height+Bottom_Inset',[Carcass_Height,Bottom_Inset])
            self.splitter.x_rot(value = 0)
            self.splitter.y_rot(value = 0)
            self.splitter.z_rot(value = 0)
            if self.blind_side == "Left":
                self.splitter.x_dim('Product_Width-(Blind_Width+Blind_Panel_Reveal+Right_Stile_Width)',[Product_Width,Blind_Width,Blind_Panel_Reveal,Right_Stile_Width])
            else:
                self.splitter.x_dim('Product_Width-(Blind_Width+Blind_Panel_Reveal+Left_Stile_Width)',[Product_Width,Blind_Width,Blind_Panel_Reveal,Left_Stile_Width])
            self.splitter.y_dim('fabs(Carcass_Depth)-Back_Inset',[Carcass_Depth,Back_Inset])
            self.splitter.z_dim('Frame_Height-Top_Rail_Width-Bottom_Rail_Width',[Frame_Height,Top_Rail_Width,Bottom_Rail_Width])
            
        self.update()

class Face_Frame_Inside_Corner(fd.Library_Assembly):
    
    library_name = "Cabinets - Face Frame"
    property_id = "face_frame_cabients.cabinet_prompts"
    type_assembly = "PRODUCT"
    placement_type = "Corner"

    carcass = None
    interior = None
    exterior = None
    face_frame = None
    
    def set_drivers_for_assembly(self,assembly):
        Width = self.carcass.get_var("dim_x",'Width')
        Height = self.carcass.get_var("dim_z",'Height')
        Depth = self.carcass.get_var("dim_y",'Depth')
        Left_Side_Thickness = self.carcass.get_var("Left Side Thickness")
        Right_Side_Thickness = self.carcass.get_var("Right Side Thickness")
        Top_Inset = self.carcass.get_var("Top Inset")
        Bottom_Inset = self.carcass.get_var("Bottom Inset")
        Back_Inset = self.carcass.get_var("Back Inset")
        
        assembly.x_loc('Left_Side_Thickness',[Left_Side_Thickness])
        assembly.y_loc('Depth',[Depth])
        if self.carcass.carcass_type in {"Base","Tall","Sink"}:
            assembly.z_loc('Bottom_Inset',[Bottom_Inset])
        if self.carcass.carcass_type in {"Upper","Suspended"}:
            self.mirror_z = True
            assembly.z_loc('Height+Bottom_Inset',[Height,Bottom_Inset])
        assembly.x_rot(value = 0)
        assembly.y_rot(value = 0)
        assembly.z_rot(value = 0)
        assembly.x_dim('Width-(Left_Side_Thickness+Right_Side_Thickness)',[Width,Left_Side_Thickness,Right_Side_Thickness])
        assembly.y_dim('fabs(Depth)-Back_Inset',[Depth,Back_Inset])
        assembly.z_dim('fabs(Height)-Bottom_Inset-Top_Inset',[Height,Bottom_Inset,Top_Inset])
        
    def add_pie_cut_ff_and_doors(self):
        Product_Width = self.get_var('dim_x','Product_Width')
        Product_Height = self.get_var('dim_z','Product_Height')
        Product_Depth = self.get_var('dim_y','Product_Depth') 
        Top_Rail_Width = self.get_var('Top Rail Width','Top_Rail_Width')   
        Bottom_Rail_Width = self.get_var('Bottom Rail Width','Bottom_Rail_Width') 
        Left_Stile_Width = self.get_var('Left Stile Width','Left_Stile_Width') 
        Right_Stile_Width = self.get_var('Right Stile Width','Right_Stile_Width')                
        
        Carcass_Width = self.carcass.get_var("dim_x",'Carcass_Width')
        Carcass_Height = self.carcass.get_var("dim_z",'Carcass_Height')
        Carcass_Depth = self.carcass.get_var("dim_y",'Carcass_Depth')
        Left_Depth = self.carcass.get_var('Cabinet Depth Left','Left_Depth')
        Right_Depth = self.carcass.get_var('Cabinet Depth Right','Right_Depth') 
        Toe_Kick_Height = self.carcass.get_var("Toe Kick Height")        
        Top_Inset = self.carcass.get_var("Top Inset")
        Bottom_Inset = self.carcass.get_var("Bottom Inset")
        Cabinet_Depth_Left = self.carcass.get_var("Cabinet Depth Left")
        Cabinet_Depth_Right = self.carcass.get_var("Cabinet Depth Right")
        Left_Fin_End = self.carcass.get_var("Left Fin End")
        Right_Fin_End = self.carcass.get_var("Right Fin End")        
        Top_Thickness = self.carcass.get_var("Top Thickness")
        Bottom_Thickness = self.carcass.get_var("Bottom Thickness")
        Left_Side_Thickness = self.carcass.get_var("Left Side Thickness")
        Right_Side_Thickness = self.carcass.get_var("Right Side Thickness") 
        
        face_frame = self.add_assembly((HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Face Frames",self.face_frame))    
        face_frame.set_name("Face Frame")          
        
        face_frame.x_loc('Left_Depth',[Left_Depth])
        face_frame.y_loc('-Right_Depth',[Right_Depth])
        
        if self.carcass.carcass_type in {"Base","Tall","Sink"}:
            face_frame.z_loc('Toe_Kick_Height-Bottom_Rail_Width+Bottom_Thickness',[Toe_Kick_Height,Bottom_Rail_Width,Bottom_Thickness])
        if self.carcass.carcass_type in {"Upper","Suspended"}:
            face_frame.z_loc('Product_Height-Bottom_Rail_Width+Bottom_Thickness',[Product_Height,Bottom_Rail_Width,Bottom_Thickness])        
        
        face_frame.x_dim('Product_Width-Left_Depth',[Left_Depth,Product_Width])
        face_frame.y_dim('Product_Depth+Right_Depth',[Right_Depth,Product_Depth])
        
        if self.carcass.carcass_type in {"Base","Tall","Sink"}:
            face_frame.z_dim('Product_Height-Toe_Kick_Height+(Bottom_Rail_Width-Bottom_Thickness)',[Product_Height,Toe_Kick_Height,Bottom_Rail_Width,Bottom_Thickness])
        if self.carcass.carcass_type in {"Upper","Suspended"}:
            face_frame.z_dim('fabs(Product_Height)+(Bottom_Rail_Width-Bottom_Thickness)',[Product_Height,Bottom_Rail_Width,Bottom_Thickness])        
        
        face_frame.prompt("Top Rail Width",'Top_Rail_Width',[Top_Rail_Width])
        face_frame.prompt("Bottom Rail Width",'Bottom_Rail_Width',[Bottom_Rail_Width])
        face_frame.prompt("Left Stile Width",'Left_Stile_Width',[Left_Stile_Width])
        face_frame.prompt("Right Stile Width",'Right_Stile_Width',[Right_Stile_Width])          
        
        Face_Frame_Thickness = face_frame.get_var("Face Frame Thickness")
        Top_Rail_Width = face_frame.get_var("Top Rail Width")
        Left_Stile_Width = face_frame.get_var("Left Stile Width")
        Right_Stile_Width = face_frame.get_var("Right Stile Width")
        
        self.exterior.draw()
        self.exterior.obj_bp.parent = self.obj_bp
        self.exterior.x_dim('Carcass_Width-Right_Side_Thickness',[Carcass_Width,Right_Side_Thickness])
        self.exterior.y_dim('Carcass_Depth+Left_Side_Thickness',[Carcass_Depth,Left_Side_Thickness])
        self.exterior.z_dim('fabs(Carcass_Height)-Bottom_Inset-Top_Inset',[Carcass_Height,Bottom_Inset,Top_Inset])
        
        if self.carcass.carcass_type == "Base":
            self.exterior.z_loc('Bottom_Inset',[Bottom_Inset])
        if self.carcass.carcass_type == "Upper":
            self.exterior.z_loc('Carcass_Height+Bottom_Inset',[Carcass_Height,Bottom_Inset])
            
        self.exterior.z_rot("",[])
            
        self.exterior.prompt("Left Side Depth","Cabinet_Depth_Left+Face_Frame_Thickness",[Cabinet_Depth_Left,Face_Frame_Thickness])
        self.exterior.prompt("Right Side Depth","Cabinet_Depth_Right+Face_Frame_Thickness",[Cabinet_Depth_Right,Face_Frame_Thickness])
        self.exterior.prompt("Frame Left Gap","IF(Left_Fin_End,Left_Stile_Width-Left_Side_Thickness,0)",[Left_Side_Thickness,Left_Fin_End,Left_Stile_Width])
        self.exterior.prompt("Frame Right Gap","IF(Right_Fin_End,Right_Stile_Width-Right_Side_Thickness,0)",[Right_Side_Thickness,Right_Fin_End,Right_Stile_Width])
        self.exterior.prompt("Frame Top Gap","Top_Rail_Width-Top_Thickness",[Top_Thickness,Top_Rail_Width])
        
    def add_diagonal_ff_and_doors(self):
        Product_Height = self.get_var('dim_z','Product_Height')
        Top_Rail_Width = self.get_var('Top Rail Width','Top_Rail_Width')   
        Bottom_Rail_Width = self.get_var('Bottom Rail Width','Bottom_Rail_Width') 
        Left_Stile_Width = self.get_var('Left Stile Width','Left_Stile_Width') 
        Right_Stile_Width = self.get_var('Right Stile Width','Right_Stile_Width')         
        
        Width = self.carcass.get_var("dim_x",'Width')
        Height = self.carcass.get_var("dim_z",'Height')
        Depth = self.carcass.get_var("dim_y",'Depth')
        Top_Inset = self.carcass.get_var("Top Inset")
        Bottom_Inset = self.carcass.get_var("Bottom Inset")
        Cabinet_Depth_Left = self.carcass.get_var("Cabinet Depth Left")
        Cabinet_Depth_Right = self.carcass.get_var("Cabinet Depth Right")
        Toe_Kick_Height = self.carcass.get_var("Toe Kick Height")
        Top_Thickness = self.carcass.get_var("Top Thickness")
        Bottom_Thickness = self.carcass.get_var("Bottom Thickness")
        Left_Side_Thickness = self.carcass.get_var("Left Side Thickness")
        Right_Side_Thickness = self.carcass.get_var("Right Side Thickness")
        
        #FACE FRAME
        face_frame = self.add_assembly((HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Face Frames",self.face_frame))    
        face_frame.set_name("Face Frame")        
        
        face_frame.x_loc('Cabinet_Depth_Left',[Cabinet_Depth_Left])   
        face_frame.y_loc('Depth+Left_Side_Thickness',[Depth,Left_Side_Thickness]) 

        if self.carcass.carcass_type in {"Base","Tall","Sink"}:
            face_frame.z_dim('Product_Height-Toe_Kick_Height+(Bottom_Rail_Width-Bottom_Thickness)',[Product_Height,Toe_Kick_Height,Bottom_Rail_Width,Bottom_Thickness])
        if self.carcass.carcass_type in {"Upper","Suspended"}:
            face_frame.z_dim('fabs(Product_Height)+(Bottom_Rail_Width-Bottom_Thickness)',[Product_Height,Bottom_Rail_Width,Bottom_Thickness]) 
            
        if self.carcass.carcass_type in {"Base","Tall","Sink"}:
            face_frame.z_loc('Toe_Kick_Height-Bottom_Rail_Width+Bottom_Thickness',[Toe_Kick_Height,Bottom_Rail_Width,Bottom_Thickness])
        if self.carcass.carcass_type in {"Upper","Suspended"}:
            face_frame.z_loc('Product_Height-Bottom_Rail_Width+Bottom_Thickness',[Product_Height,Bottom_Rail_Width,Bottom_Thickness])                
            
        face_frame.z_rot('atan((fabs(Depth)-Left_Side_Thickness-Cabinet_Depth_Right)/(fabs(Width)-Right_Side_Thickness-Cabinet_Depth_Left))',[Depth,Left_Side_Thickness,Cabinet_Depth_Right,Width,Right_Side_Thickness,Cabinet_Depth_Left])
        face_frame.x_dim('sqrt(((fabs(Depth)-Left_Side_Thickness-Cabinet_Depth_Right)**2)+((fabs(Width)-Right_Side_Thickness-Cabinet_Depth_Left)**2))',
                         [Depth,Left_Side_Thickness,Cabinet_Depth_Right,Width,Right_Side_Thickness,Cabinet_Depth_Left])
             
        face_frame.prompt("Face Frame Thickness",value=fd.inches(1.1))
        face_frame.prompt("Top Rail Width",'Top_Rail_Width',[Top_Rail_Width])
        face_frame.prompt("Bottom Rail Width",'Bottom_Rail_Width',[Bottom_Rail_Width])
        face_frame.prompt("Left Stile Width",'Left_Stile_Width',[Left_Stile_Width])
        face_frame.prompt("Right Stile Width",'Right_Stile_Width',[Right_Stile_Width])                
        
        #DOORS
        Face_Frame_Thickness = face_frame.get_var("Face Frame Thickness")
        Top_Rail_Width = face_frame.get_var("Top Rail Width")
        Left_Stile_Width = face_frame.get_var("Left Stile Width")
        Right_Stile_Width = face_frame.get_var("Right Stile Width")       
        Face_Frame_Width = face_frame.get_var("dim_x","Face_Frame_Width") 
        
        self.exterior.draw()
        self.exterior.obj_bp.parent = self.obj_bp
        
        self.exterior.add_prompt(name="Door Insert Rotation",prompt_type='ANGLE',tab_index=1)
        self.exterior.prompt("Door Insert Rotation","atan((fabs(Depth)-Left_Side_Thickness-Cabinet_Depth_Right)/(fabs(Width)-Right_Side_Thickness-Cabinet_Depth_Left))",[Depth,Left_Side_Thickness,Cabinet_Depth_Right,Width,Right_Side_Thickness,Cabinet_Depth_Left])
        Door_Insert_Rotation = self.exterior.get_var("Door Insert Rotation","Door_Insert_Rotation")
        
        self.exterior.x_loc('Cabinet_Depth_Left+Left_Stile_Width*cos(Door_Insert_Rotation)',
                            [Cabinet_Depth_Left,Left_Stile_Width,Door_Insert_Rotation])
        self.exterior.y_loc('Depth+Left_Side_Thickness+Left_Stile_Width*sin(Door_Insert_Rotation)',
                            [Depth,Left_Side_Thickness,Left_Stile_Width,Door_Insert_Rotation])
         
        if self.carcass.carcass_type == "Base":
            self.exterior.z_loc('Bottom_Inset',[Bottom_Inset])
        if self.carcass.carcass_type == "Upper":
            self.exterior.z_loc('Height+Bottom_Inset',[Height,Bottom_Inset])
 
        self.exterior.z_rot('Door_Insert_Rotation',[Door_Insert_Rotation])
        
        self.exterior.x_dim("Face_Frame_Width-Right_Stile_Width-Left_Stile_Width",[Face_Frame_Width,Right_Stile_Width,Left_Stile_Width])
        self.exterior.y_dim('Depth+Cabinet_Depth_Right+Right_Side_Thickness',[Depth,Cabinet_Depth_Right,Right_Side_Thickness])
        self.exterior.z_dim('fabs(Height)-Bottom_Inset-Top_Inset',[Height,Bottom_Inset,Top_Inset])
        
        self.exterior.prompt("Frame Thickness","Face_Frame_Thickness",[Face_Frame_Thickness])      
        self.exterior.prompt("Frame Top Gap","Top_Rail_Width-Top_Thickness",[Top_Thickness,Top_Rail_Width])
        
        Door_Thickness = self.exterior.get_var("Door Thickness","Door_Thickness")
        self.exterior.prompt("Door Y Offset","-(Face_Frame_Thickness-Door_Thickness)",[Door_Thickness,Face_Frame_Thickness])
        
    def draw(self):
        self.create_assembly()
        
        self.add_tab(name='Face Frame Options',tab_type='VISIBLE')
        self.add_prompt(name="Top Rail Width",prompt_type='DISTANCE',value=fd.inches(2),tab_index=0)
        self.add_prompt(name="Bottom Rail Width",prompt_type='DISTANCE',value=fd.inches(1.5),tab_index=0)
        self.add_prompt(name="Left Stile Width",prompt_type='DISTANCE',value=fd.inches(2),tab_index=0)
        self.add_prompt(name="Right Stile Width",prompt_type='DISTANCE',value=fd.inches(2),tab_index=0)

        Product_Width = self.get_var('dim_x','Product_Width')
        Product_Height = self.get_var('dim_z','Product_Height')
        Product_Depth = self.get_var('dim_y','Product_Depth')
  
        Left_Stile_Width = self.get_var('Left Stile Width','Left_Stile_Width') 
        Right_Stile_Width = self.get_var('Right Stile Width','Right_Stile_Width')        
        
        self.carcass.draw()
        self.carcass.obj_bp.parent = self.obj_bp
        
        Left_Side_Thickness = self.carcass.get_var("Left Side Thickness")
        Right_Side_Thickness = self.carcass.get_var("Right Side Thickness")
        Left_Fin_End = self.carcass.get_var("Left Fin End")
        Right_Fin_End = self.carcass.get_var("Right Fin End")       
        
        self.carcass.z_dim('Product_Height',[Product_Height])

        if self.carcass.carcass_shape == 'Notched':
            self.product_shape = 'INSIDE_NOTCH'
            
            self.carcass.x_dim('Product_Width-IF(Right_Fin_End,0,Right_Stile_Width-Right_Side_Thickness)',[Product_Width,Right_Fin_End,Right_Stile_Width,Right_Side_Thickness])        
            self.carcass.y_dim('Product_Depth+IF(Left_Fin_End,0,Left_Stile_Width-Left_Side_Thickness)',[Product_Depth,Left_Fin_End,Left_Stile_Width,Left_Side_Thickness])        
            
            if self.exterior:
                self.add_pie_cut_ff_and_doors()
         
        if self.carcass.carcass_shape == 'Diagonal':
            self.product_shape = 'INSIDE_DIAGONAL'
            
            self.carcass.x_dim('Product_Width',[Product_Width])        
            self.carcass.y_dim('Product_Depth',[Product_Depth])            
            
            if self.exterior:
                self.add_diagonal_ff_and_doors()

        self.update()
        
class PROMPTS_Frameless_Cabinet_Prompts(bpy.types.Operator):
    bl_idname = "cabinetlib.frameless_cabinet_prompts"
    bl_label = "Frameless Cabinet Prompts" 
    bl_options = {'UNDO'}
    
    object_name = bpy.props.StringProperty(name="Object Name")
    
    width = bpy.props.FloatProperty(name="Width",unit='LENGTH',precision=4)
    height = bpy.props.FloatProperty(name="Height",unit='LENGTH',precision=4)
    depth = bpy.props.FloatProperty(name="Depth",unit='LENGTH',precision=4)

    product_tabs = bpy.props.EnumProperty(name="Door Swing",items=[('CARCASS',"Carcass","Carcass Options"),
                                                         ('EXTERIOR',"Exterior","Exterior Options"),
                                                         ('INTERIOR',"Interior","Interior Options"),
                                                         ('SPLITTER',"Openings","Openings Options")])

    door_rotation = bpy.props.FloatProperty(name="Door Rotation",subtype='ANGLE',min=0,max=math.radians(120))
    
    door_swing = bpy.props.EnumProperty(name="Door Swing",items=[('Left Swing',"Left Swing","Left Swing"),
                                                                 ('Right Swing',"Right Swing","Right Swing")])
    
    product = None
    
    open_door_prompts = []
    
    show_exterior_options = False
    show_interior_options = False
    show_splitter_options = False
    
    inserts = []
    
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
            
        for open_door_prompt in self.open_door_prompts:
            open_door_prompt.set_value(self.door_rotation)
            
        fd.run_calculators(self.product.obj_bp)
        return True

    def execute(self, context):
        fd.run_calculators(self.product.obj_bp)
        return {'FINISHED'}

    def invoke(self,context,event):
        obj = bpy.data.objects[self.object_name]
        obj_product_bp = fd.get_bp(obj,'PRODUCT')
        self.product = fd.Assembly(obj_product_bp)
        if self.product.obj_bp:
            self.depth = math.fabs(self.product.obj_y.location.y)
            self.height = math.fabs(self.product.obj_z.location.z)
            self.width = math.fabs(self.product.obj_x.location.x)
            new_list = []
            self.inserts = fd.get_insert_bp_list(self.product.obj_bp,new_list)
        for insert in self.inserts:
            if "Door Options" in insert.mv.PromptPage.COL_MainTab:
                door = fd.Assembly(insert)
                door_rotation = door.get_prompt("Door Rotation")
                if door_rotation:
                    self.open_door_prompts.append(door_rotation)
                    self.door_rotation = door_rotation.value()
                self.show_exterior_options = True
            if "Drawer Options" in insert.mv.PromptPage.COL_MainTab:
                self.show_exterior_options = True
            if "Interior Options" in insert.mv.PromptPage.COL_MainTab:
                self.show_interior_options = True
            if "Opening Heights" in insert.mv.PromptPage.COL_MainTab:
                self.show_splitter_options = True
            if "Opening Widths" in insert.mv.PromptPage.COL_MainTab:
                self.show_splitter_options = True
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=fd.get_prop_dialog_width(500))

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
            
    def draw_carcass_prompts(self,layout):
        for insert in self.inserts:
            if "Carcass Options" in insert.mv.PromptPage.COL_MainTab:
                carcass = fd.Assembly(insert)
                left_fin_end = carcass.get_prompt("Left Fin End")
                right_fin_end = carcass.get_prompt("Right Fin End")
                left_wall_filler = carcass.get_prompt("Left Side Wall Filler")
                right_wall_filler = carcass.get_prompt("Right Side Wall Filler")
                
                valance_height_top = carcass.get_prompt("Valance Height Top")
                toe_kick_height = carcass.get_prompt("Toe Kick Height")
                remove_bottom = carcass.get_prompt("Remove Bottom")
                remove_back = carcass.get_prompt("Remove Back")
                use_thick_back = carcass.get_prompt("Use Thick Back")
                use_nailers = carcass.get_prompt("Use Nailers")
                cabinet_depth_left = carcass.get_prompt("Cabinet Depth Left")
                cabinet_depth_right = carcass.get_prompt("Cabinet Depth Right")
                
                sub_front_height = carcass.get_prompt("Sub Front Height")
                
                # SIDE OPTIONS:
                if left_wall_filler and right_wall_filler:
                    col = layout.column(align=True)
                    col.label("Side Options:")
                    
                    row = col.row()
                    row.prop(left_wall_filler,'DistanceValue',text="Left Filler Amount")
                    row.prop(left_fin_end,'CheckBoxValue',text="Left Fin End")
                    
                    row = col.row()
                    row.prop(right_wall_filler,'DistanceValue',text="Right Filler Amount")
                    row.prop(right_fin_end,'CheckBoxValue',text="Right Fin End")
                
                # CARCASS OPTIONS:
                col = layout.column(align=True)
                col.label("Carcass Options:")
                row = col.row()
                if use_thick_back:
                    row.prop(use_thick_back,'CheckBoxValue',text="Use Thick Back")
                if use_nailers:
                    row.prop(use_nailers,'CheckBoxValue',text="Use Nailers")
                if remove_bottom:
                    row.prop(remove_bottom,'CheckBoxValue',text="Remove Bottom")
                if remove_back:
                    row.prop(remove_back,'CheckBoxValue',text="Remove Back")
                if cabinet_depth_left:
                    row = col.row()
                    row.prop(cabinet_depth_left,'DistanceValue',text="Cabinet Depth Left")
                    row.prop(cabinet_depth_right,'DistanceValue',text="Cabinet Depth Right")
                
                # TOE KICK OPTIONS
                if toe_kick_height:
                    col = layout.column(align=True)
                    toe_kick_setback = carcass.get_prompt("Toe Kick Setback")
                    col.label("Toe Kick Options:")
                    row = col.row()
                    row.prop(toe_kick_height,'DistanceValue',text="Toe Kick Height")
                    row.prop(toe_kick_setback,'DistanceValue',text="Toe Kick Setback")
                    
                # VALANCE OPTIONS
                if valance_height_top:
                    r_full_height = carcass.get_prompt("Right Side Full Height")
                    l_full_height = carcass.get_prompt("Left Side Full Height")
                    valance_each_unit = carcass.get_prompt("Valance Each Unit")
                    
                    col = layout.column(align=True)
                    col.label("Valance Options:")
                    door_valance_top = carcass.get_prompt("Door Valance Top")
                    row = col.row()
                    row.prop(valance_height_top,'DistanceValue',text="Valance Height Top")
                    row.prop(door_valance_top,'CheckBoxValue',text="Door Valance Top")

                    valance_height_bottom = carcass.get_prompt("Valance Height Bottom")
                    
                    if valance_height_bottom:
                        door_valance_bottom = carcass.get_prompt("Door Valance Bottom")
                        row = col.row()
                        row.prop(valance_height_bottom,'DistanceValue',text="Valance Height Bottom")
                        row.prop(door_valance_bottom,'CheckBoxValue',text="Door Valance Bottom")
                    
                    row = col.row()
                    row.prop(l_full_height,'CheckBoxValue',text="Left Side Full Height")
                    row.prop(r_full_height,'CheckBoxValue',text="Right Side Full Height")
                    
                    row = col.row()
                    row.prop(valance_each_unit,'CheckBoxValue',text="Add Valance For Each Unit")
                    
                if sub_front_height:
                    pass
        
    def draw_opening_prompt(self):
        pass
        
    def draw_door_prompts(self,layout):
        for insert in self.inserts:
            if "Door Options" in insert.mv.PromptPage.COL_MainTab:
                row = layout.row()
                row.label("Open Door")
                row.prop(self,'door_rotation',text="",slider=True)
                break
            
        for insert in self.inserts:
            if "Door Options" in insert.mv.PromptPage.COL_MainTab:
                box = layout.box()
                col = box.column(align=True)
                row = col.row()
                row.label(insert.mv.name_object + " Options:")
                door = fd.Assembly(insert)
                left_swing = door.get_prompt("Left Swing")
                inset_front = door.get_prompt("Inset Front")
                hot = door.get_prompt("Half Overlay Top")
                hob = door.get_prompt("Half Overlay Bottom")
                hol = door.get_prompt("Half Overlay Left")
                hor = door.get_prompt("Half Overlay Right")
                
                row.prop(inset_front,'CheckBoxValue',text="Inset Door")
                
                if left_swing:
                    row.prop(left_swing,'CheckBoxValue',text="Left Swing Door")
                    
                if hot:
                    row = col.row()
                    row.label("Half Overlays:")
                    row.prop(hot,'CheckBoxValue',text="Top")
                    row.prop(hob,'CheckBoxValue',text="Bottom")
                    row.prop(hol,'CheckBoxValue',text="Left")
                    row.prop(hor,'CheckBoxValue',text="Right")
        
    def draw_drawer_prompts(self,layout):
        for insert_bp in self.inserts:
            if "Drawer Options" in insert_bp.mv.PromptPage.COL_MainTab:
                insert = fd.Assembly(insert_bp)
                open_prompt = insert.get_prompt("Open")
                
                if open_prompt:
                    row = layout.row()
                    row.label("Open Drawer")
                    row.prop(open_prompt,"PercentageValue",text="")
                
                box = layout.box()
                col = box.column(align=True)
                row = col.row()
                row.label(insert_bp.mv.name_object + " Options:")
                
                inset_front = insert.get_prompt("Inset Front")
                half_overlay_top = insert.get_prompt("Half Overlay Top")
                
                if inset_front:
                    row.prop(inset_front,'CheckBoxValue',text="Inset Front")
                    
                if half_overlay_top:
                    half_overlay_bottom = insert.get_prompt("Half Overlay Bottom")
                    half_overlay_left = insert.get_prompt("Half Overlay Left")
                    half_overlay_right = insert.get_prompt("Half Overlay Right")
                    row = col.row()
                    row.label("Half Overlays:")
                    row.prop(half_overlay_top,'CheckBoxValue',text="Top")
                    row.prop(half_overlay_bottom,'CheckBoxValue',text="Bottom")
                    row.prop(half_overlay_left,'CheckBoxValue',text="Left")
                    row.prop(half_overlay_right,'CheckBoxValue',text="Right")
                
            if "Drawer Heights" in insert_bp.mv.PromptPage.COL_MainTab:
                insert = fd.Assembly(insert_bp)
                drawer_height_1 = insert.get_prompt("Top Drawer Height")
                drawer_height_2 = insert.get_prompt("Second Drawer Height")
                drawer_height_3 = insert.get_prompt("Third Drawer Height")
                drawer_height_4 = insert.get_prompt("Bottom Drawer Height")
                
                if drawer_height_1:
                    row = box.row()
                    row.label("Drawer 1 Height:")
                    if drawer_height_1.equal:
                        row.label(str(fd.unit(drawer_height_1.DistanceValue)))
                        row.prop(drawer_height_1,'equal',text="")
                    else:
                        row.prop(drawer_height_1,'DistanceValue',text="")
                        row.prop(drawer_height_1,'equal',text="")
                
                if drawer_height_2:
                    row = box.row()
                    row.label("Drawer 2 Height:")
                    if drawer_height_2.equal:
                        row.label(str(fd.unit(drawer_height_2.DistanceValue)))
                        row.prop(drawer_height_2,'equal',text="")
                    else:
                        row.prop(drawer_height_2,'DistanceValue',text="")
                        row.prop(drawer_height_2,'equal',text="")
                
                if drawer_height_3:
                    row = box.row()
                    row.label("Drawer 3 Height:")
                    if drawer_height_3.equal:
                        row.label(str(fd.unit(drawer_height_3.DistanceValue)))
                        row.prop(drawer_height_3,'equal',text="")
                    else:
                        row.prop(drawer_height_3,'DistanceValue',text="")
                        row.prop(drawer_height_3,'equal',text="")
                
                if drawer_height_4:
                    row = box.row()
                    row.label("Drawer 4 Height:")
                    if drawer_height_4.equal:
                        row.label(str(fd.unit(drawer_height_4.DistanceValue)))
                        row.prop(drawer_height_4,'equal',text="")
                    else:
                        row.prop(drawer_height_4,'DistanceValue',text="")
                        row.prop(drawer_height_4,'equal',text="")
        
    def draw_interior_prompts(self,layout):
        for insert in self.inserts:
            if "Interior Options" in insert.mv.PromptPage.COL_MainTab:
                box = layout.box()
                col = box.column(align=True)
                col.label("Interior Options:")
                carcass = fd.Assembly(insert)
                adj_shelf_qty = carcass.get_prompt("Adj Shelf Qty")
                fix_shelf_qty = carcass.get_prompt("Fixed Shelf Qty")
                div_qty_per_row = carcass.get_prompt("Divider Qty Per Row")
                division_qty = carcass.get_prompt("Division Qty")
                adj_shelf_rows = carcass.get_prompt("Adj Shelf Rows")
                fixed_shelf_rows = carcass.get_prompt("Fixed Shelf Rows")
                
                if adj_shelf_qty:
                    row = col.row()
                    row.label("Adjustable Shelf Qty")
                    row.prop(adj_shelf_qty,'QuantityValue',text="")
        
                    row.label("Fixed Shelf Qty")
                    row.prop(fix_shelf_qty,'QuantityValue',text="")
                    
                if div_qty_per_row:
                    row = col.row()
                    row.label("Divider Qty Per Row")
                    row.prop(div_qty_per_row,'QuantityValue',text="")
                
                if division_qty:
                    row = col.row()
                    row.label("Division Qty")
                    row.prop(division_qty,'QuantityValue',text="")
                
                if adj_shelf_rows:
                    row = col.row()
                    row.label("Adjustable Shelf Rows")
                    row.prop(adj_shelf_rows,'QuantityValue',text="")
                    
                    row.label("Fixed Shelf Rows")
                    row.prop(fixed_shelf_rows,'QuantityValue',text="")
        
    def draw_splitter_prompts(self,layout):
        for insert in self.inserts:
            if "Opening Heights" in insert.mv.PromptPage.COL_MainTab:
                box = layout.box()
                col = box.column(align=True)
                col.label("Splitter Options:")
                splitter = fd.Assembly(insert)
                opening_1 = splitter.get_prompt("Opening 1 Height")
                opening_2 = splitter.get_prompt("Opening 2 Height")
                opening_3 = splitter.get_prompt("Opening 3 Height")
                opening_4 = splitter.get_prompt("Opening 4 Height")
                
                if opening_1:
                    row = box.row()
                    row.label("Opening 1 Height:")
                    if opening_1.equal:
                        row.label(str(fd.unit(opening_1.DistanceValue)))
                        row.prop(opening_1,'equal',text="")
                    else:
                        row.prop(opening_1,'DistanceValue',text="")
                        row.prop(opening_1,'equal',text="")
                if opening_2:
                    row = box.row()
                    row.label("Opening 2 Height:")
                    if opening_2.equal:
                        row.label(str(fd.unit(opening_2.DistanceValue)))
                        row.prop(opening_2,'equal',text="")
                    else:
                        row.prop(opening_2,'DistanceValue',text="")
                        row.prop(opening_2,'equal',text="")
                if opening_3:
                    row = box.row()
                    row.label("Opening 3 Height:")
                    if opening_3.equal:
                        row.label(str(fd.unit(opening_3.DistanceValue)))
                        row.prop(opening_3,'equal',text="")
                    else:
                        row.prop(opening_3,'DistanceValue',text="")
                        row.prop(opening_3,'equal',text="")
                if opening_4:
                    row = box.row()
                    row.label("Opening 4 Height:")
                    if opening_4.equal:
                        row.label(str(fd.unit(opening_4.DistanceValue)))
                        row.prop(opening_4,'equal',text="")
                    else:
                        row.prop(opening_4,'DistanceValue',text="")
                        row.prop(opening_4,'equal',text="")
        
    def draw(self, context):
        layout = self.layout
        if self.product.obj_bp:
            if self.product.obj_bp.name in context.scene.objects:
                box = layout.box()
                
                split = box.split(percentage=.8)
                split.label(self.product.obj_bp.mv.name_object + " | " + self.product.obj_bp.cabinetlib.spec_group_name,icon='LATTICE_DATA')
                split.menu('MENU_Current_Cabinet_Menu',text="Menu",icon='DOWNARROW_HLT')
                
                self.draw_product_size(box)
                
                prompt_box = box.box()
                row = prompt_box.row(align=True)
                row.prop_enum(self, "product_tabs", 'CARCASS') 
                if self.show_exterior_options:
                    row.prop_enum(self, "product_tabs", 'EXTERIOR') 
                if self.show_interior_options:
                    row.prop_enum(self, "product_tabs", 'INTERIOR') 
                if self.show_splitter_options:
                    row.prop_enum(self, "product_tabs", 'SPLITTER') 

                if self.product_tabs == 'CARCASS':
                    self.draw_carcass_prompts(prompt_box)
                if self.product_tabs == 'EXTERIOR':
                    self.draw_door_prompts(prompt_box)
                    self.draw_drawer_prompts(prompt_box)
                if self.product_tabs == 'INTERIOR':
                    self.draw_interior_prompts(prompt_box)
                if self.product_tabs == 'SPLITTER':
                    self.draw_splitter_prompts(prompt_box)     
      
class PROMPTS_Face_Frame_Cabinet_Prompts(bpy.types.Operator):
    bl_idname = "face_frame_cabients.cabinet_prompts"
    bl_label = "Face Frame Cabinet Prompts" 
    bl_options = {'UNDO'}
         
    object_name = bpy.props.StringProperty(name="Object Name")
     
    width = bpy.props.FloatProperty(name="Width",unit='LENGTH',precision=4)
    height = bpy.props.FloatProperty(name="Height",unit='LENGTH',precision=4)
    depth = bpy.props.FloatProperty(name="Depth",unit='LENGTH',precision=4)
 
    product_tabs = bpy.props.EnumProperty(name="Door Swing",items=[('CARCASS',"Carcass","Carcass Options"),
                                                         ('EXTERIOR',"Exterior","Exterior Options"),
                                                         ('INTERIOR',"Interior","Interior Options"),
                                                         ('SPLITTER',"Openings","Openings Options"),
                                                         ('FACEFRAME',"Face Frame","Face Frame Options")])
 
    door_rotation = bpy.props.FloatProperty(name="Door Rotation",subtype='ANGLE',min=0,max=math.radians(120))
     
    door_swing = bpy.props.EnumProperty(name="Door Swing",items=[('Left Swing',"Left Swing","Left Swing"),
                                                       ('Right Swing',"Right Swing","Right Swing")])
     
    product = None
     
    open_door_prompt = None
     
    open_door_prompts = []
     
    inserts = []
     
    show_exterior_options = False
    show_interior_options = False
    show_splitter_options = False
     
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
             
        for prompt in self.open_door_prompts:
            prompt.set_value(self.door_rotation)
             
        fd.run_calculators(self.product.obj_bp)
        self.product.obj_bp.location = self.product.obj_bp.location
        return True
 
    def execute(self, context):
        fd.run_calculators(self.product.obj_bp)
         
        return {'FINISHED'}
 
    def invoke(self,context,event):
        self.open_door_prompts = []
        obj = bpy.data.objects[self.object_name]
        obj_product_bp = fd.get_bp(obj,'PRODUCT')
        self.product = fd.Assembly(obj_product_bp)
        if self.product.obj_bp:
            self.depth = math.fabs(self.product.obj_y.location.y)
            self.height = math.fabs(self.product.obj_z.location.z)
            self.width = math.fabs(self.product.obj_x.location.x)
            new_list = []
            self.inserts = fd.get_insert_bp_list(self.product.obj_bp,new_list)
        for insert in self.inserts:
            if "Door Options" in insert.mv.PromptPage.COL_MainTab:
                door = fd.Assembly(insert)
                door_rotation = door.get_prompt("Door Rotation")
                if door_rotation:
                    self.open_door_prompts.append(door_rotation)
                    self.door_rotation = door_rotation.value()
                self.show_exterior_options = True
            if "Drawer Options" in insert.mv.PromptPage.COL_MainTab:
                self.show_exterior_options = True
            if "Interior Options" in insert.mv.PromptPage.COL_MainTab:
                self.show_interior_options = True
            if "Opening Heights" in insert.mv.PromptPage.COL_MainTab:
                self.show_splitter_options = True
            if "Opening Widths" in insert.mv.PromptPage.COL_MainTab:
                self.show_splitter_options = True
 
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=fd.get_prop_dialog_width(500))
 
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
             
    def draw_carcass_prompts(self,layout):
        for insert in self.inserts:
            if "Carcass Options" in insert.mv.PromptPage.COL_MainTab:
                carcass = fd.Assembly(insert)
                left_fin_end = carcass.get_prompt("Left Fin End")
                right_fin_end = carcass.get_prompt("Right Fin End")
#                 left_wall_filler = carcass.get_prompt("Left Side Wall Filler")
#                 right_wall_filler = carcass.get_prompt("Right Side Wall Filler")
                 
                toe_kick_height = carcass.get_prompt("Toe Kick Height")
                remove_bottom = carcass.get_prompt("Remove Bottom")
                remove_back = carcass.get_prompt("Remove Back")
                use_thick_back = carcass.get_prompt("Use Thick Back")
                use_nailers = carcass.get_prompt("Use Nailers")
                cabinet_depth_left = carcass.get_prompt("Cabinet Depth Left")
                cabinet_depth_right = carcass.get_prompt("Cabinet Depth Right")
                 
                # SIDE OPTIONS:
                col = layout.column(align=True)
                col.label("Side Options:")
                row = col.row()
                row.prop(left_fin_end,'CheckBoxValue',text="Left Fin End")
                row.prop(right_fin_end,'CheckBoxValue',text="Right Fin End")
                 
                # CARCASS OPTIONS:
                col = layout.column(align=True)
                col.label("Carcass Options:")
                row = col.row()
                if use_thick_back:
                    row.prop(use_thick_back,'CheckBoxValue',text="Use Thick Back")
                if use_nailers:
                    row.prop(use_nailers,'CheckBoxValue',text="Use Nailers")
                if remove_bottom:
                    row.prop(remove_bottom,'CheckBoxValue',text="Remove Bottom")
                if remove_back:
                    row.prop(remove_back,'CheckBoxValue',text="Remove Back")
                if cabinet_depth_left:
                    row = col.row()
                    row.prop(cabinet_depth_left,'DistanceValue',text="Cabinet Depth Left")
                    row.prop(cabinet_depth_right,'DistanceValue',text="Cabinet Depth Right")
                 
                # TOE KICK OPTIONS
                if toe_kick_height:
                    col = layout.column(align=True)
                    toe_kick_setback = carcass.get_prompt("Toe Kick Setback")
                    col.label("Toe Kick Options:")
                    row = col.row()
                    row.prop(toe_kick_height,'DistanceValue',text="Toe Kick Height")
                    row.prop(toe_kick_setback,'DistanceValue',text="Toe Kick Setback")
                     
    def draw_door_prompts(self,layout):
        for insert in self.inserts:
            if "Door Options" in insert.mv.PromptPage.COL_MainTab:
                 
                #TODO make pie cut door insert rot z for door open
                if "Pie Cut" not in insert.mv.name_object:
                    row = layout.row()
                    row.label("Open")
                    row.prop(self,'door_rotation',text="",slider=True)
                    break
             
        for insert in self.inserts:
            if "Door Options" in insert.mv.PromptPage.COL_MainTab:
                box = layout.box()
                col = box.column(align=True)
                col.label(insert.mv.name_object + " Options:")
                door = fd.Assembly(insert)
                left_swing = door.get_prompt("Left Swing")
                inset_front = door.get_prompt("Inset Front")
                 
                row = col.row()
                row.label("Inset Door")
                row.prop(inset_front,'CheckBoxValue',text="")
 
                if left_swing:
                    row = col.row()
                    row.label("Left Door Swing")
                    row.prop(left_swing,'CheckBoxValue',text="")
         
    def draw_drawer_prompts(self,layout):
        for insert_bp in self.inserts:
            if "Drawer Options" in insert_bp.mv.PromptPage.COL_MainTab:
                insert = fd.Assembly(insert_bp)
                open_prompt = insert.get_prompt("Open")
                 
                if open_prompt:
                    row = layout.row()
                    row.label("Open Drawer")
                    row.prop(open_prompt,"PercentageValue",text="")
                 
                box = layout.box()
                col = box.column(align=True)
                row = col.row()
                row.label(insert_bp.mv.name_object + " Options:")
                 
                inset_front = insert.get_prompt("Inset Front")
                half_overlay_top = insert.get_prompt("Half Overlay Top")
                 
                if inset_front:
                    row.prop(inset_front,'CheckBoxValue',text="Inset Front")
                     
                if half_overlay_top:
                    half_overlay_bottom = insert.get_prompt("Half Overlay Bottom")
                    half_overlay_left = insert.get_prompt("Half Overlay Left")
                    half_overlay_right = insert.get_prompt("Half Overlay Right")
                    row = col.row()
                    row.label("Half Overlays:")
                    row.prop(half_overlay_top,'CheckBoxValue',text="Top")
                    row.prop(half_overlay_bottom,'CheckBoxValue',text="Bottom")
                    row.prop(half_overlay_left,'CheckBoxValue',text="Left")
                    row.prop(half_overlay_right,'CheckBoxValue',text="Right")
                 
            if "Drawer Heights" in insert_bp.mv.PromptPage.COL_MainTab:
                insert = fd.Assembly(insert_bp)
                drawer_height_1 = insert.get_prompt("Top Drawer Height")
                drawer_height_2 = insert.get_prompt("Second Drawer Height")
                drawer_height_3 = insert.get_prompt("Third Drawer Height")
                drawer_height_4 = insert.get_prompt("Bottom Drawer Height")
                 
                if drawer_height_1:
                    row = box.row()
                    row.label("Drawer 1 Height:")
                    if drawer_height_1.equal:
                        row.label(str(fd.unit(drawer_height_1.DistanceValue)))
                        row.prop(drawer_height_1,'equal',text="")
                    else:
                        row.prop(drawer_height_1,'DistanceValue',text="")
                        row.prop(drawer_height_1,'equal',text="")
                 
                if drawer_height_2:
                    row = box.row()
                    row.label("Drawer 2 Height:")
                    if drawer_height_2.equal:
                        row.label(str(fd.unit(drawer_height_2.DistanceValue)))
                        row.prop(drawer_height_2,'equal',text="")
                    else:
                        row.prop(drawer_height_2,'DistanceValue',text="")
                        row.prop(drawer_height_2,'equal',text="")
                 
                if drawer_height_3:
                    row = box.row()
                    row.label("Drawer 3 Height:")
                    if drawer_height_3.equal:
                        row.label(str(fd.unit(drawer_height_3.DistanceValue)))
                        row.prop(drawer_height_3,'equal',text="")
                    else:
                        row.prop(drawer_height_3,'DistanceValue',text="")
                        row.prop(drawer_height_3,'equal',text="")
                 
                if drawer_height_4:
                    row = box.row()
                    row.label("Drawer 4 Height:")
                    if drawer_height_4.equal:
                        row.label(str(fd.unit(drawer_height_4.DistanceValue)))
                        row.prop(drawer_height_4,'equal',text="")
                    else:
                        row.prop(drawer_height_4,'DistanceValue',text="")
                        row.prop(drawer_height_4,'equal',text="")
         
    def draw_face_frame_options(self,layout):
        top_rail_width = self.product.get_prompt("Top Rail Width")
        bottom_rail_width = self.product.get_prompt("Bottom Rail Width")
        left_stile_width = self.product.get_prompt("Left Stile Width")
        right_stile_width = self.product.get_prompt("Right Stile Width")
         
        if top_rail_width:
            box = layout.box()
            box.label("Face Frame Options:")
            row = box.row()
            row.prop(top_rail_width,"DistanceValue",text="Top Rail Width") 
            row.prop(bottom_rail_width,"DistanceValue",text="Bottom Rail Width") 
            row = box.row()
            row.prop(left_stile_width,"DistanceValue",text="Left Stile Width") 
            row.prop(right_stile_width,"DistanceValue",text="Right Stile Width") 
             
    def draw_interior_prompts(self,layout):
        for insert in self.inserts:
            if "Interior Options" in insert.mv.PromptPage.COL_MainTab:
                box = layout.box()
                col = box.column(align=True)
                col.label("Interior Options:")
                carcass = fd.Assembly(insert)
                adj_shelf_qty = carcass.get_prompt("Adj Shelf Qty")
                fix_shelf_qty = carcass.get_prompt("Fixed Shelf Qty")
                div_qty_per_row = carcass.get_prompt("Divider Qty Per Row")
                division_qty = carcass.get_prompt("Division Qty")
                adj_shelf_rows = carcass.get_prompt("Adj Shelf Rows")
                fixed_shelf_rows = carcass.get_prompt("Fixed Shelf Rows")
                 
                if adj_shelf_qty:
                    row = col.row()
                    row.label("Adjustable Shelf Qty")
                    row.prop(adj_shelf_qty,'QuantityValue',text="")
         
                    row.label("Fixed Shelf Qty")
                    row.prop(fix_shelf_qty,'QuantityValue',text="")
                     
                if div_qty_per_row:
                    row = col.row()
                    row.label("Divider Qty Per Row")
                    row.prop(div_qty_per_row,'QuantityValue',text="")
                 
                if division_qty:
                    row = col.row()
                    row.label("Division Qty")
                    row.prop(division_qty,'QuantityValue',text="")
                 
                if adj_shelf_rows:
                    row = col.row()
                    row.label("Adjustable Shelf Rows")
                    row.prop(adj_shelf_rows,'QuantityValue',text="")
                     
                    row.label("Fixed Shelf Rows")
                    row.prop(fixed_shelf_rows,'QuantityValue',text="")
         
    def draw_splitter_prompts(self,layout):
        for insert in self.inserts:
            if "Opening Heights" in insert.mv.PromptPage.COL_MainTab:
                box = layout.box()
                col = box.column(align=True)
                col.label("Splitter Options:")
                splitter = fd.Assembly(insert)
                opening_1 = splitter.get_prompt("Opening 1 Height")
                opening_2 = splitter.get_prompt("Opening 2 Height")
                opening_3 = splitter.get_prompt("Opening 3 Height")
                opening_4 = splitter.get_prompt("Opening 4 Height")
                 
                if opening_1:
                    row = col.row()
                    row.label("Opening 1 Height:")
                    if opening_1.equal:
                        row.label(str(fd.unit(opening_1.DistanceValue)))
                        row.prop(opening_1,'equal',text="")
                    else:
                        row.prop(opening_1,'DistanceValue',text="")
                        row.prop(opening_1,'equal',text="")
                if opening_2:
                    row = col.row()
                    row.label("Opening 2 Height:")
                    if opening_2.equal:
                        row.label(str(fd.unit(opening_2.DistanceValue)))
                        row.prop(opening_2,'equal',text="")
                    else:
                        row.prop(opening_2,'DistanceValue',text="")
                        row.prop(opening_2,'equal',text="")
                if opening_3:
                    row = col.row()
                    row.label("Opening 3 Height:")
                    if opening_3.equal:
                        row.label(str(fd.unit(opening_3.DistanceValue)))
                        row.prop(opening_3,'equal',text="")
                    else:
                        row.prop(opening_3,'DistanceValue',text="")
                        row.prop(opening_3,'equal',text="")
                if opening_4:
                    row = col.row()
                    row.label("Opening 4 Height:")
                    if opening_4.equal:
                        row.label(str(fd.unit(opening_4.DistanceValue)))
                        row.prop(opening_4,'equal',text="")
                    else:
                        row.prop(opening_4,'DistanceValue',text="")
                        row.prop(opening_4,'equal',text="")
         
    def draw_product_placment(self,layout):
        box = layout.box()
        row = box.row()
        row.label('Location:')
        row.prop(self.product.obj_bp,'location',text="")
        row.label('Rotation:')
        row.prop(self.product.obj_bp,'rotation_euler',index=2,text="")
         
    def draw(self, context):
        layout = self.layout
        if self.product.obj_bp:
            if self.product.obj_bp.name in context.scene.objects:
                box = layout.box()
                  
                split = box.split(percentage=.8)
                split.label(self.product.obj_bp.mv.name_object + " | " + self.product.obj_bp.cabinetlib.spec_group_name,icon='LATTICE_DATA')
                split.menu('MENU_Current_Cabinet_Menu',text="Menu",icon='DOWNARROW_HLT')
                 
                self.draw_product_size(box)
                 
                prompt_box = box.box()
                row = prompt_box.row(align=True)
                row.prop_enum(self, "product_tabs", 'CARCASS') 
                if self.show_exterior_options:
                    row.prop_enum(self, "product_tabs", 'EXTERIOR') 
                if self.show_interior_options:
                    row.prop_enum(self, "product_tabs", 'INTERIOR') 
                if self.show_splitter_options:
                    row.prop_enum(self, "product_tabs", 'SPLITTER') 
                row.prop_enum(self, "product_tabs", 'FACEFRAME') 
                if self.product_tabs == 'CARCASS':
                    self.draw_carcass_prompts(prompt_box)
                if self.product_tabs == 'FACEFRAME':
                    self.draw_face_frame_options(prompt_box)
                if self.product_tabs == 'EXTERIOR':
                    self.draw_door_prompts(prompt_box)
                    self.draw_drawer_prompts(prompt_box)
                if self.product_tabs == 'INTERIOR':
                    self.draw_interior_prompts(prompt_box)
                if self.product_tabs == 'SPLITTER':
                    self.draw_splitter_prompts(prompt_box)      
                    
def register():
    bpy.utils.register_class(PROMPTS_Face_Frame_Cabinet_Prompts)
    bpy.utils.register_class(PROMPTS_Frameless_Cabinet_Prompts)
    
def unregister():
    bpy.utils.unregister_class(PROMPTS_Face_Frame_Cabinet_Prompts)
    bpy.utils.unregister_class(PROMPTS_Frameless_Cabinet_Prompts)    
        
