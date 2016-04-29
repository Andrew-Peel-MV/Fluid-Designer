"""
Microvellum 
Cabinets
Stores the logic for the different types of closet carcasses.
TODO: Create Wall Hung Closet Carcass
"""
import bpy
import fd
import math

from bpy.app.handlers import persistent

HIDDEN_FOLDER_NAME = "_HIDDEN"
PART_WITH_EDGEBANDING = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Cut Parts","Part with Edgebanding")
PART_WITH_FRONT_EDGEBANDING = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Cut Parts","Part with Front Edgebanding")
PART_WITH_NO_EDGEBANDING = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Cut Parts","Part with No Edgebanding")
BLIND_PANEL = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Cut Parts","Part with Edgebanding")
ADJ_MACHINING = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Machining","Adjustable Shelf Holes")
LINE_BORE = (HIDDEN_FOLDER_NAME,"Cabinet Assemblies","Machining","Line Bore Holes")

EXPOSED_CABINET_MATERIAL = ("Plastics","White Melamine")
UNEXPOSED_CABINET_MATERIAL = ("Wood","Wood Core","Particle Board")
SEMI_EXPOSED_CABINET_MATERIAL = ("Plastics","White Melamine")

PANEL_HEIGHTS=[('83','3 5/6"','3 5/6"'),
               ('115','4 9/16"','4 9/16"'),
               ('147','5 13/16"','5 13/16"'),
               ('179','7 1/16"','7 1/16"'),
               ('211','8 5/16"','8 5/16"'),
               ('243','9 5/8"','9 5/8"'),
               ('275','10 7/8"','10 7/8"'),
               ('307','12 1/8"','12 1/8"'),
               ('339','13 3/8"','13 3/8"'),
               ('371','14 5/8"','14 5/8"'),
               ('403','15 7/8"','15 7/8"'),
               ('435','17 1/8"','17 1/8"'),
               ('467','18 3/8"','18 3/8"'),
               ('499','19 11/16"','19 11/16"'),
               ('531','20 15/16"','20 15/16"'),
               ('563','22 3/16"','22 3/16"'),
               ('595','23 7/16"','23 7/16"'),
               ('627','24 3/4"','24 3/4"'),
               ('659','26"','26"'),
               ('691','27 1/4"','27 1/4"'),
               ('723','28 1/2"','28 1/2"'),
               ('755','29 3/4"','29 3/4"'),
               ('787','31"','31"'),
               ('819','32 1/4"','32 1/4"'),
               ('851','33 9/16"','33 9/16"'),
               ('883','34 3/4"','34 3/4"'),
               ('915','36 1/16"','36 1/16"'),
               ('947','37 5/16"','37 5/16"'),
               ('979','38 9/16"','38 9/16"'),
               ('1011','39 13/16"','39 13/16"'),
               ('1043','41 1/16"','41 1/16"'),
               ('1075','42 3/8"','24 3/4"'),
               ('1107','43 9/16"','26"'),
               ('1139','44 7/8"','27 1/4"'),
               ('1171','46 1/8"','28 1/2"'),
               ('1203','47 3/8"','29 3/4"'),
               ('1235','48 5/8"','31"'),
               ('1267','49 7/8"','32 1/4"'),
               ('1299','51 3/16"','33 9/16"'),
               ('1331','52 7/16"','34 3/4"'),
               ('1363','53 11/16"','36 1/16"'),
               ('1395','54 15/16"','37 5/16"'),
               ('1427','56 1/4"','38 9/16"'),
               ('1459','57 1/2"','39 13/16"'),
               ('1491','58 11/16"','41 1/16"'),
               ('1523','60"','24 3/4"'),
               ('1555','61 1/4"','26"'),
               ('1587','62 1/2"','27 1/4"'),
               ('1619','63 3/4"','28 1/2"'),
               ('1651','65"','29 3/4"'),
               ('1683','66 1/4"','31"'),
               ('1715','67 1/2"','32 1/4"'),
               ('1748','68 13/16"','33 9/16"'),
               ('1779','70 1/16"','34 3/4"'),
               ('1811','71 5/16"','36 1/16"'),
               ('1843','72 5/8"','37 5/16"'),
               ('1875','73 13/16"','38 9/16"'),
               ('1907','75 1/8"','39 13/16"'),
               ('1939','76 3/8"','41 1/16"'),
               ('1971','77 5/8"','27 1/4"'),
               ('2003','78 15/16"','28 1/2"'),
               ('2035','80 3/16"','29 3/4"'),
               ('2067','81 7/16"','31"'),
               ('2099','82 11/16"','32 1/4"'),
               ('2131','83 15/16"','33 9/16"'),
               ('2163','85 1/4"','34 3/4"'),
               ('2195','86 1/2"','36 1/16"'),
               ('2227','87 3/4"','37 5/16"'),
               ('2259','89"','38 9/16"'),
               ('2291','90 1/4"','39 13/16"'),
               ('2323','91 1/2"','41 1/16"'),
               ('2355','92 3/4"','24 3/4"'),
               ('2387','94"','26"'),
               ('2419','95 5/16"','27 1/4"'),
               ('2451','96 1/2"','28 1/2"'),
               ('2483','97 13/16','29 3/4"'),
               ('2515','99 1/16"','31"'),
               ('2547','100 5/16"','32 1/4"'),
               ('2579','101 5/8"','33 9/16"'),
               ('2611','102 7/8"','34 3/4"'),
               ('2643','104 1/8"','36 1/16"'),
               ('2675','106 5/8"','38 9/16"'),
               ('2707','107 15/16"','39 13/16"'),
               ('2739','109 1/8"','41 1/16"'),
               ('2771','110 7/8"','26"'),
               ('2807','111 11/16"','27 1/4"'),
               ('2835','112 15/16"','28 1/2"'),
               ('2867','114 3/16"','29 3/4"'),
               ('2899','114 3/16"','31"'),
               ('2931','115 1/2"','32 1/4"'),
               ('2963','116 3/4"','33 9/16"'),
               ('2995','118"','34 3/4"'),
               ('3027','119 1/4"','36 1/16"'),
               ('3059','120 1/2"','37 5/16"')]

END_CONDITIONS=[('EP','End Panel','EP (Panel Visible)'),
                ('WP','Wall Panel','WP (Panel Against Wall)'),
                ('CP','Center Panel','CP (Panel Against Panel)'),
                ('OFF','Off','Turn Off Side')]

def add_fixed_shelf_machining(part,product,index):
    Width = part.get_var('dim_y','Width')
    Length = part.get_var('dim_x','Length')
    if product:
        obj, left_token = part.add_machine_token('Left Drilling' ,'BORE','5')
        obj, right_token = part.add_machine_token('Right Drilling' ,'BORE','5')
        if index == 1:
            Left_End_Condition = product.get_var("Left End Condition")
            left_token.add_driver(obj,'dim_in_z','IF(Left_End_Condition==3,0,INCH(.5))',[Left_End_Condition])
            right_token.add_driver(obj,'dim_in_z','IF(Left_End_Condition==3,0,INCH(.5))',[Left_End_Condition])
        elif index == product.opening_qty + 1:
            Right_End_Condition = product.get_var("Right End Condition")
            left_token.add_driver(obj,'dim_in_z','IF(Right_End_Condition==3,0,INCH(.5))',[Right_End_Condition])
            right_token.add_driver(obj,'dim_in_z','IF(Right_End_Condition==3,0,INCH(.5))',[Right_End_Condition])
        else:
            left_token.dim_in_z = fd.inches(.5)
            right_token.dim_in_z = fd.inches(.5)
    else:
        obj, left_token = part.add_machine_token('Left Drilling' ,'BORE','5')
        obj, right_token = part.add_machine_token('Right Drilling' ,'BORE','5')
        left_token.dim_in_z = fd.inches(.5)
        right_token.dim_in_z = fd.inches(.5)
        
    left_token.dim_in_x = fd.millimeters(9)
    left_token.dim_in_y = fd.millimeters(37)
    left_token.face_bore_dia = 20
    left_token.end_dim_in_x  = fd.millimeters(9)
    left_token.add_driver(obj,'end_dim_in_y','fabs(Width)-INCH(1.4567)',[Width])
    left_token.add_driver(obj,'distance_between_holes','fabs(Width)-(INCH(1.4567)*2)',[Width])
    left_token.associative_dia = 0
    left_token.associative_depth = 0
    
    right_token.add_driver(obj,'dim_in_x','Length-INCH(.354)',[Length])
    right_token.dim_in_y = fd.millimeters(37)
    right_token.face_bore_dia = 20
    right_token.add_driver(obj,'end_dim_in_x','Length-INCH(.354)',[Length])
    right_token.add_driver(obj,'end_dim_in_y','fabs(Width)-INCH(1.4567)',[Width])
    right_token.add_driver(obj,'distance_between_holes','fabs(Width)-(INCH(1.4567)*2)',[Width])
    right_token.associative_dia = 0
    right_token.associative_depth = 0
    
