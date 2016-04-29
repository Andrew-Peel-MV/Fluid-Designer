"""
Microvellum 
Face Frame Library
Stores all the products for the Face Frame Library
"""

import bpy
import fd
import LM_cabinets
import LM_carcass
import LM_exteriors
import LM_interiors
import LM_splitters

LIBRARY_NAME = "Cabinets - Face Frame"
BASE_CATEGORY_NAME = "Base Cabinets"
TALL_CATEGORY_NAME = "Tall Cabinets"
UPPER_CATEGORY_NAME = "Upper Cabinets"
OUTSIDE_CORNER_CATEGORY_NAME = "Outside Corner Cabinets"
INSIDE_CORNER_CATEGORY_NAME = "Inside Corner Cabinets"
TRANSITION_CATEGORY_NAME = "Transition Cabinets"
STARTER_CATEGORY_NAME = "Starter Cabinets"
DRAWER_CATEGORY_NAME = "Drawer Cabinets"
BLIND_CORNER_CATEGORY_NAME = "Blind Corner Cabinets"

#---------PRODUCT: BASE CABINETS

class PRODUCT_Microwave_2_Door_Base_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = BASE_CATEGORY_NAME
        self.assembly_name = "Microwave 2 Door Base FF"
        self.width = g.Width_2_Door
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings_FF()
        self.splitter.opening_1_height = fd.inches(15)
        self.splitter.exterior_2 = LM_exteriors.INSERT_Base_Double_Door_FF()

class PRODUCT_Microwave_2_Drawer_Base_FF(LM_cabinets.Face_Frame_Standard): # DRAWER STACK
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = BASE_CATEGORY_NAME
        self.assembly_name = "Microwave 2 Drawer Base FF"
        self.width = g.Width_2_Door
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.splitter = LM_splitters.INSERT_3_Vertical_Openings_FF()
        self.splitter.exterior_2 = LM_exteriors.INSERT_1_Drawer_FF()
        self.splitter.exterior_3 = LM_exteriors.INSERT_1_Drawer_FF()
#         self.splitter.exterior_2 = LM_exteriors.INSERT_2_Drawer_Stack()

class PRODUCT_2_Door_Sink_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = BASE_CATEGORY_NAME
        self.assembly_name = "2 Door Sink FF"
        self.width = g.Width_2_Door
        self.height = g.Sink_Cabinet_Height
        self.depth = g.Sink_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.carcass.remove_top = True
        self.exterior = LM_exteriors.INSERT_Base_Double_Door_FF()
        self.interior = None
        
class PRODUCT_2_Door_with_False_Front_Sink_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = "Base Cabinets"
        self.assembly_name = "2 Door with False Front Sink FF"
        self.width = g.Width_2_Door
        self.height = g.Sink_Cabinet_Height
        self.depth = g.Sink_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.carcass.remove_top = True
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings_FF()
        self.splitter.opening_1_height = g.Top_Drawer_Front_Height - fd.inches(1)
        self.splitter.exterior_1 = LM_exteriors.INSERT_1_Drawer_FF()
        self.splitter.exterior_1.add_drawer = False
        self.splitter.exterior_1.add_pull = False
        self.splitter.exterior_2 = LM_exteriors.INSERT_Base_Double_Door_FF()

class PRODUCT_2_Door_2_False_Front_Sink_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = "Base Cabinets"
        self.assembly_name = "2 Door 2 False Front Sink FF"
        self.width = g.Width_2_Door
        self.height = g.Sink_Cabinet_Height
        self.depth = g.Sink_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.carcass.remove_top = True
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings_FF()
        self.splitter.opening_1_height = g.Top_Drawer_Front_Height - fd.inches(1)
        self.splitter.exterior_1 = LM_exteriors.INSERT_Horizontal_Drawers_FF()
        self.splitter.exterior_1.add_drawer = False
        self.splitter.exterior_1.add_pull = False
        self.splitter.exterior_2 = LM_exteriors.INSERT_Base_Double_Door_FF()
        
class PRODUCT_1_Door_Sink_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = BASE_CATEGORY_NAME
        self.assembly_name = "1 Door Sink FF"
        self.width = g.Width_1_Door
        self.height = g.Sink_Cabinet_Height
        self.depth = g.Sink_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.carcass.remove_top = True
        self.exterior = LM_exteriors.INSERT_Base_Single_Door_FF()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_1_Door_Base_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = BASE_CATEGORY_NAME
        self.assembly_name = "1 Door Base FF"
        self.width = g.Width_1_Door
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.exterior = LM_exteriors.INSERT_Base_Single_Door_FF()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_2_Door_Base_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = BASE_CATEGORY_NAME
        self.assembly_name = "2 Door Base FF"
        self.width = g.Width_2_Door
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.exterior = LM_exteriors.INSERT_Base_Double_Door_FF()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_1_Door_1_Drawer_Base_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = BASE_CATEGORY_NAME
        self.assembly_name = "1 Door 1 Drawer Base FF"
        self.width = g.Width_1_Door
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings_FF()
        self.splitter.opening_1_height = g.Top_Drawer_Front_Height - fd.inches(1)
        self.splitter.exterior_1 = LM_exteriors.INSERT_1_Drawer_FF()
        self.splitter.interior_2 = LM_interiors.INSERT_Shelves()
        self.splitter.exterior_2 = LM_exteriors.INSERT_Base_Single_Door_FF()

