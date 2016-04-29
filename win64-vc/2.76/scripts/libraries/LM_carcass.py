"""
Microvellum 
Carcass
Stores the construction logic for the different types of carcasses that are available
in the frameless and face frame library
"""

import bpy
import fd
import LM_machining

HIDDEN_FOLDER_NAME = "_HIDDEN"
NOTCHED_SIDE = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Cut Parts","Notched Side")
PART_WITH_FRONT_EDGEBANDING = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Cut Parts","Part with Front Edgebanding")
PART_WITH_NO_EDGEBANDING = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Cut Parts","Part with No Edgebanding")
PART_WITH_FRONT_AND_BOTTOM_EDGEBANDING = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Cut Parts","Part with Front and Bottom Edgebanding")
PART_WITH_EDGEBANDGING = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Cut Parts","Part with Edgebanding")
LEG_LEVELERS = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Hardware","Leg Levelers")
CHAMFERED_PART = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Cut Parts","Chamfered Part")
CORNER_NOTCH_PART = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Cut Parts","Corner Notch Part")
TRANSITION_PART = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Cut Parts","Transition Part with Front Edgebanding")
BENDING_PART = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Cut Parts","Bending Part")
RADIUS_CORNER_PART_WITH_EDGEBANDING = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Cut Parts","Radius Corner Part with Edgebanding")

EXPOSED_CABINET_MATERIAL = ("Plastics","White Melamine")
UNEXPOSED_CABINET_MATERIAL = ("Wood","Wood Core","Particle Board")
SEMI_EXPOSED_CABINET_MATERIAL = ("Plastics","White Melamine")


class Material_Pointers():
    
    Exposed_Exterior_Surface = fd.Material_Pointer(EXPOSED_CABINET_MATERIAL)

    Exposed_Interior_Surface = fd.Material_Pointer(EXPOSED_CABINET_MATERIAL)

    Semi_Exposed_Surface = fd.Material_Pointer(SEMI_EXPOSED_CABINET_MATERIAL)
    
    Exposed_Exterior_Edge = fd.Material_Pointer(EXPOSED_CABINET_MATERIAL)

    Concealed_Surface = fd.Material_Pointer(UNEXPOSED_CABINET_MATERIAL)

    Concealed_Edge = fd.Material_Pointer(UNEXPOSED_CABINET_MATERIAL)

class Cutpart_Pointers():
    
    Base_Side = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                core="Concealed_Surface",
                                top="Concealed_Surface",
                                bottom="Semi_Exposed_Surface")

    Base_Side_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                     core="Concealed_Surface",
                                     top="Concealed_Surface",
                                     bottom="Exposed_Interior_Surface")

    Sink_Side = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                core="Concealed_Surface",
                                top="Concealed_Surface",
                                bottom="Semi_Exposed_Surface")

    Sink_Side_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                     core="Concealed_Surface",
                                     top="Concealed_Surface",
                                     bottom="Exposed_Interior_Surface")
    
    Tall_Side = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                core="Concealed_Surface",
                                top="Concealed_Surface",
                                bottom="Semi_Exposed_Surface")

    Tall_Side_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                     core="Concealed_Surface",
                                     top="Concealed_Surface",
                                     bottom="Exposed_Interior_Surface")
    
    Upper_Side = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                 core="Concealed_Surface",
                                 top="Concealed_Surface",
                                 bottom="Semi_Exposed_Surface")

    Upper_Side_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                      core="Concealed_Surface",
                                      top="Concealed_Surface",
                                      bottom="Exposed_Interior_Surface")
    
    Suspended_Side = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                     core="Concealed_Surface",
                                     top="Concealed_Surface",
                                     bottom="Semi_Exposed_Surface")

    Suspended_Side_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                          core="Concealed_Surface",
                                          top="Concealed_Surface",
                                          bottom="Exposed_Interior_Surface")
    
    Base_Side_FE = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                   core="Concealed_Surface",
                                   top="Exposed_Exterior_Surface",
                                   bottom="Semi_Exposed_Surface")

    Base_Side_FE_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                        core="Concealed_Surface",
                                        top="Exposed_Exterior_Surface",
                                        bottom="Exposed_Interior_Surface")
    
    Sink_Side_FE = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                   core="Concealed_Surface",
                                   top="Exposed_Exterior_Surface",
                                   bottom="Semi_Exposed_Surface")

    Sink_Side_FE_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                        core="Concealed_Surface",
                                        top="Exposed_Exterior_Surface",
                                        bottom="Exposed_Interior_Surface")
    
    Tall_Side_FE = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                   core="Concealed_Surface",
                                   top="Exposed_Exterior_Surface",
                                   bottom="Semi_Exposed_Surface")

    Tall_Side_FE_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                        core="Concealed_Surface",
                                        top="Exposed_Exterior_Surface",
                                        bottom="Exposed_Interior_Surface")
    
    Upper_Side_FE = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                    core="Concealed_Surface",
                                    top="Exposed_Exterior_Surface",
                                    bottom="Semi_Exposed_Surface")

    Upper_Side_FE_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                         core="Concealed_Surface",
                                         top="Exposed_Exterior_Surface",
                                         bottom="Exposed_Interior_Surface")
    
    Suspended_Side_FE = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                        core="Concealed_Surface",
                                        top="Exposed_Exterior_Surface",
                                        bottom="Semi_Exposed_Surface")

    Suspended_Side_FE_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                             core="Concealed_Surface",
                                             top="Exposed_Exterior_Surface",
                                             bottom="Exposed_Interior_Surface")
    
    Base_Back = fd.Cutpart_Pointer(thickness=fd.inches(.25),
                                core="Concealed_Surface",
                                top="Concealed_Surface",
                                bottom="Semi_Exposed_Surface")

    Base_Back_Open = fd.Cutpart_Pointer(thickness=fd.inches(.25),
                                     core="Concealed_Surface",
                                     top="Concealed_Surface",
                                     bottom="Exposed_Interior_Surface")
    
    Sink_Back = fd.Cutpart_Pointer(thickness=fd.inches(.25),
                                core="Concealed_Surface",
                                top="Concealed_Surface",
                                bottom="Semi_Exposed_Surface")

    Sink_Back_Open = fd.Cutpart_Pointer(thickness=fd.inches(.25),
                                     core="Concealed_Surface",
                                     top="Concealed_Surface",
                                     bottom="Exposed_Interior_Surface")
    
    Tall_Back = fd.Cutpart_Pointer(thickness=fd.inches(.25),
                                core="Concealed_Surface",
                                top="Concealed_Surface",
                                bottom="Semi_Exposed_Surface")

    Tall_Back_Open = fd.Cutpart_Pointer(thickness=fd.inches(.25),
                                     core="Concealed_Surface",
                                     top="Concealed_Surface",
                                     bottom="Exposed_Interior_Surface")
    
    Upper_Back = fd.Cutpart_Pointer(thickness=fd.inches(.25),
                                 core="Concealed_Surface",
                                 top="Concealed_Surface",
                                 bottom="Semi_Exposed_Surface")

    Upper_Back_Open = fd.Cutpart_Pointer(thickness=fd.inches(.25),
                                      core="Concealed_Surface",
                                      top="Concealed_Surface",
                                      bottom="Exposed_Interior_Surface")
    
    Suspended_Back = fd.Cutpart_Pointer(thickness=fd.inches(.25),
                                     core="Concealed_Surface",
                                     top="Concealed_Surface",
                                     bottom="Semi_Exposed_Surface")

    Suspended_Back_Open = fd.Cutpart_Pointer(thickness=fd.inches(.25),
                                          core="Concealed_Surface",
                                          top="Concealed_Surface",
                                          bottom="Exposed_Interior_Surface")
    
    Base_Thick_Back = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                      core="Concealed_Surface",
                                      top="Concealed_Surface",
                                      bottom="Semi_Exposed_Surface")

    Base_Thick_Back_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                           core="Concealed_Surface",
                                           top="Concealed_Surface",
                                           bottom="Exposed_Interior_Surface")
    
    Sink_Thick_Back = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                      core="Concealed_Surface",
                                      top="Concealed_Surface",
                                      bottom="Semi_Exposed_Surface")

    Sink_Thick_Back_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                           core="Concealed_Surface",
                                           top="Concealed_Surface",
                                           bottom="Exposed_Interior_Surface")
    
    Tall_Thick_Back = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                      core="Concealed_Surface",
                                      top="Concealed_Surface",
                                      bottom="Semi_Exposed_Surface")

    Tall_Thick_Back_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                           core="Concealed_Surface",
                                           top="Concealed_Surface",
                                           bottom="Exposed_Interior_Surface")
    
    Upper_Thick_Back = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                       core="Concealed_Surface",
                                       top="Concealed_Surface",
                                       bottom="Semi_Exposed_Surface")

    Upper_Thick_Back_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                            core="Concealed_Surface",
                                            top="Concealed_Surface",
                                            bottom="Exposed_Interior_Surface")
      
    Suspended_Thick_Back = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                           core="Concealed_Surface",
                                           top="Concealed_Surface",
                                           bottom="Semi_Exposed_Surface")

    Suspended_Thick_Back_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                                core="Concealed_Surface",
                                                top="Concealed_Surface",
                                                bottom="Exposed_Interior_Surface")
    
    Base_Bottom = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                  core="Concealed_Surface",
                                  top="Concealed_Surface",
                                  bottom="Semi_Exposed_Surface")
    
    Base_Bottom_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                       core="Concealed_Surface",
                                       top="Concealed_Surface",
                                       bottom="Exposed_Interior_Surface")
    
    Sink_Bottom = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                  core="Concealed_Surface",
                                  top="Concealed_Surface",
                                  bottom="Semi_Exposed_Surface")
     
    Sink_Bottom_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                       core="Concealed_Surface",
                                       top="Concealed_Surface",
                                       bottom="Exposed_Interior_Surface")
    
    Tall_Bottom = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                  core="Concealed_Surface",
                                  top="Concealed_Surface",
                                  bottom="Semi_Exposed_Surface")

    Tall_Bottom_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                       core="Concealed_Surface",
                                       top="Concealed_Surface",
                                       bottom="Exposed_Interior_Surface")
    
    Upper_Bottom = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                   core="Concealed_Surface",
                                   top="Exposed_Exterior_Surface",
                                   bottom="Semi_Exposed_Surface")
    
    Upper_Bottom_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                        core="Concealed_Surface",
                                        top="Exposed_Exterior_Surface",
                                        bottom="Exposed_Interior_Surface")
    
    Suspended_Bottom = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                       core="Concealed_Surface",
                                       top="Concealed_Surface",
                                       bottom="Semi_Exposed_Surface")
    
    Suspended_Bottom_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                            core="Concealed_Surface",
                                            top="Concealed_Surface",
                                            bottom="Exposed_Interior_Surface")
    
    Base_Top = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                               core="Concealed_Surface",
                               top="Concealed_Surface",
                               bottom="Semi_Exposed_Surface")
    
    Base_Top_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                    core="Concealed_Surface",
                                    top="Concealed_Surface",
                                    bottom="Exposed_Interior_Surface")
    
    Sink_Top = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                               core="Concealed_Surface",
                               top="Concealed_Surface",
                               bottom="Semi_Exposed_Surface")
     
    Sink_Top_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                    core="Concealed_Surface",
                                    top="Concealed_Surface",
                                    bottom="Exposed_Interior_Surface")
    
    Tall_Top = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                               core="Concealed_Surface",
                               top="Concealed_Surface",
                               bottom="Semi_Exposed_Surface")

    Tall_Top_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                    core="Concealed_Surface",
                                    top="Concealed_Surface",
                                    bottom="Exposed_Interior_Surface")
    
    Upper_Top = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                core="Concealed_Surface",
                                top="Concealed_Surface",
                                bottom="Semi_Exposed_Surface")
     
    Upper_Top_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                     core="Concealed_Surface",
                                     top="Concealed_Surface",
                                     bottom="Exposed_Interior_Surface")
    
    Suspended_Top = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                    core="Concealed_Surface",
                                    top="Concealed_Surface",
                                    bottom="Semi_Exposed_Surface")
    
    Suspended_Top_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                         core="Concealed_Surface",
                                         top="Concealed_Surface",
                                         bottom="Exposed_Interior_Surface")
    
    Nailer = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                             core="Concealed_Surface",
                             top="Concealed_Surface",
                             bottom="Concealed_Surface")
    
    Toe_Kick = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                               core="Concealed_Surface",
                               top="Concealed_Surface",
                               bottom="Concealed_Surface")
    
    Filler = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                             core="Concealed_Surface",
                             top="Exposed_Exterior_Surface",
                             bottom="Concealed_Surface")
    
    Finger_Pull_Rail = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                       core="Concealed_Surface",
                                       top="Concealed_Surface",
                                       bottom="Exposed_Exterior_Surface")
    
    Valance = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                              core="Concealed_Surface",
                              top="Exposed_Exterior_Surface",
                              bottom="Concealed_Surface")
    
    Sink_Sub_Front = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                     core="Concealed_Surface",
                                     top="Exposed_Exterior_Surface",
                                     bottom="Concealed_Surface")
    
class Edgepart_Pointers():
    
    Cabinet_Body_Edges = fd.Edgepart_Pointer(thickness=fd.inches(.01),
                                          material="Exposed_Exterior_Edge")

    Cabinet_Body_Edges_Open = fd.Edgepart_Pointer(thickness=fd.inches(.01),
                                               material="Exposed_Exterior_Edge")
    
#---------ASSEMBLY INSTRUCTIONS
    
