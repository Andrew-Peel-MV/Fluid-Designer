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
import bgl
import fd
import math
from bpy.types import Header, Menu, Operator
import os, subprocess
import time
from bpy.app.handlers import persistent
import bpy_extras.image_utils as img_utils

from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       PointerProperty,
                       EnumProperty)

from mathutils import Matrix
from bpy_extras.io_utils import axis_conversion
from mathutils.geometry import normal

def get_export_prompts(obj_bp):
    """ Used in create_fluid_project_xml
        this collects all of the needed product prompts for the 121 product match
    """
    
    prompts = {}
    
    def add_prompt(prompt):
        if prompt.Type == 'NUMBER':
            prompts[prompt.name] = str(prompt.NumberValue)
        if prompt.Type == 'QUANTITY':
            prompts[prompt.name] = str(prompt.QuantityValue)
        if prompt.Type == 'COMBOBOX':
            prompts[prompt.name] = str(prompt.COL_EnumItem[prompt.EnumIndex].name)
        if prompt.Type == 'CHECKBOX':
            prompts[prompt.name] = str(prompt.CheckBoxValue)
        if prompt.Type == 'TEXT':
            prompts[prompt.name] = str(prompt.TextValue)
        if prompt.Type == 'DISTANCE':
            prompts[prompt.name] = str(round(fd.meter_to_unit(prompt.DistanceValue),4))
        if prompt.Type == 'ANGLE':
            prompts[prompt.name] = str(prompt.AngleValue)
        if prompt.Type == 'PERCENTAGE':
            prompts[prompt.name] = str(prompt.PercentageValue)
        if prompt.Type == 'PRICE':
            prompts[prompt.name] = str(prompt.PriceValue)
    
    def add_child_prompts(obj):
        for child in obj.children:
            if child.mv.type == 'BPASSEMBLY':
                add_prompts(child)
            if len(child.children) > 0:
                add_child_prompts(child)
        
    def add_prompts(obj):
        for prompt in obj.mv.PromptPage.COL_Prompt:
            if prompt.export:
                add_prompt(prompt)
                
    add_prompts(obj_bp)
    add_child_prompts(obj_bp)

    return prompts

def faces_from_mesh(ob, global_matrix, use_mesh_modifiers=False, triangulate=True):
    """
    From an object, return a generator over a list of faces.

    Each faces is a list of his vertexes. Each vertex is a tuple of
    his coordinate.

    use_mesh_modifiers
        Apply the preview modifier to the returned liste

    triangulate
        Split the quad into two triangles
    """

    # get the editmode data
    ob.update_from_editmode()

    # get the modifiers
    try:
        mesh = ob.to_mesh(bpy.context.scene, use_mesh_modifiers, "PREVIEW")
    except RuntimeError:
        raise StopIteration

    mesh.transform(global_matrix * ob.matrix_world)

    if triangulate:
        # From a list of faces, return the face triangulated if needed.
        def iter_face_index():
            for face in mesh.tessfaces:
                vertices = face.vertices[:]
                if len(vertices) == 4:
                    yield vertices[0], vertices[1], vertices[2]
                    yield vertices[2], vertices[3], vertices[0]
                else:
                    yield vertices
    else:
        def iter_face_index():
            for face in mesh.tessfaces:
                yield face.vertices[:]

    vertices = mesh.vertices

    for indexes in iter_face_index():
        yield [vertices[index].co.copy() for index in indexes]

    bpy.data.meshes.remove(mesh)

class OPS_render_scene(Operator):
    bl_idname = "fd_scene.render_scene"
    bl_label = "Render Scene"

    write_still = BoolProperty(name="Write Still",
                               description="Write image to disk after render",
                               default=False)

    def execute(self, context):
        ui = context.scene.mv.ui
        rd = context.scene.render
        rl = rd.layers.active
        freestyle_settings = rl.freestyle_settings
        scene = context.scene

        if scene.camera is None:
            self.report({'ERROR'}, "Cannot render - there is no camera in the scene!")
            #Add camera automatically?
            return {'FINISHED'}

        if ui.render_type_tabs == 'NPR':
            rd.engine = 'BLENDER_RENDER'
            rd.use_freestyle = True
            rd.line_thickness = 0.75
            rd.resolution_percentage = 100
            rl.use_pass_combined = False
            rl.use_pass_z = False
            freestyle_settings.crease_angle = 2.617994

        if context.window_manager.mv.use_opengl_dimensions:
            file_format = context.scene.render.image_settings.file_format.lower()
            
            bpy.ops.render.render('INVOKE_DEFAULT', write_still=True)
            
            while not os.path.exists(bpy.path.abspath(context.scene.render.filepath) + "." + file_format):
                time.sleep(0.1)

            img_result = fd.render_opengl(self,context)

            if self.write_still == True:
                abs_filepath = bpy.path.abspath(context.scene.render.filepath)
                save_path = abs_filepath.replace("_tmp","") + "." + file_format.lower()
                img_result.save_render(save_path)

        else:
            bpy.ops.render.render('INVOKE_DEFAULT')

            if self.write_still == True:
                bpy.ops.render.render('INVOKE_DEFAULT',write_still=True)

        return {'FINISHED'}

    @persistent
    def set_to_cycles_re(self):
        bpy.context.scene.render.engine = 'CYCLES'

    bpy.app.handlers.render_complete.append(set_to_cycles_re)

class OPS_render_settings(Operator): 
    bl_idname = "fd_scene.render_settings"
    bl_label = "Render Settings"
    
    def execute(self, context):
        return {'FINISHED'}
    
    def check(self,context):
        return True
    
    def invoke(self,context,event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=fd.get_prop_dialog_width(400))

    def draw(self, context):
        layout = self.layout
        scene = bpy.context.scene
        rd = scene.render
        image_settings = rd.image_settings
        ui = context.scene.mv.ui
        rl = rd.layers.active
        linestyle = rl.freestyle_settings.linesets[0].linestyle
        
        box = layout.box()
        row = box.row(align=True)
        row.prop_enum(ui,"render_type_tabs", 'PRR',icon='RENDER_STILL',text="Photo Realistic Render")
        row.prop_enum(ui,"render_type_tabs", 'NPR',icon='SNAP_FACE',text="Line Drawing")
        row = box.row(align=True)
        row.label(text="Render Size:",icon='STICKY_UVS_VERT')        
        row.prop(rd, "resolution_x", text="X")
        row.prop(rd, "resolution_y", text="Y")
        
        if ui.render_type_tabs == 'PRR':
            row = box.row()
            row.label(text="Rendering Quality:",icon='IMAGE_COL')
            row.prop(scene.cycles,"samples",text='Passes')
            row = box.row()
            row.label(text="Image Format:",icon='IMAGE_DATA')
            row.prop(image_settings,"file_format",text="")
            row = box.row()
            row.label(text="Display Mode:",icon='RENDER_RESULT')
            row.prop(rd,"display_mode",text="")
            row = box.row()
            row.label(text="Use Transparent Film:",icon='SEQUENCE')
            row.prop(scene.cycles,"film_transparent",text='')
            
        if ui.render_type_tabs == 'NPR':
            row = box.row()
            row.label(text="Image Format:",icon='IMAGE_DATA')
            row.prop(image_settings,"file_format",text="")
            row = box.row()
            row.label(text="Display Mode:",icon='RENDER_RESULT')
            row.prop(rd,"display_mode",text="")
            row = box.row()
            row.prop(linestyle, "color", text="Line Color")
            row = box.row()
            row.prop(bpy.data.worlds[0], "horizon_color", text="Background Color")
        
