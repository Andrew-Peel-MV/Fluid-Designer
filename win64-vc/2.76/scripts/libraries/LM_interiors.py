"""
Microvellum 
Interiors
Stores the logic and insert defs for all interior components for cabinets and closets.
Shelves, Dividers, Divisions, Rollouts, Wire Baskets, Hanging Rods
"""

import bpy
import fd
import math
import LM_drawer_boxes

HIDDEN_FOLDER_NAME = "_HIDDEN"
PART_WITH_EDGEBANDING = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Cut Parts","Part with Edgebanding")
PART_WITH_FRONT_EDGEBANDING = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Cut Parts","Part with Front Edgebanding")
ADJ_MACHINING = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Machining","Adjustable Shelf Holes")
DRAWER_BOX = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Drawer Boxes","Wood Drawer Box")
WIRE_BASKET = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Hardware","Wire Basket")
ROUND_HANGING_ROD = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Hardware","Hang Rod Round")
OVAL_HANGING_ROD = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Hardware","Hang Rod Oval")
SPACER = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Hardware","Spacer")

EXPOSED_CABINET_MATERIAL = ("Plastics","White Melamine")
UNEXPOSED_CABINET_MATERIAL = ("Wood","Wood Core","Particle Board")
SEMI_EXPOSED_CABINET_MATERIAL = ("Plastics","White Melamine")

#---------SPEC GROUP POINTERS

class Material_Pointers():
    
    Exposed_Interior_Surface = fd.Material_Pointer(EXPOSED_CABINET_MATERIAL)

    Semi_Exposed_Surface = fd.Material_Pointer(SEMI_EXPOSED_CABINET_MATERIAL)
    
    Exposed_Interior_Edge = fd.Material_Pointer(EXPOSED_CABINET_MATERIAL)

    Semi_Exposed_Edge = fd.Material_Pointer(SEMI_EXPOSED_CABINET_MATERIAL)
    
    Concealed_Surface = fd.Material_Pointer(UNEXPOSED_CABINET_MATERIAL)

    Concealed_Edge = fd.Material_Pointer(UNEXPOSED_CABINET_MATERIAL)

class Cutpart_Pointers():
    
    Base_Adjustable_Shelf = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                            core="Concealed_Surface",
                                            top="Semi_Exposed_Surface",
                                            bottom="Semi_Exposed_Surface")

    Base_Adjustable_Shelf_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                                 core="Concealed_Surface",
                                                 top="Exposed_Interior_Surface",
                                                 bottom="Exposed_Interior_Surface")

    Tall_Adjustable_Shelf = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                            core="Concealed_Surface",
                                            top="Semi_Exposed_Surface",
                                            bottom="Semi_Exposed_Surface")

    Tall_Adjustable_Shelf_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                                 core="Concealed_Surface",
                                                 top="Exposed_Interior_Surface",
                                                 bottom="Exposed_Interior_Surface")

    Upper_Adjustable_Shelf = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                             core="Concealed_Surface",
                                             top="Semi_Exposed_Surface",
                                             bottom="Semi_Exposed_Surface")

    Upper_Adjustable_Shelf_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                                  core="Concealed_Surface",
                                                  top="Exposed_Interior_Surface",
                                                  bottom="Exposed_Interior_Surface")
    
    Base_Fixed_Shelf = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                       core="Concealed_Surface",
                                       top="Semi_Exposed_Surface",
                                       bottom="Semi_Exposed_Surface")

    Base_Fixed_Shelf_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                            core="Concealed_Surface",
                                            top="Exposed_Interior_Surface",
                                            bottom="Exposed_Interior_Surface")

    Tall_Fixed_Shelf = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                       core="Concealed_Surface",
                                       top="Semi_Exposed_Surface",
                                       bottom="Semi_Exposed_Surface")

    Tall_Fixed_Shelf_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                            core="Concealed_Surface",
                                            top="Exposed_Interior_Surface",
                                            bottom="Exposed_Interior_Surface")

    Upper_Fixed_Shelf = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                        core="Concealed_Surface",
                                        top="Semi_Exposed_Surface",
                                        bottom="Semi_Exposed_Surface")

    Upper_Fixed_Shelf_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                             core="Concealed_Surface",
                                             top="Exposed_Interior_Surface",
                                             bottom="Exposed_Interior_Surface")
    
    Base_Division = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                    core="Concealed_Surface",
                                    top="Semi_Exposed_Surface",
                                    bottom="Semi_Exposed_Surface")

    Base_Division_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                         core="Concealed_Surface",
                                         top="Exposed_Interior_Surface",
                                         bottom="Exposed_Interior_Surface")

    Tall_Division = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                    core="Concealed_Surface",
                                    top="Semi_Exposed_Surface",
                                    bottom="Semi_Exposed_Surface")

    Tall_Division_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                         core="Concealed_Surface",
                                         top="Exposed_Interior_Surface",
                                         bottom="Exposed_Interior_Surface")

    Upper_Division = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                     core="Concealed_Surface",
                                     top="Semi_Exposed_Surface",
                                     bottom="Semi_Exposed_Surface")

    Upper_Division_Open = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                          core="Concealed_Surface",
                                          top="Exposed_Interior_Surface",
                                          bottom="Exposed_Interior_Surface")
    
    Base_Divider = fd.Cutpart_Pointer(thickness=fd.inches(.25),
                                   core="Concealed_Surface",
                                   top="Semi_Exposed_Surface",
                                   bottom="Semi_Exposed_Surface")

    Base_Divider_Open = fd.Cutpart_Pointer(thickness=fd.inches(.25),
                                        core="Concealed_Surface",
                                        top="Exposed_Interior_Surface",
                                        bottom="Exposed_Interior_Surface")

    Tall_Divider = fd.Cutpart_Pointer(thickness=fd.inches(.25),
                                   core="Concealed_Surface",
                                   top="Semi_Exposed_Surface",
                                   bottom="Semi_Exposed_Surface")

    Tall_Divider_Open = fd.Cutpart_Pointer(thickness=fd.inches(.25),
                                        core="Concealed_Surface",
                                        top="Exposed_Interior_Surface",
                                        bottom="Exposed_Interior_Surface")

    Upper_Divider = fd.Cutpart_Pointer(thickness=fd.inches(.25),
                                    core="Concealed_Surface",
                                    top="Semi_Exposed_Surface",
                                    bottom="Semi_Exposed_Surface")

    Upper_Divider_Open = fd.Cutpart_Pointer(thickness=fd.inches(.25),
                                         core="Concealed_Surface",
                                         top="Exposed_Interior_Surface",
                                         bottom="Exposed_Interior_Surface")
    
class Edgepart_Pointers():
    
    Interior_Edges = fd.Edgepart_Pointer(thickness=fd.inches(.01),
                                      material="Semi_Exposed_Edge")

    Interior_Edges_Open = fd.Edgepart_Pointer(thickness=fd.inches(.01),
                                           material="Exposed_Interior_Edge")

#---------ASSEMBLY INSTRUCTIONS
    
