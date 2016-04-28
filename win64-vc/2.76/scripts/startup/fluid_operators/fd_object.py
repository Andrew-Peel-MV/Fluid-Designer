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

import bpy, bgl
from bpy.types import Header, Menu, Operator
import math
import mathutils
import bmesh
import fd

from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       BoolVectorProperty,
                       PointerProperty,
                       EnumProperty)

class OPS_grab_object(Operator):
    bl_idname = "fd_object.grab_object"
    bl_label = "Grab Object"
#     bl_options = {'UNDO'}
    
    @classmethod
    def poll(cls, context):
        if context.object:
            return True
        else:
            return False
        return True

    def get_moveable_object(self,obj):
        if (obj.lock_location[0] or fd.get_driver(obj,'location',0)) and (obj.lock_location[1] or fd.get_driver(obj,'location',1)) and (obj.lock_location[2] or fd.get_driver(obj,'location',2)) and obj.parent:
            return self.get_moveable_object(obj.parent)
        else:
            return obj

    def execute(self, context):
        obj = context.object
        if obj.mode == 'OBJECT' and len(context.selected_objects) == 1:
            moveable_obj = self.get_moveable_object(obj)
            bpy.ops.object.select_all(action='DESELECT')
            moveable_obj.select = True
            context.scene.objects.active = moveable_obj
        bpy.ops.transform.transform('INVOKE_DEFAULT',mode='TRANSLATION')
        return {'FINISHED'}
    
class OPS_select_object_by_name(Operator):
    bl_idname = "fd_object.select_object_by_name"
    bl_label = "Select Object"
    bl_options = {'UNDO'}
    
    object_name = StringProperty(name="Object Name")

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        obj = bpy.data.objects[self.object_name]
        bpy.ops.object.select_all(action='DESELECT')
        obj.hide = False
        obj.hide_select = False
        obj.select = True
        context.scene.objects.active = obj
        return {'FINISHED'}
    
class OPS_toggle_edit_mode(Operator):
    bl_idname = "fd_object.toggle_edit_mode"
    bl_label = "Toggle Edit Mode"
    bl_description = "This will toggle between object and edit mode"
    
    object_name = StringProperty(name="Object Name")

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        obj = bpy.data.objects[self.object_name]
        obj.hide = False
        obj.hide_select = False
        obj.select = True
        context.scene.objects.active = obj
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}
    
class OPS_unwrap_mesh(Operator):
    bl_idname = "fd_object.unwrap_mesh"
    bl_label = "Unwrap Mesh"
    bl_options = {'UNDO'}
    
    object_name = StringProperty(name="Object Name")
    
    def execute(self, context):
        if self.object_name in bpy.data.objects:
            obj = bpy.data.objects[self.object_name]
            context.scene.objects.active = obj
        obj = context.active_object
        mode = obj.mode
        if obj.mode == 'OBJECT':
            bpy.ops.object.editmode_toggle()
            
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.uv.smart_project(angle_limit=66, island_margin=0, user_area_weight=0)
        if mode == 'OBJECT':
            bpy.ops.object.editmode_toggle()
        return {'FINISHED'}
    
class OPS_clear_vertex_groups(Operator):
    bl_idname = "fd_object.clear_vertex_groups"
    bl_label = "Clear Vertex Groups"
    bl_description = "This clears all of the vertex group assignments"
    bl_options = {'UNDO'}
    
    object_name = StringProperty(name="Object Name")
    
    def execute(self,context):

        obj = bpy.data.objects[self.object_name]
        
        if obj.mode == 'EDIT':
            bpy.ops.object.editmode_toggle()
            
        for vgroup in obj.vertex_groups:
            for vert in obj.data.vertices:
                vgroup.remove((vert.index,))

        if obj.mode == 'OBJECT':
            bpy.ops.object.editmode_toggle()

        return{'FINISHED'}
    
class OPS_assign_verties_to_vertex_group(Operator):
    bl_idname = "fd_object.assign_verties_to_vertex_group"
    bl_label = "Assign Verties to Vertex Group"
    bl_description = "This clears all of the vertex group assignments"
    bl_options = {'UNDO'}
    
    vertex_group_name = StringProperty(name="Vertex Group Name")
    
    def execute(self,context):

        obj = context.active_object
        
        if obj.mode == 'EDIT':
            bpy.ops.object.editmode_toggle()
            
        vgroup = obj.vertex_groups[self.vertex_group_name]
        
        for vert in obj.data.vertices:
            if vert.select == True:
                vgroup.add((vert.index,),1,'ADD')

        if obj.mode == 'OBJECT':
            bpy.ops.object.editmode_toggle()

        return{'FINISHED'}
    
