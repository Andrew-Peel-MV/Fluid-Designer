"""
Microvellum 
Frameless Library
Stores all the products for the Frameless Library
"""

import bpy
import fd
import LM_cabinets
import LM_carcass
import LM_exteriors
import LM_interiors
import LM_splitters

LIBRARY_NAME = "Cabinets - Frameless"
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

class PRODUCT_1_Door_Base(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = BASE_CATEGORY_NAME
        self.assembly_name = "1 Door Base"
        self.width = g.Width_1_Door
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.exterior = LM_exteriors.INSERT_Base_Single_Door()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_2_Door_Base(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = BASE_CATEGORY_NAME
        self.assembly_name = "2 Door Base"
        self.width = g.Width_2_Door
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.exterior = LM_exteriors.INSERT_Base_Double_Door()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_2_Door_Sink(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = BASE_CATEGORY_NAME
        self.assembly_name = "2 Door Sink"
        self.width = g.Width_2_Door
        self.height = g.Sink_Cabinet_Height
        self.depth = g.Sink_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Sink_Carcass()
        self.exterior = LM_exteriors.INSERT_Base_Double_Door()
        self.interior = None
        
class PRODUCT_2_Door_with_False_Front_Sink(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = BASE_CATEGORY_NAME
        self.assembly_name = "2 Door with False Front Sink"
        self.width = g.Width_2_Door
        self.height = g.Sink_Cabinet_Height
        self.depth = g.Sink_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Sink_Carcass()
        self.exterior = LM_exteriors.INSERT_Base_Double_Door_With_False_Front()
        self.interior = None
        
class PRODUCT_2_Door_2_False_Front_Sink(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = BASE_CATEGORY_NAME
        self.assembly_name = "2 Door 2 False Front Sink"
        self.width = g.Width_2_Door
        self.height = g.Sink_Cabinet_Height
        self.depth = g.Sink_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Sink_Carcass()
        self.exterior = LM_exteriors.INSERT_Base_Double_Door_With_2_False_Front()
        self.interior = None
        
class PRODUCT_1_Door_Sink(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = BASE_CATEGORY_NAME
        self.assembly_name = "1 Door Sink"
        self.width = g.Width_1_Door
        self.height = g.Sink_Cabinet_Height
        self.depth = g.Sink_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Sink_Carcass()
        self.exterior = LM_exteriors.INSERT_Base_Single_Door()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_1_Door_1_Drawer_Base(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = BASE_CATEGORY_NAME
        self.assembly_name = "1 Door 1 Drawer Base"
        self.width = g.Width_1_Door
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings()
        self.splitter.opening_1_height = g.Top_Drawer_Front_Height - fd.inches(1)
        self.splitter.exterior_1 = LM_exteriors.INSERT_1_Drawer()
        self.splitter.exterior_1.prompts = {'Half Overlay Bottom':True}
        self.splitter.interior_2 = LM_interiors.INSERT_Shelves()
        self.splitter.exterior_2 = LM_exteriors.INSERT_Base_Single_Door()
        self.splitter.exterior_2.prompts = {'Half Overlay Top':True}

class PRODUCT_2_Door_2_Drawer_Base(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = BASE_CATEGORY_NAME
        self.assembly_name = "2 Door 2 Drawer Base"
        self.width = g.Width_2_Door
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings()
        self.splitter.opening_1_height = g.Top_Drawer_Front_Height - fd.inches(1)
        self.splitter.exterior_1 = LM_exteriors.INSERT_Horizontal_Drawers()
        self.splitter.exterior_1.prompts = {'Half Overlay Bottom':True}
        self.splitter.interior_2 = LM_interiors.INSERT_Shelves()
        self.splitter.exterior_2 = LM_exteriors.INSERT_Base_Double_Door()
        self.splitter.exterior_2.prompts = {'Half Overlay Top':True}

class PRODUCT_Microwave_2_Door_Base(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = BASE_CATEGORY_NAME
        self.assembly_name = "Microwave 2 Door Base"
        self.width = g.Width_2_Door
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings()
        self.splitter.exterior_2 = LM_exteriors.INSERT_Base_Double_Door()

class PRODUCT_Microwave_2_Drawer_Base(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = BASE_CATEGORY_NAME
        self.assembly_name = "Microwave 2 Drawer Base"
        self.width = g.Width_2_Door
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings()
        self.splitter.exterior_2 = LM_exteriors.INSERT_2_Drawer_Stack()

#---------PRODUCT: TALL CABINETS

class PRODUCT_4_Door_Oven_Tall(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = TALL_CATEGORY_NAME
        self.assembly_name = "4 Door Oven Tall"
        self.width = g.Width_2_Door
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Carcass()
        self.splitter = LM_splitters.INSERT_3_Vertical_Openings()
        self.splitter.exterior_1 = LM_exteriors.INSERT_Upper_Double_Door()
        self.splitter.exterior_3 = LM_exteriors.INSERT_Base_Double_Door()

class PRODUCT_4_Door_Micro_and_Oven_Tall(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = TALL_CATEGORY_NAME
        self.assembly_name = "4 Door Micro and Oven Tall"
        self.width = g.Width_2_Door
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Carcass()
        self.splitter = LM_splitters.INSERT_4_Vertical_Openings()
        self.splitter.exterior_1 = LM_exteriors.INSERT_Upper_Double_Door()
        self.splitter.exterior_4 = LM_exteriors.INSERT_Base_Double_Door()

class PRODUCT_Refrigerator_Tall(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = TALL_CATEGORY_NAME
        self.assembly_name = "Refrigerator Tall"
        self.width = g.Width_2_Door
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Carcass()
        self.carcass.prompts = {'Remove Bottom':True}
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings()
        self.splitter.opening_1_height = fd.inches(10)
        self.splitter.exterior_1 = LM_exteriors.INSERT_Upper_Double_Door()
        
class PRODUCT_1_Door_Tall(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = TALL_CATEGORY_NAME
        self.assembly_name = "1 Door Tall"
        self.width = g.Width_1_Door
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Carcass()
        self.exterior = LM_exteriors.INSERT_Tall_Single_Door()
        self.interior = LM_interiors.INSERT_Shelves()
        
class PRODUCT_2_Door_Tall(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = TALL_CATEGORY_NAME
        self.assembly_name = "2 Door Tall"
        self.width = g.Width_2_Door
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Carcass()
        self.exterior = LM_exteriors.INSERT_Tall_Double_Door()
        self.interior = LM_interiors.INSERT_Shelves()
        
class PRODUCT_1_Double_Door_Tall(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = TALL_CATEGORY_NAME
        self.assembly_name = "1 Double Door Tall"
        self.width = g.Width_1_Door
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings()
        self.splitter.exterior_1 = LM_exteriors.INSERT_Upper_Single_Door()
        self.splitter.exterior_1.prompts = {'Half Overlay Bottom':True}
        self.splitter.interior_2 = LM_interiors.INSERT_Shelves()
        self.splitter.exterior_2 = LM_exteriors.INSERT_Base_Single_Door()
        self.splitter.exterior_2.prompts = {'Half Overlay Top':True}

class PRODUCT_2_Double_Door_Tall(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = TALL_CATEGORY_NAME
        self.assembly_name = "2 Double Door Tall"
        self.width = g.Width_2_Door
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings()
        self.splitter.exterior_1 = LM_exteriors.INSERT_Upper_Double_Door()
        self.splitter.exterior_1.prompts = {'Half Overlay Bottom':True}
        self.splitter.interior_2 = LM_interiors.INSERT_Shelves()
        self.splitter.exterior_2 = LM_exteriors.INSERT_Base_Double_Door()
        self.splitter.exterior_2.prompts = {'Half Overlay Top':True}
        
class PRODUCT_2_Door_2_Drawer_Tall(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = TALL_CATEGORY_NAME
        self.assembly_name = "2 Door 2 Drawer Tall"
        self.width = g.Width_2_Door
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings()
        self.splitter.opening_2_height = fd.inches(20)
        self.splitter.exterior_1 = LM_exteriors.INSERT_Tall_Double_Door()
        self.splitter.exterior_1.prompts = {'Half Overlay Bottom':True}
        self.splitter.interior_1 = LM_interiors.INSERT_Shelves()
        self.splitter.exterior_2 = LM_exteriors.INSERT_2_Drawer_Stack()
        self.splitter.exterior_2.prompts = {'Half Overlay Top':True}

class PRODUCT_2_Door_3_Drawer_Tall(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = TALL_CATEGORY_NAME
        self.assembly_name = "2 Door 3 Drawer Tall"
        self.width = g.Width_2_Door
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings()
        self.splitter.opening_2_height = fd.inches(20)
        self.splitter.exterior_1 = LM_exteriors.INSERT_Tall_Double_Door()
        self.splitter.exterior_1.prompts = {'Half Overlay Bottom':True}
        self.splitter.interior_1 = LM_interiors.INSERT_Shelves()
        self.splitter.exterior_2 = LM_exteriors.INSERT_3_Drawer_Stack()
        self.splitter.exterior_2.prompts = {'Half Overlay Top':True}
        
#---------PRODUCT: UPPER CABINETS

class PRODUCT_1_Door_Upper(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = UPPER_CATEGORY_NAME
        self.assembly_name = "1 Door Upper"
        self.width = g.Width_1_Door
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Cabinet_Depth
        self.mirror_z = True
        self.height_above_floor = g.Height_Above_Floor
        self.carcass = LM_carcass.INSERT_Upper_Carcass()
        self.exterior = LM_exteriors.INSERT_Upper_Single_Door()
        self.interior = LM_interiors.INSERT_Shelves()
        
class PRODUCT_2_Door_Upper(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = UPPER_CATEGORY_NAME
        self.assembly_name = "2 Door Upper"
        self.width = g.Width_2_Door
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Cabinet_Depth
        self.mirror_z = True
        self.height_above_floor = g.Height_Above_Floor
        self.carcass = LM_carcass.INSERT_Upper_Carcass()
        self.exterior = LM_exteriors.INSERT_Upper_Double_Door()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_1_Double_Door_Upper(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = UPPER_CATEGORY_NAME
        self.assembly_name = "1 Double Door Upper"
        self.width = g.Width_1_Door
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Cabinet_Depth
        self.mirror_z = True
        self.height_above_floor = g.Height_Above_Floor
        self.carcass = LM_carcass.INSERT_Upper_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings()
        self.splitter.exterior_1 = LM_exteriors.INSERT_Upper_Single_Door()
        self.splitter.exterior_1.prompts = {'Half Overlay Bottom':True}
        self.splitter.exterior_2 = LM_exteriors.INSERT_Upper_Single_Door()
        self.splitter.exterior_2.prompts = {'Half Overlay Top':True}

class PRODUCT_2_Double_Door_Upper(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = UPPER_CATEGORY_NAME
        self.assembly_name = "2 Double Door Upper"
        self.width = g.Width_2_Door
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Cabinet_Depth
        self.mirror_z = True
        self.height_above_floor = g.Height_Above_Floor
        self.carcass = LM_carcass.INSERT_Upper_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings()
        self.splitter.exterior_1 = LM_exteriors.INSERT_Upper_Double_Door()
        self.splitter.exterior_1.prompts = {'Half Overlay Bottom':True}
        self.splitter.exterior_2 = LM_exteriors.INSERT_Upper_Double_Door()
        self.splitter.exterior_2.prompts = {'Half Overlay Top':True}

class PRODUCT_Microwave_2_Door_Upper(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = UPPER_CATEGORY_NAME
        self.assembly_name = "Microwave 2 Door Upper"
        self.width = g.Width_2_Door
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Cabinet_Depth
        self.mirror_z = True
        self.carcass = LM_carcass.INSERT_Upper_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings()
        self.splitter.exterior_1 = LM_exteriors.INSERT_Upper_Double_Door()

class PRODUCT_2_Door_Upper_with_Microwave(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = UPPER_CATEGORY_NAME
        self.assembly_name = "2 Door Upper with Microwave"
        self.width = fd.inches(30)
        self.height = g.Upper_Cabinet_Height - fd.inches(20)
        self.depth = g.Upper_Cabinet_Depth
        self.mirror_z = True
        self.height_above_floor = g.Height_Above_Floor
        self.carcass = LM_carcass.INSERT_Upper_Carcass()
        self.exterior = LM_exteriors.INSERT_Upper_Double_Door()
        self.interior = None
        self.add_microwave = True
        
class PRODUCT_2_Door_Upper_with_Vent(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = UPPER_CATEGORY_NAME
        self.assembly_name = "1 Door Upper with Vent"
        self.width = g.Width_2_Door
        self.height = g.Upper_Cabinet_Height - fd.inches(20)
        self.depth = g.Upper_Cabinet_Depth
        self.mirror_z = True
        self.height_above_floor = g.Height_Above_Floor
        self.carcass = LM_carcass.INSERT_Upper_Carcass()
        self.exterior = LM_exteriors.INSERT_Upper_Double_Door()
        self.interior = None
        self.add_vent_hood = True
        
class PRODUCT_2_Door_2_Drawer_Upper(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = UPPER_CATEGORY_NAME
        self.assembly_name = "2 Door 2 Drawer Upper"
        self.width = g.Width_2_Door
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Cabinet_Depth
        self.mirror_z = True
        self.height_above_floor = g.Height_Above_Floor
        self.carcass = LM_carcass.INSERT_Upper_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings()
        self.splitter.exterior_1 = LM_exteriors.INSERT_Upper_Double_Door()
        self.splitter.exterior_1.prompts = {'Half Overlay Bottom':True}
        self.splitter.interior_1 = LM_interiors.INSERT_Shelves()
        self.splitter.exterior_2 = LM_exteriors.INSERT_2_Drawer_Stack()
        self.splitter.exterior_2.prompts = {'Half Overlay Top':True}

#---------PRODUCT: OUTSIDE CORNER CABINETS

class PRODUCT_Outside_Radius_Corner_Base(LM_cabinets.Frameless_Outside_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = OUTSIDE_CORNER_CATEGORY_NAME
        self.assembly_name = "Outside Radius Corner Base"
        self.width = g.Width_1_Door
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Outside_Radius_Corner_Carcass()
        self.exterior = None
        self.interior = None

class PRODUCT_Outside_Radius_Corner_Tall(LM_cabinets.Frameless_Outside_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = OUTSIDE_CORNER_CATEGORY_NAME
        self.assembly_name = "Outside Radius Corner Tall"
        self.width = g.Width_1_Door
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Outside_Radius_Corner_Carcass()
        self.exterior = None
        self.interior = None
        
class PRODUCT_Outside_Radius_Corner_Upper(LM_cabinets.Frameless_Outside_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = OUTSIDE_CORNER_CATEGORY_NAME
        self.assembly_name = "Outside Radius Corner Upper"
        self.width = g.Width_1_Door
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Cabinet_Depth
        self.mirror_z = True
        self.height_above_floor = g.Height_Above_Floor
        self.carcass = LM_carcass.INSERT_Upper_Outside_Radius_Corner_Carcass()
        self.exterior = None
        self.interior = None
        
class PRODUCT_Outside_Chamfer_Corner_Base(LM_cabinets.Frameless_Outside_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = OUTSIDE_CORNER_CATEGORY_NAME
        self.assembly_name = "Outside Chamfer Corner Base"
        self.width = g.Width_1_Door
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Outside_Chamfered_Corner_Carcass()
        self.exterior = None
        self.interior = None

class PRODUCT_Outside_Chamfer_Corner_Tall(LM_cabinets.Frameless_Outside_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = OUTSIDE_CORNER_CATEGORY_NAME
        self.assembly_name = "Outside Chamfer Corner Tall"
        self.width = g.Width_1_Door
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Outside_Chamfered_Corner_Carcass()
        self.exterior = None
        self.interior = None
        
class PRODUCT_Outside_Chamfer_Corner_Upper(LM_cabinets.Frameless_Outside_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = OUTSIDE_CORNER_CATEGORY_NAME
        self.assembly_name = "Outside Chamfer Corner Upper"
        self.width = g.Width_1_Door
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Cabinet_Depth
        self.mirror_z = True
        self.height_above_floor = g.Height_Above_Floor
        self.carcass = LM_carcass.INSERT_Upper_Outside_Chamfered_Corner_Carcass()
        self.exterior = None
        self.interior = None
        
#---------PRODUCT: TRANSITION CABINETS

class PRODUCT_1_Door_Base_Transition(LM_cabinets.Frameless_Transition):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = TRANSITION_CATEGORY_NAME
        self.assembly_name = "1 Door Base Transition"
        self.width = g.Width_1_Door
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Transition_Carcass()
        self.exterior = LM_exteriors.INSERT_Base_Single_Door()
        self.exterior.prompts = {'Half Overlay Left':True,'Half Overlay Right':True}
        self.interior = None

class PRODUCT_2_Door_Base_Transition(LM_cabinets.Frameless_Transition):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = TRANSITION_CATEGORY_NAME
        self.assembly_name = "2 Door Base Transition"
        self.width = g.Width_2_Door
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Transition_Carcass()
        self.exterior = LM_exteriors.INSERT_Base_Double_Door()
        self.exterior.prompts = {'Half Overlay Left':True,'Half Overlay Right':True}
        self.interior = None

class PRODUCT_1_Door_Tall_Transition(LM_cabinets.Frameless_Transition):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = TRANSITION_CATEGORY_NAME
        self.assembly_name = "1 Door Tall Transition"
        self.width = g.Width_1_Door
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Transition_Carcass()
        self.exterior = LM_exteriors.INSERT_Tall_Single_Door()
        self.exterior.prompts = {'Half Overlay Left':True,'Half Overlay Right':True}
        self.interior = None

class PRODUCT_2_Door_Tall_Transition(LM_cabinets.Frameless_Transition):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = TRANSITION_CATEGORY_NAME
        self.assembly_name = "2 Door Tall Transition"
        self.width = g.Width_2_Door
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Transition_Carcass()
        self.exterior = LM_exteriors.INSERT_Tall_Double_Door()
        self.exterior.prompts = {'Half Overlay Left':True,'Half Overlay Right':True}
        self.interior = None

class PRODUCT_1_Door_Upper_Transition(LM_cabinets.Frameless_Transition):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = TRANSITION_CATEGORY_NAME
        self.assembly_name = "1 Door Upper Transition"
        self.width = g.Width_1_Door
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Cabinet_Depth
        self.mirror_z = True
        self.height_above_floor = g.Height_Above_Floor
        self.carcass = LM_carcass.INSERT_Upper_Transition_Carcass()
        self.exterior = LM_exteriors.INSERT_Upper_Single_Door()
        self.exterior.prompts = {'Half Overlay Left':True,'Half Overlay Right':True}
        self.interior = None

class PRODUCT_2_Door_Upper_Transition(LM_cabinets.Frameless_Transition):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = TRANSITION_CATEGORY_NAME
        self.assembly_name = "2 Door Upper Transition"
        self.width = g.Width_2_Door
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Cabinet_Depth
        self.mirror_z = True
        self.height_above_floor = g.Height_Above_Floor
        self.carcass = LM_carcass.INSERT_Upper_Transition_Carcass()
        self.exterior = LM_exteriors.INSERT_Upper_Double_Door()
        self.exterior.prompts = {'Half Overlay Left':True,'Half Overlay Right':True}
        self.interior = None
        
#---------PRODUCT: STARTER CABINETS

class PRODUCT_Base_Starter(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = STARTER_CATEGORY_NAME
        self.assembly_name = "Base Starter"
        self.width = g.Width_1_Door
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.exterior = None
        self.interior = None
        self.add_empty_opening = True

class PRODUCT_Tall_Starter(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = STARTER_CATEGORY_NAME
        self.assembly_name = "Tall Starter"
        self.width = g.Width_1_Door
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Carcass()
        self.exterior = None
        self.interior = None
        self.add_empty_opening = True

class PRODUCT_Upper_Starter(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = STARTER_CATEGORY_NAME
        self.assembly_name = "Upper Starter"
        self.width = g.Width_1_Door
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Cabinet_Depth
        self.mirror_z = True
        self.carcass = LM_carcass.INSERT_Upper_Carcass()
        self.exterior = None
        self.interior = None
        self.height_above_floor = g.Height_Above_Floor
        self.add_empty_opening = True

class PRODUCT_Sink_Starter(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = STARTER_CATEGORY_NAME
        self.assembly_name = "Sink Starter"
        self.width = g.Width_1_Door
        self.height = g.Sink_Cabinet_Height
        self.depth = g.Sink_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Sink_Carcass()
        self.exterior = None
        self.interior = None
        self.add_empty_opening = True

class PRODUCT_Suspended_Starter(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = STARTER_CATEGORY_NAME
        self.assembly_name = "Suspended Starter"
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
        
class PRODUCT_1_Drawer(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = DRAWER_CATEGORY_NAME
        self.assembly_name = "1 Drawer"
        self.width = g.Width_Drawer
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.exterior = LM_exteriors.INSERT_1_Drawer()

class PRODUCT_2_Drawer(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = DRAWER_CATEGORY_NAME
        self.assembly_name = "2 Drawer"
        self.width = g.Width_Drawer
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.exterior = LM_exteriors.INSERT_2_Drawer_Stack()
        if not g.Equal_Drawer_Stack_Heights:
            self.exterior.top_drawer_front_height = g.Top_Drawer_Front_Height

class PRODUCT_3_Drawer(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = DRAWER_CATEGORY_NAME
        self.assembly_name = "3 Drawer"
        self.width = g.Width_Drawer
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.exterior = LM_exteriors.INSERT_3_Drawer_Stack()
        if not g.Equal_Drawer_Stack_Heights:
            self.exterior.top_drawer_front_height = g.Top_Drawer_Front_Height
            
class PRODUCT_4_Drawer(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = DRAWER_CATEGORY_NAME
        self.assembly_name = "4 Drawer"
        self.width = g.Width_Drawer
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.exterior = LM_exteriors.INSERT_4_Drawer_Stack()
        if not g.Equal_Drawer_Stack_Heights:
            self.exterior.top_drawer_front_height = g.Top_Drawer_Front_Height
            
class PRODUCT_1_Drawer_Suspended(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = DRAWER_CATEGORY_NAME
        self.assembly_name = "1 Drawer Suspended"
        self.width = g.Width_Drawer
        self.height = g.Suspended_Cabinet_Height
        self.depth = g.Suspended_Cabinet_Depth
        self.mirror_z = True
        self.carcass = LM_carcass.INSERT_Suspended_Carcass()
        self.height_above_floor = g.Base_Cabinet_Height
        self.exterior = LM_exteriors.INSERT_1_Drawer()
        
class PRODUCT_2_Drawer_Suspended(LM_cabinets.Frameless_Standard):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = DRAWER_CATEGORY_NAME
        self.assembly_name = "2 Drawer Suspended"
        self.width = g.Width_Drawer * 2
        self.height = g.Suspended_Cabinet_Height
        self.depth = g.Suspended_Cabinet_Depth
        self.mirror_z = True
        self.carcass = LM_carcass.INSERT_Suspended_Carcass()
        self.height_above_floor = g.Base_Cabinet_Height
        self.exterior = LM_exteriors.INSERT_Horizontal_Drawers()
        
#---------PRODUCT: BLIND CORNER CABINETS

class PRODUCT_1_Door_Blind_Left_Corner_Base(LM_cabinets.Frameless_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "1 Door Blind Left Corner Base"
        self.blind_side = "Left"
        self.width = g.Base_Width_Blind
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.exterior = LM_exteriors.INSERT_Base_Single_Door()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_1_Door_Blind_Right_Corner_Base(LM_cabinets.Frameless_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "1 Door Blind Right Corner Base"
        self.blind_side = "Right"
        self.width = g.Base_Width_Blind
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.exterior = LM_exteriors.INSERT_Base_Single_Door()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_1_Door_Blind_Left_Corner_Tall(LM_cabinets.Frameless_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "1 Door Blind Left Corner Tall"
        self.blind_side = "Left"
        self.width = g.Tall_Width_Blind
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Carcass()
        self.exterior = LM_exteriors.INSERT_Tall_Single_Door()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_1_Door_Blind_Right_Corner_Tall(LM_cabinets.Frameless_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "1 Door Blind Right Corner Tall"
        self.blind_side = "Right"
        self.width = g.Tall_Width_Blind
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Carcass()
        self.exterior = LM_exteriors.INSERT_Tall_Single_Door()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_1_Door_Blind_Left_Corner_Upper(LM_cabinets.Frameless_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "1 Door Blind Left Corner Upper"
        self.blind_side = "Left"
        self.height_above_floor = g.Height_Above_Floor
        self.mirror_z = True
        self.width = g.Upper_Width_Blind
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Upper_Carcass()
        self.exterior = LM_exteriors.INSERT_Upper_Single_Door()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_1_Door_Blind_Right_Corner_Upper(LM_cabinets.Frameless_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "1 Door Blind Right Corner Upper"
        self.blind_side = "Right"
        self.height_above_floor = g.Height_Above_Floor
        self.mirror_z = True
        self.width = g.Upper_Width_Blind
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Upper_Carcass()
        self.exterior = LM_exteriors.INSERT_Upper_Single_Door()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_2_Door_Blind_Left_Corner_Base(LM_cabinets.Frameless_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "2 Door Blind Left Corner Base"
        self.blind_side = "Left"
        self.width = g.Base_Width_Blind
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.exterior = LM_exteriors.INSERT_Base_Single_Door()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_2_Door_Blind_Right_Corner_Base(LM_cabinets.Frameless_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "2 Door Blind Right Corner Base"
        self.blind_side = "Right"
        self.width = g.Base_Width_Blind
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.exterior = LM_exteriors.INSERT_Base_Double_Door()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_2_Door_Blind_Left_Corner_Tall(LM_cabinets.Frameless_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "2 Door Blind Left Corner Tall"
        self.blind_side = "Left"
        self.width = g.Tall_Width_Blind
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Carcass()
        self.exterior = LM_exteriors.INSERT_Tall_Double_Door()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_2_Door_Blind_Right_Corner_Tall(LM_cabinets.Frameless_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "2 Door Blind Right Corner Tall"
        self.blind_side = "Right"
        self.width = g.Tall_Width_Blind
        self.height = g.Tall_Cabinet_Height
        self.depth = g.Tall_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Tall_Carcass()
        self.exterior = LM_exteriors.INSERT_Tall_Double_Door()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_2_Door_Blind_Left_Corner_Upper(LM_cabinets.Frameless_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "2 Door Blind Left Corner Upper"
        self.blind_side = "Left"
        self.height_above_floor = g.Height_Above_Floor
        self.mirror_z = True
        self.width = g.Upper_Width_Blind
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Upper_Carcass()
        self.exterior = LM_exteriors.INSERT_Upper_Double_Door()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_2_Door_Blind_Right_Corner_Upper(LM_cabinets.Frameless_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "2 Door Blind Right Corner Upper"
        self.blind_side = "Right"
        self.height_above_floor = g.Height_Above_Floor
        self.mirror_z = True
        self.width = g.Upper_Width_Blind
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Upper_Carcass()
        self.exterior = LM_exteriors.INSERT_Upper_Double_Door()
        self.interior = LM_interiors.INSERT_Shelves()

class PRODUCT_1_Door_1_Drawer_Blind_Right_Corner_Base(LM_cabinets.Frameless_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "1 Door 1 Drawer Blind Right Corner Base"
        self.blind_side = "Right"
        self.width = g.Base_Width_Blind
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings()
        self.splitter.opening_1_height = g.Top_Drawer_Front_Height - fd.inches(1)
        self.splitter.exterior_1 = LM_exteriors.INSERT_1_Drawer()
        self.splitter.exterior_1.prompts = {'Half Overlay Bottom':True}
        self.splitter.exterior_2 = LM_exteriors.INSERT_Base_Single_Door()
        self.splitter.exterior_2.prompts = {'Half Overlay Top':True}
        
class PRODUCT_1_Door_1_Drawer_Blind_Left_Corner_Base(LM_cabinets.Frameless_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "1 Door 1 Drawer Blind Left Corner Base"
        self.blind_side = "Left"
        self.width = g.Base_Width_Blind
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings()
        self.splitter.opening_1_height = g.Top_Drawer_Front_Height - fd.inches(1)
        self.splitter.exterior_1 = LM_exteriors.INSERT_1_Drawer()
        self.splitter.exterior_1.prompts = {'Half Overlay Bottom':True}
        self.splitter.exterior_2 = LM_exteriors.INSERT_Base_Single_Door()
        self.splitter.exterior_2.prompts = {'Half Overlay Top':True}
        
class PRODUCT_2_Door_2_Drawer_Blind_Right_Corner_Base(LM_cabinets.Frameless_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "2 Door 2 Drawer Blind Right Corner Base"
        self.blind_side = "Right"
        self.width = g.Base_Width_Blind
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings()
        self.splitter.opening_1_height = g.Top_Drawer_Front_Height - fd.inches(1)
        self.splitter.exterior_1 = LM_exteriors.INSERT_Horizontal_Drawers()
        self.splitter.exterior_1.prompts = {'Half Overlay Bottom':True}
        self.splitter.exterior_2 = LM_exteriors.INSERT_Base_Double_Door()
        self.splitter.exterior_2.prompts = {'Half Overlay Top':True}
        
class PRODUCT_2_Door_2_Drawer_Blind_Left_Corner_Base(LM_cabinets.Frameless_Blind_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.assembly_name = "2 Door 2 Drawer Blind Left Corner Base"
        self.blind_side = "Left"
        self.width = g.Base_Width_Blind
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Cabinet_Depth
        self.carcass = LM_carcass.INSERT_Base_Carcass()
        self.splitter = LM_splitters.INSERT_2_Vertical_Openings()
        self.splitter.opening_1_height = g.Top_Drawer_Front_Height - fd.inches(1)
        self.splitter.exterior_1 = LM_exteriors.INSERT_Horizontal_Drawers()
        self.splitter.exterior_1.prompts = {'Half Overlay Bottom':True}
        self.splitter.exterior_2 = LM_exteriors.INSERT_Base_Double_Door()
        self.splitter.exterior_2.prompts = {'Half Overlay Top':True}
        
#---------PRODUCT: INSIDE CORNER CABINETS

class PRODUCT_Pie_Cut_Corner_Base(LM_cabinets.Frameless_Inside_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = INSIDE_CORNER_CATEGORY_NAME
        self.assembly_name = "Pie Cut Corner Base"
        self.width = g.Base_Inside_Corner_Size
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Inside_Corner_Size
        self.carcass = LM_carcass.INSERT_Base_Inside_Corner_Notched_Carcass()
        self.exterior = LM_exteriors.INSERT_Base_Pie_Cut_Door()
        self.interior = None
        
class PRODUCT_Pie_Cut_Corner_Upper(LM_cabinets.Frameless_Inside_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = INSIDE_CORNER_CATEGORY_NAME
        self.assembly_name = "Pie Cut Corner Upper"
        self.width = g.Upper_Inside_Corner_Size
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Inside_Corner_Size
        self.height_above_floor = g.Height_Above_Floor
        self.mirror_z = True
        self.carcass = LM_carcass.INSERT_Upper_Inside_Corner_Notched_Carcass()
        self.exterior = LM_exteriors.INSERT_Upper_Pie_Cut_Door()
        self.interior = None
        
class PRODUCT_1_Door_Diagonal_Corner_Base(LM_cabinets.Frameless_Inside_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = INSIDE_CORNER_CATEGORY_NAME
        self.assembly_name = "1 Door Diagonal Corner Base"
        self.width = g.Base_Inside_Corner_Size
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Inside_Corner_Size
        self.carcass = LM_carcass.INSERT_Base_Inside_Corner_Diagonal_Carcass()
        self.exterior = LM_exteriors.INSERT_Base_Single_Door()
        self.interior = None
        
class PRODUCT_2_Door_Diagonal_Corner_Base(LM_cabinets.Frameless_Inside_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = INSIDE_CORNER_CATEGORY_NAME
        self.assembly_name = "2 Door Diagonal Corner Base"
        self.width = g.Base_Inside_Corner_Size
        self.height = g.Base_Cabinet_Height
        self.depth = g.Base_Inside_Corner_Size
        self.carcass = LM_carcass.INSERT_Base_Inside_Corner_Diagonal_Carcass()
        self.exterior = LM_exteriors.INSERT_Base_Double_Door()
        self.interior = None
        
class PRODUCT_1_Door_Diagonal_Corner_Upper(LM_cabinets.Frameless_Inside_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = INSIDE_CORNER_CATEGORY_NAME
        self.assembly_name = "1 Door Diagonal Corner Upper"
        self.width = g.Upper_Inside_Corner_Size
        self.height = g.Base_Cabinet_Height
        self.depth = g.Upper_Inside_Corner_Size
        self.height_above_floor = g.Height_Above_Floor
        self.mirror_z = True
        self.carcass = LM_carcass.INSERT_Upper_Inside_Corner_Diagonal_Carcass()
        self.exterior = LM_exteriors.INSERT_Upper_Single_Door()
        self.interior = None
        
class PRODUCT_2_Door_Diagonal_Corner_Upper(LM_cabinets.Frameless_Inside_Corner):
    
    def __init__(self):
        g = bpy.context.scene.lm_frameless_cabinets
        self.library_name = LIBRARY_NAME
        self.category_name = INSIDE_CORNER_CATEGORY_NAME
        self.assembly_name = "2 Door Diagonal Corner Upper"
        self.width = g.Upper_Inside_Corner_Size
        self.height = g.Upper_Cabinet_Height
        self.depth = g.Upper_Inside_Corner_Size
        self.height_above_floor = g.Height_Above_Floor
        self.mirror_z = True
        self.carcass = LM_carcass.INSERT_Upper_Inside_Corner_Diagonal_Carcass()
        self.exterior = LM_exteriors.INSERT_Upper_Double_Door()
        self.interior = None

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
        box.label("Standard Frameless Cabinet Sizes:")
        
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
    bpy.types.Scene.lm_frameless_cabinets = bpy.props.PointerProperty(type = PROPERTIES_Scene_Variables)
    
def unregister():
    bpy.utils.unregister_class(PROPERTIES_Scene_Variables)
    