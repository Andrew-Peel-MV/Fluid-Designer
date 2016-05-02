import bpy
import math

from bpy.types import Header, Menu, Operator, UIList, PropertyGroup

from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       BoolVectorProperty,
                       PointerProperty,
                       EnumProperty,
                       CollectionProperty)

import os
import fd
import inspect

class OPS_load_library_module(Operator):
    bl_idname = "fd_scripting_tools.load_library_module"
    bl_label = "Load Library Module"
    bl_description = "This will load a library module" 
    
    filepath = StringProperty(name="Library Module Filepath")
    
    def execute(self,context):
        text_space = None
        for area in  bpy.data.screens['Default'].areas:
            if area.type == 'TEXT_EDITOR':
                for space in area.spaces:
                    if space.type == 'TEXT_EDITOR':
                        text_space = space
                        space.show_syntax_highlight = True
                        space.show_line_numbers = True
                        
        path, module_name = os.path.split(self.filepath)

        if module_name in bpy.data.texts and text_space:
            text_space.text = bpy.data.texts[module_name]
        else:
            bpy.ops.text.open(filepath=self.filepath)

        bpy.ops.fd_scripting_tools.read_active_module()
        bpy.ops.fd_scripting_tools.start_modal_operator()            
        return {'FINISHED'}

class OPS_save_and_load_library_module(Operator):
    bl_idname = "fd_scripting_tools.save_and_load_library_module"
    bl_label = "Save and Reload Library Module"
    bl_description = "This will save and reload the current library module"
    
    library_module_name = StringProperty(name="Library Module Name")
    
    @classmethod
    def poll(self,context):
        if bpy.context.edit_text != None:
            return True
        else:
            return False    
    
    def invoke(self,context,event):
        systemPreferences = bpy.context.user_preferences.system
        retinaFactor = getattr(systemPreferences, "pixel_size", 1)        
        dpiFactor = systemPreferences.dpi * retinaFactor / 72
        return context.window_manager.invoke_props_dialog(self, 400 * dpiFactor, 200 * dpiFactor)        
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self, "library_module_name", text = "Library Module Name")    
    
    def execute(self,context):
        library_module_path = fd.get_library_scripts_dir()
        
        for file in os.listdir(path=library_module_path):
            if self.library_module_name.replace(" ","_") in file:
                self.report({'ERROR_INVALID_INPUT'},
                            "Library Name: " + "\"" + self.library_module_name + "\"" + " Already Exists! \n Please Use a Different Name")
                return {'FINISHED'}
                
        module_name = "LM_" + self.library_module_name.replace(" ","_") + ".py"
        save_path = os.path.join(library_module_path, module_name)
        bpy.ops.text.save_as(filepath=save_path)
        bpy.ops.text.open(filepath=save_path)
        
        return{'FINISHED'}
                    
class OPS_read_active_module(Operator):
    bl_idname = "fd_scripting_tools.read_active_module"
    bl_label = "Read Active Module"
    bl_description = "This will read the active python module"
    
    @classmethod
    def poll(self,context):
        if bpy.context.edit_text != None:
            return True
        else:
            return False
        
    def get_module_members(self,libraries,library_name,module_name):
        if library_name in libraries:
            lib = libraries[library_name]
        else:
            lib = libraries.add()
            lib.name = library_name
            lib.module_name = module_name
        return lib        
        
    def execute(self,context):
        from importlib import import_module, reload
        import sys
        wm = context.window_manager.cabinetlib
        for member in wm.module_members:
            wm.module_members.remove(0)
        
        active_module = bpy.context.edit_text.name.replace(".py","")
        
        mod = import_module(active_module)
        del sys.modules[active_module]
#         mod1 = import_module(active_module)
        mod = reload(mod)
        for name, obj in inspect.getmembers(mod):

            if inspect.isclass(obj) and "PRODUCT_" in name:
                mod_member = wm.module_members.add()
                mod_member.name = name
                
            elif inspect.isclass(obj) and "INSERT_" in name:    
                mod_member = wm.module_members.add()
                mod_member.name = name            
                
            elif "PROPERTIES" in name:    
                mod_member = wm.module_members.add()
                mod_member.name = name                                       
                
            elif "PROMPTS" in name:    
                mod_member = wm.module_members.add()
                mod_member.name = name     
                
            elif "Material_Pointers" in name:    
                mod_member = wm.module_members.add()
                mod_member.name = name 
                
            elif "Cutpart_Pointers" in name:    
                mod_member = wm.module_members.add()
                mod_member.name = name 
                
            elif "Edgepart_Pointers" in name:    
                mod_member = wm.module_members.add()
                mod_member.name = name                      
                
            elif "OPERATOR" in name:
                mod_member = wm.module_members.add()
                mod_member.name = name                                     
                
            elif inspect.isclass(obj) and "LM_" in obj.__module__:
                mod_member = wm.module_members.add()
                mod_member.name = name   
#                 product = obj()
#                 item = lib.items.add()
#                 item.name = product.assembly_name
#                 item.class_name = name
#                 item.library_name = product.library_name
#                 item.category_name = product.category_name
#                 library_path = fd.get_library_dir("products")
#                 thumbnail_path = os.path.join(library_path,item.library_name,item.category_name,item.name.strip() + ".png")
#                 if os.path.exists(thumbnail_path):
#                     item.has_thumbnail = True
#                 else:
#                     item.has_thumbnail = False
#                 file_path = os.path.join(library_path,item.library_name,item.category_name,item.name.strip() + ".blend")
#                 if os.path.exists(file_path):
#                     item.has_file = True
#                 else:
#                     item.has_file = False        

        return {'FINISHED'} 
    
classes = [
           OPS_load_library_module,
           OPS_save_and_load_library_module,
           OPS_read_active_module
           ]    

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

if __name__ == "__main__":
    register()