class OPS_vertex_group_select(Operator):
    bl_idname = "fd_object.vertex_group_select"
    bl_label = "Vertex Group Select"
    bl_description = "This selects all of the verties that are assigned to that vertex group"
    bl_options = {'UNDO'}
    
    object_name = StringProperty(name="Object Name")
    
    def execute(self,context):
        obj = bpy.data.objects[self.object_name]
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.vertex_group_select()
        return{'FINISHED'}
    
class OPS_add_material_slot(Operator):
    bl_idname = "fd_object.add_material_slot"
    bl_label = "Add Material Slot"
    bl_options = {'UNDO'}
    
    object_name = StringProperty(name="Object Name")
    
    def execute(self,context):
        obj = bpy.data.objects[self.object_name]
        override = {'active_object':obj,
                    'object':obj,
                    'window':context.window,
                    'region':context.region}
        bpy.ops.object.material_slot_add(override)
        return{'FINISHED'}
    
class OPS_apply_hook_modifiers(Operator):
    bl_idname = "fd_object.apply_hook_modifiers"
    bl_label = "Apply Hook Modifiers"
    bl_options = {'UNDO'}

    object_name = StringProperty(name="Object Name")

    def execute(self, context):
        obj = bpy.data.objects[self.object_name]
        context.scene.objects.active = obj
        list_mod = []
        if obj:
            for mod in obj.modifiers:
                if mod.type in {'HOOK','MIRROR'}:
                    list_mod.append(mod.name)

        for mod in list_mod:
            bpy.ops.object.modifier_apply(apply_as='DATA',modifier=mod)
            
        obj.lock_location = (False,False,False)
        obj.lock_scale = (False,False,False)
        obj.lock_rotation = (False,False,False)
        
        return {'FINISHED'}

class OPS_apply_shape_keys(Operator):
    bl_idname = "fd_object.apply_shape_keys"
    bl_label = "Apply Shape Keys"
    bl_options = {'UNDO'}

    object_name = StringProperty(name="Object Name")

    def execute(self, context):
        obj = bpy.data.objects[self.object_name]
        context.scene.objects.active = obj
        if obj.type == 'MESH':
            if obj.data.shape_keys:
                bpy.ops.object.shape_key_add(from_mix=True)
                for index, key in enumerate(obj.data.shape_keys.key_blocks):
                    obj.active_shape_key_index = 0
                    bpy.ops.object.shape_key_remove(all=False)
                obj.lock_location = (False,False,False)
                obj.lock_scale = (False,False,False)
                obj.lock_rotation = (False,False,False)
        return {'FINISHED'}
    
class OPS_apply_bool_modifiers(Operator):
    bl_idname = "fd_object.apply_bool_modifiers"
    bl_label = "Apply Boolean Modifiers"
    bl_options = {'UNDO'}

    object_name = StringProperty(name="Object Name")

    def execute(self, context):
        obj = bpy.data.objects[self.object_name]
        context.scene.objects.active = obj
        list_mod = []
        if obj:
            for mod in obj.modifiers:
                if mod.type == 'BOOLEAN':
                    list_mod.append(mod.name)
                    
        for mod in list_mod:
            bpy.ops.object.modifier_apply(apply_as='DATA',modifier=mod)                    

        return {'FINISHED'}    

class OPS_set_base_point(Operator):
    bl_idname = "fd_object.set_base_point"
    bl_label = "Set Base Point"
    bl_options = {'UNDO'}

    object_name = StringProperty(name="Object Name")

    def execute(self, context):
        obj = bpy.data.objects[self.object_name]
        cursor_x = context.scene.cursor_location[0]
        cursor_y = context.scene.cursor_location[1]
        cursor_z = context.scene.cursor_location[2]
        bpy.ops.view3d.snap_cursor_to_selected()
        if obj.mode == 'EDIT':
            bpy.ops.object.editmode_toggle()
            
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        
        context.scene.cursor_location = (cursor_x,cursor_y,cursor_z)
        if obj.mode == 'OBJECT':
            bpy.ops.object.editmode_toggle()
            
        return {'FINISHED'}    

