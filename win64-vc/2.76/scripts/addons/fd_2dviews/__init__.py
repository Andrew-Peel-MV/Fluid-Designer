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
    "name": "2D Views",
    "author": "Ryan Montes",
    "version": (1, 0, 0),
    "blender": (2, 7, 0),
    "location": "Tools Shelf",
    "description": "This add-on creates a UI to generate 2D Views",
    "warning": "",
    "wiki_url": "",
    "category": "Fluid Designer"
}

import bpy

class PANEL_2D_Views(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "objectmode"
    bl_label = "2D Views"
    bl_category = "Fluid Designer"
    bl_options = {'DEFAULT_CLOSED'}    
    
    index = bpy.props.IntProperty(name="Scene Index")
    
    @classmethod
    def poll(cls, context):
        return True

    def draw_header(self, context):
        layout = self.layout
        layout.label('',icon='ALIGN')

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        panel_box = layout.box()
        
        row = panel_box.row(align=True)
        row.scale_y = 1.3
        
        elv_scenes = []
        for scene in bpy.data.scenes:
            if scene.mv.elevation_scene:
                elv_scenes.append(scene)
                
        if len(elv_scenes) < 1:
            row.operator("fd_scene.prepare_2d_views",text="Prepare 2D Views",icon='SCENE_DATA')
        else:
            row.operator("fd_scene.prepare_2d_views",text="",icon='FILE_REFRESH')
            row.operator("fd_scene.render_2d_views",text="Render Selected Scenes",icon='SCENE_DATA')
            row.menu('MENU_Elevation_Scene_Options',text="",icon='DOWNARROW_HLT')
            panel_box.template_list("LIST_scenes", 
                                    " ", 
                                    bpy.data, 
                                    "scenes", 
                                    bpy.context.window_manager.mv, 
                                    "elevation_scene_index")
                
class MENU_Elevation_Scene_Options(bpy.types.Menu):
    bl_label = "Elevation Scene Options"

    def draw(self, context):
        layout = self.layout
        layout.operator("fd_general.select_all_elevation_scenes",text="Select All",icon='CHECKBOX_HLT').select_all = True
        layout.operator("fd_general.select_all_elevation_scenes",text="Deselect All",icon='CHECKBOX_DEHLT').select_all = False
        layout.separator()
        layout.operator("fd_scene.clear_2d_views",text="Clear All 2D Views",icon='X')

def register():
    bpy.utils.register_class(PANEL_2D_Views)
    bpy.utils.register_class(MENU_Elevation_Scene_Options)

def unregister():
    bpy.utils.unregister_class(PANEL_2D_Views)
    bpy.utils.unregister_class(MENU_Elevation_Scene_Options)

if __name__ == "__main__":
    register()
