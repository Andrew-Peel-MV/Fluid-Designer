"""
Microvellum 
Splitters
Stores the logic and insert defs for the splitter library
"""

import bpy
import fd

HIDDEN_FOLDER_NAME = "_HIDDEN"
PART_WITH_EDGEBANDING = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Cut Parts","Part with Edgebanding")
PART_WITH_FRONT_EDGEBANDING = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Cut Parts","Part with Front Edgebanding")
ADJ_MACHINING = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Machining","Adjustable Shelf Holes")

EXPOSED_CABINET_MATERIAL = ("Wood","Wood Finished","Jarrah Legno")
UNEXPOSED_CABINET_MATERIAL = ("Wood","Wood Core","Particle Board")
SEMI_EXPOSED_CABINET_MATERIAL = ("Plastics","White Melamine")

#---------SPEC GROUP POINTERS

class Material_Pointers():
    
    Exposed_Exterior_Surface = fd.Material_Pointer(EXPOSED_CABINET_MATERIAL)
    
    Exposed_Interior_Surface = fd.Material_Pointer(EXPOSED_CABINET_MATERIAL)

    Semi_Exposed_Surface = fd.Material_Pointer(SEMI_EXPOSED_CABINET_MATERIAL)
    
    Exposed_Interior_Edge = fd.Material_Pointer(EXPOSED_CABINET_MATERIAL)

    Semi_Exposed_Edge = fd.Material_Pointer(SEMI_EXPOSED_CABINET_MATERIAL)
    
    Concealed_Surface = fd.Material_Pointer(UNEXPOSED_CABINET_MATERIAL)

    Concealed_Edge = fd.Material_Pointer(UNEXPOSED_CABINET_MATERIAL)

class Cutpart_Pointers():
    
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
    
    Frame = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                               core="Concealed_Surface",
                               top="Exposed_Interior_Surface",
                               bottom="Exposed_Interior_Surface")
    
class Edgepart_Pointers():
    
    Interior_Edges = fd.Edgepart_Pointer(thickness=fd.inches(.01),
                                         material="Semi_Exposed_Edge")

    Interior_Edges_Open = fd.Edgepart_Pointer(thickness=fd.inches(.01),
                                              material="Exposed_Interior_Edge")

#---------ASSEMBLY INSTRUCTIONS
        