class OPS_apply_array_modifiers(Operator):
    bl_idname = "fd_object.apply_array_modifiers"
    bl_label = "Apply Array Modifiers"
    bl_options = {'UNDO'}

    object_name = StringProperty(name="Object Name")

    def execute(self, context):
        obj = bpy.data.objects[self.object_name]
        context.scene.objects.active = obj
        list_mod = []
        if obj:
            for mod in obj.modifiers:
                if mod.type == 'ARRAY':
                    list_mod.append(mod.name)
                    
        for mod in list_mod:
            bpy.ops.object.modifier_apply(apply_as='DATA',modifier=mod)                    

        return {'FINISHED'}            

class OPS_add_camera(Operator):
    bl_idname = "fd_object.add_camera"
    bl_label = "Add Camera"
    bl_options = {'UNDO'}

    def execute(self, context):
        bpy.ops.object.camera_add(view_align=False)
        camera = context.active_object
        bpy.ops.view3d.camera_to_view()
        camera.data.clip_start = 0
        camera.data.clip_end = 9999
        camera.data.ortho_scale = 200.0
        return {'FINISHED'}

class OPS_add_modifier(Operator):
    bl_idname = "fd_object.add_modifier"
    bl_label = "Add Modifier"
    bl_options = {'UNDO'}
    
    type = EnumProperty(items=fd.enums.enum_modifiers, name="Modifier Type")
    
    @classmethod
    def poll(cls, context):
        return True
    
    def execute(self, context):
        bpy.ops.object.modifier_add(type=self.type)
        return{'FINISHED'}    

class OPS_add_constraint(Operator):    
    bl_idname = "fd_object.add_constraint"
    bl_label = "Add Constraint"
    bl_options = {'UNDO'}
    
    type = EnumProperty(items=fd.enums.enum_constraints, name="Constraint Type")
    
    @classmethod
    def poll(cls, context):
        return True
    
    def execute(self, context):
        bpy.ops.object.constraint_add(type=self.type)
        return{'FINISHED'}    

class OPS_collapse_all_modifiers(Operator):
    bl_idname = "fd_object.collapse_all_modifiers"
    bl_label = "Collapse All Modifiers"
    bl_options = {'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return context.active_object

    def execute(self, context):
        for mod in context.active_object.modifiers:
            mod.show_expanded = False
        return {'FINISHED'}
    
class OPS_collapse_all_constraints(Operator):
    bl_idname = "fd_object.collapse_all_constraints"
    bl_label = "Collapse All Constraints"
    bl_options = {'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return context.active_object

    def execute(self, context):
        for con in context.active_object.constraints:
            con.show_expanded = False
        return {'FINISHED'}
    
class OPS_camera_properties(Operator):
    bl_idname = "fd_object.camera_properties"
    bl_label = "Camera Properties"

    lock_camera = BoolProperty(name="Lock Camera to View")

    @classmethod
    def poll(cls, context):
        return True

    def check(self,context):
        return True

    def __del__(self):
        if self.lock_camera == True:
            bpy.context.space_data.lock_camera = True
        else:
            bpy.context.space_data.lock_camera = False

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self,context,event):
        self.lock_camera = context.space_data.lock_camera
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=fd.get_prop_dialog_width(400))

    def draw(self, context):
        obj = context.active_object
        fd.draw_object_info(self.layout,obj)
        fd.draw_object_data(self.layout, obj)
        self.layout.prop(self,'lock_camera')