class OPS_add_thumbnail_camera_and_lighting(Operator):
    bl_idname = "fd_scene.add_thumbnail_camera_and_lighting"
    bl_label = "Add Thumbnail Camera"
    bl_options = {'UNDO'}

    def execute(self, context):
        bpy.ops.object.camera_add(view_align=True)
        camera = context.active_object
        context.scene.camera = camera
        context.scene.cycles.film_transparent = True
        
        camera.data.clip_end = 9999
        camera.scale = (10,10,10)
        
        bpy.ops.object.lamp_add(type='SUN')
        sun = bpy.context.object
        sun.select = False
        sun.rotation_euler = (.785398, .785398, 0.0)
        
        context.scene.render.resolution_x = 1080
        context.scene.render.resolution_y = 1080
        context.scene.render.resolution_percentage = 25
        
        override = {}
        for window in bpy.context.window_manager.windows:
            screen = window.screen
             
            for area in screen.areas:
                if area.type == 'VIEW_3D':
                    override = {'window': window, 'screen': screen, 'area': area}
                    bpy.ops.view3d.camera_to_view(override)
                    for space in area.spaces:
                        if space.type == 'VIEW_3D':
                            space.lock_camera = True
                    break
        return {'FINISHED'}
        
class OPS_create_unity_build(Operator): #Not Used
    bl_idname = "fd_scene.create_unity_build"
    bl_label = "Build for Unity 3D"
    bl_options = {'UNDO'}
    
    save_name = StringProperty(name="Name")
    
    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        subprocess.call("\"C:\\Program Files (x86)\\Unity\\Editor\\Unity.exe\"" + \
                         "-batchmode -executeMethod PerformBuild.build", shell=False)
        return {'FINISHED'}            

class OPS_prepare_For_sketchfab(Operator):
    """ This prepares the scene for uploading to Sketchfab.
    """
    bl_idname = "cabinetlib.delete_hidden_objects"
    bl_label = "Delete Hidden Objects"
    bl_description = "This simplifies the scene."
    bl_options = {'UNDO'}
    
    _timer = None
    current_item = 0
    objects = []
    delete_objs = []
    bps = []
    
    def invoke(self, context, event):
        wm = context.window_manager
        
        for obj in bpy.context.scene.objects:
            if obj.type == 'CURVE' and obj.parent:
                obj.select = True
                bpy.context.scene.objects.active = obj
                bpy.ops.object.convert(target='MESH')
                bpy.ops.object.select_all(action='DESELECT')
                #these also need to be unwraped correctly
            
            if obj.type == 'MESH':
                if len(obj.data.vertices) > 1:
                    self.objects.append(obj)   
        
        self._timer = wm.event_timer_add(0.001, context.window)
        wm.modal_handler_add(self)
        if context.area.type == 'VIEW_3D':
            args = (self, context)
            self._handle = bpy.types.SpaceView3D.draw_handler_add(fd.draw_callback_px, args, 'WINDOW', 'POST_PIXEL')
            self.mouse_loc = []
            self.mouse_text = "Preparing Object "  + str(self.current_item + 1) + " of " + str(len(self.objects))
            self.header_text = "Preparing Object " + str(self.current_item + 1) + " of " + str(len(self.objects))
        return {'RUNNING_MODAL'}    
    
    def modal(self, context, event):
        context.area.tag_redraw()
        self.mouse_loc = (event.mouse_region_x,event.mouse_region_y)
        if event.type in {'RIGHTMOUSE', 'ESC'}:
            return self.cancel(context)
        
        if event.type == 'TIMER':
            if self.current_item + 1 <= len(self.objects):                     
                obj = self.objects[self.current_item]
                bpy.context.scene.objects.active = obj
                #clear shapekeys
                if obj.data.shape_keys:
                    bpy.ops.fd_object.apply_shape_keys(object_name=obj.name)           
                
                #clear modifiers 
#                 for mod in obj.modifiers:
#                     bpy.ops.object.modifier_apply(mod.name)
#                 if obj.modifiers != 'NONE':  
                    #obj.to_mesh(context.scene,True,'PREVIEW')
                    #This needs to be done in the correct order (mods applied only if first in stack)
                bpy.ops.fd_object.apply_hook_modifiers(object_name=obj.name)
                bpy.ops.fd_object.apply_bool_modifiers(object_name=obj.name)
                    #bpy.ops.fd_object.apply_array_modifiers(object_name=obj.name)
