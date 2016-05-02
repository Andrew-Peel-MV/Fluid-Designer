import bpy
import fd

class PROPERTIES_My_Property_Group(bpy.types.PropertyGroup):
    Main_Tabs = bpy.props.EnumProperty(name="Main Tabs",
                                       items=[('OPTION1',"Option 1",'Shows Option 1'),
                                              ('OPTION2',"Option 2",'Shows Option 2'),
                                              ('OPTION3',"Option 3",'Shows Option 3')],
                                       default = 'OPTION1')
        
    Float_Property = bpy.props.FloatProperty(name="Number Property", 
                                             description="This is how you create a number property", 
                                             default=1.0)
        
    Int_Property = bpy.props.IntProperty(name="Integer Property", 
                                         description="This is how you create a whole number property", 
                                         default=1)
        
    Check_Box_Property = bpy.props.BoolProperty(name="Check Box Property", 
                                                description="This is how you create a check box property", 
                                                default=False)
        
class PANEL_My_Panel(bpy.types.Panel):
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
        
        if my_properties.Main_Tabs == 'OPTION1':
            layout.prop(my_properties,'Float_Property')
            
        if my_properties.Main_Tabs == 'OPTION2':
            layout.prop(my_properties,'Int_Property')
            
        if my_properties.Main_Tabs == 'OPTION3':
            layout.prop(my_properties,'Check_Box_Property')
        
def register():
    bpy.utils.register_class(PROPERTIES_My_Property_Group)
    bpy.utils.register_class(PANEL_My_Panel)
    
    bpy.types.Scene.lm_namespace = bpy.props.PointerProperty(type = PROPERTIES_My_Property_Group)
    
def unregister():
    bpy.utils.unregister_class(PROPERTIES_My_Property_Group)
    bpy.utils.unregister_class(PANEL_My_Panel)
        