#         if context.active_object.type == 'CAMERA':
#             obj = context.active_object
#             cam = obj.data
#             ccam = cam.cycles
#             layout = self.layout
#             box = layout.box()
#             name_box = box.box()
#             row = name_box.row()
#             split = row.split(percentage=0.2)
#             split.label("Name:",icon='SCENE')
#             split.prop(obj,"name",text="")
#             
#             box.label("Transform:")
#             box1 = box.box()
#             row = box1.row()
#             split = box1.split()
#             col = split.column()
#             row = col.row(align=True)          
#             row.prop(obj,"lock_location",index=0,text="")  
#             row.prop(obj,"location",index=0,text="X")
#             row = col.row(align=True)
#             row.prop(obj,"lock_location",index=1,text="")
#             row.prop(obj,"location",index=1,text="Y")
#             row = col.row(align=True)
#             row.prop(obj,"lock_location",index=2,text="")
#             row.prop(obj,"location",index=2,text="Z")
#             col = split.column()
#             row = col.row(align=True)
#             row.prop(obj,"lock_rotation",index=0,text="")
#             row.prop(obj,"rotation_euler",index=0,text="X")
#             row = col.row(align=True)
#             row.prop(obj,"lock_rotation",index=1,text="")
#             row.prop(obj,"rotation_euler",index=1,text="Y")
#             row = col.row(align=True)
#             row.prop(obj,"lock_rotation",index=2,text="")
#             row.prop(obj,"rotation_euler",index=2,text="Z")
#             
#             box.label("Camera Type:")           
#             cam_opt_box_1 = box.box()
#             row = cam_opt_box_1.row()
#             row.prop(cam, "type", expand=True, text="Camera Type")
#             split = cam_opt_box_1.split()
#             col = split.column()
#             if cam.type == 'PERSP':
#                 row = col.row()
#                 if cam.lens_unit == 'MILLIMETERS':
#                     row.prop(cam, "lens")
#                 elif cam.lens_unit == 'FOV':
#                     row.prop(cam, "angle")
#                 row.prop(cam, "lens_unit", text="")
#     
#             if cam.type == 'ORTHO':
#                 col.prop(cam, "ortho_scale")
#         
#             if cam.type == 'PANO':
#                 engine = bpy.context.scene.render.engine
#                 if engine == 'CYCLES':
#                     ccam = cam.cycles
#                     col.prop(ccam, "panorama_type", text="Panorama Type")
#                     if ccam.panorama_type == 'FISHEYE_EQUIDISTANT':
#                         col.prop(ccam, "fisheye_fov")
#                     elif ccam.panorama_type == 'FISHEYE_EQUISOLID':
#                         row = col.row()
#                         row.prop(ccam, "fisheye_lens", text="Lens")
#                         row.prop(ccam, "fisheye_fov")
#                 elif engine == 'BLENDER_RENDER':
#                     row = col.row()
#                     if cam.lens_unit == 'MILLIMETERS':
#                         row.prop(cam, "lens")
#                     elif cam.lens_unit == 'FOV':
#                         row.prop(cam, "angle")
#                     row.prop(cam, "lens_unit", text="")            
#                 
#             box.label("Camera Options:")
#             cam_opt_box_2 = box.box()
#             row = cam_opt_box_2.row()
# #             row.menu("CAMERA_MT_presets", text=bpy.types.CAMERA_MT_presets.bl_label) # THIS ERRORS OUT DUE TO CONTEXT  
#             row.prop_menu_enum(cam, "show_guide")            
#             row = cam_opt_box_2.row()
#             split = row.split()
#             col = split.column()
#             col.prop(cam, "clip_start", text="Clipping Start")
#             col.prop(cam, "clip_end", text="Clipping End")      
#             col = row.column()         
#             col.prop(bpy.context.scene.cycles,"film_transparent",text="Transparent Film")   
#             col.prop(self,"lock_camera",text="Lock Camera to View")
    
import inspect
    
class OPS_draw_floor_plane(Operator):
    bl_idname = "fd_object.draw_floor_plane"
    bl_label = "Draw Floor Plane"
    bl_options = {'UNDO'}
    
    def execute(self, context):
        largest_x = 0
        largest_y = 0
        smallest_x = 0
        smallest_y = 0
        wall_groups = []
        for obj in context.visible_objects:
            if obj.mv.type == 'BPWALL':
                wall_groups.append(fd.Wall(obj))
            
        for group in wall_groups:
            start_point = (group.obj_bp.matrix_world[0][3],group.obj_bp.matrix_world[1][3],0)
            end_point = (group.obj_x.matrix_world[0][3],group.obj_x.matrix_world[1][3],0)

            if start_point[0] > largest_x:
                largest_x = start_point[0]
            if start_point[1] > largest_y:
                largest_y = start_point[1]
            if start_point[0] < smallest_x:
                smallest_x = start_point[0]
            if start_point[1] < smallest_y:
                smallest_y = start_point[1]
            if end_point[0] > largest_x:
                largest_x = end_point[0]
            if end_point[1] > largest_y:
                largest_y = end_point[1]
            if end_point[0] < smallest_x:
                smallest_x = end_point[0]
            if end_point[1] < smallest_y:
                smallest_y = end_point[1]

        loc = (smallest_x , smallest_y,0)
        width = math.fabs(smallest_y) + math.fabs(largest_y)
        length = math.fabs(largest_x) + math.fabs(smallest_x)
        if width == 0:
            width = fd.inches(-48)
        if length == 0:
            length = fd.inches(-48)
        obj_plane = fd.create_floor_mesh('Floor',(length,width,0.0))
        obj_plane.location = loc
        
        #SET CONTEXT
        context.scene.objects.active = obj_plane
        
        return {'FINISHED'}
    
