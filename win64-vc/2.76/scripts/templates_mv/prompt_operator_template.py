# This is an example template for Library Assemblies

import bpy
import fd

class PROMPTS_Prompts_Page(bpy.types.Operator):
    bl_idname = "promptui.prompts_page"
    bl_label = "Prompt Page Name" 
    
    object_name = bpy.props.StringProperty(name="Object Name")
    
    # Store the product as a class level property for convenience. This is not required
    product = None

    def check(self, context):
        # This gets called every time a user changes a property on the interface
        return True

    def execute(self, context):
        # This gets called when the OK button is clicked
        return {'FINISHED'}

    def invoke(self,context,event):
        # This gets called first and is used as an init call
        obj = context.scene.objects[self.object_name]
        obj_product_bp = fd.get_bp(obj,'PRODUCT')
        self.product = fd.Assembly(obj_product_bp)
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=fd.get_prop_dialog_width(480))
        
    def draw(self, context):
        # This draw the interface
        layout = self.layout
        layout.label("Add some text...")

        # Draw Product Size
        box = layout.box()
        box.prop(self.product.obj_x,'location',index=0,text="Width")
        box.prop(self.product.obj_y,'location',index=1,text="Depth")
        box.prop(self.product.obj_z,'location',index=2,text="Height")

        # You can get Prompts from the Product and Display them on the interface
        some_prompt = self.product.get_prompt("Some Prompt")
        box = layout.box()
        box.prop(some_prompt,"DistanceValue",text="Some Prompt")

        # Draw Product Location and Rotation
        box = layout.box()
        row = box.row()
        row.label('Location:')
        row.prop(self.product.obj_bp,'location',text="")
        row.label('Rotation:')
        row.prop(self.product.obj_bp,'rotation_euler',index=2,text="")
        
def register():
    bpy.utils.register_class(PROMPTS_Prompts_Page)
    
def unregister():
    bpy.utils.unregister_class(PROMPTS_Prompts_Page)
        