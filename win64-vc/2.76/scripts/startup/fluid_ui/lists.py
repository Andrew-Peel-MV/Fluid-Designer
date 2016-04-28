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
from bpy.types import Panel, Menu, Header, UIList

import fd

class FD_UL_materials(bpy.types.UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.label(text=item.name,icon='MATERIAL')

class FD_UL_vgroups(bpy.types.UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.label(text=item.name,icon='GROUP_VERTEX')

class FD_UL_prompttabs(UIList):
    
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.label(text=item.name)
        layout.prop(item,'type')

class FD_UL_combobox(UIList):
    
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.label(text=item.name)

class FD_UL_promptitems(UIList):
    
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.label(text=item.name)
        if item.Type == 'NUMBER':
            layout.label(str(item.NumberValue))
        if item.Type == 'CHECKBOX':
            layout.label(str(item.CheckBoxValue))
        if item.Type == 'QUANTITY':
            layout.label(str(item.QuantityValue))
        if item.Type == 'COMBOBOX':
            layout.label(str(item.EnumIndex))
        if item.Type == 'DISTANCE':
            layout.label(str(fd.unit(item.DistanceValue)))
        if item.Type == 'ANGLE':
            layout.label(str(item.AngleValue))
        if item.Type == 'PERCENTAGE':
            layout.label(str(item.PercentageValue))
        if item.Type == 'PRICE':
            layout.label(str(item.PriceValue))

class FD_UL_objects(bpy.types.UIList):
    
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        if item.name not in bpy.data.objects:
            layout.label(text=item.name + " *(missing)",icon='ERROR')
        else:
            obj = bpy.data.objects[item.name]
            
            if obj.type == 'MESH':
                layout.label(text=obj.mv.name_object,icon='OUTLINER_OB_MESH')
    
            if obj.type == 'EMPTY':
                layout.label(text=obj.mv.name_object,icon='OUTLINER_OB_EMPTY')
                    
                if obj.mv.use_as_mesh_hook:
                    layout.label(text="",icon='HOOK')
                    
            if obj.type == 'CURVE':
                layout.label(text=obj.mv.name_object,icon='OUTLINER_OB_CURVE')
                
            if obj.type == 'FONT':
                layout.label(text=obj.mv.name_object,icon='OUTLINER_OB_FONT')
    
            layout.operator("fd_object.select_object_by_name",icon='MAN_TRANS',text="").object_name = item.name
            layout.operator("fd_assembly.delete_object_in_assembly",icon='X',text="",emboss=False).object_name = obj.name

class LIST_specgroups(UIList):
    
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.label(text=item.name,icon='SOLO_ON')
        props = layout.operator('cabinetlib.delete_spec_group',text="",icon='X',emboss=False)
        props.spec_group_name = item.name
        
class LIST_material_pointers(UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        props = layout.operator("cabinetlib.set_pointer",text='',icon='FORWARD')
        props.pointer_name = item.name
        props.pointer_type = 'MATERIAL'
        layout.label(text=item.name,icon='HAND')
        layout.label(text=str(item.item_name),icon='STYLUS_PRESSURE')

class LIST_cutparts(UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        split = layout.split(percentage=.7)
        split.label(text=item.name,icon='MOD_UVPROJECT')
        split.prop(item,'thickness',text="")

class LIST_edgeparts(UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        split = layout.split(percentage=.7)
        split.label(text=item.name,icon='EDGESEL')
        split.prop(item,'thickness',text="")

class LIST_productlist(UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        if item.bp_name in bpy.data.objects:
            obj_bp = bpy.data.objects[item.bp_name]
            layout.label(text=item.name,icon='LATTICE_DATA')
            layout.prop(obj_bp.cabinetlib,'is_custom')
            layout.operator('cabinetlib.prompts',text="",icon='INFO',emboss=False).object_name = obj_bp.name
        else:
            layout.label(text=item.name + " Not Found (Refresh List)",icon='ERROR')
        
class LIST_lib(UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.label(text=item.name,icon='LATTICE_DATA')
        
class LIST_lib_productlist(UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.label(text=item.name,icon='LATTICE_DATA')
        if not item.has_thumbnail:
            layout.label('',icon='RENDER_RESULT')
        if not item.has_file:
            layout.label('',icon='FILE_BLEND')
        layout.prop(item,'selected',text="")

class LIST_lib_insertlist(UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.label(text=item.name,icon='STICKY_UVS_LOC')
        if not item.has_thumbnail:
            layout.label('',icon='RENDER_RESULT')
        if not item.has_file:
            layout.label('',icon='FILE_BLEND')
        layout.prop(item,'selected',text="")

class LIST_sheetstock(UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.label(text=item.name,icon='MOD_UVPROJECT')
        layout.operator('mvcabients.change_material_info',text="",icon='INFO',emboss=False).material_name = item.name
        
class LIST_sheetsizes(UIList):
    
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.label(text='Sheet Size:',icon='MESH_GRID')
        layout.prop(item,'width')
        layout.prop(item,'length')
        material = context.scene.cabinetlib.sheets[context.scene.cabinetlib.sheet_index]
        if len(material.sizes) == index + 1:
            layout.operator('cabinetlib.add_sheet_size',text="",icon='ZOOMIN')
        else:
            layout.label(text="",icon='BLANK1')

class LIST_edgebanding(UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.label(text=item.name,icon='EDGESEL')
        layout.prop(item,'thickness')
        layout.operator('mvcabients.change_edgebanding_info',text="",icon='INFO',emboss=False).material_name = item.name

class LIST_scenes(UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        
        if item.mv.plan_view_scene or item.mv.elevation_scene:
            layout.label(item.mv.name_scene)
            layout.prop(item.mv, 'elevation_selected', text="")
        else:
            layout.label(item.name)

classes = [
           FD_UL_materials,
           FD_UL_vgroups,
           FD_UL_prompttabs,
           FD_UL_combobox,
           FD_UL_objects,
           FD_UL_promptitems,
           LIST_specgroups,
           LIST_material_pointers,
           LIST_cutparts,
           LIST_edgeparts,
           LIST_productlist,
           LIST_lib,
           LIST_lib_productlist,
           LIST_lib_insertlist,
           LIST_sheetstock,
           LIST_sheetsizes,
           LIST_edgebanding,
           LIST_scenes
           ]

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