class OPS_add_room_lamp(Operator):
    bl_idname = "fd_object.add_room_lamp"
    bl_label = "Add Room Lamp"
    bl_options = {'UNDO'}
    
    def execute(self, context):
        largest_x = 0
        largest_y = 0
        smallest_x = 0
        smallest_y = 0
        wall_groups = []
        for obj in context.visible_objects:
            if obj.mv.type == 'BPWALL':
                wall_groups.append(fd.Wall(obj))
            
        for group in wall_groups:
            start_point = (group.obj_bp.matrix_world[0][3],group.obj_bp.matrix_world[1][3],0)
            end_point = (group.obj_x.matrix_world[0][3],group.obj_x.matrix_world[1][3],0)
            height = group.obj_z.location.z
            
            if start_point[0] > largest_x:
                largest_x = start_point[0]
            if start_point[1] > largest_y:
                largest_y = start_point[1]
            if start_point[0] < smallest_x:
                smallest_x = start_point[0]
            if start_point[1] < smallest_y:
                smallest_y = start_point[1]
            if end_point[0] > largest_x:
                largest_x = end_point[0]
            if end_point[1] > largest_y:
                largest_y = end_point[1]
            if end_point[0] < smallest_x:
                smallest_x = end_point[0]
            if end_point[1] < smallest_y:
                smallest_y = end_point[1]

        x = (math.fabs(largest_x) - math.fabs(smallest_x))/2
        y = (math.fabs(largest_y) - math.fabs(smallest_y))/2
        z = height - fd.inches(.01)
        
        width = math.fabs(smallest_y) + math.fabs(largest_y)
        length = math.fabs(largest_x) + math.fabs(smallest_x)
        if width == 0:
            width = fd.inches(-48)
        if length == 0:
            length = fd.inches(-48)

        bpy.ops.object.lamp_add(type = 'AREA')
        obj_lamp = context.active_object
        obj_lamp.location.x = x
        obj_lamp.location.y = y
        obj_lamp.location.z = z
        obj_lamp.data.shape = 'RECTANGLE'
        obj_lamp.data.size = length + fd.inches(20)
        obj_lamp.data.size_y = width + fd.inches(20)
        return {'FINISHED'}
    
class OPS_add_machine_token(Operator):
    bl_idname = "cabinetlib.add_machine_token"
    bl_label = "Add Machine Token"
    
    token_name = StringProperty(name="Token Name",default="New Machine Token")
    token_type = EnumProperty(items=fd.enums.enum_machine_tokens, name="Machine Token Type")
    
    @classmethod
    def poll(cls, context):
        if context.object:
            if context.object.cabinetlib.type_mesh == 'CUTPART':
                return True
        return False

    def invoke(self,context,event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=fd.get_prop_dialog_width(400))

    def execute(self, context):
        token = context.object.cabinetlib.mp.machine_tokens.add()      
        token.name = self.token_name
        token.type_token = self.token_type
        return {'FINISHED'}
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self,'token_name')
    
class OPS_delete_machine_token(Operator):
    bl_idname = "cabinetlib.delete_machine_token"
    bl_label = "Delete Machine Token"
    
    token_name = StringProperty(name="Token Name")
    
    @classmethod
    def poll(cls, context):
        if context.object:
            if context.object.cabinetlib.type_mesh == 'CUTPART':
                return True
        return False
    
    def execute(self, context):
        tokens = context.object.cabinetlib.mp.machine_tokens
        if self.token_name in tokens:
            for index, token in enumerate(tokens):
                if token.name == self.token_name:
                    tokens.remove(index)
                    break
        return {'FINISHED'}
    
    
#------REGISTER
classes = [
           OPS_grab_object,
           OPS_select_object_by_name,
           OPS_toggle_edit_mode,
           OPS_unwrap_mesh,
           OPS_add_material_slot,
           OPS_apply_hook_modifiers,
           OPS_apply_shape_keys,
           OPS_apply_bool_modifiers,
           OPS_apply_array_modifiers,
           OPS_set_base_point,
           OPS_clear_vertex_groups,
           OPS_vertex_group_select,
           OPS_add_camera,
           OPS_add_modifier,
           OPS_add_constraint,
           OPS_collapse_all_modifiers,
           OPS_collapse_all_constraints,
           OPS_camera_properties,
           OPS_draw_floor_plane,
           OPS_add_room_lamp,
           OPS_add_machine_token,
           OPS_delete_machine_token,
           OPS_assign_verties_to_vertex_group
           ]

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

if __name__ == "__main__":
    register()