def add_panel_drilling(part,product,index):
    Width = part.get_var('dim_y','Width')
    Height = part.get_var('dim_x','Height')
    Panel_Thickness = product.get_var('Panel Thickness')
    
    if index == 1:
        Height = product.get_var("Opening " + str(index) + " Height",'Height')
        Width = product.get_var("Opening " + str(index) + " Depth",'Width')
        Stop_LB = product.get_var("Opening " + str(index) + " Stop LB",'Stop_LB')
        Start_LB = product.get_var("Opening " + str(index) + " Start LB",'Start_LB')
        Drill_Thru_5 = product.get_var("Opening " + str(index) + " Drill Thru Left",'Drill_Thru_5')
        Add_Mid = product.get_var("Opening " + str(index) + " Add Mid Drilling",'Add_Mid')
        Remove_5 = product.get_var("Opening " + str(index) + " Remove Left Drill",'Remove_5')
    else:
        Height = product.get_var("Opening " + str(index - 1) + " Height",'Height')
        Width = product.get_var("Opening " + str(index - 1) + " Depth",'Width')
        Stop_LB = product.get_var("Opening " + str(index - 1) + " Stop LB",'Stop_LB')
        Start_LB = product.get_var("Opening " + str(index - 1) + " Start LB",'Start_LB')
        Drill_Thru_5 = product.get_var("Opening " + str(index - 1) + " Drill Thru Right",'Drill_Thru_5')
        Add_Mid = product.get_var("Opening " + str(index - 1) + " Add Mid Drilling",'Add_Mid')
        Remove_5 = product.get_var("Opening " + str(index - 1) + " Remove Left Drill",'Remove_5')

    obj, token = part.add_machine_token('Drilling Front Bottom 5' ,'BORE','5')
    token.dim_in_x = fd.millimeters(9.5)
    token.dim_in_y = fd.inches(1.4567)
    token.add_driver(obj,'dim_in_z','IF(Remove_5,0,IF(Drill_Thru_5,Panel_Thickness,INCH(.5)))',[Drill_Thru_5,Panel_Thickness,Remove_5])
    token.face_bore_dia = 5
    token.add_driver(obj,'end_dim_in_x','IF(Stop_LB==0,Height,Stop_LB)',[Height,Stop_LB])
    token.end_dim_in_y  = fd.inches(1.4567)
    token.distance_between_holes = fd.millimeters(32) #7
    token.associative_dia = 0 
    token.associative_depth = 0 

    obj, token = part.add_machine_token('Drilling Rear Bottom 5' ,'BORE','5')
    token.dim_in_x = fd.millimeters(9.5)
    token.add_driver(obj, 'dim_in_y','fabs(Width)-INCH(1.4567)',[Width])
    token.dim_in_z = fd.inches(1) 
    token.add_driver(obj,'dim_in_z','IF(Remove_5,0,IF(Drill_Thru_5,Panel_Thickness,INCH(.5)))',[Drill_Thru_5,Panel_Thickness,Remove_5])
    token.face_bore_dia = 5
    token.add_driver(obj,'end_dim_in_x','IF(Stop_LB==0,Height,Stop_LB)',[Height,Stop_LB])
    token.add_driver(obj,'end_dim_in_y','fabs(Width)-INCH(1.4567)',[Width])
    token.distance_between_holes = fd.millimeters(32) 
    token.associative_dia = 0 
    token.associative_depth = 0 

    obj, token = part.add_machine_token('Drilling Mid Bottom 5' ,'BORE','5')
    token.dim_in_x = fd.millimeters(9.5)
    token.dim_in_y = fd.inches(12 - 1.4567)
    token.add_driver(obj,'dim_in_z','IF(Remove_5,0,IF(Add_Mid,IF(Drill_Thru_5,Panel_Thickness,INCH(.5)),0))',[Drill_Thru_5,Add_Mid,Panel_Thickness,Remove_5])
    token.face_bore_dia = 5
    token.add_driver(obj,'end_dim_in_x','IF(Stop_LB==0,Height,Stop_LB)',[Height,Stop_LB])
    token.end_dim_in_y  = fd.inches(12 - 1.4567)
    token.distance_between_holes = fd.millimeters(32) #7
    token.associative_dia = 0 
    token.associative_depth = 0 
    
    #TOP
    
    obj, token = part.add_machine_token('Drilling Front Top 5' ,'BORE','5')
    token.add_driver(obj,'dim_in_x','Start_LB',[Start_LB])
    token.dim_in_y = fd.inches(1.4567)
    token.add_driver(obj,'dim_in_z','IF(Remove_5,0,IF(Start_LB>0,IF(Drill_Thru_5,Panel_Thickness,INCH(.5)),0))',[Drill_Thru_5,Panel_Thickness,Remove_5,Start_LB])
    token.face_bore_dia = 5
    token.add_driver(obj,'end_dim_in_x','Height',[Height])
    token.end_dim_in_y  = fd.inches(1.4567)
    token.distance_between_holes = fd.millimeters(32) #7
    token.associative_dia = 0 
    token.associative_depth = 0 

    obj, token = part.add_machine_token('Drilling Rear Top 5' ,'BORE','5')
    token.add_driver(obj,'dim_in_x','Start_LB',[Start_LB])
    token.add_driver(obj, 'dim_in_y','fabs(Width)-INCH(1.4567)',[Width])
    token.dim_in_z = fd.inches(1) 
    token.add_driver(obj,'dim_in_z','IF(Remove_5,0,IF(Start_LB>0,IF(Drill_Thru_5,Panel_Thickness,INCH(.5)),0))',[Drill_Thru_5,Panel_Thickness,Remove_5,Start_LB])
    token.face_bore_dia = 5
    token.add_driver(obj,'end_dim_in_x','Height',[Height])
    token.add_driver(obj,'end_dim_in_y','fabs(Width)-INCH(1.4567)',[Width])
    token.distance_between_holes = fd.millimeters(32) 
    token.associative_dia = 0 
    token.associative_depth = 0 

    obj, token = part.add_machine_token('Drilling Mid Top 5' ,'BORE','5')
    token.add_driver(obj,'dim_in_x','Start_LB',[Start_LB])
    token.dim_in_y = fd.inches(12 - 1.4567)
    token.add_driver(obj,'dim_in_z','IF(Remove_5,0,IF(Add_Mid,IF(Start_LB>0,IF(Drill_Thru_5,Panel_Thickness,INCH(.5)),0),0))',[Drill_Thru_5,Panel_Thickness,Remove_5,Add_Mid,Start_LB])
    token.face_bore_dia = 5
    token.add_driver(obj,'end_dim_in_x','Height',[Height])
    token.end_dim_in_y  = fd.inches(12 - 1.4567)
    token.distance_between_holes = fd.millimeters(32) #7
    token.associative_dia = 0 
    token.associative_depth = 0 
    
    if index != 1 and index != product.opening_qty + 1:
        Height = product.get_var("Opening " + str(index) + " Height",'Height')
        Width = product.get_var("Opening " + str(index) + " Depth",'Width')
        Stop_LB_6 = product.get_var("Opening " + str(index) + " Stop LB",'Stop_LB_6')
        Start_LB_6 = product.get_var("Opening " + str(index) + " Start LB",'Start_LB_6')
        Drill_Thru_6 = product.get_var("Opening " + str(index) + " Drill Thru Left",'Drill_Thru_6')
        Add_Mid_6 = product.get_var("Opening " + str(index) + " Add Mid Drilling",'Add_Mid_6')
        Remove_6 = product.get_var("Opening " + str(index) + " Remove Left Drill",'Remove_6')

        obj, token = part.add_machine_token('Drilling Front Bottom 6' ,'BORE','6')
        token.dim_in_x = fd.millimeters(9.5)
        token.dim_in_y = fd.inches(1.4567)
        token.add_driver(obj,'dim_in_z','IF(Remove_6,0,IF(Drill_Thru_6,Panel_Thickness,INCH(.5)))',[Remove_6,Drill_Thru_6,Panel_Thickness])
        token.face_bore_dia = 5
        token.add_driver(obj,'end_dim_in_x','IF(Stop_LB_6==0,Height,Stop_LB_6)',[Height,Stop_LB_6])
        token.end_dim_in_y  = fd.inches(1.4567)
        token.distance_between_holes = fd.millimeters(32)
        token.associative_dia = 0 
        token.associative_depth = 0 
        
        obj, token = part.add_machine_token('Drilling Rear Bottom 6' ,'BORE','6')
        token.dim_in_x = fd.millimeters(9.5)
        token.add_driver(obj, 'dim_in_y','fabs(Width)-INCH(1.4567)',[Width])
        token.add_driver(obj,'dim_in_z','IF(Remove_6,0,IF(Drill_Thru_6,Panel_Thickness,INCH(.5)))',[Remove_6,Drill_Thru_6,Panel_Thickness])
        token.face_bore_dia = 5 
        token.add_driver(obj,'end_dim_in_x','IF(Stop_LB_6==0,Height,Stop_LB_6)',[Height,Stop_LB_6])
        token.add_driver(obj,'end_dim_in_y','fabs(Width)-INCH(1.4567)',[Width])
        token.distance_between_holes = fd.millimeters(32) 
        token.associative_dia = 0 
        token.associative_depth = 0 
        
        obj, token = part.add_machine_token('Drilling Mid Bottom 6' ,'BORE','6')
        token.dim_in_x = fd.millimeters(9.5)
        token.dim_in_y = fd.inches(12 - 1.4567)
        token.add_driver(obj,'dim_in_z','IF(Remove_6,0,IF(Add_Mid_6,IF(Drill_Thru_6,Panel_Thickness,INCH(.5)),0))',[Remove_6,Add_Mid_6,Drill_Thru_6,Panel_Thickness])
        token.face_bore_dia = 5
        token.add_driver(obj,'end_dim_in_x','IF(Stop_LB_6==0,Height,Stop_LB_6)',[Height,Stop_LB_6])
        token.end_dim_in_y  = fd.inches(12 - 1.4567)
        token.distance_between_holes = fd.millimeters(32)
        token.associative_dia = 0
        token.associative_depth = 0
        
        #TOP
        
        obj, token = part.add_machine_token('Drilling Front Top 6' ,'BORE','6')
        token.add_driver(obj,'dim_in_x','Start_LB_6',[Start_LB_6])
        token.dim_in_y = fd.inches(1.4567)
        token.add_driver(obj,'dim_in_z','IF(Remove_6,0,IF(Start_LB_6>0,IF(Drill_Thru_6,Panel_Thickness,INCH(.5)),0))',[Remove_6,Drill_Thru_6,Panel_Thickness,Start_LB_6])
        token.face_bore_dia = 5
        token.add_driver(obj,'end_dim_in_x','Height',[Height])
        token.end_dim_in_y  = fd.inches(1.4567)
        token.distance_between_holes = fd.millimeters(32)
        token.associative_dia = 0
        token.associative_depth = 0
        
        obj, token = part.add_machine_token('Drilling Rear Top 6' ,'BORE','6')
        token.add_driver(obj,'dim_in_x','Start_LB_6',[Start_LB_6])
        token.add_driver(obj, 'dim_in_y','fabs(Width)-INCH(1.4567)',[Width])
        token.add_driver(obj,'dim_in_z','IF(Remove_6,0,IF(Start_LB_6>0,IF(Drill_Thru_6,Panel_Thickness,INCH(.5)),0))',[Remove_6,Drill_Thru_6,Panel_Thickness,Start_LB_6])
        token.face_bore_dia = 5 
        token.add_driver(obj,'end_dim_in_x','Height',[Height])
        token.add_driver(obj,'end_dim_in_y','fabs(Width)-INCH(1.4567)',[Width])
        token.distance_between_holes = fd.millimeters(32) 
        token.associative_dia = 0
        token.associative_depth = 0
        
        obj, token = part.add_machine_token('Drilling Mid Top 6' ,'BORE','6')
        token.add_driver(obj,'dim_in_x','Start_LB_6',[Start_LB_6])
        token.dim_in_y = fd.inches(12 - 1.4567)
        token.add_driver(obj,'dim_in_z','IF(Remove_6,0,IF(Add_Mid_6,IF(Start_LB_6>0,IF(Drill_Thru_6,Panel_Thickness,INCH(.5)),0),0))',[Remove_6,Drill_Thru_6,Panel_Thickness,Start_LB_6,Add_Mid_6])
        token.face_bore_dia = 5
        token.add_driver(obj,'end_dim_in_x','Height',[Height])
        token.end_dim_in_y  = fd.inches(12 - 1.4567)
        token.distance_between_holes = fd.millimeters(32)
        token.associative_dia = 0
        token.associative_depth = 0

class Material_Pointers():
    
    Exposed_Exterior_Surface = fd.Material_Pointer(EXPOSED_CABINET_MATERIAL)
    Exposed_Exterior_Edge = fd.Material_Pointer(EXPOSED_CABINET_MATERIAL)

class Cutpart_Pointers():
    
    Closet_Panel = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                      core="Exposed_Exterior_Surface",
                                      top="Exposed_Exterior_Surface",
                                      bottom="Exposed_Exterior_Surface")

    Closet_Shelf = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                      core="Exposed_Exterior_Surface",
                                      top="Exposed_Exterior_Surface",
                                      bottom="Exposed_Exterior_Surface")

    Closet_Toe_Kick = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                         core="Exposed_Exterior_Surface",
                                         top="Exposed_Exterior_Surface",
                                         bottom="Exposed_Exterior_Surface")
    
    Closet_Back = fd.Cutpart_Pointer(thickness=fd.inches(.75),
                                     core="Exposed_Exterior_Surface",
                                     top="Exposed_Exterior_Surface",
                                     bottom="Exposed_Exterior_Surface")
    
class Edgepart_Pointers():
    
    Closet_Body_Edges = fd.Edgepart_Pointer(thickness=fd.inches(.01),
                                            material="Exposed_Exterior_Edge")

#---------PRODUCT TEMPLATES