#                     #Apply Bevel Modifiers
                
                #clear drivers 
                if obj.animation_data:
                    for DR in obj.animation_data.drivers:
                        obj.driver_remove(DR.data_path)                 
                
                #clear vertex groups         
                if obj.vertex_groups:
                    bpy.context.scene.objects.active = obj
                    bpy.ops.object.vertex_group_remove(all=True) 
                
                #clear parent and keep transformation          
                obj.matrix_local = obj.matrix_world
                obj.parent = None
                    
                self.current_item += 1
                
                if self.current_item + 1 <= len(self.objects):
                    self.mouse_text = "Preparing Object " + str(self.current_item + 1) + " of " + str(len(self.objects))
                    self.header_text = "Preparing Object " + str(self.current_item + 1) + " of " + str(len(self.objects))
                context.area.tag_redraw()
            else:
                self.delete_extra_objs()
                bpy.ops.fd_material.clear_material_copies()
                bpy.ops.fd_scene.join_meshes_by_material()  
                return self.cancel(context)
        return {'PASS_THROUGH'}    
    
    def delete_extra_objs(self):  
        for obj in bpy.context.scene.objects:
            if obj.parent:
                if obj.parent.mv.type != 'BPWALL': 
                    if obj not in self.delete_objs:
                        self.delete_objs.append(obj)
                             
                    if obj.type == 'EMPTY':
                        if obj not in self.delete_objs:
                            self.delete_objs.append(obj)
                             
                    if obj.mv.type == 'BPASSEMBLY':
                        if obj not in self.delete_objs:
                            self.delete_objs.append(obj)
                             
            if obj.mv.use_as_bool_obj:
                if obj not in self.delete_objs:
                    self.delete_objs.append(obj)
                 
            if obj.mv.type in {'BPWALL','BPASSEMBLY','VPDIMX','VPDIMY','VPDIMZ'}:
                if obj not in self.delete_objs:
                    self.delete_objs.append(obj)    
                    
            if obj.hide == True or obj.hide_select == True:
                if obj not in self.delete_objs:
                    self.delete_objs.append(obj) 
                      
        fd.delete_obj_list(self.delete_objs)        
    
    def cancel(self, context):
        progress = context.window_manager.cabinetlib
        progress.current_item = 0
        wm = context.window_manager
        wm.event_timer_remove(self._timer)
        bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
        return {'FINISHED'}    

class OPS_join_meshes_by_material(Operator):
    bl_idname = "fd_scene.join_meshes_by_material"
    bl_label = "Join Meshes by Material"
    bl_options = {'UNDO'}
    
    obj_join = []

    def gather_objects_by_material(self, mat):
        for obj in bpy.context.scene.objects:
            if obj.type == 'MESH':
                if obj.material_slots:
                    if obj.material_slots[0].material == mat:
                        self.obj_join.append(obj)        

    def execute(self, context):                 
        objects = bpy.context.scene.objects
        materials = bpy.data.materials
        
        #seperate meshes by material slots
#         for obj in objects:
#             obj.select = True
        bpy.ops.object.select_all(action='SELECT')    
        bpy.ops.mesh.separate(type='MATERIAL')
        bpy.ops.object.select_all(action='DESELECT')            
        #bpy.context.scene.objects.active = None

        #add objs w same materials to list
        #do this faster
        
        for mat in materials:
            self.gather_objects_by_material(mat)

            #join objects
            if self.obj_join:
                bpy.context.scene.objects.active = self.obj_join[0]
                for obj in self.obj_join:
                    obj.select = True
                    #bpy.context.selected_objects.append(obj)  
                
                if bpy.context.active_object != 'NONE':    
                    bpy.ops.object.join()              
                    bpy.ops.object.select_all(action='DESELECT')
                    bpy.context.scene.objects.active = None
                
            self.obj_join.clear()
#                       
#                 bpy.ops.object.join()
#                 bpy.ops.object.select_all(action='DESELECT')
#                 bpy.context.scene.objects.active = None
#                 obj_join.clear()
#                 
#             else:
#                 continue
            
        return {'FINISHED'}

class OPS_Prepare_Plan_view(Operator):
    bl_idname = "fd_scene.prepare_plan_view"    
    bl_label = "Prepare Plan View"
    bl_description = "Prepare Plan View"
    bl_options = {'UNDO'}    
    
    padding = FloatProperty(name="Padding",
                            default=0.25)
    
    def execute(self,context):
        
        original_scene = context.screen.scene
        
        prev_pv = None

        for scene in bpy.data.scenes:
            if scene.mv.plan_view_scene:
                prev_pv = scene
                context.screen.scene = scene
                bpy.ops.scene.delete()        
            
        bpy.ops.scene.new('INVOKE_DEFAULT',type='EMPTY')   
        pv_scene = context.scene     
        pv_scene.name = "Plan View"
        pv_scene.mv.name_scene = "Plan View" 
        pv_scene.mv.plan_view_scene = True 
        if prev_pv:
            pv_scene.mv.elevation_selected = prev_pv.mv.elevation_selected
            
        for obj in original_scene.objects:
            pv_scene.objects.link(obj)    
            
        for obj in pv_scene.objects:
            if obj.mv.type == 'BPWALL':
                wall = fd.Wall(obj_bp = obj)
                wall.get_wall_mesh().select = True
                
        cam_name = "Plan View Camera"
        
        camera_data = bpy.data.cameras.new(cam_name)
        camera_obj = bpy.data.objects.new(name=cam_name, 
                                          object_data=camera_data)
        
        pv_scene.objects.link(camera_obj)
        pv_scene.camera = camera_obj                
                
        camera_obj.rotation_euler.z = math.radians(-90.0)    
        camera_obj.data.type = 'ORTHO'
        pv_scene.render.resolution_y = 1280
        bpy.ops.view3d.camera_to_view_selected()    
        camera_obj.data.ortho_scale += self.padding                
        
        pv_scene.mv.opengl_dim.gl_default_color = (0.1, 0.1, 0.1, 1.0)
        pv_scene.mv.ui.render_type_tabs = 'NPR'
        lineset = pv_scene.render.layers["RenderLayer"].freestyle_settings.linesets.new("LineSet")
        lineset.linestyle = \
        original_scene.render.layers["RenderLayer"].freestyle_settings.linesets["LineSet"].linestyle
        
        if pv_scene.world == None:
            pv_scene.world = bpy.data.worlds["World"]        
        
        pv_scene.world.horizon_color = (1.0, 1.0, 1.0)
        pv_scene.render.display_mode = 'NONE'
        pv_scene.render.use_lock_interface = True

        context.window_manager.mv.use_opengl_dimensions = True
        
        return {'FINISHED'}   
    
