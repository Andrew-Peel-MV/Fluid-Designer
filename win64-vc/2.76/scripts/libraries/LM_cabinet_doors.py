"""
Microvellum 
Cabinet Doors
Experimental library module to create 5 piece doors
No other library modules are using this module. This is
provided as an example of how a 5 piece door library can
be created.
"""

import bpy
import fd
import math

DOOR_MATERIAL = ("Wood","Wood Finished","Macchiato Walnut")
HIDDEN_FOLDER_NAME = "_HIDDEN"
CATEGORY_NAME = "5 Piece Door Assemblies"

class Material_Pointers():
    Door_Material = fd.Material_Pointer(DOOR_MATERIAL)

class Scene_Variables(bpy.types.PropertyGroup):
    Door_Width = bpy.props.FloatProperty(name="Door Width",
                                         description="Default width for doors",
                                         default=fd.inches(18.0),
                                         unit='LENGTH')  
    
    Door_Height = bpy.props.FloatProperty(name="Door Height",
                                          description="Default height for doors",
                                          default=fd.inches(24.0),
                                          unit='LENGTH')  
    
    Door_Depth = bpy.props.FloatProperty(name="Door Depth",
                                         description="Default depth for doors",
                                         default=fd.inches(0.75),
                                         unit='LENGTH')  
    
class Cabinet_Door(fd.Library_Assembly):
    library_name = "Cabinet Doors"
    category_name = ""
    assembly_name = ""
    property_id = ""
    type_assembly = "PRODUCT"
    mirror_z = False
    mirror_y = False
    width = 0.0
    height = 0.0
    depth = 0.0
    
    panel = ""
    stile = ""
    stile_width = 0.0
    top_rail = ""
    top_rail_height = 0.0
    bottom_rail = ""
    bottom_rail_height = 0.0
    mullion = ""
    
    profile_width = fd.inches(0.53125)
    panel_overlap = fd.inches(0.25)
    
#     cut_down_height = 0.0
#     cut_down_width = 0.0
#     stile_cut_down = fd.inches(1)
#     rail_cut_down = fd.inches(1)
    
    min_width = 0.0
    min_width_replacement = ""
    min_height = 0.0
    min_height_replacement = ""

    def draw(self):
        self.create_assembly()
        
        self.add_tab(name='Main Options',tab_type='VISIBLE')
        self.add_prompt(name="Mullion Door",prompt_type='CHECKBOX',value=False,tab_index=0)
        self.add_prompt(name="Beauty Mold",prompt_type='CHECKBOX',value=False,tab_index=0)
        
        self.add_tab(name="Formulas", tab_type='HIDDEN')
        self.add_prompt(name="Min Width", prompt_type='DISTANCE', value=self.min_width, tab_index=1,lock=True)
        self.add_prompt(name="Min Height", prompt_type='DISTANCE', value=self.min_height, tab_index=1,lock=True)
        self.add_prompt(name="Profile Width", prompt_type='DISTANCE', value=self.profile_width, tab_index=1,lock=True)
        self.add_prompt(name="Top Rail Height", prompt_type='DISTANCE', value=self.top_rail_height, tab_index=1,lock=True)
        self.add_prompt(name="Bottom Rail Height", prompt_type='DISTANCE', value=self.bottom_rail_height, tab_index=1,lock=True)
        self.add_prompt(name="Stile Width", prompt_type='DISTANCE', value=self.stile_width, tab_index=1,lock=True)
        self.add_prompt(name="Panel Overlap", prompt_type='DISTANCE', value=self.panel_overlap, tab_index=1,lock=True)
#         self.add_prompt(name="Cut Down Width", prompt_type='DISTANCE', value=self.cut_down_width, tab_index=1,lock=True)
#         self.add_prompt(name="Cut Down Height", prompt_type='DISTANCE', value=self.cut_down_height, tab_index=1,lock=True)  
#         self.add_prompt(name="Stile Cut Down", prompt_type='DISTANCE', value=self.stile_cut_down, tab_index=1,lock=True)
#         self.add_prompt(name="Rail Cut Down", prompt_type='DISTANCE', value=self.rail_cut_down, tab_index=1,lock=True)     
        
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        M_Door = self.get_var('Mullion Door', 'M_Door')
        Min_Width = self.get_var('Min Width','Min_Width')
        Min_Height = self.get_var('Min Height','Min_Height')
        P_Wd = self.get_var('Profile Width','P_Wd')
        Tr_Height = self.get_var('Top Rail Height','Tr_Height')
        Br_Height = self.get_var('Bottom Rail Height','Br_Height')
        St_Wd = self.get_var('Stile Width','St_Wd')
        Pan_Ovlp = self.get_var('Panel Overlap','Pan_Ovlp')