class PRODUCT_2_Door_2_Drawer_Base_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = BASE_CATEGORY_NAME
        self.assembly_name = "2 Door 2 Drawer Base FF"
        self.width = g.Width_2_Door
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings_FF()
        self.splitter.opening_1_height = g.Top_Drawer_Front_Height - fd.inches(1)
        self.splitter.exterior_1 = LM_exteriors.INSERT_Horizontal_Drawers_FF()
        self.splitter.interior_2 = LM_interiors.INSERT_Shelves()
        self.splitter.exterior_2 = LM_exteriors.INSERT_Base_Double_Door_FF()

#---------PRODUCT: TALL CABINETS

class PRODUCT_4_Door_Oven_Tall_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = TALL_CATEGORY_NAME
        self.assembly_name = "4 Door Oven Tall FF"
        self.width = g.Width_2_Door
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Carcass()
        self.splitter = LM_splitters.INSERT_3_Vertical_Openings_FF()
        self.splitter.exterior_1 = LM_exteriors.INSERT_Upper_Double_Door_FF()
        self.splitter.exterior_3 = LM_exteriors.INSERT_Base_Double_Door_FF()

class PRODUCT_4_Door_Micro_and_Oven_Tall_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = TALL_CATEGORY_NAME
        self.assembly_name = "4 Door Micro and Oven Tall FF"
        self.width = g.Width_2_Door
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Carcass()
        self.splitter = LM_splitters.INSERT_4_Vertical_Openings_FF()
        self.splitter.exterior_1 = LM_exteriors.INSERT_Upper_Double_Door_FF()
        self.splitter.exterior_4 = LM_exteriors.INSERT_Base_Double_Door_FF()

#TODO: FIX FACE FRAME - Remove Bottom Rail
# class PRODUCT_Refrigerator_Tall_FF(LM_cabinets.Face_Frame_Standard):
#     
#     def __init__(self):
#         g = bpy.context.scene.lm_face_frame_cabients
#         self.library_name = LIBRARY_NAME
#         self.category_name = TALL_CATEGORY_NAME
#         self.assembly_name = "Refrigerator Tall FF"
#         self.width = g.Width_2_Door
#         self.height = g.Tall_Cabinet_Height
#         self.depth = g.Tall_Cabinet_Depth
#         self.carcass = LM_carcass.INSERT_Tall_Carcass()
#         self.carcass.prompts = {'Remove Bottom':True}
#         self.splitter = LM_splitters.INSERT_Vertical_Splitters_1_FF()
#         self.splitter.opening_1_height = fd.inches(10)
#         self.splitter.exterior_1 = LM_exteriors.INSERT_Upper_Double_Door_FF()

class PRODUCT_1_Door_Tall_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = TALL_CATEGORY_NAME
        self.assembly_name = "1 Door Tall FF"
        self.width = g.Width_1_Door
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Carcass()
        self.exterior = LM_exteriors.INSERT_Tall_Single_Door_FF()
        self.interior = LM_interiors.INSERT_Shelves()
        
class PRODUCT_2_Door_Tall_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = TALL_CATEGORY_NAME
        self.assembly_name = "2 Door Tall FF"
        self.width = g.Width_2_Door
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Carcass()
        self.exterior = LM_exteriors.INSERT_Tall_Double_Door_FF()
        self.interior = LM_interiors.INSERT_Shelves()
        
class PRODUCT_1_Double_Door_Tall_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = TALL_CATEGORY_NAME
        self.assembly_name = "1 Double Door Tall FF"
        self.width = g.Width_1_Door
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings_FF()
        self.splitter.exterior_1 = LM_exteriors.INSERT_Upper_Single_Door_FF()
        self.splitter.interior_2 = LM_interiors.INSERT_Shelves()
        self.splitter.exterior_2 = LM_exteriors.INSERT_Base_Single_Door_FF()

class PRODUCT_2_Double_Door_Tall_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = TALL_CATEGORY_NAME
        self.assembly_name = "2 Double Door Tall FF"
        self.width = g.Width_2_Door
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings_FF()
        self.splitter.exterior_1 = LM_exteriors.INSERT_Upper_Double_Door_FF()
        self.splitter.interior_2 = LM_interiors.INSERT_Shelves()
        self.splitter.exterior_2 = LM_exteriors.INSERT_Base_Double_Door_FF()
        
class PRODUCT_2_Door_2_Drawer_Tall_FF(LM_cabinets.Face_Frame_Standard): # NEED DRAWER STACK
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = TALL_CATEGORY_NAME
        self.assembly_name = "2 Door 2 Drawer Tall FF"
        self.width = g.Width_2_Door
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Carcass()
        self.splitter = LM_splitters.INSERT_3_Vertical_Openings_FF()
        self.splitter.opening_2_height = fd.inches(10)
        self.splitter.opening_3_height = fd.inches(10)
        self.splitter.exterior_1 = LM_exteriors.INSERT_Tall_Double_Door_FF()
        self.splitter.interior_1 = LM_interiors.INSERT_Shelves()
        self.splitter.exterior_2 = LM_exteriors.INSERT_1_Drawer_FF()
        self.splitter.exterior_3 = LM_exteriors.INSERT_1_Drawer_FF()