class OPS_Prepare_2d_elevations(Operator):
    bl_idname = "fd_scene.prepare_2d_elevations"    
    bl_label = "Prepare for Printing 2D Elevation"
    bl_description = "Prepare for Printing 2D Elevation"
    bl_options = {'UNDO'}    
    
    padding = 0.75  
            
    def group_wall_objects(self, obj_bp, group):
        objs = []
        objs.append(obj_bp)
        
        for child in obj_bp.children:
            if len(child.children) > 0:
                self.group_wall_objects(child, group)
            else:
                objs.append(child)

        for obj in objs:
            group.objects.link(obj)
            
    def link_grp_instance_to_scene(self, group, scene, obj_bp):  
        instance = bpy.data.objects.new(obj_bp.mv.name_object + " "  + "Instance" , None)
        scene.objects.link(instance)
        instance.dupli_type = 'GROUP'
        instance.dupli_group = group        
        
    def set_cameras(self, current_scene, new_scene, wall):  
        camera_data = bpy.data.cameras.new(new_scene.name)
        camera_obj = bpy.data.objects.new(name=camera_data.name + " Camera", 
                                          object_data=camera_data)
         
        current_scene.objects.link(camera_obj)    
        current_scene.camera = camera_obj
        camera_obj.data.type = 'ORTHO'
        camera_obj.rotation_euler.x = math.radians(90.0) 
        camera_obj.rotation_euler.z = wall.obj_bp.rotation_euler.z    
        camera_obj.location = wall.obj_bp.location       
        
        bpy.ops.object.select_all(action='DESELECT')
        wall.get_wall_mesh().select = True
        bpy.ops.view3d.camera_to_view_selected()     
        
        current_scene.camera = None
        current_scene.objects.unlink(camera_obj)
        new_scene.objects.link(camera_obj)
        new_scene.camera = camera_obj
        new_scene.render.resolution_y = 1280
        bpy.data.cameras[new_scene.name].ortho_scale += self.padding
        
    def link_vis_dim_empties_to_scene(self, scene, obj_bp):
        for child in obj_bp.children:
            if child.mv.type in ('VISDIM_A','VISDIM_B'):
                scene.objects.link(child)
            if len(child.children) > 0:
                self.link_vis_dim_empties_to_scene(scene, child) 
                      
    def execute(self, context):
        original_scene = bpy.data.scenes[context.scene.name]
        context.window_manager.mv.use_opengl_dimensions = True
        walls = []
        existing_scenes = {}
        
        for scene in bpy.data.scenes:
            if scene.mv.elevation_scene:# or scene.mv.plan_view_scene:
                existing_scenes[scene.name] = scene.mv.elevation_selected
                context.screen.scene = scene
                bpy.ops.scene.delete()
         
        for obj in context.scene.objects:
            if obj.mv.type == 'BPWALL':
                wall = fd.Wall(obj_bp = obj)
                walls.append(wall)
                if len(wall.get_wall_groups()) > 0:
                     
                    wall_group = bpy.data.groups.new(obj.mv.name_object)
                    self.group_wall_objects(obj, wall_group)
                      
                    bpy.ops.scene.new('INVOKE_DEFAULT',type='EMPTY')
                    new_scene = context.scene
                    new_scene.name = obj.name
                    
                    print(existing_scenes)
                    if new_scene.name in existing_scenes:
                        new_scene.mv.elevation_selected = existing_scenes[new_scene.name]
                        print("NEW SCENE",new_scene.mv.elevation_selected)
                        
                    new_scene.mv.name_scene = obj.mv.name_object + " " + str(obj.cabinetlib.item_number)
                    new_scene.mv.elevation_img_name = obj.name
                    new_scene.mv.elevation_scene = True
                      
                    new_scene.world = original_scene.world
                    self.link_vis_dim_empties_to_scene(new_scene, obj)
      
                    bpy.context.screen.scene = original_scene
                        
                    self.link_grp_instance_to_scene(wall_group, new_scene, obj)   
                         
                    self.set_cameras(original_scene, new_scene, wall)
                
                    new_scene.mv.opengl_dim.gl_default_color = (0.1, 0.1, 0.1, 1.0)
                    new_scene.mv.ui.render_type_tabs = 'NPR'
                    lineset = new_scene.render.layers["RenderLayer"].freestyle_settings.linesets.new("LineSet")
                    lineset.linestyle = \
                    original_scene.render.layers["RenderLayer"].freestyle_settings.linesets["LineSet"].linestyle                
                    
                    if new_scene.world.name != "World":
                        new_scene.world = bpy.data.worlds["World"]
                            
                    new_scene.world.horizon_color = (1.0, 1.0, 1.0)
                    new_scene.render.display_mode = 'NONE'
                    new_scene.render.use_lock_interface = True
         
        bpy.ops.fd_scene.prepare_plan_view()
        bpy.context.screen.scene = original_scene
        
        return {'FINISHED'}
    
class OPS_clear_2d_views(Operator):   
    bl_idname = "fd_scene.clear_2d_views"    
    bl_label = "Delete 2d View Scenes"
    bl_description = "Delete all 2d view scenes"
    bl_options = {'UNDO'}     
    
    def execute(self, context):
        for scene in bpy.data.scenes:
            if scene.mv.elevation_scene or scene.mv.plan_view_scene:
                context.screen.scene = scene
                bpy.ops.scene.delete()                         
                
        return {'FINISHED'}
    
