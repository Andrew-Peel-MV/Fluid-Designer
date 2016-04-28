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

class PANEL_Library_Modules(Panel):
    bl_space_type = "TEXT_EDITOR"
    bl_region_type = "UI"
    bl_label = "Library Modules"

    attribs_to_hide = ['open_name','parts','prompts','group','g','sg','category_name','library_name']

    def draw(self, context):
        layout = self.layout
        space = context.space_data
        layout.menu('MENU_Library_Modules',text="Open Library Module",icon='LATTICE_DATA')
#         if space.text:
#             layout.operator('cabinetlib.create_product_class')
#         col = layout.column(align=True)
#         box = col.box()
#         
#         wm = context.window_manager.cabinetlib
# #         wm.cabinetlib.draw_library_items(layout,'INSERT')
#         
#         box.operator('cabinetlib.load_items_from_inserts')
#         
#         col.template_list("LIST_lib_insertlist_text", " ", wm.lib_insert, "items", wm.lib_insert, "index")
#         if wm.lib_insert.index < len(wm.lib_insert.items) - 1:
#             item = wm.lib_insert.items[wm.lib_insert.index]
#             box = col.box()
#             box.label("Class Name: " + item.class_name)
#             col = box.column(align=True)
#             col.label("Available Attributes:")
#             for attrib in eval("inserts." + item.class_name + "().attributes"):
#                 col.label(attrib,icon='DOT')
#             for name, obj in inspect.getmembers(eval("inserts." + item.class_name)):
#                 if "__" not in name and not callable(obj) and name not in self.attribs_to_hide:
#                     col.label(name,icon='DOT')

class MENU_Library_Modules(Menu):
    bl_label = "Library Modules"

    def draw(self, context):
        layout = self.layout
        dir, filename = os.path.split(__file__)
        script_library_path = fd.get_library_scripts_dir()
        files = os.listdir(script_library_path)
#         layout.label('Product Libraries',icon='LATTICE_DATA')
        col = layout.column(align=True)
        for file in files:
            filename, ext = os.path.splitext(file)
            if ext == '.py':
                col.operator('text.open',text=filename.replace("_"," "),icon='LATTICE_DATA').filepath = os.path.join(script_library_path,file)
        

classes = [
           PANEL_Library_Modules,
           MENU_Library_Modules
           ]

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

if __name__ == "__main__":
    register()
