"""
Microvellum 
Closet Configurations
Stores the inserts for the closet configuration library
"""

import bpy
import fd

import LM_exteriors
import LM_interiors
import LM_splitters

LIBRARY_NAME = "Closet Configurations"
DOOR_DRAWER_CATEGORY_NAME = "Doors and Drawers"
HANGING_ROD_AND_SHELVES = "Hanging Rods and Shelves"

class INSERT_Tilt_Hamper_1(LM_splitters.Vertical_Splitters):
     
    def __init__(self):
        self.library_name = LIBRARY_NAME
        self.category_name = DOOR_DRAWER_CATEGORY_NAME
        self.assembly_name = "Tilt-Out Hamper"
        self.width = fd.inches(18)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
        self.vertical_openings = 2
        self.exterior_1 = None
        self.exterior_2 = LM_exteriors.INSERT_Tilt_Out_Hamper()
        self.exterior_2.prompts = {'Half Overlay Top':True, 'Half Overlay Bottom':True,'Half Overlay Left':True,'Half Overlay Right':True}
        self.opening_1_height = 0
        self.opening_2_height = fd.inches(25)
        
class INSERT_1_Drawer(LM_splitters.Vertical_Splitters):
    
    def __init__(self):
        self.library_name = LIBRARY_NAME
        self.category_name = DOOR_DRAWER_CATEGORY_NAME
        self.assembly_name = "1 Drawer"
        self.width = fd.inches(18)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
        self.vertical_openings = 2
        self.exterior_1 = None
        self.exterior_2 = LM_exteriors.INSERT_1_Drawer()
        self.exterior_2.prompts = {'Half Overlay Top':True, 'Half Overlay Bottom':True,'Half Overlay Left':True,'Half Overlay Right':True}
        self.opening_1_height = 0
        self.opening_2_height = fd.inches(25)
        
class INSERT_2_Drawer(LM_splitters.Vertical_Splitters):
     
    def __init__(self):
        self.library_name = LIBRARY_NAME
        self.category_name = DOOR_DRAWER_CATEGORY_NAME
        self.assembly_name = "2 Drawer"
        self.width = fd.inches(18)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
        self.vertical_openings = 2
        self.exterior_1 = None
        self.exterior_2 = LM_exteriors.INSERT_2_Drawer_Stack()
        self.exterior_2.prompts = {'Half Overlay Top':True, 'Half Overlay Bottom':True,'Half Overlay Left':True,'Half Overlay Right':True}
        self.opening_1_height = 0
        self.opening_2_height = fd.inches(25)
        
class INSERT_3_Drawer(LM_splitters.Vertical_Splitters):
     
    def __init__(self):
        self.library_name = LIBRARY_NAME
        self.category_name = DOOR_DRAWER_CATEGORY_NAME
        self.assembly_name = "3 Drawer"
        self.width = fd.inches(18)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
        self.vertical_openings = 2
        self.exterior_1 = None
        self.exterior_2 = LM_exteriors.INSERT_3_Drawer_Stack()
        self.exterior_2.prompts = {'Half Overlay Top':True, 'Half Overlay Bottom':True,'Half Overlay Left':True,'Half Overlay Right':True}
        self.opening_1_height = 0
        self.opening_2_height = fd.inches(25)
        
class INSERT_4_Drawer(LM_splitters.Vertical_Splitters):
     
    def __init__(self):
        self.library_name = LIBRARY_NAME
        self.category_name = DOOR_DRAWER_CATEGORY_NAME
        self.assembly_name = "4 Drawer"
        self.width = fd.inches(18)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
        self.vertical_openings = 2
        self.exterior_1 = None
        self.exterior_2 = LM_exteriors.INSERT_4_Drawer_Stack()
        self.exterior_2.prompts = {'Half Overlay Top':True, 'Half Overlay Bottom':True,'Half Overlay Left':True,'Half Overlay Right':True}
        self.opening_1_height = 0
        self.opening_2_height = fd.inches(25)
        
#---------INSERT Doors
        