class OPS_prepare_2d_views(Operator):   
    bl_idname = "fd_scene.prepare_2d_views"    
    bl_label = "Prepare 2d View Scenes"
    bl_description = "Prepare 2D View Scenes"
    bl_options = {'UNDO'}          

    ev_pad = FloatProperty(name="Elevation View Padding",
                           default=0.75)
    
    pv_pad = FloatProperty(name="Plan View Padding",
                           default=0.75)  
            
    def link_grp_instance_to_scene(self, group, scene, obj_bp):  
        instance = bpy.data.objects.new(obj_bp.mv.name_object + " "  + "Instance" , None)
        scene.objects.link(instance)
        instance.dupli_type = 'GROUP'
        instance.dupli_group = group        
        
    def set_cameras(self, current_scene, new_scene, wall):  
        camera_data = bpy.data.cameras.new(new_scene.name)
        camera_obj = bpy.data.objects.new(name=camera_data.name + " Camera", 
                                          object_data=camera_data)
         
        current_scene.objects.link(camera_obj)    
        current_scene.camera = camera_obj
        camera_obj.data.type = 'ORTHO'
        camera_obj.rotation_euler.x = math.radians(90.0) 
        camera_obj.rotation_euler.z = wall.obj_bp.rotation_euler.z    
        camera_obj.location = wall.obj_bp.location       
        
        bpy.ops.object.select_all(action='DESELECT')
        wall.get_wall_mesh().select = True
        bpy.ops.view3d.camera_to_view_selected()     
        
        current_scene.camera = None
        current_scene.objects.unlink(camera_obj)
        new_scene.objects.link(camera_obj)
        new_scene.camera = camera_obj
        new_scene.render.resolution_y = 1280
        bpy.data.cameras[new_scene.name].ortho_scale += self.ev_pad
        
    def link_vis_dim_empties_to_scene(self, scene, obj_bp):
        for child in obj_bp.children:
            if child.mv.type in ('VISDIM_A','VISDIM_B'):
                scene.objects.link(child)
            if len(child.children) > 0:
                self.link_vis_dim_empties_to_scene(scene, child) 
                      
    def execute(self, context):
        context.window_manager.mv.use_opengl_dimensions = True
        
        existing_scenes = {}
        for scene in bpy.data.scenes:
            if scene.mv.elevation_scene or scene.mv.plan_view_scene:
                existing_scenes[scene.name] = scene.mv.elevation_selected
                context.screen.scene = scene
                bpy.ops.scene.delete()
            else:
                original_scene = bpy.data.scenes[context.scene.name]
        context.screen.scene = original_scene        
            
        bpy.ops.scene.new('INVOKE_DEFAULT',type='EMPTY')   
        pv_scene = context.scene     
        pv_scene.name = "Plan View"
        pv_scene.mv.name_scene = "Plan View" 
        pv_scene.mv.plan_view_scene = True 
            
        if pv_scene.name in existing_scenes:
            pv_scene.mv.elevation_selected = existing_scenes[pv_scene.name]            
            
        for obj in original_scene.objects:
            pv_scene.objects.link(obj)    
            
        for obj in pv_scene.objects:
            if obj.mv.type == 'BPWALL':
                wall = fd.Wall(obj_bp = obj)
                wall.get_wall_mesh().select = True
                
        cam_name = "Plan View Camera"
        camera_data = bpy.data.cameras.new(cam_name)
        camera_obj = bpy.data.objects.new(name=cam_name,object_data=camera_data)
        pv_scene.objects.link(camera_obj)
        pv_scene.camera = camera_obj                        
        camera_obj.rotation_euler.z = math.radians(-90.0)    
        camera_obj.data.type = 'ORTHO'
        pv_scene.render.resolution_y = 1280
        bpy.ops.view3d.camera_to_view_selected()    
        camera_obj.data.ortho_scale += self.pv_pad                
        
        pv_scene.mv.ui.render_type_tabs = 'NPR'
        lineset = pv_scene.render.layers["RenderLayer"].freestyle_settings.linesets.new("LineSet")
        lineset.linestyle = \
        original_scene.render.layers["RenderLayer"].freestyle_settings.linesets["LineSet"].linestyle 
      
        pv_scene.world = bpy.data.worlds["World"]
        pv_scene.world.horizon_color = (1.0, 1.0, 1.0)
        pv_scene.render.display_mode = 'NONE'
        pv_scene.render.use_lock_interface = True        

        for obj in context.scene.objects:
            if obj.mv.type == 'BPWALL':
                wall = fd.Wall(obj_bp = obj)
                if len(wall.get_wall_groups()) > 0:
                    
                    wall_group = wall.create_wall_group()
                       
                    bpy.ops.scene.new('INVOKE_DEFAULT',type='EMPTY')
                    new_scene = context.scene
                    new_scene.name = obj.name   
                    new_scene.mv.name_scene = obj.mv.name_object + " " + str(obj.cabinetlib.item_number)
                    new_scene.mv.elevation_img_name = obj.name
                    
                    #when creating a new scene first elevation scene.mv.plan_view_scene == True
                    #Should be False by default
                    #This could be from using bpy.ops to create a new scene instead of creating new from data.scenes collection
                    new_scene.mv.plan_view_scene = False
                    
                    new_scene.mv.elevation_scene = True
                    new_scene.world = original_scene.world                      
                      
                    if new_scene.name in existing_scenes:
                        new_scene.mv.elevation_selected = existing_scenes[new_scene.name]
                    
                    self.link_vis_dim_empties_to_scene(new_scene, obj)
        
                    bpy.context.screen.scene = original_scene
                          
                    self.link_grp_instance_to_scene(wall_group, new_scene, obj)   
                           
                    self.set_cameras(original_scene, new_scene, wall)
                  
                    new_scene.mv.ui.render_type_tabs = 'NPR'
                    lineset = new_scene.render.layers["RenderLayer"].freestyle_settings.linesets.new("LineSet")
                    lineset.linestyle = \
                    original_scene.render.layers["RenderLayer"].freestyle_settings.linesets["LineSet"].linestyle                
                              
                    new_scene.world.horizon_color = (1.0, 1.0, 1.0)
                    new_scene.render.display_mode = 'NONE'
                    new_scene.render.use_lock_interface = True

        bpy.context.screen.scene = original_scene

        return {'FINISHED'}
       
class OPS_render_2d_views(Operator):
    bl_idname = "fd_scene.render_2d_views"
    bl_label = "Render 2D Views"
    bl_description = "Renders 2d Scenes"
    
    render_all = BoolProperty(name="Render all elevation scenes", default=False)
    
    def invoke(self, context, event):
        wm = context.window_manager
        if not bpy.data.is_saved:
            return wm.invoke_props_dialog(self, width=fd.get_prop_dialog_width(400))     
        else:
            return self.execute(context)         
    
    def draw(self,context):
        layout = self.layout
        layout.label("File must be saved before rendering",icon='INFO')  
    
    def execute(self, context):
        active_filename = bpy.path.basename(context.blend_data.filepath).replace(".blend","")
        write_dir = bpy.path.abspath("//") + active_filename
        
        bpy.ops.fd_scene.prepare_2d_views()
        
        if not os.path.exists(write_dir):
            os.mkdir(write_dir)        
        else:
            for file in os.listdir(write_dir):
                os.unlink(write_dir + "\\" + file)        
        
        if self.render_all:
            bpy.ops.fd_general.select_all_elevation_scenes(select_all=True)
        
        for scene in bpy.data.scenes:
            if scene.mv.elevation_selected:
                
                scene.mv.opengl_dim.gl_default_color = (0.1, 0.1, 0.1, 1.0)
                
                if scene.mv.plan_view_scene:
                    img_name = active_filename + "_tmp"
                else:
                    img_name = scene.mv.elevation_img_name + "_tmp"
                
                context.screen.scene = scene
                context.scene.render.filepath = "//" + active_filename + "\\" + img_name
                bpy.ops.fd_scene.render_scene(write_still=True)
                 
        if not self.render_all:
            for scene in bpy.data.scenes:
                if not scene.mv.elevation_scene or not scene.mv.plan_view_scene:
                    context.screen.scene = scene
                    default_glcolor = scene.mv.opengl_dim.gl_default_color
                    
            for scene in bpy.data.scenes:
                scene.mv.opengl_dim.gl_default_color = default_glcolor
                
            file_format = context.screen.scene.render.file_extension        
            bpy.ops.fd_general.open_browser_window(path=bpy.path.abspath("//") +\
                                                   active_filename +\
                                                   "\\" +\
                                                   img_name.replace("_tmp","") +\
                                                   file_format)                
        
        return {'FINISHED'}
       