class Opening_Bays(fd.Library_Assembly):
    
    library_name = "Closets"
    property_id = "closets.opening_starter"
    type_assembly = "PRODUCT"
    product_shape = "CUSTOM"
    
    product_type = "Base" # {Base, Tall, Upper, Sink, Suspended}
    opening_qty = 2
    
    angle_back = False
    
    def add_opening_prompts(self):
        self.add_tab(name='Opening Widths',tab_type='CALCULATOR',calc_type="XDIM")   
        
        for i in range(1,self.opening_qty+1):
            self.add_prompt(name="Opening " + str(i) + " Width",
                            prompt_type='DISTANCE',
                            value=0,
                            tab_index=0,
                            equal=True)
            
            self.add_prompt(name="Opening " + str(i) + " Depth",
                            prompt_type='DISTANCE',
                            value=self.depth,
                            tab_index=1)
            
            self.add_prompt(name="Opening " + str(i) + " Height",
                            prompt_type='DISTANCE',
                            value=self.height,
                            tab_index=1)
        
    def add_machining_prompts(self):
        self.add_tab(name='Machining Options',tab_type='VISIBLE') #3
        
        for i in range(1,self.opening_qty+1):
            self.add_prompt(name="Opening " + str(i) + " Stop LB",
                            prompt_type='DISTANCE',
                            value=0,
                            tab_index=3,
                            equal=True)
            
            self.add_prompt(name="Opening " + str(i) + " Start LB",
                            prompt_type='DISTANCE',
                            value=0,
                            tab_index=3,
                            equal=True)
            
            self.add_prompt(name="Opening " + str(i) + " Add Mid Drilling",
                            prompt_type='CHECKBOX',
                            value=False,
                            tab_index=3)
            
            self.add_prompt(name="Opening " + str(i) + " Drill Thru Left",
                            prompt_type='CHECKBOX',
                            value=False,
                            tab_index=3)
        
            self.add_prompt(name="Opening " + str(i) + " Drill Thru Right",
                            prompt_type='CHECKBOX',
                            value=False,
                            tab_index=3)
        
            self.add_prompt(name="Opening " + str(i) + " Remove Left Drill",
                            prompt_type='CHECKBOX',
                            value=False,
                            tab_index=3)
        
            self.add_prompt(name="Opening " + str(i) + " Remove Right Drill",
                            prompt_type='CHECKBOX',
                            value=False,
                            tab_index=3)
        
    def add_carcass_prompts(self):
        g = bpy.context.scene.lm_closets
        self.add_tab(name='Carcass Options',tab_type='VISIBLE') #1
        self.add_tab(name='Formulas',tab_type='HIDDEN') #2
        
        self.add_prompt(name="Left End Condition",prompt_type='COMBOBOX',items=['EP','WP','CP','OFF'],value=1,tab_index=1,columns=4)
        self.add_prompt(name="Right End Condition",prompt_type='COMBOBOX',items=['EP','WP','CP','OFF'],value=1,tab_index=1,columns=4)
        self.add_prompt(name="Left Side Wall Filler",prompt_type='DISTANCE',value=0.0,tab_index=1)
        self.add_prompt(name="Right Side Wall Filler",prompt_type='DISTANCE',value=0.0,tab_index=1)
        self.add_prompt(name="Toe Kick Height",prompt_type='DISTANCE',value=g.Toe_Kick_Height,tab_index=1)
        self.add_prompt(name="Toe Kick Setback",prompt_type='DISTANCE',value=g.Toe_Kick_Setback,tab_index=1)
        self.add_prompt(name="Add Backing",prompt_type='CHECKBOX',value=g.Add_Backing,tab_index=1)
        
        self.add_prompt(name="Add Top Accent Shelf",prompt_type='CHECKBOX',value=g.Add_Top_Accent_Shelf,tab_index=1)
        self.add_prompt(name="Top Shelf Overhang",prompt_type='DISTANCE',value=g.Top_Shelf_Overhang,tab_index=1)
        self.add_prompt(name="Crown Molding Height",prompt_type='DISTANCE',value=g.Crown_Molding_Height,tab_index=1)
        self.add_prompt(name="Crown Molding Depth",prompt_type='DISTANCE',value=g.Crown_Molding_Depth,tab_index=1)
        
        self.add_prompt(name="Panel Thickness",prompt_type='DISTANCE',value=fd.inches(0.75),tab_index=2)
        self.add_prompt(name="Left Side Thickness",prompt_type='DISTANCE',value=fd.inches(0.75),tab_index=2)
        self.add_prompt(name="Right Side Thickness",prompt_type='DISTANCE',value=fd.inches(0.75),tab_index=2)
        self.add_prompt(name="Back Thickness",prompt_type='DISTANCE',value=fd.inches(0.25),tab_index=2)
        self.add_prompt(name="Shelf Thickness",prompt_type='DISTANCE',value=fd.inches(0.75),tab_index=2)
        self.add_prompt(name="Largest Opening Size",prompt_type='DISTANCE',value=fd.inches(42),tab_index=2)
        
        Left_End_Condition = self.get_var('Left End Condition')
        Right_End_Condition = self.get_var('Right End Condition')
        Panel_Thickness = self.get_var('Panel Thickness')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Right_Side_Thickness = self.get_var('Right Side Thickness')
        sgi = self.get_var('cabinetlib.spec_group_index','sgi')
        
        self.prompt("Left Side Thickness", 'IF(Left_End_Condition!=3,THICKNESS(sgi,"Closet_Panel"),0)',[Left_End_Condition,sgi])
        self.prompt("Right Side Thickness", 'IF(Right_End_Condition!=3,THICKNESS(sgi,"Closet_Panel"),0)',[Right_End_Condition,sgi])
        self.prompt("Panel Thickness", 'THICKNESS(sgi,"Closet_Panel")',[sgi])
        
        self.calculator_deduction("Left_Side_Thickness+Right_Side_Thickness+Panel_Thickness*(" + str(self.opening_qty) +"-1)",[Left_Side_Thickness,Right_Side_Thickness,Panel_Thickness])
        
    def get_last_opening_depth_formula(self):
        if self.opening_qty == 1:
            Depth_1 = self.get_var('Opening 1 Depth','Depth_1')
            return Depth_1, "Depth_1"
        if self.opening_qty == 2:
            Depth_2 = self.get_var('Opening 2 Depth','Depth_2')
            return Depth_2, "Depth_2"
        if self.opening_qty == 3:
            Depth_3 = self.get_var('Opening 3 Depth','Depth_3')
            return Depth_3, "Depth_3"
        if self.opening_qty == 4:
            Depth_4 = self.get_var('Opening 4 Depth','Depth_4')
            return Depth_4, "Depth_4"
        if self.opening_qty == 5:
            Depth_5 = self.get_var('Opening 5 Depth','Depth_5')
            return Depth_5, "Depth_5"
        if self.opening_qty == 6:
            Depth_6 = self.get_var('Opening 6 Depth','Depth_6')
            return Depth_6, "Depth_6"
        if self.opening_qty == 7:
            Depth_7 = self.get_var('Opening 7 Depth','Depth_7')
            return Depth_7, "Depth_7"
        if self.opening_qty == 8:
            Depth_8 = self.get_var('Opening 8 Depth','Depth_8')
            return Depth_8, "Depth_8"
        
    def get_last_opening_height_formula(self):
        if self.opening_qty == 1:
            Height_1 = self.get_var('Opening 1 Height','Height_1')
            return Height_1, "Height_1"
        if self.opening_qty == 2:
            Height_2 = self.get_var('Opening 2 Height','Height_2')
            return Height_2, "Height_2"
        if self.opening_qty == 3:
            Height_3 = self.get_var('Opening 3 Height','Height_3')
            return Height_3, "Height_3"
        if self.opening_qty == 4:
            Height_4 = self.get_var('Opening 4 Height','Height_4')
            return Height_4, "Height_4"
        if self.opening_qty == 5:
            Height_5 = self.get_var('Opening 5 Height','Height_5')
            return Height_5, "Height_5"
        if self.opening_qty == 6:
            Height_6 = self.get_var('Opening 6 Height','Height_6')
            return Height_6, "Height_6"
        if self.opening_qty == 7:
            Height_7 = self.get_var('Opening 7 Height','Height_7')
            return Height_7, "Height_7"
        if self.opening_qty == 8:
            Height_8 = self.get_var('Opening 8 Height','Height_8')
            return Height_8, "Height_8"
        
    def add_sides(self):
        Product_Width = self.get_var('dim_x','Product_Width')
        Left_Side_Wall_Filler = self.get_var('Left Side Wall Filler')
        Right_Side_Wall_Filler = self.get_var('Right Side Wall Filler')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Right_Side_Thickness = self.get_var('Right Side Thickness')
        Depth_1 = self.get_var('Opening 1 Depth','Depth_1')
        Height_1 = self.get_var('Opening 1 Height','Height_1')
        Add_Backing = self.get_var('Add Backing')
        Back_Thickness = self.get_var('Back Thickness')
        Left_End_Condition = self.get_var('Left End Condition')
        Right_End_Condition = self.get_var('Right End Condition')
        
        left_filler = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        left_filler.set_name("Left Filler")
        left_filler.x_dim('Height_1',[Height_1])
        left_filler.y_dim('-Left_Side_Wall_Filler',[Left_Side_Wall_Filler])
        left_filler.z_dim('Left_Side_Thickness',[Left_Side_Thickness])
        left_filler.x_loc(value = 0)
        left_filler.y_loc('-Depth_1',[Depth_1])
        left_filler.z_loc(value = 0)
        left_filler.x_rot(value = 0)
        left_filler.y_rot(value = -90)
        left_filler.z_rot(value = -90)
        left_filler.prompt('Hide','IF(Left_Side_Wall_Filler==0,True,False)',[Left_Side_Wall_Filler])
        left_filler.cutpart("Closet_Panel")

        left_side = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        left_side.set_name("Left Side")
        left_side.x_dim('Height_1',[Height_1])
        left_side.y_dim('-Depth_1',[Depth_1])
        left_side.z_dim('-Left_Side_Thickness',[Left_Side_Thickness])
        left_side.x_loc(value = 0)
        left_side.y_loc('IF(Add_Backing,-Back_Thickness,0)',[Add_Backing,Back_Thickness])
        left_side.z_loc(value = 0)
        left_side.x_rot(value = 0)
        left_side.y_rot(value = -90)
        left_side.z_rot(value = 0)
        left_side.prompt('Hide','IF(Left_End_Condition==3,True,False)',[Left_End_Condition])
        left_side.cutpart("Closet_Panel")
        left_side.edgebanding("Closet_Body_Edges",l1 = True)
        add_panel_drilling(left_side,self,1)
        
        right_filler = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        right_filler.set_name("Right Filler")
        right_filler.x_dim(self.get_last_opening_height_formula()[1],[self.get_last_opening_height_formula()[0]])
        right_filler.y_dim('Right_Side_Wall_Filler',[Right_Side_Wall_Filler])
        right_filler.z_dim('Left_Side_Thickness',[Left_Side_Thickness])
        right_filler.x_loc('Product_Width',[Product_Width])
        right_filler.y_loc('-' + self.get_last_opening_depth_formula()[1],[self.get_last_opening_depth_formula()[0]])
        right_filler.z_loc(value = 0)
        right_filler.x_rot(value = 0)
        right_filler.y_rot(value = -90)
        right_filler.z_rot(value = -90)
        right_filler.prompt('Hide','IF(Right_Side_Wall_Filler==0,True,False)',[Right_Side_Wall_Filler])
        right_filler.cutpart("Closet_Panel")
        
        right_side = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        right_side.set_name("Right Side")
        right_side.x_dim(self.get_last_opening_height_formula()[1],[self.get_last_opening_height_formula()[0]])
        right_side.y_dim('-' + self.get_last_opening_depth_formula()[1],[self.get_last_opening_depth_formula()[0]])
        right_side.z_dim('Right_Side_Thickness',[Right_Side_Thickness])
        right_side.x_loc('Product_Width',[Product_Width])
        right_side.y_loc('IF(Add_Backing,-Back_Thickness,0)',[Add_Backing,Back_Thickness])
        right_side.z_loc(value = 0)
        right_side.x_rot(value = 0)
        right_side.y_rot(value = -90)
        right_side.z_rot(value = 0)
        right_side.prompt('Hide','IF(Right_End_Condition==3,True,False)',[Right_End_Condition])
        right_side.cutpart("Closet_Panel")
        right_side.edgebanding("Closet_Body_Edges",l1 = True)
        add_panel_drilling(right_side,self,self.opening_qty+1)

    def add_panel(self,i):
        Product_Width = self.get_var('dim_x','Product_Width')
        Thickness = self.get_var('Panel Thickness','Thickness')
        Left_Side_Thickness = self.get_var('Left Side Thickness')
        Add_Backing = self.get_var('Add Backing')
        Back_Thickness = self.get_var('Back Thickness')
        Width_1 = self.get_var('Opening 1 Width','Width_1')
        Depth_1 = self.get_var('Opening 1 Depth','Depth_1')
        Height_1 = self.get_var('Opening 1 Height','Height_1')
        
        panel_x_loc_vars = [Product_Width,Thickness,Width_1,Left_Side_Thickness]
        panel_x_loc_expression = 'Left_Side_Thickness+Width_1+Thickness'
        Depth_2 = self.get_var('Opening 2 Depth','Depth_2')
        Height_2 = self.get_var('Opening 2 Height','Height_2')
        panel_depth_vars = [Depth_1,Depth_2]
        panel_depth_expression = "-max(Depth_1,Depth_2)"
        panel_height_vars = [Height_1,Height_2]
        panel_height_expression = "max(Height_1,Height_2)"
        if i > 1:
            Width_2 = self.get_var('Opening 2 Width','Width_2')
            panel_x_loc_vars.append(Width_2)
            panel_x_loc_expression = 'Left_Side_Thickness+Width_1+Width_2+(Thickness*2)'
            Depth_3 = self.get_var('Opening 3 Depth','Depth_3')
            Height_3 = self.get_var('Opening 3 Height','Height_3')
            panel_depth_vars = [Depth_2,Depth_3]
            panel_depth_expression = "-max(Depth_2,Depth_3)"
            panel_height_vars = [Height_2,Height_3]
            panel_height_expression = "max(Height_2,Height_3)"
        if i > 2:
            Width_3 = self.get_var('Opening 3 Width','Width_3')
            panel_x_loc_vars.append(Width_3)
            panel_x_loc_expression = 'Left_Side_Thickness+Width_1+Width_2+Width_3+(Thickness*3)'
            Depth_4 = self.get_var('Opening 4 Depth','Depth_4')
            Height_4 = self.get_var('Opening 4 Height','Height_4')
            panel_depth_vars = [Depth_3,Depth_4]
            panel_depth_expression = "-max(Depth_3,Depth_4)"
            panel_height_vars = [Height_3,Height_4]
            panel_height_expression = "max(Height_3,Height_4)"
        if i > 3:
            Width_4 = self.get_var('Opening 4 Width','Width_4')
            panel_x_loc_vars.append(Width_4)
            panel_x_loc_expression = 'Left_Side_Thickness+Width_1+Width_2+Width_3+Width_4+(Thickness*4)'
            Depth_5 = self.get_var('Opening 5 Depth','Depth_5')
            Height_5 = self.get_var('Opening 5 Height','Height_5')
            panel_depth_vars = [Depth_4,Depth_5]
            panel_depth_expression = "-max(Depth_4,Depth_5)"
            panel_height_vars = [Height_4,Height_5]
            panel_height_expression = "max(Height_4,Height_5)"
        if i > 4:
            Width_5 = self.get_var('Opening 5 Width','Width_5')
            panel_x_loc_vars.append(Width_5)
            panel_x_loc_expression = 'Left_Side_Thickness+Width_1+Width_2+Width_3+Width_4+Width_5+(Thickness*5)'
            Depth_6 = self.get_var('Opening 6 Depth','Depth_6')
            Height_6 = self.get_var('Opening 6 Height','Height_6')
            panel_depth_vars = [Depth_5,Depth_6]
            panel_depth_expression = "-max(Depth_5,Depth_6)"
            panel_height_vars = [Height_5,Height_6]
            panel_height_expression = "max(Height_5,Height_6)"
        if i > 5:
            Width_6 = self.get_var('Opening 6 Width','Width_6')
            panel_x_loc_vars.append(Width_6)
            panel_x_loc_expression = 'Left_Side_Thickness+Width_1+Width_2+Width_3+Width_4+Width_5+Width_6+(Thickness*6)'
            Depth_7 = self.get_var('Opening 7 Depth','Depth_7')
            Height_7 = self.get_var('Opening 7 Height','Height_7')
            panel_depth_vars = [Depth_6,Depth_7]
            panel_depth_expression = "-max(Depth_6,Depth_7)"
            panel_height_vars = [Height_6,Height_7]
            panel_height_expression = "max(Height_6,Height_7)"
        if i > 6:
            Width_7 = self.get_var('Opening 7 Width','Width_7')
            panel_x_loc_vars.append(Width_7)
            panel_x_loc_expression = 'Left_Side_Thickness+Width_1+Width_2+Width_3+Width_4+Width_5+Width_6+Width_7+(Thickness*7)'
            Depth_8 = self.get_var('Opening 8 Depth','Depth_8')
            Height_8 = self.get_var('Opening 8 Height','Height_8')
            panel_depth_vars = [Depth_7,Depth_8]
            panel_depth_expression = "-max(Depth_7,Depth_8)"
            panel_height_vars = [Height_7,Height_8]
            panel_height_expression = "max(Height_7,Height_8)"
        if i > 7:
            Width_8 = self.get_var('Opening 8 Width','Width_8')
            panel_x_loc_vars.append(Width_8)
            panel_x_loc_expression = 'Left_Side_Thickness+Width_1+Width_2+Width_3+Width_4+Width_5+Width_6+Width_7+Width_8+(Thickness*8)'
            Depth_9 = self.get_var('Opening 9 Depth','Depth_9')
            Height_9 = self.get_var('Opening 9 Height','Height_9')
            panel_depth_vars = [Depth_8,Depth_9]
            panel_depth_expression = "-max(Depth_8,Depth_9)"
            panel_height_vars = [Height_8,Height_9]
            panel_height_expression = "max(Height_8,Height_9)"
        
        panel = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        panel.set_name("Center Panel " + str(i))
        panel.x_loc(panel_x_loc_expression,panel_x_loc_vars)
        panel.y_loc('IF(Add_Backing,-Back_Thickness,0)',[Add_Backing,Back_Thickness])
        panel.z_loc(value = 0)
        panel.x_rot(value = 0)
        panel.y_rot(value = -90)
        panel.z_rot(value = 0)
        panel.x_dim(panel_height_expression,panel_height_vars)
        panel.y_dim(panel_depth_expression,panel_depth_vars)
        panel.z_dim('Thickness',[Thickness])
        panel.cutpart("Closet_Panel")
        panel.edgebanding("Closet_Body_Edges",l1 = True)
        add_panel_drilling(panel,self,i)
        return panel
        
    def add_top(self,i,panel):
        Width = self.get_var('Opening ' + str(i) + ' Width','Width')
        Depth = self.get_var('Opening ' + str(i) + ' Depth','Depth')
        Height = self.get_var('Opening ' + str(i) + ' Height','Height')
        Add_Backing = self.get_var('Add Backing')
        Back_Thickness = self.get_var('Back Thickness')
        Shelf_Thickness = self.get_var('Shelf Thickness')
        
        if panel:
            X_Loc = panel.get_var('loc_x','X_Loc')
        else:
            X_Loc = self.get_var('Left Side Thickness','X_Loc')
        
        top = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        top.set_name("Top Shelf " + str(i))
        top.x_loc('X_Loc',[X_Loc])
        top.y_loc('IF(Add_Backing,-Back_Thickness,0)',[Add_Backing,Back_Thickness])
        top.z_loc('Height',[Height])
        top.x_rot(value = 0)
        top.y_rot(value = 0)
        top.z_rot(value = 0)
        top.x_dim('Width',[Width])
        top.y_dim("-Depth",[Depth])
        top.z_dim('-Shelf_Thickness',[Shelf_Thickness])
        top.cutpart("Closet_Shelf")
        top.edgebanding("Closet_Body_Edges",l1 = True)
        add_fixed_shelf_machining(top,self,i)
    
    def add_bottom(self,i,panel):
        Width = self.get_var('Opening ' + str(i) + ' Width','Width')
        Depth = self.get_var('Opening ' + str(i) + ' Depth','Depth')
        Add_Backing = self.get_var('Add Backing')
        Back_Thickness = self.get_var('Back Thickness')
        Shelf_Thickness = self.get_var('Shelf Thickness')
        Toe_Kick_Height = self.get_var('Toe Kick Height')

        if panel:
            X_Loc = panel.get_var('loc_x','X_Loc')
        else:
            X_Loc = self.get_var('Left Side Thickness','X_Loc')
        
        bottom = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        bottom.set_name("Bottom Shelf " + str(i))
        bottom.x_loc('X_Loc',[X_Loc])
        bottom.y_loc('IF(Add_Backing,-Back_Thickness,0)',[Add_Backing,Back_Thickness])
        bottom.z_loc('Toe_Kick_Height',[Toe_Kick_Height])
        bottom.x_rot(value = 0)
        bottom.y_rot(value = 0)
        bottom.z_rot(value = 0)
        bottom.x_dim('Width',[Width])
        bottom.y_dim("-Depth",[Depth])
        bottom.z_dim('Shelf_Thickness',[Shelf_Thickness])
        bottom.cutpart("Closet_Shelf")
        bottom.edgebanding("Closet_Body_Edges",l1 = True)
        add_fixed_shelf_machining(bottom,self,i)
    
    def add_system_holes(self,i,panel):
        Width = self.get_var('Opening ' + str(i) + ' Width','Width')
        Height = self.get_var('Opening ' + str(i) + ' Height','Height')
        Depth = self.get_var('Opening ' + str(i) + ' Depth','Depth')
        Add_Backing = self.get_var('Add Backing')
        Back_Thickness = self.get_var('Back Thickness')
        Left_End_Condition = self.get_var('Left End Condition')
        Right_End_Condition = self.get_var('Right End Condition')
        
        Stop_LB = self.get_var("Opening " + str(i) + " Stop LB",'Stop_LB')
        Start_LB = self.get_var("Opening " + str(i) + " Start LB",'Start_LB')
        Drill_Thru_Left = self.get_var("Opening " + str(i) + " Drill Thru Left",'Drill_Thru_Left')
        Drill_Thru_Right = self.get_var("Opening " + str(i) + " Drill Thru Right",'Drill_Thru_Right')
        Add_Mid = self.get_var("Opening " + str(i) + " Add Mid Drilling",'Add_Mid')
        Remove_Left = self.get_var("Opening " + str(i) + " Remove Left Drill",'Remove_Left')
        Remove_Right = self.get_var("Opening " + str(i) + " Remove Right Drill",'Remove_Right')
        Panel_Thickness = self.get_var('Panel Thickness')
        
        if panel:
            X_Loc = panel.get_var('loc_x','X_Loc')
        else:
            X_Loc = self.get_var('Left Side Thickness','X_Loc')
            
        ass_list = []
            
        lfb_holes = self.add_assembly(LINE_BORE)
        lfb_holes.set_name("Left Front Bottom Holes " + str(i))
        ass_list.append(lfb_holes)
        lrb_holes = self.add_assembly(LINE_BORE)
        lrb_holes.set_name("Left Rear Bottom Holes " + str(i))
        ass_list.append(lrb_holes)
        rfb_holes = self.add_assembly(LINE_BORE)
        rfb_holes.set_name("Right Front Bottom Holes " + str(i))
        ass_list.append(rfb_holes)
        rrb_holes = self.add_assembly(LINE_BORE)
        rrb_holes.set_name("Right Rear Bottom Holes " + str(i))
        ass_list.append(rrb_holes)
        lfb_holes = self.add_assembly(LINE_BORE)
        lfb_holes.set_name("Left Front Top Holes " + str(i))
        ass_list.append(lfb_holes)
        lrb_holes = self.add_assembly(LINE_BORE)
        lrb_holes.set_name("Left Rear Top Holes " + str(i))
        ass_list.append(lrb_holes)
        rfb_holes = self.add_assembly(LINE_BORE)
        rfb_holes.set_name("Right Front Top Holes " + str(i))
        ass_list.append(rfb_holes)
        rrb_holes = self.add_assembly(LINE_BORE)
        rrb_holes.set_name("Right Rear Top Holes " + str(i))
        ass_list.append(rrb_holes)
        rfb_holes = self.add_assembly(LINE_BORE)
        rfb_holes.set_name("Left Mid Top Holes " + str(i))
        ass_list.append(rfb_holes)
        rrb_holes = self.add_assembly(LINE_BORE)
        rrb_holes.set_name("Right Mid Top Holes " + str(i))
        ass_list.append(rrb_holes)
        rfb_holes = self.add_assembly(LINE_BORE)
        rfb_holes.set_name("Left Mid Bottom Holes " + str(i))
        ass_list.append(rfb_holes)
        rrb_holes = self.add_assembly(LINE_BORE)
        rrb_holes.set_name("Right Mid Bottom Holes " + str(i))
        ass_list.append(rrb_holes)
        
        for ass in ass_list:
 
            ass.x_rot(value = 0)
            ass.y_rot(value = -90)
            ass.z_rot(value = 0)
            ass.y_dim(value = 0)
            ass.prompt('Shelf Hole Spacing',value = fd.inches(1.2598))
            
            if "Left" in ass.obj_bp.mv.name_object:
                ass.x_loc('X_Loc+INCH(.01)',[X_Loc])
                ass.z_dim('IF(Drill_Thru_Left,Panel_Thickness+INCH(.02),INCH(.2))',[Drill_Thru_Left,Panel_Thickness])

                if "Top" in ass.obj_bp.mv.name_object:
                    if i == 1:                  #FIRST OPENING
                        ass.prompt('Hide','IF(Left_End_Condition!=3,IF(OR(Remove_Left,Start_LB==0),True,False),True)',[Left_End_Condition,Remove_Left,Start_LB])
                    elif i == self.opening_qty: #LAST OPENING
                        ass.prompt('Hide','IF(Right_End_Condition!=3,IF(OR(Remove_Left,Start_LB==0),True,False),True)',[Right_End_Condition,Remove_Left,Start_LB])
                    else:                       #MIDDLE OPENING
                        ass.prompt('Hide','IF(OR(Remove_Left,Start_LB==0),True,False)',[Remove_Left,Start_LB])
                else:
                    if i == 1:                  #FIRST OPENING
                        ass.prompt('Hide','IF(Left_End_Condition!=3,IF(Remove_Left,True,False),True)',[Left_End_Condition,Remove_Left])
                    elif i == self.opening_qty: #LAST OPENING
                        ass.prompt('Hide','IF(Right_End_Condition!=3,IF(Remove_Left,True,False),True)',[Right_End_Condition,Remove_Left])
                    else:                       #MIDDLE OPENING
                        ass.prompt('Hide','IF(Remove_Left,True,False)',[Remove_Left])
            
            if "Right" in ass.obj_bp.mv.name_object:
                ass.x_loc('X_Loc+Width-INCH(.01)',[X_Loc,Width])
                ass.z_dim('IF(Drill_Thru_Right,-Panel_Thickness-INCH(.02),-INCH(.2))',[Drill_Thru_Right,Panel_Thickness])

                if "Top" in ass.obj_bp.mv.name_object:
                    if i == 1:                  #FIRST OPENING
                        ass.prompt('Hide','IF(Left_End_Condition!=3,IF(OR(Remove_Right,Start_LB==0),True,False),True)',[Left_End_Condition,Remove_Right,Start_LB])
                    elif i == self.opening_qty: #LAST OPENING
                        ass.prompt('Hide','IF(Right_End_Condition!=3,IF(OR(Remove_Right,Start_LB==0),True,False),True)',[Right_End_Condition,Remove_Right,Start_LB])
                    else:                       #MIDDLE OPENING
                        ass.prompt('Hide','IF(OR(Remove_Right,Start_LB==0),True,False)',[Remove_Right,Start_LB])
                else:
                    if i == 1:                  #FIRST OPENING
                        ass.prompt('Hide','IF(Left_End_Condition!=3,IF(Remove_Right,True,False),True)',[Left_End_Condition,Remove_Right])
                    elif i == self.opening_qty: #LAST OPENING
                        ass.prompt('Hide','IF(Right_End_Condition!=3,IF(Remove_Right,True,False),True)',[Right_End_Condition,Remove_Right])
                    else:                       #MIDDLE OPENING
                        ass.prompt('Hide','IF(Remove_Right,True,False)',[Remove_Right])

            if "Top" in ass.obj_bp.mv.name_object:
                ass.z_loc('Start_LB',[Start_LB])
                ass.x_dim('Height-Start_LB',[Height,Start_LB])

            if "Bottom" in ass.obj_bp.mv.name_object:
                ass.z_loc(value = fd.millimeters(9.525))
                ass.x_dim('IF(Stop_LB>0,Stop_LB,Height)',[Height,Stop_LB])

            if "Front" in ass.obj_bp.mv.name_object:
                ass.y_loc("-Depth-IF(Add_Backing,Back_Thickness,0)+INCH(1.4567)",[Depth,Add_Backing,Back_Thickness])
            
            if "Rear" in ass.obj_bp.mv.name_object:
                ass.y_loc("-IF(Add_Backing,Back_Thickness,0)-INCH(1.4567)",[Add_Backing,Back_Thickness])
            
            if "Mid" in ass.obj_bp.mv.name_object:
                ass.y_loc("-IF(Add_Backing,Back_Thickness,0)-INCH(12)+INCH(1.4567)",[Add_Backing,Back_Thickness])
                if "Left" in ass.obj_bp.mv.name_object:
                    if "Top" in ass.obj_bp.mv.name_object:
                        ass.prompt('Hide','IF(OR(Remove_Left,Start_LB==0),True,IF(Add_Mid,False,True))',[Remove_Left,Start_LB,Add_Mid])
                    else:
                        ass.prompt('Hide','IF(Remove_Left,True,IF(Add_Mid,False,True))',[Remove_Left,Add_Mid])
                if "Right" in ass.obj_bp.mv.name_object:
                    if "Top" in ass.obj_bp.mv.name_object:
                        ass.prompt('Hide','IF(OR(Remove_Right,Start_LB==0),True,IF(Add_Mid,False,True))',[Remove_Right,Start_LB,Add_Mid])
                    else:
                        ass.prompt('Hide','IF(Remove_Right,True,IF(Add_Mid,False,True))',[Remove_Right,Add_Mid])
                        
    
    def add_closet_opening(self,i,panel):
        Width = self.get_var('Opening ' + str(i) + ' Width','Width')
        Height = self.get_var('Opening ' + str(i) + ' Height','Height')
        Depth = self.get_var('Opening ' + str(i) + ' Depth','Depth')
        Add_Backing = self.get_var('Add Backing')
        Back_Thickness = self.get_var('Back Thickness')
        Left_End_Condition = self.get_var('Left End Condition')
        Right_End_Condition = self.get_var('Right End Condition')
        Toe_Kick_Height = self.get_var('Toe Kick Height')
        Shelf_Thickness = self.get_var('Shelf Thickness')
        
        if panel:
            X_Loc = panel.get_var('loc_x','X_Loc')
        else:
            X_Loc = self.get_var('Left Side Thickness','X_Loc')
        
        opening = self.add_opening()
        opening.set_name(self.get_opening_name(i))
        opening.add_tab(name='Material Thickness',tab_type='HIDDEN')
        opening.add_prompt(name="Left Side Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        opening.add_prompt(name="Right Side Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        opening.add_prompt(name="Top Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        opening.add_prompt(name="Bottom Thickness",prompt_type='DISTANCE',value=fd.inches(.75),tab_index=0)
        
        if i == 1: #FIRST
            opening.x_loc('IF(Left_End_Condition==3,0,X_Loc)',[Left_End_Condition,X_Loc])
            opening.y_loc("IF(Left_End_Condition==3,0,-Depth-IF(Add_Backing,Back_Thickness,0))",[Left_End_Condition,Depth,Add_Backing,Back_Thickness])
            opening.z_loc('IF(Left_End_Condition==3,0,Toe_Kick_Height+Shelf_Thickness)',[Left_End_Condition,Toe_Kick_Height,Shelf_Thickness])
            opening.x_rot(value = 0)
            opening.y_rot(value = 0)
            opening.z_rot(value = 0)
            opening.x_dim('IF(Left_End_Condition==3,0,Width)',[Left_End_Condition,Width])
            opening.y_dim("IF(Left_End_Condition==3,0,fabs(Depth))",[Depth,Left_End_Condition])
            opening.z_dim('IF(Left_End_Condition==3,0,Height-Toe_Kick_Height-(Shelf_Thickness*2))',[Left_End_Condition,Toe_Kick_Height,Shelf_Thickness,Height])
        elif i == self.opening_qty: #LAST
            opening.x_loc('IF(Right_End_Condition==3,0,X_Loc)',[Right_End_Condition,X_Loc])
            opening.y_loc("IF(Right_End_Condition==3,0,-Depth-IF(Add_Backing,Back_Thickness,0))",[Right_End_Condition,Depth,Add_Backing,Back_Thickness])
            opening.z_loc('IF(Right_End_Condition==3,0,Toe_Kick_Height+Shelf_Thickness)',[Right_End_Condition,Toe_Kick_Height,Shelf_Thickness])
            opening.x_rot(value = 0)
            opening.y_rot(value = 0)
            opening.z_rot(value = 0)
            opening.x_dim('IF(Right_End_Condition==3,0,Width)',[Right_End_Condition,Width])
            opening.y_dim("IF(Right_End_Condition==3,0,fabs(Depth))",[Depth,Right_End_Condition])
            opening.z_dim('IF(Right_End_Condition==3,0,Height-Toe_Kick_Height-(Shelf_Thickness*2))',[Right_End_Condition,Toe_Kick_Height,Shelf_Thickness,Height])
        else: #MIDDLE
            opening.x_loc('X_Loc',[X_Loc])
            opening.y_loc("-Depth-IF(Add_Backing,Back_Thickness,0)",[Depth,Add_Backing,Back_Thickness])
            opening.z_loc('Toe_Kick_Height+Shelf_Thickness',[Toe_Kick_Height,Shelf_Thickness])
            opening.x_rot(value = 0)
            opening.y_rot(value = 0)
            opening.z_rot(value = 0)
            opening.x_dim('Width',[Width])
            opening.y_dim("fabs(Depth)",[Depth])
            opening.z_dim('Height-Toe_Kick_Height-(Shelf_Thickness*2)',[Toe_Kick_Height,Shelf_Thickness,Height])
    
    def add_toe_kick(self,i,panel):
        Width = self.get_var('Opening ' + str(i) + ' Width','Width')
        Depth = self.get_var('Opening ' + str(i) + ' Depth','Depth')
        Add_Backing = self.get_var('Add Backing')
        Back_Thickness = self.get_var('Back Thickness')
        Toe_Kick_Height = self.get_var('Toe Kick Height')
        Toe_Kick_Setback = self.get_var('Toe Kick Setback')
        Left_End_Condition = self.get_var('Left End Condition')
        Right_End_Condition = self.get_var('Right End Condition')
        Shelf_Thickness = self.get_var('Shelf Thickness')
        
        if panel:
            X_Loc = panel.get_var('loc_x','X_Loc')
        else:
            X_Loc = self.get_var('Left Side Thickness','X_Loc')
        
        kick = self.add_assembly(PART_WITH_NO_EDGEBANDING)
        kick.set_name("Toe Kick " + str(i))
        kick.y_dim('-Toe_Kick_Height',[Toe_Kick_Height,Shelf_Thickness])
        kick.z_dim(value = fd.inches(.75))
        kick.y_loc('-Depth+Toe_Kick_Setback-IF(Add_Backing,Back_Thickness,0)',[Depth,Toe_Kick_Setback,Add_Backing,Back_Thickness])
        kick.z_loc(value = 0)
        kick.x_rot(value = -90)
        kick.y_rot(value = 0)
        kick.z_rot(value = 0)
        kick.cutpart("Closet_Toe_Kick")
        
        if i == 1: #FIRST OPENING
            kick.x_dim("Width+IF(Left_End_Condition!=3,0,Toe_Kick_Setback)",[Width,Left_End_Condition,Toe_Kick_Setback])
            kick.x_loc("X_Loc-IF(Left_End_Condition!=3,0,Toe_Kick_Setback)",[X_Loc,Left_End_Condition,Toe_Kick_Setback])
        elif i == self.opening_qty: #LAST OPENING
            kick.x_dim("Width+IF(Right_End_Condition!=3,0,Toe_Kick_Setback)",[Width,Right_End_Condition,Toe_Kick_Setback])
            kick.x_loc('X_Loc',[X_Loc])
        else: #MIDDLE OPENING
            kick.x_dim("Width",[Width])
            kick.x_loc('X_Loc',[X_Loc])
    
    def add_back(self,i,panel):
        Width = self.get_var('Opening ' + str(i) + ' Width','Width')
        Height = self.get_var('Opening ' + str(i) + ' Height','Height')
        Add_Backing = self.get_var('Add Backing')
        Back_Thickness = self.get_var('Back Thickness')
        Thickness = self.get_var('Thickness')

        if panel:
            X_Loc = panel.get_var('loc_x','X_Loc')
        else:
            X_Loc = self.get_var('Left Side Thickness','X_Loc')
        
        back = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        back.set_name("Back " + str(i))
        back.x_loc("X_Loc-(Thickness/2)",[X_Loc,Thickness])
        back.y_loc(value = 0)
        back.z_loc(value = 0)
        back.x_rot(value = 0)
        back.y_rot(value = -90)
        back.z_rot(value = 90)
        back.x_dim('Height',[Height])
        back.y_dim("(Width+Thickness)*-1",[Width,Thickness])
        back.z_dim('Back_Thickness',[Back_Thickness])
        back.prompt('Hide','IF(Add_Backing,False,True)',[Add_Backing])
        back.cutpart("Closet_Back")
        
    def add_top_shelf(self,i,panel):
        Width = self.get_var('Opening ' + str(i) + ' Width','Width')
        Depth = self.get_var('Opening ' + str(i) + ' Depth','Depth')
        Height = self.get_var('Opening ' + str(i) + ' Height','Height')
        Add_Backing = self.get_var('Add Backing')
        Back_Thickness = self.get_var('Back Thickness')
        Shelf_Thickness = self.get_var('Shelf Thickness')
        PT = self.get_var('Panel Thickness','PT')
        Add_Top_Accent_Shelf = self.get_var('Add Top Accent Shelf')
        OH = self.get_var('Top Shelf Overhang','OH')
        Crown_Molding_Height = self.get_var('Crown Molding Height')
        CD = self.get_var('Crown Molding Depth','CD')
        LC = self.get_var('Left End Condition','LC')
        RC = self.get_var('Right End Condition','RC')
        
        if panel:
            X_Loc = panel.get_var('loc_x','X_Loc')
        else:
            X_Loc = self.get_var('Left Side Thickness','X_Loc')
        
        top_shelf = self.add_assembly(PART_WITH_FRONT_EDGEBANDING)
        top_shelf.set_name("Top Accent Shelf " + str(i))
        if i == 1:
            top_shelf.x_loc('IF(LC==0,-OH-CD,IF(LC==1,0,IF(LC==2,X_Loc/2,OH+CD)))',[X_Loc,OH,CD,LC])
        else:
            P_Depth = self.get_var('Opening ' + str(i - 1) + ' Depth','P_Depth')
            P_Height = self.get_var('Opening ' + str(i - 1) + ' Height','P_Height')
            left_offset_formula = "IF(Height>P_Height,PT+OH+CD,IF(Height<P_Height,0,IF(Depth>P_Depth,PT+OH+CD,IF(Depth<P_Depth,-OH-CD,PT/2))))"
            top_shelf.x_loc('X_Loc-' + left_offset_formula,[X_Loc,Height,P_Height,P_Depth,Depth,PT,CD,OH])
        top_shelf.y_loc('IF(Add_Backing,-Back_Thickness,0)',[Add_Backing,Back_Thickness])
        top_shelf.z_loc('Height+Crown_Molding_Height',[Height,Crown_Molding_Height])
        top_shelf.x_rot(value = 0)
        top_shelf.y_rot(value = 0)
        top_shelf.z_rot(value = 0)
        if i == 1:
            N_Depth = self.get_var('Opening ' + str(i + 1) + ' Depth','N_Depth')
            N_Height = self.get_var('Opening ' + str(i + 1) + ' Height','N_Height')
            left_offset_formula = "IF(LC==0,X_Loc+OH+CD,IF(LC==1,X_Loc,IF(LC==2,X_Loc/2,-OH-CD)))"
            right_offset_formula = "IF(Height>N_Height,PT+OH+CD,IF(Height<N_Height,0,IF(Depth>N_Depth,PT+OH+CD,IF(Depth<N_Depth,-OH-CD,PT/2))))"
            top_shelf.x_dim('Width+' + left_offset_formula + '+' + right_offset_formula,[Width,Height,Depth,N_Height,N_Depth,X_Loc,OH,CD,LC,PT])
        elif i == self.opening_qty:
            P_Depth = self.get_var('Opening ' + str(i - 1) + ' Depth','P_Depth')
            P_Height = self.get_var('Opening ' + str(i - 1) + ' Height','P_Height')
            left_offset_formula = "IF(Height>P_Height,PT+OH+CD,IF(Height<P_Height,0,IF(Depth>P_Depth,PT+OH+CD,IF(Depth<P_Depth,-OH-CD,PT/2))))"
            right_offset_formula = "IF(RC==0,PT+OH+CD,IF(RC==1,PT,IF(RC==2,PT/2,-OH-CD)))"
            top_shelf.x_dim('Width+' + left_offset_formula + '+' + right_offset_formula,[Width,Height,Depth,P_Height,P_Depth,X_Loc,OH,CD,RC,PT])
        else:
            N_Depth = self.get_var('Opening ' + str(i + 1) + ' Depth','N_Depth')
            P_Depth = self.get_var('Opening ' + str(i - 1) + ' Depth','P_Depth')
            N_Height = self.get_var('Opening ' + str(i + 1) + ' Height','N_Height')
            P_Height = self.get_var('Opening ' + str(i - 1) + ' Height','P_Height')
            left_offset_formula = "IF(Height>P_Height,PT+OH+CD,IF(Height<P_Height,0,IF(Depth>P_Depth,PT+OH+CD,IF(Depth<P_Depth,-OH-CD,PT/2))))"
            right_offset_formula = "IF(Height>N_Height,PT+OH+CD,IF(Height<N_Height,0,IF(Depth>N_Depth,PT+OH+CD,IF(Depth<N_Depth,-OH-CD,PT/2))))"
            top_shelf.x_dim('Width+' + left_offset_formula + '+' + right_offset_formula,[Width,Height,Depth,P_Depth,N_Height,P_Height,N_Depth,X_Loc,OH,CD,PT])
        top_shelf.y_dim("-Depth-CD-OH",[Depth,CD,OH])
        top_shelf.z_dim('Shelf_Thickness',[Shelf_Thickness])
        top_shelf.prompt('Hide','IF(Add_Top_Accent_Shelf,False,True)',[Add_Top_Accent_Shelf])
        top_shelf.cutpart("Closet_Shelf")
        top_shelf.edgebanding("Closet_Body_Edges",l1 = True)

    def add_inside_dimension(self,i,panel):
        Width = self.get_var('Opening ' + str(i) + ' Width','Width')
        Largest_Opening_Size = self.get_var('Largest Opening Size')
        
        if panel:
            X_Loc = panel.get_var('loc_x','X_Loc')
        else:
            X_Loc = self.get_var('Left Side Thickness','X_Loc')
            
        dim = fd.Dimension()
        dim.parent(self.obj_bp)
        dim.start_z(value = fd.inches(-4))
        dim.start_x('X_Loc',[X_Loc])
        dim.end_x('Width',[Width])
        dim.set_color('IF(Width>Largest_Opening_Size,3,0)',[Width,Largest_Opening_Size])
        
    def get_opening_name(self,i):
        if i == 1:
            return "A"
        if i == 2:
            return "B"
        if i == 3:
            return "C"
        if i == 4:
            return "D"
        if i == 5:
            return "E"
        if i == 6:
            return "F"
        if i == 7:
            return "G"
        if i == 8:
            return "H"
        
    def draw(self):
        self.create_assembly()
        
        self.add_opening_prompts()
        self.add_carcass_prompts()
        self.add_machining_prompts()
        
        Product_Height = self.get_var('dim_z','Product_Height')
        
        #HEIGHT DIM
        dim = fd.Dimension()
        dim.parent(self.obj_bp)
        dim.start_x(value = fd.inches(-2))
        dim.end_z('Product_Height',[Product_Height])
        dim.set_text_offset_x(value = -25)
        
        self.add_sides()
        self.add_top(1,None)
        self.add_bottom(1,None)
        self.add_toe_kick(1,None)
        self.add_back(1,None)
        self.add_top_shelf(1,None)
        self.add_closet_opening(1,None)
        self.add_system_holes(1,None)
        self.add_inside_dimension(1,None)
        
        for i in range(2,self.opening_qty + 1):
            panel = self.add_panel(i - 1)
            
            self.add_top(i,panel)
            self.add_bottom(i,panel)
            self.add_toe_kick(i,panel)
            self.add_back(i,panel)
            self.add_top_shelf(i,panel)
            self.add_closet_opening(i,panel)
            self.add_system_holes(i,panel)
            self.add_inside_dimension(i,panel)
            
        self.update()

#---------PRODUCT: STARTER CABINETS

class PRODUCT_1_Tall_Opening_Bay(Opening_Bays):
    
    def __init__(self):
        g = bpy.context.scene.lm_closets
        self.category_name = "Floor Mounted"
        self.assembly_name = "1 Opening"
        self.product_type = "Tall"
        self.opening_qty = 1
        self.width = fd.inches(18*2)
        self.height = g.Default_Closet_Height
        self.depth = g.Default_Closet_Depth

class PRODUCT_2_Tall_Opening_Bay(Opening_Bays):
    
    def __init__(self):
        g = bpy.context.scene.lm_closets
        self.category_name = "Floor Mounted"
        self.assembly_name = "2 Openings"
        self.product_type = "Tall"
        self.opening_qty = 2
        self.width = fd.inches(18*2)
        self.height = g.Default_Closet_Height
        self.depth = g.Default_Closet_Depth

class PRODUCT_3_Tall_Opening_Bay(Opening_Bays):
    
    def __init__(self):
        g = bpy.context.scene.lm_closets
        self.category_name = "Floor Mounted"
        self.assembly_name = "3 Openings"
        self.product_type = "Tall"
        self.opening_qty = 3
        self.width = fd.inches(18*3)
        self.height = g.Default_Closet_Height
        self.depth = g.Default_Closet_Depth

class PRODUCT_4_Tall_Opening_Bay(Opening_Bays):
    
    def __init__(self):
        g = bpy.context.scene.lm_closets
        self.category_name = "Floor Mounted"
        self.assembly_name = "4 Openings"
        self.product_type = "Tall"
        self.opening_qty = 4
        self.width = fd.inches(18*4)
        self.height = g.Default_Closet_Height
        self.depth = g.Default_Closet_Depth

class PRODUCT_5_Tall_Opening_Bay(Opening_Bays):
    
    def __init__(self):
        g = bpy.context.scene.lm_closets
        self.category_name = "Floor Mounted"
        self.assembly_name = "5 Openings"
        self.product_type = "Tall"
        self.opening_qty = 5
        self.width = fd.inches(18*5)
        self.height = g.Default_Closet_Height
        self.depth = g.Default_Closet_Depth

class PRODUCT_6_Tall_Opening_Bay(Opening_Bays):
    
    def __init__(self):
        g = bpy.context.scene.lm_closets
        self.category_name = "Floor Mounted"
        self.assembly_name = "6 Openings"
        self.product_type = "Tall"
        self.opening_qty = 6
        self.width = fd.inches(18*6)
        self.height = g.Default_Closet_Height
        self.depth = g.Default_Closet_Depth

class PRODUCT_7_Tall_Opening_Bay(Opening_Bays):
    
    def __init__(self):
        g = bpy.context.scene.lm_closets
        self.category_name = "Floor Mounted"
        self.assembly_name = "7 Openings"
        self.product_type = "Tall"
        self.opening_qty = 7
        self.width = fd.inches(18*7)
        self.height = g.Default_Closet_Height
        self.depth = g.Default_Closet_Depth
        
class PRODUCT_8_Tall_Opening_Bay(Opening_Bays):
    
    def __init__(self):
        g = bpy.context.scene.lm_closets
        self.category_name = "Floor Mounted"
        self.assembly_name = "8 Openings"
        self.product_type = "Tall"
        self.opening_qty = 8
        self.width = fd.inches(18*8)
        self.height = g.Default_Closet_Height
        self.depth = g.Default_Closet_Depth
        
#---------USER INTERFACE

def update_closet_height(self,context):
    ''' EVENT changes height for all closet openings
    '''
    self.Opening_1_Height = self.height
    self.Opening_2_Height = self.height
    self.Opening_3_Height = self.height
    self.Opening_4_Height = self.height
    self.Opening_5_Height = self.height
    self.Opening_6_Height = self.height
    self.Opening_7_Height = self.height
    self.Opening_8_Height = self.height

class PROMPTS_Opening_Starter(bpy.types.Operator):
    bl_idname = "closets.opening_starter"
    bl_label = "Opening Starter Prompts" 
    bl_options = {'UNDO'}
    
    object_name = bpy.props.StringProperty(name="Object Name")
    
    tabs = bpy.props.EnumProperty(name="Tabs",
                        items=[('OPENINGS','Opening Sizes','Show the Width x Height x Depth for each opening'),
                               ('CONSTRUCTION','Construction Options','Show Additional Construction Options')],
                        default = 'OPENINGS')
    
    width = bpy.props.FloatProperty(name="Width",unit='LENGTH',precision=4)
    height = bpy.props.EnumProperty(name="Height",
                          items=PANEL_HEIGHTS,
                          default = '2131',
                          update=update_closet_height)

    Opening_1_Height = bpy.props.EnumProperty(name="Opening 1 Height",
                                    items=PANEL_HEIGHTS,
                                    default = '2131')
    
    Opening_2_Height = bpy.props.EnumProperty(name="Opening 2 Height",
                                    items=PANEL_HEIGHTS,
                                    default = '2131')
    
    Opening_3_Height = bpy.props.EnumProperty(name="Opening 3 Height",
                                    items=PANEL_HEIGHTS,
                                    default = '2131')
    
    Opening_4_Height = bpy.props.EnumProperty(name="Opening 4 Height",
                                    items=PANEL_HEIGHTS,
                                    default = '2131')
    
    Opening_5_Height = bpy.props.EnumProperty(name="Opening 5 Height",
                                    items=PANEL_HEIGHTS,
                                    default = '2131')
    
    Opening_6_Height = bpy.props.EnumProperty(name="Opening 6 Height",
                                    items=PANEL_HEIGHTS,
                                    default = '2131')
    
    Opening_7_Height = bpy.props.EnumProperty(name="Opening 7 Height",
                                    items=PANEL_HEIGHTS,
                                    default = '2131')
    
    Opening_8_Height = bpy.props.EnumProperty(name="Opening 8 Height",
                                    items=PANEL_HEIGHTS,
                                    default = '2131')
    
    Left_End_Condition = bpy.props.EnumProperty(name="Left Side",
                                       items=END_CONDITIONS,
                                       default = 'WP')
    
    Right_End_Condition = bpy.props.EnumProperty(name="Right Side",
                                        items=END_CONDITIONS,
                                        default = 'WP')
    
    product = None
    
    inserts = []
    
    use_32mm_system = False
    
    @classmethod
    def poll(cls, context):
        return True

    def check(self, context):
        self.product.obj_x.location.x = self.width
        if self.use_32mm_system:
            opening_1_height = self.product.get_prompt("Opening 1 Height")
            opening_2_height = self.product.get_prompt("Opening 2 Height")
            opening_3_height = self.product.get_prompt("Opening 3 Height")
            opening_4_height = self.product.get_prompt("Opening 4 Height")
            opening_5_height = self.product.get_prompt("Opening 5 Height")
            opening_6_height = self.product.get_prompt("Opening 6 Height")
            opening_7_height = self.product.get_prompt("Opening 7 Height")
            opening_8_height = self.product.get_prompt("Opening 8 Height")
            height_1 = float(self.Opening_1_Height) / 1000
            height_2 = float(self.Opening_2_Height) / 1000
            height_3 = float(self.Opening_3_Height) / 1000
            height_4 = float(self.Opening_4_Height) / 1000
            height_5 = float(self.Opening_5_Height) / 1000
            height_6 = float(self.Opening_6_Height) / 1000
            height_7 = float(self.Opening_7_Height) / 1000
            height_8 = float(self.Opening_8_Height) / 1000
            
            if opening_1_height:
                opening_1_height.set_value(height_1)
            
            if opening_2_height:
                opening_2_height.set_value(height_2)
            
            if opening_3_height:
                opening_3_height.set_value(height_3)
            
            if opening_4_height:
                opening_4_height.set_value(height_4)
            
            if opening_5_height:
                opening_5_height.set_value(height_5)
            
            if opening_6_height:
                opening_6_height.set_value(height_6)
            
            if opening_7_height:
                opening_7_height.set_value(height_7)
            
            if opening_8_height:
                opening_8_height.set_value(height_8)
        
        left_end_condition = self.product.get_prompt("Left End Condition")
        right_end_condition = self.product.get_prompt("Right End Condition")
        
        if left_end_condition:
            left_end_condition.set_value(self.Left_End_Condition)
        
        if right_end_condition:
            right_end_condition.set_value(self.Right_End_Condition)
        
        fd.run_calculators(self.product.obj_bp)
        #Hack I Dont know why i need to run calculators twice just for left right side removal
        fd.run_calculators(self.product.obj_bp)
        return True

    def execute(self, context):
        obj_list = []
        obj_list = fd.get_child_objects(self.product.obj_bp, obj_list)
        for obj in obj_list:
            if obj.type == 'EMPTY':
                obj.hide = True
        if self.product.obj_bp:
            if self.product.obj_bp.name in context.scene.objects:
                fd.run_calculators(self.product.obj_bp)
        return {'FINISHED'}

    def set_default_heights(self):
        opening_1_height = self.product.get_prompt("Opening 1 Height")
        opening_2_height = self.product.get_prompt("Opening 2 Height")
        opening_3_height = self.product.get_prompt("Opening 3 Height")
        opening_4_height = self.product.get_prompt("Opening 4 Height")
        opening_5_height = self.product.get_prompt("Opening 5 Height")
        opening_6_height = self.product.get_prompt("Opening 6 Height")
        opening_7_height = self.product.get_prompt("Opening 7 Height")
        opening_8_height = self.product.get_prompt("Opening 8 Height")
        
        if opening_1_height:
            open1_p_height = round(opening_1_height.DistanceValue*1000,0)
            for index, height in enumerate(PANEL_HEIGHTS):
                if not open1_p_height >= int(height[0]):
                    self.Opening_1_Height = PANEL_HEIGHTS[index - 1][0]
                    break
        if opening_2_height:
            open2_p_height = round(opening_2_height.DistanceValue*1000)
            for index, height in enumerate(PANEL_HEIGHTS):
                if not open2_p_height >= float(height[0]):
                    self.Opening_2_Height = PANEL_HEIGHTS[index - 1][0]
                    break
        if opening_3_height:
            open3_p_height = round(opening_3_height.DistanceValue*1000)
            for index, height in enumerate(PANEL_HEIGHTS):
                if not open3_p_height >= float(height[0]):
                    self.Opening_3_Height = PANEL_HEIGHTS[index - 1][0]
                    break
        if opening_4_height:
            open4_p_height = round(opening_4_height.DistanceValue*1000)
            for index, height in enumerate(PANEL_HEIGHTS):
                if not open4_p_height >= float(height[0]):
                    self.Opening_4_Height = PANEL_HEIGHTS[index - 1][0]
                    break
        if opening_5_height:
            open5_p_height = round(opening_5_height.DistanceValue*1000)
            for index, height in enumerate(PANEL_HEIGHTS):
                if not open5_p_height >= float(height[0]):
                    self.Opening_5_Height = PANEL_HEIGHTS[index - 1][0]
                    break
        if opening_6_height:
            open6_p_height = round(opening_6_height.DistanceValue*1000)
            for index, height in enumerate(PANEL_HEIGHTS):
                if not open6_p_height >= float(height[0]):
                    self.Opening_6_Height = PANEL_HEIGHTS[index - 1][0]
                    break
        if opening_7_height:
            open7_p_height = round(opening_7_height.DistanceValue*1000)
            for index, height in enumerate(PANEL_HEIGHTS):
                if not open7_p_height >= float(height[0]):
                    self.Opening_7_Height = PANEL_HEIGHTS[index - 1][0]
                    break
        if opening_8_height:
            open8_p_height = round(opening_8_height.DistanceValue*1000)
            for index, height in enumerate(PANEL_HEIGHTS):
                if not open8_p_height >= float(height[0]):
                    self.Opening_8_Height = PANEL_HEIGHTS[index - 1][0]
                    break
                
    def invoke(self,context,event):
        obj = bpy.data.objects[self.object_name]
        obj_product_bp = fd.get_bp(obj,'PRODUCT')
        self.product = fd.Assembly(obj_product_bp)
        self.use_32mm_system = context.scene.lm_closets.Use_32mm_System
        if self.product.obj_bp:
            if self.use_32mm_system:
                self.set_default_heights()
            self.width = math.fabs(self.product.obj_x.location.x)
            new_list = []
            self.inserts = fd.get_insert_bp_list(self.product.obj_bp,new_list)
            left_end_condition = self.product.get_prompt("Left End Condition")
            right_end_condition = self.product.get_prompt("Right End Condition")
            if left_end_condition:
                self.Left_End_Condition = left_end_condition.value()
            if right_end_condition:
                self.Right_End_Condition = right_end_condition.value()
        
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
        
        if self.use_32mm_system:
            row1 = col.row(align=True)
            if self.object_has_driver(self.product.obj_z):
                row1.label('Height: ' + str(fd.unit(math.fabs(self.product.obj_z.location.z))))
            else:
                row1.label('Height:')
                row1.prop(self,'height',text="")
                row1.prop(self.product.obj_z,'hide',text="")
        
    def object_has_driver(self,obj):
        if obj.animation_data:
            if len(obj.animation_data.drivers) > 0:
                return True
            
    def draw_common_prompts(self,layout):
        box = layout.box()
        col = box.column(align=True)
        col.prop(self,'Left_End_Condition')
        col.prop(self,'Right_End_Condition')

    def draw_splitter_widths(self,layout):
        opening_1 = self.product.get_prompt("Opening 1 Width")
        opening_2 = self.product.get_prompt("Opening 2 Width")
        opening_3 = self.product.get_prompt("Opening 3 Width")
        opening_4 = self.product.get_prompt("Opening 4 Width")
        opening_5 = self.product.get_prompt("Opening 5 Width")
        opening_6 = self.product.get_prompt("Opening 6 Width")
        opening_7 = self.product.get_prompt("Opening 7 Width")
        opening_8 = self.product.get_prompt("Opening 8 Width")
        opening_1_depth = self.product.get_prompt("Opening 1 Depth")
        opening_2_depth = self.product.get_prompt("Opening 2 Depth")
        opening_3_depth = self.product.get_prompt("Opening 3 Depth")
        opening_4_depth = self.product.get_prompt("Opening 4 Depth")
        opening_5_depth = self.product.get_prompt("Opening 5 Depth")
        opening_6_depth = self.product.get_prompt("Opening 6 Depth")
        opening_7_depth = self.product.get_prompt("Opening 7 Depth")
        opening_8_depth = self.product.get_prompt("Opening 8 Depth")
        
        col = layout.column(align=True)
        box = col.box()
        row = box.row()
        row.label("Opening Name:")
        row.label("",icon='BLANK1')
        row.label("Width:")
        row.label("Height:")
        row.label("Depth:")
        
        box = col.box()
        if opening_1:
            row = box.row()
            row.label("A Section:")
            row.prop(opening_1,'equal',text="")
            if opening_1.equal:
                row.label(str(fd.unit(opening_1.DistanceValue)) + '"')
            else:
                row.prop(opening_1,'DistanceValue',text="")
            if self.use_32mm_system:
                row.prop(self,'Opening_1_Height',text="")
            else:
                opening_1_height = self.product.get_prompt("Opening 1 Height")
                row.prop(opening_1_height,'DistanceValue',text="")
            row.prop(opening_1_depth,'DistanceValue',text="")

        if opening_2:
            row = box.row()
            row.label("B Section:")
            row.prop(opening_2,'equal',text="")
            if opening_2.equal:
                row.label(str(fd.unit(opening_2.DistanceValue)) + '"')
            else:
                row.prop(opening_2,'DistanceValue',text="")
            if self.use_32mm_system:
                row.prop(self,'Opening_2_Height',text="")
            else:
                opening_2_height = self.product.get_prompt("Opening 2 Height")
                row.prop(opening_2_height,'DistanceValue',text="")
            row.prop(opening_2_depth,'DistanceValue',text="")
                
        if opening_3:
            row = box.row()
            row.label("C Section:")
            row.prop(opening_3,'equal',text="")
            if opening_3.equal:
                row.label(str(fd.unit(opening_3.DistanceValue)) + '"')
            else:
                row.prop(opening_3,'DistanceValue',text="")
            if self.use_32mm_system:
                row.prop(self,'Opening_3_Height',text="")
            else:
                opening_3_height = self.product.get_prompt("Opening 3 Height")
                row.prop(opening_3_height,'DistanceValue',text="")
            row.prop(opening_3_depth,'DistanceValue',text="")
                
        if opening_4:
            row = box.row()
            row.label("D Section:")
            row.prop(opening_4,'equal',text="")
            if opening_4.equal:
                row.label(str(fd.unit(opening_4.DistanceValue)) + '"')
            else:
                row.prop(opening_4,'DistanceValue',text="")
            if self.use_32mm_system:
                row.prop(self,'Opening_4_Height',text="")
            else:
                opening_4_height = self.product.get_prompt("Opening 4 Height")
                row.prop(opening_4_height,'DistanceValue',text="")
            row.prop(opening_4_depth,'DistanceValue',text="")
            
        if opening_5:
            row = box.row()
            row.label("E Section:")
            row.prop(opening_5,'equal',text="")
            if opening_5.equal:
                row.label(str(fd.unit(opening_5.DistanceValue)) + '"')
            else:
                row.prop(opening_5,'DistanceValue',text="")
            if self.use_32mm_system:
                row.prop(self,'Opening_5_Height',text="")
            else:
                opening_5_height = self.product.get_prompt("Opening 5 Height")
                row.prop(opening_5_height,'DistanceValue',text="")
            row.prop(opening_5_depth,'DistanceValue',text="")
            
        if opening_6:
            row = box.row()
            row.label("F Section:")
            row.prop(opening_6,'equal',text="")
            if opening_6.equal:
                row.label(str(fd.unit(opening_6.DistanceValue)) + '"')
            else:
                row.prop(opening_6,'DistanceValue',text="")
            if self.use_32mm_system:
                row.prop(self,'Opening_6_Height',text="")
            else:
                opening_6_height = self.product.get_prompt("Opening 6 Height")
                row.prop(opening_6_height,'DistanceValue',text="")
            row.prop(opening_6_depth,'DistanceValue',text="")
            
        if opening_7:
            row = box.row()
            row.label("G Section:")
            row.prop(opening_7,'equal',text="")
            if opening_7.equal:
                row.label(str(fd.unit(opening_7.DistanceValue)) + '"')
            else:
                row.prop(opening_7,'DistanceValue',text="")
            if self.use_32mm_system:
                row.prop(self,'Opening_7_Height',text="")
            else:
                opening_7_height = self.product.get_prompt("Opening 7 Height")
                row.prop(opening_7_height,'DistanceValue',text="")
            row.prop(opening_7_depth,'DistanceValue',text="")
            
        if opening_8:
            row = box.row()
            row.label("H Section:")
            row.prop(opening_8,'equal',text="")
            if opening_8.equal:
                row.label(str(fd.unit(opening_8.DistanceValue)) + '"')
            else:
                row.prop(opening_8,'DistanceValue',text="")
            if self.use_32mm_system:
                row.prop(self,'Opening_8_Height',text="")
            else:
                opening_8_height = self.product.get_prompt("Opening 8 Height")
                row.prop(opening_8_height,'DistanceValue',text="")
            row.prop(opening_8_depth,'DistanceValue',text="")
            
    def draw_construction_options(self,layout):
        box = layout.box()
        
        toe_kick_height = self.product.get_prompt("Toe Kick Height")
        toe_kick_setback = self.product.get_prompt("Toe Kick Setback")
        left_wall_filler = self.product.get_prompt("Left Side Wall Filler")
        right_wall_filler = self.product.get_prompt("Right Side Wall Filler")
        add_backing = self.product.get_prompt("Add Backing")
        add_top_accent_shelf = self.product.get_prompt("Add Top Accent Shelf")
        top_shelf_overhang = self.product.get_prompt("Top Shelf Overhang")
        crown_molding_height = self.product.get_prompt("Crown Molding Height")
        crown_molding_depth = self.product.get_prompt("Crown Molding Depth")
        
        # SIDE OPTIONS:
        if left_wall_filler and right_wall_filler:
            col = box.column(align=True)
            col.label("Filler Options:")
            row = col.row()
            row.prop(left_wall_filler,'DistanceValue',text="Left Filler Amount")
            row = col.row()
            row.prop(right_wall_filler,'DistanceValue',text="Right Filler Amount")

        # CARCASS OPTIONS:
        col = box.column(align=True)
        col.label("Back Options:")
        row = col.row()
        if add_backing:
            row.prop(add_backing,'CheckBoxValue',text="Add Backing")
            
        col = box.column(align=True)
        col.label("Top Options:")
        row = col.row()
        if add_top_accent_shelf:
            row.prop(add_top_accent_shelf,'CheckBoxValue',text="Add Top Accent Shelf")
        if top_shelf_overhang:
            row.prop(top_shelf_overhang,'DistanceValue',text="Top Shelf Overhang")
        row = col.row()
        if crown_molding_height:
            row.prop(crown_molding_height,'DistanceValue',text="Crown Molding Height")
        if crown_molding_depth:
            row.prop(crown_molding_depth,'DistanceValue',text="Crown Molding Depth")
        
        # TOE KICK OPTIONS
        if toe_kick_height:
            col = box.column(align=True)
            col.label("Toe Kick Options:")
            row = col.row()
            row.prop(toe_kick_height,'DistanceValue',text="Toe Kick Height")
            row.prop(toe_kick_setback,'DistanceValue',text="Toe Kick Setback")
            
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
                
                split = box.split(percentage=.5)
                self.draw_product_size(split)
                self.draw_common_prompts(split)
                row = box.row()
                row.prop(self,'tabs',expand=True)
                if self.tabs == 'OPENINGS':
                    self.draw_splitter_widths(box)
                else:
                    self.draw_construction_options(box)
                self.draw_product_placment(box)

class PROPERTIES_Scene_Properties(bpy.types.PropertyGroup):
    Use_32mm_System = bpy.props.BoolProperty(name="Use 32mm System",
                                   default = False)
    
    Largest_Opening_Size = bpy.props.FloatProperty(name="Largest Opening Size",
                                         default=fd.inches(42),
                                         description="Enter the largest opening width size for closets. Dimensions display red when larger than this value.",
                                         unit='LENGTH')
    
    Default_Closet_Height = bpy.props.FloatProperty(name="Default Closet Height",
                                          default=fd.millimeters(2131),
                                          unit='LENGTH')
    
    Default_Closet_Depth = bpy.props.FloatProperty(name="Default Closet Depth",
                                         default=fd.inches(12),
                                         unit='LENGTH')
    
    Toe_Kick_Height = bpy.props.FloatProperty(name="Toe Kick Height",
                                    default=fd.inches(2.5),
                                    unit='LENGTH')
    
    Toe_Kick_Setback = bpy.props.FloatProperty(name="Toe Kick Setback",
                                     default=fd.inches(1.125),
                                     unit='LENGTH')
    
    Add_Backing = bpy.props.BoolProperty(name="Add Backing",
                               default=False)
    
    Add_Top_Accent_Shelf = bpy.props.BoolProperty(name="Add Top Shelf",
                                        default=False)
    
    Top_Shelf_Overhang = bpy.props.FloatProperty(name="Top Shelf Overhang",
                                       default=fd.inches(1),
                                       unit='LENGTH')
    
    Crown_Molding_Height = bpy.props.FloatProperty(name="Crown Molding Height",
                                         default=fd.inches(0),
                                         unit='LENGTH')
    
    Crown_Molding_Depth = bpy.props.FloatProperty(name="Crown Molding Depth",
                                        default=fd.inches(0),
                                        unit='LENGTH')
    
    def draw_update_button(self,layout,prompt_name,prompt_type,value):
        props = layout.operator('fd_prompts.update_all_prompts_in_scene',text="",icon='FILE_REFRESH',emboss=False)
        props.prompt_name = prompt_name
        props.prompt_type = prompt_type
        if prompt_type in {'NUMBER','QUANTITY','DISTANCE','PERCENTAGE','ANGLE','PRICE'}:
            props.float_value = value
        if prompt_type in {'COMBOBOX','TEXT'}:
            props.string_value = value
        if prompt_type == 'CHECKBOX':
            props.bool_value = value
        
    def draw(self,layout):
        box = layout.box()
        col = box.column(align=True)
        
        box = col.box()
        box.label('Standard Closet Sizes:')
        
        row = box.row()
        row.label('Closet Height:')
        row.prop(self,'Default_Closet_Height',text="")
        row = box.row()
        row.label('Closet Depth:')
        row.prop(self,'Default_Closet_Depth',text="")
        
        box = col.box()
        box.label('Closet Construction Options:')
        
        row = box.row()
        row.label("Largest Opening Size:")
        row.prop(self,"Largest_Opening_Size",text="")
        self.draw_update_button(row, 'Largest Opening Size', 'DISTANCE', self.Largest_Opening_Size)
        
        row = box.row()
        row.prop(self,'Add_Top_Accent_Shelf')
        self.draw_update_button(row, 'Add Top Accent Shelf', 'CHECKBOX', self.Add_Top_Accent_Shelf)
        if self.Add_Top_Accent_Shelf:
            row.prop(self,'Top_Shelf_Overhang',text="Overhang")
            self.draw_update_button(row, "Top Shelf Overhang", 'DISTANCE', self.Top_Shelf_Overhang)
        
        row = box.row()
        row.prop(self,'Add_Backing')
        self.draw_update_button(row, 'Add Backing', 'CHECKBOX', self.Add_Backing)
        
        row = box.row()
        row.prop(self,'Use_32mm_System')

def register():
    bpy.utils.register_class(PROPERTIES_Scene_Properties)
    bpy.types.Scene.lm_closets = bpy.props.PointerProperty(type = PROPERTIES_Scene_Properties)
    bpy.utils.register_class(PROMPTS_Opening_Starter)

def unregister():
    bpy.utils.unregister_class(PROPERTIES_Scene_Properties)
    bpy.utils.unregister_class(PROMPTS_Opening_Starter)
    