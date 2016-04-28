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
    "name": "Specification Groups",
    "author": "Andrew Peel",
    "version": (1, 0, 0),
    "blender": (2, 7, 0),
    "location": "Tools Shelf",
    "description": "This add-on creates a UI to modify the Specification Groups",
    "warning": "",
    "wiki_url": "",
    "category": "Fluid Designer"
}

import bpy

class PANEL_Specification_Groups(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "objectmode"
    bl_label = "Specification Groups"
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Fluid Designer"
    
    @classmethod
    def poll(cls, context):
        return True
        
    def draw_header(self, context):
        layout = self.layout
        layout.label('',icon='SOLO_ON')
    
    def draw(self, context):
        layout = self.layout
        library = context.scene.cabinetlib

        if len(library.spec_groups) == 0:
            layout.operator('cabinetlib.reload_spec_group_from_template',icon='FILE_REFRESH')
        else:
            active_spec_group = library.spec_groups[library.spec_group_index]
            
            col = layout.column(align=True)
            
            box = col.box()
            row = box.row(align=True)
            row.menu('MENU_Available_Spec_Groups',text=active_spec_group.name,icon='SOLO_ON')
            row.menu('MENU_Spec_Group_Options',text="",icon='DOWNARROW_HLT')
            
            row = box.row(align=True)
            row.scale_y = 1.3
            row.prop_enum(library, "spec_group_tabs", 'MATERIALS', icon='MATERIAL', text="Materials")
            row.prop_enum(library, "spec_group_tabs", 'CUTPARTS', icon='MOD_UVPROJECT', text="Cutparts")
            row.prop_enum(library, "spec_group_tabs", 'EDGEPARTS', icon='EDGESEL', text="Edgeparts")

            if library.spec_group_tabs == 'MATERIALS':
                active_spec_group.draw_materials(col)
            if library.spec_group_tabs == 'CUTPARTS':
                active_spec_group.draw_cutparts(col)
            if library.spec_group_tabs == 'EDGEPARTS':
                active_spec_group.draw_edgeparts(col)
                
def register():
    bpy.utils.register_class(PANEL_Specification_Groups)

def unregister():
    bpy.utils.unregister_class(PANEL_Specification_Groups)

if __name__ == "__main__":
    register()