class OPS_render_all_elevation_scenes(Operator):
    bl_idname = "fd_scene.render_all_elevation_scenes"
    bl_label = "Render all elevation scenes"
    bl_description = "Renders all elevation scenes"
        
    render = True    
    render_all = BoolProperty(name="Render all elevation scenes", default=False)
    selected_scenes = []
        
    def execute(self, context):
        if not bpy.data.is_saved or not self.render:
            return {'FINISHED'}
    
        ren_path = "//"
        file_name = bpy.path.basename(context.blend_data.filepath).replace(".blend","")
        write_dir = bpy.path.abspath(ren_path) + file_name.replace(".blend","")
        original_scene = context.scene
        
        bpy.ops.fd_scene.prepare_2d_elevations()
        
        if not os.path.exists(write_dir):
            os.mkdir(write_dir)        
        else:
            for file in os.listdir(write_dir):
                os.unlink(write_dir + "\\" + file)
        
        if self.render_all == True:
            for scene in bpy.data.scenes:
                if scene.mv.elevation_scene:
                    if scene.mv.plan_view_scene:
                        img_name = file_name + "_tmp"
                    else:
                        img_name = scene.mv.elevation_img_name + "_tmp"
                        
                    context.screen.scene = scene
                    context.scene.render.filepath = "//" + file_name + "\\" + img_name
                    bpy.ops.fd_scene.render_scene(write_still=True)            
        else:
            for scene in bpy.data.scenes:
                if (scene.mv.elevation_scene or scene.mv.plan_view_scene) and scene.mv.elevation_selected:
                    if scene.mv.plan_view_scene:
                        img_name = file_name
                    else:
                        img_name = scene.mv.elevation_img_name
                    
                    print(scene, img_name)    
                    context.screen.scene = scene
                    context.scene.render.filepath = "//" + file_name + "\\" + img_name
                    bpy.ops.fd_scene.render_scene(write_still=True)
                    
            context.screen.scene = original_scene
            file_format = context.screen.scene.render.file_extension
            bpy.ops.fd_general.open_browser_window(path=bpy.path.abspath("//") +\
                                                   file_name +\
                                                   "\\" +\
                                                   img_name +\
                                                   file_format)
                
        return{'FINISHED'}
        
#     def invoke(self,context,event):
#         wm = context.window_manager
#         
#         for scene in bpy.data.scenes:
#             if scene.mv.elevation_selected:
#                 self.selected_scenes.append(scene)
# 
#         if len(self.selected_scenes) < 1:
#             self.render = False
#         
#         if not bpy.data.is_saved:
#             return wm.invoke_props_dialog(self, width=fd.get_prop_dialog_width(400))  
#         else:
#             return self.execute(context)
#      
#     def draw(self,context):
#         layout = self.layout
#         layout.label("File must be saved before rendering",icon='INFO')           



