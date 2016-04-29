"""
Microvellum 
Exteriors
Stores the logic and insert defs for all exterior components for cabinets and closets.
Doors, Drawers, Hampers
"""

import bpy
import fd
import math
import os
from bpy.app.handlers import persistent
import LM_pulls
import LM_drawer_boxes

HIDDEN_FOLDER_NAME = "_HIDDEN"
DOOR_LIBRARY_NAME = "Cabinet Assemblies"
DOOR_CATEGORY_NAME = "Door Panels"
PART_WITH_NO_EDGEBANDING = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Cut Parts","Part with No Edgebanding")
PART_WITH_FRONT_EDGEBANDING = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Cut Parts","Part with Front Edgebanding")
MID_RAIL = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Cut Parts","Part with Edgebanding")
DIVISION = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Cut Parts","Part with Edgebanding")
DRAWER_BOX = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Drawer Boxes","Wood Drawer Box")
FLUTED_PART = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Cut Parts","Fluted Part")
WIRE_BASKET = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Hardware","Wire Basket")

ROSETTE = (HIDDEN_FOLDER_NAME,"Rosetts","Rosette")

DOOR_BOX_MATERIAL = ("Plastics","White Melamine")
DOOR_MATERIAL = ("Plastics","White Melamine")
GLASS_MATERIAL = ("Glass","Glass","Glass")

preview_collections = {}

def enum_preview_from_dir(self,context):
    enum_items = []
    
    if context is None:
        return enum_items
    
    icon_dir = os.path.join(fd.get_library_dir("assemblies"),HIDDEN_FOLDER_NAME,DOOR_LIBRARY_NAME,DOOR_CATEGORY_NAME)
    
    pcoll = preview_collections["main"]
    
    if len(pcoll.my_previews) > 0:
        return pcoll.my_previews
    
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
#             enum_items.append((name, name, "", thumb.icon_id, i))
    
    pcoll.my_previews = enum_items
    pcoll.my_previews_dir = icon_dir
    return pcoll.my_previews

#---------SPEC GROUP POINTERS

class Material_Pointers():
    
    Door_Surface = fd.Material_Pointer(DOOR_MATERIAL)
    
    Door_Edge = fd.Material_Pointer(DOOR_MATERIAL)

    Glass = fd.Material_Pointer(GLASS_MATERIAL)
    
class Cutpart_Pointers():
    
    Slab_Door = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                core="Concealed_Surface",
                                top="Door_Surface",
                                bottom="Door_Surface")
    
    Slab_Drawer_Front = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                        core="Concealed_Surface",
                                        top="Door_Surface",
                                        bottom="Door_Surface")
    
class Edgepart_Pointers():
    
    Door_Edges = fd.Edgepart_Pointer(thickness=fd.inches(.01),
                                  material="Door_Edge")

#---------FUNCTIONS
    