class Vertical_Splitters(fd.Library_Assembly):
    
    library_name = "Cabinet Splitters"
    type_assembly = "INSERT"
    placement_type = "SPLITTER"
    property_id = "interiors.splitter_prompts"
    mirror_y = False
  
    open_name = ""

    vertical_openings = 2 #1-10
    opening_1_height = 0
    opening_2_height = 0
    opening_3_height = 0
    opening_4_height = 0
    opening_5_height = 0
    opening_6_height = 0
    opening_7_height = 0
    opening_8_height = 0
    opening_9_height = 0
    opening_10_height = 0
    
    remove_splitter_1 = False
    remove_splitter_2 = False
    remove_splitter_3 = False
    remove_splitter_4 = False
    remove_splitter_5 = False
    remove_splitter_6 = False
    remove_splitter_7 = False
    remove_splitter_8 = False
    remove_splitter_9 = False
    
    interior_1 = None
    exterior_1 = None
    interior_2 = None
    exterior_2 = None
    interior_3 = None
    exterior_3 = None
    interior_4 = None
    exterior_4 = None
    interior_5 = None
    exterior_5 = None
    interior_6 = None
    exterior_6 = None
    interior_7 = None
    exterior_7 = None
    interior_8 = None
    exterior_8 = None
    interior_9 = None
    exterior_9 = None
    interior_10 = None
    exterior_10 = None
    interior_11 = None
    exterior_11 = None
    
    def add_prompts(self):
        self.add_tab(name='Opening Heights',tab_type='CALCULATOR',calc_type="ZDIM")    
        self.add_tab(name='Formulas',tab_type='HIDDEN')    
        
        for i in range(1,self.vertical_openings+1):
        
            size = eval("self.opening_" + str(i) + "_height")
        
            self.add_prompt(name="Opening " + str(i) + " Height",
                            prompt_type='DISTANCE',
                            value=size,
                            tab_index=0,
                            equal=True if size == 0 else False)
    
        self.add_prompt(name="Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Left Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Right Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Top Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Bottom Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Extend Top Amount",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        self.add_prompt(name="Extend Bottom Amount",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        
        Thickness = self.get_var('Thickness')
        
        self.calculator_deduction("Thickness*(" + str(self.vertical_openings) +"-1)",[Thickness])
        
    def add_insert(self,insert,index,z_loc_vars=[],z_loc_expression=""):
        Width = self.get_var('dim_x','Width')
        Depth = self.get_var('dim_y','Depth')
        open_var = eval("self.get_var('Opening " + str(index) + " Height')")
        z_dim_expression = "Opening_" + str(index) + "_Height"

        if insert:
            if not insert.obj_bp:
                insert.draw()
            insert.obj_bp.parent = self.obj_bp
            insert.x_loc(value = 0)
            insert.y_loc(value = 0)
            if index == self.vertical_openings:
                insert.z_loc(value = 0)
            else:
                insert.z_loc(z_loc_expression,z_loc_vars)
            insert.x_rot(value = 0)
            insert.y_rot(value = 0)
            insert.z_rot(value = 0)
            insert.x_dim('Width',[Width])
            insert.y_dim('Depth',[Depth])
            insert.z_dim(z_dim_expression,[open_var])
            if index == 1:
                # ALLOW DOOR TO EXTEND TO TOP OF VALANCE
                extend_top_amount = insert.get_prompt("Extend Top Amount")
                if extend_top_amount:
                    Extend_Top_Amount = self.get_var("Extend Top Amount")
                    insert.prompt('Extend Top Amount','Extend_Top_Amount',[Extend_Top_Amount])
            
            if index == self.vertical_openings:
                # ALLOW DOOR TO EXTEND TO BOTTOM OF VALANCE
                extend_bottom_amount = insert.get_prompt("Extend Bottom Amount")
                if extend_bottom_amount:
                    Extend_Bottom_Amount = self.get_var("Extend Bottom Amount")
                    insert.prompt('Extend Bottom Amount','Extend_Bottom_Amount',[Extend_Bottom_Amount])
        
    def get_opening(self,index):
        opening = self.add_opening()
        opening.add_tab(name='Material Thickness',tab_type='HIDDEN')
        opening.add_prompt(name="Left Side Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        opening.add_prompt(name="Right Side Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        opening.add_prompt(name="Top Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        opening.add_prompt(name="Bottom Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        opening.add_prompt(name="Extend Top Amount",prompt_type='DISTANCE',value=fd.inches(0),tab_index=0)
        opening.add_prompt(name="Extend Bottom Amount",prompt_type='DISTANCE',value=fd.inches(0),tab_index=0)
        
        exterior = eval('self.exterior_' + str(index))
        interior = eval('self.interior_' + str(index))
        
        if interior:
            opening.obj_bp.cabinetlib.interior_open = False
        
        if exterior:
            opening.obj_bp.cabinetlib.exterior_open = False
            
        return opening
        
    def add_splitters(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Thickness = self.get_var('Thickness')
        
        previous_splitter = None
        
        for i in range(1,self.vertical_openings):

            z_loc_vars = []
            open_var = eval("self.get_var('Opening " + str(i) + " Height')")
            z_loc_vars.append(open_var)
            
            if previous_splitter:
                z_loc = previous_splitter.get_var("loc_z","Splitter_Z_Loc")
                z_loc_vars.append(z_loc)
                
            splitter = self.add_assembly(PART_WITH_EDGEBANDING)
            splitter.set_name("Splitter " + str(i))
            splitter.x_loc(value = 0)
            splitter.y_loc(value = 0)
            if previous_splitter:
                z_loc_vars.append(Thickness)
                splitter.z_loc('Splitter_Z_Loc-Opening_' + str(i) + '_Height-Thickness',z_loc_vars)
            else:
                z_loc_vars.append(Height)
                splitter.z_loc('Height-Opening_' + str(i) + '_Height',z_loc_vars)
            splitter.x_rot(value = 0)
            splitter.y_rot(value = 0)
            splitter.z_rot(value = 0)
            splitter.x_dim('Width',[Width])
            splitter.y_dim('Depth',[Depth])
            splitter.z_dim('-Thickness',[Thickness])
            remove_splitter = eval("self.remove_splitter_" + str(i))
            if remove_splitter:
                splitter.prompt('Hide',value=True)
            splitter.cutpart("Base_Fixed_Shelf")
            splitter.edgebanding('Cabinet_Body_Edges',l1 = True)
            
            previous_splitter = splitter
            
            opening_z_loc_vars = []
            opening_z_loc = previous_splitter.get_var("loc_z","Splitter_Z_Loc")
            opening_z_loc_vars.append(opening_z_loc)
            
            exterior = eval('self.exterior_' + str(i))
            self.add_insert(exterior, i, opening_z_loc_vars, "Splitter_Z_Loc")
            
            interior = eval('self.interior_' + str(i))
            self.add_insert(interior, i, opening_z_loc_vars, "Splitter_Z_Loc")
            
            opening = self.get_opening(i)
            self.add_insert(opening, i, opening_z_loc_vars, "Splitter_Z_Loc")

        #ADD LAST INSERT
        bottom_exterior = eval('self.exterior_' + str(self.vertical_openings))
        self.add_insert(bottom_exterior, self.vertical_openings)
        
        bottom_interior = eval('self.interior_' + str(self.vertical_openings))
        self.add_insert(bottom_interior, self.vertical_openings)

        bottom_opening = self.get_opening(self.vertical_openings)
        self.add_insert(bottom_opening, self.vertical_openings)

    def draw(self):
        self.create_assembly()
        
        self.add_prompts()
        
        self.add_splitters()
        
        self.update()
        
class Horizontal_Splitters(fd.Library_Assembly):
    
    library_name = "Cabinet Splitters"
    type_assembly = "INSERT"
    placement_type = "SPLITTER"
    property_id = "interiors.splitter_prompts"
    mirror_y = False
  
    open_name = ""

    horizontal_openings = 2 #1-10
    opening_1_width = 0
    opening_2_width = 0
    opening_3_width = 0
    opening_4_width = 0
    opening_5_width = 0
    opening_6_width = 0
    opening_7_width = 0
    opening_8_width = 0
    opening_9_width = 0
    opening_10_width = 0
    
    interior_1 = None
    exterior_1 = None
    interior_2 = None
    exterior_2 = None
    interior_3 = None
    exterior_3 = None
    interior_4 = None
    exterior_4 = None
    interior_5 = None
    exterior_5 = None
    interior_6 = None
    exterior_6 = None
    interior_7 = None
    exterior_7 = None
    interior_8 = None
    exterior_8 = None
    interior_9 = None
    exterior_9 = None
    interior_10 = None
    exterior_10 = None
    interior_11 = None
    exterior_11 = None
    
    def add_prompts(self):
        self.add_tab(name='Opening Widths',tab_type='CALCULATOR',calc_type="XDIM")    
        self.add_tab(name='Formulas',tab_type='HIDDEN')    
        
        for i in range(1,self.horizontal_openings+1):
        
            size = eval("self.opening_" + str(i) + "_width")
        
            self.add_prompt(name="Opening " + str(i) + " Width",
                            prompt_type='DISTANCE',
                            value=size,
                            tab_index=0,
                            equal=True if size == 0 else False)
    
        self.add_prompt(name="Thickness",
                        prompt_type='DISTANCE',
                        value=fd.inches(.75),
                        tab_index=1)
        
        Thickness = self.get_var('Thickness')
        
        self.calculator_deduction("Thickness*(" + str(self.horizontal_openings) +"-1)",[Thickness])
        
    def add_insert(self,insert,index,x_loc_vars=[],x_loc_expression=""):
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        open_var = eval("self.get_var('Opening " + str(index) + " Width')")
        x_dim_expression = "Opening_" + str(index) + "_Width"
        
        if insert:
            if not insert.obj_bp:
                insert.draw()

            insert.obj_bp.parent = self.obj_bp
            if index == 1:
                insert.x_loc(value = 0)
            else:
                print(index,x_loc_expression)
                insert.x_loc(x_loc_expression,x_loc_vars)
            insert.y_loc(value = 0)
            insert.z_loc(value = 0)
            insert.x_rot(value = 0)
            insert.y_rot(value = 0)
            insert.z_rot(value = 0)
            insert.x_dim(x_dim_expression,[open_var])
            insert.y_dim('Depth',[Depth])
            insert.z_dim('Height',[Height])
        
    def get_opening(self,index):
        opening = self.add_opening()
        opening.set_name("Opening " + str(index))
        opening.add_tab(name='Material Thickness',tab_type='HIDDEN')
        opening.add_prompt(name="Left Side Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        opening.add_prompt(name="Right Side Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        opening.add_prompt(name="Top Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        opening.add_prompt(name="Bottom Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        opening.add_prompt(name="Extend Top Amount",prompt_type='DISTANCE',value=fd.inches(0),tab_index=0)
        opening.add_prompt(name="Extend Bottom Amount",prompt_type='DISTANCE',value=fd.inches(0),tab_index=0)
        
        exterior = eval('self.exterior_' + str(index))
        interior = eval('self.interior_' + str(index))
        
        if interior:
            opening.obj_bp.cabinetlib.interior_open = False
        
        if exterior:
            opening.obj_bp.cabinetlib.exterior_open = False
            
        return opening
        
    def add_splitters(self):
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Thickness = self.get_var('Thickness')
        
        previous_splitter = None
        
        for i in range(1,self.horizontal_openings):
            
            x_loc_vars = []
            open_var = eval("self.get_var('Opening " + str(i) + " Width')")
            x_loc_vars.append(open_var)
            
            if previous_splitter:
                x_loc = previous_splitter.get_var("loc_x","Splitter_X_Loc")
                x_loc_vars.append(x_loc)
                x_loc_vars.append(Thickness)

            splitter = self.add_assembly(PART_WITH_EDGEBANDING)
            splitter.set_name("Splitter " + str(i))
            if previous_splitter:
                splitter.x_loc("Splitter_X_Loc+Thickness+Opening_" + str(i) + "_Width",x_loc_vars)
            else:
                splitter.x_loc("Opening_" + str(i) + "_Width",[open_var])
                
            splitter.y_loc(value = 0)
            splitter.z_loc(value = 0)
            splitter.x_rot(value = 0)
            splitter.y_rot(value = -90)
            splitter.z_rot(value = 0)
            splitter.x_dim('Height',[Height])
            splitter.y_dim('Depth',[Depth])
            splitter.z_dim('-Thickness',[Thickness])
            splitter.cutpart("Base_Fixed_Shelf")
            splitter.edgebanding('Cabinet_Body_Edges',l1 = True)

            previous_splitter = splitter

            exterior = eval('self.exterior_' + str(i))
            self.add_insert(exterior, i, x_loc_vars, "Splitter_X_Loc+Thickness")
            
            interior = eval('self.interior_' + str(i))
            self.add_insert(interior, i, x_loc_vars, "Splitter_X_Loc+Thickness")
            
            opening = self.get_opening(i)
            self.add_insert(opening, i, x_loc_vars, "Splitter_X_Loc+Thickness")
            
        insert_x_loc_vars = []
        insert_x_loc = previous_splitter.get_var("loc_x","Splitter_X_Loc")
        insert_x_loc_vars.append(insert_x_loc)
        insert_x_loc_vars.append(Thickness)

        #ADD LAST INSERT
        last_exterior = eval('self.exterior_' + str(self.horizontal_openings))
        self.add_insert(last_exterior, self.horizontal_openings,insert_x_loc_vars, "Splitter_X_Loc+Thickness")
          
        last_interior = eval('self.interior_' + str(self.horizontal_openings))
        self.add_insert(last_interior, self.horizontal_openings,insert_x_loc_vars, "Splitter_X_Loc+Thickness")

        last_opening = self.get_opening(self.horizontal_openings)
        self.add_insert(last_opening, self.horizontal_openings,insert_x_loc_vars, "Splitter_X_Loc+Thickness")
        
    def draw(self):
        self.create_assembly()
        
        self.add_prompts()
        
        self.add_splitters()
        
        self.update()
        
class Vertical_FF_Splitters(fd.Library_Assembly):
    
    library_name = "Cabinet Splitters"
    type_assembly = "INSERT"
    placement_type = "SPLITTER"
    property_id = "interiors.splitter_prompts"
    mirror_y = False
    
    open_name = ""
    
    vertical_openings = 2 #1-10
    opening_1_height = 0
    opening_2_height = 0
    opening_3_height = 0
    opening_4_height = 0
    opening_5_height = 0
    opening_6_height = 0
    opening_7_height = 0
    opening_8_height = 0
    opening_9_height = 0
    opening_10_height = 0
    
    interior_1 = None
    exterior_1 = None
    interior_2 = None
    exterior_2 = None
    interior_3 = None
    exterior_3 = None
    interior_4 = None
    exterior_4 = None
    interior_5 = None
    exterior_5 = None
    interior_6 = None
    exterior_6 = None
    interior_7 = None
    exterior_7 = None
    interior_8 = None
    exterior_8 = None
    interior_9 = None
    exterior_9 = None
    interior_10 = None
    exterior_10 = None
    interior_11 = None
    exterior_11 = None
    
    def add_prompts(self):
        self.add_tab(name='Opening Heights',tab_type='CALCULATOR',calc_type="ZDIM")    
        self.add_tab(name='Formulas',tab_type='HIDDEN')    
        
        for i in range(1,self.vertical_openings+1):
        
            size = eval("self.opening_" + str(i) + "_height")
        
            self.add_prompt(name="Opening " + str(i) + " Height",
                            prompt_type='DISTANCE',
                            value=size,
                            tab_index=0,
                            equal=True if size == 0 else False)
    
        self.add_prompt(name="Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Rail Width",prompt_type='DISTANCE',value=fd.inches(2),tab_index=1)
        self.add_prompt(name="Frame Thickness",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        self.add_prompt(name="Frame Left Gap",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        self.add_prompt(name="Frame Right Gap",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        self.add_prompt(name="Frame Top Gap",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        self.add_prompt(name="Frame Bottom Gap",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        
        Rail_Width = self.get_var('Rail Width')
        Frame_Top_Gap = self.get_var('Frame Top Gap')
        Frame_Bottom_Gap = self.get_var('Frame Bottom Gap')
        
        self.calculator_deduction("Rail_Width*(" + str(self.vertical_openings) +"-1)+Frame_Top_Gap+Frame_Bottom_Gap",[Rail_Width,Frame_Top_Gap,Frame_Bottom_Gap])
        
    def add_insert(self,insert,index,z_loc_vars=[],z_loc_expression=""):
        Width = self.get_var('dim_x','Width')
        Depth = self.get_var('dim_y','Depth')
        Frame_Thickness = self.get_var('Frame Thickness')
        Frame_Left_Gap = self.get_var('Frame Left Gap')
        Frame_Right_Gap = self.get_var('Frame Right Gap')
        Frame_Top_Gap = self.get_var('Frame Top Gap')
        Frame_Bottom_Gap = self.get_var('Frame Bottom Gap')
        open_var = eval("self.get_var('Opening " + str(index) + " Height')")
        z_dim_expression = "Opening_" + str(index) + "_Height"

        if insert:
            if not insert.obj_bp:
                insert.draw()
            insert.obj_bp.parent = self.obj_bp
            insert.x_loc(value = 0)
            insert.y_loc(value = 0)
            if index == self.vertical_openings:
                insert.z_loc('-Frame_Bottom_Gap',[Frame_Bottom_Gap])
            else:
                insert.z_loc(z_loc_expression,z_loc_vars)
            insert.x_rot(value = 0)
            insert.y_rot(value = 0)
            insert.z_rot(value = 0)
            insert.x_dim('Width',[Width])
            insert.y_dim('Depth',[Depth])
            
            insert.prompt("Frame Thickness","Frame_Thickness",[Frame_Thickness])
            insert.prompt("Frame Left Gap","Frame_Left_Gap",[Frame_Left_Gap])
            insert.prompt("Frame Right Gap","Frame_Right_Gap",[Frame_Right_Gap])
            
            if index == 1:
                # TOP
                z_dim_vars = []
                z_dim_vars.append(open_var)
                z_dim_vars.append(Frame_Top_Gap)
                insert.z_dim("Opening_" + str(index) + "_Height+Frame_Top_Gap",z_dim_vars)
                insert.prompt("Frame Top Gap","Frame_Top_Gap",[Frame_Top_Gap])
            elif index == self.vertical_openings:
                # BOTTOM
                z_dim_vars = []
                z_dim_vars.append(open_var)
                z_dim_vars.append(Frame_Bottom_Gap)
                insert.z_dim("Opening_" + str(index) + "_Height+Frame_Bottom_Gap",z_dim_vars)
                insert.prompt("Frame Bottom Gap","Frame_Bottom_Gap",[Frame_Bottom_Gap])
            else:
                # MIDDLE
                insert.z_dim(z_dim_expression,[open_var]) 
    
    def get_opening(self,index):
        opening = self.add_opening()
        opening.set_name("Opening " + str(index))
        opening.add_tab(name='Material Thickness',tab_type='HIDDEN')
        opening.add_prompt(name="Frame Thickness",prompt_type='DISTANCE',value=fd.inches(0),tab_index=0)
        opening.add_prompt(name="Frame Left Gap",prompt_type='DISTANCE',value=fd.inches(0),tab_index=0)
        opening.add_prompt(name="Frame Right Gap",prompt_type='DISTANCE',value=fd.inches(0),tab_index=0)
        opening.add_prompt(name="Frame Top Gap",prompt_type='DISTANCE',value=fd.inches(0),tab_index=0)
        opening.add_prompt(name="Frame Bottom Gap",prompt_type='DISTANCE',value=fd.inches(0),tab_index=0)
        
        exterior = eval('self.exterior_' + str(index))
        interior = eval('self.interior_' + str(index))
        
        if interior:
            opening.obj_bp.cabinetlib.interior_open = False
        
        if exterior:
            opening.obj_bp.cabinetlib.interior_open = False
            
        return opening
        
    def add_splitters(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Rail_Width = self.get_var('Rail Width')
        Thickness = self.get_var('Thickness')
        Frame_Thickness = self.get_var('Frame Thickness')
        Frame_Top_Gap = self.get_var('Frame Top Gap')
        Frame_Left_Gap = self.get_var('Frame Left Gap')
        Frame_Right_Gap = self.get_var('Frame Right Gap')
        
        previous_splitter = None
        
        for i in range(1,self.vertical_openings):
            z_loc_vars = []
            open_var = eval("self.get_var('Opening " + str(i) + " Height')")
            z_loc_vars.append(open_var)
            
            if previous_splitter:
                z_loc = previous_splitter.get_var("loc_z","Splitter_Z_Loc")
                z_loc_vars.append(z_loc)

            splitter = self.add_assembly(PART_WITH_EDGEBANDING)
            splitter.set_name("Mid Rail " + str(i))
            splitter.x_loc('Frame_Left_Gap',[Frame_Left_Gap])
            splitter.y_loc('-Frame_Thickness',[Frame_Thickness])
            if previous_splitter:
                z_loc_vars.append(Rail_Width)
                splitter.z_loc('Splitter_Z_Loc-Opening_' + str(i) + '_Height-Rail_Width',z_loc_vars)
            else:
                z_loc_vars.append(Height)
                z_loc_vars.append(Frame_Top_Gap)
                splitter.z_loc('Height-Frame_Top_Gap-Opening_' + str(i) + '_Height',z_loc_vars)
            splitter.x_rot(value = 90)
            splitter.y_rot(value = 0)
            splitter.z_rot(value = 0)
            splitter.x_dim('Width-(Frame_Left_Gap+Frame_Right_Gap)',[Width,Frame_Left_Gap,Frame_Right_Gap])
            splitter.y_dim('-Rail_Width',[Rail_Width])
            splitter.z_dim('-Thickness',[Thickness])
            splitter.cutpart("Frame")
            splitter.edgebanding('Cabinet_Body_Edges',l1 = True)
            
            previous_splitter = splitter
            
            opening_z_loc_vars = []
            opening_z_loc = previous_splitter.get_var("loc_z","Splitter_Z_Loc")
            opening_z_loc_vars.append(opening_z_loc)
            
            exterior = eval('self.exterior_' + str(i))
            self.add_insert(exterior, i, opening_z_loc_vars, "Splitter_Z_Loc")
            
            interior = eval('self.interior_' + str(i))
            self.add_insert(interior, i, opening_z_loc_vars, "Splitter_Z_Loc")
            
            opening = self.get_opening(i)
            self.add_insert(opening, i, opening_z_loc_vars, "Splitter_Z_Loc")

        #ADD LAST INSERT
        bottom_exterior = eval('self.exterior_' + str(self.vertical_openings))
        self.add_insert(bottom_exterior, self.vertical_openings)
        
        bottom_interior = eval('self.interior_' + str(self.vertical_openings))
        self.add_insert(bottom_interior, self.vertical_openings)

        bottom_opening = self.get_opening(self.vertical_openings)
        self.add_insert(bottom_opening, self.vertical_openings)
            
    def draw(self):
        self.create_assembly()
        
        if self.vertical_openings == 1:
            pass
        else:
            self.add_prompts()
            self.add_splitters()
        
        self.update()

class Vertical_FF_Notched_Splitters(fd.Library_Assembly):
    
    library_name = "Cabinet Splitters Notched"
    type_assembly = "INSERT"
    placement_type = "SPLITTER"
    property_id = "interiors.splitter_prompts"
    mirror_y = False
  
    open_name = ""
    
    vertical_openings = 2 #1-10
    opening_1_height = 0
    opening_2_height = 0
    opening_3_height = 0
    opening_4_height = 0
    opening_5_height = 0
    opening_6_height = 0
    opening_7_height = 0
    opening_8_height = 0
    opening_9_height = 0
    opening_10_height = 0
    
    interior_1 = None
    exterior_1 = None
    interior_2 = None
    exterior_2 = None
    interior_3 = None
    exterior_3 = None
    interior_4 = None
    exterior_4 = None
    interior_5 = None
    exterior_5 = None
    interior_6 = None
    exterior_6 = None
    interior_7 = None
    exterior_7 = None
    interior_8 = None
    exterior_8 = None
    interior_9 = None
    exterior_9 = None
    interior_10 = None
    exterior_10 = None
    interior_11 = None
    exterior_11 = None
    
    def add_prompts(self):
        self.add_tab(name='Opening Heights',tab_type='CALCULATOR',calc_type="ZDIM")    
        self.add_tab(name='Formulas',tab_type='HIDDEN')    
        
        for i in range(1,self.vertical_openings+1):
        
            size = eval("self.opening_" + str(i) + "_height")
        
            self.add_prompt(name="Opening " + str(i) + " Height",
                            prompt_type='DISTANCE',
                            value=size,
                            tab_index=0,
                            equal=True if size == 0 else False)
    
        self.add_prompt(name="Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Rail Width",prompt_type='DISTANCE',value=fd.inches(2),tab_index=1)
        self.add_prompt(name="Frame Thickness",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        self.add_prompt(name="Frame Left Gap",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        self.add_prompt(name="Frame Right Gap",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        self.add_prompt(name="Frame Top Gap",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        self.add_prompt(name="Frame Bottom Gap",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        
        #----------W
        self.add_prompt(name="Right Side Depth",prompt_type='DISTANCE',value=fd.inches(23),tab_index=1)
        self.add_prompt(name="Left Side Depth",prompt_type='DISTANCE',value=fd.inches(23),tab_index=1)
        #----------W
        
        Rail_Width = self.get_var('Rail Width')
        Frame_Top_Gap = self.get_var('Frame Top Gap')
        Frame_Bottom_Gap = self.get_var('Frame Bottom Gap')
        
        self.calculator_deduction("Rail_Width*(" + str(self.vertical_openings) +"-1)+Frame_Top_Gap+Frame_Bottom_Gap",[Rail_Width,Frame_Top_Gap,Frame_Bottom_Gap])
        
    def add_insert(self,insert,index,z_loc_vars=[],z_loc_expression=""):
        Width = self.get_var('dim_x','Width')
        Depth = self.get_var('dim_y','Depth')
        Frame_Thickness = self.get_var('Frame Thickness')
        Frame_Left_Gap = self.get_var('Frame Left Gap')
        Frame_Right_Gap = self.get_var('Frame Right Gap')
        Frame_Top_Gap = self.get_var('Frame Top Gap')
        Frame_Bottom_Gap = self.get_var('Frame Bottom Gap')
        open_var = eval("self.get_var('Opening " + str(index) + " Height')")
        z_dim_expression = "Opening_" + str(index) + "_Height"

        if insert:
            if not insert.obj_bp:
                insert.draw()
            insert.obj_bp.parent = self.obj_bp
            insert.x_loc(value = 0)
            insert.y_loc(value = 0)
            if index == self.vertical_openings:
                insert.z_loc('-Frame_Bottom_Gap',[Frame_Bottom_Gap])
            else:
                insert.z_loc(z_loc_expression,z_loc_vars)
            insert.x_rot(value = 0)
            insert.y_rot(value = 0)
            insert.z_rot(value = 0)
            insert.x_dim('Width',[Width])
            insert.y_dim('Depth',[Depth])
            
            insert.prompt("Frame Thickness","Frame_Thickness",[Frame_Thickness])
            insert.prompt("Frame Left Gap","Frame_Left_Gap",[Frame_Left_Gap])
            insert.prompt("Frame Right Gap","Frame_Right_Gap",[Frame_Right_Gap])
            
            if index == 1:
                # TOP
                z_dim_vars = []
                z_dim_vars.append(open_var)
                z_dim_vars.append(Frame_Top_Gap)
                insert.z_dim("Opening_" + str(index) + "_Height+Frame_Top_Gap",z_dim_vars)
                insert.prompt("Frame Top Gap","Frame_Top_Gap",[Frame_Top_Gap])
            elif index == self.vertical_openings:
                # BOTTOM
                z_dim_vars = []
                z_dim_vars.append(open_var)
                z_dim_vars.append(Frame_Bottom_Gap)
                insert.z_dim("Opening_" + str(index) + "_Height+Frame_Bottom_Gap",z_dim_vars)
                insert.prompt("Frame Bottom Gap","Frame_Bottom_Gap",[Frame_Bottom_Gap])
            else:
                # MIDDLE
                insert.z_dim(z_dim_expression,[open_var]) 
    
    def get_opening(self,index):
        opening = self.add_opening()
        opening.set_name("Opening " + str(index))
        opening.add_tab(name='Material Thickness',tab_type='HIDDEN')
        opening.add_prompt(name="Frame Thickness",prompt_type='DISTANCE',value=fd.inches(0),tab_index=0)
        opening.add_prompt(name="Frame Left Gap",prompt_type='DISTANCE',value=fd.inches(0),tab_index=0)
        opening.add_prompt(name="Frame Right Gap",prompt_type='DISTANCE',value=fd.inches(0),tab_index=0)
        opening.add_prompt(name="Frame Top Gap",prompt_type='DISTANCE',value=fd.inches(0),tab_index=0)
        opening.add_prompt(name="Frame Bottom Gap",prompt_type='DISTANCE',value=fd.inches(0),tab_index=0)
        
        exterior = eval('self.exterior_' + str(index))
        interior = eval('self.interior_' + str(index))
        
        if interior:
            opening.obj_bp.cabinetlib.interior_open = False
        
        if exterior:
            opening.obj_bp.cabinetlib.interior_open = False
            
        return opening
        
    def add_splitters(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Left_Side_Depth = self.get_var('Left Side Depth','Left_Side_Depth')
        Right_Side_Depth = self.get_var('Right Side Depth','Right_Side_Depth')
        Rail_Width = self.get_var('Rail Width')
        Thickness = self.get_var('Thickness')
        Frame_Thickness = self.get_var('Frame Thickness')
        Frame_Top_Gap = self.get_var('Frame Top Gap')
        Frame_Left_Gap = self.get_var('Frame Left Gap')
        Frame_Right_Gap = self.get_var('Frame Right Gap')
        
        previous_splitter = None
        
        for i in range(1,self.vertical_openings):
            z_loc_vars = []
            open_var = eval("self.get_var('Opening " + str(i) + " Height')")
            z_loc_vars.append(open_var)
            
            if previous_splitter:
                z_loc = previous_splitter.get_var("loc_z","Splitter_Z_Loc")
                z_loc_vars.append(z_loc)

            splitter_l = self.add_assembly(PART_WITH_EDGEBANDING)
            splitter_l.set_name("Mid Rail Left" + str(i))
            splitter_l.x_loc('Left_Side_Depth+Frame_Left_Gap',[Frame_Left_Gap,Left_Side_Depth])
            splitter_l.y_loc('Depth',[Depth])
            if previous_splitter:
                z_loc_vars.append(Rail_Width)
                splitter_l.z_loc('Splitter_Z_Loc-Opening_' + str(i) + '_Height-Rail_Width',z_loc_vars)
            else:
                z_loc_vars.append(Height)
                z_loc_vars.append(Frame_Top_Gap)
                splitter_l.z_loc('Height-Frame_Top_Gap-Opening_' + str(i) + '_Height',z_loc_vars)
            splitter_l.x_rot(value = 90)
            splitter_l.y_rot(value = 0)
            splitter_l.z_rot(value = 90)
            
            splitter_l.x_dim('-Depth-Right_Side_Depth',[Depth,Right_Side_Depth])
            splitter_l.y_dim('-Rail_Width',[Rail_Width])
            splitter_l.z_dim('-Thickness',[Thickness])
            splitter_l.cutpart("Frame")
            splitter_l.edgebanding('Cabinet_Body_Edges',l1 = True)
            
            splitter_r = self.add_assembly(PART_WITH_EDGEBANDING)
            splitter_r.set_name("Mid Rail Right" + str(i))
            
            splitter_r.x_loc("Width-Frame_Right_Gap",[Width,Frame_Right_Gap])
            splitter_r.y_loc("-Right_Side_Depth",[Right_Side_Depth])
            
            if previous_splitter:
                z_loc_vars.append(Rail_Width)
                splitter_r.z_loc('Splitter_Z_Loc-Opening_' + str(i) + '_Height-Rail_Width',z_loc_vars)
            else:
                z_loc_vars.append(Height)
                z_loc_vars.append(Frame_Top_Gap)
                splitter_r.z_loc('Height-Frame_Top_Gap-Opening_' + str(i) + '_Height',z_loc_vars)
            
            splitter_r.x_rot(value = 90)
            splitter_r.y_rot(value = 0)
            splitter_r.z_rot(value = -180) 
            
            splitter_r.x_dim("Width-Left_Side_Depth",[Width,Left_Side_Depth])
            splitter_r.y_dim('-Rail_Width',[Rail_Width])
            splitter_r.z_dim("-Thickness",[Thickness])
            splitter_r.cutpart("Frame")
            splitter_r.edgebanding('Cabinet_Body_Edges',l1 = True)
            
            previous_splitter = splitter_l     
            
            opening_z_loc_vars = []
            opening_z_loc = previous_splitter.get_var("loc_z","Splitter_Z_Loc")
            opening_z_loc_vars.append(opening_z_loc)
            
            exterior = eval('self.exterior_' + str(i))
            self.add_insert(exterior, i, opening_z_loc_vars, "Splitter_Z_Loc")
            
            interior = eval('self.interior_' + str(i))
            self.add_insert(interior, i, opening_z_loc_vars, "Splitter_Z_Loc")
            
            opening = self.get_opening(i)
            self.add_insert(opening, i, opening_z_loc_vars, "Splitter_Z_Loc")

        #ADD LAST INSERT
        bottom_exterior = eval('self.exterior_' + str(self.vertical_openings))
        self.add_insert(bottom_exterior, self.vertical_openings)
        
        bottom_interior = eval('self.interior_' + str(self.vertical_openings))
        self.add_insert(bottom_interior, self.vertical_openings)

        bottom_opening = self.get_opening(self.vertical_openings)
        self.add_insert(bottom_opening, self.vertical_openings)
            
    def draw(self):
        self.create_assembly()
        
        if self.vertical_openings == 1:
            pass
        else:
            self.add_prompts()
            self.add_splitters()
        
        self.update()
        
class Horizontal_FF_Splitters(fd.Library_Assembly):
    
    library_name = "Cabinet Splitters"
    type_assembly = "INSERT"
    placement_type = "SPLITTER"
    property_id = "interiors.splitter_prompts"
    mirror_y = False
  
    open_name = ""
    carcass_type = "" # {Base, Tall, Upper, Sink, Suspended}
    
    horizontal_openings = 2 #1-10
    opening_1_width = 0
    opening_2_width = 0
    opening_3_width = 0
    opening_4_width = 0
    opening_5_width = 0
    opening_6_width = 0
    opening_7_width = 0
    opening_8_width = 0
    opening_9_width = 0
    opening_10_width = 0
    
    interior_1 = None
    exterior_1 = None
    interior_2 = None
    exterior_2 = None
    interior_3 = None
    exterior_3 = None
    interior_4 = None
    exterior_4 = None
    interior_5 = None
    exterior_5 = None
    interior_6 = None
    exterior_6 = None
    interior_7 = None
    exterior_7 = None
    interior_8 = None
    exterior_8 = None
    interior_9 = None
    exterior_9 = None
    interior_10 = None
    exterior_10 = None
    interior_11 = None
    exterior_11 = None
    
    def add_prompts(self):
        self.add_tab(name='Opening Widths',tab_type='CALCULATOR',calc_type="XDIM")    
        self.add_tab(name='Formulas',tab_type='HIDDEN')    
        
        for i in range(1,self.horizontal_openings+1):
        
            size = eval("self.opening_" + str(i) + "_width")
        
            self.add_prompt(name="Opening " + str(i) + " Width",
                            prompt_type='DISTANCE',
                            value=size,
                            tab_index=0,
                            equal=True if size == 0 else False)
    
        self.add_prompt(name="Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=1)
        self.add_prompt(name="Rail Width",prompt_type='DISTANCE',value=fd.inches(2),tab_index=1)
        self.add_prompt(name="Frame Thickness",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        self.add_prompt(name="Frame Left Gap",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        self.add_prompt(name="Frame Right Gap",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        self.add_prompt(name="Frame Top Gap",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        self.add_prompt(name="Frame Bottom Gap",prompt_type='DISTANCE',value=fd.inches(0),tab_index=1)
        
        Rail_Width = self.get_var('Rail Width')
        
        self.calculator_deduction("Rail_Width*(" + str(self.horizontal_openings) +"-1)",[Rail_Width])
        
    def add_insert(self,insert,index,x_loc_vars=[],x_loc_expression=""):
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Frame_Thickness = self.get_var('Frame Thickness')
        Frame_Left_Gap = self.get_var('Frame Left Gap')
        Frame_Right_Gap = self.get_var('Frame Right Gap')
        Frame_Top_Gap = self.get_var('Frame Top Gap')
        Frame_Bottom_Gap = self.get_var('Frame Bottom Gap')
        open_var = eval("self.get_var('Opening " + str(index) + " Width')")
        x_dim_expression = "Opening_" + str(index) + "_Width"

        if insert:
            if not insert.obj_bp:
                insert.draw()
            insert.obj_bp.parent = self.obj_bp
            if index == 1:
                insert.x_loc('-Frame_Left_Gap',[Frame_Left_Gap])
            else:
                insert.x_loc(x_loc_expression,x_loc_vars)
            insert.y_loc(value = 0)
            insert.z_loc(value = 0)
            insert.x_rot(value = 0)
            insert.y_rot(value = 0)
            insert.z_rot(value = 0)
            insert.y_dim('Depth',[Depth])
            insert.z_dim('Height',[Height])
            insert.prompt("Frame Thickness","Frame_Thickness",[Frame_Thickness])
            insert.prompt("Frame Top Gap","Frame_Top_Gap",[Frame_Top_Gap])
            insert.prompt("Frame Bottom Gap","Frame_Bottom_Gap",[Frame_Bottom_Gap])
            
            if index == 1:
                # LEFT
                x_dim_vars = []
                x_dim_vars.append(open_var)
                x_dim_vars.append(Frame_Left_Gap)
                insert.x_dim("Opening_" + str(index) + "_Width+Frame_Left_Gap",x_dim_vars)
                insert.prompt("Frame Left Gap","Frame_Left_Gap",[Frame_Left_Gap])
            elif index == self.horizontal_openings:
                # RIGHT
                x_dim_vars = []
                x_dim_vars.append(open_var)
                x_dim_vars.append(Frame_Right_Gap)
                insert.x_dim("Opening_" + str(index) + "_Width+Frame_Right_Gap",x_dim_vars)
                insert.prompt("Frame Right Gap","Frame_Right_Gap",[Frame_Right_Gap])
            else:
                # MIDDLE
                insert.x_dim(x_dim_expression,[open_var]) 
    
    def get_opening(self,index):
        opening = self.add_opening()
        opening.set_name("Opening " + str(index))
        opening.add_tab(name='Material Thickness',tab_type='HIDDEN')
        opening.add_prompt(name="Frame Thickness",prompt_type='DISTANCE',value=fd.inches(0),tab_index=0)
        opening.add_prompt(name="Frame Left Gap",prompt_type='DISTANCE',value=fd.inches(0),tab_index=0)
        opening.add_prompt(name="Frame Right Gap",prompt_type='DISTANCE',value=fd.inches(0),tab_index=0)
        opening.add_prompt(name="Frame Top Gap",prompt_type='DISTANCE',value=fd.inches(0),tab_index=0)
        opening.add_prompt(name="Frame Bottom Gap",prompt_type='DISTANCE',value=fd.inches(0),tab_index=0)
        
        Frame_Thickness = self.get_var('Frame Thickness')
        Frame_Left_Gap = self.get_var('Frame Left Gap')
        Frame_Right_Gap = self.get_var('Frame Right Gap')
        Frame_Top_Gap = self.get_var('Frame Top Gap')
        Frame_Bottom_Gap = self.get_var('Frame Bottom Gap')
        
        opening.prompt("Frame Top Gap","Frame_Top_Gap",[Frame_Top_Gap])
        opening.prompt("Frame Bottom Gap","Frame_Bottom_Gap",[Frame_Bottom_Gap])
        opening.prompt("Frame Thickness","Frame_Thickness",[Frame_Thickness])
        
        #TODO: Calculate logic for left and right frame gap. 
        if index == 1: #IS LEFT
            opening.prompt("Frame Left Gap","Frame_Left_Gap",[Frame_Left_Gap])
        else:
            pass #TODO: Calculate if splitter is turned on to calculate gap
         
        if index == self.horizontal_openings: #IS RIGHT
            opening.prompt("Frame Right Gap","Frame_Right_Gap",[Frame_Right_Gap])
        else:
            pass #TODO: Calculate if splitter is turned on to calculate gap
        
        exterior = eval('self.exterior_' + str(index))
        interior = eval('self.interior_' + str(index))
        
        if interior:
            opening.obj_bp.cabinetlib.interior_open = False
        
        if exterior:
            opening.obj_bp.cabinetlib.interior_open = False
            
        return opening
        
    def add_splitters(self):
        Height = self.get_var('dim_z','Height')
        Rail_Width = self.get_var('Rail Width')
        Thickness = self.get_var('Thickness')
        Frame_Thickness = self.get_var('Frame Thickness')
        Frame_Top_Gap = self.get_var('Frame Top Gap')
        Frame_Bottom_Gap = self.get_var('Frame Bottom Gap')
        
        previous_splitter = None
        
        for i in range(1,self.horizontal_openings):
            x_loc_vars = []
            open_var = eval("self.get_var('Opening " + str(i) + " Width')")
            x_loc_vars.append(open_var)
            
            if previous_splitter:
                x_loc = previous_splitter.get_var("loc_x","Splitter_X_Loc")
                x_loc_vars.append(x_loc)
                x_loc_vars.append(Rail_Width)

            splitter = self.add_assembly(PART_WITH_EDGEBANDING)
            splitter.set_name("Mid Rail " + str(i))
            if previous_splitter:
                splitter.x_loc('Splitter_X_Loc+Opening_' + str(i) + '_Width+Rail_Width',x_loc_vars)
            else:
                splitter.x_loc('Opening_' + str(i) + '_Width',x_loc_vars)
            splitter.y_loc('-Frame_Thickness',[Frame_Thickness])
            splitter.z_loc('Frame_Bottom_Gap',[Frame_Bottom_Gap])
            splitter.x_rot(value = 90)
            splitter.y_rot(value = -90)
            splitter.z_rot(value = 0)
            splitter.x_dim('Height-(Frame_Top_Gap+Frame_Bottom_Gap)',[Height,Frame_Top_Gap,Frame_Bottom_Gap])
            splitter.y_dim('-Rail_Width',[Rail_Width])
            splitter.z_dim('-Thickness',[Thickness])
            splitter.cutpart("Frame")
            splitter.edgebanding('Cabinet_Body_Edges',l1 = True)
            
            previous_splitter = splitter
            
            exterior = eval('self.exterior_' + str(i))
            self.add_insert(exterior, i, x_loc_vars, "Splitter_X_Loc+Rail_Width")
            
            interior = eval('self.interior_' + str(i))
            self.add_insert(interior, i, x_loc_vars, "Splitter_X_Loc+Rail_Width")
            
            opening = self.get_opening(i)
            self.add_insert(opening, i, x_loc_vars, "Splitter_X_Loc+Rail_Width")
            
        opening_x_loc_vars = []
        opening_x_loc_vars.append(previous_splitter.get_var("loc_x","Splitter_X_Loc"))
        opening_x_loc_vars.append(Rail_Width)
            
        #ADD LAST INSERT
        last_exterior = eval('self.exterior_' + str(self.horizontal_openings))
        self.add_insert(last_exterior, self.horizontal_openings,opening_x_loc_vars, "Splitter_X_Loc+Rail_Width")
        
        last_interior = eval('self.interior_' + str(self.horizontal_openings))
        self.add_insert(last_interior, self.horizontal_openings,opening_x_loc_vars, "Splitter_X_Loc+Rail_Width")

        last_opening = self.get_opening(self.horizontal_openings)
        self.add_insert(last_opening, self.horizontal_openings,opening_x_loc_vars, "Splitter_X_Loc+Rail_Width")

    def draw(self):
        self.create_assembly()
        
        self.add_prompts()
        self.add_splitters()
        
        self.update()
        
#---------INSERTS        

class INSERT_2_Horizontal_Openings(Horizontal_Splitters):
    
    def __init__(self):
        self.category_name = "Frameless"
        self.assembly_name = "2 Horizontal Openings"
        self.horizontal_openings = 2
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
class INSERT_3_Horizontal_Openings(Horizontal_Splitters):
    
    def __init__(self):
        self.category_name = "Frameless"
        self.assembly_name = "3 Horizontal Openings"
        self.horizontal_openings = 3
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
class INSERT_4_Horizontal_Openings(Horizontal_Splitters):
    
    def __init__(self):
        self.category_name = "Frameless"
        self.assembly_name = "4 Horizontal Openings"
        self.horizontal_openings = 4
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
class INSERT_5_Horizontal_Openings(Horizontal_Splitters):
    
    def __init__(self):
        self.category_name = "Frameless"
        self.assembly_name = "5 Horizontal Openings"
        self.horizontal_openings = 5
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
class INSERT_2_Vertical_Openings(Vertical_Splitters):
    
    def __init__(self):
        self.category_name = "Frameless"
        self.assembly_name = "2 Vertical Openings"
        self.vertical_openings = 2
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
class INSERT_3_Vertical_Openings(Vertical_Splitters):
    
    def __init__(self):
        self.category_name = "Frameless"
        self.assembly_name = "3 Vertical Openings"
        self.vertical_openings = 3
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
class INSERT_4_Vertical_Openings(Vertical_Splitters):
    
    def __init__(self):
        self.category_name = "Frameless"
        self.assembly_name = "4 Vertical Openings"
        self.vertical_openings = 4
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
class INSERT_5_Vertical_Openings(Vertical_Splitters):
    
    def __init__(self):
        self.category_name = "Frameless"
        self.assembly_name = "5 Vertical Openings"
        self.vertical_openings = 5
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
class INSERT_2_Vertical_Openings_FF(Vertical_FF_Splitters):
    
    def __init__(self):
        self.category_name = "Face Frame"
        self.assembly_name = "2 Vertical Openings FF"
        self.vertical_openings = 2
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
class INSERT_3_Vertical_Openings_FF(Vertical_FF_Splitters):
    
    def __init__(self):
        self.category_name = "Face Frame"
        self.assembly_name = "3 Vertical Openings FF"
        self.vertical_openings = 3
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
class INSERT_4_Vertical_Openings_FF(Vertical_FF_Splitters):
    
    def __init__(self):
        self.category_name = "Face Frame"
        self.assembly_name = "4 Vertical Openings FF"
        self.vertical_openings = 4
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
class INSERT_5_Vertical_Openings_FF(Vertical_FF_Splitters):
    
    def __init__(self):
        self.category_name = "Face Frame"
        self.assembly_name = "5 Vertical Openings FF"
        self.vertical_openings = 5
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
class INSERT_2_Vertical_Notched_Openings_1_FF(Vertical_FF_Notched_Splitters):
    
    def __init__(self): 
        self.category_name = "Vertical Splitters FF"
        self.assembly_name = "2 Vertical Notched Openings FF"
        self.vertical_openings = 2
        self.width = fd.inches(36)
        self.height = fd.inches(34)
        self.depth = fd.inches(-36)               
        
class INSERT_3_Vertical_Notched_Openings_FF(Vertical_FF_Notched_Splitters):
    
    def __init__(self): 
        self.category_name = "Vertical Splitters FF"
        self.assembly_name = "3 Vertical Notched Openings FF"
        self.vertical_openings = 3
        self.width = fd.inches(36)
        self.height = fd.inches(34)
        self.depth = fd.inches(-36)     
        
class INSERT_4_Vertical_Notched_Openings_FF(Vertical_FF_Notched_Splitters):
    
    def __init__(self): 
        self.category_name = "Vertical Splitters FF"
        self.assembly_name = "4 Vertical Notched Openings FF"
        self.vertical_openings = 4
        self.width = fd.inches(36)
        self.height = fd.inches(34)
        self.depth = fd.inches(-36)         
        
class INSERT_5_Vertical_Notched_Openings_FF(Vertical_FF_Notched_Splitters):
    
    def __init__(self): 
        self.category_name = "Vertical Splitters FF"
        self.assembly_name = "5 Vertical Notched Openings FF"
        self.vertical_openings = 5
        self.width = fd.inches(36)
        self.height = fd.inches(34)
        self.depth = fd.inches(-36)             
        
class INSERT_2_Horizontal_Openings_FF(Horizontal_FF_Splitters):
    
    def __init__(self):
        self.category_name = "Face Frame"
        self.assembly_name = "2 Horizontal Openings FF"
        self.horizontal_openings = 2
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
class INSERT_3_Horizontal_Openings_FF(Horizontal_FF_Splitters):
    
    def __init__(self):
        self.category_name = "Face Frame"
        self.assembly_name = "3 Horizontal Openings FF"
        self.horizontal_openings = 3
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
class INSERT_4_Horizontal_Openings_FF(Horizontal_FF_Splitters):
    
    def __init__(self):
        self.category_name = "Face Frame"
        self.assembly_name = "4 Horizontal Openings FF"
        self.horizontal_openings = 4
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
class INSERT_5_Horizontal_Openings_FF(Horizontal_FF_Splitters):
    
    def __init__(self):
        self.category_name = "Face Frame"
        self.assembly_name = "5 Horizontal Openings FF"
        self.horizontal_openings = 5
        self.width = fd.inches(18)
        self.height = fd.inches(34)
        self.depth = fd.inches(23)
        
#---------INTERFACES
        
class PROMPTS_Splitter_Prompts(bpy.types.Operator):
    bl_idname = "interiors.splitter_prompts"
    bl_label = "Vertical Splitter Prompts" 
    bl_description = "This shows all of the available vertical splitter options"
    bl_options = {'UNDO'}
    
    object_name = bpy.props.StringProperty(name="Object Name")
    
    assembly = None
    
    @classmethod
    def poll(cls, context):
        return True
        
    def check(self, context):
        fd.run_calculators(self.assembly.obj_bp)
        return True
        
    def execute(self, context):
        if self.assembly.obj_bp:
            if self.assembly.obj_bp.name in context.scene.objects:
                fd.run_calculators(self.assembly.obj_bp)
        return {'FINISHED'}
        
    def get_splitter(self,obj_bp):
        assembly = fd.Assembly(obj_bp)
        if assembly.get_prompt("Opening 1 Height") or assembly.get_prompt("Opening 1 Width"):
            return assembly
        if obj_bp.parent:
            assembly = fd.Assembly(obj_bp.parent)
            if assembly.get_prompt("Opening 1 Height") or assembly.get_prompt("Opening 1 Width"):
                return assembly
            if assembly.obj_bp.parent:
                assembly = fd.Assembly(assembly.obj_bp.parent)
                if assembly.get_prompt("Opening 1 Height") or assembly.get_prompt("Opening 1 Width"):
                    return assembly
        
    def invoke(self,context,event):
        obj = bpy.data.objects[self.object_name]
        obj_insert_bp = fd.get_bp(obj,'INSERT')
        self.assembly = self.get_splitter(obj_insert_bp)
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=fd.get_prop_dialog_width(330))
        
    def draw_selected_insert_prompts(self,layout):
        obj = bpy.data.objects[self.object_name]
        obj_insert_bp = fd.get_bp(obj,'INSERT')
        if "Drawer Options" in obj_insert_bp.mv.PromptPage.COL_MainTab:
            layout.operator("exteriors.drawer_prompts",text="Drawer Options",icon='SETTINGS').object_name = obj_insert_bp.name
        if "Door Options" in obj_insert_bp.mv.PromptPage.COL_MainTab:
            layout.operator("exteriors.door_prompts",text="Door Options",icon='SETTINGS').object_name = obj_insert_bp.name
        if "Shoe Cubby Options" in obj_insert_bp.mv.PromptPage.COL_MainTab:
            layout.operator("cbdprompts.shoe_cubbies",text="Shoe Cubby Options",icon='SETTINGS').object_name = obj_insert_bp.name
        if "Hanging Options" in obj_insert_bp.mv.PromptPage.COL_MainTab:
            layout.operator("interiors.hanging_rod_prompts",text="Hanging Rod Options",icon='SETTINGS').object_name = obj_insert_bp.name
        if "Slanted Shoe Options" in obj_insert_bp.mv.PromptPage.COL_MainTab:
            layout.operator("cbdprompts.shelf_prompt",text="Slanted Shoe Options",icon='SETTINGS').object_name = obj_insert_bp.name
        if "Wire Basket Options" in obj_insert_bp.mv.PromptPage.COL_MainTab:
            layout.operator("interiors.wire_baskets",text="Wire Basket Options",icon='SETTINGS').object_name = obj_insert_bp.name
        if "Hamper Options" in obj_insert_bp.mv.PromptPage.COL_MainTab:
            layout.operator("exteriors.hamper_prompts",text="Hamper Options",icon='SETTINGS').object_name = obj_insert_bp.name
            
    def draw(self, context):
        layout = self.layout
        if self.assembly.obj_bp:
            if self.assembly.get_prompt("Opening 1 Height"):
                name = "Height"
            else:
                name = "Width"
            if self.assembly.obj_bp.name in context.scene.objects:
                box = layout.box()
                opening_1 = self.assembly.get_prompt("Opening 1 " + name)
                opening_2 = self.assembly.get_prompt("Opening 2 " + name)
                opening_3 = self.assembly.get_prompt("Opening 3 " + name)
                opening_4 = self.assembly.get_prompt("Opening 4 " + name)
                
                if opening_1:
                    row = box.row()
                    row.label("Opening 1 " + name + ":")
                    if opening_1.equal:
                        row.label(str(fd.unit(opening_1.DistanceValue)))
                        row.prop(opening_1,'equal',text="")
                    else:
                        row.prop(opening_1,'DistanceValue',text="")
                        row.prop(opening_1,'equal',text="")
                if opening_2:
                    row = box.row()
                    row.label("Opening 2 " + name + ":")
                    if opening_2.equal:
                        row.label(str(fd.unit(opening_2.DistanceValue)))
                        row.prop(opening_2,'equal',text="")
                    else:
                        row.prop(opening_2,'DistanceValue',text="")
                        row.prop(opening_2,'equal',text="")
                if opening_3:
                    row = box.row()
                    row.label("Opening 3 " + name + ":")
                    if opening_3.equal:
                        row.label(str(fd.unit(opening_3.DistanceValue)))
                        row.prop(opening_3,'equal',text="")
                    else:
                        row.prop(opening_3,'DistanceValue',text="")
                        row.prop(opening_3,'equal',text="")
                if opening_4:
                    row = box.row()
                    row.label("Opening 4 " + name + ":")
                    if opening_4.equal:
                        row.label(str(fd.unit(opening_4.DistanceValue)))
                        row.prop(opening_4,'equal',text="")
                    else:
                        row.prop(opening_4,'DistanceValue',text="")
                        row.prop(opening_4,'equal',text="")
                        
                self.draw_selected_insert_prompts(box)

def register():
    bpy.utils.register_class(PROMPTS_Splitter_Prompts)
    
def unregister():
    bpy.utils.unregister_class(PROMPTS_Splitter_Prompts)
    
    