class INSERT_Base_Doors(LM_splitters.Vertical_Splitters):
     
    def __init__(self):
        self.library_name = LIBRARY_NAME
        self.category_name = DOOR_DRAWER_CATEGORY_NAME
        self.assembly_name = "Base Doors"
        self.width = fd.inches(18)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
        self.vertical_openings = 2
        self.exterior_1 = None
        self.exterior_2 = LM_exteriors.INSERT_Base_Double_Door()
        self.exterior_2.prompts = {'Half Overlay Top':True, 'Half Overlay Bottom':True,'Half Overlay Left':True,'Half Overlay Right':True}
        self.opening_1_height = 0
        self.opening_2_height = fd.inches(30)
        
class INSERT_Upper_Doors(LM_splitters.Vertical_Splitters):
     
    def __init__(self):
        self.library_name = LIBRARY_NAME
        self.category_name = DOOR_DRAWER_CATEGORY_NAME
        self.assembly_name = "Upper Doors"
        self.width = fd.inches(18)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
        self.vertical_openings = 2
        self.exterior_2 = None
        self.exterior_1 = LM_exteriors.INSERT_Upper_Double_Door()
        self.exterior_1.prompts = {'Half Overlay Top':True, 'Half Overlay Bottom':True,'Half Overlay Left':True,'Half Overlay Right':True}
        self.opening_1_height =  fd.inches(30)
        self.opening_2_height = 0
        
#---------INSERT Door Drawer Configurations
        
class INSERT_2_Doors_Split_2_Doors(LM_splitters.Vertical_Splitters):
     
    def __init__(self):
        self.library_name = LIBRARY_NAME
        self.category_name = DOOR_DRAWER_CATEGORY_NAME
        self.assembly_name = "2 Doors Split 2 Doors"
        self.width = fd.inches(18)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
        self.vertical_openings = 3
        self.exterior_1 = LM_exteriors.INSERT_Upper_Double_Door()
        self.exterior_1.prompts = {'Half Overlay Top':True, 'Half Overlay Bottom':True,'Half Overlay Left':True,'Half Overlay Right':True}
        self.exterior_2 = None
        self.exterior_3 = LM_exteriors.INSERT_Base_Double_Door()
        self.exterior_3.prompts = {'Half Overlay Top':True, 'Half Overlay Bottom':True,'Half Overlay Left':True,'Half Overlay Right':True}
        self.opening_1_height = fd.inches(30)
        self.opening_2_height = 0
        self.opening_3_height = fd.inches(32)
        
class INSERT_2_Drawers_Split_2_Doors(LM_splitters.Vertical_Splitters):
     
    def __init__(self):
        self.library_name = LIBRARY_NAME
        self.category_name = DOOR_DRAWER_CATEGORY_NAME
        self.assembly_name = "2 Drawers Split 2 Doors"
        self.width = fd.inches(18)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
        self.vertical_openings = 3
        self.exterior_1 = LM_exteriors.INSERT_Upper_Double_Door()
        self.exterior_1.prompts = {'Half Overlay Top':True, 'Half Overlay Bottom':True,'Half Overlay Left':True,'Half Overlay Right':True}
        self.exterior_2 = None
        self.exterior_3 = LM_exteriors.INSERT_2_Drawer_Stack()
        self.exterior_3.prompts = {'Half Overlay Top':True, 'Half Overlay Bottom':True,'Half Overlay Left':True,'Half Overlay Right':True}
        self.opening_1_height = fd.inches(30)
        self.opening_2_height = 0
        self.opening_3_height = fd.inches(32)
        
class INSERT_3_Drawers_Split_2_Doors(LM_splitters.Vertical_Splitters):
     
    def __init__(self):
        self.library_name = LIBRARY_NAME
        self.category_name = DOOR_DRAWER_CATEGORY_NAME
        self.assembly_name = "3 Drawers Split 2 Doors"
        self.width = fd.inches(18)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
        self.vertical_openings = 3
        self.exterior_1 = LM_exteriors.INSERT_Upper_Double_Door()
        self.exterior_1.prompts = {'Half Overlay Top':True, 'Half Overlay Bottom':True,'Half Overlay Left':True,'Half Overlay Right':True}
        self.exterior_2 = None
        self.exterior_3 = LM_exteriors.INSERT_3_Drawer_Stack()
        self.exterior_3.prompts = {'Half Overlay Top':True, 'Half Overlay Bottom':True,'Half Overlay Left':True,'Half Overlay Right':True}
        self.opening_1_height = fd.inches(30)
        self.opening_2_height = 0
        self.opening_3_height = fd.inches(32)
        
