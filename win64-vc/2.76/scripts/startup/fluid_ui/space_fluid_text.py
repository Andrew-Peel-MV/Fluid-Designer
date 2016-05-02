# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy
from bpy.types import Header, Menu, Panel
import os

import fd

class LIST_module_members(bpy.types.UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        if "PRODUCT_" in item.name:
            layout.label(item.name, icon='OUTLINER_OB_LATTICE')
        elif "INSERT_" in item.name:    
            layout.label(item.name, icon='STICKY_UVS_LOC')
        elif "PROPERTIES" in item.name:  
            layout.label(item.name, icon='SCENE_DATA') 
        elif "OPERATOR" in item.name:  
            layout.label(item.name, icon='MODIFIER')
        elif "PROMPTS" in item.name:  
            layout.label(item.name, icon='SETTINGS')
        elif "Material_Pointers" in item.name:  
            layout.label(item.name, icon='MATERIAL')  
        elif "Cutpart_Pointers" in item.name:  
            layout.label(item.name, icon='MOD_UVPROJECT')
        elif "Edgepart_Pointers" in item.name:  
            layout.label(item.name, icon='EDGESEL')  
        else:
            layout.label(item.name, icon='SPACE3')
          
class PANEL_Library_Modules(Panel):
    bl_space_type = "TEXT_EDITOR"
    bl_region_type = "UI"
    bl_label = "Library Modules"

    attribs_to_hide = ['open_name','parts','prompts','group','g','sg','category_name','library_name']       

    def draw(self, context):
        wm = context.window_manager.cabinetlib
        st = context.space_data
        
        layout = self.layout
        box = layout.box()
        row = box.row(align=True)
        row.prop_enum(wm, "library_module_tabs", 'LIBRARY_DEVELOPMENT', icon='FILE_TEXT', text="Scripting")
        row.prop_enum(wm, "library_module_tabs", 'FIND', icon='VIEWZOOM', text="Find")
        #row.prop_enum(wm, "library_module_tabs", 'PROPERTIES', icon='COLLAPSEMENU', text="Properties")
        
        if wm.library_module_tabs == 'LIBRARY_DEVELOPMENT':
            space = context.space_data
            row = box.row(align=True)
            if space.text:
                row.menu('MENU_Library_Modules',text=space.text.name,icon='FILE_TEXT')
            else:
                row.menu('MENU_Library_Modules',text="Open Library Module",icon='FILE_TEXT')
            row.menu('MENU_Library_Module_options',text="",icon='DOWNARROW_HLT')
            
            if wm.module_members:
                box.template_list("LIST_module_members", 
                                     " ", 
                                     wm, 
                                     "module_members", 
                                     wm, 
                                     "module_members_index",
                                     rows=20)
                
            row = box.row()
            row.operator("text.run_script")
            
        if wm.library_module_tabs == 'FIND':            
            col = box.column(align=True)
            row = col.row(align=True)
            row.prop(st, "find_text", text="")
            row.operator("text.find_set_selected", text="", icon='TEXT')
            col.operator("text.find")
    
            col = box.column(align=True)
            row = col.row(align=True)
            row.prop(st, "replace_text", text="")
            row.operator("text.replace_set_selected", text="", icon='TEXT')
            col.operator("text.replace")
            
            box.prop(st, "use_match_case")       

class MENU_Library_Module_options(Menu):
    bl_label = "Library Module Options"
    
    def draw(self, context):
        layout = self.layout
        layout.operator("fd_scripting_tools.save_and_load_library_module",text="Save Library Module As...",icon="SAVE_AS")
        layout.operator("fd_scripting_tools.read_active_module",text="Read Active Library Module",icon='FILE_REFRESH')

class MENU_Library_Modules(Menu):
    bl_label = "Library Modules"

    def draw(self, context):
        layout = self.layout
        dir, filename = os.path.split(__file__)
        script_library_path = fd.get_library_scripts_dir()
        files = os.listdir(script_library_path)
        col = layout.column(align=True)
        for file in files:
            filename, ext = os.path.splitext(file)
            if ext == '.py':
                col.operator('fd_scripting_tools.load_library_module',text=filename.replace("_"," "),icon='FILE_TEXT').filepath = os.path.join(script_library_path,file)        

classes = [
           PANEL_Library_Modules,
           MENU_Library_Modules,
           MENU_Library_Module_options,
           LIST_module_members
           ]

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

if __name__ == "__main__":
    register()
