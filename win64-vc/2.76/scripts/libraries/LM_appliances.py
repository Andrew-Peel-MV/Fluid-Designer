"""
Microvellum 
Appliances 
Stores all of the Logic, Product, and Insert Class definitions for appliances
"""

import fd

HIDDEN_FOLDER_NAME = "_HIDDEN"
APPLIANCE_LIBRARY_NAME = "Appliances Assemblies"

class Parametric_Wall_Appliance(fd.Library_Assembly):
    
    library_name = "Appliances"
    placement_type = "Standard"
    type_assembly = "PRODUCT"
    
    # Name of the category to retrieve the appliance from
    appliance_category = ""
    
    # Name of the appliance in the assembly library
    appliance_name = ""
    
    def draw(self):
        self.create_assembly()
        
        Width = self.get_var("dim_x","Width")
        Height = self.get_var("dim_z","Height")
        Depth = self.get_var("dim_y","Depth")
        
        assembly = self.add_assembly((HIDDEN_FOLDER_NAME,APPLIANCE_LIBRARY_NAME,self.appliance_category,self.appliance_name))
        assembly.x_dim('Width',[Width])
        assembly.y_dim('Depth',[Depth])
        assembly.z_dim('Height',[Height])
        
        self.update()

class Wall_Appliance(fd.Library_Assembly):
    
    library_name = "Appliances"
    placement_type = "Standard"
    type_assembly = "PRODUCT"
    
    # Name of the category to retrieve the appliance from
    appliance_category = ""
    
    # Name of the appliance in the assembly library
    appliance_name = ""
    
    def draw(self):
        self.create_assembly()
        self.add_assembly((HIDDEN_FOLDER_NAME,APPLIANCE_LIBRARY_NAME,self.appliance_category,self.appliance_name))
        self.update()
        
class Built_In_Appliance(fd.Library_Assembly):
    
    library_name = "Cabinet Appliances"
    placement_type = "EXTERIOR"
    type_assembly = "INSERT"
    
    # Name of the category to retrieve the appliance from
    appliance_category = ""
    
    # Name of the appliance in the assembly library
    appliance_name = ""
    
    # Size of the built in appliance so it can center in the opening
    appliance_width = 0
    appliance_height = 0
    
    def draw(self):
        self.create_assembly()
        
        Width = self.get_var("dim_x","Width")
        Height = self.get_var("dim_z","Height")
        
        appliance = self.add_assembly((HIDDEN_FOLDER_NAME,APPLIANCE_LIBRARY_NAME,self.appliance_category,self.appliance_name))
        appliance.x_loc('(Width/2)-(' + str(self.width) + '/2)',[Width])
        appliance.z_loc('(Height/2)-(' + str(self.height) + '/2)',[Height])
        
        self.update()
        
class Countertop_Appliance(fd.Library_Assembly):
    
    library_name = "Cabinet Appliances"
    placement_type = "SPLITTER"
    type_assembly = "INSERT"
    
    # Name of the category to retrieve the appliance from
    appliance_category = ""
    
    # Name of the appliance in the assembly library
    appliance_name = ""
    
    # Size of the built in appliance so it can center in the opening
    appliance_width = 0
    appliance_height = 0
    
    mirror_y = True
    
    def draw(self):
        self.create_assembly()
        
        Width = self.get_var("dim_x","Width")

        appliance = self.add_assembly((HIDDEN_FOLDER_NAME,APPLIANCE_LIBRARY_NAME,self.appliance_category,self.appliance_name))
        appliance.x_loc('(Width/2)-(' + str(self.width) + '/2)',[Width])
        appliance.y_loc(value=fd.inches(-2))
        appliance.z_loc(value = 0)
        
        self.update()
        
#---------PRODUCT: PARAMETRIC APPLIANCES
        