class OPS_export_mvfd(Operator):
    bl_idname = "cabinetlib.export_mvfd"
    bl_label = "Export MVFD File"
    bl_description = "This will export a mvfd file. The file must be saved first."
 
    walls = []
    products = []
    
    xml = None
    
    @classmethod
    def poll(cls, context):
        if bpy.data.filepath != "":
            return True
        else:
            return False

    def distance(self,distance):
        return str(math.fabs(round(fd.meter_to_unit(distance),4)))
    
    def location(self,location):
        return str(round(fd.meter_to_unit(location),4))
    
    def angle(self,angle):
        return str(round(math.degrees(angle),4))
    
    def clear_and_collection_data(self,context):
        for product in self.products:
            self.products.remove(product)
         
        for wall in self.walls:
            self.walls.remove(wall)
             
        bpy.ops.cabinetlib.get_materials()
        for obj in context.visible_objects:
            if obj.mv.type == 'BPWALL':
                self.walls.append(obj)
            if obj.mv.type == 'BPASSEMBLY':
                if obj.cabinetlib.type_group == 'PRODUCT':
                    self.products.append(obj)
    
    def write_properties(self,project_node):
        elm_properties = self.xml.add_element(project_node,'Properties')
        for scene in bpy.data.scenes:
            for prop in scene.mv.project_properties:
                elm_prop = self.xml.add_element(elm_properties,'Property',prop.name)
                self.xml.add_element_with_text(elm_prop,'Value',prop.value)
                self.xml.add_element_with_text(elm_prop,'GlobalVariableName',prop.global_variable_name)
                self.xml.add_element_with_text(elm_prop,'ProjectWizardVariableName',prop.project_wizard_variable_name)
                self.xml.add_element_with_text(elm_prop,'SpecificationGroupName',prop.specification_group_name)
    
    def write_locations(self,project_node):
        elm_locations = self.xml.add_element(project_node,'Locations')
        for scene in bpy.data.scenes:
            self.xml.add_element(elm_locations,'Location',scene.name)
    
    def write_walls(self,project_node):
        elm_walls = self.xml.add_element(project_node,"Walls")
        
        for obj_wall in self.walls:
            wall = fd.Wall(obj_wall)
            elm_wall = self.xml.add_element(elm_walls,'Wall',wall.obj_bp.mv.name_object)
            self.xml.add_element_with_text(elm_wall,'LinkID',obj_wall.name)
            self.xml.add_element_with_text(elm_wall,'LinkIDLocation',obj_wall.users_scene[0].name)
            self.xml.add_element_with_text(elm_wall,'Width',self.distance(wall.obj_x.location.x))
            self.xml.add_element_with_text(elm_wall,'Height',self.distance(wall.obj_z.location.z))
            self.xml.add_element_with_text(elm_wall,'Depth',self.distance(wall.obj_y.location.y))
            self.xml.add_element_with_text(elm_wall,'XOrigin',self.location(obj_wall.matrix_world[0][3]))
            self.xml.add_element_with_text(elm_wall,'YOrigin',self.location(obj_wall.matrix_world[1][3]))
            self.xml.add_element_with_text(elm_wall,'ZOrigin',self.location(obj_wall.matrix_world[2][3]))
            self.xml.add_element_with_text(elm_wall,'Angle',self.angle(obj_wall.rotation_euler.z))

    def write_products(self,project_node):
        specgroups = bpy.context.scene.cabinetlib.spec_groups
        elm_products = self.xml.add_element(project_node,"Products")
        item_number = 1
        for obj_product in self.products:
            spec_group = specgroups[obj_product.cabinetlib.spec_group_index]
            product = fd.Assembly(obj_product)
            elm_product = self.xml.add_element(elm_products,'Product',product.obj_bp.mv.name_object)
            self.xml.add_element_with_text(elm_product,'LinkID',obj_product.name)
            if obj_product.parent:
                self.xml.add_element_with_text(elm_product,'LinkIDWall',obj_product.parent.name)
            else:
                self.xml.add_element_with_text(elm_product,'LinkIDWall','None')
            
            if obj_product.cabinetlib.is_custom:
                self.xml.add_element_with_text(elm_product,'IsCustom','True')
            else:
                self.xml.add_element_with_text(elm_product,'IsCustom','True')
            self.xml.add_element_with_text(elm_product,'IsCorner','False')
            self.xml.add_element_with_text(elm_product,'LinkIDLocation',obj_product.users_scene[0].name)
            self.xml.add_element_with_text(elm_product,'LinkIDSpecificationGroup',spec_group.name)
            self.xml.add_element_with_text(elm_product,'ItemNumber',str(item_number))
            self.xml.add_element_with_text(elm_product,'LinkIDLibrary',obj_product.cabinetlib.library_name)
            self.xml.add_element_with_text(elm_product,'Width',self.distance(product.obj_x.location.x))
            self.xml.add_element_with_text(elm_product,'Height',self.distance(product.obj_z.location.z))
            self.xml.add_element_with_text(elm_product,'Depth',self.distance(product.obj_y.location.y))
            self.xml.add_element_with_text(elm_product,'XOrigin',self.location(obj_product.matrix_world[0][3]))
            self.xml.add_element_with_text(elm_product,'YOrigin',self.location(obj_product.matrix_world[1][3]))
            self.xml.add_element_with_text(elm_product,'ZOrigin',self.location(obj_product.location.z))
            if obj_product.parent:
                angle = obj_product.parent.rotation_euler.z + obj_product.rotation_euler.z
                self.xml.add_element_with_text(elm_product,'Angle',self.angle(angle))
            else:
                self.xml.add_element_with_text(elm_product,'Angle',self.angle(obj_product.rotation_euler.z))

            #PROMPTS
            elm_prompts = self.xml.add_element(elm_product,"Prompts")
            prompts_dict = get_export_prompts(obj_product)
            for prompt in prompts_dict:
                elm_prompt = self.xml.add_element(elm_prompts,'Prompt',prompt)
                prompt_value = prompts_dict[prompt]
                if prompt_value == 'True':
                    prompt_value = str(1)
                if prompt_value == 'False':
                    prompt_value = str(0)
                self.xml.add_element_with_text(elm_prompt,'Value',prompt_value)

            elm_parts = self.xml.add_element(elm_product,"Parts")
            self.write_stl_files_for_product(elm_parts,obj_product,spec_group)
                
            elm_hardware = self.xml.add_element(elm_product,"Hardware")
            self.write_hardware_for_product(elm_hardware,obj_product)
                
            item_number += 1
    
    def write_materials(self,project_node):
        elm_materials = self.xml.add_element(project_node,"Materials")
        for material in bpy.context.scene.cabinetlib.sheets:
            elm_material = self.xml.add_element(elm_materials,'Material',material.name)
            self.xml.add_element_with_text(elm_material,'Type',"2")
            self.xml.add_element_with_text(elm_material,'Thickness',self.distance(material.thickness))
            self.xml.add_element_with_text(elm_material,'LinkIDCoreRendering',material.core_material)
            self.xml.add_element_with_text(elm_material,'LinkIDTopFaceRendering',material.top_material)
            self.xml.add_element_with_text(elm_material,'LinkIDBottomFaceRendering',material.bottom_material)
            elm_sheets = self.xml.add_element(elm_material,"Sheets")
            for sheet in material.sizes:
                elm_sheet = self.xml.add_element(elm_sheets,'Sheet',self.distance(sheet.width) + " X " + self.distance(sheet.length))
                self.xml.add_element_with_text(elm_sheet,'Width',self.distance(sheet.width))
                self.xml.add_element_with_text(elm_sheet,'Length',self.distance(sheet.length))
                self.xml.add_element_with_text(elm_sheet,'LeadingLengthTrim',self.distance(sheet.leading_length_trim))
                self.xml.add_element_with_text(elm_sheet,'TrailingLengthTrim',self.distance(sheet.trailing_length_trim))
                self.xml.add_element_with_text(elm_sheet,'LeadingWidthTrim',self.distance(sheet.leading_width_trim))
                self.xml.add_element_with_text(elm_sheet,'TrailingWidthTrim',self.distance(sheet.trailing_width_trim))

    def write_edgebanding(self,project_node):
        elm_edgebanding = self.xml.add_element(project_node,"Edgebanding")
        for edgeband in bpy.context.scene.cabinetlib.edgebanding:
            elm_edge = self.xml.add_element(elm_edgebanding,'Edgeband',edgeband.name)
            self.xml.add_element_with_text(elm_edge,'Type',"3")
            self.xml.add_element_with_text(elm_edge,'Type',self.distance(edgeband.thickness))

    def write_spec_groups(self,project_node):
        elm_spec_groups = self.xml.add_element(project_node,"SpecGroups")
        
        for spec_group in bpy.context.scene.cabinetlib.spec_groups:
            elm_spec_group = self.xml.add_element(elm_spec_groups,'SpecGroup',spec_group.name)
            elm_cutparts = self.xml.add_element(elm_spec_group,'CutParts')
            for cutpart in spec_group.cutparts:
                elm_cutpart = self.xml.add_element(elm_cutparts,'PointerName',cutpart.mv_pointer_name)
                mat_name = fd.get_material_name_from_pointer(cutpart,spec_group)
                self.xml.add_element_with_text(elm_cutpart,'MaterialName',mat_name)
                 
            elm_edgeparts = self.xml.add_element(elm_spec_group,'EdgeParts')
            for edgepart in spec_group.edgeparts:
                elm_edgepart = self.xml.add_element(elm_edgeparts,'PointerName',edgepart.mv_pointer_name)
                mat_name = fd.get_edgebanding_name_from_pointer_name(edgepart.name,spec_group)
                self.xml.add_element_with_text(elm_edgepart,'MaterialName',mat_name)
                
    def write_hardware_for_product(self,elm_hardware,obj_bp):
        for child in obj_bp.children:
            if child.cabinetlib.type_mesh == 'HARDWARE':
                if not child.hide:
