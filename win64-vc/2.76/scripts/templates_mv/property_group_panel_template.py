import bpy
import fd

from bpy.types import (Operator,
                       Panel,
                       PropertyGroup)

from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       BoolVectorProperty,
                       PointerProperty,
                       CollectionProperty,
                       EnumProperty)

class My_Property_Group(PropertyGroup):
    Main_Tabs = EnumProperty(name="Main Tabs",
                       items=[('OPTION1',"Option 1",'Shows Option 1'),
                              ('OPTION2',"Option 2",'Shows Option 2'),
                              ('OPTION3',"Option 3",'Shows Option 3')],
                       default = 'OPTION1')
        
    Float_Property = FloatProperty(name="Number Property", 
                                  description="This is how you create a number property", 
                                  default=1.0)
        
    Int_Property = IntProperty(name="Integer Property", 
                                description="This is how you create a whole number property", 
                                default=1)
        
    Check_Box_Property = BoolProperty(name="Check Box Property", 
                                      description="This is how you create a check box property", 
                                      default=False)
        
class PANEL_My_Panel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "objectmode"
    bl_label = "Panel Header Name"
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Library Data"

    def draw_header(self, context):
        layout = self.layout
        layout.label('',icon='LATTICE_DATA')
    
    def draw(self, context):
        layout = self.layout
        my_properties = context.scene.lm_namespace
        
        layout.prop(my_properties,"Main_Tabs")
        
        if self.Main_Tabs == 'OPTION1':
            layout.prop(my_properties,'Float_Property')
            
        if self.Main_Tabs == 'OPTION2':
            layout.prop(my_properties,'Int_Property')
            
        if self.Main_Tabs == 'OPTION3':
            layout.prop(my_properties,'Check_Box_Property')
        
def register():
    bpy.utils.register_class(My_Property_Group)
    bpy.utils.register_class(PANEL_My_Panel)
    
    # Add properties to the Scene or the WindowManager
    # WindowManager properties do not hold their value in the Blend File after reopening
    bpy.types.Scene.lm_namespace = PointerProperty(type = My_Property_Group)
    
def unregister():
    bpy.utils.unregister_class(My_Property_Group)
    bpy.utils.unregister_class(PANEL_My_Panel)
        