class PRODUCT_Refrigerator(Parametric_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Appliances - Parametric"
        self.assembly_name = "Refrigerator"
        self.width = fd.inches(36)
        self.height = fd.inches(84)
        self.depth = fd.inches(27)
        self.appliance_category = "Parametric Appliances"
        self.appliance_name = "Professional Refrigerator Generic"
        
class PRODUCT_Range(Parametric_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Appliances - Parametric"
        self.assembly_name = "Range"
        self.width = fd.inches(30)
        self.height = fd.inches(42)
        self.depth = fd.inches(28)
        self.appliance_category = "Parametric Appliances"
        self.appliance_name = "Professional Gas Range Generic"
        
class PRODUCT_Dishwasher(Parametric_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Appliances - Parametric"
        self.assembly_name = "Dishwasher"
        self.width = fd.inches(24)
        self.height = fd.inches(33.75)
        self.depth = fd.inches(27)
        self.appliance_category = "Parametric Appliances"
        self.appliance_name = "Professional Dishwasher Generic"
        
class PRODUCT_Range_Hood(Parametric_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Appliances - Parametric"
        self.assembly_name = "Range Hood"
        self.width = fd.inches(30)
        self.height = fd.inches(14)
        self.depth = fd.inches(12.5)
        self.appliance_category = "Range Hoods"
        self.appliance_name = "Wall Mounted Range Hood 01"
        self.height_above_floor = fd.inches(60)
        
#---------PRODUCT: REFRIGERATORS
        
class PRODUCT_Professional_Refrigerator_30_Inch(Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Refrigerator"
        self.assembly_name = "Professional Refrigerator 30 Inch"
        self.width = fd.inches(30)
        self.height = fd.inches(84)
        self.depth = fd.inches(27)
        self.appliance_category = "Refrigerators"
        self.appliance_name = "Professional Refrigerator 30 inch"
        
class PRODUCT_Professional_Refrigerator_36_Inch(Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Refrigerator"
        self.assembly_name = "Professional Refrigerator 36 Inch"
        self.width = fd.inches(36)
        self.height = fd.inches(84)
        self.depth = fd.inches(27)
        self.appliance_category = "Refrigerators"
        self.appliance_name = "Professional Refrigerator 36 inch"
        
class PRODUCT_Double_Door_Refrigerator_Freezer_Bottom(Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Refrigerator"
        self.assembly_name = "Double Door Refrigerator Freezer Bottom"
        self.width = fd.inches(36)
        self.height = fd.inches(68.5)
        self.depth = fd.inches(31.75)
        self.appliance_category = "Refrigerators"
        self.appliance_name = "Double Door Refrigerator Freezer Bottom"
        
class PRODUCT_Refrigerator_Freezer_Combo_36_Inch(Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Refrigerator"
        self.assembly_name = "Refrigerator Freezer Combo 36 Inch"
        self.width = fd.inches(36)
        self.height = fd.inches(84)
        self.depth = fd.inches(27)
        self.appliance_category = "Refrigerators"
        self.appliance_name = "Refrigerator-Freezer Combo 36 inch"
        
class PRODUCT_Side_by_Side_Refrigerator_42_Inch(Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Refrigerator"
        self.assembly_name = "Side-by-Side Refrigerator 42 Inch"
        self.width = fd.inches(42)
        self.height = fd.inches(84)
        self.depth = fd.inches(27)
        self.appliance_category = "Refrigerators"
        self.appliance_name = "Side-by-Side Refrigerator 42 inch"

class PRODUCT_Side_by_Side_Refrigerator_48_Inch(Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Refrigerator"
        self.assembly_name = "Side-by-Side Refrigerator 48 Inch"
        self.width = fd.inches(48)
        self.height = fd.inches(84)
        self.depth = fd.inches(27)
        self.appliance_category = "Refrigerators"
        self.appliance_name = "Side-by-Side Refrigerator 48 inch"

#---------PRODUCT: DISH WASHERS

class PRODUCT_Professional_Dishwasher(Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Dishwashers"
        self.assembly_name = "Professional Dishwasher"
        self.width = fd.inches(24)
        self.height = fd.inches(33.37)
        self.depth = fd.inches(27)
        self.appliance_category = "Dishwasher"
        self.appliance_name = "Professional Dishwasher"
        
#---------PRODUCT: RANGE HOODS
        
class PRODUCT_Island_Range_Hood(Parametric_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Range Hoods"
        self.assembly_name = "Island Range Hood"
        self.width = fd.inches(30)
        self.height = fd.inches(30)
        self.depth = fd.inches(30)
        self.appliance_category = "Range Hoods"
        self.appliance_name = "Island Range Hood"
        self.height_above_floor = fd.inches(60)
        
class PRODUCT_Stanisci_D_Series_Hood(Parametric_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Range Hoods"
        self.assembly_name = "Stanisci D Series Hood"
        self.width = fd.inches(50)
        self.height = fd.inches(48)
        self.depth = fd.inches(22.75)
        self.appliance_category = "Range Hoods"
        self.appliance_name = "Stanisci D Series Hood"
        self.height_above_floor = fd.inches(60)
        
class PRODUCT_Stanisci_E_Series_Hood(Parametric_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Range Hoods"
        self.assembly_name = "Stanisci E Series Hood"
        self.width = fd.inches(50)
        self.height = fd.inches(42)
        self.depth = fd.inches(22.75)
        self.appliance_category = "Range Hoods"
        self.appliance_name = "Stanisci E Series Hood"
        self.height_above_floor = fd.inches(60)
        
class PRODUCT_Stanisci_G_Series_Hood(Parametric_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Range Hoods"
        self.assembly_name = "Stanisci G Series Hood"
        self.width = fd.inches(50)
        self.height = fd.inches(30)
        self.depth = fd.inches(22.75)
        self.appliance_category = "Range Hoods"
        self.appliance_name = "Stanisci G Series Hood"
        self.height_above_floor = fd.inches(60)
        
class PRODUCT_Stanisci_T_Series_Hood(Parametric_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Range Hoods"
        self.assembly_name = "Stanisci T Series Hood"
        self.width = fd.inches(50)
        self.height = fd.inches(44)
        self.depth = fd.inches(22.75)
        self.appliance_category = "Range Hoods"
        self.appliance_name = "Stanisci T Series Hood"
        self.height_above_floor = fd.inches(60)
        
class PRODUCT_Wall_Mounted_Range_Hood_01(Parametric_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Range Hoods"
        self.assembly_name = "Wall Mounted Range Hood 01"
        self.width = fd.inches(30)
        self.height = fd.inches(14)
        self.depth = fd.inches(12)
        self.appliance_category = "Range Hoods"
        self.appliance_name = "Wall Mounted Range Hood 01"
        self.height_above_floor = fd.inches(60)
        
class PRODUCT_Wall_Mounted_Range_Hood_02(Parametric_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Range Hoods"
        self.assembly_name = "Wall Mounted Range Hood 02"
        self.width = fd.inches(30)
        self.height = fd.inches(14)
        self.depth = fd.inches(21)
        self.appliance_category = "Range Hoods"
        self.appliance_name = "Wall Mounted Range Hood 02"
        self.height_above_floor = fd.inches(60)
        
#---------PRODUCT: RANGES

class PRODUCT_Gas_Range_30_Inch(Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Ranges"
        self.assembly_name = "Gas Range 30 Inch"
        self.width = fd.inches(30)
        self.height = fd.inches(42)
        self.depth = fd.inches(28)
        self.appliance_category = "Ranges"
        self.appliance_name = "Gas Range 30 inch"

class PRODUCT_Gas_Range_36_Inch(Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Ranges"
        self.assembly_name = "Gas Range 36 Inch"
        self.width = fd.inches(36)
        self.height = fd.inches(42)
        self.depth = fd.inches(28)
        self.appliance_category = "Ranges"
        self.appliance_name = "Gas Range 36 inch"

class PRODUCT_Gas_Range_48_Inch(Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Ranges"
        self.assembly_name = "Gas Range 48 Inch"
        self.width = fd.inches(48)
        self.height = fd.inches(42)
        self.depth = fd.inches(28)
        self.appliance_category = "Ranges"
        self.appliance_name = "Gas Range 48 inch"

class PRODUCT_Gas_Range_60_Inch(Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Ranges"
        self.assembly_name = "Gas Range 60 Inch"
        self.width = fd.inches(60)
        self.height = fd.inches(42)
        self.depth = fd.inches(28)
        self.appliance_category = "Ranges"
        self.appliance_name = "Gas Range 60 inch"

class PRODUCT_Wolf_Gas_Range_GR304(Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Ranges"
        self.assembly_name = "Wolf Gas Range GR304"
        self.width = fd.inches(30)
        self.height = fd.inches(42)
        self.depth = fd.inches(28)
        self.appliance_category = "Ranges"
        self.appliance_name = "Wolf Gas Range GR304"

class PRODUCT_Wolf_Gas_Range_GR366(Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Ranges"
        self.assembly_name = "Wolf Gas Range GR 366"
        self.width = fd.inches(36)
        self.height = fd.inches(42)
        self.depth = fd.inches(28)
        self.appliance_category = "Ranges"
        self.appliance_name = "Wolf Gas Range GR366"

class PRODUCT_Wolf_Gas_Range_GR488(Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Ranges"
        self.assembly_name = "Wolf Gas Range GR488"
        self.width = fd.inches(48)
        self.height = fd.inches(42)
        self.depth = fd.inches(28)
        self.appliance_category = "Ranges"
        self.appliance_name = "Wolf Gas Range GR488"

class PRODUCT_Wolf_Gas_Range_GR606(Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Ranges"
        self.assembly_name = "Wolf Gas Range GR606"
        self.width = fd.inches(60)
        self.height = fd.inches(42)
        self.depth = fd.inches(28)
        self.appliance_category = "Ranges"
        self.appliance_name = "Wolf Gas Range GR606"

#---------INSERT: Built-in Ovens

class INSERT_Viking_RVDOE_3_Series_Double_Oven(Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Ovens"
        self.assembly_name = "Viking RVDOE 3 Series Double Oven"
        self.width = fd.inches(29.75)
        self.height = fd.inches(51.375)
        self.depth = fd.inches(0)
        self.appliance_category = "Built-in Ovens"
        self.appliance_name = "Viking RVDOE 3 Series Double Oven"
        
class INSERT_Viking_RVSOE_3_Series_Single_Oven(Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Ovens"
        self.assembly_name = "Viking RVSOE 3 Series Single Oven"
        self.width = fd.inches(29.75)
        self.height = fd.inches(29.375)
        self.depth = fd.inches(0)
        self.appliance_category = "Built-in Ovens"
        self.appliance_name = "Viking RVSOE 3 Series Single Oven"
        
class INSERT_Viking_VEDO_5_Series_Double_Oven(Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Ovens"
        self.assembly_name = "Viking VEDO 5 Series Double Oven"
        self.width = fd.inches(29.5)
        self.height = fd.inches(51.875)
        self.depth = fd.inches(0)
        self.appliance_category = "Built-in Ovens"
        self.appliance_name = "Viking VEDO 5 Series Double Oven"

class INSERT_Viking_VESO_5_Series_Single_Oven(Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Ovens"
        self.assembly_name = "Viking VESO 5 Series Single Oven"
        self.width = fd.inches(29.875)
        self.height = fd.inches(29.5)
        self.depth = fd.inches(0)
        self.appliance_category = "Built-in Ovens"
        self.appliance_name = "Viking VESO 5 Series Single Oven"

class INSERT_Wolf_DO30PM_Professional_Built_in_Oven(Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Ovens"
        self.assembly_name = "Wolf DO30PM Professional Built-in Oven"
        self.width = fd.inches(29.875)
        self.height = fd.inches(50.875)
        self.depth = fd.inches(0)
        self.appliance_category = "Built-in Ovens"
        self.appliance_name = "Wolf DO30PM Professional Built-in Oven"

class INSERT_Wolf_DO30TM_Transitional_Built_in_Oven(Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Ovens"
        self.assembly_name = "Wolf DO30TM Transitional Built-in Oven"
        self.width = fd.inches(29.875)
        self.height = fd.inches(50.875)
        self.depth = fd.inches(0)
        self.appliance_category = "Built-in Ovens"
        self.appliance_name = "Wolf DO30TM Transitional Built-in Oven"

class INSERT_Wolf_SO30PM_Professional_Built_in_Oven(Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Ovens"
        self.assembly_name = "Wolf SO30PM Professional Built-in Oven"
        self.width = fd.inches(29.5)
        self.height = fd.inches(51.875)
        self.depth = fd.inches(0)
        self.appliance_category = "Built-in Ovens"
        self.appliance_name = "Wolf SO30PM Professional Built-in Oven"

class INSERT_Wolf_SO30TM_Transitional_Built_in_Oven(Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Ovens"
        self.assembly_name = "Wolf SO30TM Transitional Built-in Oven"
        self.width = fd.inches(29.875)
        self.height = fd.inches(28.5)
        self.depth = fd.inches(0)
        self.appliance_category = "Built-in Ovens"
        self.appliance_name = "Wolf SO30TM Transitional Built-in Oven"

#---------INSERT: Built-in Microwave

class INSERT_Wolf_MD30PE_Professional_Drawer_Microwave(Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Microwaves"
        self.assembly_name = "Wolf MD30PE Professional Drawer Microwave"
        self.width = fd.inches(29.875)
        self.height = fd.inches(15.125)
        self.depth = fd.inches(0)
        self.appliance_category = "Built-in Microwaves"
        self.appliance_name = "Wolf MD30PE Professional Drawer Microwave"

class INSERT_Wolf_MD30TE_Transitional_Drawer_Microwave(Built_In_Appliance):
    
    def __init__(self):
        self.category_name = "Built-in Microwaves"
        self.assembly_name = "Wolf MD30PE Transitional Drawer Microwave"
        self.width = fd.inches(29.875)
        self.height = fd.inches(15.125)
        self.depth = fd.inches(0)
        self.appliance_category = "Built-in Microwaves"
        self.appliance_name = "Wolf MD30TE Transitional Drawer Microwave"

#---------INSERT: Sinks

class INSERT_Double_Basin_Sink(Countertop_Appliance):
    
    def __init__(self):
        self.category_name = "Sinks"
        self.assembly_name = "Double Basin Sink"
        self.width = fd.inches(33)
        self.height = fd.inches(0)
        self.depth = fd.inches(17.248)
        self.appliance_category = "Sinks"
        self.appliance_name = "Double Basin Sink"

class INSERT_Single_Basin_Sink(Countertop_Appliance):
    
    def __init__(self):
        self.category_name = "Sinks"
        self.assembly_name = "Single Basin Sink"
        self.width = fd.inches(17.25)
        self.height = fd.inches(0)
        self.depth = fd.inches(17.25)
        self.appliance_category = "Sinks"
        self.appliance_name = "Single Basin Sink"

class INSERT_Bathroom_Sink(Countertop_Appliance):
    
    def __init__(self):
        self.category_name = "Sinks"
        self.assembly_name = "Bathroom Sink"
        self.width = fd.inches(20)
        self.height = fd.inches(0)
        self.depth = fd.inches(17)
        self.appliance_category = "Sinks"
        self.appliance_name = "Bathroom Sink"
        
#---------INSERT: Gas Cooktop

class INSERT_Wolf_CG152_Transitional_Gas_Cooktop(Countertop_Appliance):
    
    def __init__(self):
        self.category_name = "Cooktop"
        self.assembly_name = "Wolf CG152 Transitional Gas Cooktop"
        self.width = fd.inches(15)
        self.height = fd.inches(5)
        self.depth = fd.inches(21)
        self.appliance_category = "Gas Cooktops"
        self.appliance_name = "Wolf CG152 Transitional Gas Cooktop"
        
class INSERT_Wolf_CG304_Professional_Gas_Cooktop(Countertop_Appliance):
    
    def __init__(self):
        self.category_name = "Cooktop"
        self.assembly_name = "Wolf CG304 Professional Gas Cooktop"
        self.width = fd.inches(30)
        self.height = fd.inches(5)
        self.depth = fd.inches(21)
        self.appliance_category = "Gas Cooktops"
        self.appliance_name = "Wolf CG304 Professional Gas Cooktop"
        
class INSERT_Wolf_CG304_Transitional_Gas_Cooktop(Countertop_Appliance):
    
    def __init__(self):
        self.category_name = "Cooktop"
        self.assembly_name = "Wolf CG304 Transitional Gas Cooktop"
        self.width = fd.inches(30)
        self.height = fd.inches(5)
        self.depth = fd.inches(21)
        self.appliance_category = "Gas Cooktops"
        self.appliance_name = "Wolf CG304 Transitional Gas Cooktop"
        
class INSERT_Wolf_CG365_Professional_Gas_Cooktop(Countertop_Appliance):
    
    def __init__(self):
        self.category_name = "Cooktop"
        self.assembly_name = "Wolf CG365 Professional Gas Cooktop"
        self.width = fd.inches(36)
        self.height = fd.inches(5)
        self.depth = fd.inches(21)
        self.appliance_category = "Gas Cooktops"
        self.appliance_name = "Wolf CG365 Professional Gas Cooktop"
        
class INSERT_Wolf_CG365_Transitional_Gas_Cooktop(Countertop_Appliance):
    
    def __init__(self):
        self.category_name = "Cooktop"
        self.assembly_name = "Wolf CG365 Transitional Gas Cooktop"
        self.width = fd.inches(36)
        self.height = fd.inches(5)
        self.depth = fd.inches(21)
        self.appliance_category = "Gas Cooktops"
        self.appliance_name = "Wolf CG365 Transitional Gas Cooktop"
        
def register():
    pass
    
def unregister():
    pass

    