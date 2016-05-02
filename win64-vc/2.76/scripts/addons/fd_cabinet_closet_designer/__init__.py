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
    "name": "Cabinet & Closet Designer",
    "author": "Andrew Peel",
    "version": (1, 0, 0),
    "blender": (2, 7, 0),
    "location": "Tools Shelf",
    "description": "This add-on creates a UI to help you use the cabinet and closet library",
    "warning": "",
    "wiki_url": "",
    "category": "Fluid Designer"
}

import bpy
import fd
import math

from bpy.types import PropertyGroup, UIList, Panel, Operator

from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       BoolVectorProperty,
                       PointerProperty,
                       CollectionProperty,
                       EnumProperty)

class PANEL_Cabinet_Closet_Designer(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "objectmode"
    bl_label = "Cabinet & Closet Designer"
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Fluid Designer"
    
    @classmethod
    def poll(cls, context):
        return True

    def draw_header(self, context):
        layout = self.layout
        layout.label('',icon='BRUSH_DATA')
    
    def draw(self, context):
        layout = self.layout
        g = context.scene.lm_cabinet_closet_designer
        g.draw(layout)

def register():
    bpy.utils.register_class(PANEL_Cabinet_Closet_Designer)

def unregister():
    bpy.utils.unregister_class(PANEL_Cabinet_Closet_Designer)
    
if __name__ == "__main__":
    register()