#                     self.write_hardware_node(elm_hardware, child)
                    self.xml.add_element(elm_hardware,'Hardware',child.mv.name_object)
            self.write_hardware_for_product(elm_hardware, child)

    def write_stl_files_for_product(self,elm_parts,obj_bp,spec_group):
        for child in obj_bp.children:
            if child.cabinetlib.type_mesh == 'CUTPART':
                if not child.hide:
                    self.write_stl_node(elm_parts, child, spec_group)
            self.write_stl_files_for_product(elm_parts, child, spec_group)

    def write_stl_node(self,node,obj,spec_group):
        assembly = fd.Assembly(obj.parent)
        elm_part = self.xml.add_element(node,'Part',assembly.obj_bp.mv.name_object)
        self.xml.add_element_with_text(elm_part,'PartType',fd.get_material_name(obj))
        self.xml.add_element_with_text(elm_part,'MaterialName',fd.get_material_name(obj))
        self.xml.add_element_with_text(elm_part,'StlName',obj.name + '.stl')
        self.xml.add_element_with_text(elm_part,'Thickness',self.distance(fd.get_part_thickness(obj)))
        self.xml.add_element_with_text(elm_part,'LinkIDProduct',fd.get_bp(obj,'PRODUCT').name)
        self.xml.add_element_with_text(elm_part,'PartLength',str(fd.unit(obj.dimensions.x)))
        self.xml.add_element_with_text(elm_part,'PartWidth',str(fd.unit(obj.dimensions.y)))
        self.xml.add_element_with_text(elm_part,'Comment',assembly.obj_bp.cabinetlib.comment)
        self.xml.add_element_with_text(elm_part,'XOrigin',self.distance(0))
        self.xml.add_element_with_text(elm_part,'YOrigin',self.distance(0))
        self.xml.add_element_with_text(elm_part,'ZOrigin',self.distance(0))
        self.xml.add_element_with_text(elm_part,'XRotation',self.angle(assembly.obj_bp.rotation_euler.x))
        self.xml.add_element_with_text(elm_part,'YRotation',self.angle(assembly.obj_bp.rotation_euler.y))
        self.xml.add_element_with_text(elm_part,'ZRotation',self.angle(assembly.obj_bp.rotation_euler.z))
        self.xml.add_element_with_text(elm_part,'EdgeWidth1',fd.get_edgebanding_name_from_pointer_name(obj.cabinetlib.edge_w1,spec_group))
        self.xml.add_element_with_text(elm_part,'EdgeLength1',fd.get_edgebanding_name_from_pointer_name(obj.cabinetlib.edge_l1,spec_group))
        self.xml.add_element_with_text(elm_part,'EdgeWidth2',fd.get_edgebanding_name_from_pointer_name(obj.cabinetlib.edge_w2,spec_group))
        self.xml.add_element_with_text(elm_part,'EdgeLength2',fd.get_edgebanding_name_from_pointer_name(obj.cabinetlib.edge_l2,spec_group))
        self.write_machine_tokens(elm_part, obj)
        global_matrix = axis_conversion(to_forward='Y',to_up='Z').to_4x4() * Matrix.Scale(1.0, 4)
        faces = faces_from_mesh(obj, global_matrix, True)
        self.write_geometry(elm_part, faces)

    def write_geometry(self,elm_part,faces):
        elm_geo = self.xml.add_element(elm_part,"Geometry")
        for face in faces:
            elm_face = self.xml.add_element(elm_geo,'Face',"Face")
            nor = '%f,%f,%f' % normal(*face)[:]
            norm = nor.split(",")
            elm_normal = self.xml.add_element(elm_face,'Normal','Normal')
            self.xml.add_element_with_text(elm_normal,'X',str(norm[0]))
            self.xml.add_element_with_text(elm_normal,'Y',str(norm[1]))
            self.xml.add_element_with_text(elm_normal,'Z',str(norm[2]))
            for vert in face:
                elm_vertex = self.xml.add_element(elm_face,'Vertex',"Vertex")
                self.xml.add_element_with_text(elm_vertex,'X',str(fd.unit(vert[0])))
                self.xml.add_element_with_text(elm_vertex,'Y',str(fd.unit(vert[1])))
                self.xml.add_element_with_text(elm_vertex,'Z',str(fd.unit(vert[2])))

    def write_machine_tokens(self,elm_part,obj_part):
        elm_tokens = self.xml.add_element(elm_part,"MachineTokens")
        for token in obj_part.cabinetlib.mp.machine_tokens:
            elm_token = self.xml.add_element(elm_tokens,'MachineToken',token.name)
            param_dict = token.create_parameter_dictionary()
            self.xml.add_element_with_text(elm_token,'Instruction',token.type_token + token.face)
            self.xml.add_element_with_text(elm_token,'Par1',param_dict['Par1'])
            self.xml.add_element_with_text(elm_token,'Par2',param_dict['Par2'])
            self.xml.add_element_with_text(elm_token,'Par3',param_dict['Par3'])
            self.xml.add_element_with_text(elm_token,'Par4',param_dict['Par4'])
            self.xml.add_element_with_text(elm_token,'Par5',param_dict['Par5'])
            self.xml.add_element_with_text(elm_token,'Par6',param_dict['Par6'])
            self.xml.add_element_with_text(elm_token,'Par7',param_dict['Par7'])
            self.xml.add_element_with_text(elm_token,'Par8',param_dict['Par8'])
            self.xml.add_element_with_text(elm_token,'Par9',param_dict['Par9'])
 
    def execute(self, context):
        project_name, ext = os.path.splitext(os.path.basename(bpy.data.filepath))
         
        self.clear_and_collection_data(context)
        
        # CREATE XML
        self.xml = fd.MV_XML()
        root = self.xml.create_tree()
        
        elm_project = self.xml.add_element(root,'Project',project_name)
        self.write_properties(elm_project)
        self.write_locations(elm_project)
        self.write_walls(elm_project)
        self.write_products(elm_project)
        self.write_materials(elm_project)
        self.write_edgebanding(elm_project)
        self.write_spec_groups(elm_project)
        
        # WRITE FILE
        path = os.path.join(os.path.dirname(bpy.data.filepath),"MV.xml")
        self.xml.write(path)
        return {'FINISHED'}

#------REGISTER

classes = [
           OPS_render_scene,
           OPS_render_settings,
           OPS_add_thumbnail_camera_and_lighting,
           OPS_create_unity_build,
           OPS_prepare_For_sketchfab,
           OPS_join_meshes_by_material,
           OPS_Prepare_Plan_view,
           OPS_Prepare_2d_elevations,
           OPS_clear_2d_views,
           OPS_prepare_2d_views,
           OPS_render_2d_views,
           OPS_render_all_elevation_scenes,
           OPS_export_mvfd
           ]

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

if __name__ == "__main__":
    register()