class INSERT_4_Drawers_Split_2_Doors(LM_splitters.Vertical_Splitters):
     
    def __init__(self):
        self.library_name = LIBRARY_NAME
        self.category_name = DOOR_DRAWER_CATEGORY_NAME
        self.assembly_name = "4 Drawers Split 2 Doors"
        self.width = fd.inches(18)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
        self.vertical_openings = 3
        self.exterior_1 = LM_exteriors.INSERT_Upper_Double_Door()
        self.exterior_1.prompts = {'Half Overlay Top':True, 'Half Overlay Bottom':True,'Half Overlay Left':True,'Half Overlay Right':True}
        self.exterior_2 = None
        self.exterior_3 = LM_exteriors.INSERT_4_Drawer_Stack()
        self.exterior_3.prompts = {'Half Overlay Top':True, 'Half Overlay Bottom':True,'Half Overlay Left':True,'Half Overlay Right':True}
        self.opening_1_height = fd.inches(30)
        self.opening_2_height = 0
        self.opening_3_height = fd.inches(32)
        
class INSERT_Tilt_Hamper_3_Drawers_Split_2_Doors(LM_splitters.Vertical_Splitters):
     
    def __init__(self):
        self.library_name = LIBRARY_NAME
        self.category_name = DOOR_DRAWER_CATEGORY_NAME
        self.assembly_name = "Tilt-Out Hamper 3 Drawers Split 2 Doors"
        self.width = fd.inches(18)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
        self.vertical_openings = 4
        self.exterior_1 = LM_exteriors.INSERT_Upper_Double_Door()
        self.exterior_1.prompts = {'Half Overlay Top':True, 'Half Overlay Bottom':True,'Half Overlay Left':True,'Half Overlay Right':True}
        self.exterior_2 = None
        self.exterior_3 = LM_exteriors.INSERT_3_Drawer_Stack()
        self.exterior_3.prompts = {'Half Overlay Top':True, 'Half Overlay Bottom':True,'Half Overlay Left':True,'Half Overlay Right':True}
        self.exterior_4 = LM_exteriors.INSERT_Tilt_Out_Hamper()
        self.exterior_4.prompts = {'Half Overlay Top':True, 'Half Overlay Bottom':True,'Half Overlay Left':True,'Half Overlay Right':True}
        self.opening_1_height = fd.inches(30)
        self.opening_2_height = 0
        self.opening_3_height = fd.inches(15)
        self.opening_4_height = fd.inches(20)
        
class INSERT_Tilt_Hamper_2_Drawers_Split_2_Doors(LM_splitters.Vertical_Splitters):
     
    def __init__(self):
        self.library_name = LIBRARY_NAME
        self.category_name = DOOR_DRAWER_CATEGORY_NAME
        self.assembly_name = "Tilt-Out Hamper 2 Drawers Split 2 Doors"
        self.width = fd.inches(18)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
        self.vertical_openings = 4
        self.exterior_1 = LM_exteriors.INSERT_Upper_Double_Door()
        self.exterior_1.prompts = {'Half Overlay Top':True, 'Half Overlay Bottom':True,'Half Overlay Left':True,'Half Overlay Right':True}
        self.exterior_2 = None
        self.exterior_3 = LM_exteriors.INSERT_2_Drawer_Stack()
        self.exterior_3.prompts = {'Half Overlay Top':True, 'Half Overlay Bottom':True,'Half Overlay Left':True,'Half Overlay Right':True}
        self.exterior_4 = LM_exteriors.INSERT_Tilt_Out_Hamper()
        self.exterior_4.prompts = {'Half Overlay Top':True, 'Half Overlay Bottom':True,'Half Overlay Left':True,'Half Overlay Right':True}
        self.opening_1_height = fd.inches(30)
        self.opening_2_height = 0
        self.opening_3_height = fd.inches(10)
        self.opening_4_height = fd.inches(20)
        