class Shelves(fd.Library_Assembly):
    
    library_name = "Cabinet Interiors"
    type_assembly = "INSERT"
    placement_type = "INTERIOR"
    property_id = "interiors.shelf_prompt" #TODO: Create Prompts Page
    mirror_y = False
    
    carcass_type = "" # {Base, Tall, Upper, Sink, Suspended}
    open_name = ""
    shelf_qty = 1
    add_adjustable_shelves = True
    add_fixed_shelves = False
    
    def add_common_prompts(self):
        self.add_tab(name='Interior Options',tab_type='VISIBLE')
        self.add_tab(name='Formulas',tab_type='HIDDEN')

        self.add_prompt(name="Edgebanding Thickness",
                        prompt_type='DISTANCE',
                        value=fd.inches(.75),
                        tab_index=1)
    
        sgi = self.get_var('cabinetlib.spec_group_index','sgi')
    
        self.prompt('Edgebanding Thickness','EDGE_THICKNESS(sgi,"Interior_Edges' + self.open_name + '")',[sgi])
    
    def add_adj_prompts(self):
        g = bpy.context.scene.lm_interiors
        
        self.add_prompt(name="Adj Shelf Qty",
                        prompt_type='QUANTITY',
                        value=self.shelf_qty,
                        tab_index=0)
        
        self.add_prompt(name="Adj Shelf Setback",
                        prompt_type='DISTANCE',
                        value=g.Adj_Shelf_Setback,
                        tab_index=0)
        
        self.add_prompt(name="Space From Front",
                        prompt_type='DISTANCE',
                        value=fd.inches(1.5),
                        tab_index=0)
        
        self.add_prompt(name="Space From Rear",
                        prompt_type='DISTANCE',
                        value=fd.inches(1.5),
                        tab_index=0)
        
        self.add_prompt(name="Space From Top",
                        prompt_type='DISTANCE',
                        value=fd.inches(1.5),
                        tab_index=0)
        
        self.add_prompt(name="Space From Bottom",
                        prompt_type='DISTANCE',
                        value=fd.inches(1.5),
                        tab_index=0)
        
        self.add_prompt(name="Shelf Hole Spacing",
                        prompt_type='DISTANCE',
                        value=fd.inches(32/25.4),
                        tab_index=0)
        
        self.add_prompt(name="Shelf Clip Gap",
                        prompt_type='DISTANCE',
                        value=fd.inches(.125),
                        tab_index=0)

        self.add_prompt(name="Adjustable Shelf Thickness",
                        prompt_type='DISTANCE',
                        value=fd.inches(.75),
                        tab_index=1)
        
        self.add_prompt(name="Shelf Pin Quantity",
                        prompt_type='QUANTITY',
                        value=0,
                        tab_index=1)

        sgi = self.get_var('cabinetlib.spec_group_index','sgi')
        Adj_Shelf_Qty = self.get_var('Adj Shelf Qty')
        
        self.prompt('Adjustable Shelf Thickness','THICKNESS(sgi,"' + self.carcass_type + '_Adjustable_Shelf' + self.open_name + '")',[sgi])
        self.prompt('Shelf Pin Quantity','Adj_Shelf_Qty*4',[Adj_Shelf_Qty])
        
    def add_fixed_prompts(self):
        g = bpy.context.scene.lm_interiors

        self.add_prompt(name="Fixed Shelf Qty",
                        prompt_type='QUANTITY',
                        value=0,
                        tab_index=0)
        
        self.add_prompt(name="Fixed Shelf Setback",
                        prompt_type='DISTANCE',
                        value=g.Fixed_Shelf_Setback,
                        tab_index=0)
        
        self.add_prompt(name="Fixed Shelf Thickness",
                        prompt_type='DISTANCE',
                        value=fd.inches(.75),
                        tab_index=1)
        
        sgi = self.get_var('cabinetlib.spec_group_index','sgi')

        self.prompt('Fixed Shelf Thickness','THICKNESS(sgi,"' + self.carcass_type + '_Fixed_Shelf' + self.open_name + '")',[sgi])
        
    def add_advanced_frameless_prompts(self):
        self.add_prompt(name="Shelf Row Quantity",
                        prompt_type='QUANTITY',
                        value=0,
                        tab_index=0)
        
        adj_qty = self.get_var('Adj Shelf Qty','adj_qty')
        fixed_qty = self.get_var('Fixed Shelf Qty','fixed_qty')
        
        self.prompt('Shelf Row Quantity','IF(adj_qty>fixed_qty,adj_qty,fixed_qty)',[adj_qty,fixed_qty])
        
    def add_adjustable_shelves(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Adj_Shelf_Qty = self.get_var("Adj Shelf Qty")
        Adj_Shelf_Setback = self.get_var("Adj Shelf Setback")
        Adjustable_Shelf_Thickness = self.get_var("Adjustable Shelf Thickness")
        Shelf_Clip_Gap = self.get_var("Shelf Clip Gap")

        for i in range(1,6):
            spacing = '((Height-(Adjustable_Shelf_Thickness*Adj_Shelf_Qty))/(Adj_Shelf_Qty+1))'
            adj_shelf = self.add_assembly(PART_WITH_EDGEBANDING)
            adj_shelf.set_name("Adjustable Shelf")
            adj_shelf.x_loc('Shelf_Clip_Gap',[Shelf_Clip_Gap])
            adj_shelf.y_loc('Depth',[Depth])
            adj_shelf.z_loc('(' + spacing + ')*IF(' + str(i) + '>Adj_Shelf_Qty,0,' + str(i) + ')+IF(' + str(i) + '>Adj_Shelf_Qty,0,Adjustable_Shelf_Thickness*' + str(i - 1) + ')',
                            [Height,Adjustable_Shelf_Thickness,Adj_Shelf_Qty])
            adj_shelf.x_rot(value = 0)
            adj_shelf.y_rot(value = 0)
            adj_shelf.z_rot(value = 0)
            adj_shelf.x_dim('Width-(Shelf_Clip_Gap*2)',[Width,Shelf_Clip_Gap])
            adj_shelf.y_dim('-Depth+Adj_Shelf_Setback',[Depth,Adj_Shelf_Setback])
            adj_shelf.z_dim('Adjustable_Shelf_Thickness',[Adjustable_Shelf_Thickness])
            adj_shelf.prompt('Hide','IF(' + str(i) + '>Adj_Shelf_Qty,True,False)',[Adj_Shelf_Qty])
            adj_shelf.cutpart(self.carcass_type + "_Adjustable_Shelf")
            adj_shelf.edgebanding('Interior_Edges',l1 = True, w1 = True, l2 = True, w2 = True)
            
    def add_adjustable_shelf_holes(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Adj_Shelf_Setback = self.get_var("Adj Shelf Setback")
        Space_From_Front = self.get_var("Space From Front")
        Space_From_Rear = self.get_var("Space From Rear")
        Space_From_Top = self.get_var("Space From Top")
        Space_From_Bottom = self.get_var("Space From Bottom")
        Shelf_Hole_Spacing = self.get_var("Shelf Hole Spacing")
        Adj_Shelf_Qty = self.get_var("Adj Shelf Qty")
        
        shelf_holes = self.add_assembly(ADJ_MACHINING)
        shelf_holes.set_name("Adjustable Shelf Holes")
        shelf_holes.x_loc(value = 0)
        shelf_holes.y_loc('Adj_Shelf_Setback',[Adj_Shelf_Setback])
        shelf_holes.z_loc('',[])
        shelf_holes.x_rot(value = 0)
        shelf_holes.y_rot(value = 0)
        shelf_holes.z_rot(value = 0)
        shelf_holes.x_dim('Width',[Width])
        shelf_holes.y_dim('Depth-Adj_Shelf_Setback',[Depth,Adj_Shelf_Setback])
        shelf_holes.z_dim('Height',[Height])
        shelf_holes.prompt('Hide','IF(Adj_Shelf_Qty>0,False,True)',[Adj_Shelf_Qty])
        shelf_holes.prompt('Space From Bottom','Space_From_Bottom',[Space_From_Bottom])
        shelf_holes.prompt('Space From Top','Space_From_Top',[Space_From_Top])
        shelf_holes.prompt('Space From Front','Space_From_Front',[Space_From_Front])
        shelf_holes.prompt('Space From Rear','Space_From_Rear',[Space_From_Rear])
        shelf_holes.prompt('Shelf Hole Spacing','Shelf_Hole_Spacing',[Shelf_Hole_Spacing])
        
    def add_fixed_shelves(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Fixed_Shelf_Qty = self.get_var("Fixed Shelf Qty")
        Fixed_Shelf_Setback = self.get_var("Fixed Shelf Setback")
        Fixed_Shelf_Thickness = self.get_var("Fixed Shelf Thickness")

        for i in range(1,6):
            spacing = '((Height-(Fixed_Shelf_Thickness*Fixed_Shelf_Qty))/(Fixed_Shelf_Qty+1))'
            fix_shelf = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
            fix_shelf.set_name("Fixed Shelf")
            fix_shelf.x_loc(value = 0)
            fix_shelf.y_loc('Depth',[Depth])
            fix_shelf.z_loc('(' + spacing + ')*IF(' + str(i) + '>Fixed_Shelf_Qty,0,' + str(i) + ')+IF(' + str(i) + '>Fixed_Shelf_Qty,0,Fixed_Shelf_Thickness*' + str(i - 1) + ')',
                            [Height,Fixed_Shelf_Thickness,Fixed_Shelf_Qty])
            fix_shelf.x_rot(value = 0)
            fix_shelf.y_rot(value = 0)
            fix_shelf.z_rot(value = 0)
            fix_shelf.x_dim('Width',[Width])
            fix_shelf.y_dim('-Depth+Fixed_Shelf_Setback',[Depth,Fixed_Shelf_Setback])
            fix_shelf.z_dim('Fixed_Shelf_Thickness',[Fixed_Shelf_Thickness])
            fix_shelf.prompt('Hide','IF(' + str(i) + '>Fixed_Shelf_Qty,True,False)',[Fixed_Shelf_Qty])
            fix_shelf.cutpart(self.carcass_type + "_Fixed_Shelf")
            fix_shelf.edgebanding('Interior_Edges',l1 = True)
            
    def draw(self):
        self.create_assembly()
        
        self.add_common_prompts()
        
        if self.add_adjustable_shelves:
            self.add_adj_prompts()
            self.add_adjustable_shelves()
            self.add_adjustable_shelf_holes()
            
        if self.add_fixed_shelves:
            self.add_fixed_prompts()
            self.add_fixed_shelves()
            
        if self.add_adjustable_shelves and self.add_fixed_shelves:
            self.add_advanced_frameless_prompts()
            
        self.update()
        
class Dividers(fd.Library_Assembly):
    
    library_name = "Cabinet Interiors"
    type_assembly = "INSERT"
    placement_type = "INTERIOR"
    property_id = "" #TODO: Create Prompts Page
    mirror_y = False
    
    carcass_type = "" # {Base, Tall, Upper, Sink, Suspended}
    open_name = ""
    shelf_qty = 1
    add_adjustable_shelves = True
    add_fixed_shelves = False
    
    def add_common_prompts(self):
        self.add_tab(name='Interior Options',tab_type='VISIBLE')
        self.add_tab(name='Formulas',tab_type='HIDDEN')

        self.add_prompt(name="Fixed Shelf Qty",prompt_type='QUANTITY',value=self.shelf_qty,tab_index=0)
        self.add_prompt(name="Divider Qty Per Row",prompt_type='QUANTITY',value=2,tab_index=0)
        self.add_prompt(name="Divider Setback",prompt_type='DISTANCE',value=fd.inches(0.25),tab_index=0)
        
        self.add_prompt(name="Shelf Setback",prompt_type='DISTANCE',value=0,tab_index=1)
        self.add_prompt(name="Shelf Thickness",prompt_type='DISTANCE',value=fd.inches(0.75),tab_index=1)
        self.add_prompt(name="Divider Thickness",prompt_type='DISTANCE',value=fd.inches(0.25),tab_index=1)

        self.add_prompt(name="Edgebanding Thickness",
                        prompt_type='DISTANCE',
                        value=fd.inches(.75),
                        tab_index=1)
    
        sgi = self.get_var('cabinetlib.spec_group_index','sgi')
        
        self.prompt('Divider Thickness','THICKNESS(sgi,"Base_Divider' + self.open_name +'")',[sgi])
        self.prompt('Shelf Thickness','THICKNESS(sgi,"Base_Fixed_Shelf' + self.open_name +'")',[sgi])
        self.prompt('Edgebanding Thickness','EDGE_THICKNESS(sgi,"Interior_Edges' + self.open_name + '")',[sgi])
    
    def add_dividers(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Shelf_Thickness = self.get_var('Shelf Thickness')
        Shelf_Setback = self.get_var('Shelf Setback')
        Divider_Setback = self.get_var('Divider Setback')
        Divider_Thickness = self.get_var('Divider Thickness')
        Fixed_Shelf_Qty = self.get_var('Fixed Shelf Qty')
        Divider_Qty_Per_Row = self.get_var('Divider Qty Per Row')

        divider = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        divider.set_name("Divider")
        divider.x_loc("Width-(Width/(Divider_Qty_Per_Row+1))+(Divider_Thickness/2)",[Width,Divider_Thickness,Divider_Qty_Per_Row])
        divider.y_loc("Depth",[Depth])
        divider.z_loc(value = 0)
        divider.x_rot(value = 0)
        divider.y_rot(value = -90)
        divider.z_rot(value = 0)
        divider.x_dim("(Height-(Shelf_Thickness*Fixed_Shelf_Qty))/(Fixed_Shelf_Qty+1)",[Height,Shelf_Thickness,Fixed_Shelf_Qty])
        divider.y_dim("(Depth*-1)+Divider_Setback+Shelf_Setback",[Depth,Divider_Setback,Shelf_Setback])
        divider.z_dim("Divider_Thickness",[Divider_Thickness])
        divider.prompt('Z Quantity','Divider_Qty_Per_Row',[Divider_Qty_Per_Row])
        divider.prompt('Z Offset','Width/(Divider_Qty_Per_Row+1)',[Width,Divider_Qty_Per_Row])
        divider.prompt('X Quantity','Fixed_Shelf_Qty+1',[Fixed_Shelf_Qty])
        divider.prompt('X Offset','Height/(Fixed_Shelf_Qty+1)+(Shelf_Thickness/(Fixed_Shelf_Qty+1))',[Height,Fixed_Shelf_Qty,Shelf_Thickness])
        divider.cutpart(self.carcass_type + "_Divider")
        divider.edgebanding('Interior_Edges',l1 = True)
        
    def add_fixed_shelves(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Fixed_Shelf_Qty = self.get_var("Fixed Shelf Qty")
        Shelf_Setback = self.get_var("Shelf Setback")
        Shelf_Thickness = self.get_var("Shelf Thickness")

        fix_shelf = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        fix_shelf.set_name("Fixed Shelf")
        fix_shelf.y_loc("Depth",[Depth])
        fix_shelf.z_loc("(Height-(Shelf_Thickness*Fixed_Shelf_Qty))/(Fixed_Shelf_Qty+1)",[Height,Shelf_Thickness,Fixed_Shelf_Qty])
        fix_shelf.x_dim("Width",[Width])
        fix_shelf.y_dim("(Depth*-1)+Shelf_Setback",[Depth,Shelf_Setback])
        fix_shelf.z_dim("Shelf_Thickness",[Shelf_Thickness])
        fix_shelf.prompt('Z Quantity','Fixed_Shelf_Qty',[Fixed_Shelf_Qty])
        fix_shelf.prompt('Z Offset','Height/(Fixed_Shelf_Qty+1)+(Shelf_Thickness/(Fixed_Shelf_Qty+1))',[Height,Fixed_Shelf_Qty,Shelf_Thickness])
        fix_shelf.cutpart(self.carcass_type + "_Fixed_Shelf")
        fix_shelf.edgebanding('Interior_Edges',l1 = True)

    def draw(self):
        self.create_assembly()
        
        self.add_common_prompts()
        self.add_fixed_shelves()
        self.add_dividers()
        
        self.update()
        
class Divisions(fd.Library_Assembly):
    
    library_name = "Cabinet Interiors"
    type_assembly = "INSERT"
    placement_type = "INTERIOR"
    property_id = "" #TODO: Create Prompts Page
    mirror_y = False
    
    carcass_type = "" # Base, Tall, Upper, Sink, Suspended
    open_name = ""
    shelf_qty = 1
    add_adjustable_shelves = True
    add_fixed_shelves = False
    
    def add_common_prompts(self):
        self.add_tab(name='Interior Options',tab_type='VISIBLE')
        self.add_tab(name='Formulas',tab_type='HIDDEN')

        self.add_prompt(name="Division Qty",prompt_type='QUANTITY',value=2,tab_index=0)
        self.add_prompt(name="Division Setback",prompt_type='DISTANCE',value=fd.inches(0.25),tab_index=0)
        self.add_prompt(name="Adj Shelf Rows",prompt_type='QUANTITY',value=2,tab_index=0)
        self.add_prompt(name="Fixed Shelf Rows",prompt_type='QUANTITY',value=0,tab_index=0)
        
        self.add_prompt(name="Division Thickness",prompt_type='DISTANCE',value=fd.inches(0.75),tab_index=1)
        self.add_prompt(name="Shelf Setback",prompt_type='DISTANCE',value=fd.inches(0.25),tab_index=1)
        self.add_prompt(name="Shelf Holes Space From Bottom",prompt_type='DISTANCE',value=fd.inches(2.5),tab_index=1)
        self.add_prompt(name="Shelf Holes Space From Top",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        self.add_prompt(name="Shelf Holes Front Setback",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        self.add_prompt(name="Shelf Holes Rear Setback",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        self.add_prompt(name="Adjustable Shelf Thickness",prompt_type='DISTANCE',value=fd.inches(0.75),tab_index=1)
        self.add_prompt(name="Fixed Shelf Thickness",prompt_type='DISTANCE',value=fd.inches(0.75),tab_index=1)
        self.add_prompt(name="Shelf Clip Gap",prompt_type='DISTANCE',value=fd.inches(0.125),tab_index=1)
        self.add_prompt(name="Shelf Hole Spacing",prompt_type='DISTANCE',value=fd.inches(1.25),tab_index=1)
        self.add_prompt(name="Shelf Pin Quantity",prompt_type='QUANTITY',value=0,tab_index=1)
        
        sgi = self.get_var('cabinetlib.spec_group_index','sgi')
        Adj_Shelf_Rows = self.get_var('Adj Shelf Rows')
        Division_Qty = self.get_var('Division Qty')
        
        self.prompt('Shelf Pin Quantity','(Adj_Shelf_Rows*Division_Qty)*4',[Adj_Shelf_Rows,Division_Qty])
        self.prompt('Division Thickness','THICKNESS(sgi,"Base_Division' + self.open_name +'")',[sgi])
        self.prompt('Fixed Shelf Thickness','THICKNESS(sgi,"Base_Fixed_Shelf' + self.open_name +'")',[sgi])
        self.prompt('Adjustable Shelf Thickness','THICKNESS(sgi,"Base_Adjustable_Shelf' + self.open_name +'")',[sgi])
    
    def add_divisions(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Division_Qty = self.get_var('Division Qty')   
        Division_Thickness = self.get_var('Division Thickness')  
        Division_Setback = self.get_var('Division Setback') 
        
        #LOGIC
        division = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        division.set_name("Divider")
        division.x_loc("Width-(Width-(Division_Thickness*Division_Qty))/(Division_Qty+1)",[Width,Division_Thickness,Division_Qty])
        division.y_loc("Depth",[Depth])
        division.z_loc(value = 0)
        division.x_rot(value = 0)
        division.y_rot(value = -90)
        division.z_rot(value = 0)
        division.x_dim("Height",[Height])
        division.y_dim("(Depth*-1)+Division_Setback",[Depth,Division_Setback])
        division.z_dim("Division_Thickness",[Division_Thickness])
        division.prompt('Hide','IF(Division_Qty==0,True,False)',[Division_Qty])
        division.prompt('Z Quantity','Division_Qty',[Division_Qty])
        division.prompt('Z Offset','((Width-(Division_Thickness*Division_Qty))/(Division_Qty+1))+Division_Thickness',[Division_Qty,Width,Division_Thickness])
        division.cutpart(self.carcass_type + "_Division")
        division.edgebanding('Interior_Edges',l1 = True)

    def add_fixed_shelves(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Division_Qty = self.get_var('Division Qty')   
        Division_Thickness = self.get_var('Division Thickness')  
        Division_Setback = self.get_var('Division Setback') 
        Shelf_Setback = self.get_var('Shelf Setback')
        Fixed_Shelf_Rows = self.get_var('Fixed Shelf Rows')
        Fixed_Shelf_Thickness = self.get_var('Fixed Shelf Thickness')
        
        fix_shelf = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        fix_shelf.set_name("Fixed Shelf")
        fix_shelf.x_loc(value = 0)
        fix_shelf.y_loc("Depth",[Depth]) 
        fix_shelf.z_loc("(Height-(Fixed_Shelf_Thickness*Fixed_Shelf_Rows))/(Fixed_Shelf_Rows+1)",[Height,Fixed_Shelf_Thickness,Fixed_Shelf_Rows]) 
        fix_shelf.x_rot(value = 0)
        fix_shelf.y_rot(value = 0)
        fix_shelf.z_rot(value = 0)
        fix_shelf.x_dim("(Width-(Division_Thickness*Division_Qty))/(Division_Qty+1)",[Width,Division_Qty,Division_Thickness]) 
        fix_shelf.y_dim("(Depth*-1)+Shelf_Setback+Division_Setback",[Shelf_Setback,Depth,Division_Setback]) 
        fix_shelf.z_dim("Fixed_Shelf_Thickness",[Fixed_Shelf_Thickness]) 
        fix_shelf.prompt('Hide','IF(Fixed_Shelf_Rows==0,True,False)',[Fixed_Shelf_Rows])
        fix_shelf.prompt('Z Quantity','Fixed_Shelf_Rows',[Fixed_Shelf_Rows])
        fix_shelf.prompt('Z Offset','Height/(Fixed_Shelf_Rows+1)+(Fixed_Shelf_Thickness/(Fixed_Shelf_Rows+1))',[Height,Fixed_Shelf_Thickness,Fixed_Shelf_Rows])
        fix_shelf.prompt('X Quantity','Division_Qty+1',[Division_Qty])
        fix_shelf.prompt('X Offset','((Width-(Division_Thickness*Division_Qty))/(Division_Qty+1))+Division_Thickness',[Width,Division_Qty,Division_Thickness])
        fix_shelf.cutpart(self.carcass_type + "_Fixed_Shelf")
        fix_shelf.edgebanding('Interior_Edges',l1 = True)

    def add_adj_shelves(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Division_Qty = self.get_var('Division Qty')   
        Division_Thickness = self.get_var('Division Thickness')  
        Division_Setback = self.get_var('Division Setback') 
        Shelf_Clip_Gap = self.get_var('Shelf Clip Gap') 
        Shelf_Setback = self.get_var('Shelf Setback')
        Adj_Shelf_Rows = self.get_var('Adj Shelf Rows')
        Adjustable_Shelf_Thickness = self.get_var('Adjustable Shelf Thickness')
        
        adj_shelf = self.add_assembly(PART_WITH_EDGEBANDING)
        adj_shelf.set_name("Adjustable Shelf")
        adj_shelf.x_loc("Shelf_Clip_Gap",[Shelf_Clip_Gap])
        adj_shelf.y_loc("Depth",[Depth])
        adj_shelf.z_loc("(Height-(Adjustable_Shelf_Thickness*Adj_Shelf_Rows))/(Adj_Shelf_Rows+1)",[Height,Adjustable_Shelf_Thickness,Adj_Shelf_Rows])
        adj_shelf.x_rot(value = 0)
        adj_shelf.y_rot(value = 0)
        adj_shelf.z_rot(value = 0)
        adj_shelf.x_dim("(Width-(Division_Thickness*Division_Qty)-((Shelf_Clip_Gap*2)*(Division_Qty+1)))/(Division_Qty+1)",[Width,Division_Qty,Division_Thickness,Shelf_Clip_Gap])
        adj_shelf.y_dim("(Depth*-1)+Shelf_Setback+Division_Setback",[Depth,Shelf_Setback,Division_Setback])
        adj_shelf.z_dim("Adjustable_Shelf_Thickness",[Adjustable_Shelf_Thickness])
        adj_shelf.prompt('Hide','IF(Adj_Shelf_Rows==0,True,False)',[Adj_Shelf_Rows])
        adj_shelf.prompt('Z Quantity','Adj_Shelf_Rows',[Adj_Shelf_Rows])
        adj_shelf.prompt('Z Offset','Height/(Adj_Shelf_Rows+1)+(Adjustable_Shelf_Thickness/(Adj_Shelf_Rows+1))',[Adj_Shelf_Rows,Height,Adjustable_Shelf_Thickness])
        adj_shelf.prompt('X Quantity','Division_Qty+1',[Division_Qty])
        adj_shelf.prompt('X Offset','((Width-(Division_Thickness*Division_Qty)-((Shelf_Clip_Gap*2)*(Division_Qty+1)))/(Division_Qty+1))+(Shelf_Clip_Gap*2)+Division_Thickness',[Width,Division_Thickness,Division_Qty,Shelf_Clip_Gap])
        adj_shelf.cutpart(self.carcass_type + "_Adjustable_Shelf")
        adj_shelf.edgebanding('Interior_Edges',l1 = True, w1 = True, l2 = True, w2 = True)

    def add_adj_shelf_machining(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Division_Qty = self.get_var('Division Qty')   
        Division_Thickness = self.get_var('Division Thickness')  
        Division_Setback = self.get_var('Division Setback') 
        Shelf_Setback = self.get_var('Shelf Setback')
        Adj_Shelf_Rows = self.get_var('Adj Shelf Rows')

        holes = self.add_assembly(ADJ_MACHINING)
        holes.set_name("Adjustable Shelf Holes")
        holes.x_loc(value = 0)
        holes.y_loc("Division_Setback+Shelf_Setback",[Division_Setback,Shelf_Setback])
        holes.z_loc(value = 0)
        holes.x_rot(value = 0)
        holes.y_rot(value = 0)
        holes.z_rot(value = 0)
        holes.x_dim("(Width-(Division_Thickness*Division_Qty))/(Division_Qty+1)",[Width,Division_Thickness,Division_Qty])
        holes.y_dim("fabs(Depth)-Division_Setback-Shelf_Setback",[Depth,Division_Setback,Shelf_Setback])
        holes.z_dim("Height",[Height])
        holes.prompt('Hide','IF(Adj_Shelf_Rows==0,True,False)',[Adj_Shelf_Rows])
        holes.prompt('Opening Quantity','Division_Qty+1',[Division_Qty])
        holes.prompt('Opening X Offset','(Width-(Division_Thickness*Division_Qty))/(Division_Qty+1)+Division_Thickness',[Width,Division_Thickness,Division_Qty])

    def draw(self):
        self.create_assembly()
        
        self.add_common_prompts()
        self.add_divisions()
        self.add_fixed_shelves()
        self.add_adj_shelves()
#         self.add_adj_shelf_machining()
        
        self.update()
        
class Rollouts(fd.Library_Assembly):
    
    library_name = "Cabinet Interiors"
    type_assembly = "INSERT"
    placement_type = "INTERIOR"
    property_id = "" #TODO: Create Prompts Page
    mirror_y = False
    
    rollout_qty = 3
    
    def draw(self):
        self.create_assembly()

        self.add_tab(name='Rollout Options',tab_type='VISIBLE')
        
        self.add_prompt(name="Rollout Quantity",
                        prompt_type='QUANTITY',
                        value=self.rollout_qty,
                        tab_index=0)
        
        self.add_prompt(name="Rollout 1 Z Dim",
                        prompt_type='DISTANCE',
                        value=fd.inches(4),
                        tab_index=0)
        
        self.add_prompt(name="Rollout 2 Z Dim",
                        prompt_type='DISTANCE',
                        value=fd.inches(4),
                        tab_index=0)
        
        self.add_prompt(name="Rollout 3 Z Dim",
                        prompt_type='DISTANCE',
                        value=fd.inches(4),
                        tab_index=0)
        
        self.add_prompt(name="Rollout 4 Z Dim",
                        prompt_type='DISTANCE',
                        value=fd.inches(4),
                        tab_index=0)
        
        self.add_prompt(name="Bottom Gap",
                        prompt_type='DISTANCE',
                        value=fd.inches(1.7),
                        tab_index=0)
        
        self.add_prompt(name="Drawer Box Slide Gap",
                        prompt_type='DISTANCE',
                        value=fd.inches(2),
                        tab_index=0)

        self.add_prompt(name="Rollout Setback",
                        prompt_type='DISTANCE',
                        value=fd.inches(.5),
                        tab_index=0)
        
        self.add_prompt(name="Distance Between Rollouts",
                        prompt_type='DISTANCE',
                        value=fd.inches(2),
                        tab_index=0)

        Width = self.get_var('dim_x','Width')
        Depth = self.get_var('dim_y','Depth')
        Rollout_1_Z_Dim = self.get_var('Rollout 1 Z Dim')
        Rollout_2_Z_Dim = self.get_var('Rollout 2 Z Dim')
        Rollout_3_Z_Dim = self.get_var('Rollout 3 Z Dim')
        Rollout_4_Z_Dim = self.get_var('Rollout 4 Z Dim')
        Bottom_Gap = self.get_var("Bottom Gap")
        Distance_Between_Rollouts = self.get_var("Distance Between Rollouts")
        Rollout_Quantity = self.get_var("Rollout Quantity")
        Rollout_Setback = self.get_var("Rollout Setback")
        Drawer_Box_Slide_Gap = self.get_var("Drawer Box Slide Gap")
        
        rollout_1 = LM_drawer_boxes.Wood_Drawer_Box()
        rollout_1.draw()
        rollout_1.obj_bp.parent = self.obj_bp
        rollout_1.set_name("Rollout 1")
        rollout_1.x_loc('Distance_Between_Rollouts',[Distance_Between_Rollouts])
        rollout_1.y_loc('Rollout_Setback',[Rollout_Setback])
        rollout_1.z_loc('Bottom_Gap',[Bottom_Gap])
        rollout_1.x_rot(value = 0)
        rollout_1.y_rot(value = 0)
        rollout_1.z_rot(value = 0)
        rollout_1.x_dim('Width-(Drawer_Box_Slide_Gap*2)',[Width,Drawer_Box_Slide_Gap])
        rollout_1.y_dim('Depth',[Depth])
        rollout_1.z_dim('Rollout_1_Z_Dim',[Rollout_1_Z_Dim])
        
        rollout_2 = LM_drawer_boxes.Wood_Drawer_Box()
        rollout_2.draw()
        rollout_2.obj_bp.parent = self.obj_bp
        rollout_2.set_name("Rollout 2")
        rollout_2.x_loc('Distance_Between_Rollouts',[Distance_Between_Rollouts])
        rollout_2.y_loc('Rollout_Setback',[Rollout_Setback])
        rollout_2.z_loc('Bottom_Gap+Rollout_1_Z_Dim+Distance_Between_Rollouts',[Bottom_Gap,Rollout_1_Z_Dim,Distance_Between_Rollouts])
        rollout_2.x_rot(value = 0)
        rollout_2.y_rot(value = 0)
        rollout_2.z_rot(value = 0)
        rollout_2.x_dim('Width-(Drawer_Box_Slide_Gap*2)',[Width,Drawer_Box_Slide_Gap])
        rollout_2.y_dim('Depth',[Depth])
        rollout_2.z_dim('Rollout_2_Z_Dim',[Rollout_2_Z_Dim])
        rollout_2.prompt('Hide','IF(Rollout_Quantity>1,False,True)',[Rollout_Quantity])
        
        rollout_3 = LM_drawer_boxes.Wood_Drawer_Box()
        rollout_3.draw()
        rollout_3.obj_bp.parent = self.obj_bp
        rollout_3.set_name("Rollout 3")
        rollout_3.x_loc('Distance_Between_Rollouts',[Distance_Between_Rollouts])
        rollout_3.y_loc('Rollout_Setback',[Rollout_Setback])
        rollout_3.z_loc('Bottom_Gap+Rollout_1_Z_Dim+Rollout_2_Z_Dim+(Distance_Between_Rollouts*2)',[Bottom_Gap,Rollout_1_Z_Dim,Rollout_2_Z_Dim,Distance_Between_Rollouts])
        rollout_3.x_rot(value = 0)
        rollout_3.y_rot(value = 0)
        rollout_3.z_rot(value = 0)
        rollout_3.x_dim('Width-(Drawer_Box_Slide_Gap*2)',[Width,Drawer_Box_Slide_Gap])
        rollout_3.y_dim('Depth',[Depth])
        rollout_3.z_dim('Rollout_3_Z_Dim',[Rollout_3_Z_Dim])
        rollout_3.prompt('Hide','IF(Rollout_Quantity>2,False,True)',[Rollout_Quantity])

        rollout_4 = LM_drawer_boxes.Wood_Drawer_Box()
        rollout_4.draw()
        rollout_4.obj_bp.parent = self.obj_bp
        rollout_4.set_name("Rollout 3")
        rollout_4.x_loc('Distance_Between_Rollouts',[Distance_Between_Rollouts])
        rollout_4.y_loc('Rollout_Setback',[Rollout_Setback])
        rollout_4.z_loc('Bottom_Gap+Rollout_1_Z_Dim+Rollout_2_Z_Dim+Rollout_3_Z_Dim+(Distance_Between_Rollouts*3)',[Bottom_Gap,Rollout_1_Z_Dim,Rollout_2_Z_Dim,Rollout_3_Z_Dim,Distance_Between_Rollouts])
        rollout_4.x_rot(value = 0)
        rollout_4.y_rot(value = 0)
        rollout_4.z_rot(value = 0)
        rollout_4.x_dim('Width-(Drawer_Box_Slide_Gap*2)',[Width,Drawer_Box_Slide_Gap])
        rollout_4.y_dim('Depth',[Depth])
        rollout_4.z_dim('Rollout_4_Z_Dim',[Rollout_4_Z_Dim])
        rollout_4.prompt('Hide','IF(Rollout_Quantity>3,False,True)',[Rollout_Quantity])

        self.update()

class Wire_Baskets(fd.Library_Assembly):
    
    library_name = "Cabinet Interiors"
    type_assembly = "INSERT"
    placement_type = "INTERIOR"
    property_id = "interiors.wire_baskets"
    mirror_y = False
    
    basket_qty = 3
    
    def draw(self):
        self.create_assembly()

        self.add_tab(name='Wire Basket Options',tab_type='VISIBLE')
        
        self.add_prompt(name="Open",
                        prompt_type='PERCENTAGE',
                        value=0,
                        tab_index=0)
        
        self.add_prompt(name="Basket Quantity",
                        prompt_type='QUANTITY',
                        value=self.basket_qty,
                        tab_index=0)
        
        self.add_prompt(name="Basket 1 Z Dim",
                        prompt_type='DISTANCE',
                        value=fd.inches(4),
                        tab_index=0)
        
        self.add_prompt(name="Basket 2 Z Dim",
                        prompt_type='DISTANCE',
                        value=fd.inches(4),
                        tab_index=0)
        
        self.add_prompt(name="Basket 3 Z Dim",
                        prompt_type='DISTANCE',
                        value=fd.inches(4),
                        tab_index=0)
        
        self.add_prompt(name="Basket 4 Z Dim",
                        prompt_type='DISTANCE',
                        value=fd.inches(4),
                        tab_index=0)
        
        self.add_prompt(name="Bottom Gap",
                        prompt_type='DISTANCE',
                        value=fd.inches(1.7),
                        tab_index=0)
        
        self.add_prompt(name="Distance Between Baskets",
                        prompt_type='DISTANCE',
                        value=fd.inches(2),
                        tab_index=0)
        
        self.add_prompt(name="Drawer Slide Quantity",prompt_type='QUANTITY',value=0,tab_index=1)

        Open = self.get_var('Open')
        Width = self.get_var('dim_x','Width')
        Depth = self.get_var('dim_y','Depth')
        Basket_1_Z_Dim = self.get_var('Basket 1 Z Dim')
        Basket_2_Z_Dim = self.get_var('Basket 2 Z Dim')
        Basket_3_Z_Dim = self.get_var('Basket 3 Z Dim')
        Basket_4_Z_Dim = self.get_var('Basket 4 Z Dim')
        Bottom_Gap = self.get_var("Bottom Gap")
        Distance_Between_Baskets = self.get_var("Distance Between Baskets")
        Basket_Quantity = self.get_var("Basket Quantity")

        basket_1 = self.add_assembly(WIRE_BASKET)
        basket_1.set_name("Basket 1")
        basket_1.x_loc(value = 0)
        basket_1.y_loc('-Depth*Open',[Open,Depth])
        basket_1.z_loc('Bottom_Gap',[Bottom_Gap])
        basket_1.x_rot(value = 0)
        basket_1.y_rot(value = 0)
        basket_1.z_rot(value = 0)
        basket_1.x_dim('Width',[Width])
        basket_1.y_dim('Depth',[Depth])
        basket_1.z_dim('Basket_1_Z_Dim',[Basket_1_Z_Dim])
        basket_1.material('Wire Basket')

        basket_2 = self.add_assembly(WIRE_BASKET)
        basket_2.set_name("Basket 2")
        basket_2.x_loc(value = 0)
        basket_2.y_loc('-Depth*Open',[Open,Depth])
        basket_2.z_loc('Bottom_Gap+Basket_1_Z_Dim+Distance_Between_Baskets',[Bottom_Gap,Basket_1_Z_Dim,Distance_Between_Baskets])
        basket_2.x_rot(value = 0)
        basket_2.y_rot(value = 0)
        basket_2.z_rot(value = 0)
        basket_2.x_dim('Width',[Width])
        basket_2.y_dim('Depth',[Depth])
        basket_2.z_dim('Basket_2_Z_Dim',[Basket_2_Z_Dim])
        basket_2.prompt('Hide','IF(Basket_Quantity>1,False,True)',[Basket_Quantity])
        basket_2.material('Wire Basket')
        
        basket_3 = self.add_assembly(WIRE_BASKET)
        basket_3.set_name("Basket 3")
        basket_3.x_loc(value = 0)
        basket_3.y_loc('-Depth*Open',[Open,Depth])
        basket_3.z_loc('Bottom_Gap+Basket_1_Z_Dim+Basket_2_Z_Dim+(Distance_Between_Baskets*2)',[Bottom_Gap,Basket_1_Z_Dim,Basket_2_Z_Dim,Distance_Between_Baskets])
        basket_3.x_rot(value = 0)
        basket_3.y_rot(value = 0)
        basket_3.z_rot(value = 0)
        basket_3.x_dim('Width',[Width])
        basket_3.y_dim('Depth',[Depth])
        basket_3.z_dim('Basket_3_Z_Dim',[Basket_3_Z_Dim])
        basket_3.prompt('Hide','IF(Basket_Quantity>2,False,True)',[Basket_Quantity])
        basket_3.material('Wire Basket')
        
        basket_4 = self.add_assembly(WIRE_BASKET)
        basket_4.set_name("Basket 3")
        basket_4.x_loc(value = 0)
        basket_4.y_loc('-Depth*Open',[Open,Depth])
        basket_4.z_loc('Bottom_Gap+Basket_1_Z_Dim+Basket_2_Z_Dim+Basket_3_Z_Dim+(Distance_Between_Baskets*3)',[Bottom_Gap,Basket_1_Z_Dim,Basket_2_Z_Dim,Basket_3_Z_Dim,Distance_Between_Baskets])
        basket_4.x_rot(value = 0)
        basket_4.y_rot(value = 0)
        basket_4.z_rot(value = 0)
        basket_4.x_dim('Width',[Width])
        basket_4.y_dim('Depth',[Depth])
        basket_4.z_dim('Basket_4_Z_Dim',[Basket_4_Z_Dim])
        basket_4.prompt('Hide','IF(Basket_Quantity>3,False,True)',[Basket_Quantity])
        basket_4.material('Wire Basket')
        
        self.update()

class Slanted_Shoe_Shelves(fd.Library_Assembly):

    #TODO: How should the angle of the shelves be calculated? Can the designer just set the value?
    #TODO: What is the maximum number of shelves possible
    #TODO: Add different Shelf Lip Types
    #TODO: What are the Profile shapes for Deco #100, #300, #400
    
    library_name = "Cabinet Interiors"
    property_id = "interiors.shelf_prompt"
    placement_type = "INTERIOR"
    type_assembly = "INSERT"
    mirror_y = False
    
    shelf_qty = 1
    add_adjustable_shelves = True
    add_fixed_shelves = False
    
    def add_common_prompts(self):
        self.add_tab(name='Slanted Shoe Options',tab_type='VISIBLE')
        self.add_tab(name='Formulas',tab_type='HIDDEN')

        self.add_prompt(name="Edgebanding Thickness",
                        prompt_type='DISTANCE',
                        value=fd.inches(.75),
                        tab_index=1)
    
        sgi = self.get_var('cabinetlib.spec_group_index','sgi')
    
        self.prompt('Edgebanding Thickness','EDGE_THICKNESS(sgi,"Interior_Edges")',[sgi])
    
    def add_adj_prompts(self):
        g = bpy.context.scene.lm_interiors
        
        self.add_prompt(name="Adj Shelf Qty",
                        prompt_type='QUANTITY',
                        value=self.shelf_qty,
                        tab_index=0)
        
        self.add_prompt(name="Adj Shelf Setback",
                        prompt_type='DISTANCE',
                        value=g.Adj_Shelf_Setback,
                        tab_index=0)
        
        self.add_prompt(name="Space From Front",
                        prompt_type='DISTANCE',
                        value=fd.inches(1.5),
                        tab_index=0)
        
        self.add_prompt(name="Space From Rear",
                        prompt_type='DISTANCE',
                        value=fd.inches(1.5),
                        tab_index=0)
        
        self.add_prompt(name="Space From Top",
                        prompt_type='DISTANCE',
                        value=fd.inches(1.5),
                        tab_index=0)
        
        self.add_prompt(name="Space From Bottom",
                        prompt_type='DISTANCE',
                        value=fd.inches(1.5),
                        tab_index=0)
        
        self.add_prompt(name="Shelf Hole Spacing",
                        prompt_type='DISTANCE',
                        value=fd.inches(32/25.4),
                        tab_index=0)
        
        self.add_prompt(name="Shelf Clip Gap",
                        prompt_type='DISTANCE',
                        value=fd.inches(.125),
                        tab_index=0)

        self.add_prompt(name="Shelf Angle",
                        prompt_type='ANGLE',
                        value=math.radians(20),
                        tab_index=0)

        self.add_prompt(name="Adjustable Shelf Thickness",
                        prompt_type='DISTANCE',
                        value=fd.inches(.75),
                        tab_index=1)

        sgi = self.get_var('cabinetlib.spec_group_index','sgi')

        self.prompt('Adjustable Shelf Thickness','THICKNESS(sgi,"Base_Adjustable_Shelf")',[sgi])
        
    def add_adjustable_shelves(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Adj_Shelf_Qty = self.get_var("Adj Shelf Qty")
        Adj_Shelf_Setback = self.get_var("Adj Shelf Setback")
        Adjustable_Shelf_Thickness = self.get_var("Adjustable Shelf Thickness")
        Shelf_Clip_Gap = self.get_var("Shelf Clip Gap")
        Shelf_Angle = self.get_var("Shelf Angle")

        for i in range(1,6):
            spacing = '((Height-(Adjustable_Shelf_Thickness*Adj_Shelf_Qty))/(Adj_Shelf_Qty+1))'
            adj_shelf = self.add_assembly(PART_WITH_EDGEBANDING)
            adj_shelf.set_name("Adjustable Shelf " + str(i))
            adj_shelf.x_loc('Shelf_Clip_Gap',[Shelf_Clip_Gap])
            adj_shelf.y_loc('Depth',[Depth])
            adj_shelf.z_loc('(' + spacing + ')*IF(' + str(i) + '>Adj_Shelf_Qty,0,' + str(i) + ')+IF(' + str(i) + '>Adj_Shelf_Qty,0,Adjustable_Shelf_Thickness*' + str(i - 1) + ')',
                            [Height,Adjustable_Shelf_Thickness,Adj_Shelf_Qty])
            adj_shelf.x_rot('Shelf_Angle',[Shelf_Angle])
            adj_shelf.y_rot(value = 0)
            adj_shelf.z_rot(value = 0)
            adj_shelf.x_dim('Width-(Shelf_Clip_Gap*2)',[Width,Shelf_Clip_Gap])
            adj_shelf.y_dim('-Depth+Adj_Shelf_Setback',[Depth,Adj_Shelf_Setback])
            adj_shelf.z_dim('Adjustable_Shelf_Thickness',[Adjustable_Shelf_Thickness])
            adj_shelf.prompt('Hide','IF(' + str(i) + '>Adj_Shelf_Qty,True,False)',[Adj_Shelf_Qty])
            adj_shelf.cutpart("Base_Adjustable_Shelf")
            adj_shelf.edgebanding('Interior_Edges',l1 = True, w1 = True, l2 = True, w2 = True)

            Z_Loc = adj_shelf.get_var('loc_z','Z_Loc')
            Shelf_Depth = adj_shelf.get_var('dim_y','Shelf_Depth')
                 
            shelf_lip = self.add_assembly(PART_WITH_EDGEBANDING)
            shelf_lip.set_name("Shelf Lip " + str(i))
            shelf_lip.x_loc('Shelf_Clip_Gap',[Shelf_Clip_Gap])
            shelf_lip.y_loc('fabs(Depth)-(fabs(Shelf_Depth)*cos(Shelf_Angle))',[Depth,Shelf_Depth,Shelf_Angle])
            shelf_lip.z_loc('Z_Loc-(fabs(Shelf_Depth)*sin(Shelf_Angle))',[Z_Loc,Shelf_Depth,Shelf_Angle])
            shelf_lip.x_rot('Shelf_Angle-radians(90)',[Shelf_Angle])
            shelf_lip.y_rot(value = 0)
            shelf_lip.z_rot(value = 0)
            shelf_lip.x_dim('Width-(Shelf_Clip_Gap*2)',[Width,Shelf_Clip_Gap])
            shelf_lip.y_dim(value = fd.inches(-2))
            shelf_lip.z_dim('-Adjustable_Shelf_Thickness',[Adjustable_Shelf_Thickness])
            shelf_lip.prompt('Hide','IF(' + str(i) + '>Adj_Shelf_Qty,True,False)',[Adj_Shelf_Qty])
            shelf_lip.cutpart("Base_Adjustable_Shelf")
            shelf_lip.edgebanding('Interior_Edges',l1 = True, w1 = True, l2 = True, w2 = True)
        
    def draw(self):
        self.create_assembly()
        
        self.add_common_prompts()
        
        self.add_adj_prompts()
        self.add_adjustable_shelves()
        
        self.update()

class Hanging_Rods(fd.Library_Assembly):
    
    library_name = "Cabinet Interiors"
    insert_type = "Interior"
    placement_type = "INTERIOR"
    type_assembly = "INSERT"
    mirror_y = False
    property_id = "interiors.hanging_rod_prompts"
    
    hanging_rod_qty = 1
    
    #TODO: Create OpenGL Call to ensure that there is at least 24" of room for clothes to hang
    #TODO: If section is not 12" deep then turn on another row of Shelf Holes at 12"
    
    def draw(self):
        self.create_assembly()

        self.add_tab(name='Hanging Options',tab_type='VISIBLE')
        self.add_prompt(name="Hanging Rod Type",prompt_type='COMBOBOX',value=0,items=['Round','Oval'],columns=2,tab_index=0)
        self.add_prompt(name="Hanging Rod Location From Top",prompt_type='DISTANCE',value=fd.inches(2.145),tab_index=0)
        self.add_prompt(name="Hanging Rod Setback",prompt_type='DISTANCE',value=fd.inches(2),tab_index=0)
        self.add_prompt(name="Hanging Rod Quantity",prompt_type='QUANTITY',value=self.hanging_rod_qty,tab_index=0)
        self.add_prompt(name="Hanging Rod Offset",prompt_type='DISTANCE',value=fd.inches(41.6),tab_index=0)
        
        Width = self.get_var('dim_x','Width')
        Depth = self.get_var('dim_y','Depth')
        Height = self.get_var('dim_z','Height')
        Z_Loc = self.get_var("Hanging Rod Location From Top",'Z_Loc')
        Z_Qty = self.get_var("Hanging Rod Quantity",'Z_Qty')
        Z_Offset = self.get_var("Hanging Rod Offset",'Z_Offset')
        Hanging_Rod_Type = self.get_var("Hanging Rod Type")
        Hanging_Rod_Setback = self.get_var("Hanging Rod Setback")
        
        rod = self.add_assembly(ROUND_HANGING_ROD)
        rod.set_name("Hanging Rod Round")
        rod.add_prompt(name="Hanging Rod Qty",prompt_type='DISTANCE',value=0,tab_index=0)
        rod.x_loc(value = 0)
        rod.y_loc('Hanging_Rod_Setback',[Hanging_Rod_Setback])
        rod.z_loc('Height-Z_Loc',[Height,Z_Loc])
        rod.x_rot(value = 0)
        rod.y_rot(value = 0)
        rod.z_rot(value = 0)
        rod.x_dim('Width',[Width])
        rod.y_dim('-Depth',[Depth])
        rod.z_dim(value = 0)
        rod.prompt("Z Quantity",'Z_Qty',[Z_Qty])
        rod.prompt("Z Offset",'Z_Offset',[Z_Offset])
        rod.prompt("Hide",'IF(Hanging_Rod_Type==0,False,True)',[Hanging_Rod_Type])
        rod.prompt('Hanging Rod Qty','Width*Z_Qty',[Width,Z_Qty])
        
        rod = self.add_assembly(OVAL_HANGING_ROD)
        rod.set_name("Hanging Rod Oval")
        rod.add_prompt(name="Hanging Rod Qty",prompt_type='DISTANCE',value=0,tab_index=0)
        rod.x_loc(value = 0)
        rod.y_loc('Hanging_Rod_Setback',[Hanging_Rod_Setback])
        rod.z_loc('Height-Z_Loc',[Height,Z_Loc])
        rod.x_rot(value = 0)
        rod.y_rot(value = 0)
        rod.z_rot(value = 0)
        rod.x_dim('Width',[Width])
        rod.y_dim('-Depth',[Depth])
        rod.z_dim(value = 0)
        rod.prompt("Z Quantity",'Z_Qty',[Z_Qty])
        rod.prompt("Z Offset",'Z_Offset',[Z_Offset])
        rod.prompt("Hide",'IF(Hanging_Rod_Type==1,False,True)',[Hanging_Rod_Type])
        rod.prompt('Hanging Rod Qty','Width*Z_Qty',[Width,Z_Qty])
        
        self.update()

#---------INSERTS
        
class INSERT_Shelves(Shelves):
    
    def __init__(self):
        g = bpy.context.scene.lm_interiors
        self.category_name = "Standard"
        self.assembly_name = "Shelves"
        self.carcass_type = "Base"
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        self.shelf_qty = 1
        
class INSERT_Base_Dividers(Dividers):
    
    def __init__(self):
        g = bpy.context.scene.lm_interiors
        self.category_name = "Standard"
        self.assembly_name = "Dividers"
        self.carcass_type = "Base"
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        self.shelf_qty = g.Base_Adj_Shelf_Qty

class INSERT_Base_Divisions(Divisions):
    
    def __init__(self):
        g = bpy.context.scene.lm_interiors
        self.category_name = "Standard"
        self.assembly_name = "Divisions"
        self.carcass_type = "Base"
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        self.shelf_qty = g.Base_Adj_Shelf_Qty

class INSERT_Rollouts(Rollouts):
    
    def __init__(self):
        g = bpy.context.scene.lm_interiors
        self.category_name = "Standard"
        self.assembly_name = "Rollouts"
        self.carcass_type = "Base"
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        self.rollout_qty = 2

class INSERT_Wire_Baskets(Wire_Baskets):
    
    def __init__(self):
        g = bpy.context.scene.lm_interiors
        self.category_name = "Standard"
        self.assembly_name = "Wire Baskets"
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)

class INSERT_Slanted_Shoe_Shelves(Slanted_Shoe_Shelves):
    
    def __init__(self):
        g = bpy.context.scene.lm_interiors
        self.category_name = "Standard"
        self.assembly_name = "Slanted Shoe Shelves"
        self.carcass_type = "Base"
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        self.shelf_qty = g.Base_Adj_Shelf_Qty
        
class INSERT_Hanging_Rod(Hanging_Rods):
    
    def __init__(self):
        g = bpy.context.scene.lm_interiors
        self.category_name = "Standard"
        self.assembly_name = "Hanging Rod"
        self.width = fd.inches(18)
        self.height = fd.inches(5)
        self.depth = fd.inches(23)
        self.hanging_rod_qty = 1
        
class INSERT_Double_Hanging_Rod(Hanging_Rods):
    
    def __init__(self):
        g = bpy.context.scene.lm_interiors
        self.category_name = "Standard"
        self.assembly_name = "Double Hanging Rod"
        self.width = fd.inches(18)
        self.height = fd.inches(60)
        self.depth = fd.inches(23)
        self.hanging_rod_qty = 2
        
#---------INTERFACES

class PROMPTS_Hanging_Rod_Prompts(bpy.types.Operator):
    bl_idname = "interiors.hanging_rod_prompts"
    bl_label = "Hanging Rod Prompts" 
    bl_description = "This shows all of the available hanging rod options"
    bl_options = {'UNDO'}
    
    object_name = bpy.props.StringProperty(name="Object Name")
    
    hanging_rod_type = bpy.props.EnumProperty(name="Hanging Rod Type",items=[('Round',"Round","Round"),
                                                                             ('Oval',"Oval","Oval")])
    
    assembly = None
    
    @classmethod
    def poll(cls, context):
        return True
        
    def check(self, context):
        hanging_rod_type = self.assembly.get_prompt("Hanging Rod Type")
        hanging_rod_type.set_value(self.hanging_rod_type) 
        self.assembly.obj_bp.location = self.assembly.obj_bp.location # Redraw Viewport
        return True
        
    def execute(self, context):
        return {'FINISHED'}
            
    def set_default_properties(self):
        hanging_rod_type = self.assembly.get_prompt("Hanging Rod Type")
        if hanging_rod_type:
            self.hanging_rod_type = hanging_rod_type.COL_EnumItem[hanging_rod_type.EnumIndex].name
            
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
                
                hanging_rod_quantity = self.assembly.get_prompt("Hanging Rod Quantity")
                hanging_rod_offset = self.assembly.get_prompt("Hanging Rod Offset")
                
                box = layout.box()
                row = box.row()
                row.label("Hanging Rod Type")
                row.prop(self,'hanging_rod_type',text="")
                row = box.row()
                row.label("Quantity")
                row.prop(hanging_rod_quantity,'QuantityValue',text="")
                row = box.row()
                row.label("Offset")
                row.prop(hanging_rod_offset,'DistanceValue',text="")
        
class PROMPTS_Shelf_Prompts(bpy.types.Operator):
    bl_idname = "interiors.shelf_prompt"
    bl_label = "Shelf Prompts" 
    bl_description = "This shows all of the available vertical splitter options"
    bl_options = {'UNDO'}
    
    object_name = bpy.props.StringProperty(name="Object Name")
    
    adj_shelf_qty = bpy.props.IntProperty(name="Adjustable Shelf Quantity",min=0,max=5)
    fix_shelf_qty = bpy.props.IntProperty(name="Fixed Shelf Quantity",min=0,max=5)
    
    adj_shelf_qty_prompt = None
    fix_shelf_qty_prompt = None
    
    assembly = None
    
    @classmethod
    def poll(cls, context):
        return True
        
    def check(self, context):
        fd.run_calculators(self.assembly.obj_bp)
        
        if self.adj_shelf_qty_prompt:
            self.adj_shelf_qty_prompt.set_value(self.adj_shelf_qty)
        
        if self.fix_shelf_qty_prompt:
            self.fix_shelf_qty_prompt.set_value(self.fix_shelf_qty)
            
        self.assembly.obj_bp.location = self.assembly.obj_bp.location # Redraw Viewport
        
        return True
        
    def execute(self, context):
        return {'FINISHED'}

    def invoke(self,context,event):
        obj = bpy.data.objects[self.object_name]
        obj_insert_bp = fd.get_bp(obj,'INSERT')
        self.assembly = fd.Assembly(obj_insert_bp)
        
        self.adj_shelf_qty_prompt = self.assembly.get_prompt("Adj Shelf Qty")
        self.fix_shelf_qty_prompt = self.assembly.get_prompt("Fixed Shelf Qty")

        if self.adj_shelf_qty_prompt:
            self.adj_shelf_qty = self.adj_shelf_qty_prompt.value()
        
        if self.fix_shelf_qty_prompt:
            self.fix_shelf_qty = self.fix_shelf_qty_prompt.value()
        
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=fd.get_prop_dialog_width(330))
        
    def draw(self, context):
        layout = self.layout
        if self.assembly.obj_bp:
            if self.assembly.obj_bp.name in context.scene.objects:
                
                if self.adj_shelf_qty_prompt:
                    adj_shelf_setback = self.assembly.get_prompt("Adj Shelf Setback")
                    shelf_angle = self.assembly.get_prompt("Shelf Angle")
                    box = layout.box()
                    row = box.row()
                    row.label("Adjustable Shelf Options:")
                    row = box.row()
                    row.prop(self,'adj_shelf_qty')
                    if self.adj_shelf_qty > 0:
                        row = box.row()
                        row.prop(adj_shelf_setback,'DistanceValue',text="Adj Shelf Setback")
                        row = box.row()
                    if shelf_angle:
                        row = box.row()
                        row.prop(shelf_angle,'AngleValue',text="Shelf Angle")
                        
                if self.fix_shelf_qty_prompt:
                    fix_shelf_setback = self.assembly.get_prompt("Fixed Shelf Setback")
                    box = layout.box()
                    row = box.row()
                    row.label("Fixed Shelf Options:")
                    row = box.row()
                    row.prop(self,'fix_shelf_qty')
                    if self.fix_shelf_qty > 0:
                        row = box.row()
                        row.prop(fix_shelf_setback,'DistanceValue',text="Fix Shelf Setback")
                        row = box.row()
                        
class PROMPTS_Wire_Baskets(bpy.types.Operator):
    bl_idname = "interiors.wire_baskets"
    bl_label = "Wire Basket Prompts" 
    bl_description = "This shows all of the available wire basket options"
    bl_options = {'UNDO'}
    
    object_name = bpy.props.StringProperty(name="Object Name")
    
    assembly = None
    
    @classmethod
    def poll(cls, context):
        return True
        
    def check(self, context):
        self.assembly.obj_bp.location = self.assembly.obj_bp.location # Redraw Viewport
        return True
        
    def execute(self, context):
        return {'FINISHED'}
    
    def invoke(self,context,event):
        obj = bpy.data.objects[self.object_name]
        obj_insert_bp = fd.get_bp(obj,'INSERT')
        self.assembly = fd.Assembly(obj_insert_bp)
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=fd.get_prop_dialog_width(330))
        
    def draw(self, context):
        layout = self.layout
        if self.assembly.obj_bp:
            if self.assembly.obj_bp.name in context.scene.objects:
                
                open_var = self.assembly.get_prompt("Open")
                qty = self.assembly.get_prompt("Basket Quantity")
                b1_z_dim = self.assembly.get_prompt("Basket 1 Z Dim")
                b2_z_dim = self.assembly.get_prompt("Basket 2 Z Dim")
                b3_z_dim = self.assembly.get_prompt("Basket 3 Z Dim")
                b4_z_dim = self.assembly.get_prompt("Basket 4 Z Dim")
                dist_between_baskets = self.assembly.get_prompt("Distance Between Baskets")
                bottom_gap = self.assembly.get_prompt("Bottom Gap")
                
                box = layout.box()
                row = box.row()
                row.label("Open")
                row.prop(open_var,'PercentageValue',text="")
                row = box.row()
                row.label("Quantity")
                row.prop(qty,'QuantityValue',text="")
                if qty.QuantityValue > 3:
                    row = box.row()
                    row.label("Basket 4 Height")
                    row.prop(b4_z_dim,'DistanceValue',text="")
                if qty.QuantityValue > 2:
                    row = box.row()
                    row.label("Basket 3 Height")
                    row.prop(b3_z_dim,'DistanceValue',text="")
                if qty.QuantityValue > 1:
                    row = box.row()
                    row.label("Basket 2 Height")
                    row.prop(b2_z_dim,'DistanceValue',text="")
                row = box.row()
                row.label("Basket 1 Height")
                row.prop(b1_z_dim,'DistanceValue',text="")
                row = box.row()
                row.label("Distance Between Baskets")
                row.prop(dist_between_baskets,'DistanceValue',text="")
                row = box.row()
                row.label("Bottom Gap")
                row.prop(bottom_gap,'DistanceValue',text="")
                
class PROMPTS_Shoe_Cubbies(bpy.types.Operator):
    bl_idname = "interiors.shoe_cubbies"
    bl_label = "Shoe Cubbies Prompts" 
    bl_description = "This shows all of the available shoe cubby options"
    bl_options = {'UNDO'}
    
    object_name = bpy.props.StringProperty(name="Object Name")
    
    assembly = None
    
    vertical_opening_space = 0
    horizontal_opening_space = 0
    
    @classmethod
    def poll(cls, context):
        return True
        
    def check(self, context):
        self.assembly.obj_bp.location = self.assembly.obj_bp.location # Redraw Viewport
        
        return True
        
    def execute(self, context):
        return {'FINISHED'}

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
                vert_qty = self.assembly.get_prompt("Vertical Quantity")
                horz_qty = self.assembly.get_prompt("Horizontal Quantity")
                setback = self.assembly.get_prompt("Cubby Setback")
                panel_thickness = self.assembly.get_prompt("Panel Thickness")
                
                layout.prop(vert_qty,'QuantityValue',text="Vertical Quantity")
                layout.prop(horz_qty,'QuantityValue',text="Horizontal Quantity")
                layout.prop(setback,'DistanceValue',text="Setback Amount")
                
                height = self.assembly.obj_z.location.z
                width = self.assembly.obj_x.location.x
                v_qty = vert_qty.QuantityValue
                h_qty = horz_qty.QuantityValue
                
                vertical_opening = (height - (panel_thickness.DistanceValue*h_qty))/(h_qty+1)
                horizontal_opening = (width - (panel_thickness.DistanceValue*v_qty))/(v_qty+1)
                
                layout.label("Shoe Cubby Vertical Opening Space: " + str(fd.unit(vertical_opening)) + '"')
                layout.label("Shoe Cubby Horizontal Opening Space: " + str(fd.unit(horizontal_opening)) + '"')

#         self.prompt("Vertical Spacing",'(Height-(Panel_Thickness*Horizontal_Quantity))/(Horizontal_Quantity+1)',[Height,Panel_Thickness,Horizontal_Quantity])
#         self.prompt("Horizontal Spacing",'(Width-(Panel_Thickness*Vertical_Quantity))/(Vertical_Quantity+1)',[Width,Panel_Thickness,Vertical_Quantity])

class PROPERTIES_Scene_Variables(bpy.types.PropertyGroup):
    Main_Tabs = bpy.props.EnumProperty(name="Main Tabs",
                                       items=[('SHELVES',"Shelves",'Adjustable and Fixed Shelf Options'),
                                              ('DIVIDERS',"Dividers",'Divider Options'),
                                              ('DIVISIONS',"Divisions",'Division Options'),
                                              ('ROLLOUTS',"Rollouts",'Rollout Options')],
                                       default = 'SHELVES')

    Base_Adj_Shelf_Qty = bpy.props.IntProperty(name="Base Adjustable Shelf Quantity",
                                               description="Default number of adjustable shelves for base cabinets",
                                               default=1)
    
    Tall_Adj_Shelf_Qty = bpy.props.IntProperty(name="Tall Adjustable Shelf Quantity",
                                               description="Default number of adjustable shelves for tall cabinets",
                                               default=4)
    
    Upper_Adj_Shelf_Qty = bpy.props.IntProperty(name="Upper Adjustable Shelf Quantity",
                                                description="Default number of adjustable shelves for upper cabinets",
                                                default=2)
    
    Adj_Shelf_Setback = bpy.props.FloatProperty(name="Adjustable Shelf Setback",
                                                description="This sets the default adjustable shelf setback",
                                                default=fd.inches(.25),
                                                unit='LENGTH')
    
    Fixed_Shelf_Setback = bpy.props.FloatProperty(name="Fixed Shelf Setback",
                                                  description="This sets the default fixed shelf setback",
                                                  default=fd.inches(.25),
                                                  unit='LENGTH')
    
    def draw(self,layout):
        box = layout.box()
        box.prop(self,"Base_Adj_Shelf_Qty")
        box.prop(self,"Tall_Adj_Shelf_Qty")
        box.prop(self,"Upper_Adj_Shelf_Qty")
        box.prop(self,"Adj_Shelf_Setback")
        box.prop(self,"Fixed_Shelf_Setback")

def register():
    bpy.utils.register_class(PROPERTIES_Scene_Variables)
    bpy.types.Scene.lm_interiors = bpy.props.PointerProperty(type = PROPERTIES_Scene_Variables)
    bpy.utils.register_class(PROMPTS_Hanging_Rod_Prompts)
    bpy.utils.register_class(PROMPTS_Shelf_Prompts)
    bpy.utils.register_class(PROMPTS_Wire_Baskets)
    bpy.utils.register_class(PROMPTS_Shoe_Cubbies)
    
def unregister():
    bpy.utils.unregister_class(PROPERTIES_Scene_Variables)
    bpy.utils.unregister_class(PROMPTS_Hanging_Rod_Prompts)
    bpy.utils.unregister_class(PROMPTS_Shelf_Prompts)
    bpy.utils.unregister_class(PROMPTS_Wire_Baskets)
    bpy.utils.unregister_class(PROMPTS_Shoe_Cubbies)
    