class Standard_Carcass(fd.Library_Assembly):
    
    library_name = "Carcasses"
    placement_type = ""
    type_assembly = "INSERT"
    
    carcass_type = "" # {Base, Tall, Upper, Sink, Suspended}
    open_name = ""
    
    remove_top = False # Used to remove top for face frame sink cabinets
    
    def add_common_carcass_prompts(self):
        g = bpy.context.scene.lm_carcass
        self.add_tab(name='Carcass Options',tab_type='VISIBLE')
        self.add_tab(name='Formulas',tab_type='HIDDEN')
        self.add_tab(name='Machining Options',tab_type='HIDDEN')
        self.add_prompt(name="Left Fin End",prompt_type='CHECKBOX',value=False,tab_index=0,export=True)
        self.add_prompt(name="Right Fin End",prompt_type='CHECKBOX',value=False,tab_index=0,export=True)
        self.add_prompt(name="Left Side Wall Filler",prompt_type='DISTANCE',value=0.0,tab_index=0,export=True)
        self.add_prompt(name="Right Side Wall Filler",prompt_type='DISTANCE',value=0.0,tab_index=0,export=True)
        self.add_prompt(name="Use Nailers",prompt_type='CHECKBOX',value= g.Use_Nailers,tab_index=0,export=True)
        self.add_prompt(name="Nailer Width",prompt_type='DISTANCE',value= g.Nailer_Width,tab_index=0,export=True)
        self.add_prompt(name="Center Nailer Switch",prompt_type='DISTANCE',value= g.Center_Nailer_Switch,tab_index=0)
        self.add_prompt(name="Use Thick Back",prompt_type='CHECKBOX',value= g.Use_Thick_Back,tab_index=0,export=True)
        self.add_prompt(name="Remove Back",prompt_type='CHECKBOX',value= g.Remove_Back,tab_index=0,export=True)
        self.add_prompt(name="Remove Bottom",prompt_type='CHECKBOX',value= False,tab_index=0,export=True)
        
        if self.carcass_type in {'Base','Suspended'} and not g.Use_Full_Tops:
            self.add_prompt(name="Stretcher Width",prompt_type='DISTANCE',value=g.Stretcher_Width,tab_index=0,export=True)
        
        self.add_prompt(name="Left Side Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Right Side Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Top Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Bottom Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Back Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Thick Back Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Filler Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Nailer Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Edgebanding Thickness",prompt_type='DISTANCE',value=fd.inches(.02),tab_index=1)
        self.add_prompt(name="Back Inset",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        self.add_prompt(name="Top Inset",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        self.add_prompt(name="Bottom Inset",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        
    def add_base_assembly_prompts(self):
        g = bpy.context.scene.lm_carcass
        self.add_prompt(name="Toe Kick Height",prompt_type='DISTANCE',value= g.Toe_Kick_Height,tab_index=0,export=True)
        self.add_prompt(name="Toe Kick Setback",prompt_type='DISTANCE',value= g.Toe_Kick_Setback,tab_index=0,export=True)
        self.add_prompt(name="Toe Kick Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        
    def add_valance_prompts(self,add_bottom_valance):
        g = bpy.context.scene.lm_carcass
        self.add_prompt(name="Valance Height Top",prompt_type='DISTANCE',value=g.Valance_Height_Top,tab_index=0,export=True)
        self.add_prompt(name="Door Valance Top",prompt_type='CHECKBOX',value=g.Door_Valance_Top,tab_index=0,export=True)
        if add_bottom_valance:
            self.add_prompt(name="Valance Height Bottom",prompt_type='DISTANCE',value=g.Valance_Height_Bottom,tab_index=0,export=True)
            self.add_prompt(name="Door Valance Bottom",prompt_type='CHECKBOX',value=g.Door_Valance_Bottom,tab_index=0,export=True)
        self.add_prompt(name="Left Side Full Height",prompt_type='CHECKBOX',value=False,tab_index=0,export=True)
        self.add_prompt(name="Right Side Full Height",prompt_type='CHECKBOX',value=False,tab_index=0,export=True)
        self.add_prompt(name="Valance Each Unit",prompt_type='CHECKBOX',value=g.Valance_Each_Unit,tab_index=0,export=True)
        self.add_prompt(name="Valance Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
    
    def add_sink_prompts(self):
        g = bpy.context.scene.lm_carcass
        self.add_prompt(name="Sub Front Height",prompt_type='DISTANCE',value= g.Sub_Front_Height,tab_index=0,export=True)
        self.add_prompt(name="Sub Front Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
    
    def add_prompt_formuls(self):
        sgi = self.get_var('cabinetlib.spec_group_index','sgi')
        tt = self.get_var("Top Thickness",'tt')
        bt = self.get_var("Bottom Thickness",'bt')
        use_nailers = self.get_var("Use Nailers",'use_nailers')
        nt = self.get_var("Nailer Thickness",'nt')
        bkt = self.get_var("Back Thickness",'bkt')
        tbkt = self.get_var("Thick Back Thickness",'tbkt')
        use_thick_back = self.get_var("Use Thick Back",'use_thick_back')
        remove_back = self.get_var("Remove Back",'remove_back')
        lfe = self.get_var("Left Fin End",'lfe')
        rfe = self.get_var("Right Fin End",'rfe')
        Remove_Bottom = self.get_var('Remove Bottom','Remove_Bottom')
        if self.carcass_type in {'Base','Sink','Tall'}:
            kick_height = self.get_var("Toe Kick Height",'kick_height')
        if self.carcass_type in {'Upper','Tall'}:
            vhb = self.get_var("Valance Height Bottom",'vhb')
            vht = self.get_var("Valance Height Top",'vht')

        Side_Pointer_Name = self.carcass_type + '_Side' + self.open_name
        FE_Pointer_Name = self.carcass_type + '_Side_FE' + self.open_name
        Top_Pointer_Name = self.carcass_type + '_Top' + self.open_name
        Bottom_Pointer_Name = self.carcass_type + '_Bottom' + self.open_name
        Back_Pointer_Name = self.carcass_type + '_Back' + self.open_name
        Thick_Back_Pointer_Name = self.carcass_type + '_Thick_Back' + self.open_name
        Edgebanding_Pointer_Name = 'Cabinet_Body_Edges' + self.open_name

        self.prompt('Left Side Thickness','IF(lfe,THICKNESS(sgi,"' + FE_Pointer_Name +'"),THICKNESS(sgi,"' + Side_Pointer_Name +'"))',[lfe,sgi])
        self.prompt('Right Side Thickness','IF(rfe,THICKNESS(sgi,"' + FE_Pointer_Name +'"),THICKNESS(sgi,"' + Side_Pointer_Name +'"))',[rfe,sgi])
        if self.carcass_type == "Sink" or self.remove_top:
            self.prompt('Top Thickness',value = 0)
        else:
            self.prompt('Top Thickness','THICKNESS(sgi,"' + Top_Pointer_Name +'")',[sgi])
        self.prompt('Bottom Thickness','THICKNESS(sgi,"' + Bottom_Pointer_Name +'")',[sgi])
        if self.carcass_type in {'Base','Sink','Tall'}:
            self.prompt('Toe Kick Thickness','THICKNESS(sgi,"Toe_Kick")',[sgi])
        if self.carcass_type == 'Sink':
            self.prompt('Sub Front Thickness','THICKNESS(sgi,"Sink_Sub_Front")',[sgi])
        self.prompt('Back Thickness','IF(remove_back,0,IF(use_thick_back,THICKNESS(sgi,"' + Thick_Back_Pointer_Name +'"),THICKNESS(sgi,"' + Back_Pointer_Name +'")))',[sgi,use_thick_back,remove_back])
        self.prompt('Thick Back Thickness','THICKNESS(sgi,"' + self.carcass_type + '_Thick_Back' + self.open_name +'")',[sgi])
        self.prompt('Filler Thickness','THICKNESS(sgi,"Filler")',[sgi])
        self.prompt('Nailer Thickness','THICKNESS(sgi,"Nailer")',[sgi])
        if self.carcass_type in {'Tall','Upper'}:
            self.prompt('Valance Thickness','THICKNESS(sgi,"Valance")',[sgi])
        self.prompt('Edgebanding Thickness','EDGE_THICKNESS(sgi,"' + Edgebanding_Pointer_Name + '")',[sgi])
        
        # Used to calculate the exterior opening for doors
        if self.carcass_type == 'Base':
            self.prompt('Top Inset','tt',[tt])
            self.prompt('Bottom Inset','kick_height+bt',[kick_height,bt])
        if self.carcass_type == 'Sink':
            Sub_Front_Height = self.get_var("Sub Front Height")
            self.prompt('Top Inset','Sub_Front_Height',[Sub_Front_Height])
            self.prompt('Bottom Inset','kick_height+bt',[kick_height,bt])
        if self.carcass_type == 'Tall':
            self.prompt('Top Inset','vht+tt',[vht,tt])
            self.prompt('Bottom Inset','kick_height+bt',[kick_height,bt])
        if self.carcass_type == 'Upper':
            self.prompt('Top Inset','vht+tt',[vht,tt])
            self.prompt('Bottom Inset','IF(Remove_Bottom,0,vhb+bt)',[vhb,bt,Remove_Bottom])
        if self.carcass_type == 'Suspended':
            self.prompt('Top Inset','tt',[tt])
            self.prompt('Bottom Inset','IF(Remove_Bottom,0,bt)',[bt,Remove_Bottom])
        
        self.prompt('Back Inset','IF(use_nailers,nt,0)+IF(remove_back,0,IF(use_thick_back,tbkt,bkt))',[use_nailers,nt,bkt,tbkt,use_thick_back,remove_back])
    
    def add_base_sides(self):
        g = bpy.context.scene.lm_carcass
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Toe_Kick_Height = self.get_var('Toe Kick Height')
        Toe_Kick_Setback = self.get_var('Toe Kick Setback')
        Left_Fin_End = self.get_var('Left Fin End')
        Right_Fin_End = self.get_var('Right Fin End')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Right_Side_Thickness = self.get_var('Right Side Thickness')
        
        left_side = self.add_assembly(NOTCHED_SIDE if g.Use_Notched_Sides else PART_WITH_FRONT_EDGEBANDING)
        left_side.set_name(self.carcass_type + " Left Side")
        left_side.add_prompt(name="Is Cutpart",prompt_type='CHECKBOX',value=True,tab_index=0)
        left_side.x_loc(value = 0)
        left_side.y_loc(value = 0)
        if g.Use_Notched_Sides:
            left_side.z_loc(value = 0)
            left_side.x_dim('Height',[Height])
            left_side.prompt('Notch X Dimension','Toe_Kick_Height',[Toe_Kick_Height])
            left_side.prompt('Notch Y Dimension','Toe_Kick_Setback',[Toe_Kick_Setback])
        else:
            left_side.z_loc('Toe_Kick_Height',[Toe_Kick_Height])
            left_side.x_dim('Height-Toe_Kick_Height',[Height,Toe_Kick_Height])
        left_side.x_rot(value = 0)
        left_side.y_rot(value = -90)
        left_side.z_rot(value = 0)
        left_side.y_dim('Depth',[Depth])
        left_side.z_dim('-Left_Side_Thickness',[Left_Side_Thickness])
        left_side.prompt('Hide','IF(Left_Fin_End,True,False)',[Left_Fin_End])
        left_side.cutpart(self.carcass_type + "_Side")
        left_side.edgebanding('Cabinet_Body_Edges',l1=True)
        
        right_side = self.add_assembly(NOTCHED_SIDE if g.Use_Notched_Sides else PART_WITH_FRONT_EDGEBANDING)
        right_side.set_name(self.carcass_type + " Right Side")
        right_side.add_prompt(name="Is Cutpart",prompt_type='CHECKBOX',value=True,tab_index=0)
        right_side.x_loc('Width',[Width])
        right_side.y_loc(value = 0)
        if g.Use_Notched_Sides:
            right_side.z_loc(value = 0)
            right_side.x_dim('Height',[Height])
            right_side.prompt('Notch X Dimension','Toe_Kick_Height',[Toe_Kick_Height])
            right_side.prompt('Notch Y Dimension','Toe_Kick_Setback',[Toe_Kick_Setback])
        else:
            right_side.z_loc('Toe_Kick_Height',[Toe_Kick_Height])
            right_side.x_dim('Height-Toe_Kick_Height',[Height,Toe_Kick_Height])
        right_side.x_rot(value = 0)
        right_side.y_rot(value = -90)
        right_side.z_rot(value = 0)
        right_side.x_dim(value = 0)
        right_side.y_dim('Depth',[Depth])
        right_side.z_dim('Right_Side_Thickness',[Right_Side_Thickness])
        right_side.prompt('Hide','IF(Right_Fin_End,True,False)',[Right_Fin_End])
        right_side.cutpart(self.carcass_type + "_Side")
        right_side.edgebanding('Cabinet_Body_Edges',l1=True)
        
        left_fe = self.add_assembly(NOTCHED_SIDE if g.Use_Notched_Sides else PART_WITH_FRONT_EDGEBANDING)
        left_fe.set_name(self.carcass_type + " Left FE")
        left_fe.add_prompt(name="Is Cutpart",prompt_type='CHECKBOX',value=True,tab_index=0)
        left_fe.x_loc(value = 0)
        left_fe.y_loc(value = 0)
        if g.Use_Notched_Sides:
            left_fe.z_loc(value = 0)
            left_fe.x_dim('Height',[Height])
            left_fe.prompt('Notch X Dimension','Toe_Kick_Height',[Toe_Kick_Height])
            left_fe.prompt('Notch Y Dimension','Toe_Kick_Setback',[Toe_Kick_Setback])
        else:
            left_fe.z_loc('Toe_Kick_Height',[Toe_Kick_Height])
            left_fe.x_dim('Height-Toe_Kick_Height',[Height,Toe_Kick_Height])
        left_fe.x_rot(value = 0)
        left_fe.y_rot(value = -90)
        left_fe.z_rot(value = 0)
        left_fe.x_dim(value = 0)
        left_fe.y_dim('Depth',[Depth])
        left_fe.z_dim('-Left_Side_Thickness',[Left_Side_Thickness])
        left_fe.prompt('Hide','IF(Left_Fin_End,False,True)',[Left_Fin_End])
        left_fe.cutpart(self.carcass_type + "_Side_FE")
        left_fe.edgebanding('Cabinet_Body_Edges',l1=True)
        
        right_fe = self.add_assembly(NOTCHED_SIDE if g.Use_Notched_Sides else PART_WITH_FRONT_EDGEBANDING)
        right_fe.set_name(self.carcass_type + " Right FE")
        right_fe.add_prompt(name="Is Cutpart",prompt_type='CHECKBOX',value=True,tab_index=0)
        right_fe.x_loc('Width',[Width])
        right_fe.y_loc(value = 0)
        if g.Use_Notched_Sides:
            right_fe.z_loc(value = 0)
            right_fe.x_dim('Height',[Height])
            right_fe.prompt('Notch X Dimension','Toe_Kick_Height',[Toe_Kick_Height])
            right_fe.prompt('Notch Y Dimension','Toe_Kick_Setback',[Toe_Kick_Setback])
        else:
            right_fe.z_loc('Toe_Kick_Height',[Toe_Kick_Height])
            right_fe.x_dim('Height-Toe_Kick_Height',[Height,Toe_Kick_Height])
        right_fe.x_rot(value = 0)
        right_fe.y_rot(value = -90)
        right_fe.z_rot(value = 0)
        right_fe.x_dim(value = 0)
        right_fe.y_dim('Depth',[Depth])
        right_fe.z_dim('Right_Side_Thickness',[Right_Side_Thickness])
        right_fe.prompt('Hide','IF(Right_Fin_End,False,True)',[Right_Fin_End])
        right_fe.cutpart(self.carcass_type + "_Side_FE")
        right_fe.edgebanding('Cabinet_Body_Edges',l1=True)
        
    def add_tall_sides(self):
        g = bpy.context.scene.lm_carcass
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Toe_Kick_Height = self.get_var('Toe Kick Height')
        Toe_Kick_Setback = self.get_var('Toe Kick Setback')
        Left_Fin_End = self.get_var('Left Fin End')
        Right_Fin_End = self.get_var('Right Fin End')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Right_Side_Thickness = self.get_var('Right Side Thickness')
        Left_Side_Full_Height = self.get_var('Left Side Full Height')
        Right_Side_Full_Height = self.get_var('Right Side Full Height')
        Top_Inset = self.get_var('Top Inset')
        Top_Thickness = self.get_var('Top Thickness')
    
        left_side = self.add_assembly(NOTCHED_SIDE if g.Use_Notched_Sides else PART_WITH_FRONT_EDGEBANDING)
        left_side.set_name(self.carcass_type + " Left Side")
        left_side.x_loc(value = 0)
        left_side.y_loc(value = 0)
        if g.Use_Notched_Sides:
            left_side.z_loc(value = 0)
            left_side.x_dim('Height+IF(Left_Side_Full_Height,0,-Top_Inset+Top_Thickness)',[Height,Top_Inset,Top_Thickness,Left_Side_Full_Height])
            left_side.prompt('Notch X Dimension','Toe_Kick_Height',[Toe_Kick_Height])
            left_side.prompt('Notch Y Dimension','Toe_Kick_Setback',[Toe_Kick_Setback])
        else:
            left_side.z_loc('Toe_Kick_Height',[Toe_Kick_Height])
            left_side.x_dim('Height-Toe_Kick_Height+IF(Left_Side_Full_Height,0,-Top_Inset+Top_Thickness)',[Left_Side_Full_Height,Height,Toe_Kick_Height,Top_Thickness,Top_Inset])
        left_side.x_rot(value = 0)
        left_side.y_rot(value = -90)
        left_side.z_rot(value = 0)
        left_side.y_dim('Depth',[Depth])
        left_side.z_dim('-Left_Side_Thickness',[Left_Side_Thickness])
        left_side.prompt('Hide','IF(Left_Fin_End,True,False)',[Left_Fin_End])
        left_side.cutpart(self.carcass_type + "_Side")
        left_side.edgebanding('Cabinet_Body_Edges',l1=True)
        
        right_side = self.add_assembly(NOTCHED_SIDE if g.Use_Notched_Sides else PART_WITH_FRONT_EDGEBANDING)
        right_side.set_name(self.carcass_type + " Right Side")
        right_side.x_loc('Width',[Width])
        right_side.y_loc(value = 0)
        if g.Use_Notched_Sides:
            right_side.z_loc(value = 0)
            right_side.x_dim('Height+IF(Right_Side_Full_Height,0,-Top_Inset+Top_Thickness)',[Height,Top_Inset,Top_Thickness,Right_Side_Full_Height])
            right_side.prompt('Notch X Dimension','Toe_Kick_Height',[Toe_Kick_Height])
            right_side.prompt('Notch Y Dimension','Toe_Kick_Setback',[Toe_Kick_Setback])
        else:
            right_side.z_loc('Toe_Kick_Height',[Toe_Kick_Height])
            right_side.x_dim('Height-Toe_Kick_Height+IF(Right_Side_Full_Height,0,-Top_Inset+Top_Thickness)',[Right_Side_Full_Height,Top_Thickness,Top_Inset,Height,Toe_Kick_Height])
        right_side.x_rot(value = 0)
        right_side.y_rot(value = -90)
        right_side.z_rot(value = 0)
        right_side.x_dim(value = 0)
        right_side.y_dim('Depth',[Depth])
        right_side.z_dim('Right_Side_Thickness',[Right_Side_Thickness])
        right_side.prompt('Hide','IF(Right_Fin_End,True,False)',[Right_Fin_End])
        right_side.cutpart(self.carcass_type + "_Side")
        right_side.edgebanding('Cabinet_Body_Edges',l1=True)
        
        left_fe = self.add_assembly(NOTCHED_SIDE if g.Use_Notched_Sides else PART_WITH_FRONT_EDGEBANDING)
        left_fe.set_name(self.carcass_type + " Left FE")
        left_fe.x_loc(value = 0)
        left_fe.y_loc(value = 0)
        if g.Use_Notched_Sides:
            left_fe.z_loc(value = 0)
            left_fe.x_dim('Height',[Height])
            left_fe.prompt('Notch X Dimension','Toe_Kick_Height',[Toe_Kick_Height])
            left_fe.prompt('Notch Y Dimension','Toe_Kick_Setback',[Toe_Kick_Setback])
        else:
            left_fe.z_loc('Toe_Kick_Height',[Toe_Kick_Height])
            left_fe.x_dim('Height-Toe_Kick_Height',[Height,Toe_Kick_Height])
        left_fe.x_rot(value = 0)
        left_fe.y_rot(value = -90)
        left_fe.z_rot(value = 0)
        left_fe.x_dim(value = 0)
        left_fe.y_dim('Depth',[Depth])
        left_fe.z_dim('-Left_Side_Thickness',[Left_Side_Thickness])
        left_fe.prompt('Hide','IF(Left_Fin_End,False,True)',[Left_Fin_End])
        left_fe.cutpart(self.carcass_type + "_Side_FE")
        left_fe.edgebanding('Cabinet_Body_Edges',l1=True)
        
        right_fe = self.add_assembly(NOTCHED_SIDE if g.Use_Notched_Sides else PART_WITH_FRONT_EDGEBANDING)
        right_fe.set_name(self.carcass_type + " Right FE")
        right_fe.x_loc('Width',[Width])
        right_fe.y_loc(value = 0)
        if g.Use_Notched_Sides:
            right_fe.z_loc(value = 0)
            right_fe.x_dim('Height',[Height])
            right_fe.prompt('Notch X Dimension','Toe_Kick_Height',[Toe_Kick_Height])
            right_fe.prompt('Notch Y Dimension','Toe_Kick_Setback',[Toe_Kick_Setback])
        else:
            right_fe.z_loc('Toe_Kick_Height',[Toe_Kick_Height])
            right_fe.x_dim('Height-Toe_Kick_Height',[Height,Toe_Kick_Height])
        right_fe.x_rot(value = 0)
        right_fe.y_rot(value = -90)
        right_fe.z_rot(value = 0)
        right_fe.x_dim(value = 0)
        right_fe.y_dim('Depth',[Depth])
        right_fe.z_dim('Right_Side_Thickness',[Right_Side_Thickness])
        right_fe.prompt('Hide','IF(Right_Fin_End,False,True)',[Right_Fin_End])
        right_fe.cutpart(self.carcass_type + "_Side_FE")
        right_fe.edgebanding('Cabinet_Body_Edges',l1=True)
        
    def add_upper_sides(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Left_Fin_End = self.get_var('Left Fin End')
        Right_Fin_End = self.get_var('Right Fin End')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Right_Side_Thickness = self.get_var('Right Side Thickness')
        Left_Side_Full_Height = self.get_var('Left Side Full Height')
        Right_Side_Full_Height = self.get_var('Right Side Full Height')
        Valance_Height_Top = self.get_var('Valance Height Top')
        Valance_Height_Bottom = self.get_var('Valance Height Bottom')

        left_side = self.add_assembly(PART_WITH_FRONT_AND_BOTTOM_EDGEBANDING)
        left_side.set_name(self.carcass_type + " Left Side")
        left_side.x_loc(value = 0)
        left_side.y_loc(value = 0)
        left_side.z_loc('IF(Left_Side_Full_Height,0,-Valance_Height_Top)',[Left_Side_Full_Height,Valance_Height_Top])
        left_side.x_rot(value = 0)
        left_side.y_rot(value = -90)
        left_side.z_rot(value = 0)
        left_side.x_dim('Height+IF(Left_Side_Full_Height,0,Valance_Height_Top+Valance_Height_Bottom)',[Height,Valance_Height_Bottom,Valance_Height_Top,Left_Side_Full_Height])
        left_side.y_dim('Depth',[Depth])
        left_side.z_dim('-Left_Side_Thickness',[Left_Side_Thickness])
        left_side.prompt('Hide','IF(Left_Fin_End,True,False)',[Left_Fin_End])
        left_side.cutpart(self.carcass_type + "_Side")
        left_side.edgebanding('Cabinet_Body_Edges',l1=True)
        
        right_side = self.add_assembly(PART_WITH_FRONT_AND_BOTTOM_EDGEBANDING)
        right_side.set_name(self.carcass_type + " Right Side")
        right_side.x_loc('Width',[Width])
        right_side.y_loc(value = 0)
        right_side.z_loc('IF(Right_Side_Full_Height,0,-Valance_Height_Top)',[Right_Side_Full_Height,Valance_Height_Top])
        right_side.x_rot(value = 0)
        right_side.y_rot(value = -90)
        right_side.z_rot(value = 0)
        right_side.x_dim('Height+IF(Right_Side_Full_Height,0,Valance_Height_Top+Valance_Height_Bottom)',[Height,Right_Side_Full_Height,Valance_Height_Top,Valance_Height_Bottom])
        right_side.y_dim('Depth',[Depth])
        right_side.z_dim('Right_Side_Thickness',[Right_Side_Thickness])
        right_side.prompt('Hide','IF(Right_Fin_End,True,False)',[Right_Fin_End])
        right_side.cutpart(self.carcass_type + "_Side")
        right_side.edgebanding('Cabinet_Body_Edges',l1=True)
        
        left_fe = self.add_assembly(PART_WITH_FRONT_AND_BOTTOM_EDGEBANDING)
        left_fe.set_name(self.carcass_type + " Left FE")
        left_fe.x_loc(value = 0)
        left_fe.y_loc(value = 0)
        left_fe.z_loc(value = 0)
        left_fe.x_rot(value = 0)
        left_fe.y_rot(value = -90)
        left_fe.z_rot(value = 0)
        left_fe.x_dim('Height',[Height])
        left_fe.y_dim('Depth',[Depth])
        left_fe.z_dim('-Left_Side_Thickness',[Left_Side_Thickness])
        left_fe.prompt('Hide','IF(Left_Fin_End,False,True)',[Left_Fin_End])
        left_fe.cutpart(self.carcass_type + "_Side_FE")
        left_fe.edgebanding('Cabinet_Body_Edges',l1=True)
        
        right_fe = self.add_assembly(PART_WITH_FRONT_AND_BOTTOM_EDGEBANDING)
        right_fe.set_name(self.carcass_type + " Right FE")
        right_fe.x_loc('Width',[Width])
        right_fe.y_loc(value = 0)
        right_fe.z_loc(value = 0)
        right_fe.x_rot(value = 0)
        right_fe.y_rot(value = -90)
        right_fe.z_rot(value = 0)
        right_fe.x_dim('Height',[Height])
        right_fe.y_dim('Depth',[Depth])
        right_fe.z_dim('Right_Side_Thickness',[Right_Side_Thickness])
        right_fe.prompt('Hide','IF(Right_Fin_End,False,True)',[Right_Fin_End])
        right_fe.cutpart(self.carcass_type + "_Side_FE")
        right_fe.edgebanding('Cabinet_Body_Edges',l1=True)
        
    def add_suspended_sides(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Left_Fin_End = self.get_var('Left Fin End')
        Right_Fin_End = self.get_var('Right Fin End')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Right_Side_Thickness = self.get_var('Right Side Thickness')

        left_side = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        left_side.set_name(self.carcass_type + " Left Side")
        left_side.x_loc(value = 0)
        left_side.y_loc(value = 0)
        left_side.z_loc(value = 0)
        left_side.x_rot(value = 0)
        left_side.y_rot(value = -90)
        left_side.z_rot(value = 0)
        left_side.x_dim('Height',[Height])
        left_side.y_dim('Depth',[Depth])
        left_side.z_dim('-Left_Side_Thickness',[Left_Side_Thickness])
        left_side.prompt('Hide','IF(Left_Fin_End,True,False)',[Left_Fin_End])
        left_side.cutpart(self.carcass_type + "_Side")
        left_side.edgebanding('Cabinet_Body_Edges',l1=True)
        
        right_side = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        right_side.set_name(self.carcass_type + " Right Side")
        right_side.x_loc('Width',[Width])
        right_side.y_loc(value = 0)
        right_side.z_loc(value = 0)
        right_side.x_rot(value = 0)
        right_side.y_rot(value = -90)
        right_side.z_rot(value = 0)
        right_side.x_dim('Height',[Height])
        right_side.y_dim('Depth',[Depth])
        right_side.z_dim('Right_Side_Thickness',[Right_Side_Thickness])
        right_side.prompt('Hide','IF(Right_Fin_End,True,False)',[Right_Fin_End])
        right_side.cutpart(self.carcass_type + "_Side")
        right_side.edgebanding('Cabinet_Body_Edges',l1=True)
        
        left_fe = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        left_fe.set_name(self.carcass_type + " Left FE")
        left_fe.x_loc(value = 0)
        left_fe.y_loc(value = 0)
        left_fe.z_loc(value = 0)
        left_fe.x_rot(value = 0)
        left_fe.y_rot(value = -90)
        left_fe.z_rot(value = 0)
        left_fe.x_dim('Height',[Height])
        left_fe.y_dim('Depth',[Depth])
        left_fe.z_dim('-Left_Side_Thickness',[Left_Side_Thickness])
        left_fe.prompt('Hide','IF(Left_Fin_End,False,True)',[Left_Fin_End])
        left_fe.cutpart(self.carcass_type + "_Side_FE")
        left_fe.edgebanding('Cabinet_Body_Edges',l1=True)
        
        right_fe = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        right_fe.set_name(self.carcass_type + " Right FE")
        right_fe.x_loc('Width',[Width])
        right_fe.y_loc(value = 0)
        right_fe.z_loc(value = 0)
        right_fe.x_rot(value = 0)
        right_fe.y_rot(value = -90)
        right_fe.z_rot(value = 0)
        right_fe.x_dim('Height',[Height])
        right_fe.y_dim('Depth',[Depth])
        right_fe.z_dim('Right_Side_Thickness',[Right_Side_Thickness])
        right_fe.prompt('Hide','IF(Right_Fin_End,False,True)',[Right_Fin_End])
        right_fe.cutpart(self.carcass_type + "_Side_FE")
        right_fe.edgebanding('Cabinet_Body_Edges',l1=True)
        
    def add_fillers(self):
        width = self.get_var('dim_x','width')
        depth = self.get_var('dim_y','depth')
        height = self.get_var('dim_z','height')
        l_filler = self.get_var("Left Side Wall Filler",'l_filler')
        r_filler = self.get_var("Right Side Wall Filler",'r_filler')
        ft = self.get_var("Filler Thickness",'ft')
        if self.carcass_type in {'Base','Sink','Tall'}:
            kick_height = self.get_var("Toe Kick Height",'kick_height')
            
        left_filler = self.add_assembly(PART_WITH_NO_EDGEBANDING)
        left_filler.set_name("Left Filler")
        left_filler.x_loc(value = fd.inches(0))
        left_filler.y_loc('depth',[depth])
        left_filler.z_loc('height',[height])
        left_filler.x_rot(value = 90)
        left_filler.y_rot(value = 90)
        left_filler.z_rot(value = 180)
        left_filler.y_dim('l_filler',[l_filler])
        left_filler.z_dim('ft',[ft])
        left_filler.prompt('Hide','IF(l_filler>0,False,True)',[l_filler])
        left_filler.cutpart('Filler')
        
        right_filler = self.add_assembly(PART_WITH_NO_EDGEBANDING)
        right_filler.set_name("Right Filler")
        right_filler.x_loc('width',[width])
        right_filler.y_loc('depth',[depth])
        right_filler.z_loc('height',[height])
        right_filler.x_rot(value = 90)
        right_filler.y_rot(value = 90)
        right_filler.z_rot(value = 0)
        right_filler.y_dim('r_filler',[r_filler])
        right_filler.z_dim('-ft',[ft])
        right_filler.prompt('Hide','IF(r_filler>0,False,True)',[r_filler])
        right_filler.cutpart('Filler')
        
        if self.carcass_type in {'Base','Sink','Tall'}:
            left_filler.x_dim('height-kick_height',[height,kick_height])
            right_filler.x_dim('height-kick_height',[height,kick_height])
            
        if self.carcass_type in {'Upper','Suspended'}:
            left_filler.x_dim('height',[height])
            right_filler.x_dim('height',[height])
            
    def add_full_top(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Top_Thickness = self.get_var('Top Thickness')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Right_Side_Thickness = self.get_var('Right Side Thickness')
        Top_Inset = self.get_var('Top Inset')
        
        top = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        top.set_name(self.carcass_type + " Top")
        top.x_dim('Width-(Left_Side_Thickness+Right_Side_Thickness)',[Width,Left_Side_Thickness,Right_Side_Thickness])
        top.y_dim('Depth',[Depth])
        top.z_dim('-Top_Thickness',[Top_Thickness])
        top.x_loc('Left_Side_Thickness',[Left_Side_Thickness])
        top.y_loc(value = 0)
        top.z_loc('IF(Height>0,Height-Top_Inset+Top_Thickness,-Top_Inset+Top_Thickness)',[Height,Top_Inset,Top_Thickness])
        top.x_rot(value = 0)
        top.y_rot(value = 0)
        top.z_rot(value = 0)
        top.cutpart(self.carcass_type + "_Top")
        top.edgebanding('Cabinet_Body_Edges', l1 = True)
        
    def add_stretchers(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Top_Thickness = self.get_var('Top Thickness')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Right_Side_Thickness = self.get_var('Right Side Thickness')
        Stretcher_Width = self.get_var('Stretcher Width')
        
        front_s = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        front_s.set_name(self.carcass_type + " Front Stretcher")
        front_s.x_dim('Width-(Left_Side_Thickness+Right_Side_Thickness)',[Width,Left_Side_Thickness,Right_Side_Thickness])
        front_s.y_dim('-Stretcher_Width',[Stretcher_Width])
        front_s.z_dim('-Top_Thickness',[Top_Thickness])
        front_s.x_loc('Left_Side_Thickness',[Left_Side_Thickness])
        front_s.y_loc('Depth+Stretcher_Width',[Stretcher_Width,Depth])
        front_s.z_loc('IF(Height>0,Height,0)',[Height])
        front_s.x_rot(value = 0)
        front_s.y_rot(value = 0)
        front_s.z_rot(value = 0)
        front_s.cutpart(self.carcass_type + "_Top")
        front_s.edgebanding('Cabinet_Body_Edges', l1 = True)
        
        rear_s = self.add_assembly(PART_WITH_NO_EDGEBANDING)
        rear_s.set_name(self.carcass_type + " Rear Stretcher")
        rear_s.x_dim('Width-(Left_Side_Thickness+Right_Side_Thickness)',[Width,Left_Side_Thickness,Right_Side_Thickness])
        rear_s.y_dim('-Stretcher_Width',[Stretcher_Width])
        rear_s.z_dim('-Top_Thickness',[Top_Thickness])
        rear_s.x_loc('Left_Side_Thickness',[Left_Side_Thickness])
        rear_s.y_loc(value = 0)
        rear_s.z_loc('IF(Height>0,Height,0)',[Height])
        rear_s.x_rot(value = 0)
        rear_s.y_rot(value = 0)
        rear_s.z_rot(value = 0)
        rear_s.cutpart(self.carcass_type + "_Top")
        
    def add_sink_top(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Right_Side_Thickness = self.get_var('Right Side Thickness')
        Sub_Front_Height = self.get_var('Sub Front Height')
        Sub_Front_Thickness = self.get_var('Sub Front Thickness')
        
        front_s = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        front_s.set_name(self.carcass_type + " Front Stretcher")
        front_s.x_dim('Width-(Left_Side_Thickness+Right_Side_Thickness)',[Width,Left_Side_Thickness,Right_Side_Thickness])
        front_s.y_dim('-Sub_Front_Height',[Sub_Front_Height])
        front_s.z_dim('-Sub_Front_Thickness',[Sub_Front_Thickness])
        front_s.x_loc('Left_Side_Thickness',[Left_Side_Thickness])
        front_s.y_loc('Depth',[Depth])
        front_s.z_loc('IF(Height>0,Height,0)',[Height])
        front_s.x_rot(value = 90)
        front_s.y_rot(value = 0)
        front_s.z_rot(value = 0)
        front_s.cutpart("Sink_Sub_Front")
        front_s.edgebanding('Cabinet_Body_Edges', l1 = True)
        
    def add_bottom(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Toe_Kick_Height = self.get_var('Toe Kick Height')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Right_Side_Thickness = self.get_var('Right Side Thickness')
        Bottom_Thickness = self.get_var('Bottom Thickness')
        Remove_Bottom = self.get_var('Remove Bottom')
        
        bottom = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        bottom.set_name(self.carcass_type + " Bottom")
        bottom.x_dim('Width-(Left_Side_Thickness+Right_Side_Thickness)',[Width,Left_Side_Thickness,Right_Side_Thickness])
        bottom.y_dim('Depth',[Depth])
        bottom.z_dim('Bottom_Thickness',[Bottom_Thickness])
        bottom.x_loc('Left_Side_Thickness',[Left_Side_Thickness])
        bottom.y_loc(value = 0)
        bottom.x_rot(value = 0)
        bottom.y_rot(value = 0)
        bottom.z_rot(value = 0)
        bottom.prompt('Hide','Remove_Bottom',[Remove_Bottom])
        bottom.cutpart(self.carcass_type + "_Bottom")
        bottom.edgebanding('Cabinet_Body_Edges', l1 = True)
        
        if self.carcass_type in {'Upper','Suspended'}:
            Bottom_Inset = self.get_var('Bottom Inset')
            bottom.z_loc('Height+Bottom_Inset-Bottom_Thickness',[Height,Bottom_Inset,Bottom_Thickness])
            
        if self.carcass_type in {'Base','Tall','Sink'}:
            bottom.z_loc('Toe_Kick_Height',[Toe_Kick_Height])
            
    def add_toe_kick(self):
        Width = self.get_var('dim_x','Width')
        Depth = self.get_var('dim_y','Depth')
        Toe_Kick_Height = self.get_var('Toe Kick Height')
        Toe_Kick_Setback = self.get_var('Toe Kick Setback')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Right_Side_Thickness = self.get_var('Right Side Thickness')
        Remove_Bottom = self.get_var('Remove Bottom')
        
        kick = self.add_assembly(PART_WITH_NO_EDGEBANDING)
        kick.set_name("Toe Kick")
        kick.x_dim('Width-(Left_Side_Thickness+Right_Side_Thickness)',[Width,Left_Side_Thickness,Right_Side_Thickness])
        kick.y_dim('Toe_Kick_Height',[Toe_Kick_Height])
        kick.z_dim(value = fd.inches(-.75))
        kick.x_loc('Left_Side_Thickness',[Left_Side_Thickness])
        kick.y_loc('Depth+Toe_Kick_Setback',[Depth,Toe_Kick_Setback])
        kick.z_loc(value = 0)
        kick.x_rot(value = 90)
        kick.y_rot(value = 0)
        kick.z_rot(value = 0)
        kick.prompt('Hide','Remove_Bottom',[Remove_Bottom])
        kick.cutpart("Toe_Kick")
    
    def add_leg_levelers(self):
        Width = self.get_var('dim_x','Width')
        Depth = self.get_var('dim_y','Depth')
        Toe_Kick_Height = self.get_var('Toe Kick Height')
        Toe_Kick_Setback = self.get_var('Toe Kick Setback')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Right_Side_Thickness = self.get_var('Right Side Thickness')

        legs = self.add_assembly(LEG_LEVELERS)
        legs.set_name("Leg Levelers")
        legs.x_loc('Left_Side_Thickness',[Left_Side_Thickness])
        legs.y_loc(value = 0)
        legs.z_loc(value = 0)
        legs.x_rot(value = 0)
        legs.y_rot(value = 0)
        legs.z_rot(value = 0)
        legs.x_dim('Width-(Left_Side_Thickness+Right_Side_Thickness)',[Width,Left_Side_Thickness,Right_Side_Thickness])
        legs.y_dim('Depth+Toe_Kick_Setback',[Depth,Toe_Kick_Setback])
        legs.z_dim('Toe_Kick_Height',[Toe_Kick_Height])
    
    def add_back(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Right_Side_Thickness = self.get_var('Right Side Thickness')
        Top_Inset = self.get_var('Top Inset')
        Bottom_Inset = self.get_var('Bottom Inset')
        Back_Thickness = self.get_var('Back Thickness')
        Bottom_Thickness = self.get_var('Bottom Thickness')
        Top_Thickness = self.get_var('Top Thickness')
        Use_Nailers = self.get_var('Use Nailers')
        Nailer_Thickness = self.get_var('Nailer Thickness')
        Remove_Back = self.get_var('Remove Back')
        Remove_Bottom = self.get_var('Remove Bottom')
        Toe_Kick_Height = self.get_var('Toe Kick Height')
        
        back = self.add_assembly(PART_WITH_NO_EDGEBANDING)
        back.set_name(self.carcass_type + " Back")
        back.x_loc('Left_Side_Thickness',[Left_Side_Thickness])
        back.y_loc('IF(Use_Nailers,-Nailer_Thickness,0)',[Use_Nailers,Nailer_Thickness])
        back.x_rot(value = 0)
        back.y_rot(value = -90)
        back.z_rot(value = -90)
        
        if self.carcass_type in {'Base','Sink'}:
            back.x_dim('fabs(Height)-IF(Remove_Bottom,0,Toe_Kick_Height+Bottom_Thickness)-Top_Thickness',[Height,Toe_Kick_Height,Bottom_Thickness,Remove_Bottom,Top_Thickness])
        
        if self.carcass_type == 'Tall':
            back.x_dim('fabs(Height)-IF(Remove_Bottom,0,Toe_Kick_Height+Bottom_Thickness)-Top_Inset',[Height,Top_Inset,Toe_Kick_Height,Bottom_Thickness,Remove_Bottom])
        
        if self.carcass_type in {'Upper','Suspended'}:
            back.x_dim('fabs(Height)-(Top_Inset+Bottom_Inset)',[Height,Top_Inset,Bottom_Inset])
            
        back.y_dim('Width-(Left_Side_Thickness+Right_Side_Thickness)',[Width,Left_Side_Thickness,Right_Side_Thickness])
        back.z_dim('-Back_Thickness',[Back_Thickness])
        back.cutpart(self.carcass_type + "_Back" + self.open_name)
        back.edgebanding('Cabinet_Body_Edges', l1 = True)
        back.prompt('Hide','IF(Remove_Back,True,False)',[Remove_Back])
        
        if self.carcass_type in {'Base','Tall','Sink'}:
            back.z_loc('IF(Remove_Bottom,0,Toe_Kick_Height+Bottom_Thickness)',[Remove_Bottom,Toe_Kick_Height,Bottom_Thickness])
        
        if self.carcass_type in {'Upper','Suspended'}:
            back.z_loc('Height+Bottom_Inset',[Height,Bottom_Inset])
    
    def add_nailers(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Right_Side_Thickness = self.get_var('Right Side Thickness')
        Top_Thickness = self.get_var('Top Thickness')
        Top_Inset = self.get_var('Top Inset')
        Bottom_Inset = self.get_var('Bottom Inset')
        Remove_Bottom = self.get_var('Remove Bottom')
        Use_Nailers = self.get_var('Use Nailers')
        Nailer_Thickness = self.get_var('Nailer Thickness')
        Nailer_Width = self.get_var('Nailer Width')
        Center_Nailer_Switch = self.get_var('Center Nailer Switch')
        
        top_n = self.add_assembly(PART_WITH_NO_EDGEBANDING)
        top_n.set_name("Top Nailer")
        top_n.x_loc('Left_Side_Thickness',[Left_Side_Thickness])
        top_n.y_loc('IF(Use_Nailers,-Nailer_Thickness,0)',[Use_Nailers,Nailer_Thickness])
        if self.carcass_type in {'Base','Sink'}:
            top_n.z_loc('Height-Top_Thickness',[Height,Top_Thickness])
        if self.carcass_type in {'Upper','Tall'}:
            top_n.z_loc('IF(Height>0,Height-Top_Inset,-Top_Inset)',[Height,Top_Inset])
        top_n.x_rot(value = 90)
        top_n.y_rot(value = 0)
        top_n.z_rot(value = 0)
        top_n.x_dim('Width-(Left_Side_Thickness+Right_Side_Thickness)',[Width,Left_Side_Thickness,Right_Side_Thickness])
        top_n.y_dim('-Nailer_Width',[Nailer_Width])
        top_n.z_dim('-Nailer_Thickness',[Nailer_Thickness])
        top_n.prompt('Hide','IF(Use_Nailers,False,True)',[Use_Nailers])
        top_n.cutpart("Nailer")
    
        center_n = self.add_assembly(PART_WITH_NO_EDGEBANDING)
        center_n.set_name("Center Nailer")
        center_n.x_loc('Left_Side_Thickness',[Left_Side_Thickness])
        center_n.y_loc('IF(Use_Nailers,-Nailer_Thickness,0)',[Use_Nailers,Nailer_Thickness])
        center_n.z_loc('IF(Height>0,(Height/2)-(Nailer_Width/2)+(Bottom_Inset/2),(Height/2)-(Nailer_Width/2))',[Height,Nailer_Width,Bottom_Inset])
        center_n.x_rot(value = 90)
        center_n.y_rot(value = 0)
        center_n.z_rot(value = 0)
        center_n.x_dim('Width-(Left_Side_Thickness+Right_Side_Thickness)',[Width,Left_Side_Thickness,Right_Side_Thickness])
        center_n.y_dim('Nailer_Width',[Nailer_Width])
        center_n.z_dim('-Nailer_Thickness',[Nailer_Thickness])
        center_n.prompt('Hide','IF(Use_Nailers,IF(Height>Center_Nailer_Switch,False,True),True)',[Height,Center_Nailer_Switch,Use_Nailers])
        center_n.cutpart("Nailer")
    
        bottom_n = self.add_assembly(PART_WITH_NO_EDGEBANDING)
        bottom_n.set_name("Bottom Nailer")
        bottom_n.x_loc('Left_Side_Thickness',[Left_Side_Thickness])
        bottom_n.y_loc('IF(Use_Nailers,-Nailer_Thickness,0)',[Use_Nailers,Nailer_Thickness])
        bottom_n.z_loc('IF(Height>0,IF(Remove_Bottom,0,Bottom_Inset),Height+Bottom_Inset)',[Height,Bottom_Inset,Remove_Bottom])
        bottom_n.x_rot(value = 90)
        bottom_n.y_rot(value = 0)
        bottom_n.z_rot(value = 0)
        bottom_n.x_dim('Width-(Left_Side_Thickness+Right_Side_Thickness)',[Width,Left_Side_Thickness,Right_Side_Thickness])
        bottom_n.y_dim('Nailer_Width',[Nailer_Width])
        bottom_n.z_dim('-Nailer_Thickness',[Nailer_Thickness])
        bottom_n.prompt('Hide','IF(Use_Nailers,False,True)',[Use_Nailers])
        bottom_n.cutpart("Nailer")
    
    def add_valances(self):
        Width = self.get_var('dim_x','Width')
        Depth = self.get_var('dim_y','Depth')
        Height = self.get_var('dim_z','Height')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Right_Side_Thickness = self.get_var('Right Side Thickness')
        Top_Inset = self.get_var('Top Inset')
        Top_Thickness = self.get_var('Top Thickness')
        Left_Fin_End = self.get_var('Left Fin End')
        Right_Fin_End = self.get_var('Right Fin End')
        Left_Side_Full_Height = self.get_var('Left Side Full Height')
        Right_Side_Full_Height = self.get_var('Right Side Full Height')
        Valance_Thickness = self.get_var("Valance Thickness")
        Valance_Each_Unit = self.get_var("Valance Each Unit")
        Valance_Height_Top = self.get_var("Valance Height Top")
        Valance_Height_Bottom = self.get_var("Valance Height Bottom")
        
        top_val = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        top_val.set_name("Top Valance")
        top_val.x_loc('IF(OR(Left_Fin_End,Left_Side_Full_Height),Left_Side_Thickness,0)',[Left_Fin_End,Left_Side_Full_Height,Left_Side_Thickness])
        top_val.y_loc('Depth',[Depth])
        top_val.z_loc('IF(Height>0,Height-Top_Inset+Top_Thickness,-Top_Inset+Top_Thickness)',[Height,Top_Thickness,Top_Inset])
        top_val.x_rot(value = 90)
        top_val.y_rot(value = 0)
        top_val.z_rot(value = 0)
        top_val.x_dim('Width-(IF(OR(Left_Fin_End,Left_Side_Full_Height),Left_Side_Thickness,0)+IF(OR(Right_Fin_End,Right_Side_Full_Height),Right_Side_Thickness,0))',[Width,Right_Fin_End,Left_Fin_End,Left_Side_Full_Height,Left_Side_Thickness,Right_Side_Full_Height,Right_Side_Thickness])
        top_val.y_dim('Valance_Height_Top',[Valance_Height_Top])
        top_val.z_dim('-Valance_Thickness',[Valance_Thickness])
        top_val.prompt('Hide','IF(AND(Valance_Each_Unit,Valance_Height_Top>0),False,True)',[Valance_Each_Unit,Valance_Height_Top])
        top_val.cutpart("Valance")
        top_val.edgebanding('Cabinet_Body_Edges',l1=True)
        
        if self.carcass_type == 'Upper':
            bottom_val = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
            bottom_val.set_name("Bottom Valance")
            bottom_val.x_loc('IF(OR(Left_Fin_End,Left_Side_Full_Height),Left_Side_Thickness,0)',[Left_Fin_End,Left_Side_Full_Height,Left_Side_Thickness])
            bottom_val.y_loc('Depth',[Depth])
            bottom_val.z_loc('Height+Valance_Height_Bottom',[Height,Valance_Height_Bottom])
            bottom_val.x_rot(value = 90)
            bottom_val.y_rot(value = 0)
            bottom_val.z_rot(value = 0)
            bottom_val.x_dim('Width-(IF(OR(Left_Fin_End,Left_Side_Full_Height),Left_Side_Thickness,0)+IF(OR(Right_Fin_End,Right_Side_Full_Height),Right_Side_Thickness,0))',[Width,Right_Fin_End,Left_Fin_End,Left_Side_Full_Height,Left_Side_Thickness,Right_Side_Full_Height,Right_Side_Thickness])
            bottom_val.y_dim('-Valance_Height_Bottom',[Valance_Height_Bottom])
            bottom_val.z_dim('-Valance_Thickness',[Valance_Thickness])
            bottom_val.prompt('Hide','IF(AND(Valance_Each_Unit,Valance_Height_Bottom>0),False,True)',[Valance_Each_Unit,Valance_Height_Bottom])
            bottom_val.cutpart("Valance")
            bottom_val.edgebanding('Cabinet_Body_Edges',l1=True)
            
    def add_appliance_opening(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Top_Thickness = self.get_var('Top Thickness')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Right_Side_Thickness = self.get_var('Right Side Thickness')
        Top_Inset = self.get_var('Top Inset')
        
        opening = self.add_opening()
        opening.set_name("Appliance Opening")
        opening.x_dim('Width-(Left_Side_Thickness+Right_Side_Thickness)',[Width,Left_Side_Thickness,Right_Side_Thickness])
        opening.y_dim('Depth',[Depth])
        opening.z_dim(value = fd.inches(-4))
        opening.x_loc('Left_Side_Thickness',[Left_Side_Thickness])
        opening.y_loc(value = 0)
        opening.z_loc('Height+INCH(1.5)',[Height])
        opening.x_rot(value = 0)
        opening.y_rot(value = 0)
        opening.z_rot(value = 0)
        
    def draw(self):
        g = bpy.context.scene.lm_carcass
        self.create_assembly()

        self.add_common_carcass_prompts()
        if self.carcass_type == "Base":
            self.add_base_assembly_prompts()
            if not self.remove_top:
                if g.Use_Full_Tops:
                    self.add_full_top()
                else:
                    self.add_stretchers()
            if g.Use_Notched_Sides:
                self.add_toe_kick()
            self.add_base_sides()
            if g.Use_Leg_Levelers:
                self.add_leg_levelers()

        if self.carcass_type == "Tall":
            self.add_base_assembly_prompts()
            self.add_full_top()
            self.add_valance_prompts(add_bottom_valance=False)
            if g.Use_Notched_Sides:
                self.add_toe_kick()
            self.add_tall_sides()
            if g.Use_Leg_Levelers:
                self.add_leg_levelers()
            self.add_valances()
            
        if self.carcass_type == "Upper":
            self.flip_z = True
            self.add_full_top()
            self.add_valance_prompts(add_bottom_valance=True)
            self.add_valances()
            self.add_upper_sides()
            
        if self.carcass_type == "Sink":
            self.add_base_assembly_prompts()
            self.add_sink_prompts()
            self.add_sink_top()
            if g.Use_Notched_Sides:
                self.add_toe_kick()
            self.add_base_sides()
            if g.Use_Leg_Levelers:
                self.add_leg_levelers()
            self.add_appliance_opening()
                
        if self.carcass_type == "Suspended":
            self.flip_z = True
            self.add_suspended_sides()
            if not self.remove_top:
                if g.Use_Full_Tops:
                    self.add_full_top()
                else:
                    self.add_stretchers()

        if self.remove_top:
            self.add_appliance_opening()

        self.add_fillers()
        self.add_bottom()
        self.add_back()
        self.add_nailers()
        self.add_prompt_formuls()
        
        self.update()
        
class Transition_Carcass(fd.Library_Assembly):
    
    library_name = "Carcasses"
    placement_type = ""
    type_assembly = "INSERT"
    
    carcass_type = "" # {Base, Tall, Upper, Sink, Suspended}
    open_name = ""
    
    def add_common_carcass_prompts(self):
        g = bpy.context.scene.lm_carcass
        self.add_tab(name='Carcass Options',tab_type='VISIBLE')
        self.add_tab(name='Formulas',tab_type='HIDDEN')
        self.add_tab(name='Machining Options',tab_type='HIDDEN')
        self.add_prompt(name="Left Fin End",prompt_type='CHECKBOX',value=False,tab_index=0)
        self.add_prompt(name="Right Fin End",prompt_type='CHECKBOX',value=False,tab_index=0)
        self.add_prompt(name="Left Side Wall Filler",prompt_type='DISTANCE',value=0.0,tab_index=0)
        self.add_prompt(name="Right Side Wall Filler",prompt_type='DISTANCE',value=0.0,tab_index=0)
        self.add_prompt(name="Cabinet Depth Left",prompt_type='DISTANCE',value=fd.inches(23.0),tab_index=0)
        self.add_prompt(name="Cabinet Depth Right",prompt_type='DISTANCE',value=fd.inches(12.0),tab_index=0)
        self.add_prompt(name="Use Nailers",prompt_type='CHECKBOX',value= g.Use_Nailers,tab_index=0)
        self.add_prompt(name="Nailer Width",prompt_type='DISTANCE',value= g.Nailer_Width,tab_index=0)
        self.add_prompt(name="Center Nailer Switch",prompt_type='DISTANCE',value= g.Center_Nailer_Switch,tab_index=0)
        self.add_prompt(name="Use Thick Back",prompt_type='CHECKBOX',value= g.Use_Thick_Back,tab_index=0)
        self.add_prompt(name="Remove Back",prompt_type='CHECKBOX',value= g.Remove_Back,tab_index=0)
        self.add_prompt(name="Remove Bottom",prompt_type='CHECKBOX',value= False,tab_index=0)
        
        if self.carcass_type in {'Base','Suspended'} and not g.Use_Full_Tops:
            self.add_prompt(name="Stretcher Width",prompt_type='DISTANCE',value=g.Stretcher_Width,tab_index=0)
        
        self.add_prompt(name="Left Side Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Right Side Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Top Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Bottom Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Back Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Thick Back Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Filler Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Nailer Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Edgebanding Thickness",prompt_type='DISTANCE',value=fd.inches(.02),tab_index=1)
        self.add_prompt(name="Back Inset",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        self.add_prompt(name="Top Inset",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        self.add_prompt(name="Bottom Inset",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        
    def add_base_assembly_prompts(self):
        g = bpy.context.scene.lm_carcass
        self.add_prompt(name="Toe Kick Height",prompt_type='DISTANCE',value= g.Toe_Kick_Height,tab_index=0)
        self.add_prompt(name="Toe Kick Setback",prompt_type='DISTANCE',value= g.Toe_Kick_Setback,tab_index=0)
        self.add_prompt(name="Toe Kick Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        
    def add_valance_prompts(self,add_bottom_valance):
        g = bpy.context.scene.lm_carcass
        self.add_prompt(name="Valance Height Top",prompt_type='DISTANCE',value=g.Valance_Height_Top,tab_index=0)
        self.add_prompt(name="Door Valance Top",prompt_type='CHECKBOX',value=g.Door_Valance_Top,tab_index=0)
        if add_bottom_valance:
            self.add_prompt(name="Valance Height Bottom",prompt_type='DISTANCE',value=g.Valance_Height_Bottom,tab_index=0)
            self.add_prompt(name="Door Valance Bottom",prompt_type='CHECKBOX',value=g.Door_Valance_Bottom,tab_index=0)
        self.add_prompt(name="Left Side Full Height",prompt_type='CHECKBOX',value=False,tab_index=0)
        self.add_prompt(name="Right Side Full Height",prompt_type='CHECKBOX',value=False,tab_index=0)
        self.add_prompt(name="Valance Each Unit",prompt_type='CHECKBOX',value=g.Valance_Each_Unit,tab_index=0)
        self.add_prompt(name="Valance Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
    
    def add_prompt_formuls(self):
        sgi = self.get_var('cabinetlib.spec_group_index','sgi')
        tt = self.get_var("Top Thickness",'tt')
        bt = self.get_var("Bottom Thickness",'bt')
        use_nailers = self.get_var("Use Nailers",'use_nailers')
        nt = self.get_var("Nailer Thickness",'nt')
        bkt = self.get_var("Back Thickness",'bkt')
        tbkt = self.get_var("Thick Back Thickness",'tbkt')
        use_thick_back = self.get_var("Use Thick Back",'use_thick_back')
        remove_back = self.get_var("Remove Back",'remove_back')
        lfe = self.get_var("Left Fin End",'lfe')
        rfe = self.get_var("Right Fin End",'rfe')
        Remove_Bottom = self.get_var('Remove Bottom','Remove_Bottom')
        if self.carcass_type in {'Base','Sink','Tall'}:
            kick_height = self.get_var("Toe Kick Height",'kick_height')
        if self.carcass_type in {'Upper','Tall'}:
            vhb = self.get_var("Valance Height Bottom",'vhb')
            vht = self.get_var("Valance Height Top",'vht')

        Side_Pointer_Name = self.carcass_type + '_Side' + self.open_name
        FE_Pointer_Name = self.carcass_type + '_Side_FE' + self.open_name
        Top_Pointer_Name = self.carcass_type + '_Top' + self.open_name
        Bottom_Pointer_Name = self.carcass_type + '_Bottom' + self.open_name
        Back_Pointer_Name = self.carcass_type + '_Back' + self.open_name
        Thick_Back_Pointer_Name = self.carcass_type + '_Thick_Back' + self.open_name
        Edgebanding_Pointer_Name = 'Cabinet_Body_Edges' + self.open_name

        self.prompt('Left Side Thickness','IF(lfe,THICKNESS(sgi,"' + FE_Pointer_Name +'"),THICKNESS(sgi,"' + Side_Pointer_Name +'"))',[lfe,sgi])
        self.prompt('Right Side Thickness','IF(rfe,THICKNESS(sgi,"' + FE_Pointer_Name +'"),THICKNESS(sgi,"' + Side_Pointer_Name +'"))',[rfe,sgi])
        if self.carcass_type == "Sink":
            self.prompt('Top Thickness',value = 0)
        else:
            self.prompt('Top Thickness','THICKNESS(sgi,"' + Top_Pointer_Name +'")',[sgi])
        self.prompt('Bottom Thickness','THICKNESS(sgi,"' + Bottom_Pointer_Name +'")',[sgi])
        if self.carcass_type in {'Base','Sink','Tall'}:
            self.prompt('Toe Kick Thickness','THICKNESS(sgi,"Toe_Kick")',[sgi])
        self.prompt('Back Thickness','IF(remove_back,0,IF(use_thick_back,THICKNESS(sgi,"' + Thick_Back_Pointer_Name +'"),THICKNESS(sgi,"' + Back_Pointer_Name +'")))',[sgi,use_thick_back,remove_back])
        self.prompt('Thick Back Thickness','THICKNESS(sgi,"' + self.carcass_type + '_Thick_Back' + self.open_name +'")',[sgi])
        self.prompt('Filler Thickness','THICKNESS(sgi,"Filler")',[sgi])
        self.prompt('Nailer Thickness','THICKNESS(sgi,"Nailer")',[sgi])
        if self.carcass_type in {'Tall','Upper'}:
            self.prompt('Valance Thickness','THICKNESS(sgi,"Valance")',[sgi])
        self.prompt('Edgebanding Thickness','EDGE_THICKNESS(sgi,"' + Edgebanding_Pointer_Name + '")',[sgi])
        
        if self.carcass_type == 'Base':
            self.prompt('Top Inset','tt',[tt])
            self.prompt('Bottom Inset','kick_height+bt',[kick_height,bt])
        if self.carcass_type == 'Sink':
            Sub_Front_Height = self.get_var("Sub Front Height")
            self.prompt('Top Inset','Sub_Front_Height',[Sub_Front_Height])
            self.prompt('Bottom Inset','kick_height+bt',[kick_height,bt])
        if self.carcass_type == 'Tall':
            self.prompt('Top Inset','vht+tt',[vht,tt])
            self.prompt('Bottom Inset','kick_height+bt',[kick_height,bt])
        if self.carcass_type == 'Upper':
            self.prompt('Top Inset','vht+tt',[vht,tt])
            self.prompt('Bottom Inset','IF(Remove_Bottom,0,vhb+bt)',[vhb,bt,Remove_Bottom])
        if self.carcass_type == 'Suspended':
            self.prompt('Top Inset','tt',[tt])
            self.prompt('Bottom Inset','IF(Remove_Bottom,0,bt)',[bt,Remove_Bottom])
        
        self.prompt('Back Inset','IF(use_nailers,nt,0)+IF(remove_back,0,IF(use_thick_back,tbkt,bkt))',[use_nailers,nt,bkt,tbkt,use_thick_back,remove_back])
    
    def add_base_sides(self):
        g = bpy.context.scene.lm_carcass
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Toe_Kick_Height = self.get_var('Toe Kick Height')
        Toe_Kick_Setback = self.get_var('Toe Kick Setback')
        Left_Fin_End = self.get_var('Left Fin End')
        Right_Fin_End = self.get_var('Right Fin End')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Right_Side_Thickness = self.get_var('Right Side Thickness')
        Cabinet_Depth_Left = self.get_var('Cabinet Depth Left')
        Cabinet_Depth_Right = self.get_var('Cabinet Depth Right')
        
        left_side = self.add_assembly(NOTCHED_SIDE if g.Use_Notched_Sides else PART_WITH_FRONT_EDGEBANDING)
        left_side.set_name(self.carcass_type + " Left Side")
        left_side.x_loc(value = 0)
        left_side.y_loc(value = 0)
        if g.Use_Notched_Sides:
            left_side.z_loc(value = 0)
            left_side.x_dim('Height',[Height])
            left_side.prompt('Notch X Dimension','Toe_Kick_Height',[Toe_Kick_Height])
            left_side.prompt('Notch Y Dimension','Toe_Kick_Setback',[Toe_Kick_Setback])
        else:
            left_side.z_loc('Toe_Kick_Height',[Toe_Kick_Height])
            left_side.x_dim('Height-Toe_Kick_Height',[Height,Toe_Kick_Height])
        left_side.x_rot(value = 0)
        left_side.y_rot(value = -90)
        left_side.z_rot(value = 0)
        left_side.y_dim('-Cabinet_Depth_Left',[Cabinet_Depth_Left])
        left_side.z_dim('-Left_Side_Thickness',[Left_Side_Thickness])
        left_side.prompt('Hide','IF(Left_Fin_End,True,False)',[Left_Fin_End])
        left_side.cutpart(self.carcass_type + "_Side")
        left_side.edgebanding('Cabinet_Body_Edges',l1=True)
        
        right_side = self.add_assembly(NOTCHED_SIDE if g.Use_Notched_Sides else PART_WITH_FRONT_EDGEBANDING)
        right_side.set_name(self.carcass_type + " Right Side")
        right_side.x_loc('Width',[Width])
        right_side.y_loc(value = 0)
        if g.Use_Notched_Sides:
            right_side.z_loc(value = 0)
            right_side.x_dim('Height',[Height])
            right_side.prompt('Notch X Dimension','Toe_Kick_Height',[Toe_Kick_Height])
            right_side.prompt('Notch Y Dimension','Toe_Kick_Setback',[Toe_Kick_Setback])
        else:
            right_side.z_loc('Toe_Kick_Height',[Toe_Kick_Height])
            right_side.x_dim('Height-Toe_Kick_Height',[Height,Toe_Kick_Height])
        right_side.x_rot(value = 0)
        right_side.y_rot(value = -90)
        right_side.z_rot(value = 0)
        right_side.x_dim(value = 0)
        right_side.y_dim('-Cabinet_Depth_Right',[Cabinet_Depth_Right])
        right_side.z_dim('Right_Side_Thickness',[Right_Side_Thickness])
        right_side.prompt('Hide','IF(Right_Fin_End,True,False)',[Right_Fin_End])
        right_side.cutpart(self.carcass_type + "_Side")
        right_side.edgebanding('Cabinet_Body_Edges',l1=True)
        
        left_fe = self.add_assembly(NOTCHED_SIDE if g.Use_Notched_Sides else PART_WITH_FRONT_EDGEBANDING)
        left_fe.set_name(self.carcass_type + " Left FE")
        left_fe.x_loc(value = 0)
        left_fe.y_loc(value = 0)
        if g.Use_Notched_Sides:
            left_fe.z_loc(value = 0)
            left_fe.x_dim('Height',[Height])
            left_fe.prompt('Notch X Dimension','Toe_Kick_Height',[Toe_Kick_Height])
            left_fe.prompt('Notch Y Dimension','Toe_Kick_Setback',[Toe_Kick_Setback])
        else:
            left_fe.z_loc('Toe_Kick_Height',[Toe_Kick_Height])
            left_fe.x_dim('Height-Toe_Kick_Height',[Height,Toe_Kick_Height])
        left_fe.x_rot(value = 0)
        left_fe.y_rot(value = -90)
        left_fe.z_rot(value = 0)
        left_fe.x_dim(value = 0)
        left_fe.y_dim('-Cabinet_Depth_Left',[Cabinet_Depth_Left])
        left_fe.z_dim('-Left_Side_Thickness',[Left_Side_Thickness])
        left_fe.prompt('Hide','IF(Left_Fin_End,False,True)',[Left_Fin_End])
        left_fe.cutpart(self.carcass_type + "_Side_FE")
        left_fe.edgebanding('Cabinet_Body_Edges',l1=True)
        
        right_fe = self.add_assembly(NOTCHED_SIDE if g.Use_Notched_Sides else PART_WITH_FRONT_EDGEBANDING)
        right_fe.set_name(self.carcass_type + " Right FE")
        right_fe.x_loc('Width',[Width])
        right_fe.y_loc(value = 0)
        if g.Use_Notched_Sides:
            right_fe.z_loc(value = 0)
            right_fe.x_dim('Height',[Height])
            right_fe.prompt('Notch X Dimension','Toe_Kick_Height',[Toe_Kick_Height])
            right_fe.prompt('Notch Y Dimension','Toe_Kick_Setback',[Toe_Kick_Setback])
        else:
            right_fe.z_loc('Toe_Kick_Height',[Toe_Kick_Height])
            right_fe.x_dim('Height-Toe_Kick_Height',[Height,Toe_Kick_Height])
        right_fe.x_rot(value = 0)
        right_fe.y_rot(value = -90)
        right_fe.z_rot(value = 0)
        right_fe.x_dim(value = 0)
        right_fe.y_dim('-Cabinet_Depth_Right',[Cabinet_Depth_Right])
        right_fe.z_dim('Right_Side_Thickness',[Right_Side_Thickness])
        right_fe.prompt('Hide','IF(Right_Fin_End,False,True)',[Right_Fin_End])
        right_fe.cutpart(self.carcass_type + "_Side_FE")
        right_fe.edgebanding('Cabinet_Body_Edges',l1=True)
        
    def add_tall_sides(self):
        g = bpy.context.scene.lm_carcass
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Toe_Kick_Height = self.get_var('Toe Kick Height')
        Toe_Kick_Setback = self.get_var('Toe Kick Setback')
        Left_Fin_End = self.get_var('Left Fin End')
        Right_Fin_End = self.get_var('Right Fin End')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Right_Side_Thickness = self.get_var('Right Side Thickness')
        Left_Side_Full_Height = self.get_var('Left Side Full Height')
        Right_Side_Full_Height = self.get_var('Right Side Full Height')
        Top_Inset = self.get_var('Top Inset')
        Top_Thickness = self.get_var('Top Thickness')
        Cabinet_Depth_Left = self.get_var('Cabinet Depth Left')
        Cabinet_Depth_Right = self.get_var('Cabinet Depth Right')
        
        left_side = self.add_assembly(NOTCHED_SIDE if g.Use_Notched_Sides else PART_WITH_FRONT_EDGEBANDING)
        left_side.set_name(self.carcass_type + " Left Side")
        left_side.x_loc(value = 0)
        left_side.y_loc(value = 0)
        if g.Use_Notched_Sides:
            left_side.z_loc(value = 0)
            left_side.x_dim('Height+IF(Left_Side_Full_Height,0,-Top_Inset+Top_Thickness)',[Height,Top_Inset,Top_Thickness,Left_Side_Full_Height])
            left_side.prompt('Notch X Dimension','Toe_Kick_Height',[Toe_Kick_Height])
            left_side.prompt('Notch Y Dimension','Toe_Kick_Setback',[Toe_Kick_Setback])
        else:
            left_side.z_loc('Toe_Kick_Height',[Toe_Kick_Height])
            left_side.x_dim('Height-Toe_Kick_Height+IF(Left_Side_Full_Height,0,-Top_Inset+Top_Thickness)',[Left_Side_Full_Height,Height,Toe_Kick_Height,Top_Thickness,Top_Inset])
        left_side.x_rot(value = 0)
        left_side.y_rot(value = -90)
        left_side.z_rot(value = 0)
        left_side.y_dim('-Cabinet_Depth_Left',[Cabinet_Depth_Left])
        left_side.z_dim('-Left_Side_Thickness',[Left_Side_Thickness])
        left_side.prompt('Hide','IF(Left_Fin_End,True,False)',[Left_Fin_End])
        left_side.cutpart(self.carcass_type + "_Side")
        left_side.edgebanding('Cabinet_Body_Edges',l1=True)
        
        right_side = self.add_assembly(NOTCHED_SIDE if g.Use_Notched_Sides else PART_WITH_FRONT_EDGEBANDING)
        right_side.set_name(self.carcass_type + " Right Side")
        right_side.x_loc('Width',[Width])
        right_side.y_loc(value = 0)
        if g.Use_Notched_Sides:
            right_side.z_loc(value = 0)
            right_side.x_dim('Height+IF(Right_Side_Full_Height,0,-Top_Inset+Top_Thickness)',[Height,Top_Inset,Top_Thickness,Right_Side_Full_Height])
            right_side.prompt('Notch X Dimension','Toe_Kick_Height',[Toe_Kick_Height])
            right_side.prompt('Notch Y Dimension','Toe_Kick_Setback',[Toe_Kick_Setback])
        else:
            right_side.z_loc('Toe_Kick_Height',[Toe_Kick_Height])
            right_side.x_dim('Height-Toe_Kick_Height+IF(Right_Side_Full_Height,0,-Top_Inset+Top_Thickness)',[Right_Side_Full_Height,Top_Thickness,Top_Inset,Height,Toe_Kick_Height])
        right_side.x_rot(value = 0)
        right_side.y_rot(value = -90)
        right_side.z_rot(value = 0)
        right_side.x_dim(value = 0)
        right_side.y_dim('-Cabinet_Depth_Right',[Cabinet_Depth_Right])
        right_side.z_dim('Right_Side_Thickness',[Right_Side_Thickness])
        right_side.prompt('Hide','IF(Right_Fin_End,True,False)',[Right_Fin_End])
        right_side.cutpart(self.carcass_type + "_Side")
        right_side.edgebanding('Cabinet_Body_Edges',l1=True)
        
        left_fe = self.add_assembly(NOTCHED_SIDE if g.Use_Notched_Sides else PART_WITH_FRONT_EDGEBANDING)
        left_fe.set_name(self.carcass_type + " Left FE")
        left_fe.x_loc(value = 0)
        left_fe.y_loc(value = 0)
        if g.Use_Notched_Sides:
            left_fe.z_loc(value = 0)
            left_fe.x_dim('Height',[Height])
            left_fe.prompt('Notch X Dimension','Toe_Kick_Height',[Toe_Kick_Height])
            left_fe.prompt('Notch Y Dimension','Toe_Kick_Setback',[Toe_Kick_Setback])
        else:
            left_fe.z_loc('Toe_Kick_Height',[Toe_Kick_Height])
            left_fe.x_dim('Height-Toe_Kick_Height',[Height,Toe_Kick_Height])
        left_fe.x_rot(value = 0)
        left_fe.y_rot(value = -90)
        left_fe.z_rot(value = 0)
        left_fe.x_dim(value = 0)
        left_fe.y_dim('-Cabinet_Depth_Left',[Cabinet_Depth_Left])
        left_fe.z_dim('-Left_Side_Thickness',[Left_Side_Thickness])
        left_fe.prompt('Hide','IF(Left_Fin_End,False,True)',[Left_Fin_End])
        left_fe.cutpart(self.carcass_type + "_Side_FE")
        left_fe.edgebanding('Cabinet_Body_Edges',l1=True)
        
        right_fe = self.add_assembly(NOTCHED_SIDE if g.Use_Notched_Sides else PART_WITH_FRONT_EDGEBANDING)
        right_fe.set_name(self.carcass_type + " Right FE")
        right_fe.x_loc('Width',[Width])
        right_fe.y_loc(value = 0)
        if g.Use_Notched_Sides:
            right_fe.z_loc(value = 0)
            right_fe.x_dim('Height',[Height])
            right_fe.prompt('Notch X Dimension','Toe_Kick_Height',[Toe_Kick_Height])
            right_fe.prompt('Notch Y Dimension','Toe_Kick_Setback',[Toe_Kick_Setback])
        else:
            right_fe.z_loc('Toe_Kick_Height',[Toe_Kick_Height])
            right_fe.x_dim('Height-Toe_Kick_Height',[Height,Toe_Kick_Height])
        right_fe.x_rot(value = 0)
        right_fe.y_rot(value = -90)
        right_fe.z_rot(value = 0)
        right_fe.x_dim(value = 0)
        right_fe.y_dim('-Cabinet_Depth_Right',[Cabinet_Depth_Right])
        right_fe.z_dim('Right_Side_Thickness',[Right_Side_Thickness])
        right_fe.prompt('Hide','IF(Right_Fin_End,False,True)',[Right_Fin_End])
        right_fe.cutpart(self.carcass_type + "_Side_FE")
        right_fe.edgebanding('Cabinet_Body_Edges',l1=True)
        
    def add_upper_sides(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Left_Fin_End = self.get_var('Left Fin End')
        Right_Fin_End = self.get_var('Right Fin End')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Right_Side_Thickness = self.get_var('Right Side Thickness')
        Left_Side_Full_Height = self.get_var('Left Side Full Height')
        Right_Side_Full_Height = self.get_var('Right Side Full Height')
        Valance_Height_Top = self.get_var('Valance Height Top')
        Valance_Height_Bottom = self.get_var('Valance Height Bottom')
        Cabinet_Depth_Left = self.get_var('Cabinet Depth Left')
        Cabinet_Depth_Right = self.get_var('Cabinet Depth Right')
        
        left_side = self.add_assembly(PART_WITH_FRONT_AND_BOTTOM_EDGEBANDING)
        left_side.set_name(self.carcass_type + " Left Side")
        left_side.x_loc(value = 0)
        left_side.y_loc(value = 0)
        left_side.z_loc('IF(Left_Side_Full_Height,0,-Valance_Height_Top)',[Left_Side_Full_Height,Valance_Height_Top])
        left_side.x_rot(value = 0)
        left_side.y_rot(value = -90)
        left_side.z_rot(value = 0)
        left_side.x_dim('Height+IF(Left_Side_Full_Height,0,Valance_Height_Top+Valance_Height_Bottom)',[Height,Valance_Height_Bottom,Valance_Height_Top,Left_Side_Full_Height])
        left_side.y_dim('-Cabinet_Depth_Left',[Cabinet_Depth_Left])
        left_side.z_dim('-Left_Side_Thickness',[Left_Side_Thickness])
        left_side.prompt('Hide','IF(Left_Fin_End,True,False)',[Left_Fin_End])
        left_side.cutpart(self.carcass_type + "_Side")
        left_side.edgebanding('Cabinet_Body_Edges',l1=True)
        
        right_side = self.add_assembly(PART_WITH_FRONT_AND_BOTTOM_EDGEBANDING)
        right_side.set_name(self.carcass_type + " Right Side")
        right_side.x_loc('Width',[Width])
        right_side.y_loc(value = 0)
        right_side.z_loc('IF(Right_Side_Full_Height,0,-Valance_Height_Top)',[Right_Side_Full_Height,Valance_Height_Top])
        right_side.x_rot(value = 0)
        right_side.y_rot(value = -90)
        right_side.z_rot(value = 0)
        right_side.x_dim('Height+IF(Right_Side_Full_Height,0,Valance_Height_Top+Valance_Height_Bottom)',[Height,Right_Side_Full_Height,Valance_Height_Top,Valance_Height_Bottom])
        right_side.y_dim('-Cabinet_Depth_Right',[Cabinet_Depth_Right])
        right_side.z_dim('Right_Side_Thickness',[Right_Side_Thickness])
        right_side.prompt('Hide','IF(Right_Fin_End,True,False)',[Right_Fin_End])
        right_side.cutpart(self.carcass_type + "_Side")
        right_side.edgebanding('Cabinet_Body_Edges',l1=True)
        
        left_fe = self.add_assembly(PART_WITH_FRONT_AND_BOTTOM_EDGEBANDING)
        left_fe.set_name(self.carcass_type + " Left FE")
        left_fe.x_loc(value = 0)
        left_fe.y_loc(value = 0)
        left_fe.z_loc(value = 0)
        left_fe.x_rot(value = 0)
        left_fe.y_rot(value = -90)
        left_fe.z_rot(value = 0)
        left_fe.x_dim('Height',[Height])
        left_fe.y_dim('-Cabinet_Depth_Left',[Cabinet_Depth_Left])
        left_fe.z_dim('-Left_Side_Thickness',[Left_Side_Thickness])
        left_fe.prompt('Hide','IF(Left_Fin_End,False,True)',[Left_Fin_End])
        left_fe.cutpart(self.carcass_type + "_Side_FE")
        left_fe.edgebanding('Cabinet_Body_Edges',l1=True)
        
        right_fe = self.add_assembly(PART_WITH_FRONT_AND_BOTTOM_EDGEBANDING)
        right_fe.set_name(self.carcass_type + " Right FE")
        right_fe.x_loc('Width',[Width])
        right_fe.y_loc(value = 0)
        right_fe.z_loc(value = 0)
        right_fe.x_rot(value = 0)
        right_fe.y_rot(value = -90)
        right_fe.z_rot(value = 0)
        right_fe.x_dim('Height',[Height])
        right_fe.y_dim('-Cabinet_Depth_Right',[Cabinet_Depth_Right])
        right_fe.z_dim('Right_Side_Thickness',[Right_Side_Thickness])
        right_fe.prompt('Hide','IF(Right_Fin_End,False,True)',[Right_Fin_End])
        right_fe.cutpart(self.carcass_type + "_Side_FE")
        right_fe.edgebanding('Cabinet_Body_Edges',l1=True)
        
    def add_suspended_sides(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Left_Fin_End = self.get_var('Left Fin End')
        Right_Fin_End = self.get_var('Right Fin End')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Right_Side_Thickness = self.get_var('Right Side Thickness')
        Cabinet_Depth_Left = self.get_var('Cabinet Depth Left')
        Cabinet_Depth_Right = self.get_var('Cabinet Depth Right')

        left_side = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        left_side.set_name(self.carcass_type + " Left Side")
        left_side.x_loc(value = 0)
        left_side.y_loc(value = 0)
        left_side.z_loc(value = 0)
        left_side.x_rot(value = 0)
        left_side.y_rot(value = -90)
        left_side.z_rot(value = 0)
        left_side.x_dim('Height',[Height])
        left_side.y_dim('-Cabinet_Depth_Left',[Cabinet_Depth_Left])
        left_side.z_dim('-Left_Side_Thickness',[Left_Side_Thickness])
        left_side.prompt('Hide','IF(Left_Fin_End,True,False)',[Left_Fin_End])
        left_side.cutpart(self.carcass_type + "_Side")
        left_side.edgebanding('Cabinet_Body_Edges',l1=True)
        
        right_side = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        right_side.set_name(self.carcass_type + " Right Side")
        right_side.x_loc('Width',[Width])
        right_side.y_loc(value = 0)
        right_side.z_loc(value = 0)
        right_side.x_rot(value = 0)
        right_side.y_rot(value = -90)
        right_side.z_rot(value = 0)
        right_side.x_dim('Height',[Height])
        right_side.y_dim('-Cabinet_Depth_Right',[Cabinet_Depth_Right])
        right_side.z_dim('Right_Side_Thickness',[Right_Side_Thickness])
        right_side.prompt('Hide','IF(Right_Fin_End,True,False)',[Right_Fin_End])
        right_side.cutpart(self.carcass_type + "_Side")
        right_side.edgebanding('Cabinet_Body_Edges',l1=True)
        
        left_fe = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        left_fe.set_name(self.carcass_type + " Left FE")
        left_fe.x_loc(value = 0)
        left_fe.y_loc(value = 0)
        left_fe.z_loc(value = 0)
        left_fe.x_rot(value = 0)
        left_fe.y_rot(value = -90)
        left_fe.z_rot(value = 0)
        left_fe.x_dim('Height',[Height])
        left_fe.y_dim('-Cabinet_Depth_Left',[Cabinet_Depth_Left])
        left_fe.z_dim('-Left_Side_Thickness',[Left_Side_Thickness])
        left_fe.prompt('Hide','IF(Left_Fin_End,False,True)',[Left_Fin_End])
        left_fe.cutpart(self.carcass_type + "_Side_FE")
        left_fe.edgebanding('Cabinet_Body_Edges',l1=True)
        
        right_fe = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        right_fe.set_name(self.carcass_type + " Right FE")
        right_fe.x_loc('Width',[Width])
        right_fe.y_loc(value = 0)
        right_fe.z_loc(value = 0)
        right_fe.x_rot(value = 0)
        right_fe.y_rot(value = -90)
        right_fe.z_rot(value = 0)
        right_fe.x_dim('Height',[Height])
        right_fe.y_dim('-Cabinet_Depth_Right',[Cabinet_Depth_Right])
        right_fe.z_dim('Right_Side_Thickness',[Right_Side_Thickness])
        right_fe.prompt('Hide','IF(Right_Fin_End,False,True)',[Right_Fin_End])
        right_fe.cutpart(self.carcass_type + "_Side_FE")
        right_fe.edgebanding('Cabinet_Body_Edges',l1=True)
        
    def add_fillers(self):
        width = self.get_var('dim_x','width')
        height = self.get_var('dim_z','height')
        l_filler = self.get_var("Left Side Wall Filler",'l_filler')
        r_filler = self.get_var("Right Side Wall Filler",'r_filler')
        ft = self.get_var("Filler Thickness",'ft')
        if self.carcass_type in {'Base','Sink','Tall'}:
            kick_height = self.get_var("Toe Kick Height",'kick_height')
        Cabinet_Depth_Left = self.get_var('Cabinet Depth Left')
        Cabinet_Depth_Right = self.get_var('Cabinet Depth Right')
        
        left_filler = self.add_assembly(PART_WITH_NO_EDGEBANDING)
        left_filler.set_name("Left Filler")
        left_filler.x_loc(value = fd.inches(0))
        left_filler.y_loc('-Cabinet_Depth_Left',[Cabinet_Depth_Left])
        left_filler.z_loc('height',[height])
        left_filler.x_rot(value = 90)
        left_filler.y_rot(value = 90)
        left_filler.z_rot(value = 180)
        left_filler.y_dim('l_filler',[l_filler])
        left_filler.z_dim('ft',[ft])
        left_filler.prompt('Hide','IF(l_filler>0,False,True)',[l_filler])
        left_filler.cutpart('Filler')
        
        right_filler = self.add_assembly(PART_WITH_NO_EDGEBANDING)
        right_filler.set_name("Right Filler")
        right_filler.x_loc('width',[width])
        right_filler.y_loc('-Cabinet_Depth_Right',[Cabinet_Depth_Right])
        right_filler.z_loc('height',[height])
        right_filler.x_rot(value = 90)
        right_filler.y_rot(value = 90)
        right_filler.z_rot(value = 0)
        right_filler.y_dim('r_filler',[r_filler])
        right_filler.z_dim('-ft',[ft])
        right_filler.prompt('Hide','IF(r_filler>0,False,True)',[r_filler])
        right_filler.cutpart('Filler')
        
        if self.carcass_type in {'Base','Sink','Tall'}:
            left_filler.x_dim('height-kick_height',[height,kick_height])
            right_filler.x_dim('height-kick_height',[height,kick_height])
            
        if self.carcass_type in {'Upper','Suspended'}:
            left_filler.x_dim('height',[height])
            right_filler.x_dim('height',[height])
            
    def add_full_top(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Top_Thickness = self.get_var('Top Thickness')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Right_Side_Thickness = self.get_var('Right Side Thickness')
        Top_Inset = self.get_var('Top Inset')
        Cabinet_Depth_Left = self.get_var('Cabinet Depth Left')
        Cabinet_Depth_Right = self.get_var('Cabinet Depth Right')
        
        top = self.add_assembly(TRANSITION_PART)
        top.set_name(self.carcass_type + " Top")
        top.x_dim('Width-(Left_Side_Thickness+Right_Side_Thickness)',[Width,Left_Side_Thickness,Right_Side_Thickness])
        top.y_dim('Depth',[Depth])
        top.z_dim('-Top_Thickness',[Top_Thickness])
        top.x_loc('Left_Side_Thickness',[Left_Side_Thickness])
        top.y_loc(value = 0)
        top.z_loc('IF(Height>0,Height-Top_Inset+Top_Thickness,-Top_Inset+Top_Thickness)',[Height,Top_Inset,Top_Thickness])
        top.x_rot(value = 0)
        top.y_rot(value = 0)
        top.z_rot(value = 0)
        top.prompt("Left Depth",'Cabinet_Depth_Left',[Cabinet_Depth_Left])
        top.prompt("Right Depth",'Cabinet_Depth_Right',[Cabinet_Depth_Right])
        top.cutpart(self.carcass_type + "_Top")
        top.edgebanding('Cabinet_Body_Edges', l1 = True)
        
    def add_bottom(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Toe_Kick_Height = self.get_var('Toe Kick Height')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Right_Side_Thickness = self.get_var('Right Side Thickness')
        Bottom_Thickness = self.get_var('Bottom Thickness')
        Remove_Bottom = self.get_var('Remove Bottom')
        Cabinet_Depth_Left = self.get_var('Cabinet Depth Left')
        Cabinet_Depth_Right = self.get_var('Cabinet Depth Right')
        
        bottom = self.add_assembly(TRANSITION_PART)
        bottom.set_name(self.carcass_type + " Bottom")
        bottom.x_dim('Width-(Left_Side_Thickness+Right_Side_Thickness)',[Width,Left_Side_Thickness,Right_Side_Thickness])
        bottom.y_dim('Depth',[Depth])
        bottom.z_dim('Bottom_Thickness',[Bottom_Thickness])
        bottom.x_loc('Left_Side_Thickness',[Left_Side_Thickness])
        bottom.y_loc(value = 0)
        bottom.x_rot(value = 0)
        bottom.y_rot(value = 0)
        bottom.z_rot(value = 0)
        bottom.prompt('Hide','Remove_Bottom',[Remove_Bottom])
        bottom.prompt("Left Depth",'Cabinet_Depth_Left',[Cabinet_Depth_Left])
        bottom.prompt("Right Depth",'Cabinet_Depth_Right',[Cabinet_Depth_Right])
        bottom.cutpart(self.carcass_type + "_Bottom")
        bottom.edgebanding('Cabinet_Body_Edges', l1 = True)
        
        if self.carcass_type in {'Upper','Suspended'}:
            Bottom_Inset = self.get_var('Bottom Inset')
            bottom.z_loc('Height+Bottom_Inset-Bottom_Thickness',[Height,Bottom_Inset,Bottom_Thickness])
            
        if self.carcass_type in {'Base','Tall','Sink'}:
            bottom.z_loc('Toe_Kick_Height',[Toe_Kick_Height])
            
    def add_toe_kick(self):
        Width = self.get_var('dim_x','Width')
        Toe_Kick_Height = self.get_var('Toe Kick Height')
        Toe_Kick_Setback = self.get_var('Toe Kick Setback')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Right_Side_Thickness = self.get_var('Right Side Thickness')
        Remove_Bottom = self.get_var('Remove Bottom')
        Cabinet_Depth_Left = self.get_var('Cabinet Depth Left')
        Cabinet_Depth_Right = self.get_var('Cabinet Depth Right')
        
        kick = self.add_assembly(PART_WITH_NO_EDGEBANDING)
        kick.set_name("Toe Kick")
        kick.x_dim('sqrt(((Cabinet_Depth_Left-Cabinet_Depth_Right)**2)+((Width-(Left_Side_Thickness+Right_Side_Thickness))**2))',[Cabinet_Depth_Left,Cabinet_Depth_Right,Width,Left_Side_Thickness,Right_Side_Thickness])
        kick.y_dim('Toe_Kick_Height',[Toe_Kick_Height])
        kick.z_dim(value = fd.inches(-.75))
        kick.x_loc('Left_Side_Thickness',[Left_Side_Thickness])
        kick.y_loc('-Cabinet_Depth_Left+Toe_Kick_Setback',[Cabinet_Depth_Left,Toe_Kick_Setback])
        kick.z_loc(value = 0)
        kick.x_rot(value = 90)
        kick.y_rot(value = 0)
        kick.z_rot('atan((Cabinet_Depth_Left-Cabinet_Depth_Right)/(Width-(Left_Side_Thickness+Right_Side_Thickness)))',[Cabinet_Depth_Left,Cabinet_Depth_Right,Width,Left_Side_Thickness,Right_Side_Thickness])
        kick.prompt('Hide','Remove_Bottom',[Remove_Bottom])
        kick.cutpart("Toe_Kick")
        
    def add_back(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Right_Side_Thickness = self.get_var('Right Side Thickness')
        Top_Inset = self.get_var('Top Inset')
        Bottom_Inset = self.get_var('Bottom Inset')
        Back_Thickness = self.get_var('Back Thickness')
        Bottom_Thickness = self.get_var('Bottom Thickness')
        Top_Thickness = self.get_var('Top Thickness')
        Use_Nailers = self.get_var('Use Nailers')
        Nailer_Thickness = self.get_var('Nailer Thickness')
        Remove_Back = self.get_var('Remove Back')
        Remove_Bottom = self.get_var('Remove Bottom')
        Toe_Kick_Height = self.get_var('Toe Kick Height')
        
        back = self.add_assembly(PART_WITH_NO_EDGEBANDING)
        back.set_name(self.carcass_type + " Back")
        back.x_loc('Left_Side_Thickness',[Left_Side_Thickness])
        back.y_loc('IF(Use_Nailers,-Nailer_Thickness,0)',[Use_Nailers,Nailer_Thickness])
        back.x_rot(value = 0)
        back.y_rot(value = -90)
        back.z_rot(value = -90)
        
        if self.carcass_type in {'Base','Sink'}:
            back.x_dim('fabs(Height)-IF(Remove_Bottom,0,Toe_Kick_Height+Bottom_Thickness)-Top_Thickness',[Height,Toe_Kick_Height,Bottom_Thickness,Remove_Bottom,Top_Thickness])
        
        if self.carcass_type == 'Tall':
            back.x_dim('fabs(Height)-IF(Remove_Bottom,0,Toe_Kick_Height+Bottom_Thickness)-Top_Inset',[Height,Top_Inset,Toe_Kick_Height,Bottom_Thickness,Remove_Bottom])
        
        if self.carcass_type in {'Upper','Suspended'}:
            back.x_dim('fabs(Height)-(Top_Inset+Bottom_Inset)',[Height,Top_Inset,Bottom_Inset])
            
        back.y_dim('Width-(Left_Side_Thickness+Right_Side_Thickness)',[Width,Left_Side_Thickness,Right_Side_Thickness])
        back.z_dim('-Back_Thickness',[Back_Thickness])
        back.cutpart(self.carcass_type + "_Back" + self.open_name)
        back.edgebanding('Cabinet_Body_Edges', l1 = True)
        back.prompt('Hide','IF(Remove_Back,True,False)',[Remove_Back])
        
        if self.carcass_type in {'Base','Tall','Sink'}:
            back.z_loc('IF(Remove_Bottom,0,Toe_Kick_Height+Bottom_Thickness)',[Remove_Bottom,Toe_Kick_Height,Bottom_Thickness])
        
        if self.carcass_type in {'Upper','Suspended'}:
            back.z_loc('Height+Bottom_Inset',[Height,Bottom_Inset])
    
    def add_nailers(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Right_Side_Thickness = self.get_var('Right Side Thickness')
        Top_Thickness = self.get_var('Top Thickness')
        Top_Inset = self.get_var('Top Inset')
        Bottom_Inset = self.get_var('Bottom Inset')
        Remove_Bottom = self.get_var('Remove Bottom')
        Use_Nailers = self.get_var('Use Nailers')
        Nailer_Thickness = self.get_var('Nailer Thickness')
        Nailer_Width = self.get_var('Nailer Width')
        Center_Nailer_Switch = self.get_var('Center Nailer Switch')
        
        top_n = self.add_assembly(PART_WITH_NO_EDGEBANDING)
        top_n.set_name("Top Nailer")
        top_n.x_loc('Left_Side_Thickness',[Left_Side_Thickness])
        top_n.y_loc('IF(Use_Nailers,-Nailer_Thickness,0)',[Use_Nailers,Nailer_Thickness])
        if self.carcass_type in {'Base','Sink'}:
            top_n.z_loc('Height-Top_Thickness',[Height,Top_Thickness])
        if self.carcass_type in {'Upper','Tall'}:
            top_n.z_loc('IF(Height>0,Height-Top_Inset,-Top_Inset)',[Height,Top_Inset])
        top_n.x_rot(value = 90)
        top_n.y_rot(value = 0)
        top_n.z_rot(value = 0)
        top_n.x_dim('Width-(Left_Side_Thickness+Right_Side_Thickness)',[Width,Left_Side_Thickness,Right_Side_Thickness])
        top_n.y_dim('-Nailer_Width',[Nailer_Width])
        top_n.z_dim('-Nailer_Thickness',[Nailer_Thickness])
        top_n.prompt('Hide','IF(Use_Nailers,False,True)',[Use_Nailers])
        top_n.cutpart("Nailer")
    
        center_n = self.add_assembly(PART_WITH_NO_EDGEBANDING)
        center_n.set_name("Center Nailer")
        center_n.x_loc('Left_Side_Thickness',[Left_Side_Thickness])
        center_n.y_loc('IF(Use_Nailers,-Nailer_Thickness,0)',[Use_Nailers,Nailer_Thickness])
        center_n.z_loc('IF(Height>0,(Height/2)-(Nailer_Width/2)+(Bottom_Inset/2),(Height/2)-(Nailer_Width/2))',[Height,Nailer_Width,Bottom_Inset])
        center_n.x_rot(value = 90)
        center_n.y_rot(value = 0)
        center_n.z_rot(value = 0)
        center_n.x_dim('Width-(Left_Side_Thickness+Right_Side_Thickness)',[Width,Left_Side_Thickness,Right_Side_Thickness])
        center_n.y_dim('Nailer_Width',[Nailer_Width])
        center_n.z_dim('-Nailer_Thickness',[Nailer_Thickness])
        center_n.prompt('Hide','IF(Use_Nailers,IF(Height>Center_Nailer_Switch,False,True),True)',[Height,Center_Nailer_Switch,Use_Nailers])
        center_n.cutpart("Nailer")
    
        bottom_n = self.add_assembly(PART_WITH_NO_EDGEBANDING)
        bottom_n.set_name("Bottom Nailer")
        bottom_n.x_loc('Left_Side_Thickness',[Left_Side_Thickness])
        bottom_n.y_loc('IF(Use_Nailers,-Nailer_Thickness,0)',[Use_Nailers,Nailer_Thickness])
        bottom_n.z_loc('IF(Height>0,IF(Remove_Bottom,0,Bottom_Inset),Height+Bottom_Inset)',[Height,Bottom_Inset,Remove_Bottom])
        bottom_n.x_rot(value = 90)
        bottom_n.y_rot(value = 0)
        bottom_n.z_rot(value = 0)
        bottom_n.x_dim('Width-(Left_Side_Thickness+Right_Side_Thickness)',[Width,Left_Side_Thickness,Right_Side_Thickness])
        bottom_n.y_dim('Nailer_Width',[Nailer_Width])
        bottom_n.z_dim('-Nailer_Thickness',[Nailer_Thickness])
        bottom_n.prompt('Hide','IF(Use_Nailers,False,True)',[Use_Nailers])
        bottom_n.cutpart("Nailer")
    
    def add_valances(self):
        width = self.get_var('dim_x','width')
        Height = self.get_var('dim_z','Height')
        Top_Inset = self.get_var('Top Inset')
        Top_Thickness = self.get_var('Top Thickness')
        Valance_Thickness = self.get_var("Valance Thickness")
        Valance_Each_Unit = self.get_var("Valance Each Unit")
        Valance_Height_Top = self.get_var("Valance Height Top")
        Valance_Height_Bottom = self.get_var("Valance Height Bottom")
        
        ld = self.get_var('Cabinet Depth Left','ld')
        rd = self.get_var('Cabinet Depth Right','rd')
        lst = self.get_var('Left Side Thickness','lst')
        rst = self.get_var('Right Side Thickness','rst')
        
        top_val = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        top_val.set_name("Top Valance")
        top_val.x_loc('lst',[lst])
        top_val.y_loc('-ld',[ld])
        top_val.z_loc('IF(Height>0,Height-Top_Inset+Top_Thickness,-Top_Inset+Top_Thickness)',[Height,Top_Thickness,Top_Inset])
        top_val.x_rot(value = 90)
        top_val.y_rot(value = 0)
        top_val.z_rot('atan((ld-rd)/(width-lst-rst))',[rd,ld,width,lst,rst])
        top_val.x_dim('sqrt(((ld-rd)**2)+((width-lst-rst)**2))',[lst,rst,width,ld,rd])
        top_val.y_dim('Valance_Height_Top',[Valance_Height_Top])
        top_val.z_dim('-Valance_Thickness',[Valance_Thickness])
        top_val.prompt('Hide','IF(AND(Valance_Each_Unit,Valance_Height_Top>0),False,True)',[Valance_Each_Unit,Valance_Height_Top])
        top_val.cutpart("Valance")
        top_val.edgebanding('Cabinet_Body_Edges',l1=True)
        
        if self.carcass_type == 'Upper':
            bottom_val = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
            bottom_val.set_name("Bottom Valance")
            bottom_val.x_loc('lst',[lst])
            bottom_val.y_loc('-ld',[ld])
            bottom_val.z_loc('Height+Valance_Height_Bottom',[Height,Valance_Height_Bottom])
            bottom_val.x_rot(value = 90)
            bottom_val.y_rot(value = 0)
            bottom_val.z_rot('atan((ld-rd)/(width-lst-rst))',[rd,ld,width,lst,rst])
            bottom_val.x_dim('sqrt(((ld-rd)**2)+((width-lst-rst)**2))',[lst,rst,width,ld,rd])
            bottom_val.y_dim('-Valance_Height_Bottom',[Valance_Height_Bottom])
            bottom_val.z_dim('-Valance_Thickness',[Valance_Thickness])
            bottom_val.prompt('Hide','IF(AND(Valance_Each_Unit,Valance_Height_Bottom>0),False,True)',[Valance_Each_Unit,Valance_Height_Bottom])
            bottom_val.cutpart("Valance")
            bottom_val.edgebanding('Cabinet_Body_Edges',l1=True)
            
    def draw(self):
        g = bpy.context.scene.lm_carcass
        self.create_assembly()

        self.add_common_carcass_prompts()
        if self.carcass_type == "Base":
            self.add_base_assembly_prompts()

            self.add_full_top()
            if g.Use_Notched_Sides:
                self.add_toe_kick()
            self.add_base_sides()
#             if g.Use_Leg_Levelers:
#                 self.add_leg_levelers()

        if self.carcass_type == "Tall":
            self.add_base_assembly_prompts()
            self.add_full_top()
            self.add_valance_prompts(add_bottom_valance=False)
            if g.Use_Notched_Sides:
                self.add_toe_kick()
            self.add_tall_sides()
#             if g.Use_Leg_Levelers:
#                 self.add_leg_levelers()
            self.add_valances()
                
        if self.carcass_type == "Upper":
            self.flip_z = True
            self.add_full_top()
            self.add_valance_prompts(add_bottom_valance=True)
            self.add_valances()
            self.add_upper_sides()
            
        if self.carcass_type == "Sink":
            self.add_base_assembly_prompts()
            self.add_sink_prompts()
            self.add_sink_top()
            if g.Use_Notched_Sides:
                self.add_toe_kick()
            self.add_base_sides()
#             if g.Use_Leg_Levelers:
#                 self.add_leg_levelers()
                
        if self.carcass_type == "Suspended":
            self.flip_z = True
            self.add_finger_pull_prompts()
            self.add_suspended_sides()
            self.add_full_top()

        self.add_fillers()
        self.add_bottom()
        self.add_back()
        self.add_nailers()
        self.add_prompt_formuls()
        
        self.update()
        
class Inside_Corner_Carcass(fd.Library_Assembly):
    
    library_name = "Carcasses"
    placement_type = ""
    type_assembly = "INSERT"
    
    carcass_type = "" # {Base, Tall, Upper}
    open_name = ""
    
    carcass_shape = "" # {Notched, Diagonal}
    left_right_depth = fd.inches(23)
    
    def add_common_carcass_prompts(self):
        g = bpy.context.scene.lm_carcass
        
        self.add_tab(name='Carcass Options',tab_type='VISIBLE')
        self.add_tab(name='Formulas',tab_type='HIDDEN')
        self.add_tab(name='Machining Options',tab_type='HIDDEN')
        self.add_prompt(name="Left Fin End",prompt_type='CHECKBOX',value=False,tab_index=0)
        self.add_prompt(name="Right Fin End",prompt_type='CHECKBOX',value=False,tab_index=0)
        self.add_prompt(name="Left Side Wall Filler",prompt_type='DISTANCE',value=0.0,tab_index=0)
        self.add_prompt(name="Right Side Wall Filler",prompt_type='DISTANCE',value=0.0,tab_index=0)
        
        self.add_prompt(name="Cabinet Depth Left",prompt_type='DISTANCE',value=self.left_right_depth,tab_index=0)
        self.add_prompt(name="Cabinet Depth Right",prompt_type='DISTANCE',value=self.left_right_depth,tab_index=0)
        
        self.add_prompt(name="Left Side Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Right Side Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Top Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Bottom Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Back Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Thick Back Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Filler Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Nailer Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Edgebanding Thickness",prompt_type='DISTANCE',value=fd.inches(.02),tab_index=1)
        self.add_prompt(name="Back Inset",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        self.add_prompt(name="Top Inset",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        self.add_prompt(name="Bottom Inset",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        
    def add_base_assembly_prompts(self):
        g = bpy.context.scene.lm_carcass
        self.add_prompt(name="Toe Kick Height",prompt_type='DISTANCE',value= g.Toe_Kick_Height,tab_index=0)
        self.add_prompt(name="Toe Kick Setback",prompt_type='DISTANCE',value= g.Toe_Kick_Setback,tab_index=0)
        self.add_prompt(name="Toe Kick Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
    
    def add_valance_prompts(self,add_bottom_valance):
        g = bpy.context.scene.lm_carcass
        self.add_prompt(name="Valance Height Top",prompt_type='DISTANCE',value=g.Valance_Height_Top,tab_index=0,export=True)
        self.add_prompt(name="Door Valance Top",prompt_type='CHECKBOX',value=g.Door_Valance_Top,tab_index=0,export=True)
        if add_bottom_valance:
            self.add_prompt(name="Valance Height Bottom",prompt_type='DISTANCE',value=g.Valance_Height_Bottom,tab_index=0,export=True)
            self.add_prompt(name="Door Valance Bottom",prompt_type='CHECKBOX',value=g.Door_Valance_Bottom,tab_index=0,export=True)
        self.add_prompt(name="Left Side Full Height",prompt_type='CHECKBOX',value=False,tab_index=0,export=True)
        self.add_prompt(name="Right Side Full Height",prompt_type='CHECKBOX',value=False,tab_index=0,export=True)
        self.add_prompt(name="Valance Each Unit",prompt_type='CHECKBOX',value=g.Valance_Each_Unit,tab_index=0,export=True)
        self.add_prompt(name="Valance Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
    
    def add_prompt_formuls(self):
        sgi = self.get_var('cabinetlib.spec_group_index','sgi')
        tt = self.get_var("Top Thickness",'tt')
        bt = self.get_var("Bottom Thickness",'bt')
        bkt = self.get_var("Back Thickness",'bkt')
        lfe = self.get_var("Left Fin End",'lfe')
        rfe = self.get_var("Right Fin End",'rfe')
        if self.carcass_type in {'Base','Sink','Tall'}:
            kick_height = self.get_var("Toe Kick Height",'kick_height')
        if self.carcass_type in {'Upper','Tall'}:
            vhb = self.get_var("Valance Height Bottom",'vhb')
            vht = self.get_var("Valance Height Top",'vht')
            
        Side_Pointer_Name = self.carcass_type + '_Side' + self.open_name
        FE_Pointer_Name = self.carcass_type + '_Side_FE' + self.open_name
        Top_Pointer_Name = self.carcass_type + '_Top' + self.open_name
        Bottom_Pointer_Name = self.carcass_type + '_Bottom' + self.open_name
        Thick_Back_Pointer_Name = self.carcass_type + '_Thick_Back' + self.open_name
        Edgebanding_Pointer_Name = 'Cabinet_Body_Edges' + self.open_name
        
        self.prompt('Left Side Thickness','IF(lfe,THICKNESS(sgi,"' + FE_Pointer_Name +'"),THICKNESS(sgi,"' + Side_Pointer_Name +'"))',[lfe,sgi])
        self.prompt('Right Side Thickness','IF(rfe,THICKNESS(sgi,"' + FE_Pointer_Name +'"),THICKNESS(sgi,"' + Side_Pointer_Name +'"))',[rfe,sgi])
        self.prompt('Top Thickness','THICKNESS(sgi,"' + Top_Pointer_Name +'")',[sgi])
        self.prompt('Bottom Thickness','THICKNESS(sgi,"' + Bottom_Pointer_Name +'")',[sgi])
        if self.carcass_type in {'Base','Sink','Tall'}:
            self.prompt('Toe Kick Thickness','THICKNESS(sgi,"Toe_Kick")',[sgi])
        if self.carcass_type == 'Sink':
            self.prompt('Sub Front Thickness','THICKNESS(sgi,"Sink_Sub_Front")',[sgi])
        self.prompt('Back Thickness','THICKNESS(sgi,"' + Thick_Back_Pointer_Name +'")',[sgi])
        self.prompt('Thick Back Thickness','THICKNESS(sgi,"' + self.carcass_type + '_Thick_Back' + self.open_name +'")',[sgi])
        self.prompt('Filler Thickness','THICKNESS(sgi,"Filler")',[sgi])
        self.prompt('Nailer Thickness','THICKNESS(sgi,"Nailer")',[sgi])
        if self.carcass_type in {'Tall','Upper'}:
            self.prompt('Valance Thickness','THICKNESS(sgi,"Valance")',[sgi])
        self.prompt('Edgebanding Thickness','EDGE_THICKNESS(sgi,"' + Edgebanding_Pointer_Name + '")',[sgi])
        
        if self.carcass_type == 'Base':
            self.prompt('Top Inset','tt',[tt])
            self.prompt('Bottom Inset','kick_height+bt',[kick_height,bt])
        if self.carcass_type == 'Sink':
            print('SINKS')
            self.prompt('Top Inset',value = fd.inches(.75))
            self.prompt('Bottom Inset','kick_height+bt',[kick_height,bt])
        if self.carcass_type == 'Tall':
            self.prompt('Top Inset','vht+tt',[vht,tt])
            self.prompt('Bottom Inset','kick_height+bt',[kick_height,bt])
        if self.carcass_type == 'Upper':
            self.prompt('Top Inset','vht+tt',[vht,tt])
            self.prompt('Bottom Inset','vhb+bt',[vhb,bt])
        if self.carcass_type == 'Suspended':
            self.prompt('Top Inset','tt',[tt])
            self.prompt('Bottom Inset','bt',[bt])
        
        self.prompt('Back Inset','bkt',[bkt])
    
    def add_sides(self):
        g = bpy.context.scene.lm_carcass
        width = self.get_var('dim_x','width')
        height = self.get_var('dim_z','height')
        depth = self.get_var('dim_y','depth')
        Toe_Kick_Height = self.get_var('Toe Kick Height')
        Toe_Kick_Setback = self.get_var('Toe Kick Setback')
        Left_Fin_End = self.get_var('Left Fin End')
        Right_Fin_End = self.get_var('Right Fin End')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Right_Side_Thickness = self.get_var('Right Side Thickness')
        Cabinet_Depth_Left = self.get_var("Cabinet Depth Left")
        Cabinet_Depth_Right = self.get_var("Cabinet Depth Right")
        sides = []
    
        if self.carcass_type in {"Base","Tall","Sink"}:
            left_side = self.add_assembly(NOTCHED_SIDE if g.Use_Notched_Sides else PART_WITH_FRONT_EDGEBANDING)
            left_side.set_name(self.carcass_type + " Left Side")
            left_side.y_loc('depth',[depth])
            left_side.x_dim('height',[height])
            left_side.y_dim('-Cabinet_Depth_Left',[Cabinet_Depth_Left])
            left_side.z_rot(value = 90)
            sides.append(left_side)
        
            right_side = self.add_assembly(NOTCHED_SIDE if g.Use_Notched_Sides else PART_WITH_FRONT_EDGEBANDING)
            right_side.set_name(self.carcass_type + " Right Side")
            right_side.x_dim('height',[height])
            right_side.y_dim('-Cabinet_Depth_Right',[Cabinet_Depth_Right])
            sides.append(right_side)
            
            left_fe = self.add_assembly(NOTCHED_SIDE if g.Use_Notched_Sides else PART_WITH_FRONT_EDGEBANDING)
            left_fe.set_name(self.carcass_type + " Left FE")
            left_fe.y_loc('depth',[depth])
            left_fe.x_dim('height',[height])
            left_fe.y_dim('-Cabinet_Depth_Left',[Cabinet_Depth_Left])
            left_fe.z_rot(value = 90)
            sides.append(left_fe)
            
            right_fe = self.add_assembly(NOTCHED_SIDE if g.Use_Notched_Sides else PART_WITH_FRONT_EDGEBANDING)
            right_fe.set_name(self.carcass_type + " Right FE")
            right_fe.x_dim('height',[height])
            right_fe.y_dim('-Cabinet_Depth_Right',[Cabinet_Depth_Right])
            sides.append(right_fe)
        
        if self.carcass_type in {"Upper","Suspended"}:
            left_side = self.add_assembly(PART_WITH_FRONT_AND_BOTTOM_EDGEBANDING)
            left_side.set_name(self.carcass_type + " Left Side")
            left_side.y_loc('depth',[depth])
            left_side.x_dim('height',[height])
            left_side.y_dim('-Cabinet_Depth_Left',[Cabinet_Depth_Left])
            left_side.z_rot(value = 90)
            sides.append(left_side)
        
            right_side = self.add_assembly(PART_WITH_FRONT_AND_BOTTOM_EDGEBANDING)
            right_side.set_name(self.carcass_type + " Right Side")
            right_side.x_dim('height',[height])
            right_side.y_dim('-Cabinet_Depth_Right',[Cabinet_Depth_Right])
            sides.append(right_side)
            
            left_fe = self.add_assembly(PART_WITH_FRONT_AND_BOTTOM_EDGEBANDING)
            left_fe.set_name(self.carcass_type + " Left FE")
            left_fe.y_loc('depth',[depth])
            left_fe.x_dim('height',[height])
            left_fe.y_dim('-Cabinet_Depth_Left',[Cabinet_Depth_Left])
            left_fe.z_rot(value = 90)
            sides.append(left_fe)
            
            right_fe = self.add_assembly(PART_WITH_FRONT_AND_BOTTOM_EDGEBANDING)
            right_fe.set_name(self.carcass_type + " Right FE")
            right_fe.x_dim('height',[height])
            right_fe.y_dim('-Cabinet_Depth_Right',[Cabinet_Depth_Right])
            sides.append(right_fe)
    
        for side in sides:
            side.x_loc(value = 0)
            side.y_loc(value = 0)
            side.z_loc(value = 0)
            side.x_rot(value = 0)
            side.y_rot(value = -90)
            side.edgebanding('Cabinet_Body_Edges',l1=True)
            if self.carcass_type in {'Base','Tall'}:
                side.prompt('Notch X Dimension','Toe_Kick_Height',[Toe_Kick_Height])
                side.prompt('Notch Y Dimension','Toe_Kick_Setback',[Toe_Kick_Setback])
            if "Left Side" in side.obj_bp.mv.name_object:
                side.prompt('Hide','IF(Left_Fin_End,True,False)',[Left_Fin_End])
                side.z_dim('-Left_Side_Thickness',[Left_Side_Thickness])
                side.cutpart(self.carcass_type + "_Side")
            if "Right Side" in side.obj_bp.mv.name_object:
                side.prompt('Hide','IF(Right_Fin_End,True,False)',[Right_Fin_End])
                side.z_dim('Right_Side_Thickness',[Right_Side_Thickness])
                side.cutpart(self.carcass_type + "_Side")
                side.x_loc('width',[width])
            if "Left FE" in side.obj_bp.mv.name_object:
                side.prompt('Hide','IF(Left_Fin_End,False,True)',[Left_Fin_End])
                side.z_dim('-Left_Side_Thickness',[Left_Side_Thickness])
                side.cutpart(self.carcass_type + "_Side_FE")
            if "Right FE" in side.obj_bp.mv.name_object:
                side.prompt('Hide','IF(Right_Fin_End,False,True)',[Right_Fin_End])
                side.z_dim('Right_Side_Thickness',[Right_Side_Thickness])
                side.cutpart(self.carcass_type + "_Side_FE")
                side.x_loc('width',[width])
                
    def add_fillers(self):
        Width = self.get_var('dim_x','Width')
        Depth = self.get_var('dim_y','Depth')
        Height = self.get_var('dim_z','Height')
        Left_Side_Wall_Filler = self.get_var("Left Side Wall Filler")
        Right_Side_Wall_Filler = self.get_var("Right Side Wall Filler")
        Filler_Thickness = self.get_var("Filler Thickness")
        Cabinet_Depth_Left = self.get_var("Cabinet Depth Left")
        Cabinet_Depth_Right = self.get_var("Cabinet Depth Right")
        
        if self.carcass_type in {'Base','Sink','Tall'}:
            Toe_Kick_Height = self.get_var("Toe Kick Height")
            
        left_filler = self.add_assembly(PART_WITH_NO_EDGEBANDING)
        left_filler.set_name("Left Filler")
        left_filler.x_loc('Cabinet_Depth_Left',[Cabinet_Depth_Left])
        left_filler.y_loc('Depth',[Depth])
        left_filler.z_loc('Height',[Height])
        left_filler.x_rot(value = 90)
        left_filler.y_rot(value = 90)
        left_filler.z_rot(value = -90)
        left_filler.y_dim('Left_Side_Wall_Filler',[Left_Side_Wall_Filler])
        left_filler.z_dim('Filler_Thickness',[Filler_Thickness])
        left_filler.prompt('Hide','IF(Left_Side_Wall_Filler>0,False,True)',[Left_Side_Wall_Filler])
        left_filler.cutpart('Filler')
        
        right_filler = self.add_assembly(PART_WITH_NO_EDGEBANDING)
        right_filler.set_name("Right Filler")
        right_filler.x_loc('Width',[Width])
        right_filler.y_loc('-Cabinet_Depth_Right',[Cabinet_Depth_Right])
        right_filler.z_loc('Height',[Height])
        right_filler.x_rot(value = 90)
        right_filler.y_rot(value = 90)
        right_filler.z_rot(value = 0)
        right_filler.y_dim('Right_Side_Wall_Filler',[Right_Side_Wall_Filler])
        right_filler.z_dim('-Filler_Thickness',[Filler_Thickness])
        right_filler.prompt('Hide','IF(Right_Side_Wall_Filler>0,False,True)',[Right_Side_Wall_Filler])
        right_filler.cutpart('Filler')
        
        if self.carcass_type in {'Base','Sink','Tall'}:
            left_filler.x_dim('Height-Toe_Kick_Height',[Height,Toe_Kick_Height])
            right_filler.x_dim('Height-Toe_Kick_Height',[Height,Toe_Kick_Height])
            
        if self.carcass_type in {'Upper','Suspended'}:
            left_filler.x_dim('Height',[Height])
            right_filler.x_dim('Height',[Height])
            
    def add_full_top(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Top_Thickness = self.get_var('Top Thickness')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Right_Side_Thickness = self.get_var('Right Side Thickness')
        Cabinet_Depth_Left = self.get_var("Cabinet Depth Left")
        Cabinet_Depth_Right = self.get_var("Cabinet Depth Right")
        
        if self.carcass_shape == 'Diagonal':
            top = self.add_assembly(CHAMFERED_PART)
        if self.carcass_shape == 'Notched':
            top = self.add_assembly(CORNER_NOTCH_PART)
        
        top.set_name(self.carcass_type + " Top")
        top.x_dim('Width-Right_Side_Thickness',[Width,Right_Side_Thickness])
        top.y_dim('Depth+Left_Side_Thickness',[Depth,Left_Side_Thickness])
        top.z_dim('-Top_Thickness',[Top_Thickness])
        top.x_loc(value = 0)
        top.y_loc(value = 0)
        top.z_loc('IF(Height>0,Height,0)',[Height])
        top.x_rot(value = 0)
        top.y_rot(value = 0)
        top.z_rot(value = 0)
        top.cutpart(self.carcass_type + "_Top")
        top.prompt('Left Depth','Cabinet_Depth_Left',[Cabinet_Depth_Left])
        top.prompt('Right Depth','Cabinet_Depth_Right',[Cabinet_Depth_Right])
        top.edgebanding('Cabinet_Body_Edges', l1 = True)
        
    def add_bottom(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Toe_Kick_Height = self.get_var('Toe Kick Height')
        Toe_Kick_Setback = self.get_var('Toe Kick Setback')
        Toe_Kick_Thickness = self.get_var('Toe Kick Thickness')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Right_Side_Thickness = self.get_var('Right Side Thickness')
        Bottom_Thickness = self.get_var('Bottom Thickness')
        Cabinet_Depth_Left = self.get_var("Cabinet Depth Left")
        Cabinet_Depth_Right = self.get_var("Cabinet Depth Right")
        
        if self.carcass_shape == 'Diagonal':
            bottom = self.add_assembly(CHAMFERED_PART)
        if self.carcass_shape == 'Notched':
            bottom = self.add_assembly(CORNER_NOTCH_PART)
            
        bottom.set_name(self.carcass_type + " Bottom")
        bottom.x_dim('Width-Right_Side_Thickness',[Width,Right_Side_Thickness])
        bottom.y_dim('Depth+Left_Side_Thickness',[Depth,Left_Side_Thickness])
        bottom.x_loc(value = 0)
        bottom.y_loc(value = 0)
        bottom.x_rot(value = 0)
        bottom.y_rot(value = 0)
        bottom.z_rot(value = 0)
        bottom.prompt('Left Depth','Cabinet_Depth_Left',[Cabinet_Depth_Left])
        bottom.prompt('Right Depth','Cabinet_Depth_Right',[Cabinet_Depth_Right])
        bottom.cutpart(self.carcass_type + "_Bottom")
        bottom.edgebanding('Cabinet_Body_Edges', l1 = True)
        
        if self.carcass_type in {'Upper','Suspended'}:
            bottom.z_dim('Bottom_Thickness',[Bottom_Thickness])
            bottom.z_loc('Height',[Height])
            
        if self.carcass_type in {'Base','Tall','Sink'}:
            bottom.z_dim('Bottom_Thickness',[Bottom_Thickness])
            bottom.z_loc('Toe_Kick_Height',[Toe_Kick_Height])
            
            left_kick = self.add_assembly(PART_WITH_NO_EDGEBANDING)
            left_kick.set_name("Left Toe Kick")
            left_kick.y_dim('Toe_Kick_Height',[Toe_Kick_Height])
            left_kick.z_dim('-Toe_Kick_Thickness',[Toe_Kick_Thickness])
            left_kick.x_loc('Cabinet_Depth_Left-Toe_Kick_Setback',[Cabinet_Depth_Left,Toe_Kick_Setback])
            left_kick.y_loc('Depth+Left_Side_Thickness',[Depth,Left_Side_Thickness])
            left_kick.z_loc(value = 0)
            left_kick.x_rot(value = 90)
            left_kick.y_rot(value = 0)
            left_kick.z_rot(value = 90)
            left_kick.cutpart("Toe_Kick")
    
            if self.carcass_shape == 'Notched':
                left_kick.x_dim('fabs(Depth)-Cabinet_Depth_Right+Toe_Kick_Setback',[Depth,Cabinet_Depth_Right,Toe_Kick_Setback])
                
                right_kick = self.add_assembly(PART_WITH_NO_EDGEBANDING)
                right_kick.set_name("Left Toe Kick")
                right_kick.x_dim('fabs(Width)-Cabinet_Depth_Left+Toe_Kick_Setback-Right_Side_Thickness',[Width,Cabinet_Depth_Left,Toe_Kick_Setback,Right_Side_Thickness])
                right_kick.y_dim('Toe_Kick_Height',[Toe_Kick_Height])
                right_kick.z_dim('-Toe_Kick_Thickness',[Toe_Kick_Thickness])
                right_kick.x_loc('Cabinet_Depth_Left-Toe_Kick_Setback',[Cabinet_Depth_Left,Toe_Kick_Setback,Toe_Kick_Thickness])
                right_kick.y_loc('-Cabinet_Depth_Right+Toe_Kick_Setback',[Cabinet_Depth_Right,Toe_Kick_Setback])
                right_kick.z_loc(value = 0)
                right_kick.x_rot(value = 90)
                right_kick.y_rot(value = 0)
                right_kick.z_rot(value = 0)
                right_kick.cutpart("Toe_Kick")
            
            else:
                left_kick.x_dim('sqrt(((fabs(Depth)-Left_Side_Thickness-Cabinet_Depth_Right+Toe_Kick_Setback)**2)+((fabs(Width)-Right_Side_Thickness-Cabinet_Depth_Left+Toe_Kick_Setback)**2))',
                                [Depth,Width,Cabinet_Depth_Right,Cabinet_Depth_Left,Left_Side_Thickness,Right_Side_Thickness,Toe_Kick_Setback])
                
                left_kick.z_rot('atan((fabs(Depth)-Left_Side_Thickness-Cabinet_Depth_Right+Toe_Kick_Setback)/(fabs(Width)-Right_Side_Thickness-Cabinet_Depth_Left+Toe_Kick_Setback))',
                                [Depth,Width,Left_Side_Thickness,Right_Side_Thickness,Cabinet_Depth_Left,Cabinet_Depth_Right,Toe_Kick_Setback])
    
    def add_backs(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Right_Side_Thickness = self.get_var('Right Side Thickness')
        Top_Inset = self.get_var('Top Inset')
        Bottom_Inset = self.get_var('Bottom Inset')
        Back_Thickness = self.get_var('Back Thickness')

        r_back = self.add_assembly(PART_WITH_NO_EDGEBANDING)
        r_back.set_name(self.carcass_type + " Back")
        r_back.x_loc('Back_Thickness',[Back_Thickness])
        r_back.y_loc(value = 0)
        r_back.z_loc('IF(Height>0,Bottom_Inset,Height+Bottom_Inset)',[Bottom_Inset,Height])
        r_back.x_rot(value = 0)
        r_back.y_rot(value = -90)
        r_back.z_rot(value = -90)
        r_back.x_dim('fabs(Height)-(Top_Inset+Bottom_Inset)',[Height,Top_Inset,Bottom_Inset])
        r_back.y_dim('Width-(Back_Thickness+Right_Side_Thickness)',[Width,Back_Thickness,Right_Side_Thickness])
        r_back.z_dim('-Back_Thickness',[Back_Thickness])
        r_back.cutpart(self.carcass_type + "_Thick_Back" + self.open_name)
        
        l_back = self.add_assembly(PART_WITH_NO_EDGEBANDING)
        l_back.set_name(self.carcass_type + " Back")
        l_back.x_loc(value=0)
        l_back.y_loc(value = 0)
        l_back.z_loc('IF(Height>0,Bottom_Inset,Height+Bottom_Inset)',[Bottom_Inset,Height])
        l_back.x_rot(value = 0)
        l_back.y_rot(value = -90)
        l_back.z_rot(value = 180)
        l_back.x_dim('fabs(Height)-(Top_Inset+Bottom_Inset)',[Height,Top_Inset,Bottom_Inset])
        l_back.y_dim('fabs(Depth)-Right_Side_Thickness',[Depth,Right_Side_Thickness])
        l_back.z_dim('Back_Thickness',[Back_Thickness])
        l_back.cutpart(self.carcass_type + "_Thick_Back" + self.open_name)
        
    def add_valances(self):
        pass
    
    def draw(self):
        self.create_assembly()
        
        self.add_common_carcass_prompts()
        
        if self.carcass_type in {"Base","Tall"}:
            self.add_base_assembly_prompts()
        
        self.add_prompt_formuls()
        self.add_sides()
        self.add_full_top()
        self.add_bottom()
        self.add_backs()
        self.add_fillers()

        self.update()
        
class Outside_Corner_Carcass(fd.Library_Assembly):
    
    library_name = "Carcasses"
    placement_type = ""
    type_assembly = "INSERT"
    
    carcass_type = "" # Base, Tall, Upper, Sink, Suspended
    open_finish = False
    carcass_shape = '' # Diagonal, Radius
    open_name = ""

    def add_prompts(self):
        g = bpy.context.scene.lm_carcass
        self.add_tab(name='Carcass Options',tab_type='VISIBLE')
        self.add_tab(name='Formulas',tab_type='HIDDEN')
        
        if self.carcass_type == "Base":
            self.add_prompt(name="Toe Kick Height",prompt_type='DISTANCE',value= g.Toe_Kick_Height,tab_index=0)
            self.add_prompt(name="Toe Kick Setback",prompt_type='DISTANCE',value= g.Toe_Kick_Setback,tab_index=0)
            
        if self.carcass_type == "Tall":
            self.add_prompt(name="Toe Kick Height",prompt_type='DISTANCE',value= g.Toe_Kick_Height,tab_index=0)
            self.add_prompt(name="Toe Kick Setback",prompt_type='DISTANCE',value= g.Toe_Kick_Setback,tab_index=0)
            self.add_prompt(name="Valance Each Unit",prompt_type='CHECKBOX',value= g.Valance_Each_Unit,tab_index=0)
            self.add_prompt(name="Valance Height Top",prompt_type='DISTANCE',value= g.Valance_Height_Top,tab_index=0)
            self.add_prompt(name="Door Valance Top",prompt_type='CHECKBOX',value= g.Door_Valance_Top,tab_index=0)
            self.add_prompt(name="Valance Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=2)
            
        if self.carcass_type == "Upper":
            self.add_prompt(name="Valance Each Unit",prompt_type='CHECKBOX',value= g.Valance_Each_Unit,tab_index=0)
            self.add_prompt(name="Valance Height Top",prompt_type='DISTANCE',value= g.Valance_Height_Top,tab_index=0)
            self.add_prompt(name="Valance Height Bottom",prompt_type='DISTANCE',value= g.Valance_Height_Bottom,tab_index=0)
            self.add_prompt(name="Door Valance Top",prompt_type='CHECKBOX',value= g.Door_Valance_Top,tab_index=0)
            self.add_prompt(name="Door Valance Bottom",prompt_type='CHECKBOX',value= g.Door_Valance_Bottom,tab_index=0)
            self.add_prompt(name="Valance Thickness",prompt_type='DISTANCE',value= fd.inches(.75),tab_index=1)

        self.add_prompt(name="Toe Kick Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Thick Back Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Top Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Bottom Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Fixed Shelf Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Top Inset",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Bottom Inset",prompt_type='DISTANCE',value=0,tab_index=1)

        tt = self.get_var('Top Thickness','tt')
        bt = self.get_var('Bottom Thickness','bt')
        depth = self.get_var('dim_y','depth')
        
        self.x_dim('fabs(depth)',[depth])
        
        if self.carcass_type == 'Base':
            kick_height = self.get_var('Toe Kick Height','kick_height')
            
            self.prompt("Top Inset",'tt',[tt])
            self.prompt("Bottom Inset",'bt+kick_height',[bt,kick_height])
            
        if self.carcass_type == 'Tall':
            kick_height = self.get_var('Toe Kick Height','kick_height')
            vht = self.get_var('Valance Height Top','vht')
            
            self.prompt("Top Inset",'tt+vht',[tt,vht])
            self.prompt("Bottom Inset",'bt+kick_height',[bt,kick_height])
            
        if self.carcass_type == 'Upper':
            vht = self.get_var('Valance Height Top','vht')
            vhb = self.get_var('Valance Height Bottom','vhb')
            
            self.prompt("Top Inset",'tt+vht',[tt,vht])
            self.prompt("Bottom Inset",'bt+vhb',[bt,vhb])
    
    def add_left_back(self):
        kick_height = self.get_var('Toe Kick Height','kick_height')
        height = self.get_var('dim_z','height')
        depth = self.get_var('dim_y','depth')
        
        left_back = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        left_back.set_name("Left Back")
        left_back.x_loc(value=fd.inches(0))
        left_back.y_loc(value=fd.inches(0))
        left_back.z_loc('kick_height',[kick_height])
        left_back.y_rot(value=-90)
        left_back.x_dim('height-kick_height',[height,kick_height])
        left_back.y_dim('depth',[depth])
        left_back.z_dim(value=fd.inches(-.75))
        left_back.cutpart(self.carcass_type + '_Thick_Back' + self.open_name)
        left_back.edgebanding('Cabinet_Body_Edges',l1=True)
    
    def add_right_back(self):
        height = self.get_var('dim_z','height')
        width = self.get_var('dim_x','width')
        kick_height = self.get_var('Toe Kick Height','kick_height')
        tbt = self.get_var('Thick Back Thickness','tbt')
        
        right_back = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        right_back.set_name("Right Back")
        right_back.x_loc('tbt',[tbt])
        right_back.y_loc(value=fd.inches(0))
        right_back.z_loc('kick_height',[kick_height])
        right_back.y_rot(value=-90)
        right_back.z_rot(value=90)
        right_back.x_dim('height-kick_height',[height,kick_height])
        right_back.y_dim('(width-tbt)*-1',[width,tbt])
        right_back.x_dim(value=fd.inches(.75))
        right_back.cutpart(self.carcass_type + '_Thick_Back' + self.open_name)
        right_back.edgebanding('Cabinet_Body_Edges',l1=True)
        
    def add_top(self):
        height = self.get_var('dim_z','height')
        width = self.get_var('dim_x','width')
        depth = self.get_var('dim_y','depth')
        tbt = self.get_var('Thick Back Thickness','tbt')
        tt = self.get_var('Top Thickness','tt')
        vht = self.get_var('Valance Height Top','vht')

        top = self.add_assembly(RADIUS_CORNER_PART_WITH_EDGEBANDING if self.carcass_shape == 'Radius' else CHAMFERED_PART)
        top.set_name("Top")
        top.x_loc('tbt',[tbt])
        top.y_loc('-tbt',[tbt])
        if self.carcass_type == 'Base':
            top.z_loc('height',[height])
        if self.carcass_type == 'Tall':
            top.z_loc('height-vht',[height,vht])
        if self.carcass_type == 'Upper':
            top.z_loc('-vht',[vht])
        top.y_rot(value=-180)
        top.z_rot(value=90)
        top.x_dim('fabs(depth)-tbt',[depth,tbt])
        top.y_dim('(width-tbt)*-1',[width,tbt])
        top.z_dim('tt',[tt])
        top.prompt('Radius','width-tbt',[width,tbt])
        if self.carcass_shape == 'Diagonal':
            top.prompt('Left Depth',value = 0)
            top.prompt('Right Depth',value = 0)
        top.cutpart(self.carcass_type + '_Top' + self.open_name)
        top.edgebanding('Cabinet_Body_Edges',l1=True)
        
    def add_bottom(self):
        height = self.get_var('dim_z','height')
        width = self.get_var('dim_x','width')
        depth = self.get_var('dim_y','depth')
        kick_height = self.get_var('Toe Kick Height','kick_height')
        tbt = self.get_var('Thick Back Thickness','tbt')
        vhb = self.get_var('Valance Height Bottom','vhb')
        bt = self.get_var('Bottom Thickness','bt')

        bottom = self.add_assembly(RADIUS_CORNER_PART_WITH_EDGEBANDING if self.carcass_shape == 'Radius' else CHAMFERED_PART)
        bottom.x_loc('tbt',[tbt])
        bottom.y_loc('-tbt',[tbt])
        if self.carcass_type == 'Upper':
            bottom.z_loc('height+vhb',[height,vhb])
        else:
            bottom.z_loc('kick_height',[kick_height])
        bottom.y_rot(value=-180)
        bottom.z_rot(value=90)
        bottom.x_dim('fabs(depth)-tbt',[depth,tbt])
        bottom.y_dim('(width-tbt)*-1',[width,tbt])
        bottom.z_dim('(bt)*-1',[bt])
        bottom.prompt('Radius','width-tbt',[width,tbt])
        if self.carcass_shape == 'Diagonal':
            bottom.prompt('Left Depth',value = 0)
            bottom.prompt('Right Depth',value = 0)
        bottom.cutpart(self.carcass_type + '_Bottom' + self.open_name)
        bottom.edgebanding('Cabinet_Body_Edges',l1=True)
        
    def add_toe_kick(self):
        width = self.get_var('dim_x','width')
        depth = self.get_var('dim_y','depth')
        kick_height = self.get_var('Toe Kick Height','kick_height')
        kick_setback = self.get_var('Toe Kick Setback','kick_setback')
        tkt = self.get_var('Toe Kick Thickness','tkt')

        toe_kick = self.add_assembly(BENDING_PART if self.carcass_shape == 'Radius' else PART_WITH_NO_EDGEBANDING)
        toe_kick.x_loc('width-kick_setback',[width,kick_setback])
        toe_kick.y_loc(value=fd.inches(0))
        toe_kick.x_loc(value=fd.inches(0))
        toe_kick.x_rot(value=90)
        if self.carcass_shape == 'Diagonal':
            toe_kick.x_dim('sqrt(((fabs(depth)-kick_setback)**2)+((fabs(width)-kick_setback)**2))*-1',[width,depth,kick_setback])
            toe_kick.z_rot('atan((fabs(depth)+kick_setback)/(fabs(width)+kick_setback))',[width,depth,kick_setback])

        if self.carcass_shape == 'Radius':
            toe_kick.z_rot(value=-90)
            toe_kick.x_dim('radians(90)*(width-kick_setback)',[width,kick_setback])
            toe_kick.prompt('Bending',value=90)

        toe_kick.y_dim('kick_height',[kick_height])
        toe_kick.z_dim('tkt',[tkt])
        toe_kick.cutpart('Toe_Kick')
    
    def add_top_valance(self):
        width = self.get_var('dim_x','width')
        depth = self.get_var('dim_y','depth')
        height = self.get_var('dim_z','height')
        vht = self.get_var('Valance Height Top','vht')
        tbt = self.get_var('Thick Back Thickness','tbt')
        vt = self.get_var('Valance Thickness','vt')

        top_valance = self.add_assembly(BENDING_PART if self.carcass_shape == 'Radius' else PART_WITH_NO_EDGEBANDING)
        top_valance.set_name("Top Valance")
        top_valance.x_loc('width',[width])
        top_valance.y_loc('-tbt',[tbt])
        if self.carcass_type == 'Tall':
            top_valance.z_loc('height-vht',[height,vht])
        if self.carcass_type == 'Upper':
            top_valance.z_loc('-vht',[vht])
        top_valance.x_rot(value=90)
        if self.carcass_shape == 'Diagonal':
            top_valance.x_dim('sqrt(((fabs(depth)-tbt)**2)+((fabs(width)-tbt)**2))*-1',[width,depth,tbt])
            top_valance.z_rot('atan((fabs(depth)-tbt)/(fabs(width)-tbt))',[width,depth,tbt])
            
        if self.carcass_shape == 'Radius':
            top_valance.z_rot(value=-90)
            top_valance.x_dim('radians(90)*(width-tbt)',[width,tbt])
            top_valance.prompt('Bending',value=90)
            
        top_valance.y_dim('vht',[vht])
        top_valance.z_dim('-vt',[vt])
        top_valance.cutpart('Valance')
        top_valance.prompt('Hide','IF(vht<=0,True,False)',[vht])
        
    def add_bottom_valance(self):
        width = self.get_var('dim_x','width')
        height = self.get_var('dim_z','height')
        depth = self.get_var('dim_y','depth')
        vhb = self.get_var('Valance Height Bottom','vhb')
        tbt = self.get_var('Thick Back Thickness','tbt')
        vt = self.get_var('Valance Thickness','vt')

        bottom_valance = self.add_assembly(BENDING_PART if self.carcass_shape == 'Radius' else PART_WITH_NO_EDGEBANDING)
        bottom_valance.set_name("Bottom Valance")
        bottom_valance.x_loc('width',[width])
        bottom_valance.y_loc('-tbt',[tbt])
        bottom_valance.z_loc('height',[height,vhb])
        bottom_valance.x_rot(value=90)
        if self.carcass_shape == 'Diagonal':
            bottom_valance.x_dim('sqrt(((fabs(depth)-tbt)**2)+((fabs(width)-tbt)**2))*-1',[width,depth,tbt])
            bottom_valance.z_rot('atan((fabs(depth)-tbt)/(fabs(width)-tbt))',[width,depth,tbt])
            
        if self.carcass_shape == 'Radius':
            bottom_valance.z_rot(value=-90)
            bottom_valance.x_dim('radians(90)*(width-tbt)',[width,tbt])
            bottom_valance.prompt('Bending',value=90)
            
        bottom_valance.y_dim('vhb',[vhb])
        bottom_valance.z_dim('-vt',[vt])
        bottom_valance.cutpart('Valance')
        bottom_valance.prompt('Hide','IF(vhb<=0,True,False)',[vhb])
    
    def draw(self):
        self.create_assembly()
        self.open_name = ' Open' if self.open_finish else ''
            
        self.add_prompts()
        self.add_left_back()
        self.add_right_back()
        self.add_bottom()
        self.add_top()

        if self.carcass_type in {"Base","Tall"}:
            self.add_toe_kick()
            
        if self.carcass_type == 'Tall':
            self.add_top_valance()
        
        if self.carcass_type == 'Upper':
            self.add_top_valance()
            self.add_bottom_valance()
            
        self.update()
        
#---------Standard Carcasses
        
class INSERT_Base_Carcass(Standard_Carcass):
    
    def __init__(self):
        self.category_name = "Carcasses"
        self.assembly_name = "Base Carcass"
        self.carcass_type = "Base"
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
class INSERT_Tall_Carcass(Standard_Carcass):
    
    def __init__(self):
        self.category_name = "Carcasses"
        self.assembly_name = "Tall Carcass"
        self.carcass_type = "Tall"
        self.width = fd.inches(18)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
        
class INSERT_Upper_Carcass(Standard_Carcass):
    
    def __init__(self):
        self.category_name = "Carcasses"
        self.assembly_name = "Upper Carcass"
        self.carcass_type = "Upper"
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(12)
        
class INSERT_Sink_Carcass(Standard_Carcass):
    
    def __init__(self):
        self.category_name = "Carcasses"
        self.assembly_name = "Sink Carcass"
        self.carcass_type = "Sink"
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
class INSERT_Suspended_Carcass(Standard_Carcass):
    
    def __init__(self):
        self.category_name = "Carcasses"
        self.assembly_name = "Suspended Carcass"
        self.carcass_type = "Suspended"
        self.width = fd.inches(18)
        self.height = fd.inches(6)
        self.depth = fd.inches(23)

#---------Transition Carcasses

class INSERT_Base_Transition_Carcass(Transition_Carcass):
    
    def __init__(self):
        self.category_name = "Carcasses"
        self.assembly_name = "Base Carcass"
        self.carcass_type = "Base"
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
class INSERT_Tall_Transition_Carcass(Transition_Carcass):
    
    def __init__(self):
        self.category_name = "Carcasses"
        self.assembly_name = "Tall Carcass"
        self.carcass_type = "Tall"
        self.width = fd.inches(18)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
        
class INSERT_Upper_Transition_Carcass(Transition_Carcass):
    
    def __init__(self):
        self.category_name = "Carcasses"
        self.assembly_name = "Upper Carcass"
        self.carcass_type = "Upper"
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(12)
        
class INSERT_Sink_Transition_Carcass(Transition_Carcass):
    
    def __init__(self):
        self.category_name = "Carcasses"
        self.assembly_name = "Sink Carcass"
        self.carcass_type = "Sink"
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
class INSERT_Suspended_Transition_Carcass(Transition_Carcass):
    
    def __init__(self):
        self.category_name = "Carcasses"
        self.assembly_name = "Suspended Carcass"
        self.carcass_type = "Suspended"
        self.width = fd.inches(18)
        self.height = fd.inches(6)
        self.depth = fd.inches(23)

#---------Inside Corner Carcasses

class INSERT_Base_Inside_Corner_Notched_Carcass(Inside_Corner_Carcass):
    
    def __init__(self):
        self.category_name = "Carcasses"
        self.assembly_name = "Base Inside Corner Notched Carcass"
        self.carcass_type = "Base"
        self.carcass_shape = "Notched"
        self.width = fd.inches(36)
        self.height = fd.inches(34)
        self.depth = fd.inches(36)
        self.left_right_depth = fd.inches(23)
        
class INSERT_Upper_Inside_Corner_Notched_Carcass(Inside_Corner_Carcass):
    
    def __init__(self):
        self.category_name = "Carcasses"
        self.assembly_name = "Upper Inside Corner Notched Carcass"
        self.carcass_type = "Upper"
        self.carcass_shape = "Notched"
        self.width = fd.inches(12)
        self.height = fd.inches(34)
        self.depth = fd.inches(12)
        self.left_right_depth = fd.inches(12)

class INSERT_Base_Inside_Corner_Diagonal_Carcass(Inside_Corner_Carcass):
    
    def __init__(self):
        self.category_name = "Carcasses"
        self.assembly_name = "Base Inside Corner Diagonal Carcass"
        self.carcass_type = "Base"
        self.carcass_shape = "Diagonal"
        self.width = fd.inches(36)
        self.height = fd.inches(34)
        self.depth = fd.inches(36)
        self.left_right_depth = fd.inches(23)
        
class INSERT_Upper_Inside_Corner_Diagonal_Carcass(Inside_Corner_Carcass):
    
    def __init__(self):
        self.category_name = "Carcasses"
        self.assembly_name = "Upper Inside Corner Diagonal Carcass"
        self.carcass_type = "Upper"
        self.carcass_shape = "Diagonal"
        self.width = fd.inches(12)
        self.height = fd.inches(34)
        self.depth = fd.inches(12)
        self.left_right_depth = fd.inches(12)

#---------Outside Corner Carcasses

class INSERT_Base_Outside_Chamfered_Corner_Carcass(Outside_Corner_Carcass):
    
    def __init__(self):
        self.category_name = "Carcasses"
        self.assembly_name = "Base Outside Chamfered Corner Carcass"
        self.carcass_type = "Base"
        self.carcass_shape = "Diagonal"
        self.width = fd.inches(23)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
class INSERT_Base_Outside_Radius_Corner_Carcass(Outside_Corner_Carcass):
    
    def __init__(self):
        self.category_name = "Carcasses"
        self.assembly_name = "Base Outside Radius Corner Carcass"
        self.carcass_type = "Base"
        self.carcass_shape = "Radius"
        self.width = fd.inches(23)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)

class INSERT_Tall_Outside_Chamfered_Corner_Carcass(Outside_Corner_Carcass):
    
    def __init__(self):
        self.category_name = "Carcasses"
        self.assembly_name = "Tall Outside Chamfered Corner Carcass"
        self.carcass_type = "Tall"
        self.carcass_shape = "Diagonal"
        self.width = fd.inches(23)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
        
class INSERT_Tall_Outside_Radius_Corner_Carcass(Outside_Corner_Carcass):
    
    def __init__(self):
        self.category_name = "Carcasses"
        self.assembly_name = "Tall Outside Radius Corner Carcass"
        self.carcass_type = "Tall"
        self.carcass_shape = "Radius"
        self.width = fd.inches(23)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)

class INSERT_Upper_Outside_Chamfered_Corner_Carcass(Outside_Corner_Carcass):
    
    def __init__(self):
        self.category_name = "Carcasses"
        self.assembly_name = "Upper Outside Chamfered Corner Carcass"
        self.carcass_type = "Upper"
        self.carcass_shape = "Diagonal"
        self.width = fd.inches(12)
        self.height = fd.inches(34)
        self.depth = fd.inches(12)
        
class INSERT_Upper_Outside_Radius_Corner_Carcass(Outside_Corner_Carcass):
    
    def __init__(self):
        self.category_name = "Carcasses"
        self.assembly_name = "Upper Outside Radius Corner Carcass"
        self.carcass_type = "Upper"
        self.carcass_shape = "Radius"
        self.width = fd.inches(12)
        self.height = fd.inches(34)
        self.depth = fd.inches(12)

class PROPERTIES_Scene_Variables(bpy.types.PropertyGroup):
    
    Use_Full_Tops = bpy.props.BoolProperty(name="Use Full Tops", 
                                           description="Check this to use full tops and not stretchers on base cabinets", 
                                           default=False)
    
    Use_Notched_Sides = bpy.props.BoolProperty(name="Use Notched Sides", 
                                               description="Check this to use notched sides for base and tall cabinets", 
                                               default=True)
    
    Use_Thick_Back = bpy.props.BoolProperty(name="Use Thick Back", 
                                            description="Check this to use thick backs", 
                                            default=False)
    
    Use_Nailers = bpy.props.BoolProperty(name="Use Nailers", 
                                         description="Check this to use nailers", 
                                         default=True)
    
    Use_Leg_Levelers = bpy.props.BoolProperty(name="Use Leg Levelers", 
                                              description="Turn this on to use leg levelers for the base assembly. Otherwise cabinet sides will extend the full height of the cabinet", 
                                              default=False)
    
    Remove_Back = bpy.props.BoolProperty(name="Remove Back", 
                                         description="This removes the cabinet back. ", 
                                         default=False)
    
    Extend_Sides_To_Floor = bpy.props.BoolProperty(name="Extend Sides To Floor", 
                                                   description="Extend sides to the floor for base and tall cabinets. ", 
                                                   default=True)
    
    Door_Valance_Top = bpy.props.BoolProperty(name="Door Valance Top", 
                                              description="Extend top of door to top of valance. ", 
                                              default=True)
    
    Door_Valance_Bottom = bpy.props.BoolProperty(name="Door Valance Bottom", 
                                                 description="Extend bottom of door to bottom of valance. ", 
                                                 default=True)
    
    Valance_Each_Unit = bpy.props.BoolProperty(name="Valacne Each Unit", 
                                               description="Add a separte valance part for each cabinet. ", 
                                               default=True)
    
    Toe_Kick_Height = bpy.props.FloatProperty(name="Toe Kick Height",
                                              description="Default toe kick height for cabinets",
                                              default=fd.inches(4.0),
                                              unit='LENGTH')
    
    Toe_Kick_Setback = bpy.props.FloatProperty(name="Toe Kick Setback",
                                               description="Default toe kick height setback for cabinets",
                                               default=fd.inches(3.25),
                                               unit='LENGTH')
    
    Center_Nailer_Switch = bpy.props.FloatProperty(name="Center Nailer Switch",
                                                   description="Smallest height of a cabinet to include a center nailer",
                                                   default=fd.inches(60),
                                                   unit='LENGTH')
    
    Nailer_Width = bpy.props.FloatProperty(name="Nailer Width",
                                           description="Default width for nailers",
                                           default=fd.inches(4),
                                           unit='LENGTH')
    
    Stretcher_Width = bpy.props.FloatProperty(name="Stretcher Width",
                                              description="Default width for stretchers",
                                              default=fd.inches(4),
                                              unit='LENGTH')
    
    Valance_Height_Top = bpy.props.FloatProperty(name="Valance Height Top",
                                                 description="Default Top Valance Height",
                                                 default=fd.inches(0),
                                                 unit='LENGTH')
    
    Valance_Height_Bottom = bpy.props.FloatProperty(name="Valance Height Bottom",
                                                    description="Default Bottom Valance Height",
                                                    default=fd.inches(0),
                                                    unit='LENGTH')
    
    Sub_Front_Height = bpy.props.FloatProperty(name="Sub Front Height",
                                               description="Default Sink Sub Front Height",
                                               default=fd.inches(7),
                                               unit='LENGTH')

    def draw(self,layout):
        col = layout.column(align=True)

        box = col.box()
        row = box.row(align=True)
        row.label("Cabinet Back Options:")
        row = box.row(align=True)
        row.prop(self,"Remove_Back")
        row.prop(self,"Use_Nailers")
        row.prop(self,"Use_Thick_Back")
        row = box.row(align=True)
        row.label("Nailer Width:")
        row.prop(self,"Nailer_Width",text="")
        row = box.row(align=True)
        row.label("Center Nailer Switch:")
        row.prop(self,"Center_Nailer_Switch",text="")
            
        box = col.box()
        row = box.row(align=True)
        row.label("Cabinet Top Options:")
        row = box.row(align=True)
        row.prop(self,"Use_Full_Tops")
        if not self.Use_Full_Tops:
            row = box.row(align=True)
            row.label("Stretcher Width:")
            row.prop(self,"Stretcher_Width",text="")
        row = box.row(align=True)
        row.label("Sub Front Height:")
        row.prop(self,"Sub_Front_Height",text="")
        
        box = col.box()
        row = box.row(align=True)
        row.label("Cabinet Side Options:")
        row = box.row(align=True)
        row.prop(self,"Use_Notched_Sides")
        row.prop(self,"Extend_Sides_To_Floor")
        
        box = col.box()
        row = box.row(align=True)
        row.label("Cabinet Valance Options:")
        row = box.row(align=True)
        row.label("Valance Height Top:")
        row.prop(self,"Valance_Height_Top")
        row = box.row(align=True)
        row.label("Valance Height Bottom:")
        row.prop(self,"Valance_Height_Bottom")
        row = box.row(align=True)
        row.prop(self,"Door_Valance_Top")
        row.prop(self,"Door_Valance_Bottom")
        row = box.row(align=True)
        row.prop(self,"Valance_Each_Unit")
        
        box = col.box()
        row = box.row(align=True)
        row.label("Cabinet Base Assembly:")
        row = box.row(align=True)
        row.label("Toe Kick Height:")
        row.prop(self,"Toe_Kick_Height")
        row = box.row(align=True)
        row.label("Toe Kick Setback:")
        row.prop(self,"Toe_Kick_Setback")
        row = box.row(align=True)
        row.prop(self,"Use_Leg_Levelers")

def register():
    bpy.utils.register_class(PROPERTIES_Scene_Variables)
    bpy.types.Scene.lm_carcass = bpy.props.PointerProperty(type = PROPERTIES_Scene_Variables)
    
def unregister():
    bpy.utils.unregister_class(PROPERTIES_Scene_Variables)
    
    