class INSERT_Tilt_Hamper_1_Drawers_Split_2_Doors(LM_splitters.Vertical_Splitters):
     
    def __init__(self):
        self.library_name = LIBRARY_NAME
        self.category_name = DOOR_DRAWER_CATEGORY_NAME
        self.assembly_name = "Tilt-Out Hamper 1 Drawer Split 2 Doors"
        self.width = fd.inches(18)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
        self.vertical_openings = 4
        self.exterior_1 = LM_exteriors.INSERT_Upper_Double_Door()
        self.exterior_1.prompts = {'Half Overlay Top':True, 'Half Overlay Bottom':True,'Half Overlay Left':True,'Half Overlay Right':True}
        self.exterior_2 = None
        self.exterior_3 = LM_exteriors.INSERT_1_Drawer()
        self.exterior_3.prompts = {'Half Overlay Top':True, 'Half Overlay Bottom':True,'Half Overlay Left':True,'Half Overlay Right':True}
        self.exterior_4 = LM_exteriors.INSERT_Tilt_Out_Hamper()
        self.exterior_4.prompts = {'Half Overlay Top':True, 'Half Overlay Bottom':True,'Half Overlay Left':True,'Half Overlay Right':True}
        self.opening_1_height = fd.inches(30)
        self.opening_2_height = 0
        self.opening_3_height = fd.inches(10)
        self.opening_4_height = fd.inches(20)
        
class INSERT_2_Drawers_2_Doors(LM_splitters.Vertical_Splitters):
     
    def __init__(self):
        self.library_name = LIBRARY_NAME
        self.category_name = DOOR_DRAWER_CATEGORY_NAME
        self.assembly_name = "2 Drawers 2 Doors"
        self.width = fd.inches(18)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
        self.vertical_openings = 2
        self.exterior_1 = LM_exteriors.INSERT_Tall_Double_Door()
        self.exterior_1.prompts = {'Half Overlay Top':True, 
                                   'Half Overlay Bottom':True,
                                   'Half Overlay Left':True,
                                   'Half Overlay Right':True}
        self.exterior_2 = LM_exteriors.INSERT_2_Drawer_Stack()
        self.exterior_2.prompts = {'Half Overlay Top':True, 
                                   'Half Overlay Bottom':True,
                                   'Half Overlay Left':True,
                                   'Half Overlay Right':True}
        self.opening_2_height = fd.inches(14)
        
class INSERT_3_Drawers_2_Doors(LM_splitters.Vertical_Splitters):
     
    def __init__(self):
        self.library_name = LIBRARY_NAME
        self.category_name = DOOR_DRAWER_CATEGORY_NAME
        self.assembly_name = "3 Drawers 2 Doors"
        self.width = fd.inches(18)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
        self.vertical_openings = 2
        self.exterior_1 = LM_exteriors.INSERT_Tall_Double_Door()
        self.exterior_1.prompts = {'Half Overlay Top':True, 'Half Overlay Bottom':True,'Half Overlay Left':True,'Half Overlay Right':True}
        self.exterior_2 = LM_exteriors.INSERT_3_Drawer_Stack()
        self.exterior_2.prompts = {'Half Overlay Top':True, 'Half Overlay Bottom':True,'Half Overlay Left':True,'Half Overlay Right':True}
        self.opening_2_height = fd.inches(18)
        
class INSERT_4_Drawers_2_Doors(LM_splitters.Vertical_Splitters):
     
    def __init__(self):
        self.library_name = LIBRARY_NAME
        self.category_name = DOOR_DRAWER_CATEGORY_NAME
        self.assembly_name = "4 Drawers 2 Doors"
        self.width = fd.inches(18)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
        self.vertical_openings = 2
        self.exterior_1 = LM_exteriors.INSERT_Tall_Double_Door()
        self.exterior_1.prompts = {'Half Overlay Top':True, 'Half Overlay Bottom':True,'Half Overlay Left':True,'Half Overlay Right':True}
        self.exterior_2 = LM_exteriors.INSERT_4_Drawer_Stack()
        self.exterior_2.prompts = {'Half Overlay Top':True, 'Half Overlay Bottom':True,'Half Overlay Left':True,'Half Overlay Right':True}
        self.opening_2_height = fd.inches(24)
        
#---------INSERT Hanging Rod Configurations
        