#         Cd_Width = self.get_var('Cut Down Width','Cd_Width')
#         Cd_Height = self.get_var('Cut Down Height','Cd_Height')       
#         Stile_Cd = self.get_var('Stile Cut Down','Stile_Cd')
#         Rail_Cd = self.get_var('Rail Cut Down','Rail_Cd')
        
        rail_top = self.add_assembly((HIDDEN_FOLDER_NAME,CATEGORY_NAME,self.top_rail))
        rail_top.set_name("Top Rail")
        rail_top.x_loc('IF(Width>0,Width-(St_Wd-P_Wd),-(St_Wd-P_Wd))',[Width,St_Wd,P_Wd])   
        rail_top.z_loc('Height',[Height])
        rail_top.x_rot(value = 90)
        rail_top.y_rot(value = -180)
        rail_top.x_dim('IF(Width>0,Width-(St_Wd*2)+(P_Wd*2),-Width-(St_Wd*2)+(P_Wd*2))',[Width,St_Wd,P_Wd])
        rail_top.y_dim('Tr_Height',[Tr_Height]) 
        rail_top.prompt("Hide",'OR(abs(Width)<abs(Min_Width),abs(Height)<abs(Min_Height))',[Width,Height,Min_Width,Min_Height])
               
        rail_bottom = self.add_assembly((HIDDEN_FOLDER_NAME,CATEGORY_NAME,self.bottom_rail))
        rail_bottom.set_name("Bottom Rail")
        rail_bottom.x_loc('IF(Width>0,(St_Wd-P_Wd),Width+(St_Wd-P_Wd))',[Width,St_Wd,P_Wd])   
        rail_bottom.x_rot(value = 90)
        rail_bottom.x_dim('IF(Width>0,Width-(St_Wd*2)+(P_Wd*2),-Width-(St_Wd*2)+(P_Wd*2))',[Width,St_Wd,P_Wd])
        rail_bottom.y_dim('Br_Height',[Br_Height]) 
        rail_bottom.prompt("Hide",'OR(abs(Width)<abs(Min_Width),abs(Height)<abs(Min_Height))',[Width,Height,Min_Width,Min_Height])     
        
        stile_left = self.add_assembly((HIDDEN_FOLDER_NAME,CATEGORY_NAME,self.stile))
        stile_left.set_name("Left Stile")
        stile_left.x_loc('IF(Width<0,Width,0)',[Width])
        stile_left.y_loc(value = fd.inches(-0.75))
        stile_left.x_rot(value = -90)
        stile_left.y_rot(value = -90)
        stile_left.x_dim('Height',[Height])
        stile_left.y_dim('St_Wd',[St_Wd])
        stile_left.z_dim('Depth',[Depth])
        stile_left.prompt("Top Profile Gap",'Tr_Height-P_Wd',[Tr_Height,P_Wd])
        stile_left.prompt("Bottom Profile Gap",'Br_Height-P_Wd',[Br_Height,P_Wd])
        stile_left.prompt("Hide",'OR(abs(Width)<abs(Min_Width),abs(Height)<abs(Min_Height))',[Width,Height,Min_Width,Min_Height])
        
        stile_right = self.add_assembly((HIDDEN_FOLDER_NAME,CATEGORY_NAME,self.stile))
        stile_right.set_name("Left Stile")
        stile_right.x_loc('IF(Width>0,Width,0)',[Width])
        stile_right.y_rot(value = -90)
        stile_right.z_rot(value = 90)
        stile_right.x_dim('Height',[Height])
        stile_right.y_dim('St_Wd',[St_Wd])
        stile_right.z_dim('Depth',[Depth])  
        stile_right.prompt("Top Profile Gap",'Tr_Height-P_Wd',[Tr_Height,P_Wd])
        stile_right.prompt("Bottom Profile Gap",'Br_Height-P_Wd',[Br_Height,P_Wd])
        stile_right.prompt("Hide",'OR(abs(Width)<abs(Min_Width),abs(Height)<abs(Min_Height))',[Width,Height,Min_Width,Min_Height])
          
        panel = self.add_assembly((HIDDEN_FOLDER_NAME,CATEGORY_NAME,self.panel))
        panel.set_name("Panel")
        panel.x_loc('IF(Width>0,Width-St_Wd+Pan_Ovlp,-St_Wd+Pan_Ovlp)',[Width,St_Wd,Pan_Ovlp])
        panel.y_loc(value = fd.inches(-0.25))
        panel.z_loc('INCH(2.5)-Pan_Ovlp',[Pan_Ovlp])
        panel.y_rot(value = -90)
        panel.z_rot(value = 90)
        panel.x_dim('Height-INCH(5)+(Pan_Ovlp*2)',[Height,Pan_Ovlp]) 
        panel.y_dim('IF(Width>0,Width-(St_Wd*2)+(Pan_Ovlp*2),-Width-(St_Wd*2)+(Pan_Ovlp*2))',[Width,St_Wd,Pan_Ovlp])
        panel.prompt("Hide",'IF(M_Door,True,OR(abs(Width)<abs(Min_Width),abs(Height)<abs(Min_Height)))',[Width,Height,Min_Width,Min_Height,M_Door])
        
        min_width_replacement = self.add_assembly((HIDDEN_FOLDER_NAME,CATEGORY_NAME,"Slab_Door"))
        min_width_replacement.set_name("Min Width Replacement - " + self.min_width_replacement)
        min_width_replacement.x_loc('IF(Width>0,Width,0)',[Width])
        min_width_replacement.x_rot(value = 90)
        min_width_replacement.y_rot(value = -90)
        min_width_replacement.x_dim("Height",[Height]) 
        min_width_replacement.y_dim('IF(Width>0,Width,-Width)',[Width])
        min_width_replacement.prompt("Hide",'abs(Width)>abs(Min_Width)',[Width,Min_Width])
        
        min_height_replacement = self.add_assembly((HIDDEN_FOLDER_NAME,CATEGORY_NAME,"Slab_Door"))
        min_height_replacement.set_name("Min Height Replacement - " + self.min_height_replacement)
        min_height_replacement.x_loc('IF(Width>0,0,Width)',[Width])
        min_height_replacement.x_rot(value = 90)
        min_height_replacement.x_dim('IF(Width>0,Width,-Width)',[Width])
        min_height_replacement.y_dim("Height",[Height])       
        min_height_replacement.prompt("Hide",'Height>Min_Height',[Height,Min_Height])        
        
        mullion = self.add_assembly((HIDDEN_FOLDER_NAME,CATEGORY_NAME,self.mullion))
        mullion.set_name("Mullion Insert")
        mullion.x_loc('IF(Width>0,St_Wd-P_Wd,Width+(St_Wd-P_Wd))',[Width,St_Wd,P_Wd])
        mullion.y_loc("-Depth",[Depth])
        mullion.z_loc(value = fd.inches(1.96875))
        mullion.x_dim("abs(Width)-INCH(3.9375)",[Width])
        mullion.z_dim("Height-INCH(3.9375)",[Height])
        mullion.prompt("Hide","IF(M_Door==False,True,OR(abs(Width)<abs(Min_Width),abs(Height)<abs(Min_Height)))",[M_Door,Width,Height,Min_Width,Min_Height])        
        mullion.prompt("Num Horizontal Mullion","IF(Height>INCH(26),2,1)*IF(abs(Width)>INCH(14),2,1)",[Height,Width])       
        mullion.prompt("Num Vertical Mullion","IF(abs(Width)<INCH(14),0,1)",[Width])   
               
        self.update()
    