class PRODUCT_2_Door_3_Drawer_Tall_FF(LM_cabinets.Face_Frame_Standard): # NEED DRAWER STACK
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = TALL_CATEGORY_NAME
        self.assembly_name = "2 Door 3 Drawer Tall FF"
        self.width = g.Width_2_Door
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Carcass()
        self.splitter = LM_splitters.INSERT_4_Vertical_Openings_FF()
        self.splitter.opening_2_height = fd.inches(6)
        self.splitter.opening_3_height = fd.inches(6)
        self.splitter.opening_4_height = fd.inches(6)
        self.splitter.exterior_1 = LM_exteriors.INSERT_Tall_Double_Door_FF()
        self.splitter.interior_1 = LM_interiors.INSERT_Shelves()
        self.splitter.exterior_2 = LM_exteriors.INSERT_1_Drawer_FF()
        self.splitter.exterior_3 = LM_exteriors.INSERT_1_Drawer_FF()
        self.splitter.exterior_4 = LM_exteriors.INSERT_1_Drawer_FF()
        
#---------PRODUCT: UPPER CABINETS

class PRODUCT_1_Door_Upper_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = UPPER_CATEGORY_NAME
        self.assembly_name = "1 Door Upper FF"
        self.width = g.Width_1_Door
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Cabinet_Depth
        self.mirror_z = True
        self.height_above_floor = g.Height_Above_Floor
        self.carcass = LM_carcass.INSERT_Upper_Carcass()
        self.exterior = LM_exteriors.INSERT_Upper_Single_Door_FF()
        self.interior = LM_interiors.INSERT_Shelves()
        
class PRODUCT_2_Door_Upper_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = UPPER_CATEGORY_NAME
        self.assembly_name = "2 Door Upper FF"
        self.width = g.Width_2_Door
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Cabinet_Depth
        self.mirror_z = True
        self.height_above_floor = g.Height_Above_Floor
        self.carcass = LM_carcass.INSERT_Upper_Carcass()
        self.exterior = LM_exteriors.INSERT_Upper_Double_Door_FF()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_1_Double_Door_Upper_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = UPPER_CATEGORY_NAME
        self.assembly_name = "1 Double Door Upper FF"
        self.width = g.Width_1_Door
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Cabinet_Depth
        self.mirror_z = True
        self.height_above_floor = g.Height_Above_Floor
        self.carcass = LM_carcass.INSERT_Upper_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings_FF()
        self.splitter.exterior_1 = LM_exteriors.INSERT_Upper_Single_Door_FF()
        self.splitter.exterior_2 = LM_exteriors.INSERT_Upper_Single_Door_FF()

class PRODUCT_2_Double_Door_Upper_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = UPPER_CATEGORY_NAME
        self.assembly_name = "2 Double Door Upper FF"
        self.width = g.Width_2_Door
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Cabinet_Depth
        self.mirror_z = True
        self.height_above_floor = g.Height_Above_Floor
        self.carcass = LM_carcass.INSERT_Upper_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings_FF()
        self.splitter.exterior_1 = LM_exteriors.INSERT_Upper_Double_Door_FF()
        self.splitter.exterior_2 = LM_exteriors.INSERT_Upper_Double_Door_FF()

class PRODUCT_Microwave_2_Door_Upper_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = UPPER_CATEGORY_NAME
        self.assembly_name = "Microwave 2 Door Upper FF"
        self.width = g.Width_2_Door
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Cabinet_Depth
        self.mirror_z = True
        self.height_above_floor = g.Height_Above_Floor
        self.carcass = LM_carcass.INSERT_Upper_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings_FF()
        self.splitter.exterior_1 = LM_exteriors.INSERT_Upper_Double_Door_FF()

class PRODUCT_2_Door_Upper_with_Microwave_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = UPPER_CATEGORY_NAME
        self.assembly_name = "2 Door Upper with Microwave FF"
        self.width = fd.inches(30)
        self.height = g.Upper_Cabinet_Height - fd.inches(20)
        self.depth = g.Upper_Cabinet_Depth
        self.mirror_z = True
        self.height_above_floor = g.Height_Above_Floor
        self.carcass = LM_carcass.INSERT_Upper_Carcass()
        self.exterior = LM_exteriors.INSERT_Upper_Double_Door_FF()
        self.interior = None
        self.add_microwave = True
        
class PRODUCT_2_Door_Upper_with_Vent_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = UPPER_CATEGORY_NAME
        self.assembly_name = "1 Door Upper with Vent FF"
        self.width = g.Width_2_Door
        self.height = g.Upper_Cabinet_Height - fd.inches(20)
        self.depth = g.Upper_Cabinet_Depth
        self.mirror_z = True
        self.height_above_floor = g.Height_Above_Floor
        self.carcass = LM_carcass.INSERT_Upper_Carcass()
        self.exterior = LM_exteriors.INSERT_Upper_Double_Door_FF()
        self.interior = None
        self.add_vent_hood = True
        