class INSERT_Single_Hanging_Rod(LM_splitters.Vertical_Splitters):
     
    def __init__(self):
        self.library_name = LIBRARY_NAME
        self.category_name = HANGING_ROD_AND_SHELVES
        self.assembly_name = "Single Hanging Rod"
        self.width = fd.inches(18)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
        self.vertical_openings = 2
        self.remove_splitter_1 = True
        self.exterior_1 = None
        self.exterior_2 = None
        self.interior_1 = LM_interiors.INSERT_Hanging_Rod()
        self.interior_2 = None
        self.opening_1_height = fd.inches(10)
        self.opening_2_height = 0
        
class INSERT_Hanging_Rod_Open_Top(LM_splitters.Vertical_Splitters):
     
    def __init__(self):
        self.library_name = LIBRARY_NAME
        self.category_name = HANGING_ROD_AND_SHELVES
        self.assembly_name = "Hanging Rod Open Top"
        self.width = fd.inches(18)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
        self.vertical_openings = 2
        self.exterior_1 = None
        self.exterior_2 = None
        self.interior_1 = None
        self.interior_2 = LM_interiors.INSERT_Hanging_Rod()
        self.opening_1_height = fd.inches(10)
        self.opening_2_height = 0
        
class INSERT_Double_Hanging_Rod_Open_Top(LM_splitters.Vertical_Splitters):
     
    def __init__(self):
        self.library_name = LIBRARY_NAME
        self.category_name = HANGING_ROD_AND_SHELVES
        self.assembly_name = "Double Hanging Rod Open Top"
        self.width = fd.inches(18)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
        self.vertical_openings = 2
        self.exterior_1 = None
        self.exterior_2 = None
        self.interior_1 = None
        self.interior_2 = LM_interiors.INSERT_Double_Hanging_Rod()
        self.opening_1_height = fd.inches(10)
        self.opening_2_height = 0
        
class INSERT_Baskets_Hanging_Rod_Open_Top(LM_splitters.Vertical_Splitters):
     
    def __init__(self):
        self.library_name = LIBRARY_NAME
        self.category_name = HANGING_ROD_AND_SHELVES
        self.assembly_name = "Baskets Hanging Rod Open Top"
        self.width = fd.inches(18)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
        self.vertical_openings = 3
        self.remove_splitter_2 = True
        self.exterior_1 = None
        self.exterior_2 = None
        self.interior_1 = None
        self.interior_2 = LM_interiors.INSERT_Hanging_Rod()
        self.interior_3 = LM_interiors.INSERT_Wire_Baskets()
        self.opening_1_height = fd.inches(10)
        self.opening_2_height = 0
        
class INSERT_Rollouts_Hanging_Rod_Open_Top(LM_splitters.Vertical_Splitters):
     
    def __init__(self):
        self.library_name = LIBRARY_NAME
        self.category_name = HANGING_ROD_AND_SHELVES
        self.assembly_name = "Baskets Hanging Rod Open Top"
        self.width = fd.inches(18)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
        self.vertical_openings = 3
        self.remove_splitter_2 = True
        self.exterior_1 = None
        self.exterior_2 = None
        self.interior_1 = None
        self.interior_2 = LM_interiors.INSERT_Hanging_Rod()
        self.interior_3 = LM_interiors.INSERT_Rollouts()
        self.opening_1_height = fd.inches(20)
        self.opening_2_height = 0
        
class INSERT_Shoe_Shelves_Hanging_Rod_Open_Top(LM_splitters.Vertical_Splitters):
     
    def __init__(self):
        self.library_name = LIBRARY_NAME
        self.category_name = HANGING_ROD_AND_SHELVES
        self.assembly_name = "Shoe Shelves Hanging Rod Open Top"
        self.width = fd.inches(18)
        self.height = fd.inches(84)
        self.depth = fd.inches(23)
        self.vertical_openings = 3
        self.remove_splitter_2 = True
        self.exterior_1 = None
        self.exterior_2 = None
        self.interior_1 = None
        self.interior_2 = LM_interiors.INSERT_Hanging_Rod()
        self.interior_3 = LM_interiors.INSERT_Slanted_Shoe_Shelves()
        self.interior_3.shelf_qty = 3
        self.opening_1_height = fd.inches(10)
        self.opening_2_height = 0
        