class PRODUCT_American(Cabinet_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_cabinet_doors
        self.category_name = "Cabinet Doors"
        self.assembly_name = "American"
        self.width = fd.inches(18)
        self.height = fd.inches(24)
        self.depth = fd.inches(0.75)
        
        self.panel = "Panel_Raised_Smooth"
        self.stile = "Stile_ACEH-18"
        self.stile_width = fd.inches(2.5)
        self.top_rail = "Rail_ACEH_Standard-18" 
        self.top_rail_height = fd.inches(2.5)
        self.bottom_rail = "Rail_ACEH_Standard-18" 
        self.bottom_rail_height = fd.inches(2.5)
        self.mullion = "Mullion_ACEH"
        
        self.min_width = fd.inches(6.8125)
        self.min_width_replacement = "Slab_Door"
        self.min_height = fd.inches(5.6875)
        self.min_height_replacement = "Slab_Door"         
      
class PRODUCT_Imperial(Cabinet_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_cabinet_doors
        self.category_name = "Cabinet Doors"
        self.assembly_name = "Imperial"
        self.width = fd.inches(18)
        self.height = fd.inches(24)
        self.depth = fd.inches(0.75)
        
        self.panel = "Panel_Raised_Smooth_Cathedral"
        self.stile = "Stile_ACEH-18"
        self.stile_width = fd.inches(2.5)
        self.top_rail = "Rail_ACEH_Cathedral-18" 
        self.top_rail_height = fd.inches(4)
        self.bottom_rail = "Rail_ACEH_Standard-18" 
        self.bottom_rail_height = fd.inches(2.5)
        self.mullion = "Mullion_ACEH"
               
        self.min_width = fd.inches(8.75)
        self.min_width_replacement = "Slab_Door"#AM
        self.min_height = fd.inches(5.6875)
        self.min_height_replacement = "Slab_Door"         
                 
class PRODUCT_Sentinel(Cabinet_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_cabinet_doors
        self.category_name = "Cabinet Doors"
        self.assembly_name = "Sentinel"
        self.width = fd.inches(18)
        self.height = fd.inches(24)
        self.depth = fd.inches(0.75)
        
        self.panel = "Panel_Raised_Smooth_Arched"
        self.stile = "Stile_ACEH-18"
        self.stile_width = fd.inches(2.5)
        self.top_rail = "Rail_ACEH_Arched-18" 
        self.top_rail_height = fd.inches(4)
        self.bottom_rail = "Rail_ACEH_Standard-18" 
        self.bottom_rail_height = fd.inches(2.5)
        self.mullion = "Mullion_ACEH"
        
        self.min_width = fd.inches(8.75)
        self.min_width_replacement = "Slab_Door"#AM
        self.min_height = fd.inches(5.6875)
        self.min_height_replacement = "Slab_Door"         
               
class PRODUCT_Prestige(Cabinet_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_cabinet_doors
        self.category_name = "Cabinet Doors"
        self.assembly_name = "Prestige"
        self.width = fd.inches(18)
        self.height = fd.inches(24)
        self.depth = fd.inches(0.75)
        
        self.panel = "Panel_Raised_Smooth_Dbl_Cathedral"
        self.stile = "Stile_ACEH-18"
        self.stile_width = fd.inches(2.5)
        self.top_rail = "Rail_ACEH_Cathedral-18" 
        self.top_rail_height = fd.inches(4)
        self.bottom_rail = "Rail_ACEH_Cathedral-18" 
        self.bottom_rail_height = fd.inches(4)
        self.mullion = "Mullion_ACEH"
        
        self.min_width = fd.inches(8.75)
        self.min_width_replacement = "Slab_Door"
        self.min_height = fd.inches(14.125)
        self.min_height_replacement = "Slab_Door"            
        
class PRODUCT_Regency(Cabinet_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_cabinet_doors
        self.category_name = "Cabinet Doors"
        self.assembly_name = "Regency"
        self.width = fd.inches(18)
        self.height = fd.inches(24)
        self.depth = fd.inches(0.75)
        
        self.panel = "Panel_Raised_Smooth_Dbl_Arched"
        self.stile = "Stile_ACEH-18"
        self.stile_width = fd.inches(2.5)
        self.top_rail = "Rail_ACEH_Arched-18" 
        self.top_rail_height = fd.inches(4)
        self.bottom_rail = "Rail_ACEH_Arched-18" 
        self.bottom_rail_height = fd.inches(4)
        self.mullion = "Mullion_ACEH"
        
        self.min_width = fd.inches(8.75)
        self.min_width_replacement = "Slab_Door"
        self.min_height = fd.inches(14.125)
        self.min_height_replacement = "Slab_Door"          
        
class PRODUCT_Richmond(Cabinet_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_cabinet_doors
        self.category_name = "Cabinet Doors"
        self.assembly_name = "Richmond"
        self.width = fd.inches(18)
        self.height = fd.inches(24)
        self.depth = fd.inches(0.75)
        
        self.panel = "Panel_Raised_Smooth"
        self.stile = "Stile_ACEH-18"
        self.stile_width = fd.inches(2.5)
        self.top_rail = "Rail_ACEH_Standard-18" 
        self.top_rail_height = fd.inches(2.5)
        self.bottom_rail = "Rail_ACEH_Standard-18" 
        self.bottom_rail_height = fd.inches(2.5)
        self.mullion = "Mullion_ACEH"
        
        self.min_width = fd.inches(6.8125)
        self.min_width_replacement = "Slab_Door"
        self.min_height = fd.inches(5.6875)
        self.min_height_replacement = "Slab_Door"         
        
# class PRODUCT_Banbury(Cabinet_Door): BUILD MID STILE/RAIL
#     
#     def __init__(self):
#         g = bpy.context.scene.lm_cabinet_doors
#         self.category_name = "Cabinet Doors"
#         self.assembly_name = "Banbury"
#         self.width = fd.inches(18)
#         self.height = fd.inches(24)
#         self.depth = fd.inches(0.75)
#         
#         self.panel = "Panel_Raised_Smooth"
#         self.stile = "Stile_ACEH-18"
#         
#         self.top_rail = "Rail_ACEH_Standard-18" 
#         self.top_rail_height = fd.inches(2.5)
#         self.bottom_rail = "Rail_ACEH_Standard-18" 
#         self.bottom_rail_height = fd.inches(2.5)
#         self.mullion = "Mullion_ACEH"
#         
#         self.min_width = fd.inches(6.8125)
#         self.min_width_replacement = "Slab_Door"
#         self.min_height = fd.inches(5.6875)
#         self.min_height_replacement = "Slab_Door"         
        
# class PRODUCT_Dynasty(Cabinet_Door): BUILD MID STILE/RAIL
#     
#     def __init__(self):
#         g = bpy.context.scene.lm_cabinet_doors
#         self.category_name = "Cabinet Doors"
#         self.assembly_name = "Dynasty"
#         self.width = fd.inches(18)
#         self.height = fd.inches(24)
#         self.depth = fd.inches(0.75)
#         
#         self.panel = "Panel_Raised_Smooth"
#         self.stile = "Stile_ACEH-18"
#         
#         self.top_rail = "Rail_ACEH_Standard-18" 
#         self.top_rail_height = fd.inches(2.5)
#         self.bottom_rail = "Rail_ACEH_Standard-18" 
#         self.bottom_rail_height = fd.inches(2.5)
#         self.mullion = "Mullion_ACEH"
#         
#         self.min_width = fd.inches(6.8125)
#         self.min_width_replacement = "Slab_Door"
#         self.min_height = fd.inches(5.6875)
#         self.min_height_replacement = "Slab_Door"        
        
class PRODUCT_Yorktown(Cabinet_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_cabinet_doors
        self.category_name = "Cabinet Doors"
        self.assembly_name = "Yorktown"
        self.width = fd.inches(18)
        self.height = fd.inches(24)
        self.depth = fd.inches(0.75)
        
        self.panel = "Panel_Raised_Smooth"
        self.stile = "Stile_BDF-18"
        self.stile_width = fd.inches(2.5)
        self.top_rail = "Rail_BDF_Standard-18" 
        self.top_rail_height = fd.inches(2.5)
        self.bottom_rail = "Rail_BDF_Standard-18" 
        self.bottom_rail_height = fd.inches(2.5)
        self.mullion = "Mullion_BDF"
        
        self.min_width = fd.inches(6.8125)
        self.min_width_replacement = "Slab_Door"
        self.min_height = fd.inches(5.6875)
        self.min_height_replacement = "Slab_Door"           
        
class PRODUCT_Concord(Cabinet_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_cabinet_doors
        self.category_name = "Cabinet Doors"
        self.assembly_name = "Concord"
        self.width = fd.inches(18)
        self.height = fd.inches(24)
        self.depth = fd.inches(0.75)
        
        self.panel = "Panel_Raised_Smooth_Arched"
        self.stile = "Stile_BDF-18"
        self.stile_width = fd.inches(2.5)
        self.top_rail = "Rail_BDF_Arched-18" 
        self.top_rail_height = fd.inches(4)
        self.bottom_rail = "Rail_BDF_Standard-18" 
        self.bottom_rail_height = fd.inches(2.5)
        self.mullion = "Mullion_BDF"
        
        self.min_width = fd.inches(8.75)
        self.min_width_replacement = "Slab_Door"
        self.min_height = fd.inches(5.6875)
        self.min_height_replacement = "Slab_Door"         
        
class PRODUCT_Trenton(Cabinet_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_cabinet_doors
        self.category_name = "Cabinet Doors"
        self.assembly_name = "Trenton"
        self.width = fd.inches(18)
        self.height = fd.inches(24)
        self.depth = fd.inches(0.75)
        
        self.panel = "Panel_Raised_Beaded"
        self.stile = "Stile_ACEH-18"
        self.stile_width = fd.inches(2.5)
        self.top_rail = "Rail_ACEH_Standard-18" 
        self.top_rail_height = fd.inches(2.5)
        self.bottom_rail = "Rail_ACEH_Standard-18" 
        self.bottom_rail_height = fd.inches(2.5)
        self.mullion = "Mullion_ACEH"
        
        self.min_width = fd.inches(6.8125)
        self.min_width_replacement = "Slab_Door"
        self.min_height = fd.inches(5.6875)
        self.min_height_replacement = "Slab_Door"          
        
class PRODUCT_Dover(Cabinet_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_cabinet_doors
        self.category_name = "Cabinet Doors"
        self.assembly_name = "Dover"
        self.width = fd.inches(18)
        self.height = fd.inches(24)
        self.depth = fd.inches(0.75)
        
        self.panel = "Panel_Raised_Beaded_Cathedral"
        self.stile = "Stile_ACEH-18"
        self.stile_width = fd.inches(2.5)
        self.top_rail = "Rail_ACEH_Cathedral-18" 
        self.top_rail_height = fd.inches(4)
        self.bottom_rail = "Rail_ACEH_Standard-18" 
        self.bottom_rail_height = fd.inches(2.5)
        self.mullion = "Mullion_ACEH"
        
        self.min_width = fd.inches(8.75)
        self.min_width_replacement = "Slab_Door"
        self.min_height = fd.inches(14.125)
        self.min_height_replacement = "Slab_Door"          
        
class PRODUCT_Plymouth(Cabinet_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_cabinet_doors
        self.category_name = "Cabinet Doors"
        self.assembly_name = "Plymouth"
        self.width = fd.inches(18)
        self.height = fd.inches(24)
        self.depth = fd.inches(0.75)
        
        self.panel = "Panel_Raised_Beaded_Dbl_Cathedral"
        self.stile = "Stile_ACEH-18"
        self.stile_width = fd.inches(2.5)
        self.top_rail = "Rail_ACEH_Cathedral-18" 
        self.top_rail_height = fd.inches(4)
        self.bottom_rail = "Rail_ACEH_Cathedral-18" 
        self.bottom_rail_height = fd.inches(4)
        self.mullion = "Mullion_ACEH"
        
        self.min_width = fd.inches(8.75)
        self.min_width_replacement = "Slab_Door"
        self.min_height = fd.inches(14.125)
        self.min_height_replacement = "Slab_Door"         
        
class PRODUCT_Almont(Cabinet_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_cabinet_doors
        self.category_name = "Cabinet Doors"
        self.assembly_name = "Almont"
        self.width = fd.inches(18)
        self.height = fd.inches(24)
        self.depth = fd.inches(0.75)
        
        self.panel = "Panel_Raised_Beaded"
        self.stile = "Stile_ACEH-18"
        self.stile_width = fd.inches(2.5)
        self.top_rail = "Rail_ACEH_Standard-18" 
        self.top_rail_height = fd.inches(2.5)
        self.bottom_rail = "Rail_ACEH_Standard-18" 
        self.bottom_rail_height = fd.inches(2.5)
        self.mullion = "Mullion_ACEH"
        
        self.min_width = fd.inches(6.8125)
        self.min_width_replacement = "Slab_Door"
        self.min_height = fd.inches(5.6875)
        self.min_height_replacement = "Slab_Door"           
    
class PRODUCT_Farmington(Cabinet_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_cabinet_doors
        self.category_name = "Cabinet Doors"
        self.assembly_name = "Farmington"
        self.width = fd.inches(18)
        self.height = fd.inches(24)
        self.depth = fd.inches(0.75)
        
        self.panel = "Panel_Raised_Beaded"
        self.stile = "Stile_BDF-18"
        self.stile_width = fd.inches(2.5)
        self.top_rail = "Rail_BDF_Standard-18" 
        self.top_rail_height = fd.inches(2.5)
        self.bottom_rail = "Rail_BDF_Standard-18" 
        self.bottom_rail_height = fd.inches(2.5)
        self.mullion = "Mullion_BDF"
        
        self.min_width = fd.inches(6.8125)
        self.min_width_replacement = "Slab_Door"
        self.min_height = fd.inches(5.6875)
        self.min_height_replacement = "Slab_Door"     

class PRODUCT_Shelburne(Cabinet_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_cabinet_doors
        self.category_name = "Cabinet Doors"
        self.assembly_name = "Shelburne"
        self.width = fd.inches(18)
        self.height = fd.inches(24)
        self.depth = fd.inches(0.75)
        
        self.panel = "Panel_Raised_Beaded_Cathedral"
        self.stile = "Stile_BDF-18"
        self.stile_width = fd.inches(2.5)
        self.top_rail = "Rail_BDF_Cathedral-18" 
        self.top_rail_height = fd.inches(4)
        self.bottom_rail = "Rail_BDF_Standard-18" 
        self.bottom_rail_height = fd.inches(2.5)
        self.mullion = "Mullion_BDF"
        
        self.min_width = fd.inches(8.75)
        self.min_width_replacement = "Slab_Door"
        self.min_height = fd.inches(5.6875)
        self.min_height_replacement = "Slab_Door"
        
class PRODUCT_Windsor(Cabinet_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_cabinet_doors
        self.category_name = "Cabinet Doors"
        self.assembly_name = "Windsor"
        self.width = fd.inches(18)
        self.height = fd.inches(24)
        self.depth = fd.inches(0.75)
        
        self.panel = "Panel_Raised_Beaded_Arched"
        self.stile = "Stile_BDF-18"
        self.stile_width = fd.inches(2.5)
        self.top_rail = "Rail_BDF_Arched-18" 
        self.top_rail_height = fd.inches(4)
        self.bottom_rail = "Rail_BDF_Standard-18" 
        self.bottom_rail_height = fd.inches(2.5)
        self.mullion = "Mullion_BDF"
        
        self.min_width = fd.inches(8.75)
        self.min_width_replacement = "Slab_Door"
        self.min_height = fd.inches(5.6875)
        self.min_height_replacement = "Slab_Door"        
        
class PRODUCT_Groveland(Cabinet_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_cabinet_doors
        self.category_name = "Cabinet Doors"
        self.assembly_name = "Groveland"
        self.width = fd.inches(18)
        self.height = fd.inches(24)
        self.depth = fd.inches(0.75)
        
        self.panel = "Panel_Flat"
        self.stile = "Stile_GI-18"
        self.stile_width = fd.inches(2.5)
        self.top_rail = "Rail_GI_Standard-18" 
        self.top_rail_height = fd.inches(2.5)
        self.bottom_rail = "Rail_GI_Standard-18" 
        self.bottom_rail_height = fd.inches(2.5)
        self.mullion = "Mullion_GI"
        
        self.min_width = fd.inches(6.8125)
        self.min_width_replacement = "Slab_Door"
        self.min_height = fd.inches(5.6875)
        self.min_height_replacement = "Slab_Door"         
        
class PRODUCT_Lexington(Cabinet_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_cabinet_doors
        self.category_name = "Cabinet Doors"
        self.assembly_name = "Lexington"
        self.width = fd.inches(18)
        self.height = fd.inches(24)
        self.depth = fd.inches(0.75)
        
        self.panel = "Panel_Flat"
        self.stile = "Stile_ACEH-18"
        self.stile_width = fd.inches(2.5)
        self.top_rail = "Rail_ACEH_Standard-18" 
        self.top_rail_height = fd.inches(2.5)
        self.bottom_rail = "Rail_ACEH_Standard-18"     
        self.bottom_rail_height = fd.inches(2.5)    
        self.mullion = "Mullion_ACEH"
        
        self.min_width = fd.inches(6.8125)
        self.min_width_replacement = "Slab_Door"
        self.min_height = fd.inches(5.6875)
        self.min_height_replacement = "Slab_Door"
        
class PRODUCT_Heritage(Cabinet_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_cabinet_doors
        self.category_name = "Cabinet Doors"
        self.assembly_name = "Heritage"
        self.width = fd.inches(18)
        self.height = fd.inches(24)
        self.depth = fd.inches(0.75)
        
        self.panel = "Panel_Flat"
        self.stile = "Stile_ACEH-18"
        self.stile_width = fd.inches(2.5)
        self.top_rail = "Rail_ACEH_Cathedral-18" 
        self.top_rail_height = fd.inches(4)
        self.bottom_rail = "Rail_ACEH_Standard-18"   
        self.bottom_rail_height = fd.inches(2.5)      
        self.mullion = "Mullion_ACEH"
        
        self.min_width = fd.inches(6.8125)
        self.min_width_replacement = "Slab_Door"
        self.min_height = fd.inches(5.6875)
        self.min_height_replacement = "Slab_Door"        
        
class PRODUCT_Royalty(Cabinet_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_cabinet_doors
        self.category_name = "Cabinet Doors"
        self.assembly_name = "Royalty"
        self.width = fd.inches(18)
        self.height = fd.inches(24)
        self.depth = fd.inches(0.75)
        
        self.panel = "Panel_Flat"
        self.stile = "Stile_ACEH-18"
        self.stile_width = fd.inches(2.5)
        self.top_rail = "Rail_ACEH_Cathedral-18" 
        self.top_rail_height = fd.inches(4)
        self.bottom_rail = "Rail_ACEH_Cathedral-18"   
        self.bottom_rail_height = fd.inches(4)      
        self.mullion = "Mullion_ACEH"
        
        self.min_width = fd.inches(6.8125)
        self.min_width_replacement = "Slab_Door"
        self.min_height = fd.inches(5.6875)
        self.min_height_replacement = "Slab_Door"         
        
class PRODUCT_Century(Cabinet_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_cabinet_doors
        self.category_name = "Cabinet Doors"
        self.assembly_name = "Century"
        self.width = fd.inches(18)
        self.height = fd.inches(24)
        self.depth = fd.inches(0.75)
        
        self.panel = "Panel_Flat"
        self.stile = "Stile_ACEH-18"
        self.stile_width = fd.inches(2.5)
        self.top_rail = "Rail_ACEH_Arched-18" 
        self.top_rail_height = fd.inches(4)
        self.bottom_rail = "Rail_ACEH_Standard-18"   
        self.bottom_rail_height = fd.inches(2.5)      
        self.mullion = "Mullion_ACEH"
        
        self.min_width = fd.inches(6.8125)
        self.min_width_replacement = "Slab_Door"
        self.min_height = fd.inches(5.6875)
        self.min_height_replacement = "Slab_Door"         
        
class PRODUCT_Liberty(Cabinet_Door):
    
    def __init__(self):
        g = bpy.context.scene.lm_cabinet_doors
        self.category_name = "Cabinet Doors"
        self.assembly_name = "Liberty"
        self.width = fd.inches(18)
        self.height = fd.inches(24)
        self.depth = fd.inches(0.75)
        
        self.panel = "Panel_Flat"
        self.stile = "Stile_ACEH-18"
        self.stile_width = fd.inches(2.5)
        self.top_rail = "Rail_ACEH_Arched-18" 
        self.top_rail_height = fd.inches(4)
        self.bottom_rail = "Rail_ACEH_Arched-18"   
        self.bottom_rail_height = fd.inches(4)      
        self.mullion = "Mullion_ACEH"
        
        self.min_width = fd.inches(6.8125)
        self.min_width_replacement = "Slab_Door"
        self.min_height = fd.inches(5.6875)
        self.min_height_replacement = "Slab_Door"         
        
class PROMPTS_Cabinet_Door_Prompts(bpy.types.Operator):
    bl_idname = "cabinetlib.cabinet_door_prompts"
    bl_label = "Cabinet Door Prompts" 
    bl_options = {'UNDO'}
    
    object_name = bpy.props.StringProperty(name="Object Name")
    
    product = None
    
    width = bpy.props.FloatProperty(name="Width",unit='LENGTH',precision=4)
    height = bpy.props.FloatProperty(name="Height",unit='LENGTH',precision=4)
    depth = bpy.props.FloatProperty(name="Depth",unit='LENGTH',precision=4)

    array_x = bpy.props.IntProperty(name="Array X",min=0,)
    
    array_x_offset = bpy.props.FloatProperty(name="Array X Offset",unit='LENGTH',precision=4)
    
    array_x_prompt = None
    
    array_x_offset_prompt = None
    
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
            
        if self.array_x_prompt:
            self.array_x_prompt.set_value(self.array_x)
            
        if self.array_x_offset_prompt:
            self.array_x_offset_prompt.set_value(self.array_x_offset)                    
             
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
            
            self.array_x_prompt = self.product.get_prompt("Array X")
            self.array_x = self.array_x_prompt.value()
            
            self.array_x_offset_prompt = self.product.get_prompt("Array X Offset")
            self.array_x_offset = self.array_x_offset_prompt.value()          
                
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
            array_x = self.product.get_prompt("Array X")
            array_x_offset = self.product.get_prompt("Array X Offset")
            
            box = layout.box()
            box.label("Main Options:")
            
            col = box.column()
            row = col.row(align=True)
            row.label("Array X:")
            row.prop(self,'array_x',text="",)   
            row = col.row(align=True)                
            row.label("Array X Offset:")
            row.prop(self, 'array_x_offset',text="")           
    
    def draw_product_placment(self,layout):
        box = layout.box()
        col = box.column()
        row = col.row(align=True)
        row.label('Location X:')
        row.prop(self.product.obj_bp,'location',index=0,text="")
        row = col.row(align=True)
        row.label('Location Z:')        
        row.prop(self.product.obj_bp,'location',index=2,text="")

    def draw(self, context):
        layout = self.layout
        if self.product.obj_bp:
            if self.product.obj_bp.name in context.scene.objects:
                box = layout.box()
                
                split = box.split(percentage=.8)
                split.label(self.product.obj_bp.mv.name_object,icon='LATTICE_DATA')
                
                self.draw_product_size(box)
                self.draw_product_placment(box)    
                self.draw_product_prompts(box)    
        
def register():
    bpy.utils.register_class(Scene_Variables)
    bpy.types.Scene.lm_cabinet_doors = bpy.props.PointerProperty(type = Scene_Variables)
    bpy.utils.register_class(PROMPTS_Cabinet_Door_Prompts)
    
def unregister():
    bpy.utils.unregister_class(Scene_Variables)
    bpy.utils.unregister_class(PROMPTS_Cabinet_Door_Prompts)          