def add_common_door_prompts(assembly):
    g = bpy.context.scene.lm_exteriors
    
    door_location = 0
    
    if assembly.door_type == 'Base':
        door_location = 0
    elif assembly.door_type == 'Tall':
        door_location = 1
    else:
        door_location = 2
    
    assembly.add_prompt(name="Door Rotation",prompt_type='ANGLE',value=0,tab_index=0)
    
    if assembly.door_swing in {"Left Swing","Right Swing"}:
        assembly.add_prompt(name="Left Swing",prompt_type='CHECKBOX',value=True if assembly.door_swing == 'Left Swing' else False,tab_index=0)
        assembly.add_prompt(name="Right Swing",prompt_type='CHECKBOX',value=False,tab_index=1) # CALCULATED
        
        #CALCULATE RIGHT SWING PROMPT NEEDED FOR MV EXPORT
        Left_Swing = assembly.get_var("Left Swing")
        assembly.prompt('Right Swing','IF(Left_Swing,True,False)',[Left_Swing])
        
    assembly.add_prompt(name="Inset Front",prompt_type='CHECKBOX',value=g.Inset_Door,tab_index=0)
    assembly.add_prompt(name="Inset Reveal",prompt_type='DISTANCE',value=g.Inset_Reveal,tab_index=0)
    assembly.add_prompt(name="Door to Cabinet Gap",prompt_type='DISTANCE',value=g.Door_To_Cabinet_Gap,tab_index=0)
    assembly.add_prompt(name="No Pulls",prompt_type='CHECKBOX',value=g.No_Pulls,tab_index=0)
    assembly.add_prompt(name="Pull Rotation",prompt_type='ANGLE',value=g.Pull_Rotation,tab_index=0)
    assembly.add_prompt(name="Pull From Edge",prompt_type='DISTANCE',value=g.Pull_From_Edge,tab_index=0)
    assembly.add_prompt(name="Pull Location",prompt_type='COMBOBOX',value=door_location,tab_index=0,items=['Base','Tall','Upper'],columns=3)
    assembly.add_prompt(name="Base Pull Location",prompt_type='DISTANCE',value=g.Base_Pull_Location,tab_index=0)
    assembly.add_prompt(name="Tall Pull Location",prompt_type='DISTANCE',value=g.Tall_Pull_Location,tab_index=0)
    assembly.add_prompt(name="Upper Pull Location",prompt_type='DISTANCE',value=g.Upper_Pull_Location,tab_index=0)
    assembly.add_prompt(name="Lock Door",prompt_type='CHECKBOX',value=False,tab_index=0)
    assembly.add_prompt(name="Pull Length",prompt_type='DISTANCE',value=0,tab_index=1)
    assembly.add_prompt(name="Door Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
    assembly.add_prompt(name="Edgebanding Thickness",prompt_type='DISTANCE',value=fd.inches(.02),tab_index=1)
    
    sgi = assembly.get_var('cabinetlib.spec_group_index','sgi')

    assembly.prompt('Door Thickness','THICKNESS(sgi,"Slab_Door")',[sgi])
    assembly.prompt('Edgebanding Thickness','EDGE_THICKNESS(sgi,"Door_Edges")',[sgi])
    
def add_common_drawer_prompts(assembly):
    g = bpy.context.scene.lm_exteriors

    assembly.add_prompt(name="No Pulls",prompt_type='CHECKBOX',value=g.No_Pulls,tab_index=0)
    assembly.add_prompt(name="Center Pulls on Drawers",prompt_type='CHECKBOX',value=g.Center_Pulls_on_Drawers,tab_index=0)
    assembly.add_prompt(name="Drawer Pull From Top",prompt_type='DISTANCE',value=g.Drawer_Pull_From_Top,tab_index=0)
    assembly.add_prompt(name="Pull Double Max Span",prompt_type='DISTANCE',value=fd.inches(30),tab_index=0)
    assembly.add_prompt(name="Lock From Top",prompt_type='DISTANCE',value=fd.inches(1.0),tab_index=0)
    assembly.add_prompt(name="Lock Drawer",prompt_type='CHECKBOX',value=False,tab_index=0)
    assembly.add_prompt(name="Inset Front",prompt_type='CHECKBOX',value=False,tab_index=0)
    assembly.add_prompt(name="Open",prompt_type='PERCENTAGE',value=0,tab_index=0)

    assembly.add_prompt(name="Inset Reveal",prompt_type='DISTANCE',value=fd.inches(0.125),tab_index=0) 
    assembly.add_prompt(name="Door to Cabinet Gap",prompt_type='DISTANCE',value=fd.inches(0.125),tab_index=0)   
    assembly.add_prompt(name="Drawer Box Top Gap",prompt_type='DISTANCE',value=fd.inches(0.5),tab_index=0)
    assembly.add_prompt(name="Drawer Box Bottom Gap",prompt_type='DISTANCE',value=fd.inches(0.5),tab_index=0)
    assembly.add_prompt(name="Drawer Box Slide Gap",prompt_type='DISTANCE',value=fd.inches(0.5),tab_index=0)
    assembly.add_prompt(name="Drawer Box Rear Gap",prompt_type='DISTANCE',value=fd.inches(0.5),tab_index=0)
    
    assembly.add_prompt(name="Front Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
    assembly.add_prompt(name="Edgebanding Thickness",prompt_type='DISTANCE',value=fd.inches(.02),tab_index=1)

    sgi = assembly.get_var('cabinetlib.spec_group_index','sgi')
 
    assembly.prompt('Front Thickness','THICKNESS(sgi,"Slab_Door")',[sgi])
    assembly.prompt('Edgebanding Thickness','EDGE_THICKNESS(sgi,"Door_Edges")',[sgi])
        
class Doors(fd.Library_Assembly):
    
    library_name = "Cabinet Exteriors"
    type_assembly = 'INSERT'
    placement_type = "EXTERIOR"
    property_id = "exteriors.door_prompts"
    door_type = "" # {Base, Tall, Upper}
    door_swing = "" # {Left Swing, Right Swing, Double Door, Flip up}

    false_front_qty = 0 # 0, 1, 2

    def add_doors_prompts(self):
        g = bpy.context.scene.lm_exteriors
        
        self.add_tab(name='Door Options',tab_type='VISIBLE')
        self.add_tab(name='Formulas',tab_type='HIDDEN')
        
        add_common_door_prompts(self)
        
        if self.false_front_qty > 0:
            self.add_prompt(name="False Front Height",prompt_type='DISTANCE',value=fd.inches(6),tab_index=0)
        
        self.add_prompt(name="Half Overlay Top",prompt_type='CHECKBOX',value=False,tab_index=0)
        self.add_prompt(name="Half Overlay Bottom",prompt_type='CHECKBOX',value=False,tab_index=0)
        self.add_prompt(name="Half Overlay Left",prompt_type='CHECKBOX',value=False,tab_index=0)
        self.add_prompt(name="Half Overlay Right",prompt_type='CHECKBOX',value=False,tab_index=0)
        
        self.add_prompt(name="Vertical Gap",prompt_type='DISTANCE',value=g.Vertical_Gap,tab_index=0)
        self.add_prompt(name="Top Reveal",prompt_type='DISTANCE',value=fd.inches(.25),tab_index=0)
        self.add_prompt(name="Bottom Reveal",prompt_type='DISTANCE',value=0,tab_index=0)
        self.add_prompt(name="Left Reveal",prompt_type='DISTANCE',value=g.Left_Reveal,tab_index=0)
        self.add_prompt(name="Right Reveal",prompt_type='DISTANCE',value=g.Right_Reveal,tab_index=0)

        #CALCULATED
        self.add_prompt(name="Top Overlay",prompt_type='DISTANCE',value=fd.inches(.6875),tab_index=1)
        self.add_prompt(name="Bottom Overlay",prompt_type='DISTANCE',value=fd.inches(.6875),tab_index=1)
        self.add_prompt(name="Left Overlay",prompt_type='DISTANCE',value=fd.inches(.6875),tab_index=1)
        self.add_prompt(name="Right Overlay",prompt_type='DISTANCE',value=fd.inches(.6875),tab_index=1)
        
        #INHERITED
        self.add_prompt(name="Extend Top Amount",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Extend Bottom Amount",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Top Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Bottom Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Left Side Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Right Side Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Division Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        
        inset = self.get_var("Inset Front",'inset')
        ir = self.get_var("Inset Reveal",'ir')
        tr = self.get_var("Top Reveal",'tr')
        br = self.get_var("Bottom Reveal",'br')
        lr = self.get_var("Left Reveal",'lr')
        rr = self.get_var("Right Reveal",'rr')
        vg = self.get_var("Vertical Gap",'vg')
        hot = self.get_var("Half Overlay Top",'hot')
        hob = self.get_var("Half Overlay Bottom",'hob')
        hol = self.get_var("Half Overlay Left",'hol')
        hor = self.get_var("Half Overlay Right",'hor')
        tt = self.get_var("Top Thickness",'tt')
        lst = self.get_var("Left Side Thickness",'lst')
        rst = self.get_var("Right Side Thickness",'rst')
        bt = self.get_var("Bottom Thickness",'bt')
        height = self.get_var("dim_z",'height')
        
        if self.door_swing == 'Double Door':
            self.prompt('Hinge Quantity','MV_CALCULATE_HINGE_QTY(height)*2',[height])
        else:
            self.prompt('Hinge Quantity','MV_CALCULATE_HINGE_QTY(height)',[height])
        self.prompt('Top Overlay','IF(inset,-ir,IF(hot,(tt/2)-(vg/2),tt-tr))',[inset,ir,hot,tt,tr,vg])
        self.prompt('Bottom Overlay','IF(inset,-ir,IF(hob,(bt/2)-(vg/2),bt-br))',[inset,ir,hob,bt,br,vg])
        self.prompt('Left Overlay','IF(inset,-ir,IF(hol,(lst/2)-(vg/2),lst-lr))',[inset,ir,hol,lst,lr,vg])
        self.prompt('Right Overlay','IF(inset,-ir,IF(hor,(rst/2)-(vg/2),rst-rr))',[inset,ir,hor,rst,rr,vg])
        
    def set_standard_drivers(self,assembly):
        Height = self.get_var('dim_z','Height')
        Inset_Front = self.get_var("Inset Front")
        Door_Gap = self.get_var("Door to Cabinet Gap",'Door_Gap')
        tt = self.get_var("Top Thickness",'tt')
        bt = self.get_var("Bottom Thickness",'bt')
        Top_Overlay = self.get_var("Top Overlay")
        Bottom_Overlay = self.get_var("Bottom Overlay")
        eta = self.get_var("Extend Top Amount",'eta')
        eba = self.get_var("Extend Bottom Amount",'eba')
        Door_Thickness = self.get_var("Door Thickness")
        False_Front_Height = self.get_var("False Front Height")
        Vertical_Gap = self.get_var("Vertical Gap")
        
        assembly.y_loc('IF(Inset_Front,Door_Thickness,-Door_Gap)',[Inset_Front,Door_Gap,Door_Thickness])
        assembly.z_loc('IF(OR(eba==0,Inset_Front==True),-Bottom_Overlay,-eba)',
                       [Inset_Front,eba,bt,Bottom_Overlay])
        assembly.x_rot(value = 0)
        assembly.y_rot(value = -90)
        if self.false_front_qty > 0:
            assembly.x_dim('Height+IF(OR(eta==0,Inset_Front==True),Top_Overlay,eta)+IF(OR(eba==0,Inset_Front==True),Bottom_Overlay,eba)-False_Front_Height-Vertical_Gap',
                           [Inset_Front,Height,Top_Overlay,Bottom_Overlay,eta,eba,tt,bt,False_Front_Height,Vertical_Gap])
        else:
            assembly.x_dim('Height+IF(OR(eta==0,Inset_Front==True),Top_Overlay,eta)+IF(OR(eba==0,Inset_Front==True),Bottom_Overlay,eba)',
                           [Inset_Front,Height,Top_Overlay,Bottom_Overlay,eta,eba,tt,bt])
        assembly.z_dim('Door_Thickness',[Door_Thickness])
        
    def set_pull_drivers(self,assembly):
        self.set_standard_drivers(assembly)
        
        Height = self.get_var('dim_z','Height')
        Pull_Length = assembly.get_var("Pull Length")
        Pull_From_Edge = self.get_var("Pull From Edge")
        Base_Pull_Location = self.get_var("Base Pull Location")
        Tall_Pull_Location = self.get_var("Tall Pull Location")
        Upper_Pull_Location = self.get_var("Upper Pull Location")
        eta = self.get_var("Extend Top Amount",'eta')
        eba = self.get_var("Extend Bottom Amount",'eba')
        World_Z = self.get_var('world_loc_z','World_Z',transform_type='LOC_Z')
        
        assembly.prompt("Pull X Location",'Pull_From_Edge',[Pull_From_Edge])
        if self.door_type == "Base":
            assembly.prompt("Pull Z Location",'Base_Pull_Location+(Pull_Length/2)',[Base_Pull_Location,Pull_Length])
        if self.door_type == "Tall":
            assembly.prompt("Pull Z Location",'Height-Tall_Pull_Location+(Pull_Length/2)+World_Z',[Height,World_Z,Tall_Pull_Location,Pull_Length])
        if self.door_type == "Upper":
            assembly.prompt("Pull Z Location",'Height+(eta+eba)-Upper_Pull_Location-(Pull_Length/2)',[Height,eta,eba,Upper_Pull_Location,Pull_Length])
    
    def draw(self):
        g = bpy.context.scene.lm_exteriors
        self.create_assembly()
        
        self.add_doors_prompts()
        
        Height = self.get_var('dim_z','Height')
        Width = self.get_var('dim_x','Width')
        Left_Overlay = self.get_var("Left Overlay")
        Right_Overlay = self.get_var("Right Overlay")
        Left_Swing = self.get_var("Left Swing")
        Vertical_Gap = self.get_var("Vertical Gap")
        Door_Rotation = self.get_var("Door Rotation")
        No_Pulls = self.get_var("No Pulls")
        False_Front_Height = self.get_var("False Front Height")
        Door_Thickness = self.get_var("Door Thickness")
        eta = self.get_var("Extend Top Amount",'eta')
        
        if self.door_type == 'Base':
            door_style_name = g.Base_Door_Style
        if self.door_type == 'Tall':
            door_style_name = g.Tall_Door_Style
        if self.door_type == 'Upper':
            door_style_name = g.Upper_Door_Style
            
        door_style = (HIDDEN_FOLDER_NAME,DOOR_LIBRARY_NAME,DOOR_CATEGORY_NAME,door_style_name)
        
        if self.false_front_qty > 0:
            front_style = (HIDDEN_FOLDER_NAME,DOOR_LIBRARY_NAME,DOOR_CATEGORY_NAME,g.Drawer_Front_Style)
            false_front = self.add_assembly(front_style)  
            false_front.set_name("False Front")
            false_front.x_loc('-Left_Overlay',[Left_Overlay])
            false_front.y_loc(value = 0)
            false_front.z_loc('Height+eta',[Height,eta])
            false_front.x_rot(value = 90)
            false_front.y_rot(value = 0)
            false_front.z_rot(value = 0)
            if self.false_front_qty > 1:
                false_front.x_dim('(Width+Left_Overlay+Right_Overlay-Vertical_Gap)/2',[Width,Left_Overlay,Right_Overlay,Vertical_Gap])
            else:
                false_front.x_dim('Width+Left_Overlay+Right_Overlay',[Width,Left_Overlay,Right_Overlay])
            false_front.y_dim('-False_Front_Height',[False_Front_Height])
            false_front.z_dim('Door_Thickness',[Door_Thickness])
            false_front.cutpart("Slab_Door")
            false_front.edgebanding('Door_Edges',l1 = True, w1 = True, l2 = True, w2 = True)
            
            if self.false_front_qty > 1:
                front_style = (HIDDEN_FOLDER_NAME,DOOR_LIBRARY_NAME,DOOR_CATEGORY_NAME,g.Drawer_Front_Style)
                false_front_2 = self.add_assembly(front_style)
                false_front_2.set_name("False Front")
                false_front_2.x_loc('Width+Right_Overlay',[Width,Right_Overlay])
                false_front_2.y_loc(value = 0)
                false_front_2.z_loc('Height+eta',[Height,eta])
                false_front_2.x_rot(value = 90)
                false_front_2.y_rot(value = 0)
                false_front_2.z_rot(value = 0)
                if self.false_front_qty > 1:
                    false_front_2.x_dim('((Width+Left_Overlay+Right_Overlay-Vertical_Gap)/2)*-1',[Width,Left_Overlay,Right_Overlay,Vertical_Gap])
                else:
                    false_front_2.x_dim('(Width+Left_Overlay+Right_Overlay)*-1',[Width,Left_Overlay,Right_Overlay])
                false_front_2.y_dim('-False_Front_Height',[False_Front_Height])
                false_front_2.z_dim('Door_Thickness',[Door_Thickness])
                false_front_2.cutpart("Slab_Door")
                false_front_2.edgebanding('Door_Edges',l1 = True, w1 = True, l2 = True, w2 = True)
        
        #LEFT DOOR
        left_door = self.add_assembly(door_style)  
        left_door.set_name(self.door_type + " Left Cabinet Door")
        self.set_standard_drivers(left_door)
        left_door.add_prompt(name="Hinge Quantity",prompt_type='QUANTITY',value=0,tab_index=0)
        left_door.x_loc('-Left_Overlay',[Left_Overlay])
        left_door.z_rot('radians(90)-Door_Rotation',[Door_Rotation])
        if self.door_swing == 'Double Door':
            left_door.y_dim('((Width+Left_Overlay+Right_Overlay-Vertical_Gap)/2)*-1',[Width,Left_Overlay,Right_Overlay,Vertical_Gap])
        else:
            left_door.y_dim('(Width+Left_Overlay+Right_Overlay)*-1',[Width,Left_Overlay,Right_Overlay])
            left_door.prompt('Hide','IF(Left_Swing,False,True)',[Left_Swing])
        left_door.cutpart("Slab_Door")
        left_door.edgebanding('Door_Edges',l1 = True, w1 = True, l2 = True, w2 = True)
        left_door.prompt('Hinge Quantity','MV_CALCULATE_HINGE_QTY(Height)',[Height])
        
        #LEFT PULL
        left_pull = LM_pulls.Standard_Pull()
        left_pull.door_type = self.door_type
        left_pull.door_swing = "Left Swing"
        left_pull.draw()
        left_pull.set_name('Left Cabinet Pull')
        left_pull.obj_bp.parent = self.obj_bp
        self.set_pull_drivers(left_pull)
        left_pull.x_loc('-Left_Overlay',[Left_Overlay])
        left_pull.z_rot('radians(90)-Door_Rotation',[Door_Rotation])
        if self.door_swing == 'Double Door':
            left_pull.y_dim('((Width+Left_Overlay+Right_Overlay-Vertical_Gap)/2)*-1',[Width,Left_Overlay,Right_Overlay,Vertical_Gap])
            left_pull.prompt('Hide','IF(No_Pulls,True,False)',[No_Pulls])
        else:
            left_pull.y_dim('(Width+Left_Overlay+Right_Overlay)*-1',[Width,Left_Overlay,Right_Overlay])
            left_pull.prompt('Hide','IF(Left_Swing,IF(No_Pulls,True,False),True)',[Left_Swing,No_Pulls])
            
        #RIGHT DOOR
        right_door = self.add_assembly(door_style)  
        right_door.set_name(self.door_type + " Right Cabinet Door")
        right_door.add_prompt(name="Hinge Quantity",prompt_type='QUANTITY',value=0,tab_index=0)
        self.set_standard_drivers(right_door)
        right_door.x_loc('Width+Right_Overlay',[Width,Right_Overlay])
        right_door.z_rot('radians(90)+Door_Rotation',[Door_Rotation])
        if self.door_swing == 'Double Door':
            right_door.y_dim('(Width+Left_Overlay+Right_Overlay-Vertical_Gap)/2',[Width,Left_Overlay,Right_Overlay,Vertical_Gap])
        else:
            right_door.y_dim('Width+Left_Overlay+Right_Overlay',[Width,Left_Overlay,Right_Overlay])
            right_door.prompt('Hide','IF(Left_Swing,True,False)',[Left_Swing])
        right_door.cutpart("Slab_Door")
        right_door.edgebanding('Door_Edges',l1 = True, w1 = True, l2 = True, w2 = True)
        right_door.prompt('Hinge Quantity','MV_CALCULATE_HINGE_QTY(Height)',[Height])
        
        #RIGHT PULL
        right_pull = LM_pulls.Standard_Pull()
        right_pull.door_type = self.door_type
        right_pull.door_swing = "Right Swing"
        right_pull.draw()
        right_pull.set_name('Right Cabinet Pull')
        right_pull.obj_bp.parent = self.obj_bp
        self.set_pull_drivers(right_pull)
        right_pull.x_loc('Width+Right_Overlay',[Width,Right_Overlay])
        right_pull.z_rot('radians(90)+Door_Rotation',[Door_Rotation])
        if self.door_swing == "Double Door":
            right_pull.y_dim('(Width+Left_Overlay+Right_Overlay-Vertical_Gap)/2',[Width,Left_Overlay,Right_Overlay,Vertical_Gap])
            right_pull.prompt('Hide','IF(No_Pulls,True,False)',[No_Pulls])
        else:
            right_pull.y_dim('(Width+Left_Overlay+Right_Overlay)',[Width,Left_Overlay,Right_Overlay])
            right_pull.prompt('Hide','IF(Left_Swing,True,IF(No_Pulls,True,False))',[Left_Swing,No_Pulls])
        
        self.update()
        
class Pie_Cut_Doors(fd.Library_Assembly):
    
    library_name = "Cabinet Exteriors"
    type_assembly = 'INSERT'
    placement_type = "EXTERIOR"
    property_id = "exteriors.door_prompts"
    door_type = "" # {Base, Tall, Upper}
    door_swing = "" # {Left Swing, Right Swing, Double Door, Flip up}

    def add_doors_prompts(self):
        g = bpy.context.scene.lm_exteriors
        
        self.add_tab(name='Door Options',tab_type='VISIBLE')
        self.add_tab(name='Formulas',tab_type='HIDDEN')
        
        add_common_door_prompts(self)
        
        self.add_prompt(name="Half Overlay Top",prompt_type='CHECKBOX',value=False,tab_index=0)
        self.add_prompt(name="Half Overlay Bottom",prompt_type='CHECKBOX',value=False,tab_index=0)
        self.add_prompt(name="Half Overlay Left",prompt_type='CHECKBOX',value=False,tab_index=0)
        self.add_prompt(name="Half Overlay Right",prompt_type='CHECKBOX',value=False,tab_index=0)
        
        self.add_prompt(name="Vertical Gap",prompt_type='DISTANCE',value=g.Vertical_Gap,tab_index=0)
        self.add_prompt(name="Top Reveal",prompt_type='DISTANCE',value=fd.inches(.25),tab_index=0)
        self.add_prompt(name="Bottom Reveal",prompt_type='DISTANCE',value=0,tab_index=0)
        self.add_prompt(name="Left Reveal",prompt_type='DISTANCE',value=g.Left_Reveal,tab_index=0)
        self.add_prompt(name="Right Reveal",prompt_type='DISTANCE',value=g.Right_Reveal,tab_index=0)
        
        #CALCULATED
        self.add_prompt(name="Top Overlay",prompt_type='DISTANCE',value=fd.inches(.6875),tab_index=1)
        self.add_prompt(name="Bottom Overlay",prompt_type='DISTANCE',value=fd.inches(.6875),tab_index=1)
        self.add_prompt(name="Left Overlay",prompt_type='DISTANCE',value=fd.inches(.6875),tab_index=1)
        self.add_prompt(name="Right Overlay",prompt_type='DISTANCE',value=fd.inches(.6875),tab_index=1)
        self.add_prompt(name="Hinge Quantity",prompt_type='QUANTITY',value=0,tab_index=1)
        
        #INHERITED
        self.add_prompt(name="Extend Top Amount",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Extend Bottom Amount",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Top Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Bottom Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Left Side Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Right Side Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Division Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        
        inset = self.get_var("Inset Front",'inset')
        ir = self.get_var("Inset Reveal",'ir')
        tr = self.get_var("Top Reveal",'tr')
        br = self.get_var("Bottom Reveal",'br')
        lr = self.get_var("Left Reveal",'lr')
        rr = self.get_var("Right Reveal",'rr')
        vg = self.get_var("Vertical Gap",'vg')
        hot = self.get_var("Half Overlay Top",'hot')
        hob = self.get_var("Half Overlay Bottom",'hob')
        hol = self.get_var("Half Overlay Left",'hol')
        hor = self.get_var("Half Overlay Right",'hor')
        tt = self.get_var("Top Thickness",'tt')
        lst = self.get_var("Left Side Thickness",'lst')
        rst = self.get_var("Right Side Thickness",'rst')
        bt = self.get_var("Bottom Thickness",'bt')
        height = self.get_var("dim_z",'height')
        
        if self.door_swing == 'Double Door':
            self.prompt('Hinge Quantity','MV_CALCULATE_HINGE_QTY(height)*2',[height])
        else:
            self.prompt('Hinge Quantity','MV_CALCULATE_HINGE_QTY(height)',[height])
        self.prompt('Top Overlay','IF(inset,-ir,IF(hot,(tt/2)-(vg/2),tt-tr))',[inset,ir,hot,tt,tr,vg])
        self.prompt('Bottom Overlay','IF(inset,-ir,IF(hob,(bt/2)-(vg/2),bt-br))',[inset,ir,hob,bt,br,vg])
        self.prompt('Left Overlay','IF(inset,-ir,IF(hol,(lst/2)-(vg/2),lst-lr))',[inset,ir,hol,lst,lr,vg])
        self.prompt('Right Overlay','IF(inset,-ir,IF(hor,(rst/2)-(vg/2),rst-rr))',[inset,ir,hor,rst,rr,vg])
        
    def set_standard_drivers(self,assembly):
        Height = self.get_var('dim_z','Height')
        Inset_Front = self.get_var("Inset Front")
        Door_Gap = self.get_var("Door to Cabinet Gap",'Door_Gap')
        tt = self.get_var("Top Thickness",'tt')
        bt = self.get_var("Bottom Thickness",'bt')
        Top_Overlay = self.get_var("Top Overlay")
        Bottom_Overlay = self.get_var("Bottom Overlay")
        eta = self.get_var("Extend Top Amount",'eta')
        eba = self.get_var("Extend Bottom Amount",'eba')
        Door_Thickness = self.get_var("Door Thickness")
        
#         assembly.y_loc('IF(Inset_Front,Door_Thickness,-Door_Gap)',[Inset_Front,Door_Gap,Door_Thickness])
        assembly.z_loc('IF(OR(eba==0,Inset_Front==True),-Bottom_Overlay,-eba)',
                       [Inset_Front,eba,bt,Bottom_Overlay])
        assembly.x_rot(value = 0)
        assembly.y_rot(value = -90)
        assembly.z_rot(value = 90)
#         assembly.x_dim('Height+IF(OR(eta==0,Inset_Front==True),Top_Overlay,tt+eta)+IF(OR(eba==0,Inset_Front==True),Bottom_Overlay,bt+eba)',
#                        [Inset_Front,Height,Top_Overlay,Bottom_Overlay,eta,eba,tt,bt])
        assembly.x_dim('Height+IF(OR(eta==0,Inset_Front==True),Top_Overlay,eta)+IF(OR(eba==0,Inset_Front==True),Bottom_Overlay,eba)',
                       [Inset_Front,Height,Top_Overlay,Bottom_Overlay,eta,eba,tt,bt])
        assembly.z_dim('Door_Thickness',[Door_Thickness])
        
    def set_pull_drivers(self,assembly):
        self.set_standard_drivers(assembly)
        
        Height = self.get_var('dim_z','Height')
        Pull_Length = assembly.get_var("Pull Length")
        Pull_From_Edge = self.get_var("Pull From Edge")
        Base_Pull_Location = self.get_var("Base Pull Location")
        Tall_Pull_Location = self.get_var("Tall Pull Location")
        Upper_Pull_Location = self.get_var("Upper Pull Location")
        eta = self.get_var("Extend Top Amount",'eta')
        eba = self.get_var("Extend Bottom Amount",'eba')
        
        assembly.prompt("Pull X Location",'Pull_From_Edge',[Pull_From_Edge])
        if self.door_type == "Base":
            assembly.prompt("Pull Z Location",'Base_Pull_Location+(Pull_Length/2)',[Base_Pull_Location,Pull_Length])
        if self.door_type == "Tall":
            assembly.prompt("Pull Z Location",'Tall_Pull_Location+(Pull_Length/2)',[Tall_Pull_Location,Pull_Length])
        if self.door_type == "Upper":
            assembly.prompt("Pull Z Location",'Height+(eta+eba)-Upper_Pull_Location-(Pull_Length/2)',[Height,eta,eba,Upper_Pull_Location,Pull_Length])
    
    def draw(self):
        g = bpy.context.scene.lm_exteriors
        self.create_assembly()
        
        self.add_doors_prompts()
        
        Width = self.get_var('dim_x','Width')
        Depth = self.get_var('dim_y','Depth')
        Height = self.get_var('dim_z','Height')
        Left_Overlay = self.get_var("Left Overlay")
        Right_Overlay = self.get_var("Right Overlay")
        Left_Swing = self.get_var("Left Swing")
        Vertical_Gap = self.get_var("Vertical Gap")
        Door_Rotation = self.get_var("Door Rotation")
        No_Pulls = self.get_var("No Pulls")
        Door_to_Cabinet_Gap = self.get_var("Door to Cabinet Gap")
        Door_Thickness = self.get_var("Door Thickness")
        Inset_Front = self.get_var("Inset Front")
        
        if self.door_type == 'Base':
            door_style_name = g.Base_Door_Style
        if self.door_type == 'Tall':
            door_style_name = g.Tall_Door_Style
        if self.door_type == 'Upper':
            door_style_name = g.Upper_Door_Style
        
        door_style = (HIDDEN_FOLDER_NAME,DOOR_LIBRARY_NAME,DOOR_CATEGORY_NAME,door_style_name)
        
        #LEFT DOOR
        left_door = self.add_assembly(door_style)  
        left_door.set_name(self.door_type + " Left Cabinet Door")
        left_door.add_prompt(name="Hinge Quantity",prompt_type='QUANTITY',value=0,tab_index=0)
        self.set_standard_drivers(left_door)
        left_door.x_loc('IF(Inset_Front,-Door_Thickness,Door_to_Cabinet_Gap)',[Door_to_Cabinet_Gap,Door_Thickness,Inset_Front])
        left_door.y_loc('Depth-Left_Overlay',[Depth,Left_Overlay])
        left_door.x_rot(value = 90)
        left_door.y_dim('(fabs(Depth)+Left_Overlay-IF(Inset_Front,0,Door_Thickness+Door_to_Cabinet_Gap))*-1',[Depth,Left_Overlay,Inset_Front,Right_Overlay,Door_Thickness,Door_to_Cabinet_Gap])
        left_door.cutpart("Slab_Door")
        left_door.edgebanding('Door_Edges',l1 = True, w1 = True, l2 = True, w2 = True)
        left_door.prompt('Hinge Quantity','MV_CALCULATE_HINGE_QTY(Height)',[Height])
        
        #LEFT PULL
        left_pull = LM_pulls.Standard_Pull()
        left_pull.door_type = self.door_type
        left_pull.draw()
        left_pull.set_name("Left Cabinet Pull")
        left_pull.obj_bp.parent = self.obj_bp
        self.set_pull_drivers(left_pull)
        left_pull.x_loc('IF(Inset_Front,-Door_Thickness,Door_to_Cabinet_Gap)',[Door_to_Cabinet_Gap,Door_Thickness,Inset_Front])
        left_pull.y_loc('-Door_to_Cabinet_Gap',[Door_to_Cabinet_Gap])
        left_pull.x_rot(value = 90)
        left_pull.y_dim('fabs(Depth)+Left_Overlay-Door_Thickness-Door_to_Cabinet_Gap',[Depth,Left_Overlay,Right_Overlay,Door_Thickness,Door_to_Cabinet_Gap])
        left_pull.prompt('Hide','IF(Left_Swing,True,IF(No_Pulls,True,False))',[Left_Swing,No_Pulls])
        
        #RIGHT DOOR
        right_door = self.add_assembly(door_style)  
        right_door.set_name(self.door_type + " Right Cabinet Door")
        self.set_standard_drivers(right_door)
        right_door.x_loc('IF(Inset_Front,0,Door_to_Cabinet_Gap+Door_Thickness)',[Inset_Front,Door_to_Cabinet_Gap,Door_Thickness])
        right_door.y_loc('IF(Inset_Front,Door_Thickness,-Door_to_Cabinet_Gap)',[Inset_Front,Door_to_Cabinet_Gap,Door_Thickness])
        right_door.y_dim('(Width+Right_Overlay-IF(Inset_Front,0,Door_Thickness+Door_to_Cabinet_Gap))*-1',[Width,Inset_Front,Right_Overlay,Door_Thickness,Door_to_Cabinet_Gap])
        right_door.cutpart("Slab_Door")
        right_door.edgebanding('Door_Edges',l1 = True, w1 = True, l2 = True, w2 = True)
        
        #RIGHT PULL
        right_pull = LM_pulls.Standard_Pull()
        right_pull.door_type = self.door_type
        right_pull.draw()
        right_pull.set_name("Right Cabinet Pull")
        right_pull.obj_bp.parent = self.obj_bp
        self.set_pull_drivers(right_pull)
        right_pull.x_loc('IF(Inset_Front,0,Door_to_Cabinet_Gap+Door_Thickness)',[Inset_Front,Door_to_Cabinet_Gap,Door_Thickness])
        right_pull.y_loc('IF(Inset_Front,Door_Thickness,-Door_to_Cabinet_Gap)',[Inset_Front,Door_to_Cabinet_Gap,Door_Thickness])
        right_pull.y_dim('(Width+Right_Overlay-IF(Inset_Front,0,Door_Thickness+Door_to_Cabinet_Gap))*-1',[Width,Inset_Front,Right_Overlay,Door_Thickness,Door_to_Cabinet_Gap])
        right_pull.prompt('Hide','IF(Left_Swing,IF(No_Pulls,True,False),True)',[Left_Swing,No_Pulls])
        
        self.update()
        
class Drawers(fd.Library_Assembly):
    
    library_name = "Cabinet Exteriors"
    property_id = "exteriors.drawer_prompts"
    type_assembly = 'INSERT'
    placement_type = "EXTERIOR"
    
    door_type = "Drawer"
    direction = 'Vertical'
    add_drawer = True
    add_pull = True
    drawer_qty = 1
    top_drawer_front_height = 0

    def add_common_prompts(self):
        g = bpy.context.scene.lm_exteriors
        self.add_tab(name='Drawer Options',tab_type='VISIBLE')
        self.add_tab(name='Formulas',tab_type='HIDDEN')
        
        add_common_drawer_prompts(self)
        
        self.add_prompt(name="Half Overlay Top",prompt_type='CHECKBOX',value=False,tab_index=0)
        self.add_prompt(name="Half Overlay Bottom",prompt_type='CHECKBOX',value=False,tab_index=0)
        self.add_prompt(name="Half Overlay Left",prompt_type='CHECKBOX',value=False,tab_index=0)
        self.add_prompt(name="Half Overlay Right",prompt_type='CHECKBOX',value=False,tab_index=0)
        
        self.add_prompt(name="Top Reveal",prompt_type='DISTANCE',value=fd.inches(0.125),tab_index=0)
        self.add_prompt(name="Bottom Reveal",prompt_type='DISTANCE',value=fd.inches(0.0),tab_index=0)
        self.add_prompt(name="Left Reveal",prompt_type='DISTANCE',value=fd.inches(0.0625),tab_index=0)
        self.add_prompt(name="Right Reveal",prompt_type='DISTANCE',value=fd.inches(0.0625),tab_index=0)
        self.add_prompt(name="Inset Reveal",prompt_type='DISTANCE',value=fd.inches(0.125),tab_index=0) 
        self.add_prompt(name="Horizontal Gap",prompt_type='DISTANCE',value=fd.inches(0.125),tab_index=0)
        
        self.add_prompt(name="Door to Cabinet Gap",prompt_type='DISTANCE',value=fd.inches(0.125),tab_index=0)   
        self.add_prompt(name="Drawer Box Top Gap",prompt_type='DISTANCE',value=fd.inches(0.5),tab_index=0)
        self.add_prompt(name="Drawer Box Bottom Gap",prompt_type='DISTANCE',value=fd.inches(0.5),tab_index=0)
        self.add_prompt(name="Drawer Box Slide Gap",prompt_type='DISTANCE',value=fd.inches(0.5),tab_index=0)
        self.add_prompt(name="Drawer Box Rear Gap",prompt_type='DISTANCE',value=fd.inches(0.5),tab_index=0)
        
        #INHERITED
        self.add_prompt(name="Left Side Thickness",prompt_type='DISTANCE',value=fd.inches(0.75),tab_index=1)
        self.add_prompt(name="Right Side Thickness",prompt_type='DISTANCE',value=fd.inches(0.75),tab_index=1)
        self.add_prompt(name="Top Thickness",prompt_type='DISTANCE',value=fd.inches(0.75),tab_index=1)
        self.add_prompt(name="Bottom Thickness",prompt_type='DISTANCE',value=fd.inches(0.75),tab_index=1)
        self.add_prompt(name="Back Thickness",prompt_type='DISTANCE',value=fd.inches(0.75),tab_index=1)
        self.add_prompt(name="Front Thickness",prompt_type='DISTANCE',value=fd.inches(0.75),tab_index=1)
        self.add_prompt(name="Division Thickness",prompt_type='DISTANCE',value=fd.inches(0.75),tab_index=1)
        
        #CALCULATED
        self.add_prompt(name="Top Overlay",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Bottom Overlay",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Left Overlay",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Right Overlay",prompt_type='DISTANCE',value=0,tab_index=1)
        
        inset = self.get_var('Inset Front','inset')
        inset_reveal = self.get_var('Inset Reveal','inset_reveal')
        lst = self.get_var('Left Side Thickness','lst')
        rst = self.get_var('Right Side Thickness','rst')
        tt = self.get_var('Top Thickness','tt')
        bt = self.get_var('Bottom Thickness','bt')
        hot = self.get_var("Half Overlay Top",'hot')
        hob = self.get_var("Half Overlay Bottom",'hob')
        hol = self.get_var("Half Overlay Left",'hol')
        hor = self.get_var("Half Overlay Right",'hor')  
        tr = self.get_var("Top Reveal",'tr')
        br = self.get_var("Bottom Reveal",'br')
        lr = self.get_var("Left Reveal",'lr')
        rr = self.get_var("Right Reveal",'rr')
        
        self.prompt("Top Overlay","IF(inset,-inset_reveal,IF(hot,(tt/2)-(tr/2),tt-tr))",
                    [inset,inset_reveal,hot,tt,tr])
        
        self.prompt("Bottom Overlay","IF(inset,-inset_reveal,IF(hob,(bt/2)-(br/2),bt-br))",
                    [inset,inset_reveal,hob,bt,br])
        
        self.prompt("Left Overlay","IF(inset,-inset_reveal,IF(hol,(lst/2)-(lr/2),lst-lr))",
                    [inset,inset_reveal,hol,lst,lr])
        
        self.prompt("Right Overlay","IF(inset,-inset_reveal,IF(hor,(rst/2)-(rr/2),rst-rr))",
                    [inset,inset_reveal,hor,rst,rr])
    
    def add_drawer_height_prompts(self):
        self.add_tab(name='Drawer Heights',tab_type='CALCULATOR',calc_type="ZDIM")
        
        top_drawer_front_equal = True
        
        if self.top_drawer_front_height != 0:
            top_drawer_front_equal = False
        
        if self.drawer_qty == 2 and self.direction == 'Vertical':
            self.add_prompt(name="Top Drawer Height",prompt_type='DISTANCE',value=self.top_drawer_front_height,tab_index=2,equal=top_drawer_front_equal)
            self.add_prompt(name="Bottom Drawer Height",prompt_type='DISTANCE',value=0,tab_index=2,equal=True)
            
        if self.drawer_qty == 3 and self.direction == 'Vertical':
            self.add_prompt(name="Top Drawer Height",prompt_type='DISTANCE',value=self.top_drawer_front_height,tab_index=2,equal=top_drawer_front_equal)
            self.add_prompt(name="Second Drawer Height",prompt_type='DISTANCE',value=0,tab_index=2,equal=True)
            self.add_prompt(name="Bottom Drawer Height",prompt_type='DISTANCE',value=0,tab_index=2,equal=True)
            
        if self.drawer_qty == 4 and self.direction == 'Vertical':
            self.add_prompt(name="Top Drawer Height",prompt_type='DISTANCE',value=self.top_drawer_front_height,tab_index=2,equal=top_drawer_front_equal)
            self.add_prompt(name="Second Drawer Height",prompt_type='DISTANCE',value=0,tab_index=2,equal=True)
            self.add_prompt(name="Third Drawer Height",prompt_type='DISTANCE',value=0,tab_index=2,equal=True)
            self.add_prompt(name="Bottom Drawer Height",prompt_type='DISTANCE',value=0,tab_index=2,equal=True)
            
        if self.drawer_qty == 5 and self.direction == 'Vertical':
            self.add_prompt(name="Top Drawer Height",prompt_type='DISTANCE',value=self.top_drawer_front_height,tab_index=2,equal=top_drawer_front_equal)
            self.add_prompt(name="Second Drawer Height",prompt_type='DISTANCE',value=0,tab_index=2,equal=True)
            self.add_prompt(name="Third Drawer Height",prompt_type='DISTANCE',value=0,tab_index=2,equal=True)
            self.add_prompt(name="Fourth Drawer Height",prompt_type='DISTANCE',value=0,tab_index=2,equal=True)
            self.add_prompt(name="Bottom Drawer Height",prompt_type='DISTANCE',value=0,tab_index=2,equal=True)
        
        if self.drawer_qty == 6 and self.direction == 'Vertical':
            self.add_prompt(name="Top Drawer Height",prompt_type='DISTANCE',value=self.top_drawer_front_height,tab_index=2,equal=top_drawer_front_equal)
            self.add_prompt(name="Second Drawer Height",prompt_type='DISTANCE',value=0,tab_index=2,equal=True)
            self.add_prompt(name="Third Drawer Height",prompt_type='DISTANCE',value=0,tab_index=2,equal=True)
            self.add_prompt(name="Fourth Drawer Height",prompt_type='DISTANCE',value=0,tab_index=2,equal=True)
            self.add_prompt(name="Fifth Drawer Height",prompt_type='DISTANCE',value=0,tab_index=2,equal=True)
            self.add_prompt(name="Bottom Drawer Height",prompt_type='DISTANCE',value=0,tab_index=2,equal=True)
            
        if self.drawer_qty == 7 and self.direction == 'Vertical':
            self.add_prompt(name="Top Drawer Height",prompt_type='DISTANCE',value=self.top_drawer_front_height,tab_index=2,equal=top_drawer_front_equal)
            self.add_prompt(name="Second Drawer Height",prompt_type='DISTANCE',value=0,tab_index=2,equal=True)
            self.add_prompt(name="Third Drawer Height",prompt_type='DISTANCE',value=0,tab_index=2,equal=True)
            self.add_prompt(name="Fourth Drawer Height",prompt_type='DISTANCE',value=0,tab_index=2,equal=True)
            self.add_prompt(name="Fifth Drawer Height",prompt_type='DISTANCE',value=0,tab_index=2,equal=True)
            self.add_prompt(name="Sixth Drawer Height",prompt_type='DISTANCE',value=0,tab_index=2,equal=True)
            self.add_prompt(name="Bottom Drawer Height",prompt_type='DISTANCE',value=0,tab_index=2,equal=True)
            
        if self.drawer_qty == 8 and self.direction == 'Vertical':
            self.add_prompt(name="Top Drawer Height",prompt_type='DISTANCE',value=self.top_drawer_front_height,tab_index=2,equal=top_drawer_front_equal)
            self.add_prompt(name="Second Drawer Height",prompt_type='DISTANCE',value=0,tab_index=2,equal=True)
            self.add_prompt(name="Third Drawer Height",prompt_type='DISTANCE',value=0,tab_index=2,equal=True)
            self.add_prompt(name="Fourth Drawer Height",prompt_type='DISTANCE',value=0,tab_index=2,equal=True)
            self.add_prompt(name="Fifth Drawer Height",prompt_type='DISTANCE',value=0,tab_index=2,equal=True)
            self.add_prompt(name="Sixth Drawer Height",prompt_type='DISTANCE',value=0,tab_index=2,equal=True)
            self.add_prompt(name="Seventh Drawer Height",prompt_type='DISTANCE',value=0,tab_index=2,equal=True)
            self.add_prompt(name="Bottom Drawer Height",prompt_type='DISTANCE',value=0,tab_index=2,equal=True)
            
        inset_reveal = self.get_var('Inset Reveal','inset_reveal')
        to = self.get_var("Top Overlay",'to')
        bo = self.get_var("Bottom Overlay",'bo')
        
        self.calculator_deduction("inset_reveal*(" + str(self.drawer_qty) +"-1)-bo-to",[inset_reveal,bo,to])

    def get_assemblies(self,name):
        """ Add a Drawer Front, Drawer Box, and Pull
            To this insert
            RETURNS: drawer front, drawer box, pull
        """
        g = bpy.context.scene.lm_exteriors
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z',"Height")
        Depth = self.get_var('dim_y',"Depth")
        Left_Overlay = self.get_var("Left Overlay")
        Right_Overlay = self.get_var("Right Overlay")
        Top_Overlay = self.get_var("Top Overlay")
        Bottom_Overlay = self.get_var("Bottom Overlay")
        Drawer_Box_Slide_Gap = self.get_var("Drawer Box Slide Gap")
        Door_to_Cabinet_Gap = self.get_var("Door to Cabinet Gap")
        Front_Thickness = self.get_var("Front Thickness")
        Drawer_Box_Rear_Gap = self.get_var("Drawer Box Rear Gap")
        Drawer_Box_Top_Gap = self.get_var("Drawer Box Top Gap")
        Drawer_Box_Bottom_Gap = self.get_var("Drawer Box Bottom Gap")
        Center_Pulls_on_Drawers = self.get_var("Center Pulls on Drawers")
        Drawer_Pull_From_Top = self.get_var("Drawer Pull From Top")
        No_Pulls = self.get_var("No Pulls")
        Inset_Front = self.get_var("Inset Front")
        Open = self.get_var("Open")
        
        door_style = (HIDDEN_FOLDER_NAME,DOOR_LIBRARY_NAME,DOOR_CATEGORY_NAME,g.Drawer_Front_Style)
        
        front = self.add_assembly(door_style)
        front.set_name(name + " Drawer Front")
        front.x_loc('-Left_Overlay',[Left_Overlay])
        front.y_loc('IF(Inset_Front,Front_Thickness,-Door_to_Cabinet_Gap)-(Depth*Open)',[Inset_Front,Door_to_Cabinet_Gap,Front_Thickness,Depth,Open])
        front.z_loc('-Bottom_Overlay',[Bottom_Overlay])
        front.x_rot(value = 90)
        front.y_rot(value = 0)
        front.z_rot(value = 0)
        front.x_dim('Width+Left_Overlay+Right_Overlay',[Width,Left_Overlay,Right_Overlay])
        front.y_dim('Height+Top_Overlay+Bottom_Overlay',[Height,Top_Overlay,Bottom_Overlay])
        front.z_dim('Front_Thickness',[Front_Thickness])
        front.cutpart("Slab_Drawer_Front")
        front.edgebanding('Door_Edges',l1 = True, w1 = True, l2 = True, w2 = True)
        
        drawer = None
        pull = None
        
        if self.add_drawer:
            drawer = LM_drawer_boxes.Wood_Drawer_Box()  #TODO: Add More Drawer Systems Dovetail, Metabox...
            drawer.draw()
            drawer.obj_bp.parent = self.obj_bp
            drawer.set_name(name + " Drawer Box")
            drawer.x_loc('Drawer_Box_Slide_Gap',[Drawer_Box_Slide_Gap])
            drawer.y_loc('IF(Inset_Front,Front_Thickness,-Door_to_Cabinet_Gap)-(Depth*Open)',[Inset_Front,Door_to_Cabinet_Gap,Front_Thickness,Depth,Open])
            drawer.z_loc('Drawer_Box_Bottom_Gap',[Drawer_Box_Bottom_Gap])
            drawer.x_rot(value = 0)
            drawer.y_rot(value = 0)
            drawer.z_rot(value = 0)
            drawer.x_dim('Width-(Drawer_Box_Slide_Gap*2)',[Width,Drawer_Box_Slide_Gap])
            drawer.y_dim('Depth-Drawer_Box_Rear_Gap-IF(Inset_Front,Front_Thickness,0)',[Depth,Drawer_Box_Rear_Gap,Inset_Front,Front_Thickness])
            drawer.z_dim('Height-Drawer_Box_Top_Gap-Drawer_Box_Bottom_Gap',[Height,Drawer_Box_Top_Gap,Drawer_Box_Bottom_Gap])
        
        if self.add_pull:
            pull = LM_pulls.Standard_Pull()
            pull.door_type = self.door_type
            pull.draw()
            pull.set_name('Cabinet Pull')
            pull.obj_bp.parent = self.obj_bp
            pull.x_loc('-Left_Overlay',[Left_Overlay])
            pull.y_loc('IF(Inset_Front,Front_Thickness,-Door_to_Cabinet_Gap)-(Depth*Open)',[Inset_Front,Door_to_Cabinet_Gap,Front_Thickness,Depth,Open])
            pull.z_loc('-Bottom_Overlay',[Bottom_Overlay])
            pull.x_rot(value = 90)
            pull.y_rot(value = 0)
            pull.z_rot(value = 0)
            pull.x_dim('Width+Left_Overlay+Right_Overlay',[Width,Left_Overlay,Right_Overlay])
            pull.y_dim('Height+Top_Overlay+Bottom_Overlay',[Height,Top_Overlay,Bottom_Overlay])
            pull.z_dim('Front_Thickness',[Front_Thickness])
            pull.prompt("Pull X Location",'IF(Center_Pulls_on_Drawers,Height/2,Drawer_Pull_From_Top)',[Center_Pulls_on_Drawers,Height,Drawer_Pull_From_Top])
            pull.prompt("Pull Z Location",'(Width/2)+Right_Overlay',[Width,Right_Overlay])
            pull.prompt("Hide",'IF(No_Pulls,True,False)',[No_Pulls])
        
        return front, drawer, pull
    
    def add_vertical_drawers(self):
        Height = self.get_var('dim_z','Height')
        Drawer_Box_Top_Gap = self.get_var('Drawer Box Top Gap')
        Drawer_Box_Bottom_Gap = self.get_var('Drawer Box Bottom Gap')
        Center_Pulls_On_Drawers = self.get_var("Center Pulls on Drawers")
        Top_Overlay = self.get_var("Top Overlay")
        Bottom_Overlay = self.get_var("Bottom Overlay")
        Drawer_Pull_From_Top = self.get_var("Drawer Pull From Top")
        Horizontal_Gap = self.get_var("Horizontal Gap")
        H1 = self.get_var("Top Drawer Height",'H1')
        H0 = self.get_var("Bottom Drawer Height",'H0')
        
        front, box, pull = self.get_assemblies('Bottom')
        front.z_loc("-Bottom_Overlay",[Bottom_Overlay])
        front.y_dim("H0",[H0])
        if box:
            box.z_loc("Drawer_Box_Bottom_Gap",[Drawer_Box_Bottom_Gap])
            box.z_dim("H0-Drawer_Box_Top_Gap-Drawer_Box_Bottom_Gap-Bottom_Overlay",[H0,Drawer_Box_Top_Gap,Drawer_Box_Bottom_Gap,Bottom_Overlay])
        if pull:
            pull.z_loc("-Bottom_Overlay",[Bottom_Overlay])
            pull.y_dim("H0",[H0])
            pull.prompt("Pull X Location",'IF(Center_Pulls_on_Drawers,H0/2,Drawer_Pull_From_Top)',[Center_Pulls_On_Drawers,H0,Drawer_Pull_From_Top])
            
        front, box, pull = self.get_assemblies('Top')
        front.z_loc("Height+Top_Overlay-H1",[Height,Top_Overlay,H1])
        front.y_dim("H1",[H1])
        Front_Z_Loc = front.get_var("loc_z","Front_Z_Loc")
        if box:
            box.z_loc("Front_Z_Loc+Drawer_Box_Bottom_Gap",[Front_Z_Loc,Drawer_Box_Bottom_Gap])
            box.z_dim("H1-Drawer_Box_Top_Gap-Drawer_Box_Bottom_Gap-Top_Overlay",[H1,Drawer_Box_Top_Gap,Drawer_Box_Bottom_Gap,Top_Overlay])
        if pull:
            pull.z_loc("Height+Top_Overlay-H1",[Height,Top_Overlay,H1])
            pull.y_dim("H1",[H1])
            pull.prompt("Pull X Location",'IF(Center_Pulls_on_Drawers,H1/2,Drawer_Pull_From_Top)',[Center_Pulls_On_Drawers,H1,Drawer_Pull_From_Top])
            
        if self.drawer_qty > 2:
            H2 = self.get_var("Second Drawer Height",'H2')
            front, box, pull = self.get_assemblies('Second')
            front.z_loc("Height+Top_Overlay-H1-H2-Horizontal_Gap",[Height,Top_Overlay,H1,H2,Drawer_Box_Bottom_Gap,Horizontal_Gap])
            front.y_dim("H2",[H2])
            Front_Z_Loc = front.get_var("loc_z","Front_Z_Loc")
            if box:
                box.z_loc("Front_Z_Loc+Drawer_Box_Bottom_Gap",[Front_Z_Loc,Drawer_Box_Bottom_Gap])
                box.z_dim("H2-Drawer_Box_Top_Gap-Drawer_Box_Bottom_Gap",[H2,Drawer_Box_Top_Gap,Drawer_Box_Bottom_Gap])
            if pull:
                pull.z_loc("Front_Z_Loc",[Front_Z_Loc])
                pull.y_dim("H2",[H2])
                pull.prompt("Pull X Location",'IF(Center_Pulls_on_Drawers,H2/2,Drawer_Pull_From_Top)',[Center_Pulls_On_Drawers,H2,Drawer_Pull_From_Top])
            
        if self.drawer_qty > 3:
            H3 = self.get_var("Third Drawer Height",'H3')
            front, box, pull = self.get_assemblies('Third')
            front.z_loc("Height+Top_Overlay-H1-H2-H3-(Horizontal_Gap*2)",[Height,Top_Overlay,H1,H2,H3,Drawer_Box_Bottom_Gap,Horizontal_Gap])
            front.y_dim("H3",[H3])
            Front_Z_Loc = front.get_var("loc_z","Front_Z_Loc")
            if box:
                box.z_loc("Front_Z_Loc+Drawer_Box_Bottom_Gap",[Front_Z_Loc,Drawer_Box_Bottom_Gap])
                box.z_dim("H3-Drawer_Box_Top_Gap-Drawer_Box_Bottom_Gap",[H3,Drawer_Box_Top_Gap,Drawer_Box_Bottom_Gap])
            if pull:
                pull.z_loc("Front_Z_Loc",[Front_Z_Loc])
                pull.y_dim("H3",[H3])
                pull.prompt("Pull X Location",'IF(Center_Pulls_on_Drawers,H3/2,Drawer_Pull_From_Top)',[Center_Pulls_On_Drawers,H3,Drawer_Pull_From_Top])

    def draw(self):
        self.create_assembly()
        self.add_common_prompts()

        if self.drawer_qty == 1:
            self.get_assemblies("Single")
        else:
            self.add_drawer_height_prompts()
            self.add_vertical_drawers()
        self.update()
        
class Horizontal_Drawers(fd.Library_Assembly):
    
    library_name = "Cabinet Exteriors"
    property_id = "exteriors.drawer_prompts"
    type_assembly = 'INSERT'
    placement_type = "EXTERIOR"
    
    door_type = "Drawer"
    add_drawer = True
    add_pull = True
    drawer_qty = 1
    top_drawer_front_height = 0

    def add_common_prompts(self):
        g = bpy.context.scene.lm_exteriors
        self.add_tab(name='Drawer Options',tab_type='VISIBLE')
        self.add_tab(name='Formulas',tab_type='HIDDEN')
        
        add_common_drawer_prompts(self)
        
        self.add_prompt(name="Half Overlay Top",prompt_type='CHECKBOX',value=False,tab_index=0)
        self.add_prompt(name="Half Overlay Bottom",prompt_type='CHECKBOX',value=False,tab_index=0)
        self.add_prompt(name="Half Overlay Left",prompt_type='CHECKBOX',value=False,tab_index=0)
        self.add_prompt(name="Half Overlay Right",prompt_type='CHECKBOX',value=False,tab_index=0)
        
        self.add_prompt(name="Vertical Gap",prompt_type='DISTANCE',value=g.Vertical_Gap,tab_index=0)
        self.add_prompt(name="Top Reveal",prompt_type='DISTANCE',value=fd.inches(.25),tab_index=0)
        self.add_prompt(name="Bottom Reveal",prompt_type='DISTANCE',value=0,tab_index=0)
        self.add_prompt(name="Left Reveal",prompt_type='DISTANCE',value=g.Left_Reveal,tab_index=0)
        self.add_prompt(name="Right Reveal",prompt_type='DISTANCE',value=g.Right_Reveal,tab_index=0)

        #CALCULATED
        self.add_prompt(name="Top Overlay",prompt_type='DISTANCE',value=fd.inches(.6875),tab_index=1)
        self.add_prompt(name="Bottom Overlay",prompt_type='DISTANCE',value=fd.inches(.6875),tab_index=1)
        self.add_prompt(name="Left Overlay",prompt_type='DISTANCE',value=fd.inches(.6875),tab_index=1)
        self.add_prompt(name="Right Overlay",prompt_type='DISTANCE',value=fd.inches(.6875),tab_index=1)
        self.add_prompt(name="Drawer Slide Quantity",prompt_type='QUANTITY',value=2,tab_index=1)
        
        #INHERITED
        self.add_prompt(name="Extend Top Amount",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Extend Bottom Amount",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Top Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Bottom Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Left Side Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Right Side Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Division Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        
        inset = self.get_var("Inset Front",'inset')
        ir = self.get_var("Inset Reveal",'ir')
        tr = self.get_var("Top Reveal",'tr')
        br = self.get_var("Bottom Reveal",'br')
        lr = self.get_var("Left Reveal",'lr')
        rr = self.get_var("Right Reveal",'rr')
        vg = self.get_var("Vertical Gap",'vg')
        hot = self.get_var("Half Overlay Top",'hot')
        hob = self.get_var("Half Overlay Bottom",'hob')
        hol = self.get_var("Half Overlay Left",'hol')
        hor = self.get_var("Half Overlay Right",'hor')
        tt = self.get_var("Top Thickness",'tt')
        lst = self.get_var("Left Side Thickness",'lst')
        rst = self.get_var("Right Side Thickness",'rst')
        bt = self.get_var("Bottom Thickness",'bt')
        
        self.prompt('Top Overlay','IF(inset,-ir,IF(hot,(tt/2)-(vg/2),tt-tr))',[inset,ir,hot,tt,tr,vg])
        self.prompt('Bottom Overlay','IF(inset,-ir,IF(hob,(bt/2)-(vg/2),bt-br))',[inset,ir,hob,bt,br,vg])
        self.prompt('Left Overlay','IF(inset,-ir,IF(hol,(lst/2)-(vg/2),lst-lr))',[inset,ir,hol,lst,lr,vg])
        self.prompt('Right Overlay','IF(inset,-ir,IF(hor,(rst/2)-(vg/2),rst-rr))',[inset,ir,hor,rst,rr,vg])
        
    def get_assemblies(self,name):
        """ Add a Drawer Front, Drawer Box, and Pull
            To this insert
            RETURNS: drawer front, drawer box, pull
        """
        g = bpy.context.scene.lm_exteriors
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z',"Height")
        Depth = self.get_var('dim_y',"Depth")
        Left_Overlay = self.get_var("Left Overlay")
        Right_Overlay = self.get_var("Right Overlay")
        Top_Overlay = self.get_var("Top Overlay")
        Bottom_Overlay = self.get_var("Bottom Overlay")
        Drawer_Box_Slide_Gap = self.get_var("Drawer Box Slide Gap")
        Door_to_Cabinet_Gap = self.get_var("Door to Cabinet Gap")
        Front_Thickness = self.get_var("Front Thickness")
        Drawer_Box_Rear_Gap = self.get_var("Drawer Box Rear Gap")
        Drawer_Box_Top_Gap = self.get_var("Drawer Box Top Gap")
        Drawer_Box_Bottom_Gap = self.get_var("Drawer Box Bottom Gap")
        Center_Pulls_on_Drawers = self.get_var("Center Pulls on Drawers")
        Drawer_Pull_From_Top = self.get_var("Drawer Pull From Top")
        No_Pulls = self.get_var("No Pulls")
        Vertical_Gap = self.get_var("Vertical Gap")
        Division_Thickness = self.get_var("Division Thickness")
        Open = self.get_var("Open")
        Inset_Front = self.get_var("Inset Front")
        
        front_style = (HIDDEN_FOLDER_NAME,DOOR_LIBRARY_NAME,DOOR_CATEGORY_NAME,g.Drawer_Front_Style)
        
        front = self.add_assembly(front_style)
        front.set_name(name + " Drawer Front")
        if name == "Left":
            front.x_loc('-Left_Overlay',[Left_Overlay])
        if name == "Right":
            front.x_loc('(Width/2)+(Vertical_Gap/2)',[Width,Vertical_Gap])
        front.y_loc('IF(Inset_Front,Front_Thickness,-Door_to_Cabinet_Gap)-(Depth*Open)',[Inset_Front,Door_to_Cabinet_Gap,Front_Thickness,Depth,Open])
        front.z_loc('-Bottom_Overlay',[Bottom_Overlay])
        front.x_rot(value = 90)
        front.y_rot(value = 0)
        front.z_rot(value = 0)
        if name == "Left":
            front.x_dim('((Width-Vertical_Gap)/2)+Left_Overlay',[Width,Vertical_Gap,Left_Overlay])
        if name == "Right":
            front.x_dim('((Width-Vertical_Gap)/2)+Right_Overlay',[Width,Vertical_Gap,Right_Overlay])
        front.y_dim('Height+Top_Overlay+Bottom_Overlay',[Height,Top_Overlay,Bottom_Overlay])
        front.z_dim('Front_Thickness',[Front_Thickness])
        front.cutpart("Slab_Drawer_Front")
        front.edgebanding('Door_Edges',l1 = True, w1 = True, l2 = True, w2 = True)
        
        drawer = LM_drawer_boxes.Wood_Drawer_Box()  #TODO: Add More Drawer Systems Dovetail, Metabox...
        drawer.draw()
        drawer.obj_bp.parent = self.obj_bp
        drawer.set_name(name + " Drawer Box")
        if name == "Left":
            drawer.x_loc('Drawer_Box_Slide_Gap',[Drawer_Box_Slide_Gap])
        if name == "Right":
            drawer.x_loc('(Width/2)+(Division_Thickness/2)+Drawer_Box_Slide_Gap',[Width,Division_Thickness,Drawer_Box_Slide_Gap])
        drawer.y_loc('IF(Inset_Front,Front_Thickness,-Door_to_Cabinet_Gap)-(Depth*Open)',[Inset_Front,Door_to_Cabinet_Gap,Front_Thickness,Depth,Open])
        drawer.z_loc('Drawer_Box_Bottom_Gap',[Drawer_Box_Bottom_Gap])
        drawer.x_rot(value = 0)
        drawer.y_rot(value = 0)
        drawer.z_rot(value = 0)
        drawer.x_dim('((Width-Division_Thickness)/2)-(Drawer_Box_Slide_Gap*2)',[Width,Division_Thickness,Drawer_Box_Slide_Gap])
        drawer.y_dim('Depth-Drawer_Box_Rear_Gap',[Depth,Drawer_Box_Rear_Gap])
        drawer.z_dim('Height-Drawer_Box_Top_Gap-Drawer_Box_Bottom_Gap',[Height,Drawer_Box_Top_Gap,Drawer_Box_Bottom_Gap])
        
        pull = LM_pulls.Standard_Pull()
        pull.door_type = self.door_type
        pull.draw()
        pull.obj_bp.parent = self.obj_bp
        pull.set_name(name + " Cabinet Pull")
        if name == "Left":
            pull.x_loc('-Left_Overlay',[Left_Overlay])
        if name == "Right":
            pull.x_loc('(Width/2)+(Vertical_Gap/2)',[Width,Vertical_Gap])
        pull.y_loc('IF(Inset_Front,Front_Thickness,-Door_to_Cabinet_Gap)-(Depth*Open)',[Inset_Front,Door_to_Cabinet_Gap,Front_Thickness,Depth,Open])
        pull.z_loc('-Bottom_Overlay',[Bottom_Overlay])
        pull.x_rot(value = 90)
        pull.y_rot(value = 0)
        pull.z_rot(value = 0)
        if name == "Left":
            pull.x_dim('((Width-Vertical_Gap)/2)+Left_Overlay',[Width,Vertical_Gap,Left_Overlay])
        if name == "Right":
            pull.x_dim('((Width-Vertical_Gap)/2)+Right_Overlay',[Width,Vertical_Gap,Right_Overlay])
        pull.y_dim('Height+Top_Overlay+Bottom_Overlay',[Height,Top_Overlay,Bottom_Overlay])
        pull.z_dim('Front_Thickness',[Front_Thickness])
        pull.prompt("Pull X Location",'IF(Center_Pulls_on_Drawers,Height/2,Drawer_Pull_From_Top)',[Center_Pulls_on_Drawers,Height,Drawer_Pull_From_Top])
        pull.prompt("Pull Z Location",'(Width/4)',[Width,Right_Overlay])
        pull.prompt("Hide",'IF(No_Pulls,True,False)',[No_Pulls])
        
        return front, drawer, pull
    
    def add_horizontal_drawers(self):
        self.get_assemblies("Left")
        self.get_assemblies("Right")

    def draw(self):
        self.create_assembly()
        self.add_common_prompts()
        
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z',"Height")
        Depth = self.get_var('dim_y',"Depth")
        Division_Thickness = self.get_var("Division Thickness")
        Inset_Front = self.get_var("Inset Front")
        Front_Thickness = self.get_var("Front Thickness")
        
        division = self.add_assembly(DIVISION)
        division.set_name("Drawer Division")
        division.x_loc('(Width/2)-(Division_Thickness/2)',[Width,Division_Thickness])
        division.y_loc('IF(Inset_Front,Front_Thickness,0)',[Inset_Front,Front_Thickness])
        division.z_loc(value = 0)
        division.x_rot(value = 90)
        division.y_rot(value = 0)
        division.z_rot(value = 90)
        division.x_dim('Depth-IF(Inset_Front,Front_Thickness,0)',[Depth,Inset_Front,Front_Thickness])
        division.y_dim('Height',[Height])
        division.z_dim('Division_Thickness',[Division_Thickness])
        
        self.add_horizontal_drawers()
        self.update()
        
class Tilt_Out_Hamper(fd.Library_Assembly):

    library_name = "Cabinet Exteriors"
    placement_type = "EXTERIOR"
    property_id = "exteriors.hamper_prompts"
    type_assembly = "INSERT"
    mirror_y = False
    
    def add_common_prompts(self):
        g = bpy.context.scene.lm_exteriors
        self.add_tab(name='Hamper Options',tab_type='VISIBLE')
        self.add_tab(name='Formulas',tab_type='HIDDEN')

        self.add_prompt(name="No Pulls",prompt_type='CHECKBOX',value=False,tab_index=0)
        self.add_prompt(name="Center Pulls on Drawers",prompt_type='CHECKBOX',value=g.Center_Pulls_on_Drawers,tab_index=0)
        self.add_prompt(name="Drawer Pull From Top",prompt_type='DISTANCE',value=g.Drawer_Pull_From_Top,tab_index=0)
        self.add_prompt(name="Pull Double Max Span",prompt_type='DISTANCE',value=fd.inches(30),tab_index=0)
        self.add_prompt(name="Lock From Top",prompt_type='DISTANCE',value=fd.inches(1.0),tab_index=0)
        self.add_prompt(name="Lock Drawer",prompt_type='CHECKBOX',value=False,tab_index=0)
        self.add_prompt(name="Inset Front",prompt_type='CHECKBOX',value=False,tab_index=0)
        self.add_prompt(name="Open",prompt_type='PERCENTAGE',value=0,tab_index=0)

        self.add_prompt(name="Half Overlay Top",prompt_type='CHECKBOX',value=True,tab_index=0)
        self.add_prompt(name="Half Overlay Bottom",prompt_type='CHECKBOX',value=True,tab_index=0)
        self.add_prompt(name="Half Overlay Left",prompt_type='CHECKBOX',value=True,tab_index=0)
        self.add_prompt(name="Half Overlay Right",prompt_type='CHECKBOX',value=True,tab_index=0)
        self.add_prompt(name="Top Reveal",prompt_type='DISTANCE',value=fd.inches(0.125),tab_index=0)
        self.add_prompt(name="Bottom Reveal",prompt_type='DISTANCE',value=fd.inches(0.0),tab_index=0)
        self.add_prompt(name="Left Reveal",prompt_type='DISTANCE',value=fd.inches(0.0625),tab_index=0)
        self.add_prompt(name="Right Reveal",prompt_type='DISTANCE',value=fd.inches(0.0625),tab_index=0)
        self.add_prompt(name="Inset Reveal",prompt_type='DISTANCE',value=fd.inches(0.125),tab_index=0) 
        self.add_prompt(name="Horizontal Gap",prompt_type='DISTANCE',value=fd.inches(0.125),tab_index=0)
        self.add_prompt(name="Door to Cabinet Gap",prompt_type='DISTANCE',value=fd.inches(0.125),tab_index=0)   
        self.add_prompt(name="Drawer Box Top Gap",prompt_type='DISTANCE',value=fd.inches(0.5),tab_index=0)
        self.add_prompt(name="Drawer Box Bottom Gap",prompt_type='DISTANCE',value=fd.inches(0.5),tab_index=0)
        self.add_prompt(name="Drawer Box Slide Gap",prompt_type='DISTANCE',value=fd.inches(0.5),tab_index=0)
        self.add_prompt(name="Drawer Box Rear Gap",prompt_type='DISTANCE',value=fd.inches(0.5),tab_index=0)
        
        self.add_prompt(name="Left Side Thickness",prompt_type='DISTANCE',value=fd.inches(0.75),tab_index=1)
        self.add_prompt(name="Right Side Thickness",prompt_type='DISTANCE',value=fd.inches(0.75),tab_index=1)
        self.add_prompt(name="Top Thickness",prompt_type='DISTANCE',value=fd.inches(0.75),tab_index=1)
        self.add_prompt(name="Bottom Thickness",prompt_type='DISTANCE',value=fd.inches(0.75),tab_index=1)
        self.add_prompt(name="Back Thickness",prompt_type='DISTANCE',value=fd.inches(0.75),tab_index=1)
        self.add_prompt(name="Front Thickness",prompt_type='DISTANCE',value=fd.inches(0.75),tab_index=1)
        self.add_prompt(name="Division Thickness",prompt_type='DISTANCE',value=fd.inches(0.75),tab_index=1)
        self.add_prompt(name="Top Overlay",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Bottom Overlay",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Left Overlay",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Right Overlay",prompt_type='DISTANCE',value=0,tab_index=1)

        inset = self.get_var('Inset Front','inset')
        inset_reveal = self.get_var('Inset Reveal','inset_reveal')
        premium = self.get_var('Use Premium Package','premium')
        lst = self.get_var('Left Side Thickness','lst')
        rst = self.get_var('Right Side Thickness','rst')
        tt = self.get_var('Top Thickness','tt')
        bt = self.get_var('Bottom Thickness','bt')
        hot = self.get_var("Half Overlay Top",'hot')
        hob = self.get_var("Half Overlay Bottom",'hob')
        hol = self.get_var("Half Overlay Left",'hol')
        hor = self.get_var("Half Overlay Right",'hor')  
        tr = self.get_var("Top Reveal",'tr')
        br = self.get_var("Bottom Reveal",'br')
        lr = self.get_var("Left Reveal",'lr')
        rr = self.get_var("Right Reveal",'rr')
        
        self.prompt("Top Overlay","IF(inset,-inset_reveal,IF(hot,(tt/2)-(tr/2),tt-tr))",
                    [inset,inset_reveal,hot,tt,tr])
        
        self.prompt("Bottom Overlay","IF(inset,-inset_reveal,IF(hob,(bt/2)-(br/2),bt-br))",
                    [inset,inset_reveal,hob,bt,br])
        
        self.prompt("Left Overlay","IF(premium,-inset_reveal,IF(inset,-inset_reveal,IF(hol,(lst/2)-(lr/2),lst-lr)))",
                    [inset,inset_reveal,hol,lst,lr,premium])
        
        self.prompt("Right Overlay","IF(premium,-inset_reveal,IF(inset,-inset_reveal,IF(hor,(rst/2)-(rr/2),rst-rr)))",
                    [inset,inset_reveal,hor,rst,rr,premium])

    def draw(self):
        g = bpy.context.scene.lm_exteriors
        
        self.create_assembly()
        
        self.add_common_prompts()
        
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z',"Height")
        Depth = self.get_var('dim_y',"Depth")
        Left_Overlay = self.get_var("Left Overlay")
        Right_Overlay = self.get_var("Right Overlay")
        Top_Overlay = self.get_var("Top Overlay")
        Bottom_Overlay = self.get_var("Bottom Overlay")
        Door_to_Cabinet_Gap = self.get_var("Door to Cabinet Gap")
        Front_Thickness = self.get_var("Front Thickness")
        Center_Pulls_on_Drawers = self.get_var("Center Pulls on Drawers")
        Drawer_Pull_From_Top = self.get_var("Drawer Pull From Top")
        Open = self.get_var("Open")
        Inset_Front = self.get_var("Inset Front")
        
        front = self.add_assembly((HIDDEN_FOLDER_NAME,DOOR_LIBRARY_NAME,DOOR_CATEGORY_NAME,g.Drawer_Front_Style))
        front.set_name("Hamper Door")
        front.add_prompt(name="Hinge Quantity",prompt_type='QUANTITY',value=0,tab_index=0)
        front.x_loc('-Left_Overlay',[Left_Overlay])
        front.y_loc('IF(Inset_Front,Front_Thickness,-Door_to_Cabinet_Gap)',[Door_to_Cabinet_Gap,Inset_Front,Front_Thickness])
        front.z_loc('-Bottom_Overlay',[Bottom_Overlay])
        front.x_rot(value = 0)
        front.y_rot('radians(-90)-(Open*.5)',[Open])
        front.z_rot(value = 90)
        front.x_dim('Height+Top_Overlay+Bottom_Overlay',[Height,Top_Overlay,Bottom_Overlay])
        front.y_dim('(Width+Left_Overlay+Right_Overlay)*-1',[Width,Left_Overlay,Right_Overlay])
        front.z_dim('Front_Thickness',[Front_Thickness])
        front.cutpart("Slab_Door")
        front.edgebanding('Door_Edges',l1 = True, w1 = True, l2 = True, w2 = True)
        front.prompt('Hinge Quantity','MV_CALCULATE_HINGE_QTY(Width)',[Width])
        
        pull = LM_pulls.Standard_Pull()
        pull.door_type = "Drawer"
        pull.draw()
        pull.set_name('Cabinet Pull')
        pull.obj_bp.parent = self.obj_bp
        pull.set_name("Hamper Cabinet Pull")
        pull.x_loc('-Left_Overlay',[Left_Overlay])
        pull.y_loc('IF(Inset_Front,Front_Thickness,-Door_to_Cabinet_Gap)',[Door_to_Cabinet_Gap,Inset_Front,Front_Thickness])
        pull.z_loc('-Bottom_Overlay',[Bottom_Overlay])
        pull.x_rot('radians(90)+(Open*.5)',[Open])
        pull.y_rot(value = 0)
        pull.z_rot(value = 0)
        pull.x_dim('Width+Left_Overlay+Right_Overlay',[Width,Left_Overlay,Right_Overlay])
        pull.y_dim('Height+Top_Overlay+Bottom_Overlay',[Height,Top_Overlay,Bottom_Overlay])
        pull.z_dim('Front_Thickness',[Front_Thickness])
        pull.prompt("Pull X Location",'IF(Center_Pulls_on_Drawers,Height/2,Drawer_Pull_From_Top)',[Center_Pulls_on_Drawers,Height,Drawer_Pull_From_Top])
        pull.prompt("Pull Z Location",'(Width/2)+Right_Overlay',[Width,Right_Overlay])
        
        basket_1 = self.add_assembly(WIRE_BASKET)
        basket_1.set_name("Hamper Basket")
        basket_1.x_loc(value = 0)
        basket_1.y_loc(value = 0)
        basket_1.z_loc(value = 0)
        basket_1.x_rot('Open*.5',[Open])
        basket_1.y_rot(value = 0)
        basket_1.z_rot(value = 0)
        basket_1.x_dim('Width',[Width])
        basket_1.y_dim('Depth',[Depth])
        basket_1.z_dim('Height-INCH(8)',[Height])
        basket_1.material('Wire Basket')
        
        self.update()
        
class FF_Doors(fd.Library_Assembly):
    
    library_name = "Cabinet Exteriors"
    type_assembly = 'INSERT'
    placement_type = "EXTERIOR"
    property_id = "exteriors.door_prompts"
    door_type = "" # {Base, Tall, Upper}
    door_swing = "" # {Left Swing, Right Swing, Double Door, Flip up}

    def add_doors_prompts(self):
        g = bpy.context.scene.lm_exteriors
        
        self.add_tab(name='Door Options',tab_type='VISIBLE')
        self.add_tab(name='Formulas',tab_type='HIDDEN')
        
        add_common_door_prompts(self)
        
        self.add_prompt(name="Mid Rail Width",prompt_type='DISTANCE',value=fd.inches(2),tab_index=0)
        self.add_prompt(name="Top Overlay",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        self.add_prompt(name="Bottom Overlay",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        self.add_prompt(name="Left Overlay",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        self.add_prompt(name="Right Overlay",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        
        #INHERITED
        self.add_prompt(name="Frame Thickness",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Frame Left Gap",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Frame Right Gap",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Frame Top Gap",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Frame Bottom Gap",prompt_type='DISTANCE',value=0,tab_index=1)
        
        #For Diagonal Corner Cabinet
        self.add_prompt(name="Door Y Offset",prompt_type='DISTANCE',value=0,tab_index=1)
        
        height = self.get_var("dim_z",'height')
        
    def set_standard_drivers(self,assembly):
        Height = self.get_var('dim_z','Height')
        Inset_Front = self.get_var("Inset Front")
        Inset_Reveal = self.get_var("Inset Reveal")
        Door_to_Cabinet_Gap = self.get_var("Door to Cabinet Gap")
        Top_Overlay = self.get_var("Top Overlay")
        Bottom_Overlay = self.get_var("Bottom Overlay")
        Door_Thickness = self.get_var("Door Thickness")
        Frame_Top_Gap = self.get_var("Frame Top Gap")
        Frame_Bottom_Gap = self.get_var("Frame Bottom Gap")
        Frame_Thickness = self.get_var("Frame Thickness")
        #For Diagonal Corner Cabinet
        Door_Y_Offset = self.get_var("Door Y Offset")        
        
        
        assembly.y_loc('IF(Inset_Front,Door_Y_Offset,-Door_to_Cabinet_Gap-Frame_Thickness)',[Inset_Front,Door_to_Cabinet_Gap,Door_Thickness,Frame_Thickness,Door_Y_Offset])
        assembly.z_loc('IF(Inset_Front,Frame_Bottom_Gap+Inset_Reveal,Frame_Bottom_Gap-Bottom_Overlay)',
                       [Inset_Front,Frame_Bottom_Gap,Inset_Reveal,Frame_Bottom_Gap,Bottom_Overlay])
        assembly.x_rot(value = 0)
        assembly.y_rot(value = -90)
        assembly.x_dim('Height-(Frame_Top_Gap+Frame_Bottom_Gap)+IF(Inset_Front,-(Inset_Reveal*2),Bottom_Overlay+Top_Overlay)',
                       [Inset_Front,Height,Top_Overlay,Bottom_Overlay,Frame_Top_Gap,Frame_Bottom_Gap,Inset_Reveal])
        assembly.z_dim('Door_Thickness',[Door_Thickness])
        
    def set_pull_drivers(self,assembly):
        self.set_standard_drivers(assembly)
        
        Height = self.get_var('dim_z','Height')
        Pull_Length = assembly.get_var("Pull Length")
        Pull_From_Edge = self.get_var("Pull From Edge")
        Base_Pull_Location = self.get_var("Base Pull Location")
        Tall_Pull_Location = self.get_var("Tall Pull Location")
        Upper_Pull_Location = self.get_var("Upper Pull Location")
        World_Z = self.get_var('world_loc_z','World_Z',transform_type='LOC_Z')
        
        assembly.prompt("Pull X Location",'Pull_From_Edge',[Pull_From_Edge])
        if self.door_type == "Base":
            assembly.prompt("Pull Z Location",'Base_Pull_Location+(Pull_Length/2)',[Base_Pull_Location,Pull_Length])
        if self.door_type == "Tall":
            assembly.prompt("Pull Z Location",'Height-Tall_Pull_Location+(Pull_Length/2)+World_Z',[Height,World_Z,Tall_Pull_Location,Pull_Length])
        if self.door_type == "Upper":
            assembly.prompt("Pull Z Location",'Height-Upper_Pull_Location-(Pull_Length/2)',[Height,Upper_Pull_Location,Pull_Length])
    
    def draw(self):
        g = bpy.context.scene.lm_exteriors
        self.create_assembly()
        
        self.add_doors_prompts()
        
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Inset_Front = self.get_var("Inset Front")
        Inset_Reveal = self.get_var("Inset Reveal")
        Left_Overlay = self.get_var("Left Overlay")
        Right_Overlay = self.get_var("Right Overlay")
        Door_Rotation = self.get_var("Door Rotation")
        Mid_Rail_Width = self.get_var("Mid Rail Width")
        No_Pulls = self.get_var("No Pulls")
        Left_Swing = self.get_var("Left Swing")
        
        Frame_Left_Gap = self.get_var("Frame Left Gap")
        Frame_Right_Gap = self.get_var("Frame Right Gap")
        Frame_Top_Gap = self.get_var("Frame Top Gap")
        Frame_Bottom_Gap = self.get_var("Frame Bottom Gap")
        
        if self.door_type == 'Base':
            door_style_name = g.Base_Door_Style
        if self.door_type == 'Tall':
            door_style_name = g.Tall_Door_Style
        if self.door_type == 'Upper':
            door_style_name = g.Upper_Door_Style
        
        door_style = (HIDDEN_FOLDER_NAME,DOOR_LIBRARY_NAME,DOOR_CATEGORY_NAME,door_style_name)
        
        left_door = self.add_assembly(door_style)
        left_door.set_name(self.door_type + " Left Cabinet Door")
        left_door.add_prompt(name="Hinge Quantity",prompt_type='QUANTITY',value=0,tab_index=0)
        self.set_standard_drivers(left_door)
        left_door.x_loc('Frame_Left_Gap+IF(Inset_Front,Inset_Reveal,-Left_Overlay)',[Frame_Left_Gap,Left_Overlay,Inset_Front,Inset_Reveal])
        left_door.z_rot('radians(90)-Door_Rotation',[Door_Rotation])
        if self.door_swing == "Double Door":
            left_door.y_dim('(((Width-(Frame_Left_Gap+Frame_Right_Gap)-Mid_Rail_Width)/2)+IF(Inset_Front,-(Inset_Reveal*2),(Left_Overlay+Right_Overlay)))*-1',
                            [Width,Frame_Left_Gap,Frame_Right_Gap,Left_Overlay,Right_Overlay,Mid_Rail_Width,Inset_Reveal,Inset_Front])
        else:
            left_door.y_dim('(Width-(Frame_Left_Gap+Frame_Right_Gap)+IF(Inset_Front,-(Inset_Reveal*2),(Left_Overlay+Right_Overlay)))*-1',
                            [Width,Frame_Left_Gap,Frame_Right_Gap,Left_Overlay,Right_Overlay,Inset_Front,Inset_Reveal])
            left_door.prompt("Hide",'IF(Left_Swing,False,True)',[Left_Swing])
        left_door.cutpart("Slab_Door")
        left_door.edgebanding('Door_Edges',l1 = True, w1 = True, l2 = True, w2 = True)
        left_door.prompt('Hinge Quantity','MV_CALCULATE_HINGE_QTY(Height)',[Height])
        
        left_pull = LM_pulls.Standard_Pull()
        left_pull.door_type = self.door_type
        left_pull.door_swing = "Left Swing"
        left_pull.draw()
        left_pull.set_name("Left Pull")
        left_pull.obj_bp.parent = self.obj_bp
        self.set_pull_drivers(left_pull)
        left_pull.x_loc('Frame_Left_Gap+IF(Inset_Front,Inset_Reveal,-Left_Overlay)',[Frame_Left_Gap,Left_Overlay,Inset_Front,Inset_Reveal])
        left_pull.z_rot('radians(90)-Door_Rotation',[Door_Rotation])
        if self.door_swing == 'Double Door':
            left_pull.y_dim('(((Width-(Frame_Left_Gap+Frame_Right_Gap)-Mid_Rail_Width)/2)+IF(Inset_Front,-(Inset_Reveal*2),(Left_Overlay+Right_Overlay)))*-1',
                            [Width,Frame_Left_Gap,Frame_Right_Gap,Left_Overlay,Right_Overlay,Mid_Rail_Width,Inset_Reveal,Inset_Front])
            left_pull.prompt('Hide','IF(No_Pulls,True,False)',[No_Pulls])
        else:
            left_pull.y_dim('(Width-(Frame_Left_Gap+Frame_Right_Gap)+IF(Inset_Front,-(Inset_Reveal*2),(Left_Overlay+Right_Overlay)))*-1',
                            [Width,Frame_Left_Gap,Frame_Right_Gap,Left_Overlay,Right_Overlay,Inset_Front,Inset_Reveal])
            left_pull.prompt('Hide','IF(Left_Swing,IF(No_Pulls,True,False),True)',[Left_Swing,No_Pulls])
        
        right_door = self.add_assembly(door_style)
        right_door.set_name(self.door_type + " Right Cabinet Door")
        right_door.add_prompt(name="Hinge Quantity",prompt_type='QUANTITY',value=0,tab_index=0)
        self.set_standard_drivers(right_door)
        right_door.x_loc('Width-Frame_Right_Gap+IF(Inset_Front,-Inset_Reveal,Right_Overlay)',[Width,Frame_Right_Gap,Right_Overlay,Inset_Front,Inset_Reveal])
        right_door.z_rot('radians(90)+Door_Rotation',[Door_Rotation])
        if self.door_swing == "Double Door":
            right_door.y_dim('((Width-(Frame_Left_Gap+Frame_Right_Gap)-Mid_Rail_Width)/2)+IF(Inset_Front,-(Inset_Reveal*2),(Left_Overlay+Right_Overlay))',
                             [Width,Frame_Left_Gap,Frame_Right_Gap,Left_Overlay,Right_Overlay,Mid_Rail_Width,Inset_Front,Inset_Reveal])
        else:
            right_door.y_dim('Width-(Frame_Left_Gap+Frame_Right_Gap)+IF(Inset_Front,-(Inset_Reveal*2),(Left_Overlay+Right_Overlay))',
                             [Width,Frame_Left_Gap,Frame_Right_Gap,Inset_Front,Inset_Reveal,Left_Overlay,Right_Overlay])
            right_door.prompt("Hide",'IF(Left_Swing,True,False)',[Left_Swing])
        right_door.cutpart("Slab_Door")
        right_door.edgebanding('Door_Edges',l1 = True, w1 = True, l2 = True, w2 = True)
        right_door.prompt('Hinge Quantity','MV_CALCULATE_HINGE_QTY(Height)',[Height])
        
        right_pull = LM_pulls.Standard_Pull()
        right_pull.door_type = self.door_type
        right_pull.door_swing = "Left Swing"
        right_pull.draw()
        right_pull.set_name("Right Pull")
        right_pull.obj_bp.parent = self.obj_bp
        self.set_pull_drivers(right_pull)
        right_pull.x_loc('Width-Frame_Right_Gap+IF(Inset_Front,-Inset_Reveal,Right_Overlay)',[Width,Frame_Right_Gap,Right_Overlay,Inset_Front,Inset_Reveal])
        right_pull.z_rot('radians(90)+Door_Rotation',[Door_Rotation])
        if self.door_swing == "Double Door":
            right_pull.y_dim('((Width-(Frame_Left_Gap+Frame_Right_Gap)-Mid_Rail_Width)/2)+IF(Inset_Front,-(Inset_Reveal*2),(Left_Overlay+Right_Overlay))',
                             [Width,Frame_Left_Gap,Frame_Right_Gap,Left_Overlay,Right_Overlay,Mid_Rail_Width,Inset_Front,Inset_Reveal])
            right_pull.prompt('Hide','IF(No_Pulls,True,False)',[No_Pulls])
        else:
            right_pull.y_dim('Width-(Frame_Left_Gap+Frame_Right_Gap)+IF(Inset_Front,-(Inset_Reveal*2),(Left_Overlay+Right_Overlay))',
                             [Width,Frame_Left_Gap,Frame_Right_Gap,Inset_Front,Inset_Reveal,Left_Overlay,Right_Overlay])
            right_pull.prompt('Hide','IF(Left_Swing,True,IF(No_Pulls,True,False))',[Left_Swing,No_Pulls])
        
        if self.door_swing == "Double Door":
            frame_opening = self.add_assembly(MID_RAIL)  
            frame_opening.set_name("Frame Opening")
            frame_opening.x_loc('Frame_Left_Gap+((Width-(Frame_Left_Gap+Frame_Right_Gap))/2)-(Mid_Rail_Width/2)',[Frame_Left_Gap,Width,Frame_Right_Gap,Mid_Rail_Width])
            frame_opening.y_loc(value = 0)
            frame_opening.z_loc('Frame_Bottom_Gap',[Frame_Bottom_Gap])
            frame_opening.x_rot(value = 0)
            frame_opening.y_rot(value = -90)
            frame_opening.z_rot(value = -90)
            frame_opening.x_dim('Height-(Frame_Top_Gap+Frame_Bottom_Gap)',[Height,Frame_Top_Gap,Frame_Bottom_Gap])
            frame_opening.y_dim('Mid_Rail_Width',[Mid_Rail_Width])
            frame_opening.z_dim(value = fd.inches(-.75))
            frame_opening.cutpart("Slab_Door")
            frame_opening.edgebanding('Door_Edges',l1 = True, w1 = True, l2 = True, w2 = True)
        
        self.update()

class FF_Pie_Cut_Doors(fd.Library_Assembly):
    
    library_name = "Cabinet Exteriors"
    type_assembly = 'INSERT'
    placement_type = "EXTERIOR"
    property_id = "exteriors.door_prompts"
    door_type = "" # {Base, Tall, Upper}
    door_swing = "" # {Left Swing, Right Swing, Double Door, Flip up}    
    
    def add_doors_prompts(self):
#         g = bpy.context.scene.lm_exteriors
        
        self.add_tab(name='Door Options',tab_type='VISIBLE')
        self.add_tab(name='Formulas',tab_type='HIDDEN')
        
        add_common_door_prompts(self)
        
        #CALCULATED
        self.add_prompt(name="Top Overlay",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        self.add_prompt(name="Bottom Overlay",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        self.add_prompt(name="Left Overlay",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        self.add_prompt(name="Right Overlay",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        self.add_prompt(name="Right Side Depth",prompt_type="DISTANCE",value=fd.inches(23),tab_index=0)
        self.add_prompt(name="Left Side Depth",prompt_type="DISTANCE",value=fd.inches(23),tab_index=0)
        
        #INHERITED
        self.add_prompt(name="Frame Thickness",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Frame Left Gap",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Frame Right Gap",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Frame Top Gap",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Frame Bottom Gap",prompt_type='DISTANCE',value=0,tab_index=1)        
        self.add_prompt(name="Hinge Quantity",prompt_type='QUANTITY',value=0,tab_index=1)
        
        height = self.get_var("dim_z",'height')
        
        if self.door_swing == 'Double Door':
            self.prompt('Hinge Quantity','MV_CALCULATE_HINGE_QTY(height)*2',[height])
        else:
            self.prompt('Hinge Quantity','MV_CALCULATE_HINGE_QTY(height)',[height])
        
    def set_shared_drivers(self,assembly,left_side=True):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Left_Side_Depth = self.get_var("Left Side Depth")
        Right_Side_Depth = self.get_var("Right Side Depth")
        Inset_Front = self.get_var("Inset Front")
        Inset_Reveal = self.get_var("Inset Reveal")
        Door_Thickness = self.get_var("Door Thickness")
        Door_to_Cabinet_Gap = self.get_var("Door to Cabinet Gap")
        Left_Overlay = self.get_var("Left Overlay")
        Right_Overlay = self.get_var("Right Overlay")
        Top_Overlay = self.get_var("Top Overlay")
        Bottom_Overlay = self.get_var("Bottom Overlay")        
        Frame_Left_Gap = self.get_var("Frame Left Gap")
        Frame_Right_Gap = self.get_var("Frame Right Gap")
        Frame_Top_Gap = self.get_var("Frame Top Gap")
        Frame_Bottom_Gap = self.get_var("Frame Bottom Gap")
        
        if left_side == True:
            assembly.x_loc("Left_Side_Depth+IF(Inset_Front,-Door_Thickness,Door_to_Cabinet_Gap)",
                           [Left_Side_Depth,Door_to_Cabinet_Gap,Inset_Front,Door_Thickness])     
            assembly.y_loc("Depth+Frame_Left_Gap-IF(Inset_Front,-Inset_Reveal,Left_Overlay)",
                           [Depth,Left_Overlay,Inset_Front,Inset_Reveal,Frame_Left_Gap])         
            assembly.z_loc("Frame_Bottom_Gap+IF(Inset_Front,Inset_Reveal,-Bottom_Overlay)",
                           [Inset_Front,Bottom_Overlay,Inset_Reveal,Frame_Bottom_Gap])   
            
            assembly.y_rot(value=-90)
            assembly.z_rot(value=180)    
            
            assembly.x_dim("Height-Frame_Bottom_Gap-Frame_Top_Gap+IF(Inset_Front,-Inset_Reveal*2,Bottom_Overlay+Top_Overlay)",
                           [Height,Inset_Front,Bottom_Overlay,Top_Overlay,Inset_Reveal,Frame_Bottom_Gap,Frame_Top_Gap])  
        
        else:
            assembly.x_loc("Left_Side_Depth+IF(Inset_Front,0,Door_Thickness+Door_to_Cabinet_Gap)",
                           [Left_Side_Depth,Door_Thickness,Door_to_Cabinet_Gap,Inset_Front])
            assembly.y_loc("-Right_Side_Depth-IF(Inset_Front,-Door_Thickness,Door_to_Cabinet_Gap)",
                           [Right_Side_Depth,Door_to_Cabinet_Gap,Door_Thickness,Inset_Front])        
            assembly.z_loc("Frame_Bottom_Gap+IF(Inset_Front,Inset_Reveal,-Bottom_Overlay)",
                           [Inset_Front,Bottom_Overlay,Inset_Reveal,Frame_Bottom_Gap])        
        
            assembly.y_rot(value=-90)
            assembly.z_rot(value=90)     
            
            assembly.x_dim("Height-Frame_Bottom_Gap-Frame_Top_Gap+IF(Inset_Front,-Inset_Reveal*2,Bottom_Overlay+Top_Overlay)",
                           [Height,Inset_Front,Bottom_Overlay,Top_Overlay,Inset_Reveal,Frame_Bottom_Gap,Frame_Top_Gap])
            assembly.y_dim("(-Width+Left_Side_Depth+Frame_Right_Gap)+IF(Inset_Front,Inset_Reveal,+Door_Thickness+Door_to_Cabinet_Gap-Right_Overlay)",
                           [Width,Left_Side_Depth,Door_Thickness,Right_Overlay,Inset_Front,Door_to_Cabinet_Gap,Inset_Reveal,Frame_Right_Gap])             
                   
    def set_pull_drivers(self,assembly): 
        Height = self.get_var('dim_z','Height')
        Pull_Length = assembly.get_var("Pull Length")
        Pull_From_Edge = self.get_var("Pull From Edge")
        Base_Pull_Location = self.get_var("Base Pull Location")
        Tall_Pull_Location = self.get_var("Tall Pull Location")
        Upper_Pull_Location = self.get_var("Upper Pull Location")
        
        assembly.prompt("Pull X Location",'Pull_From_Edge',[Pull_From_Edge])
        
        if self.door_type == "Base":
            assembly.prompt("Pull Z Location",'Base_Pull_Location+(Pull_Length/2)',[Base_Pull_Location,Pull_Length])
        if self.door_type == "Tall":
            assembly.prompt("Pull Z Location",'Tall_Pull_Location+(Pull_Length/2)',[Tall_Pull_Location,Pull_Length])
        if self.door_type == "Upper":
            assembly.prompt("Pull Z Location",'Height-Upper_Pull_Location-(Pull_Length/2)',[Height,Upper_Pull_Location,Pull_Length])
    
    def draw(self):
        g = bpy.context.scene.lm_exteriors
        self.create_assembly()
        
        self.add_doors_prompts()
        
        Depth = self.get_var('dim_y','Depth')
        Left_Overlay = self.get_var("Left Overlay")
        Left_Swing = self.get_var("Left Swing")
        No_Pulls = self.get_var("No Pulls")
        Door_to_Cabinet_Gap = self.get_var("Door to Cabinet Gap")
        Door_Thickness = self.get_var("Door Thickness")
        Inset_Front = self.get_var("Inset Front")
        Right_Side_Depth = self.get_var("Right Side Depth")
        Frame_Left_Gap = self.get_var("Frame Left Gap")
        
        if self.door_type == 'Base':
            door_style_name = g.Base_Door_Style
        if self.door_type == 'Tall':
            door_style_name = g.Tall_Door_Style
        if self.door_type == 'Upper':
            door_style_name = g.Upper_Door_Style
        
        door_style = (HIDDEN_FOLDER_NAME,DOOR_LIBRARY_NAME,DOOR_CATEGORY_NAME,door_style_name)
        
        #LEFT DOOR
        left_door = self.add_assembly(door_style)  
        left_door.set_name(self.door_type + " Left Cabinet Door")
        left_door.cutpart("Slab_Door")
        left_door.edgebanding('Door_Edges',l1 = True, w1 = True, l2 = True, w2 = True)
        self.set_shared_drivers(left_door,True)
        left_door.y_dim("(Depth+Right_Side_Depth+Door_Thickness+Door_to_Cabinet_Gap+Frame_Left_Gap)-IF(Inset_Front,Door_Thickness,Left_Overlay)",
                        [Depth,Right_Side_Depth,Door_Thickness,Inset_Front,Left_Overlay,Door_to_Cabinet_Gap,Frame_Left_Gap])
        
        #LEFT PULL
        left_pull = LM_pulls.Standard_Pull()
        left_pull.door_type = self.door_type
        left_pull.draw()
        left_pull.set_name("Left Cabinet Pull")
        left_pull.obj_bp.parent = self.obj_bp
        self.set_pull_drivers(left_pull)
        self.set_shared_drivers(left_pull,True)
        left_pull.z_dim("Door_Thickness",[Door_Thickness])  
        left_pull.prompt("Hide","IF(No_Pulls,True,IF(Left_Swing,True,False))",[No_Pulls,Left_Swing])

        #RIGHT DOOR
        right_door = self.add_assembly(door_style)  
        right_door.set_name(self.door_type + " Right Cabinet Door")
        right_door.cutpart("Slab_Door")
        right_door.edgebanding('Door_Edges',l1 = True, w1 = True, l2 = True, w2 = True)
        self.set_shared_drivers(right_door,False)
        
        #RIGHT PULL
        right_pull = LM_pulls.Standard_Pull()
        right_pull.door_type = self.door_type
        right_pull.draw()
        right_pull.set_name("Right Cabinet Pull")
        right_pull.obj_bp.parent = self.obj_bp
        self.set_pull_drivers(right_pull) 
        self.set_shared_drivers(right_pull,False)
        right_pull.z_dim("Door_Thickness",[Door_Thickness])
        right_pull.prompt("Hide","IF(No_Pulls,True,IF(Left_Swing,False,True))",[No_Pulls,Left_Swing])   
           
        self.update()    
        
class FF_Drawers(fd.Library_Assembly):
    library_name = "Cabinet Exteriors"
    type_assembly = 'INSERT'
    placement_type = "EXTERIOR"
    property_id = "exteriors.door_prompts"
    
    add_drawer = True
    add_pull = True
    door_type = "" # {Base, Tall, Upper}
    door_swing = "" # {Left Swing, Right Swing, Double Door, Flip up}

    #TODO: Finish Face Frame Drawer Stack

    def add_drawer_prompts(self):
        g = bpy.context.scene.lm_exteriors
        
        self.add_tab(name='Drawer Options',tab_type='VISIBLE')
        self.add_tab(name='Formulas',tab_type='HIDDEN')
        
        add_common_drawer_prompts(self)
        
        self.add_prompt(name="Mid Rail Width",prompt_type='DISTANCE',value=fd.inches(2),tab_index=0)
        self.add_prompt(name="Top Overlay",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        self.add_prompt(name="Bottom Overlay",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        self.add_prompt(name="Left Overlay",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        self.add_prompt(name="Right Overlay",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        
        #INHERITED
        self.add_prompt(name="Frame Thickness",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Frame Left Gap",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Frame Right Gap",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Frame Top Gap",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Frame Bottom Gap",prompt_type='DISTANCE',value=0,tab_index=1)
        
        #CALCULATIONS
        Frame_Left_Gap = self.get_var("Frame Left Gap")
        Frame_Right_Gap = self.get_var("Frame Right Gap")
        Inset_Front = self.get_var("Inset Front")
        Inset_Reveal = self.get_var("Inset Reveal")
        Left_Overlay = self.get_var("Left Overlay")
        Right_Overlay = self.get_var("Right Overlay")

        self.add_prompt(name="Left Drawer Front Extension",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Right Drawer Front Extension",prompt_type='DISTANCE',value=0,tab_index=1)
        self.prompt('Left Drawer Front Extension','-Frame_Left_Gap+IF(Inset_Front,Inset_Reveal,Left_Overlay)',[Frame_Left_Gap,Inset_Front,Inset_Reveal,Left_Overlay])
        self.prompt('Right Drawer Front Extension','-Frame_Right_Gap+IF(Inset_Front,Inset_Reveal,Right_Overlay)',[Frame_Right_Gap,Inset_Front,Inset_Reveal,Right_Overlay])
        
    def get_assemblies(self,name):
        """ Add a Drawer Front, Drawer Box, and Pull
            To this insert
            RETURNS: drawer front, drawer box, pull
        """
        g = bpy.context.scene.lm_exteriors
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z',"Height")
        Depth = self.get_var('dim_y',"Depth")
        Inset_Front = self.get_var("Inset Front")
        Inset_Reveal = self.get_var("Inset Reveal")
        Left_Overlay = self.get_var("Left Overlay")
        Right_Overlay = self.get_var("Right Overlay")
        Top_Overlay = self.get_var("Top Overlay")
        Bottom_Overlay = self.get_var("Bottom Overlay")
        Drawer_Box_Slide_Gap = self.get_var("Drawer Box Slide Gap")
        Door_to_Cabinet_Gap = self.get_var("Door to Cabinet Gap")
        Front_Thickness = self.get_var("Front Thickness")
        Drawer_Box_Rear_Gap = self.get_var("Drawer Box Rear Gap")
        Drawer_Box_Top_Gap = self.get_var("Drawer Box Top Gap")
        Drawer_Box_Bottom_Gap = self.get_var("Drawer Box Bottom Gap")
        Center_Pulls_on_Drawers = self.get_var("Center Pulls on Drawers")
        Drawer_Pull_From_Top = self.get_var("Drawer Pull From Top")
        No_Pulls = self.get_var("No Pulls")
        Frame_Top_Gap = self.get_var("Frame Top Gap")
        Frame_Bottom_Gap = self.get_var("Frame Bottom Gap")
        Frame_Left_Gap = self.get_var("Frame Left Gap")
        Frame_Right_Gap = self.get_var("Frame Right Gap")
        Frame_Thickness = self.get_var("Frame Thickness")
        Left_Drawer_Front_Extension = self.get_var("Left Drawer Front Extension")
        Right_Drawer_Front_Extension = self.get_var("Right Drawer Front Extension")
        
        door_style = (HIDDEN_FOLDER_NAME,DOOR_LIBRARY_NAME,DOOR_CATEGORY_NAME,g.Drawer_Front_Style)
        
        front = self.add_assembly(door_style)
        front.set_name(name + " Drawer Front")
        front.x_loc('-Left_Drawer_Front_Extension',[Left_Drawer_Front_Extension])
        front.y_loc('IF(Inset_Front,0,-Door_to_Cabinet_Gap-Frame_Thickness)',[Inset_Front,Door_to_Cabinet_Gap,Front_Thickness,Frame_Thickness])
        front.z_loc('Frame_Bottom_Gap+IF(Inset_Front,Inset_Reveal,-Bottom_Overlay)',[Frame_Bottom_Gap,Inset_Front,Inset_Reveal,Bottom_Overlay])
        front.x_rot(value = 90)
        front.y_rot(value = 0)
        front.z_rot(value = 0)
        front.x_dim('Width+Left_Drawer_Front_Extension+Right_Drawer_Front_Extension',[Width,Left_Drawer_Front_Extension,Right_Drawer_Front_Extension])
        front.y_dim('Height-Frame_Top_Gap-Frame_Bottom_Gap+IF(Inset_Front,-(Inset_Reveal*2),Top_Overlay+Bottom_Overlay)',
                    [Height,Frame_Top_Gap,Frame_Bottom_Gap,Inset_Front,Inset_Reveal,Top_Overlay,Bottom_Overlay])
        front.z_dim('Front_Thickness',[Front_Thickness])
        front.cutpart("Slab_Drawer_Front")
        front.edgebanding('Door_Edges',l1 = True, w1 = True, l2 = True, w2 = True)
        
        drawer = None
        pull = None
        
        if self.add_pull:
            pull = LM_pulls.Standard_Pull()
            pull.door_type = self.door_type
            pull.draw()
            pull.obj_bp.parent = self.obj_bp
            pull.x_loc('-Left_Drawer_Front_Extension',[Left_Drawer_Front_Extension])
            pull.y_loc('IF(Inset_Front,0,-Door_to_Cabinet_Gap-Frame_Thickness)',[Inset_Front,Door_to_Cabinet_Gap,Front_Thickness,Frame_Thickness])
            pull.z_loc('Frame_Bottom_Gap+IF(Inset_Front,Inset_Reveal,-Bottom_Overlay)',[Frame_Bottom_Gap,Inset_Front,Inset_Reveal,Bottom_Overlay])
            pull.x_rot(value = 90)
            pull.y_rot(value = 0)
            pull.z_rot(value = 0)
            pull.x_dim('Width+Left_Drawer_Front_Extension+Right_Drawer_Front_Extension',[Width,Left_Drawer_Front_Extension,Right_Drawer_Front_Extension])
            pull.y_dim('Height-Frame_Top_Gap-Frame_Bottom_Gap+IF(Inset_Front,-(Inset_Reveal*2),Top_Overlay+Bottom_Overlay)',
                       [Height,Frame_Top_Gap,Frame_Bottom_Gap,Inset_Front,Inset_Reveal,Top_Overlay,Bottom_Overlay])
            pull.z_dim('Front_Thickness',[Front_Thickness])
            pull.prompt("Pull X Location",'IF(Center_Pulls_on_Drawers,Height/2,Drawer_Pull_From_Top)',[Center_Pulls_on_Drawers,Height,Drawer_Pull_From_Top])
            pull.prompt("Pull Z Location",'((Width+Left_Drawer_Front_Extension+Right_Drawer_Front_Extension)/2)',[Width,Left_Drawer_Front_Extension,Right_Drawer_Front_Extension])
            pull.prompt("Hide",'IF(No_Pulls,True,False)',[No_Pulls])
        
        if self.add_drawer:
            drawer = self.add_assembly(DRAWER_BOX)  #TODO: Add More Drawer Systems Dovetail, Metabox...
            drawer.set_name(name + " Drawer Box")
            drawer.x_loc('Frame_Left_Gap+Drawer_Box_Slide_Gap',[Frame_Left_Gap,Drawer_Box_Slide_Gap])
            drawer.y_loc('-Door_to_Cabinet_Gap',[Door_to_Cabinet_Gap]) #TODO: Add Open Drawer Prompt
            drawer.z_loc('Drawer_Box_Bottom_Gap',[Drawer_Box_Bottom_Gap])
            drawer.x_rot(value = 0)
            drawer.y_rot(value = 0)
            drawer.z_rot(value = 0)
            drawer.x_dim('Width-Frame_Left_Gap-Frame_Right_Gap-(Drawer_Box_Slide_Gap*2)',[Width,Frame_Left_Gap,Frame_Right_Gap,Drawer_Box_Slide_Gap])
            drawer.y_dim('Depth-Drawer_Box_Rear_Gap',[Depth,Drawer_Box_Rear_Gap])
            drawer.z_dim('Height-Drawer_Box_Top_Gap-Drawer_Box_Bottom_Gap',[Height,Drawer_Box_Top_Gap,Drawer_Box_Bottom_Gap])

        return front, drawer, pull

    def draw(self):
        self.create_assembly()
        
        self.add_drawer_prompts()
        
        self.get_assemblies("Single")
        
        self.update()
        
class FF_Drawer(fd.Library_Assembly):
    
    library_name = "Cabinet Exteriors"
    property_id = "exteriors.drawer_prompts"
    type_assembly = 'INSERT'
    placement_type = "EXTERIOR"
    
    door_type = "Drawer"
    direction = 'Vertical'
    add_drawer = True
    add_pull = True
    drawer_qty = 1
    top_drawer_front_height = 0

    def add_drawer_prompts(self):
        g = bpy.context.scene.lm_exteriors
        
        self.add_tab(name='Drawer Options',tab_type='VISIBLE')
        self.add_tab(name='Formulas',tab_type='HIDDEN')
        
        add_common_drawer_prompts(self)
        
        self.add_prompt(name="Mid Rail Width",prompt_type='DISTANCE',value=fd.inches(2),tab_index=0)
        self.add_prompt(name="Top Overlay",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        self.add_prompt(name="Bottom Overlay",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        self.add_prompt(name="Left Overlay",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        self.add_prompt(name="Right Overlay",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        self.add_prompt(name="Drawer Slide Quantity",prompt_type='QUANTITY',value=1,tab_index=1)
        
        #INHERITED
        self.add_prompt(name="Frame Thickness",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Frame Left Gap",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Frame Right Gap",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Frame Top Gap",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Frame Bottom Gap",prompt_type='DISTANCE',value=0,tab_index=1)

    def draw(self):
        g = bpy.context.scene.lm_exteriors
        
        self.create_assembly()
        self.add_drawer_prompts()
        
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z',"Height")
        Depth = self.get_var('dim_y',"Depth")
        Frame_Top_Gap = self.get_var('Frame Top Gap')
        Frame_Bottom_Gap = self.get_var('Frame Bottom Gap')
        Frame_Thickness = self.get_var('Frame Thickness')
        Drawer_Box_Rear_Gap = self.get_var("Drawer Box Rear Gap")
        Drawer_Box_Top_Gap = self.get_var("Drawer Box Top Gap")
        Drawer_Box_Bottom_Gap = self.get_var("Drawer Box Bottom Gap")
        Drawer_Box_Slide_Gap = self.get_var("Drawer Box Slide Gap")
        Door_to_Cabinet_Gap = self.get_var("Door to Cabinet Gap")
        Top_Overlay = self.get_var("Top Overlay")
        Bottom_Overlay = self.get_var("Bottom Overlay")
        Front_Thickness = self.get_var("Front Thickness")
        Center_Pulls_on_Drawers = self.get_var("Center Pulls on Drawers")
        Drawer_Pull_From_Top = self.get_var("Drawer Pull From Top")
        No_Pulls = self.get_var("No Pulls")
        Frame_Left_Gap = self.get_var("Frame Left Gap")
        Frame_Right_Gap = self.get_var("Frame Right Gap")
        Inset_Front = self.get_var("Inset Front")
        Inset_Reveal = self.get_var("Inset Reveal")
        Left_Overlay = self.get_var("Left Overlay")
        Right_Overlay = self.get_var("Right Overlay")
        Open = self.get_var("Open")
        
        if self.add_drawer:
            drawer = self.add_assembly(DRAWER_BOX)  #TODO: Add More Drawer Systems Dovetail, Metabox...
            drawer.set_name("Left Drawer Box")
            drawer.x_loc('Frame_Left_Gap+Drawer_Box_Slide_Gap',[Frame_Left_Gap,Drawer_Box_Slide_Gap])
            drawer.y_loc('IF(Inset_Front,0,-Door_to_Cabinet_Gap-Frame_Thickness)-(Depth*Open)',[Inset_Front,Front_Thickness,Door_to_Cabinet_Gap,Depth,Open,Frame_Thickness]) 
            drawer.z_loc('Drawer_Box_Bottom_Gap',[Drawer_Box_Bottom_Gap])
            drawer.x_rot(value = 0)
            drawer.y_rot(value = 0)
            drawer.z_rot(value = 0)
            drawer.x_dim('Width-Frame_Left_Gap-Frame_Right_Gap-(Drawer_Box_Slide_Gap)*2',[Width,Frame_Left_Gap,Frame_Right_Gap,Drawer_Box_Slide_Gap])
            drawer.y_dim('IF(Inset_Front,Depth-Drawer_Box_Rear_Gap,Depth+Frame_Thickness+Door_to_Cabinet_Gap-Drawer_Box_Rear_Gap)',[Inset_Front,Frame_Thickness,Door_to_Cabinet_Gap,Depth,Drawer_Box_Rear_Gap])
            drawer.z_dim('Height-Drawer_Box_Top_Gap-Drawer_Box_Bottom_Gap-Frame_Top_Gap',[Height,Drawer_Box_Top_Gap,Drawer_Box_Bottom_Gap,Frame_Top_Gap])
        
        front_style = (HIDDEN_FOLDER_NAME,DOOR_LIBRARY_NAME,DOOR_CATEGORY_NAME,g.Drawer_Front_Style)
        
        front = self.add_assembly(front_style)
        front.set_name("Left Drawer Front")
        front.x_loc('Frame_Left_Gap+IF(Inset_Front,Inset_Reveal,-Left_Overlay)',[Frame_Left_Gap,Inset_Front,Inset_Reveal,Left_Overlay])
        front.y_loc('IF(Inset_Front,0,-Door_to_Cabinet_Gap-Frame_Thickness)-(Depth*Open)',[Inset_Front,Door_to_Cabinet_Gap,Depth,Open,Frame_Thickness])
        front.z_loc('IF(Inset_Front,Inset_Reveal,-Bottom_Overlay)',[Inset_Front,Inset_Reveal,Bottom_Overlay])
        front.x_rot(value = 90)
        front.y_rot(value = 0)
        front.z_rot(value = 0)
        front.x_dim('Width-Frame_Left_Gap-Frame_Right_Gap+IF(Inset_Front,-(Inset_Reveal)*2,Right_Overlay+Left_Overlay)',[Width,Inset_Front,Inset_Reveal,Frame_Left_Gap,Frame_Right_Gap,Right_Overlay,Left_Overlay,Inset_Reveal,Inset_Front])
        front.y_dim('Height-(Frame_Top_Gap+Frame_Bottom_Gap)+IF(Inset_Front,-(Inset_Reveal)*2,Top_Overlay+Bottom_Overlay)',[Height,Inset_Front,Inset_Reveal,Top_Overlay,Bottom_Overlay,Frame_Top_Gap,Frame_Bottom_Gap])
        front.z_dim('Front_Thickness',[Front_Thickness])
        front.cutpart("Slab_Drawer_Front")
        front.edgebanding('Door_Edges',l1 = True, w1 = True, l2 = True, w2 = True)

        Front_Width = front.get_var('dim_x',"Front_Width")

        if self.add_pull:
            pull = LM_pulls.Standard_Pull()
            pull.door_type = self.door_type
            pull.draw()
            pull.obj_bp.parent = self.obj_bp
            pull.set_name("Left Cabinet Pull")
            pull.x_loc('Frame_Left_Gap+IF(Inset_Front,Inset_Reveal,-Left_Overlay)',[Frame_Left_Gap,Inset_Front,Inset_Reveal,Left_Overlay])
            pull.y_loc('IF(Inset_Front,0,-Door_to_Cabinet_Gap-Frame_Thickness)-(Depth*Open)',[Inset_Front,Door_to_Cabinet_Gap,Depth,Open,Frame_Thickness])
            pull.z_loc('IF(Inset_Front,Inset_Reveal,-Bottom_Overlay)',[Inset_Front,Inset_Reveal,Bottom_Overlay])
            pull.x_rot(value = 90)
            pull.y_rot(value = 0)
            pull.z_rot(value = 0)
            pull.x_dim('Width-Frame_Left_Gap-Frame_Right_Gap+IF(Inset_Front,-(Inset_Reveal)*2,Right_Overlay+Left_Overlay)',[Width,Inset_Front,Inset_Reveal,Frame_Left_Gap,Frame_Right_Gap,Right_Overlay,Left_Overlay,Inset_Reveal,Inset_Front])
            pull.y_dim('Height-(Frame_Top_Gap+Frame_Bottom_Gap)+IF(Inset_Front,-(Inset_Reveal)*2,Top_Overlay+Bottom_Overlay)',[Height,Inset_Front,Inset_Reveal,Top_Overlay,Bottom_Overlay,Frame_Top_Gap,Frame_Bottom_Gap])
            pull.z_dim('Front_Thickness',[Front_Thickness])
            pull.prompt("Pull X Location",'IF(Center_Pulls_on_Drawers,Height/2,Drawer_Pull_From_Top)',[Center_Pulls_on_Drawers,Height,Drawer_Pull_From_Top])
            pull.prompt("Pull Z Location",'Front_Width/2',[Front_Width])
            pull.prompt("Hide",'IF(No_Pulls,True,False)',[No_Pulls])

        self.update()
        
class FF_Horizontal_Drawers(fd.Library_Assembly):
    
    library_name = "Cabinet Exteriors"
    property_id = "exteriors.drawer_prompts"
    type_assembly = 'INSERT'
    placement_type = "EXTERIOR"
    
    door_type = "Drawer"
    direction = 'Vertical'
    add_drawer = True
    add_pull = True
    drawer_qty = 1
    top_drawer_front_height = 0

    def add_drawer_prompts(self):
        g = bpy.context.scene.lm_exteriors
        
        self.add_tab(name='Drawer Options',tab_type='VISIBLE')
        self.add_tab(name='Formulas',tab_type='HIDDEN')
        
        add_common_drawer_prompts(self)
        
        self.add_prompt(name="Mid Rail Width",prompt_type='DISTANCE',value=fd.inches(2),tab_index=0)
        self.add_prompt(name="Top Overlay",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        self.add_prompt(name="Bottom Overlay",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        self.add_prompt(name="Left Overlay",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        self.add_prompt(name="Right Overlay",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        
        #INHERITED
        self.add_prompt(name="Frame Thickness",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Frame Left Gap",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Frame Right Gap",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Frame Top Gap",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Frame Bottom Gap",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Drawer Slide Quantity",prompt_type='QUANTITY',value=2,tab_index=1)
        
    def draw(self):
        g = bpy.context.scene.lm_exteriors
        
        self.create_assembly()
        self.add_drawer_prompts()
        
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z',"Height")
        Depth = self.get_var('dim_y',"Depth")
        Mid_Rail_Width = self.get_var('Mid Rail Width')
        Frame_Top_Gap = self.get_var('Frame Top Gap')
        Frame_Bottom_Gap = self.get_var('Frame Bottom Gap')
        Frame_Thickness = self.get_var('Frame Thickness')
        Drawer_Box_Rear_Gap = self.get_var("Drawer Box Rear Gap")
        Drawer_Box_Top_Gap = self.get_var("Drawer Box Top Gap")
        Drawer_Box_Bottom_Gap = self.get_var("Drawer Box Bottom Gap")
        Drawer_Box_Slide_Gap = self.get_var("Drawer Box Slide Gap")
        Door_to_Cabinet_Gap = self.get_var("Door to Cabinet Gap")
        Top_Overlay = self.get_var("Top Overlay")
        Bottom_Overlay = self.get_var("Bottom Overlay")
        Front_Thickness = self.get_var("Front Thickness")
        Center_Pulls_on_Drawers = self.get_var("Center Pulls on Drawers")
        Drawer_Pull_From_Top = self.get_var("Drawer Pull From Top")
        No_Pulls = self.get_var("No Pulls")
        Frame_Left_Gap = self.get_var("Frame Left Gap")
        Frame_Right_Gap = self.get_var("Frame Right Gap")
        Inset_Front = self.get_var("Inset Front")
        Inset_Reveal = self.get_var("Inset Reveal")
        Left_Overlay = self.get_var("Left Overlay")
        Right_Overlay = self.get_var("Right Overlay")
        Open = self.get_var("Open")
        
        mid_stile = self.add_assembly(MID_RAIL)
        mid_stile.set_name("Mid Rail")
        mid_stile.x_loc('Frame_Left_Gap+(Width-Mid_Rail_Width-Frame_Left_Gap-Frame_Right_Gap)/2',[Width,Mid_Rail_Width,Frame_Left_Gap,Frame_Right_Gap])
        mid_stile.y_loc('-Frame_Thickness',[Frame_Thickness])
        mid_stile.z_loc(value = 0)
        mid_stile.x_rot(value = 0)
        mid_stile.y_rot(value = -90)
        mid_stile.z_rot(value = 90)
        mid_stile.x_dim('Height-Frame_Top_Gap-Frame_Bottom_Gap',[Height,Frame_Top_Gap,Frame_Bottom_Gap])
        mid_stile.y_dim('-Mid_Rail_Width',[Mid_Rail_Width])
        mid_stile.z_dim('-Frame_Thickness',[Frame_Thickness])
        mid_stile.cutpart("Slab_Door")
        mid_stile.edgebanding('Door_Edges',l1 = True, w1 = True, l2 = True, w2 = True)
        
        Mid_Stile_X = mid_stile.get_var('loc_x','Mid_Stile_X')
        Mid_Stile_Width = mid_stile.get_var('dim_y','Mid_Stile_Width')
        
        if self.add_drawer:
            left_drawer = LM_drawer_boxes.Wood_Drawer_Box()  #TODO: Add More Drawer Systems Dovetail, Metabox...
            left_drawer.draw()
            left_drawer.obj_bp.parent = self.obj_bp
            left_drawer.set_name("Left Drawer Box")
            left_drawer.x_loc('Frame_Left_Gap+Drawer_Box_Slide_Gap',[Frame_Left_Gap,Drawer_Box_Slide_Gap])
            left_drawer.y_loc('IF(Inset_Front,0,-Door_to_Cabinet_Gap-Frame_Thickness)-(Depth*Open)',[Inset_Front,Front_Thickness,Door_to_Cabinet_Gap,Depth,Open,Frame_Thickness]) 
            left_drawer.z_loc('Drawer_Box_Bottom_Gap',[Drawer_Box_Bottom_Gap])
            left_drawer.x_rot(value = 0)
            left_drawer.y_rot(value = 0)
            left_drawer.z_rot(value = 0)
            left_drawer.x_dim('Mid_Stile_X-Frame_Left_Gap-(Drawer_Box_Slide_Gap)*2',[Mid_Stile_X,Frame_Left_Gap,Drawer_Box_Slide_Gap])
            left_drawer.y_dim('IF(Inset_Front,Depth-Drawer_Box_Rear_Gap,Depth+Frame_Thickness+Door_to_Cabinet_Gap-Drawer_Box_Rear_Gap)',[Inset_Front,Frame_Thickness,Door_to_Cabinet_Gap,Depth,Drawer_Box_Rear_Gap])
            left_drawer.z_dim('Height-Drawer_Box_Top_Gap-Drawer_Box_Bottom_Gap-Frame_Top_Gap',[Height,Drawer_Box_Top_Gap,Drawer_Box_Bottom_Gap,Frame_Top_Gap])
            
            right_drawer = LM_drawer_boxes.Wood_Drawer_Box()  #TODO: Add More Drawer Systems Dovetail, Metabox...
            right_drawer.draw()
            right_drawer.obj_bp.parent = self.obj_bp
            right_drawer.set_name("Right Drawer Box")
            right_drawer.x_loc('Mid_Stile_X+fabs(Mid_Stile_Width)+Drawer_Box_Slide_Gap',[Mid_Stile_X,Mid_Stile_Width,Drawer_Box_Slide_Gap])
            right_drawer.y_loc('IF(Inset_Front,0,-Door_to_Cabinet_Gap-Frame_Thickness)-(Depth*Open)',[Inset_Front,Front_Thickness,Door_to_Cabinet_Gap,Depth,Open,Frame_Thickness])
            right_drawer.z_loc('Drawer_Box_Bottom_Gap',[Drawer_Box_Bottom_Gap])
            right_drawer.x_rot(value = 0)
            right_drawer.y_rot(value = 0)
            right_drawer.z_rot(value = 0)
            right_drawer.x_dim('Mid_Stile_X-Frame_Left_Gap-(Drawer_Box_Slide_Gap)*2',[Mid_Stile_X,Frame_Left_Gap,Drawer_Box_Slide_Gap])
            right_drawer.y_dim('IF(Inset_Front,Depth-Drawer_Box_Rear_Gap,Depth+Frame_Thickness+Door_to_Cabinet_Gap-Drawer_Box_Rear_Gap)',[Inset_Front,Frame_Thickness,Door_to_Cabinet_Gap,Depth,Drawer_Box_Rear_Gap])
            right_drawer.z_dim('Height-Drawer_Box_Top_Gap-Drawer_Box_Bottom_Gap-Frame_Top_Gap',[Height,Drawer_Box_Top_Gap,Drawer_Box_Bottom_Gap,Frame_Top_Gap])
        
        front_style = (HIDDEN_FOLDER_NAME,DOOR_LIBRARY_NAME,DOOR_CATEGORY_NAME,g.Drawer_Front_Style)
        
        left_front = self.add_assembly(front_style)
        left_front.set_name("Left Drawer Front")
        left_front.x_loc('Frame_Left_Gap+IF(Inset_Front,Inset_Reveal,-Left_Overlay)',[Frame_Left_Gap,Inset_Front,Inset_Reveal,Left_Overlay])
        left_front.y_loc('IF(Inset_Front,0,-Door_to_Cabinet_Gap-Frame_Thickness)-(Depth*Open)',[Inset_Front,Door_to_Cabinet_Gap,Depth,Open,Frame_Thickness])
        left_front.z_loc('IF(Inset_Front,Inset_Reveal,-Bottom_Overlay)',[Inset_Front,Inset_Reveal,Bottom_Overlay])
        left_front.x_rot(value = 90)
        left_front.y_rot(value = 0)
        left_front.z_rot(value = 0)
        left_front.x_dim('Mid_Stile_X-Frame_Left_Gap+IF(Inset_Front,-(Inset_Reveal)*2,Right_Overlay+Left_Overlay)',[Mid_Stile_X,Inset_Front,Inset_Reveal,Frame_Left_Gap,Right_Overlay,Left_Overlay,Inset_Reveal,Inset_Front])
        left_front.y_dim('Height-(Frame_Top_Gap+Frame_Bottom_Gap)+IF(Inset_Front,-(Inset_Reveal)*2,Top_Overlay+Bottom_Overlay)',[Height,Inset_Front,Inset_Reveal,Top_Overlay,Bottom_Overlay,Frame_Top_Gap,Frame_Bottom_Gap])
        left_front.z_dim('Front_Thickness',[Front_Thickness])
        left_front.cutpart("Slab_Drawer_Front")
        left_front.edgebanding('Door_Edges',l1 = True, w1 = True, l2 = True, w2 = True)
        
        right_front = self.add_assembly(front_style)
        right_front.set_name("Left Drawer Front")
        right_front.x_loc('Mid_Stile_X+fabs(Mid_Stile_Width)+IF(Inset_Front,Inset_Reveal,-Left_Overlay)',[Mid_Stile_X,Inset_Front,Inset_Reveal,Mid_Stile_Width,Left_Overlay])
        right_front.y_loc('IF(Inset_Front,0,-Door_to_Cabinet_Gap-Frame_Thickness)-(Depth*Open)',[Inset_Front,Door_to_Cabinet_Gap,Depth,Open,Frame_Thickness])
        right_front.z_loc('IF(Inset_Front,Inset_Reveal,-Bottom_Overlay)',[Inset_Front,Inset_Reveal,Bottom_Overlay])
        right_front.x_rot(value = 90)
        right_front.y_rot(value = 0)
        right_front.z_rot(value = 0)
        right_front.x_dim('Mid_Stile_X-Frame_Left_Gap+IF(Inset_Front,-(Inset_Reveal)*2,Right_Overlay+Left_Overlay)',[Mid_Stile_X,Inset_Front,Inset_Reveal,Frame_Left_Gap,Right_Overlay,Left_Overlay,Inset_Reveal,Inset_Front])
        right_front.y_dim('Height-(Frame_Top_Gap+Frame_Bottom_Gap)+IF(Inset_Front,-(Inset_Reveal)*2,Top_Overlay+Bottom_Overlay)',[Height,Inset_Front,Inset_Reveal,Top_Overlay,Bottom_Overlay,Frame_Top_Gap,Frame_Bottom_Gap])
        right_front.z_dim('Front_Thickness',[Front_Thickness])
        right_front.cutpart("Slab_Drawer_Front")
        right_front.edgebanding('Door_Edges',l1 = True, w1 = True, l2 = True, w2 = True)
        
        Left_Front_Width = left_front.get_var('dim_x',"Left_Front_Width")
        Right_Front_Width = right_front.get_var('dim_x',"Right_Front_Width")
        
        if self.add_pull:
            left_pull = LM_pulls.Standard_Pull()
            left_pull.door_type = self.door_type
            left_pull.draw()
            left_pull.obj_bp.parent = self.obj_bp
            left_pull.set_name("Left Cabinet Pull")
            left_pull.x_loc('Frame_Left_Gap+IF(Inset_Front,Inset_Reveal,-Left_Overlay)',[Frame_Left_Gap,Inset_Front,Inset_Reveal,Left_Overlay])
            left_pull.y_loc('IF(Inset_Front,0,-Door_to_Cabinet_Gap-Frame_Thickness)-(Depth*Open)',[Inset_Front,Door_to_Cabinet_Gap,Depth,Open,Frame_Thickness])
            left_pull.z_loc('IF(Inset_Front,Inset_Reveal,-Bottom_Overlay)',[Inset_Front,Inset_Reveal,Bottom_Overlay])
            left_pull.x_rot(value = 90)
            left_pull.y_rot(value = 0)
            left_pull.z_rot(value = 0)
            left_pull.x_dim('Mid_Stile_X-Frame_Left_Gap+IF(Inset_Front,-(Inset_Reveal)*2,Right_Overlay+Left_Overlay)',[Mid_Stile_X,Inset_Front,Inset_Reveal,Frame_Left_Gap,Right_Overlay,Left_Overlay,Inset_Reveal,Inset_Front])
            left_pull.y_dim('Height-(Frame_Top_Gap+Frame_Bottom_Gap)+IF(Inset_Front,-(Inset_Reveal)*2,Top_Overlay+Bottom_Overlay)',[Height,Inset_Front,Inset_Reveal,Top_Overlay,Bottom_Overlay,Frame_Top_Gap,Frame_Bottom_Gap])
            left_pull.z_dim('Front_Thickness',[Front_Thickness])
            left_pull.prompt("Pull X Location",'IF(Center_Pulls_on_Drawers,Height/2,Drawer_Pull_From_Top)',[Center_Pulls_on_Drawers,Height,Drawer_Pull_From_Top])
            left_pull.prompt("Pull Z Location",'Left_Front_Width/2',[Left_Front_Width])
            left_pull.prompt("Hide",'IF(No_Pulls,True,False)',[No_Pulls])
    
            right_pull = LM_pulls.Standard_Pull()
            right_pull.door_type = self.door_type
            right_pull.draw()
            right_pull.obj_bp.parent = self.obj_bp
            right_pull.set_name("Right Cabinet Pull")
            right_pull.x_loc('Mid_Stile_X+fabs(Mid_Stile_Width)+IF(Inset_Front,Inset_Reveal,-Left_Overlay)',[Mid_Stile_X,Inset_Front,Inset_Reveal,Mid_Stile_Width,Left_Overlay])
            right_pull.y_loc('IF(Inset_Front,0,-Door_to_Cabinet_Gap-Frame_Thickness)-(Depth*Open)',[Inset_Front,Door_to_Cabinet_Gap,Depth,Open,Frame_Thickness])
            right_pull.z_loc('IF(Inset_Front,Inset_Reveal,-Bottom_Overlay)',[Inset_Front,Inset_Reveal,Bottom_Overlay])
            right_pull.x_rot(value = 90)
            right_pull.y_rot(value = 0)
            right_pull.z_rot(value = 0)
            right_pull.x_dim('Mid_Stile_X-Frame_Left_Gap+IF(Inset_Front,-(Inset_Reveal)*2,Right_Overlay+Left_Overlay)',[Mid_Stile_X,Inset_Front,Inset_Reveal,Frame_Left_Gap,Right_Overlay,Left_Overlay,Inset_Reveal,Inset_Front])
            right_pull.y_dim('Height-(Frame_Top_Gap+Frame_Bottom_Gap)+IF(Inset_Front,-(Inset_Reveal)*2,Top_Overlay+Bottom_Overlay)',[Height,Inset_Front,Inset_Reveal,Top_Overlay,Bottom_Overlay,Frame_Top_Gap,Frame_Bottom_Gap])
            right_pull.z_dim('Front_Thickness',[Front_Thickness])
            right_pull.prompt("Pull X Location",'IF(Center_Pulls_on_Drawers,Height/2,Drawer_Pull_From_Top)',[Center_Pulls_on_Drawers,Height,Drawer_Pull_From_Top])
            right_pull.prompt("Pull Z Location",'Right_Front_Width/2',[Right_Front_Width])
            right_pull.prompt("Hide",'IF(No_Pulls,True,False)',[No_Pulls])
        
        self.update()
        
class Fluted_Molding(fd.Library_Assembly):
    
    library_name = "Cabinet Exteriors"
    placement_type = "INTERIOR"
    property_id = ""
    type_assembly = "INSERT"
    mirror_y = False
    
    add_top_rosette = False
    add_bottom_rosette = False
    
    def draw(self):
        self.create_assembly()
        
        self.add_tab("Flute Panel Options", 'VISIBLE')
        self.add_prompt(name="Panel Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        
        Width = self.get_var('dim_x', "Width")
        Height = self.get_var('dim_z', "Height")
        Depth = self.get_var('dim_y', "Depth")
        Panel_Thickness = self.get_var("Panel Thickness")
        
        front_filler = self.add_assembly(PART_WITH_NO_EDGEBANDING)
        front_filler.set_name("Front Filler")
        front_filler.x_loc(value = 0)
        front_filler.y_loc(value = 0)
        front_filler.z_loc(value = 0)
        front_filler.x_rot(value = 0)
        front_filler.y_rot(value = -90)
        front_filler.z_rot(value = -90)
        front_filler.x_dim("Height",[Height])
        front_filler.y_dim("Width",[Width])
        front_filler.z_dim("Panel_Thickness",[Panel_Thickness])
        front_filler.cutpart("CBD_Shelf")
        
        rear_filler = self.add_assembly(PART_WITH_NO_EDGEBANDING)
        rear_filler.set_name("Rear Filler")
        rear_filler.x_loc(value = 0)
        rear_filler.y_loc('Depth',[Depth])
        rear_filler.z_loc(value = 0)
        rear_filler.x_rot(value = 0)
        rear_filler.y_rot(value = -90)
        rear_filler.z_rot(value = -90)
        rear_filler.x_dim("Height",[Height])
        rear_filler.y_dim("Width",[Width])
        rear_filler.z_dim("-Panel_Thickness",[Panel_Thickness])
        rear_filler.cutpart("CBD_Shelf")
        
        flute = self.add_assembly(FLUTED_PART)
        flute.set_name("Fluted Part")
        flute.x_loc(value = fd.inches(3.25))
        flute.y_loc(value = 0)
        if self.add_bottom_rosette:
            flute.z_loc(value = fd.inches(3.5))
        else:
            flute.z_loc(value = 0)
        flute.x_rot(value = 0)
        flute.y_rot(value = -90)
        flute.z_rot(value = 90)
        if self.add_bottom_rosette and self.add_top_rosette:
            flute.x_dim("Height-INCH(7)",[Height])
        elif self.add_bottom_rosette or self.add_top_rosette:
            flute.x_dim("Height-INCH(3.5)",[Height])
        else:
            flute.x_dim("Height",[Height])
        flute.y_dim("Width",[Width])
        flute.z_dim("Panel_Thickness",[Panel_Thickness])
        flute.material("CBD_Closet_Part_Surfaces")
        
        if self.add_top_rosette:
            top_rosette = self.add_object(ROSETTE)
            top_rosette.x_loc(value = fd.inches(-.25))
            top_rosette.z_loc('Height-INCH(3.5)',[Height])
            top_rosette.x_rot(value = 90)
        
        if self.add_bottom_rosette:
            bottom_rosette = self.add_object(ROSETTE)
            bottom_rosette.x_loc(value = fd.inches(-.25))
            bottom_rosette.x_rot(value = 90)

        self.update()
        
#---------INSERTS
        
class INSERT_Base_Single_Door(Doors):
    
    def __init__(self):
        self.category_name = "Frameless"
        self.assembly_name = "Base Single Door"
        self.door_type = "Base"
        self.door_swing = "Left Swing"
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)

class INSERT_Base_Single_Door_With_False_Front(Doors):
    
    def __init__(self):
        self.category_name = "Frameless"
        self.assembly_name = "Base Single Door with False Front"
        self.door_type = "Base"
        self.door_swing = "Left Swing"
        self.false_front_qty = 1
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)

class INSERT_Base_Double_Door(Doors):
    
    def __init__(self):
        self.category_name = "Frameless"
        self.assembly_name = "Base Double Door"
        self.door_type = "Base"
        self.door_swing = "Double Door"
        self.width = fd.inches(36)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
class INSERT_Base_Double_Door_With_False_Front(Doors):
    
    def __init__(self):
        self.category_name = "Frameless"
        self.assembly_name = "Base Double Door with False Front"
        self.door_type = "Base"
        self.door_swing = "Double Door"
        self.false_front_qty = 1
        self.width = fd.inches(36)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
class INSERT_Base_Double_Door_With_2_False_Front(Doors):
    
    def __init__(self):
        self.category_name = "Frameless"
        self.assembly_name = "Base Double Door with 2 False Front"
        self.door_type = "Base"
        self.door_swing = "Double Door"
        self.false_front_qty = 2
        self.width = fd.inches(36)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
class INSERT_Tall_Single_Door(Doors):
    
    def __init__(self):
        self.category_name = "Frameless"
        self.assembly_name = "Tall Single Door"
        self.door_type = "Tall"
        self.door_swing = "Left Swing"
        self.width = fd.inches(18)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)

class INSERT_Tall_Double_Door(Doors):
    
    def __init__(self):
        self.category_name = "Frameless"
        self.assembly_name = "Tall Double Door"
        self.door_type = "Tall"
        self.door_swing = "Double Door"
        self.width = fd.inches(36)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
    
class INSERT_Upper_Single_Door(Doors):
    
    def __init__(self):
        self.category_name = "Frameless"
        self.assembly_name = "Upper Single Door"
        self.door_type = "Upper"
        self.door_swing = "Left Swing"
        self.width = fd.inches(18)
        self.height = fd.inches(42)
        self.depth = fd.inches(23)

class INSERT_Upper_Double_Door(Doors):
    
    def __init__(self):
        self.category_name = "Frameless"
        self.assembly_name = "Upper Double Door"
        self.door_type = "Upper"
        self.door_swing = "Double Door"
        self.width = fd.inches(36)
        self.height = fd.inches(42)
        self.depth = fd.inches(23)
        
class INSERT_Base_Single_Door_FF(FF_Doors):
    
    def __init__(self):
        self.category_name = "Face Frame"
        self.assembly_name = "Base Single Door FF"
        self.door_type = "Base"
        self.door_swing = "Left Swing"
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
class INSERT_Base_Double_Door_FF(FF_Doors):
    
    def __init__(self):
        self.category_name = "Face Frame"
        self.assembly_name = "Base Double Door FF"
        self.door_type = "Base"
        self.door_swing = "Double Door"
        self.width = fd.inches(36)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
class INSERT_Tall_Single_Door_FF(FF_Doors):
    
    def __init__(self):
        self.category_name = "Face Frame"
        self.assembly_name = "Tall Single Door FF"
        self.door_type = "Tall"
        self.door_swing = "Left Swing"
        self.width = fd.inches(18)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
        
class INSERT_Tall_Double_Door_FF(FF_Doors):
    
    def __init__(self):
        self.category_name = "Face Frame"
        self.assembly_name = "Tall Double Door FF"
        self.door_type = "Tall"
        self.door_swing = "Double Door"
        self.width = fd.inches(36)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
        
class INSERT_Upper_Single_Door_FF(FF_Doors):
    
    def __init__(self):
        self.category_name = "Face Frame"
        self.assembly_name = "Upper Single Door FF"
        self.door_type = "Upper"
        self.door_swing = "Left Swing"
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
class INSERT_Upper_Double_Door_FF(FF_Doors):
    
    def __init__(self):
        self.category_name = "Face Frame"
        self.assembly_name = "Upper Double Door FF"
        self.door_type = "Upper"
        self.door_swing = "Double Door"
        self.width = fd.inches(36)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)

class INSERT_1_Drawer(Drawers):
    
    def __init__(self):
        self.category_name = "Frameless"
        self.assembly_name = "1 Drawer"
        self.door_type = "Drawer"
        self.width = fd.inches(18)
        self.height = fd.inches(6)
        self.depth = fd.inches(19)
        self.mirror_y = False
        
class INSERT_2_Drawer_Stack(Drawers):
    
    def __init__(self):
        self.category_name = "Frameless"
        self.assembly_name = "2 Drawer Stack"
        self.door_type = "Drawer"
        self.direction = 'Vertical'
        self.drawer_qty = 2
        self.width = fd.inches(18)
        self.height = fd.inches(6*2)
        self.depth = fd.inches(19)
        self.mirror_y = False
        
class INSERT_3_Drawer_Stack(Drawers):
    
    def __init__(self):
        self.category_name = "Frameless"
        self.assembly_name = "3 Drawer Stack"
        self.door_type = "Drawer"
        self.direction = 'Vertical'
        self.drawer_qty = 3
        self.width = fd.inches(18)
        self.height = fd.inches(6*3)
        self.depth = fd.inches(19)
        self.mirror_y = False
        
class INSERT_4_Drawer_Stack(Drawers):
    
    def __init__(self):
        self.category_name = "Frameless"
        self.assembly_name = "4 Drawer Stack"
        self.door_type = "Drawer"
        self.direction = 'Vertical'
        self.drawer_qty = 4
        self.width = fd.inches(18)
        self.height = fd.inches(6*4)
        self.depth = fd.inches(19)
        self.mirror_y = False
        
class INSERT_1_Drawer_FF(FF_Drawer):
    
    def __init__(self):
        self.category_name = "Face Frame"
        self.assembly_name = "1 Drawer FF"
        self.door_type = "Drawer"
        self.width = fd.inches(18)
        self.height = fd.inches(6)
        self.depth = fd.inches(19)
        self.mirror_y = False
        
class INSERT_Horizontal_Drawers(Horizontal_Drawers):
     
    def __init__(self):
        self.category_name = "Frameless"
        self.assembly_name = "Horizontal Drawers"
        self.width = fd.inches(36)
        self.height = fd.inches(6)
        self.depth = fd.inches(20)
        self.mirror_y = False
        
class INSERT_Horizontal_Drawers_FF(FF_Horizontal_Drawers):
    
    def __init__(self):
        self.category_name = "Face Frame"
        self.assembly_name = "Horizontal Drawers FF"
        self.width = fd.inches(36)
        self.height = fd.inches(6)
        self.depth = fd.inches(20)
        self.mirror_y = False
        
class INSERT_Base_Pie_Cut_Door(Pie_Cut_Doors):
    
    def __init__(self):
        self.category_name = "Corner"
        self.assembly_name = "Base Pie Cut Door"
        self.door_type = "Base"
        self.door_swing = "Left Swing"
        self.width = fd.inches(36)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
class INSERT_Upper_Pie_Cut_Door(Pie_Cut_Doors):
    
    def __init__(self):
        self.category_name = "Corner"
        self.assembly_name = "Upper Pie Cut Door"
        self.door_type = "Upper"
        self.door_swing = "Left Swing"
        self.width = fd.inches(36)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
class INSERT_Base_Pie_Cut_Door_FF(FF_Pie_Cut_Doors):
    
    def __init__(self):
        self.category_name = "Corner"
        self.assembly_name = "Base Pie Cut Door FF"
        self.door_type = "Base"
        self.door_swing = "Left Swing"
        self.width = fd.inches(36)
        self.height = fd.inches(34)
        self.depth = fd.inches(36)
        
class INSERT_Upper_Pie_Cut_Door_FF(FF_Pie_Cut_Doors):
    
    def __init__(self):
        self.category_name = "Corner"
        self.assembly_name = "Upper Pie Cut Door FF"
        self.door_type = "Upper"
        self.door_swing = "Left Swing"
        self.width = fd.inches(36)
        self.height = fd.inches(34)
        self.depth = fd.inches(36)
        
#---------FILLERS
        
class INSERT_Flute_Panel(Fluted_Molding):
    
    def __init__(self):
        self.category_name = "Frameless"
        self.assembly_name = "Fluted Molding"
        self.width = fd.inches(3)
        self.height = fd.inches(30)
        self.depth = fd.inches(16)
        
#---------INSERT: TILT-OUT HAMPER
        
class INSERT_Tilt_Out_Hamper(Tilt_Out_Hamper):
    
    def __init__(self):
        self.category_name = "Frameless"
        self.assembly_name = "Tilt Out Hamper"
        self.width = fd.inches(25)
        self.height = fd.inches(25)
        self.depth = fd.inches(19)
        
#---------OPERATORS

class PROMPTS_Door_Prompts(bpy.types.Operator):
    bl_idname = "exteriors.door_prompts"
    bl_label = "Door Prompts" 
    bl_description = "This shows all of the available door options"
    bl_options = {'UNDO'}
    
    object_name = bpy.props.StringProperty(name="Object Name")
    
    assembly = None
    
    door_rotation = bpy.props.FloatProperty(name="Door Rotation",subtype='ANGLE',min=0,max=math.radians(120))
    
    door_swing = bpy.props.EnumProperty(name="Door Swing",items=[('Left Swing',"Left Swing","Left Swing"),
                                                                 ('Right Swing',"Right Swing","Right Swing"),
                                                                 ('Double Door',"Double Door","Double Door")])
    
    @classmethod
    def poll(cls, context):
        return True
        
    def check(self, context):
        swing = self.assembly.get_prompt('Swing')
        door_rotation = self.assembly.get_prompt('Door Rotation')
        if swing:
            swing.set_value(self.door_swing)
        if door_rotation:
            door_rotation.set_value(self.door_rotation)
        self.assembly.obj_bp.location = self.assembly.obj_bp.location # Redraw Viewport
        return True
        
    def execute(self, context):
        return {'FINISHED'}
        
    def set_default_properties(self):
        swing = self.assembly.get_prompt("Swing")
        door_pull = self.assembly.get_prompt("Door Pull")
        door_rotation = self.assembly.get_prompt("Door Rotation")
        if swing:
            self.door_swing = swing.value()
        if door_rotation:
            self.door_rotation = door_rotation.value()
            
    def invoke(self,context,event):
        obj = bpy.data.objects[self.object_name]
        obj_insert_bp = fd.get_bp(obj,'INSERT')
        self.assembly = fd.Assembly(obj_insert_bp)
        self.set_default_properties()
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=fd.get_prop_dialog_width(330))
        
    def draw(self, context):
        layout = self.layout
        if self.assembly.obj_bp:
            if self.assembly.obj_bp.name in context.scene.objects:
                box = layout.box()
                row = box.row()
                row.label("Open Door")
                row.prop(self,'door_rotation',slider=True,text="")
                row = box.row()
                row.label("Door Swing")
                row.prop(self,'door_swing',text="")

                inset_front = self.assembly.get_prompt('Inset Front')
                
                half_overlay_top = self.assembly.get_prompt('Half Overlay Top')
                half_overlay_bottom = self.assembly.get_prompt('Half Overlay Bottom')
                half_overlay_left = self.assembly.get_prompt('Half Overlay Left')
                half_overlay_right = self.assembly.get_prompt('Half Overlay Right')
                
                inset_reveal = self.assembly.get_prompt('Inset Reveal')
                top_reveal = self.assembly.get_prompt('Top Reveal')
                bottom_reveal = self.assembly.get_prompt('Bottom Reveal')
                left_reveal = self.assembly.get_prompt('Left Reveal')
                right_reveal = self.assembly.get_prompt('Right Reveal')
                
                vertical_gap = self.assembly.get_prompt('Vertical Gap')
                door_gap = self.assembly.get_prompt('Door to Cabinet Gap')
                
                row = box.row()
                row.label("Inset Front")
                row.prop(inset_front,'CheckBoxValue',text="")
                
                if not inset_front.value():
                    box = layout.box()
                    box.label("Half Overlays:")
                    row = box.row()
                    row.prop(half_overlay_top,'CheckBoxValue',text="Top")
                    row.prop(half_overlay_bottom,'CheckBoxValue',text="Bottom")
                    row.prop(half_overlay_left,'CheckBoxValue',text="Left")
                    row.prop(half_overlay_right,'CheckBoxValue',text="Right")
                    
                box = layout.box()
                box.label("Reveal and Gaps")
                
                if inset_front.value():
                    box.prop(inset_reveal,'DistanceValue',text="Inset Reveal")
                else:
                    col = box.column(align=True)
                    col.prop(top_reveal,'DistanceValue',text="Top Reveal")
                    col.prop(bottom_reveal,'DistanceValue',text="Bottom Reveal")
                    col.prop(left_reveal,'DistanceValue',text="Left Reveal")
                    col.prop(right_reveal,'DistanceValue',text="Right Reveal")
                 
                box.prop(vertical_gap,'DistanceValue',text="Horizontal Gap")
                box.prop(door_gap,'DistanceValue',text="Door To Cabinet Gap")

class PROMPTS_Drawer_Prompts(bpy.types.Operator):
    bl_idname = "exteriors.drawer_prompts"
    bl_label = "Drawer Prompts" 
    bl_description = "This shows all of the available drawer options"
    bl_options = {'UNDO'}
    
    object_name = bpy.props.StringProperty(name="Object Name")
    
    assembly = None
    
    drawer_tabs = bpy.props.EnumProperty(name="Main Tabs",
                                         items=[('DRAWER_FRONTS',"Drawer Fronts",'Set the Drawer Front Heights'),
                                                ('DRAWER_OPTIONS',"Drawer Options",'Set the Drawer Options')],
                                         default = 'DRAWER_FRONTS')
    
    open = bpy.props.FloatProperty(name="Open",min=0,max=100,subtype='PERCENTAGE')
    
    door_swing = bpy.props.EnumProperty(name="Door Swing",items=[('Left Swing',"Left Swing","Left Swing"),
                                                                 ('Right Swing',"Right Swing","Right Swing"),
                                                                 ('Double Door',"Double Door","Double Door")])
    
    @classmethod
    def poll(cls, context):
        return True
        
    def check(self, context):
        fd.run_calculators(self.assembly.obj_bp)
        swing = self.assembly.get_prompt('Swing')
        if swing:
            swing.set_value(self.door_swing)
        self.assembly.obj_bp.location = self.assembly.obj_bp.location # Redraw Viewport
        return True
        
    def execute(self, context):
        return {'FINISHED'}
        
    def set_default_properties(self):
        pass

    def invoke(self,context,event):
        obj = bpy.data.objects[self.object_name]
        obj_insert_bp = fd.get_bp(obj,'INSERT')
        self.assembly = fd.Assembly(obj_insert_bp)
        self.set_default_properties()
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=fd.get_prop_dialog_width(330))
    
    def draw_drawer_heights(self,layout):
        top = self.assembly.get_prompt("Top Drawer Height")
        second = self.assembly.get_prompt("Second Drawer Height")
        third = self.assembly.get_prompt("Third Drawer Height")
        bottom = self.assembly.get_prompt("Bottom Drawer Height")
        
        if top:
            row = layout.row()
            row.label("Top Drawer Height:")
            if top.equal:
                row.label(str(fd.unit(top.DistanceValue)))
                row.prop(top,'equal',text="")
            else:
                row.prop(top,'DistanceValue',text="")
                row.prop(top,'equal',text="")
        
        if second:
            row = layout.row()
            row.label("Second Drawer Height:")
            if second.equal:
                row.label(str(fd.unit(second.DistanceValue)))
                row.prop(second,'equal',text="")
            else:
                row.prop(second,'DistanceValue',text="")
                row.prop(second,'equal',text="")
        
        if third:
            row = layout.row()
            row.label("Third Drawer Height:")
            if third.equal:
                row.label(str(fd.unit(third.DistanceValue)))
                row.prop(third,'equal',text="")
            else:
                row.prop(third,'DistanceValue',text="")
                row.prop(third,'equal',text="")
        
        if bottom:
            row = layout.row()
            row.label("Bottom Drawer Height:")
            if bottom.equal:
                row.label(str(fd.unit(bottom.DistanceValue)))
                row.prop(bottom,'equal',text="")
            else:
                row.prop(bottom,'DistanceValue',text="")
                row.prop(bottom,'equal',text="")
        
    def draw(self, context):
        layout = self.layout
        if self.assembly.obj_bp:
            if self.assembly.obj_bp.name in context.scene.objects:
                box = layout.box()
                row = box.row()
                row.prop(self,'drawer_tabs',expand=True)
                if self.drawer_tabs == 'DRAWER_FRONTS':
                    self.draw_drawer_heights(box)
                if self.drawer_tabs == 'DRAWER_OPTIONS':
                    inset_front = self.assembly.get_prompt('Inset Front')
                    open = self.assembly.get_prompt('Open')
                    
                    half_overlay_top = self.assembly.get_prompt('Half Overlay Top')
                    half_overlay_bottom = self.assembly.get_prompt('Half Overlay Bottom')
                    half_overlay_left = self.assembly.get_prompt('Half Overlay Left')
                    half_overlay_right = self.assembly.get_prompt('Half Overlay Right')
                    
                    inset_reveal = self.assembly.get_prompt('Inset Reveal')
                    top_reveal = self.assembly.get_prompt('Top Reveal')
                    bottom_reveal = self.assembly.get_prompt('Bottom Reveal')
                    left_reveal = self.assembly.get_prompt('Left Reveal')
                    right_reveal = self.assembly.get_prompt('Right Reveal')
                    
                    horizontal_gap  = self.assembly.get_prompt('Horizontal Gap')
                    door_gap = self.assembly.get_prompt('Door to Cabinet Gap')
                    
                    row = box.row()
                    row.label("Inset Door")
                    row.prop(inset_front,'CheckBoxValue',text="")
                    
                    row = box.row()
                    row.label("Open")
                    row.prop(open,'PercentageValue',text="")
                    
                    if not inset_front.value():
                        box = layout.box()
                        box.label("Half Overlays:")
                        row = box.row()
                        row.prop(half_overlay_top,'CheckBoxValue',text="Top")
                        row.prop(half_overlay_bottom,'CheckBoxValue',text="Bottom")
                        row.prop(half_overlay_left,'CheckBoxValue',text="Left")
                        row.prop(half_overlay_right,'CheckBoxValue',text="Right")
                        
                    box = layout.box()
                    box.label("Reveal and Gaps")
                    
                    if inset_front.value():
                        box.prop(inset_reveal,'DistanceValue',text="Inset Reveal")
                    else:
                        col = box.column(align=True)
                        col.prop(top_reveal,'DistanceValue',text="Top Reveal")
                        col.prop(bottom_reveal,'DistanceValue',text="Bottom Reveal")
                        col.prop(left_reveal,'DistanceValue',text="Left Reveal")
                        col.prop(right_reveal,'DistanceValue',text="Right Reveal")
                     
                    box.prop(horizontal_gap,'DistanceValue',text="Vertical Gap")
                    box.prop(door_gap,'DistanceValue',text="Door To Cabinet Gap")

class PROMPTS_Hamper_Prompts(bpy.types.Operator):
    bl_idname = "exteriors.hamper_prompts"
    bl_label = "Hamper Prompts" 
    bl_description = "This shows all of the available hamper options"
    bl_options = {'UNDO'}
    
    object_name = bpy.props.StringProperty(name="Object Name")
    
    assembly = None
    
    @classmethod
    def poll(cls, context):
        return True
        
    def execute(self, context):
        return {'FINISHED'}
        
    def check(self, context):
        fd.run_calculators(self.assembly.obj_bp)
        self.assembly.obj_bp.location = self.assembly.obj_bp.location # Redraw Viewport
        return True

    def invoke(self,context,event):
        obj = bpy.data.objects[self.object_name]
        obj_insert_bp = fd.get_bp(obj,'INSERT')
        self.assembly = fd.Assembly(obj_insert_bp)
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=330)
    
    def draw(self, context):
        layout = self.layout
        if self.assembly.obj_bp:
            if self.assembly.obj_bp.name in context.scene.objects:
                open_hamper = self.assembly.get_prompt('Open')
                box = layout.box()
                row = box.row()
                row.prop(open_hamper,'PercentageValue',text="Open")

class OPERATOR_Update_Project(bpy.types.Operator):
    """ This will clear all the spec groups to save on file size.
    """
    bl_idname = "exteriors.update_project"
    bl_label = "Change Door Style"
    bl_description = "This will update the project with the selected door styles"
    bl_options = {'UNDO'}
    
    cabinet_type = bpy.props.StringProperty(name = "Cabinet Type")
    
    def execute(self, context):
        g = context.scene.lm_exteriors
        doors = []
        for obj in context.scene.objects:
            if obj.mv.type == 'BPASSEMBLY':
                if self.cabinet_type == "Drawer":
                    if "Drawer Front" in obj.mv.name_object:
                        doors.append(obj)
                else:
                    if "Cabinet Door" in obj.mv.name_object and self.cabinet_type in obj.mv.name_object:
                        print("self.cabinet_type: ",self.cabinet_type)
                        print("obj.mv.name_object: ",obj.mv.name_object)
                        doors.append(obj)
                
        if self.cabinet_type == "Base":
            pull_name = g.Base_Door_Style
        if self.cabinet_type == "Tall":
            pull_name = g.Tall_Door_Style
        if self.cabinet_type == "Upper":
            pull_name = g.Upper_Door_Style
        if self.cabinet_type == "Drawer":
            pull_name = g.Drawer_Front_Style

        for door in doors:
            door_assembly = fd.Assembly(door)
            new_door = fd.get_assembly((HIDDEN_FOLDER_NAME,DOOR_LIBRARY_NAME,DOOR_CATEGORY_NAME),assembly_name=pull_name)
            new_door.obj_bp.mv.name_object = door_assembly.obj_bp.mv.name_object
            new_door.obj_bp.parent = door_assembly.obj_bp.parent
            new_door.obj_bp.location = door_assembly.obj_bp.location
            new_door.obj_bp.rotation_euler = door_assembly.obj_bp.rotation_euler
            
            property_id = door_assembly.obj_bp.mv.property_id
            
            fd.copy_drivers(door_assembly.obj_bp,new_door.obj_bp)
            fd.copy_prompt_drivers(door_assembly.obj_bp,new_door.obj_bp)
            fd.copy_drivers(door_assembly.obj_x,new_door.obj_x)
            fd.copy_drivers(door_assembly.obj_y,new_door.obj_y)
            fd.copy_drivers(door_assembly.obj_z,new_door.obj_z)
            obj_list = []
            obj_list.append(door_assembly.obj_bp)
            for child in door_assembly.obj_bp.children:
                obj_list.append(child)
            fd.delete_obj_list(obj_list)
            
            new_door.obj_bp.mv.property_id = property_id
            for child in new_door.obj_bp.children:
                child.mv.property_id = property_id
                if child.type == 'EMPTY':
                    child.hide
                if child.type == 'MESH':
                    child.draw_type = 'TEXTURED'
                    fd.assign_materials_from_pointers(child)
                if child.mv.type == 'CAGE':
                    child.hide = True
                
        return {'FINISHED'}

class OPERATOR_Update_Selection(bpy.types.Operator):
    """ This will clear all the spec groups to save on file size.
    """
    bl_idname = "exteriors.update_selection"
    bl_label = "Update Door Selection"
    bl_description = "This will change the selected door with the active door"
    bl_options = {'UNDO'}
    
    cabinet_type = bpy.props.StringProperty(name = "Cabinet Type")
    
    @classmethod
    def poll(cls, context):
        obj = context.active_object
        obj_bp = fd.get_assembly_bp(obj)
        if obj_bp:
            assembly = fd.Assembly(obj_bp)
            if "Drawer Front" in assembly.obj_bp.mv.name_object:
                return True
            elif "Cabinet Door" in assembly.obj_bp.mv.name_object:
                return True
            elif "Hamper Door" in assembly.obj_bp.mv.name_object:
                return True
            elif "False Front" in assembly.obj_bp.mv.name_object:
                return True
            else:
                return False
        return False
            
    def execute(self, context):
        g = context.scene.lm_exteriors
        obj = context.active_object
        obj_bp = fd.get_assembly_bp(obj)
        door_assembly = fd.Assembly(obj_bp)
                
        if self.cabinet_type == "Base":
            pull_name = g.Base_Door_Style
        if self.cabinet_type == "Tall":
            pull_name = g.Tall_Door_Style
        if self.cabinet_type == "Upper":
            pull_name = g.Upper_Door_Style
        if self.cabinet_type == "Drawer":
            pull_name = g.Drawer_Door_Style

        new_door = fd.get_assembly((HIDDEN_FOLDER_NAME,DOOR_LIBRARY_NAME,DOOR_CATEGORY_NAME),assembly_name=pull_name)
        new_door.obj_bp.mv.name_object = door_assembly.obj_bp.mv.name_object
        new_door.obj_bp.parent = door_assembly.obj_bp.parent
        new_door.obj_bp.location = door_assembly.obj_bp.location
        new_door.obj_bp.rotation_euler = door_assembly.obj_bp.rotation_euler
        
        property_id = door_assembly.obj_bp.mv.property_id

        fd.copy_drivers(door_assembly.obj_bp,new_door.obj_bp)
        fd.copy_prompt_drivers(door_assembly.obj_bp,new_door.obj_bp)
        fd.copy_drivers(door_assembly.obj_x,new_door.obj_x)
        fd.copy_drivers(door_assembly.obj_y,new_door.obj_y)
        fd.copy_drivers(door_assembly.obj_z,new_door.obj_z)
        obj_list = []
        obj_list.append(door_assembly.obj_bp)
        for child in door_assembly.obj_bp.children:
            obj_list.append(child)
        fd.delete_obj_list(obj_list)

        new_door.obj_bp.mv.property_id = property_id
        for child in new_door.obj_bp.children:
            child.mv.property_id = property_id
            if child.type == 'EMPTY':
                child.hide
            if child.type == 'MESH':
                child.draw_type = 'TEXTURED'
                fd.assign_materials_from_pointers(child)
            if child.mv.type == 'CAGE':
                child.hide = True

        return {'FINISHED'}

class OPERATOR_Place_Applied_Panel(bpy.types.Operator):
    bl_idname = "lm_exteriors.place_applied_panel"
    bl_label = "Place Applied Panel"
    bl_options = {'UNDO'}
    
    #READONLY
    filepath = bpy.props.StringProperty(name="Material Name")
    type_insert = bpy.props.StringProperty(name="Type Insert")
    
    item_name = None
    dir_name = ""
    
    assembly = None
    
    cages = []
    
    def get_panel(self,context):
        g = context.scene.lm_exteriors
        self.assembly = fd.get_assembly((HIDDEN_FOLDER_NAME,DOOR_LIBRARY_NAME,DOOR_CATEGORY_NAME),assembly_name=g.Applied_End_Panel_Style)
        
#     def set_properties(self):
#         list_obj = fd.get_child_objects(self.assembly.obj_bp)
#         for obj in list_obj:
#             obj.hide = False
#             obj.hide_select = False
#             obj.mv.property_id = "cabinetlib.prompts"
#             cabinet_utils.assign_materials_from_pointers(obj)
#             if obj.type == 'EMPTY':
#                 obj.hide = True
            
    def set_xray(self,turn_on=True):
        cages = []
        for child in self.assembly.obj_bp.children:
            child.show_x_ray = turn_on
            if turn_on:
                child.draw_type = 'WIRE'
            else:
                if child.mv.type == 'CAGE':
                    cages.append(child)
                child.draw_type = 'TEXTURED'
                fd.assign_materials_from_pointers(child)
        fd.delete_obj_list(cages)

    def invoke(self, context, event):
        self.get_panel(context)
        context.window.cursor_set('PAINT_BRUSH')
        context.scene.update() # THE SCENE MUST BE UPDATED FOR RAY CAST TO WORK
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def cancel_drop(self,context,event):
        if self.assembly:
            fd.delete_object_and_children(self.assembly.obj_bp)
        bpy.context.window.cursor_set('DEFAULT')
        fd.delete_obj_list(self.cages)
#         bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
        return {'FINISHED'}

    def add_to_left(self,part,product):
#         product = properties.Product(cabinet_utils.get_bp(part.obj_bp,'PRODUCT'))
        self.assembly.obj_bp.parent = product.obj_bp
        
        toe_kick_height = 0
        if product.get_prompt('Toe Kick Height'):
            toe_kick_height = product.get_prompt('Toe Kick Height')
        
        if product.obj_z.location.z > 0:
            self.assembly.obj_bp.location = (0,0,toe_kick_height)
        else:
            self.assembly.obj_bp.location = (0,0,product.obj_z.location.z)
        
        self.assembly.obj_bp.rotation_euler = (0,math.radians(-90),0)
        self.assembly.obj_x.location.x = math.fabs(product.obj_z.location.z) - toe_kick_height
        self.assembly.obj_y.location.y = product.obj_y.location.y
    
    def add_to_right(self,part,product):
#         product = properties.Product(cabinet_utils.get_bp(part.obj_bp,'PRODUCT'))
        self.assembly.obj_bp.parent = product.obj_bp
        
        toe_kick_height = 0
        if product.get_prompt('Toe Kick Height'):
            toe_kick_height = product.get_prompt('Toe Kick Height')
        
        if product.obj_z.location.z > 0:
            self.assembly.obj_bp.location = (product.obj_x.location.x,0,toe_kick_height)
        else:
            self.assembly.obj_bp.location = (product.obj_x.location.x,0,product.obj_z.location.z)
            
        self.assembly.obj_bp.rotation_euler = (0,math.radians(-90),math.radians(180))
        self.assembly.obj_x.location.x = math.fabs(product.obj_z.location.z) - toe_kick_height
        self.assembly.obj_y.location.y = math.fabs(product.obj_y.location.y)
        
    def add_to_back(self,part,product):
#         product = properties.Product(cabinet_utils.get_bp(part.obj_bp,'PRODUCT'))
        self.assembly.obj_bp.parent = product.obj_bp
        
        toe_kick_height = 0
        if product.get_prompt('Toe Kick Height'):
            toe_kick_height = product.get_prompt('Toe Kick Height')
        
        if product.obj_z.location.z > 0:
            self.assembly.obj_bp.location = (0,0,toe_kick_height)
        else:
            self.assembly.obj_bp.location = (0,0,product.obj_z.location.z)
            
        self.assembly.obj_bp.rotation_euler = (0,math.radians(-90),math.radians(-90))
        self.assembly.obj_x.location.x = math.fabs(product.obj_z.location.z) - toe_kick_height
        self.assembly.obj_y.location.y = product.obj_x.location.x
    
    def door_panel_drop(self,context,event):
        selected_point, selected_obj = fd.get_selection_point(context,event,objects=self.cages)
        bpy.ops.object.select_all(action='DESELECT')
        sel_product_bp = fd.get_bp(selected_obj,'PRODUCT')
        sel_assembly_bp = fd.get_assembly_bp(selected_obj)

        if sel_product_bp and sel_assembly_bp:
            product = fd.Library_Assembly(sel_product_bp)
            assembly = fd.Assembly(sel_assembly_bp)
            if product and assembly and 'Door' not in assembly.obj_bp.mv.name_object:
                self.assembly.obj_bp.parent = None
                if product.placement_type == 'Corner':
                    pass
                    #TODO: IMPLEMENT CORNER PLACEMENT
                else:
                    if 'Left' in assembly.obj_bp.mv.name_object:
                        self.add_to_left(assembly,product)
                    if 'Right' in assembly.obj_bp.mv.name_object:
                        self.add_to_right(assembly,product)
                    if 'Back' in assembly.obj_bp.mv.name_object:
                        self.add_to_back(assembly,product)
        else:
            self.assembly.obj_bp.parent = None
            self.assembly.obj_bp.location = selected_point

        if event.type == 'LEFTMOUSE' and event.value == 'PRESS':
            self.set_xray(False)
            fd.delete_obj_list(self.cages)
            bpy.context.window.cursor_set('DEFAULT')
            if event.shift:
                self.get_panel(context)
            else:
                bpy.ops.object.select_all(action='DESELECT')
                context.scene.objects.active = self.assembly.obj_bp
                self.assembly.obj_bp.select = True
                return {'FINISHED'}
        
        return {'RUNNING_MODAL'}
    
    def modal(self, context, event):
        context.area.tag_redraw()
        
        if event.type in {'MIDDLEMOUSE', 'WHEELUPMOUSE', 'WHEELDOWNMOUSE'}:
            return {'PASS_THROUGH'}
        
        if event.type in {'ESC'}:
            self.cancel_drop(context,event)
            return {'FINISHED'}    
        
        return self.door_panel_drop(context,event)

class PROPERTIES_Scene_Variables(bpy.types.PropertyGroup):
    #DOOR STYLES
    Base_Door_Style = bpy.props.EnumProperty(name="Base Door Style",items=enum_preview_from_dir)
    
    Tall_Door_Style = bpy.props.EnumProperty(name="Tall Door Style",items=enum_preview_from_dir)
    
    Upper_Door_Style = bpy.props.EnumProperty(name="Upper Door Style",items=enum_preview_from_dir)
    
    Drawer_Front_Style = bpy.props.EnumProperty(name="Drawer Door Style",items=enum_preview_from_dir)

    Applied_End_Panel_Style = bpy.props.EnumProperty(name="Applied End Panel Style",items=enum_preview_from_dir)
    
    Inset_Door = bpy.props.BoolProperty(name="Inset Door", 
                              description="Check this to use inset doors", 
                              default=False)
    
    Inset_Reveal = bpy.props.FloatProperty(name="Inset Reveal",
                                 description="This sets the reveal for inset doors.",
                                 default=fd.inches(.125),
                                 unit='LENGTH',
                                 precision=4)
    
    Left_Reveal = bpy.props.FloatProperty(name="Left Reveal",
                                description="This sets the left reveal for overlay doors.",
                                default=fd.inches(.0625),
                                unit='LENGTH',
                                precision=4)
    
    Right_Reveal = bpy.props.FloatProperty(name="Right Reveal",
                                 description="This sets the right reveal for overlay doors.",
                                 default=fd.inches(.0625),
                                 unit='LENGTH',
                                 precision=4)
    
    Base_Top_Reveal = bpy.props.FloatProperty(name="Base Top Reveal",
                                    description="This sets the top reveal for base overlay doors.",
                                    default=fd.inches(.25),
                                    unit='LENGTH',
                                    precision=4)
    
    Tall_Top_Reveal = bpy.props.FloatProperty(name="Tall Top Reveal",
                                    description="This sets the top reveal for tall overlay doors.",
                                    default=fd.inches(0),
                                    unit='LENGTH',
                                    precision=4)
    
    Upper_Top_Reveal = bpy.props.FloatProperty(name="Upper Top Reveal",
                                     description="This sets the top reveal for upper overlay doors.",
                                     default=fd.inches(0),
                                     unit='LENGTH',
                                     precision=4)
    
    Base_Bottom_Reveal = bpy.props.FloatProperty(name="Base Bottom Reveal",
                                       description="This sets the bottom reveal for base overlay doors.",
                                       default=fd.inches(0),
                                       unit='LENGTH',
                                       precision=4)
    
    Tall_Bottom_Reveal = bpy.props.FloatProperty(name="Tall Bottom Reveal",
                                       description="This sets the bottom reveal for tall overlay doors.",
                                       default=fd.inches(0),
                                       unit='LENGTH',
                                       precision=4)
    
    Upper_Bottom_Reveal = bpy.props.FloatProperty(name="Upper Bottom Reveal",
                                        description="This sets the bottom reveal for upper overlay doors.",
                                        default=fd.inches(.25),
                                        unit='LENGTH',
                                        precision=4)
    
    Vertical_Gap = bpy.props.FloatProperty(name="Vertical Gap",
                                 description="This sets the distance between double doors.",
                                 default=fd.inches(.125),
                                 unit='LENGTH',
                                 precision=4)
    
    Door_To_Cabinet_Gap = bpy.props.FloatProperty(name="Door to Cabinet Gap",
                                        description="This sets the distance between the back of the door and the front cabinet edge.",
                                        default=fd.inches(.125),
                                        unit='LENGTH',
                                        precision=4)
    
    #PULL OPTIONS
    Base_Pull_Location = bpy.props.FloatProperty(name="Base Pull Location",
                                       description="Z Distance from the top of the door edge to the top of the pull",
                                       default=fd.inches(2),
                                       unit='LENGTH') 
    
    Tall_Pull_Location = bpy.props.FloatProperty(name="Tall Pull Location",
                                       description="Z Distance from the bottom of the door edge to the center of the pull",
                                       default=fd.inches(40),
                                       unit='LENGTH')
    
    Upper_Pull_Location = bpy.props.FloatProperty(name="Upper Pull Location",
                                        description="Z Distance from the bottom of the door edge to the bottom of the pull",
                                        default=fd.inches(2),
                                        unit='LENGTH') 
    
    Center_Pulls_on_Drawers = bpy.props.BoolProperty(name="Center Pulls on Drawers",
                                           description="Center pulls on the drawer heights. Otherwise the pull z location is controlled with Drawer Pull From Top",
                                           default=False) 
    
    No_Pulls = bpy.props.BoolProperty(name="No Pulls",
                            description="Check this option to turn off pull hardware",
                            default=False) 
    
    Pull_From_Edge = bpy.props.FloatProperty(name="Pull From Edge",
                                   description="X Distance from the door edge to the pull",
                                   default=fd.inches(1.5),
                                   unit='LENGTH') 
    
    Drawer_Pull_From_Top = bpy.props.FloatProperty(name="Drawer Pull From Top",
                                         description="When Center Pulls on Drawers is off this is the amount from the top of the drawer front to the enter pull",
                                         default=fd.inches(1.5),unit='LENGTH') 
    
    Pull_Rotation = bpy.props.FloatProperty(name="Pull Rotation",
                                  description="Rotation of pulls on doors",
                                  default=math.radians(0),
                                  subtype='ANGLE') 

    Pull_Name = bpy.props.StringProperty(name="Pull Name",default="Test Pull")

    def draw(self,layout):
        col = layout.column(align=True)
        
        box = col.box()
        box.label("Door & Drawer Defaults:")
        
        row = box.row(align=True)
        row.prop(self,"Inset_Door")
        row.prop(self,"No_Pulls")
        
        if not self.No_Pulls:
            box = col.box()
            box.label("Pull Placement:")
            
            row = box.row(align=True)
            row.label("Base Doors:")
            row.prop(self,"Base_Pull_Location",text="From Top of Door")
            
            row = box.row(align=True)
            row.label("Tall Doors:")
            row.prop(self,"Tall_Pull_Location",text="From Bottom of Door")
            
            row = box.row(align=True)
            row.label("Upper Doors:")
            row.prop(self,"Upper_Pull_Location",text="From Bottom of Door")
            
            row = box.row(align=True)
            row.label("Distance From Edge:")
            row.prop(self,"Pull_From_Edge",text="")
            
            row = box.row(align=True)
            row.prop(self,"Center_Pulls_on_Drawers")
    
            if not self.Center_Pulls_on_Drawers:
                row.prop(self,"Drawer_Pull_From_Top",text="Distance From Top")
        
        box = col.box()
        box.label("Door & Drawer Reveals:")
        
        if self.Inset_Door:
            row = box.row(align=True)
            row.label("Inset Reveals:")
            row.prop(self,"Inset_Reveal",text="")
        else:
            row = box.row(align=True)
            row.label("Standard Reveals:")
            row.prop(self,"Left_Reveal",text="Left")
            row.prop(self,"Right_Reveal",text="Right")
            
            row = box.row(align=True)
            row.label("Base Door Reveals:")
            row.prop(self,"Base_Top_Reveal",text="Top")
            row.prop(self,"Base_Bottom_Reveal",text="Bottom")
            
            row = box.row(align=True)
            row.label("Tall Door Reveals:")
            row.prop(self,"Tall_Top_Reveal",text="Top")
            row.prop(self,"Tall_Bottom_Reveal",text="Bottom")
            
            row = box.row(align=True)
            row.label("Upper Door Reveals:")
            row.prop(self,"Upper_Top_Reveal",text="Top")
            row.prop(self,"Upper_Bottom_Reveal",text="Bottom")
            
        row = box.row(align=True)
        row.label("Vertical Gap:")
        row.prop(self,"Vertical_Gap",text="")
    
        row = box.row(align=True)
        row.label("Door To Cabinet Gap:")
        row.prop(self,"Door_To_Cabinet_Gap",text="")

def MV_CALCULATE_HINGE_QTY(height):
    if height <= fd.inches(36):
        return 2
    elif height <= fd.inches(51):
        return 3
    elif height <= fd.inches(66):
        return 4
    elif height <= fd.inches(81):
        return 5
    elif height <= fd.inches(96):
        return 6
    else:
        return 7
    
@persistent
def load_driver_functions(scene=None):
    bpy.app.driver_namespace["MV_CALCULATE_HINGE_QTY"] = MV_CALCULATE_HINGE_QTY

bpy.app.handlers.load_post.append(load_driver_functions)

def register():
    bpy.utils.register_class(PROPERTIES_Scene_Variables)
    bpy.utils.register_class(PROMPTS_Door_Prompts)
    bpy.utils.register_class(PROMPTS_Drawer_Prompts)
    bpy.utils.register_class(PROMPTS_Hamper_Prompts)
    bpy.utils.register_class(OPERATOR_Update_Project)
    bpy.utils.register_class(OPERATOR_Update_Selection)
    bpy.utils.register_class(OPERATOR_Place_Applied_Panel)
    
    bpy.types.Scene.lm_exteriors = bpy.props.PointerProperty(type = PROPERTIES_Scene_Variables)
    
    pcoll = bpy.utils.previews.new()
    pcoll.my_previews_dir = ""
    pcoll.my_previews = ()

    preview_collections["main"] = pcoll
    
def unregister():
    bpy.utils.unregister_class(PROPERTIES_Scene_Variables)
    bpy.utils.unregister_class(PROMPTS_Door_Prompts)
    bpy.utils.unregister_class(PROMPTS_Drawer_Prompts)
    bpy.utils.unregister_class(PROMPTS_Hamper_Prompts)
    bpy.utils.unregister_class(OPERATOR_Update_Project)
    bpy.utils.unregister_class(OPERATOR_Update_Selection)
    bpy.utils.unregister_class(OPERATOR_Place_Applied_Panel)
    
    