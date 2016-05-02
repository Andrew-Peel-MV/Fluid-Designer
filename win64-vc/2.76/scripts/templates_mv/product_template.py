# This is an example template for Library Assemblies
import bpy
import fd

# Add Library References below import as constants
PART = ("Cabinet Assemblies","Cut Parts","Part with Front Edgebanding")

class PRODUCT_New_Assembly(fd.Library_Assembly):
    library_name = "Library Name"
    category_name = ""
    assembly_name = ""
    property_id = ""
    type_assembly = "PRODUCT"
    mirror_z = False
    mirror_y = True
    width = 0
    height = 0
    depth = 0
    height_above_floor = 0
    
    def draw(self):
        # This creates the assembly structure. THIS MUST BE CALLED FIRST
        self.create_assembly()
        
        # This is how you add prompts. It is recommended to add a prompt tab they can be viewed on
        self.add_tab(name='Main Options',tab_type='VISIBLE')
        self.add_prompt(name="New Prompt",prompt_type='CHECKBOX',value=False,tab_index=0)
        
        # This is how to retrieve variables that can be used in python expressions
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        New_Prompt = self.get_var("New Prompt")
        
        # This is how to add assemblies from the library and set formulas
        assembly = self.add_assembly(PART)
        assembly.set_name("Left Part")
        assembly.x_loc(value = 0)
        assembly.y_loc(value = 0)
        assembly.z_loc(value = 0)
        assembly.x_rot(value = 0)
        assembly.y_rot(value = 0)
        assembly.z_rot(value = 0)
        assembly.x_dim('Width',[Width])
        assembly.y_dim('Depth',[Depth])
        assembly.z_dim('Height',[Height])

        # This updates several properties for the assembly. THIS MUST BE CALLED LAST
        self.update()
        
        