class PRODUCT_2_Door_2_Drawer_Upper_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = UPPER_CATEGORY_NAME
        self.assembly_name = "2 Door 2 Drawer Upper FF"
        self.width = g.Width_2_Door
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Cabinet_Depth
        self.mirror_z = True
        self.height_above_floor = g.Height_Above_Floor
        self.carcass = LM_carcass.INSERT_Upper_Carcass()
        self.splitter = LM_splitters.INSERT_3_Vertical_Openings_FF()
        self.splitter.exterior_1 = LM_exteriors.INSERT_Upper_Double_Door_FF()
        self.splitter.interior_1 = LM_interiors.INSERT_Shelves()
        self.splitter.exterior_2 = LM_exteriors.INSERT_1_Drawer_FF()
        self.splitter.exterior_3 = LM_exteriors.INSERT_1_Drawer_FF()

#---------PRODUCT: OUTSIDE CORNER CABINETS

# TODO: CREATE OUTSIDE CORNER FF CABINETS

# #---------PRODUCT: TRANSITION CABINETS

# TODO: CREATE TRANSITION FF CABINETS

#---------PRODUCT: STARTER CABINETS

class PRODUCT_Base_Starter_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = STARTER_CATEGORY_NAME
        self.assembly_name = "Base Starter FF"
        self.width = g.Width_1_Door
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.exterior = None
        self.interior = None
        self.add_empty_opening = True

class PRODUCT_Tall_Starter_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = STARTER_CATEGORY_NAME
        self.assembly_name = "Tall Starter FF"
        self.width = g.Width_1_Door
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Carcass()
        self.exterior = None
        self.interior = None
        self.add_empty_opening = True

class PRODUCT_Upper_Starter_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = STARTER_CATEGORY_NAME
        self.assembly_name = "Upper Starter FF"
        self.width = g.Width_1_Door
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Cabinet_Depth
        self.mirror_z = True
        self.carcass = LM_carcass.INSERT_Upper_Carcass()
        self.exterior = None
        self.interior = None
        self.height_above_floor = g.Height_Above_Floor
        self.add_empty_opening = True

class PRODUCT_Sink_Starter_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = STARTER_CATEGORY_NAME
        self.assembly_name = "Sink Starter FF"
        self.width = g.Width_1_Door
        self.height = g.Sink_Cabinet_Height
        self.depth = g.Sink_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.carcass.remove_top = True
        self.exterior = None
        self.interior = None
        self.add_empty_opening = True

class PRODUCT_Suspended_Starter_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = STARTER_CATEGORY_NAME
        self.assembly_name = "Suspended Starter FF"
        self.width = g.Width_1_Door
        self.height = g.Suspended_Cabinet_Height
        self.depth = g.Suspended_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Suspended_Carcass()
        self.mirror_z = True
        self.exterior = None
        self.interior = None
        self.height_above_floor = g.Base_Cabinet_Height
        self.add_empty_opening = True
        
#---------PRODUCT: DRAWER CABINETS
        
class PRODUCT_1_Drawer_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = DRAWER_CATEGORY_NAME
        self.assembly_name = "1 Drawer FF"
        self.width = g.Width_Drawer
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.exterior = LM_exteriors.INSERT_1_Drawer_FF()

class PRODUCT_2_Drawer_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = DRAWER_CATEGORY_NAME
        self.assembly_name = "2 Drawer FF"
        self.width = g.Width_Drawer
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings_FF()
        self.splitter.exterior_1 = LM_exteriors.INSERT_1_Drawer_FF()
        self.splitter.exterior_2 = LM_exteriors.INSERT_1_Drawer_FF()

class PRODUCT_3_Drawer_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = DRAWER_CATEGORY_NAME
        self.assembly_name = "3 Drawer FF"
        self.width = g.Width_Drawer
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.splitter = LM_splitters.INSERT_3_Vertical_Openings_FF()
        self.splitter.exterior_1 = LM_exteriors.INSERT_1_Drawer_FF()
        self.splitter.exterior_2 = LM_exteriors.INSERT_1_Drawer_FF()
        self.splitter.exterior_3 = LM_exteriors.INSERT_1_Drawer_FF()
            
class PRODUCT_4_Drawer_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = DRAWER_CATEGORY_NAME
        self.assembly_name = "4 Drawer FF"
        self.width = g.Width_Drawer
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.splitter = LM_splitters.INSERT_4_Vertical_Openings_FF()
        self.splitter.exterior_1 = LM_exteriors.INSERT_1_Drawer_FF()
        self.splitter.exterior_2 = LM_exteriors.INSERT_1_Drawer_FF()
        self.splitter.exterior_3 = LM_exteriors.INSERT_1_Drawer_FF()
        self.splitter.exterior_4 = LM_exteriors.INSERT_1_Drawer_FF()
        
