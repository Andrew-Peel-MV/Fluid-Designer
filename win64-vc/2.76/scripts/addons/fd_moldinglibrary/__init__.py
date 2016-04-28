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

bl_info = {
    "name": "Molding Library Management",
    "author": "Andrew Peel",
    "version": (1, 0, 0),
    "blender": (2, 7, 0),
    "location": "Tools Shelf",
    "description": "This add-on creates a UI to work with the Products and Inserts Library",
    "warning": "",
    "wiki_url": "",
    "category": "Fluid Designer"
}

import bpy

class PANEL_Moldings(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "objectmode"
    bl_label = "Molding Library Management"
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Fluid Designer"
    
    def draw_header(self, context):
        layout = self.layout
        layout.label('',icon='OUTLINER_OB_CURVE')
    
    def draw(self, context):
        layout = self.layout
        g = context.scene.lm_moldings
        g.draw(layout)

def register():
    bpy.utils.register_class(PANEL_Moldings)

def unregister():
    bpy.utils.unregister_class(PANEL_Moldings)

if __name__ == "__main__":
    register()
