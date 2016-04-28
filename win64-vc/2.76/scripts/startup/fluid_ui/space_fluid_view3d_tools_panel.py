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

import fd

#TODO: Finish Project Template Implementation
class PANEL_Project_Templates(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "objectmode"
    bl_label = "Project Templates"
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Fluid Designer"
    
    @classmethod
    def poll(cls, context):
        return True
        
    def draw_header(self, context):
        layout = self.layout
        layout.label('',icon='FILE_BACKUP')
    
    def draw(self, context):
        layout = self.layout
        box = layout.box()
        box.label("Select a Project Template",icon='LAYER_ACTIVE')
        split = box.split(.6)
        split.template_icon_view(context.window_manager.mv,"project_templates",show_labels=True)
        col = split.column()
        col.operator("fd_general.create_project",text="Create Project",icon='ZOOMIN')
        col.operator("fd_general.create_project",text="Save To Template",icon='BACK') #TODO: Create Save as Project Template Operator

class MENU_Product_Library_Options(Menu):
    bl_label = "Product Library Options"

    def draw(self, context):
        layout = self.layout
        layout.operator("cabinetlib.select_all_products",text="Select All",icon='CHECKBOX_HLT').select_all = True
        layout.operator("cabinetlib.select_all_products",text="Deselect All",icon='CHECKBOX_DEHLT').select_all = False

class MENU_Insert_Library_Options(Menu):
    bl_label = "Insert Library Options"

    def draw(self, context):
        layout = self.layout
        layout.operator("cabinetlib.select_all_inserts",text="Select All",icon='CHECKBOX_HLT').select_all = True
        layout.operator("cabinetlib.select_all_inserts",text="Deselect All",icon='CHECKBOX_DEHLT').select_all = False

class MENU_Spec_Group_Options(Menu):
    bl_label = "Specification Groups"

    def draw(self, context):
        layout = self.layout
        layout.operator("cabinetlib.copy_selected_spec_group",text="Copy Selected Spec Group",icon='ZOOMIN')
        layout.operator("cabinetlib.rename_spec_group",text="Rename Active Spec Group",icon='GREASEPENCIL')
        layout.operator("cabinetlib.update_scene_from_pointers",text="Update Scene from Pointers",icon='SCENE_DATA')
        layout.operator("cabinetlib.reload_spec_group_from_library_modules",text="Reload from Library Modules",icon='FILE_REFRESH')
        layout.operator("cabinetlib.clear_spec_group",text="Clear Spec Groups",icon='X')

class MENU_Current_Cabinet_Menu(Menu):
    bl_label = "Cabinet Options"

    def draw(self, context):
        layout = self.layout
        product_bp = fd.get_bp(context.object,'PRODUCT')
        if product_bp:
            layout.menu('MENU_Change_Cabinet_Spec_Group',icon='SOLO_ON')
            layout.separator()
            if product_bp.parent:
                if product_bp.parent.mv.type == 'BPWALL':
                    props = layout.operator('fd_general.place_product',text="Place Product",icon='LATTICE_DATA')
                    props.object_name = product_bp.name
            props = layout.operator('cabinetlib.make_static_product',text="Make Static",icon='MOD_DISPLACE')
            props.object_name = product_bp.name
            layout.operator('cabinetlib.select_product',text="Select All",icon='MAN_TRANS').object_name = product_bp.name
            
class MENU_Change_Cabinet_Spec_Group(Menu):
    bl_label = "Specification Groups"

    def draw(self, context):
        spec_groups = context.scene.cabinetlib.spec_groups
        layout = self.layout
        product_bp = fd.get_bp(context.object,'PRODUCT')
        for spec_group in spec_groups:
            if product_bp.cabinetlib.spec_group_name == spec_group.name:
                props = layout.operator('cabinetlib.change_product_spec_group',text=spec_group.name,icon='FILE_TICK')
                props.spec_group_name = spec_group.name
                props.object_name = product_bp.name
            else:
                props = layout.operator('cabinetlib.change_product_spec_group',text=spec_group.name,icon='LINK')
                props.spec_group_name = spec_group.name
                props.object_name = product_bp.name
                
class MENU_Available_Spec_Groups(Menu):
    bl_label = "Specification Groups"

    def draw(self, context):
        spec_groups = context.scene.cabinetlib.spec_groups
        spec_group_index = context.scene.cabinetlib.spec_group_index
        layout = self.layout
        for index, spec_group in enumerate(spec_groups):
            if index == spec_group_index:
                props = layout.operator('cabinetlib.change_active_spec_group',text=spec_group.name,icon='FILE_TICK')
                props.spec_group_name = spec_group.name
            else:
                props = layout.operator('cabinetlib.change_active_spec_group',text=spec_group.name,icon='LINK')
                props.spec_group_name = spec_group.name

#------REGISTER
classes = [
           MENU_Product_Library_Options,
           MENU_Insert_Library_Options,
           MENU_Spec_Group_Options,
           MENU_Current_Cabinet_Menu,
           MENU_Change_Cabinet_Spec_Group,
           MENU_Available_Spec_Groups
           ]

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

if __name__ == "__main__":
    register()