class PRODUCT_1_Drawer_Suspended_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = DRAWER_CATEGORY_NAME
        self.assembly_name = "1 Drawer Suspended FF"
        self.width = g.Width_Drawer
        self.height = g.Suspended_Cabinet_Height
        self.depth = g.Suspended_Cabinet_Depth
        self.mirror_z = True
        self.carcass = LM_carcass.INSERT_Suspended_Carcass()
        self.height_above_floor = g.Base_Cabinet_Height
        self.exterior = LM_exteriors.INSERT_1_Drawer_FF()
        
class PRODUCT_2_Drawer_Suspended_FF(LM_cabinets.Face_Frame_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = DRAWER_CATEGORY_NAME
        self.assembly_name = "2 Drawer Suspended FF"
        self.width = g.Width_Drawer * 2
        self.height = g.Suspended_Cabinet_Height
        self.depth = g.Suspended_Cabinet_Depth
        self.mirror_z = True
        self.carcass = LM_carcass.INSERT_Suspended_Carcass()
        self.height_above_floor = g.Base_Cabinet_Height
        self.exterior = LM_exteriors.INSERT_Horizontal_Drawers_FF()
        
#---------PRODUCT: BLIND CORNER CABINETS

class PRODUCT_1_Door_Blind_Left_Corner_Base_FF(LM_cabinets.Face_Frame_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = "Blind Corner Cabinets"
        self.assembly_name = "1 Door Blind Left Corner Base FF"
        self.blind_side = "Left"
        self.width = g.Base_Width_Blind
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.exterior = LM_exteriors.INSERT_Base_Single_Door_FF()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_1_Door_Blind_Right_Corner_Base_FF(LM_cabinets.Face_Frame_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "1 Door Blind Right Corner Base FF"
        self.blind_side = "Right"
        self.width = g.Base_Width_Blind
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.exterior = LM_exteriors.INSERT_Base_Single_Door_FF()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_1_Door_Blind_Left_Corner_Tall_FF(LM_cabinets.Face_Frame_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "1 Door Blind Left Corner Tall FF"
        self.blind_side = "Left"
        self.width = g.Tall_Width_Blind
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Carcass()
        self.exterior = LM_exteriors.INSERT_Tall_Single_Door_FF()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_1_Door_Blind_Right_Corner_Tall_FF(LM_cabinets.Face_Frame_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "1 Door Blind Right Corner Tall FF"
        self.blind_side = "Right"
        self.width = g.Tall_Width_Blind
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Carcass()
        self.exterior = LM_exteriors.INSERT_Tall_Single_Door_FF()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_1_Door_Blind_Left_Corner_Upper_FF(LM_cabinets.Face_Frame_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "1 Door Blind Left Corner Upper FF"
        self.blind_side = "Left"
        self.height_above_floor = g.Height_Above_Floor
        self.mirror_z = True
        self.width = g.Upper_Width_Blind
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Upper_Carcass()
        self.exterior = LM_exteriors.INSERT_Upper_Single_Door_FF()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_1_Door_Blind_Right_Corner_Upper_FF(LM_cabinets.Face_Frame_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "1 Door Blind Right Corner Upper FF"
        self.blind_side = "Right"
        self.height_above_floor = g.Height_Above_Floor
        self.mirror_z = True
        self.width = g.Upper_Width_Blind
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Upper_Carcass()
        self.exterior = LM_exteriors.INSERT_Upper_Single_Door_FF()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_2_Door_Blind_Left_Corner_Base_FF(LM_cabinets.Face_Frame_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "2 Door Blind Left Corner Base FF"
        self.blind_side = "Left"
        self.width = g.Base_Width_Blind
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.exterior = LM_exteriors.INSERT_Base_Double_Door_FF()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_2_Door_Blind_Right_Corner_Base_FF(LM_cabinets.Face_Frame_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "2 Door Blind Right Corner Base FF"
        self.blind_side = "Right"
        self.width = g.Base_Width_Blind
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.exterior = LM_exteriors.INSERT_Base_Double_Door_FF()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_2_Door_Blind_Left_Corner_Tall_FF(LM_cabinets.Face_Frame_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "2 Door Blind Left Corner Tall FF"
        self.blind_side = "Left"
        self.width = g.Tall_Width_Blind
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Carcass()
        self.exterior = LM_exteriors.INSERT_Tall_Double_Door_FF()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_2_Door_Blind_Right_Corner_Tall_FF(LM_cabinets.Face_Frame_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "2 Door Blind Right Corner Tall FF"
        self.blind_side = "Right"
        self.width = g.Tall_Width_Blind
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Carcass()
        self.exterior = LM_exteriors.INSERT_Tall_Double_Door_FF()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_2_Door_Blind_Left_Corner_Upper_FF(LM_cabinets.Face_Frame_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "2 Door Blind Left Corner Upper FF"
        self.blind_side = "Left"
        self.height_above_floor = g.Height_Above_Floor
        self.mirror_z = True
        self.width = g.Upper_Width_Blind
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Upper_Carcass()
        self.exterior = LM_exteriors.INSERT_Upper_Double_Door_FF()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_2_Door_Blind_Right_Corner_Upper_FF(LM_cabinets.Face_Frame_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "2 Door Blind Right Corner Upper FF"
        self.blind_side = "Right"
        self.height_above_floor = g.Height_Above_Floor
        self.mirror_z = True
        self.width = g.Upper_Width_Blind
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Upper_Carcass()
        self.exterior = LM_exteriors.INSERT_Upper_Double_Door_FF()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_1_Door_1_Drawer_Blind_Right_Corner_Base_FF(LM_cabinets.Face_Frame_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "1 Door 1 Drawer Blind Right Corner Base FF"
        self.blind_side = "Right"
        self.width = g.Base_Width_Blind
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings_FF()
        self.splitter.opening_1_height = g.Top_Drawer_Front_Height - fd.inches(1)
        self.splitter.exterior_1 = LM_exteriors.INSERT_1_Drawer_FF()
        self.splitter.exterior_2 = LM_exteriors.INSERT_Base_Single_Door_FF()
        
class PRODUCT_1_Door_1_Drawer_Blind_Left_Corner_Base_FF(LM_cabinets.Face_Frame_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "1 Door 1 Drawer Blind Left Corner Base FF"
        self.blind_side = "Left"
        self.width = g.Base_Width_Blind
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings_FF()
        self.splitter.opening_1_height = g.Top_Drawer_Front_Height - fd.inches(1)
        self.splitter.exterior_1 = LM_exteriors.INSERT_1_Drawer_FF()
        self.splitter.exterior_2 = LM_exteriors.INSERT_Base_Single_Door_FF()
        
class PRODUCT_2_Door_2_Drawer_Blind_Right_Corner_Base_FF(LM_cabinets.Face_Frame_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "2 Door 2 Drawer Blind Right Corner Base FF"
        self.blind_side = "Right"
        self.width = g.Base_Width_Blind
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings_FF()
        self.splitter.opening_1_height = g.Top_Drawer_Front_Height - fd.inches(1)
        self.splitter.exterior_1 = LM_exteriors.INSERT_Horizontal_Drawers_FF()
        self.splitter.exterior_2 = LM_exteriors.INSERT_Base_Double_Door_FF()
        
class PRODUCT_2_Door_2_Drawer_Blind_Left_Corner_Base_FF(LM_cabinets.Face_Frame_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "2 Door 2 Drawer Blind Left Corner Base FF"
        self.blind_side = "Left"
        self.width = g.Base_Width_Blind
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings_FF()
        self.splitter.opening_1_height = g.Top_Drawer_Front_Height - fd.inches(1)
        self.splitter.exterior_1 = LM_exteriors.INSERT_Horizontal_Drawers_FF()
        self.splitter.exterior_2 = LM_exteriors.INSERT_Base_Double_Door_FF()
        
#---------PRODUCT: INSIDE CORNER CABINETS

class PRODUCT_Pie_Cut_Corner_Base(LM_cabinets.Face_Frame_Inside_Corner):
     
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = INSIDE_CORNER_CATEGORY_NAME
        self.assembly_name = "Pie Cut Corner Base"
        self.width = g.Base_Inside_Corner_Size
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Inside_Corner_Size
        self.carcass = LM_carcass.INSERT_Base_Inside_Corner_Notched_Carcass()
        self.exterior = LM_exteriors.INSERT_Base_Pie_Cut_Door_FF()
        self.interior = None
        self.face_frame = "Pie Cut Face Frame"
         
class PRODUCT_Pie_Cut_Corner_Upper(LM_cabinets.Face_Frame_Inside_Corner):
     
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = INSIDE_CORNER_CATEGORY_NAME
        self.assembly_name = "Pie Cut Corner Upper"
        self.width = g.Upper_Inside_Corner_Size
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Inside_Corner_Size
        self.height_above_floor = g.Height_Above_Floor
        self.mirror_z = True
        self.carcass = LM_carcass.INSERT_Upper_Inside_Corner_Notched_Carcass()
        self.exterior = LM_exteriors.INSERT_Upper_Pie_Cut_Door_FF()
        self.interior = None
        self.face_frame = "Pie Cut Face Frame"
         
class PRODUCT_1_Door_Diagonal_Corner_Base(LM_cabinets.Face_Frame_Inside_Corner):
     
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = INSIDE_CORNER_CATEGORY_NAME
        self.assembly_name = "1 Door Diagonal Corner Base"
        self.width = g.Base_Inside_Corner_Size
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Inside_Corner_Size
        self.carcass = LM_carcass.INSERT_Base_Inside_Corner_Diagonal_Carcass()
        self.exterior = LM_exteriors.INSERT_Base_Single_Door_FF()
        self.interior = None
        self.face_frame = "Face Frame"
         
class PRODUCT_2_Door_Diagonal_Corner_Base(LM_cabinets.Face_Frame_Inside_Corner):
     
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = INSIDE_CORNER_CATEGORY_NAME
        self.assembly_name = "2 Door Diagonal Corner Base"
        self.width = g.Base_Inside_Corner_Size
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Inside_Corner_Size
        self.carcass = LM_carcass.INSERT_Base_Inside_Corner_Diagonal_Carcass()
        self.exterior = LM_exteriors.INSERT_Base_Double_Door_FF()
        self.interior = None
        self.face_frame = "Face Frame"
         
class PRODUCT_1_Door_Diagonal_Corner_Upper(LM_cabinets.Face_Frame_Inside_Corner):
     
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = INSIDE_CORNER_CATEGORY_NAME
        self.assembly_name = "1 Door Diagonal Corner Upper"
        self.width = g.Upper_Inside_Corner_Size
        self.height = g.Base_Cabinet_Height
        self.depth = g.Upper_Inside_Corner_Size
        self.height_above_floor = g.Height_Above_Floor
        self.mirror_z = True
        self.carcass = LM_carcass.INSERT_Upper_Inside_Corner_Diagonal_Carcass()
        self.exterior = LM_exteriors.INSERT_Upper_Single_Door_FF()
        self.interior = None
        self.face_frame = "Face Frame"
         
class PRODUCT_2_Door_Diagonal_Corner_Upper(LM_cabinets.Face_Frame_Inside_Corner):
     
    def __init__(self):
        g = bpy.context.scene.lm_face_frame_cabients
        self.library_name = LIBRARY_NAME
        self.category_name = INSIDE_CORNER_CATEGORY_NAME
        self.assembly_name = "2 Door Diagonal Corner Upper"
        self.width = g.Upper_Inside_Corner_Size
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Inside_Corner_Size
        self.height_above_floor = g.Height_Above_Floor
        self.mirror_z = True
        self.carcass = LM_carcass.INSERT_Upper_Inside_Corner_Diagonal_Carcass()
        self.exterior = LM_exteriors.INSERT_Upper_Double_Door_FF()
        self.interior = None
        self.face_frame = "Face Frame"

class PROPERTIES_Scene_Variables(bpy.types.PropertyGroup):
    Base_Cabinet_Depth = bpy.props.FloatProperty(name="Base Cabinet Depth",
                                                 description="Default depth for base cabinets",
                                                 default=fd.inches(23.0),
                                                 unit='LENGTH')
    
    Base_Cabinet_Height = bpy.props.FloatProperty(name="Base Cabinet Height",
                                                  description="Default height for base cabinets",
                                                  default=fd.inches(34.0),
                                                  unit='LENGTH')
    
    Base_Inside_Corner_Size= bpy.props.FloatProperty(name="Base Inside Corner Size",
                                                     description="Default width and depth for the inside base corner cabinets",
                                                     default=fd.inches(36.0),
                                                     unit='LENGTH')    
    
    Tall_Cabinet_Depth = bpy.props.FloatProperty(name="Tall Cabinet Depth",
                                                 description="Default depth for tall cabinets",
                                                 default=fd.inches(25.0),
                                                 unit='LENGTH')
    
    Tall_Cabinet_Height = bpy.props.FloatProperty(name="Tall Cabinet Height",
                                                  description="Default height for tall cabinets",
                                                  default=fd.inches(84.0),
                                                  unit='LENGTH')
    
    Upper_Cabinet_Depth = bpy.props.FloatProperty(name="Upper Cabinet Depth",
                                                  description="Default depth for upper cabinets",
                                                  default=fd.inches(12.0),
                                                  unit='LENGTH')
    
    Upper_Cabinet_Height = bpy.props.FloatProperty(name="Upper Cabinet Height",
                                                   description="Default height for upper cabinets",
                                                   default=fd.inches(34.0),
                                                   unit='LENGTH')
    
    Upper_Inside_Corner_Size= bpy.props.FloatProperty(name="Upper Inside Corner Size",
                                                      description="Default width and depth for the inside upper corner cabinets",
                                                      default=fd.inches(24.0),
                                                      unit='LENGTH')    
    
    Sink_Cabinet_Depth = bpy.props.FloatProperty(name="Upper Cabinet Depth",
                                                 description="Default depth for sink cabinets",
                                                 default=fd.inches(23.0),
                                                 unit='LENGTH')
    
    Sink_Cabinet_Height = bpy.props.FloatProperty(name="Upper Cabinet Height",
                                                  description="Default height for sink cabinets",
                                                  default=fd.inches(34.0),
                                                  unit='LENGTH')

    Suspended_Cabinet_Depth = bpy.props.FloatProperty(name="Upper Cabinet Depth",
                                                      description="Default depth for suspended cabinets",
                                                      default=fd.inches(23.0),
                                                      unit='LENGTH')
    
    Suspended_Cabinet_Height = bpy.props.FloatProperty(name="Upper Cabinet Height",
                                                       description="Default height for suspended cabinets",
                                                       default=fd.inches(6.0),
                                                       unit='LENGTH')

    Width_1_Door = bpy.props.FloatProperty(name="Width 1 Door",
                                           description="Default width for one door wide cabinets",
                                           default=fd.inches(18.0),
                                           unit='LENGTH')
    
    Width_2_Door = bpy.props.FloatProperty(name="Width 2 Door",
                                           description="Default width for two door wide and open cabinets",
                                           default=fd.inches(36.0),
                                           unit='LENGTH')
    
    Width_Drawer = bpy.props.FloatProperty(name="Width Drawer",
                                           description="Default width for drawer cabinets",
                                           default=fd.inches(18.0),
                                           unit='LENGTH')
    
    Base_Width_Blind = bpy.props.FloatProperty(name="Base Width Blind",
                                               description="Default width for base blind corner cabinets",
                                               default=fd.inches(48.0),
                                               unit='LENGTH')
    
    Tall_Width_Blind = bpy.props.FloatProperty(name="Tall Width Blind",
                                               description="Default width for tall blind corner cabinets",
                                               default=fd.inches(48.0),
                                               unit='LENGTH')
    
    Blind_Panel_Reveal = bpy.props.FloatProperty(name="Blind Panel Reveal",
                                                 description="Default reveal for blind panels",
                                                 default=fd.inches(3.0),
                                                 unit='LENGTH')
    
    Inset_Blind_Panel = bpy.props.BoolProperty(name="Inset Blind Panel",
                                               description="Check this to inset the blind panel into the cabinet carcass",
                                               default=True)
    
    Upper_Width_Blind = bpy.props.FloatProperty(name="Upper Width Blind",
                                                description="Default width for upper blind corner cabinets",
                                                default=fd.inches(36.0),
                                                unit='LENGTH')

    Height_Above_Floor = bpy.props.FloatProperty(name="Height Above Floor",
                                                 description="Default height above floor for upper cabinets",
                                                 default=fd.inches(84.0),
                                                 unit='LENGTH')
    
    Equal_Drawer_Stack_Heights = bpy.props.BoolProperty(name="Equal Drawer Stack Heights", 
                                                        description="Check this make all drawer stack heights equal. Otherwise the Top Drawer Height will be set.", 
                                                        default=True)
    
    Top_Drawer_Front_Height = bpy.props.FloatProperty(name="Top Drawer Front Height",
                                                      description="Default top drawer front height.",
                                                      default=fd.inches(6.0),
                                                      unit='LENGTH')
    
    def draw(self,layout):
        col = layout.column(align=True)
        box = col.box()
        box.label("Standard Face Frame Cabinet Sizes:")
        
        row = box.row(align=True)
        row.label("Base:")
        row.prop(self,"Base_Cabinet_Height",text="Height")
        row.prop(self,"Base_Cabinet_Depth",text="Depth")
        
        row = box.row(align=True)
        row.label("Tall:")
        row.prop(self,"Tall_Cabinet_Height",text="Height")
        row.prop(self,"Tall_Cabinet_Depth",text="Depth")
        
        row = box.row(align=True)
        row.label("Upper:")
        row.prop(self,"Upper_Cabinet_Height",text="Height")
        row.prop(self,"Upper_Cabinet_Depth",text="Depth")

        row = box.row(align=True)
        row.label("Sink:")
        row.prop(self,"Sink_Cabinet_Height",text="Height")
        row.prop(self,"Sink_Cabinet_Depth",text="Depth")
        
        row = box.row(align=True)
        row.label("Suspended:")
        row.prop(self,"Suspended_Cabinet_Height",text="Height")
        row.prop(self,"Suspended_Cabinet_Depth",text="Depth")
        
        row = box.row(align=True)
        row.label("1 Door Wide:")
        row.prop(self,"Width_1_Door",text="Width")
        
        row = box.row(align=True)
        row.label("2 Door Wide:")
        row.prop(self,"Width_2_Door",text="Width")
        
        row = box.row(align=True)
        row.label("Drawer Stack Width:")
        row.prop(self,"Width_Drawer",text="Width")

        box = col.box()
        box.label("Blind Cabinet Widths:")
        
        row = box.row(align=True)
        row.label('Base:')
        row.prop(self,"Base_Width_Blind",text="Width")
        
        row = box.row(align=True)
        row.label('Tall:')
        row.prop(self,"Tall_Width_Blind",text="Width")
        
        row = box.row(align=True)
        row.label('Upper:')
        row.prop(self,"Upper_Width_Blind",text="Width")

        box = col.box()
        box.label("Inside Corner Cabinet Sizes:")
        row = box.row(align=True)
        row.label("Base:")
        row.prop(self,"Base_Inside_Corner_Size",text="")
        
        row = box.row(align=True)
        row.label("Upper:")
        row.prop(self,"Upper_Inside_Corner_Size",text="")
        
        box = col.box()
        box.label("Placement:")
        row = box.row(align=True)
        row.label("Height Above Floor:")
        row.prop(self,"Height_Above_Floor",text="")
        
        box = col.box()
        box.label("Drawer Heights:")
        row = box.row(align=True)
        row.prop(self,"Equal_Drawer_Stack_Heights")
        if not self.Equal_Drawer_Stack_Heights:
            row.prop(self,"Top_Drawer_Front_Height")
                
def register():
    bpy.utils.register_class(PROPERTIES_Scene_Variables)
    bpy.types.Scene.lm_face_frame_cabients = bpy.props.PointerProperty(type = PROPERTIES_Scene_Variables)

def unregister():
    bpy.utils.unregister_class(PROPERTIES_Scene_Variables)
