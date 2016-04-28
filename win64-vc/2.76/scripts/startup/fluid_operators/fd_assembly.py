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
from bpy.types import Operator
import math
import bmesh

from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       BoolVectorProperty,
                       PointerProperty,
                       EnumProperty,
                       CollectionProperty)

import fd

def update_vector_groups(obj_bp):
    """ This is used to add all of the vector groups to 
        an assembly this should be called everytime a new object
        is added to an assembly.
    """
    vgroupslist = []
    vgroupslist.append('X Dimension')
    vgroupslist.append('Y Dimension')
    vgroupslist.append('Z Dimension')
    objlist = []
    
    for child in obj_bp.children:
        if child.type == 'EMPTY' and child.mv.use_as_mesh_hook:
            vgroupslist.append(child.mv.name_object)
        if child.type == 'MESH' and child.mv.type not in {'BPASSEMBLY','BPWALL'}:
            objlist.append(child)
    
    for obj in objlist:
        for vgroup in vgroupslist:
            if vgroup not in obj.vertex_groups:
                obj.vertex_groups.new(name=vgroup)

class OPS_add_wall(Operator):
    bl_idname = "fd_assembly.add_wall"
    bl_label = "Draw Wall"
    bl_description = "Draw a Wall"
#     bl_options = {'UNDO'} This is pushed manually at the end of execute
     
    add_to_selected = BoolProperty(name="Add New Wall to Selected",default=True)
     
    direction = EnumProperty(name="Placement on Wall",
                             items=[('LEFT',"Left",""),
                                    ('STRAIGHT',"Straight",""),
                                    ('RIGHT',"Right","")],
                             default='STRAIGHT')
    
    wall_length = FloatProperty(name="Wall Length",default=fd.inches(120),unit='LENGTH')
    wall_height = FloatProperty(name="Wall Height",default=fd.inches(108),unit='LENGTH')
    
    rotation = FloatProperty(name="Rotation")
    group_wall = None
    selected_wall = None
    zoom_all = False
    delete_wall = True
    
    @classmethod
    def poll(cls, context):
        return True
     
    def check(self, context):
        self.update_wall(context)
        return True
     
    def __del__(self):
        if self.delete_wall: # Only Delete Wall if user didn't click OK
            fd.delete_object_and_children(self.group_wall.obj_bp)
            
    def invoke(self,context,event):
        wm = context.window_manager
        if context.active_object:
            obj_wall_bp = fd.get_wall_bp(context.active_object)
            if obj_wall_bp:
                self.selected_wall = fd.Wall(obj_wall_bp)
                self.rotation = math.degrees(obj_wall_bp.rotation_euler.z)
            else:
                self.direction = 'STRAIGHT'
                self.rotation = 0
        else:
            self.direction = 'STRAIGHT'
            self.rotation = 0
        
        self.create_wall(context)
        self.update_wall(context)
        return wm.invoke_props_dialog(self, width=fd.get_prop_dialog_width(400))
         
    def create_wall(self,context):
        self.group_wall = fd.Wall()
        self.group_wall.create_wall()
        obj_mesh = self.group_wall.build_wall_mesh()
        self.group_wall.obj_bp.location = (0,0,0)
        obj_mesh.draw_type = 'WIRE'

    def update_wall(self,context):
        wm = context.window_manager
        if self.direction == 'LEFT':
            wm.mv.wall_rotation = self.rotation + 90
        if self.direction == 'STRAIGHT':
            wm.mv.wall_rotation = self.rotation
        if self.direction == 'RIGHT':
            wm.mv.wall_rotation = self.rotation + -90
        self.group_wall.obj_bp.rotation_euler.z = math.radians(wm.mv.wall_rotation)
        self.group_wall.obj_x.location.x = self.wall_length
        self.group_wall.obj_y.location.y = fd.inches(1)
        self.group_wall.obj_z.location.z = self.wall_height

        if self.found_wall(context) == False or self.add_to_selected == False:
            self.group_wall.obj_bp.location = context.scene.cursor_location
        else:
            if self.selected_wall:
                self.group_wall.obj_bp.location.x = self.selected_wall.obj_x.matrix_world[0][3]
                self.group_wall.obj_bp.location.y = self.selected_wall.obj_x.matrix_world[1][3]
            else:
                self.group_wall.obj_bp.location = context.scene.cursor_location
        self.group_wall.refresh_hook_modifiers()
        self.group_wall.obj_x.hide = True
        self.group_wall.obj_y.hide = True
        self.group_wall.obj_z.hide = True
        
    def draw(self,context):
        layout = self.layout
        box = layout.box()
        col = box.column(align=False)
        
        row = col.row(align=True)
        row.prop_enum(self, "direction", 'LEFT', icon='TRIA_LEFT', text="Left") 
        row.prop_enum(self, "direction", 'STRAIGHT', icon='TRIA_UP', text="Straight") 
        row.prop_enum(self, "direction", 'RIGHT', icon='TRIA_RIGHT', text="Right")   
        
        row = col.row()
        row.label("Wall Length:")
        row.prop(self,"wall_length",text="")
        
        row = col.row()
        row.label("Wall Height:")
        row.prop(self,"wall_height",text="")

        if self.found_wall(context):
            row = col.row()
            row.prop(self,"add_to_selected",text="Add to Selected Wall")

    def found_wall(self,context):
        for obj in context.visible_objects:
            if obj.mv.type == 'BPWALL':
                return True
        return False
            
    def execute(self, context):
        self.delete_wall = False
        for child in self.group_wall.obj_bp.children:
            if child.type == 'MESH':
                child.draw_type = 'TEXTURED'
                
        if self.found_wall(context) == False or self.add_to_selected == False:
            self.group_wall.obj_bp.location = context.scene.cursor_location
        else:
            if self.selected_wall:
                fd.connect_objects_location(self.selected_wall.obj_x,self.group_wall.obj_bp)
            
        if self.zoom_all:
            bpy.ops.view3d.view_all(center=True)
             
        # THIS MUST BE PUSHED MANUALLY OTHERWISE WALL MESHES 
        # BECOME WARPED WHEN USING bl_options = {'UNDO'}
        bpy.ops.ed.undo_push()
        return {'FINISHED'}

class OPS_draw_walls(Operator):
    bl_idname = "fd_assembly.draw_wall"
    bl_label = "Draws Walls"
    bl_options = {'UNDO'}
    
    #READONLY
    drawing_plane = None
    wall = None
    previous_wall = None
    
    typed_value = ""
    
    starting_point = (0,0,0)
    header_text = "(Esc, Right Click) = Cancel Command  :  (Left Click) = Place Wall  :  (Ctrl) = Disconnect/Move Wall"
    
    def cancel_drop(self,context,event):
        fd.delete_object_and_children(self.wall.obj_bp)
        context.window.cursor_set('DEFAULT')
        fd.delete_obj_list([self.drawing_plane])
        return {'FINISHED'}
        
    def __del__(self):
        bpy.context.area.header_text_set()
        
    def create_wall(self):
        con = None
        if self.previous_wall:
            con = self.previous_wall.obj_x
            
        self.wall = fd.Wall()
        self.wall.create_wall()
        obj_mesh = self.wall.build_wall_mesh()
        self.wall.obj_bp.location = self.starting_point
        obj_mesh.draw_type = 'WIRE'
        self.wall.obj_z.location.z = bpy.context.scene.mv.default_wall_height
        self.wall.obj_y.location.y = bpy.context.scene.mv.default_wall_depth
        self.wall.obj_bp.cabinetlib.item_number = self.get_wall_count()
        if con:
            fd.connect_objects_location(con,self.wall.obj_bp)
            
        width = self.wall.get_var("dim_x","width")
        height = self.wall.get_var("dim_z","height")
        depth = self.wall.get_var("dim_y","depth")
             
        dim = fd.Dimension()
        dim.parent(self.wall.obj_bp)
        dim.start_y('depth+INCH(5)',[depth])
        dim.start_z('height+INCH(5)',[height])
        dim.end_x('width',[width])
        dim.anchor.hide = True
        
    def position_wall(self,p):
        x = p[0] - self.starting_point[0]
        y = p[1] - self.starting_point[1]
        
        if math.fabs(x) > math.fabs(y):
            if x > 0:
                self.wall.obj_bp.rotation_euler.z = math.radians(0)
            else:
                self.wall.obj_bp.rotation_euler.z = math.radians(180)
            if self.typed_value == "":
                self.wall.obj_x.location.x = math.fabs(x)
            else:
                value = eval(self.typed_value)
                if bpy.context.scene.unit_settings.system == 'METRIC':
                    self.wall.obj_x.location.x = fd.millimeters(float(value))
                else:
                    self.wall.obj_x.location.x = fd.inches(float(value))
            
        if math.fabs(y) > math.fabs(x):
            if y > 0:
                self.wall.obj_bp.rotation_euler.z = math.radians(90)
            else:
                self.wall.obj_bp.rotation_euler.z = math.radians(-90)
            if self.typed_value == "":
                self.wall.obj_x.location.x = math.fabs(y)
            else:
                value = eval(self.typed_value)
                if bpy.context.scene.unit_settings.system == 'METRIC':
                    self.wall.obj_x.location.x = fd.millimeters(float(value))
                else:
                    self.wall.obj_x.location.x = fd.inches(float(value))
                
    def extend_wall(self):
        if self.previous_wall:
            prev_wall_rot = round(self.previous_wall.obj_bp.rotation_euler.z,2)
            wall_rot = round(self.wall.obj_bp.rotation_euler.z,2)
            
            extend_wall = False
            
            if prev_wall_rot == round(math.radians(0),2):
                if wall_rot == round(math.radians(-90),2):
                    extend_wall = True
            if prev_wall_rot == round(math.radians(-90),2):
                if wall_rot == round(math.radians(180),2):
                    extend_wall = True
            if prev_wall_rot == round(math.radians(180),2):
                if wall_rot == round(math.radians(90),2):
                    extend_wall = True
            if prev_wall_rot == round(math.radians(90),2):
                if wall_rot == round(math.radians(0),2):
                    extend_wall = True
            
            if extend_wall:
                obj = self.previous_wall.get_wall_mesh()
                bpy.ops.fd_object.apply_hook_modifiers(object_name=obj.name)
                
                mesh = obj.data
                
                bm = bmesh.new()
                
                size = (self.previous_wall.obj_x.location.x,self.previous_wall.obj_y.location.y,self.previous_wall.obj_z.location.z)
                
                verts = [(0.0, 0.0, 0.0),
                         (0.0, size[1], 0.0),
                         (size[0], size[1], 0.0),
                         (size[0], 0.0, 0.0),
                         (0.0, 0.0, size[2]),
                         (0.0, size[1], size[2]),
                         (size[0], size[1], size[2]),
                         (size[0], 0.0, size[2]),
                         (size[0]+bpy.context.scene.mv.default_wall_depth, size[1], 0.0),
                         (size[0]+bpy.context.scene.mv.default_wall_depth, 0.0, 0.0),
                         (size[0]+bpy.context.scene.mv.default_wall_depth, 0.0, size[2]),
                         (size[0]+bpy.context.scene.mv.default_wall_depth, size[1], size[2]),
                         ]
                
                faces = [(0, 1, 2, 3),   #bottom
                         (4, 7, 6, 5),   #top
                         (0, 4, 5, 1),   #left face
                         (1, 5, 6, 2),   #back face
                         (4, 0, 3, 7),   #wall face
                         (3, 9, 8, 2),   #2bottom
                         (7, 10, 11, 6), #2top
                         (2, 6, 11, 8),  #2backface
                         (7, 3, 9, 10),  #2wallface
                         (8, 11, 10, 9), #rightface
                        ]
                
                for v_co in verts:
                    bm.verts.new(v_co)
                
                for f_idx in faces:
                    bm.verts.ensure_lookup_table()
                    bm.faces.new([bm.verts[i] for i in f_idx])
                
                bm.to_mesh(mesh)
                
                mesh.update()
                
                fd.create_vertex_group_for_hooks(obj,[2,3,6,7,8,9,10,11],'X Dimension')
                fd.create_vertex_group_for_hooks(obj,[1,2,8,11,6,5],'Y Dimension')
                fd.create_vertex_group_for_hooks(obj,[4,5,6,7,10,11],'Z Dimension')
                fd.hook_vertex_group_to_object(obj,'X Dimension',self.previous_wall.obj_x)
                fd.hook_vertex_group_to_object(obj,'Y Dimension',self.previous_wall.obj_y)
                fd.hook_vertex_group_to_object(obj,'Z Dimension',self.previous_wall.obj_z)
                
                #THIS IS NEEDED FOR A RETURN WALL TO BE CREATED FOR 2D ELEVATION DRAWINGS
                return_obj = fd.create_cube_mesh('Return Wall',(fd.inches(.1),fd.inches(.2),size[2]))
                return_obj.parent = self.previous_wall.obj_bp
                return_obj.mv.type = 'CAGE'
                return_obj.location.x = self.previous_wall.obj_x.location.x
                fd.create_vertex_group_for_hooks(return_obj,[0,1,2,3,4,5,6,7],'X Dimension')
                fd.create_vertex_group_for_hooks(return_obj,[4,5,6,7],'Z Dimension')
                fd.hook_vertex_group_to_object(return_obj,'X Dimension',self.previous_wall.obj_x)
                fd.hook_vertex_group_to_object(return_obj,'Z Dimension',self.previous_wall.obj_z)
                self.previous_wall.obj_x.hide = True
                self.previous_wall.obj_y.hide = True
                self.previous_wall.obj_z.hide = True
                
    def set_type_value(self,event):
        if event.value == 'PRESS':
            if event.type == "ONE" or event.type == "NUMPAD_1":
                self.typed_value += "1"
            if event.type == "TWO" or event.type == "NUMPAD_2":
                self.typed_value += "2"
            if event.type == "THREE" or event.type == "NUMPAD_3":
                self.typed_value += "3"
            if event.type == "FOUR" or event.type == "NUMPAD_4":
                self.typed_value += "4"
            if event.type == "FIVE" or event.type == "NUMPAD_5":
                self.typed_value += "5"
            if event.type == "SIX" or event.type == "NUMPAD_6":
                self.typed_value += "6"
            if event.type == "SEVEN" or event.type == "NUMPAD_7":
                self.typed_value += "7"
            if event.type == "EIGHT" or event.type == "NUMPAD_8":
                self.typed_value += "8"
            if event.type == "NINE" or event.type == "NUMPAD_9":
                self.typed_value += "9"
            if event.type == "ZERO" or event.type == "NUMPAD_0":
                self.typed_value += "0"
            if event.type == "PERIOD" or event.type == "NUMPAD_PERIOD":
                last_value = self.typed_value[-1:]
                if last_value != ".":
                    self.typed_value += "."
            if event.type == 'BACK_SPACE':
                if self.typed_value != "":
                    self.typed_value = self.typed_value[:-1]
            
    def place_wall(self):
        self.wall.refresh_hook_modifiers()
        for child in self.wall.obj_bp.children:
            child.draw_type = 'TEXTURED'
        self.wall.obj_x.hide = True
        self.wall.obj_y.hide = True
        self.wall.obj_z.hide = True
        self.starting_point = (self.wall.obj_x.matrix_world[0][3], self.wall.obj_x.matrix_world[1][3], self.wall.obj_x.matrix_world[2][3])
        self.extend_wall()
        self.previous_wall = self.wall
        self.create_wall()
        self.typed_value = ""
        
    def event_is_place_wall(self,event):
        if event.type == 'LEFTMOUSE' and event.value == 'PRESS':
            return True
        elif event.type == 'NUMPAD_ENTER' and event.value == 'PRESS':
            return True
        elif event.type == 'RET' and event.value == 'PRESS':
            return True
        else:
            return False
        
    def event_is_cancel(self,event):
        if event.type == 'RIGHTMOUSE' and event.value == 'PRESS':
            return True
        elif event.type == 'ESC' and event.value == 'PRESS':
            return True
        else:
            return False
        
    def get_wall_count(self):
        wall_number = 0
        for obj in bpy.context.visible_objects:
            if obj.mv.type == "BPWALL":
                wall_number += 1
        return wall_number
            
    def modal(self, context, event):
        self.set_type_value(event)
        wall_length_text = str(fd.unit(round(self.wall.obj_x.location.x,4)))
        wall_length_unit = '"' if context.scene.unit_settings.system == 'IMPERIAL' else 'mm'
        context.area.header_text_set(text=self.header_text + '   (Current Wall Length = ' + wall_length_text + wall_length_unit + ')')
        context.window.cursor_set('PAINT_BRUSH')
        context.area.tag_redraw()
        selected_point, selected_obj = fd.get_selection_point(context,event,objects=[self.drawing_plane]) #Pass in Drawing Plane
        bpy.ops.object.select_all(action='DESELECT')
        if selected_obj:
            if event.ctrl:
                self.wall.obj_bp.constraints.clear()
                self.wall.obj_bp.location.x = selected_point[0]
                self.wall.obj_bp.location.y = selected_point[1]
                self.wall.obj_bp.location.z = 0
                self.starting_point = (self.wall.obj_bp.location.x, self.wall.obj_bp.location.y, 0)
            else:
                selected_obj.select = True
                self.position_wall(selected_point)
            
        if self.event_is_place_wall(event):
            self.place_wall()

        if event.type in {'MIDDLEMOUSE', 'WHEELUPMOUSE', 'WHEELDOWNMOUSE'}:
            return {'PASS_THROUGH'}
            
        if self.event_is_cancel(event):
            return self.cancel_drop(context,event)
            
        return {'RUNNING_MODAL'}
        
    def execute(self,context):
        wall_bp = fd.get_wall_bp(context.active_object)
        if wall_bp:
            self.previous_wall = fd.Wall(wall_bp)
            self.starting_point = (self.previous_wall.obj_x.matrix_world[0][3], self.previous_wall.obj_x.matrix_world[1][3], self.previous_wall.obj_x.matrix_world[2][3])
            
        self.create_wall()
        
        bpy.ops.mesh.primitive_plane_add()
        plane = context.active_object
        plane.location = (0,0,0)
        self.drawing_plane = context.active_object
        self.drawing_plane.draw_type = 'WIRE'
        self.drawing_plane.dimensions = (100,100,1)
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

class OPS_add_assembly(Operator):
    bl_idname = "fd_assembly.add_assembly"
    bl_label = "Empty Assembly"
    bl_description = "This operator adds a new empty assembly to the scene."
    bl_options = {'UNDO'}
    
    assembly_size = FloatVectorProperty(name="Group Size",
                                        default=(fd.inches(24),fd.inches(24),fd.inches(24)))
    
    @classmethod
    def poll(cls, context):
        return True
    
    def execute(self, context):
        group = fd.Assembly()
        group.create_assembly()
        group.obj_x.location.x = self.assembly_size[0]
        group.obj_y.location.y = self.assembly_size[1]
        group.obj_z.location.z = self.assembly_size[2]
        group.build_cage()
        bpy.ops.object.select_all(action='DESELECT')
        group.obj_bp.select = True
        context.scene.objects.active = group.obj_bp
        return {'FINISHED'}

class OPS_add_mesh_to_assembly(Operator):
    """ Since this looks to the context this should only be called from the ui.
    """
    bl_idname = "fd_assembly.add_mesh_to_assembly"
    bl_label = "Add Mesh To Assembly"
    bl_description = "This will add a mesh to the selected assembly"
    bl_options = {'UNDO'}
    
    mesh_name = StringProperty(name="Mesh Name",default="New Mesh")

    @classmethod
    def poll(cls, context):
        if context.active_object:
            obj_bp = fd.get_assembly_bp(context.active_object)
            if obj_bp:
                return True
        return False

    def execute(self, context):
        obj_bp = fd.get_assembly_bp(context.active_object)
        assembly = fd.Assembly(obj_bp)
        obj_bp = assembly.obj_bp
        dim_x = assembly.obj_x.location.x
        dim_y = assembly.obj_y.location.y
        dim_z = assembly.obj_z.location.z

        obj_mesh = fd.create_cube_mesh(self.mesh_name,(dim_x,dim_y,dim_z))
                
        if obj_mesh:
            obj_mesh.mv.name_object = self.mesh_name
            context.scene.objects.active = obj_mesh
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.normals_make_consistent(inside=False)
            bpy.ops.object.editmode_toggle()
            if obj_bp:
                obj_mesh.parent = obj_bp

            update_vector_groups(obj_bp)
            bpy.ops.fd_assembly.load_active_assembly_objects(object_name=obj_bp.name)
        return {'FINISHED'}

    def invoke(self,context,event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=fd.get_prop_dialog_width(400))

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "mesh_name")

class OPS_add_empty_to_assembly(Operator):
    """ Since this looks to the context this should only be called from the ui.
    """
    bl_idname = "fd_assembly.add_empty_to_assembly"
    bl_label = "Add Empty To Assembly"
    bl_description = "This will add an empty to the selected assembly"
    bl_options = {'UNDO'}
    
    use_as_mesh_hook = BoolProperty(name="Use As Mesh Hook",default=False)
    empty_name = StringProperty(name="Empty Name",default="New Empty")

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        obj_bp = fd.get_assembly_bp(context.active_object)

        #NOTE: Since Mesh hooks are maintained by object name
        #      You cannot have two emptyhooks with the same name.       
        for child in obj_bp.children:
            if child.type == 'EMPTY' and self.use_as_mesh_hook and child.mv.use_as_mesh_hook and child.mv.name_object == self.empty_name:
                bpy.ops.fd_general.error('INVOKE_DEFAULT',Message="A hook with that name already exists.")
                return {'CANCELLED'}
            
        #NOTE: Since Mesh hooks are maintained by object name
        #      These names are reserved the the visible prompts of the group
        if self.use_as_mesh_hook:
            if self.empty_name in {'Dimension X','Dimension Y','Dimension Z'}:
                bpy.ops.fd_general.error('INVOKE_DEFAULT',Message="That hook name are reserved for visible prompts")
                return {'CANCELLED'}
        
        bpy.ops.object.empty_add()
        obj_empty = context.active_object

        if obj_empty:
            obj_empty.empty_draw_size = fd.inches(1)
            obj_empty.mv.name_object = self.empty_name
            obj_empty.mv.use_as_mesh_hook = self.use_as_mesh_hook
            if obj_bp:
                obj_empty.parent = obj_bp
            
            context.scene.objects.active = obj_empty
            update_vector_groups(obj_bp)
            bpy.ops.fd_assembly.load_active_assembly_objects(object_name=obj_bp.name)
        return {'FINISHED'}

    def invoke(self,context,event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=fd.get_prop_dialog_width(400))

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "empty_name")
        layout.prop(self, "use_as_mesh_hook")
        
class OPS_add_curve_to_assembly(Operator):
    """ Since this looks to the context this should only be called from the ui.
    """
    bl_idname = "fd_assembly.add_curve_to_assembly"
    bl_label = "Add Curve To Assembly"
    bl_description = "This will add a curve to the selected assembly"
    bl_options = {'UNDO'}
    
    use_selected = BoolProperty(name="Use Selected",default=False)
    curve_name = StringProperty(name="Curve Name",default="New Curve")

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        obj_bp = fd.get_assembly_bp(context.active_object)
        group = fd.Assembly(obj_bp)
        dim_x = group.obj_x.location.x

        bpy.ops.curve.primitive_bezier_curve_add(enter_editmode=False)
        obj_curve = context.active_object
        obj_curve.data.show_handles = False
        
        obj_curve.data.splines[0].bezier_points[0].co = (0,0,0)
        obj_curve.data.splines[0].bezier_points[1].co = (dim_x,0,0)
        
        bpy.ops.object.editmode_toggle()
        bpy.ops.curve.select_all(action='SELECT')
        bpy.ops.curve.handle_type_set(type='VECTOR')
        bpy.ops.object.editmode_toggle()
        obj_curve.data.dimensions = '2D'
        
        if obj_curve:
            obj_curve.mv.name_object = self.curve_name
            obj_curve.parent = obj_bp
            bpy.ops.fd_assembly.load_active_assembly_objects(object_name=obj_bp.name)
        return {'FINISHED'}

    def invoke(self,context,event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=fd.get_prop_dialog_width(400))

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "curve_name")

class OPS_add_text_to_assembly(Operator):
    """ Since this looks to the context this should only be called from the ui.
    """
    bl_idname = "fd_assembly.add_text_to_assembly"
    bl_label = "Add Text To Assembly"
    bl_description = "This will add a text to the selected assembly"
    bl_options = {'UNDO'}

    text_name = StringProperty(name="Text Name",default="New Text")

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        obj_bp = fd.get_assembly_bp(context.active_object)

        bpy.ops.object.text_add()
        obj_text = context.active_object

        if obj_text:
            obj_text.mv.name_object = self.text_name

            if obj_bp:
                obj_text.parent = obj_bp
            
            context.scene.objects.active = obj_text
            bpy.ops.fd_group.load_active_group_objects(object_name=obj_bp.name)     
        return {'FINISHED'}

    def invoke(self,context,event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=fd.get_prop_dialog_width(400))

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "text_name")
    
class OPS_make_group_from_selected_assembly(Operator):
    bl_idname = "fd_assembly.make_group_from_selected_assembly"
    bl_label = "Make Group From Selected Assembly"
    bl_description = "This will create a group from the selected assembly"
    bl_options = {'UNDO'}
    
    assembly_name = StringProperty(name="Group Name",default = "New Group")
    
    @classmethod
    def poll(cls, context):
        obj_bp = fd.get_parent_assembly_bp(context.object)
        if obj_bp:
            return True
        else:
            return False

    def execute(self, context):
        obj_bp = fd.get_parent_assembly_bp(context.object)
        if obj_bp:
            list_obj = fd.get_child_objects(obj_bp)
            for obj in list_obj:
                obj.hide = False
                obj.hide_select = False
                obj.select = True
            bpy.ops.group.create(name=self.assembly_name)
            
            obj_bp.location = obj_bp.location
        return {'FINISHED'}

    def invoke(self,context,event):
        obj_bp = fd.get_parent_assembly_bp(context.object)
        if obj_bp:
            self.assembly_name = obj_bp.mv.name_object
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=fd.get_prop_dialog_width(400))

    def draw(self, context):
        layout = self.layout
        layout.prop(self,"assembly_name")

class OPS_select_selected_assembly_base_point(Operator):
    bl_idname = "fd_assembly.select_selected_assemby_base_point"
    bl_label = "Select Assembly Base Point"
    bl_options = {'UNDO'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        obj_bp = fd.get_parent_assembly_bp(obj)
        if obj_bp:
            return True
        else:
            return False

    def execute(self, context):
        obj = context.active_object
        obj_bp = fd.get_parent_assembly_bp(obj)
        if obj_bp:
            bpy.ops.object.select_all(action='DESELECT')
            obj_bp.hide = False
            obj_bp.hide_select = False
            obj_bp.select = True
            context.scene.objects.active = obj_bp
        return {'FINISHED'}

class OPS_delete_object_in_assembly(Operator):
    bl_idname = "fd_assembly.delete_object_in_assembly"
    bl_label = "Delete Object in Assembly"
    bl_options = {'UNDO'}
    
    object_name = StringProperty(name="Object Name")
    
    @classmethod
    def poll(cls, context):
        return True
    
    def execute(self, context):
        obj = bpy.data.objects[self.object_name]
        obj_bp = obj.parent
        bpy.ops.object.select_all(action='DESELECT')
        obj.select = True
        context.scene.objects.active = obj
        bpy.ops.object.delete()
        bpy.ops.fd_assembly.load_active_assembly_objects(object_name=obj_bp.name)
        obj_bp.select = True
        context.scene.objects.active = obj_bp #Set Base Point as active object so panel doesn't disappear
        return {'FINISHED'}
    
class OPS_load_active_assembly_objects(Operator):
    bl_idname = "fd_assembly.load_active_assembly_objects"
    bl_label = "Load Active Assembly Objects"
    bl_options = {'UNDO'}
    
    object_name = StringProperty(name="Object Name")
    
    @classmethod
    def poll(cls, context):
        return True
    
    def execute(self, context):
        obj = bpy.data.objects[self.object_name]
        scene = context.scene.mv
        
        for current_obj in scene.children_objects:
            scene.children_objects.remove(0)
        
        group = fd.Assembly(obj)
        group.set_object_names()
        
        scene.active_object_name = obj.name
        for child in obj.children:
            if child.mv.type not in {'VPDIMX','VPDIMY','VPDIMZ','CAGE'}:
                list_obj = scene.children_objects.add()
                list_obj.name = child.name
            
        return {'FINISHED'}
    
class OPS_rename_assembly(Operator):
    bl_idname = "fd_assembly.rename_assembly"
    bl_label = "Rename Assembly"
    bl_options = {'UNDO'}
    
    object_name = StringProperty(name="Object Name")
    new_name = StringProperty(name="New Name",default="")

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        obj_bp = bpy.data.objects[self.object_name]
        obj_bp.mv.name_object = self.new_name
        group = fd.Assembly(obj_bp)
        group.set_object_names()
        return {'FINISHED'}

    def invoke(self,context,event):
        wm = context.window_manager
        obj_bp = bpy.data.objects[self.object_name]
        self.new_name = obj_bp.mv.name_object
        return wm.invoke_props_dialog(self, width=fd.get_prop_dialog_width(400))

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "new_name")

class OPS_delete_selected_assembly(Operator):
    bl_idname = "fd_assembly.delete_selected_assembly"
    bl_label = "Delete Selected Assembly"
    bl_options = {'UNDO'}
    
    object_name = StringProperty(name="Object Name")
    
    @classmethod
    def poll(cls, context):
        obj = context.active_object
        obj_bp = fd.get_parent_assembly_bp(obj)
        if obj_bp:
            return True
        else:
            return False
    
    def get_bp(self,context):
        if self.object_name != "":
            return bpy.data.objects[self.object_name]
        else:
            obj = context.object
            return fd.get_parent_assembly_bp(obj)
    
    def get_boolean_objects(self,obj_bp,bool_list):
        for child in obj_bp.children:
            if child.mv.use_as_bool_obj:
                bool_list.append(child)
            if len(child.children) > 0:
                self.get_boolean_objects(child, bool_list)
    
    def execute(self, context):
        obj_bp = self.get_bp(context)
        self.make_opening_available(obj_bp)
        bool_list = []
        self.get_boolean_objects(obj_bp, bool_list)
        for bool_obj in bool_list:
            self.remove_referenced_modifiers(context, bool_obj)
        obj_list = []
        obj_list = fd.get_child_objects(obj_bp,obj_list)
        fd.delete_obj_list(obj_list)
        return {'FINISHED'}

    def remove_referenced_modifiers(self,context,obj_ref):
        """ This is removes boolean modifers that use this object
            mainly used to remove boolean modifiers for walls.
        """
        for obj in context.scene.objects:
            if obj.mv.type == 'NONE' and obj.type == 'MESH':
                for mod in obj.modifiers:
                    if mod.type == 'BOOLEAN':
                        if mod.object == obj_ref:
                            obj.modifiers.remove(mod)

    def make_opening_available(self,obj_bp):
        insert = fd.Assembly(obj_bp)
        if obj_bp.parent:
            for child in obj_bp.parent.children:
                if child.cabinetlib.type_group == 'OPENING' and insert.obj_bp.location == child.location:
                    if insert.obj_bp.cabinetlib.placement_type == 'SPLITTER':
                        child.cabinetlib.interior_open = True
                        child.cabinetlib.exterior_open = True
                        break
                    if insert.obj_bp.cabinetlib.placement_type == 'INTERIOR':
                        child.cabinetlib.interior_open = True
                        break
                    if insert.obj_bp.cabinetlib.placement_type == 'EXTERIOR':
                        child.cabinetlib.exterior_open = True
                        break

    def invoke(self,context,event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=fd.get_prop_dialog_width(300))

    def draw(self, context):
        obj_bp = self.get_bp(context)
        layout = self.layout
        layout.label("Assembly Name: " + obj_bp.mv.name_object)

class OPS_copy_selected_assembly(Operator):
    bl_idname = "fd_assembly.copy_selected_assembly"
    bl_label = "Copy Selected Assembly"
    bl_options = {'UNDO'}
    
    @classmethod
    def poll(cls, context):
        obj = context.active_object
        obj_bp = fd.get_parent_assembly_bp(obj)
        if obj_bp:
            return True
        else:
            return False
    
    def execute(self, context):
        obj_bools = []
        obj = context.object
        obj_bp = fd.get_parent_assembly_bp(obj)
        if obj_bp:
            obj_list = []
            obj_list = fd.get_child_objects(obj_bp,obj_list)
            bpy.ops.object.select_all(action='DESELECT')
            for obj in obj_list:
                obj.hide = False
                obj.select = True
            
            bpy.ops.object.duplicate()
            
            for obj in context.selected_objects:
                if obj.type == 'EMPTY':
                    obj.hide = True
                #COLLECT BOOLEAN OBJECTS FROM GROUP
                if obj.mv.use_as_bool_obj:
                    obj_bools.append(obj)
                obj.location = obj.location
            
            for obj in obj_list:
                if obj.type == 'EMPTY':
                    obj.hide = True
                obj.location = obj.location
            bpy.ops.object.select_all(action='DESELECT')
            
            #ASSIGN BOOLEAN MODIFIERS TO WALL
            if obj_bp.parent:
                if obj_bp.parent.mv.type == 'BPWALL':
                    wall = fd.Wall(obj_bp.parent)
                    mesh = wall.get_wall_mesh()
                    for obj_bool in obj_bools:
                        mod = mesh.modifiers.new(obj_bool.name,'BOOLEAN')
                        mod.object = obj_bool
                        mod.operation = 'DIFFERENCE'
            
            obj_bp.select = True
            context.scene.objects.active = obj_bp
            
        return {'FINISHED'}

class OPS_connect_mesh_to_hooks_in_assembly(Operator):
    bl_idname = "fd_assembly.connect_meshes_to_hooks_in_assembly"
    bl_label = "Connect Mesh to Hooks In Assembly"
    bl_options = {'UNDO'}
    
    object_name = StringProperty(name="Object Name")
    
    @classmethod
    def poll(cls, context):
        return True
    
    def execute(self, context):
        obj = bpy.data.objects[self.object_name]
        group_bp = fd.get_assembly_bp(obj)
        wall_bp = fd.get_wall_bp(obj)
        if group_bp:
            group = fd.Assembly(group_bp)
        elif wall_bp:
            group = fd.Wall(wall_bp)
        hooklist = []
        for child in group.obj_bp.children:
            if child.type == 'EMPTY'  and child.mv.use_as_mesh_hook:
                hooklist.append(child)
        
        if obj.mode == 'EDIT':
            bpy.ops.object.editmode_toggle()
        
        fd.apply_hook_modifiers(obj)
        for vgroup in obj.vertex_groups:
            if vgroup.name == 'X Dimension':
                fd.hook_vertex_group_to_object(obj,'X Dimension',group.obj_x)
            elif vgroup.name == 'Y Dimension':
                fd.hook_vertex_group_to_object(obj,'Y Dimension',group.obj_y)
            elif vgroup.name == 'Z Dimension':
                fd.hook_vertex_group_to_object(obj,'Z Dimension',group.obj_z)
            else:
                for hook in hooklist:
                    if hook.mv.name_object == vgroup.name:
                        fd.hook_vertex_group_to_object(obj,vgroup.name,hook)
                
        obj.lock_location = (True,True,True)
                
        return {'FINISHED'}

class OPS_make_static_product(Operator):
    """ This will make the currect product static.
    """
    bl_idname = "cabinetlib.make_static_product"
    bl_label = "Make Static Product"
    bl_description = "This removes all hook modifiers for the product"
    bl_options = {'UNDO'}
    
    object_name = StringProperty(name="Object Name")
    
    def apply_modifiers_for_obj(self,obj):
        if obj.type == 'MESH':
            bpy.ops.fd_object.apply_hook_modifiers(object_name=obj.name)
            obj.lock_location = (False,False,False)
        for child in obj.children:
            self.apply_modifiers_for_obj(child)
    
    def execute(self, context):
        obj_bp = bpy.data.objects[self.object_name]
        
        for child in obj_bp.children:
            self.apply_modifiers_for_obj(child)

        return {'FINISHED'}

class OPS_select_product(Operator):
    bl_idname = "cabinetlib.select_product"
    bl_label = "Select Product"
    
    object_name = StringProperty(name="Object Name")
    
    def execute(self, context):
        obj = bpy.data.objects[self.object_name]
        obj_list = []
        obj_list = fd.get_child_objects(obj,obj_list)
        bpy.ops.object.select_all(action='DESELECT')
        for obj in obj_list:
            obj.hide = False
            obj.select = True
        return {'FINISHED'}

class OPS_display_selected_wall(Operator):
    bl_idname = "fd_assembly.dislay_selected_wall"
    bl_label = "Display Selected Wall"
    
    def execute(self, context):
        obj = context.active_object
        wall_bp = fd.get_wall_bp(obj)
        wall_bps = []
        for obj in context.visible_objects:
            if obj.mv.type == 'BPWALL':
                wall_bps.append(obj)
                
        for wall in wall_bps:
            if wall != wall_bp:
                children = []
                children = fd.get_child_objects(wall)
                
                for child in children:
                    child.hide = True
            else:
                wall_assembly = fd.Assembly(wall)
                wall_assembly.obj_x.select = True
                wall_assembly.obj_y.select = True
                wall_assembly.obj_z.select = True
        
        bpy.ops.view3d.view_selected()
        
        return {'FINISHED'}

class OPS_hide_wall(Operator):
    bl_idname = "fd_assembly.hide_wall"
    bl_label = "Hide Wall"
    
    wall_bp_name = StringProperty("Wall BP Name",default="")
    
    def execute(self, context):
        if self.wall_bp_name in context.scene.objects:
            obj = context.scene.objects[self.wall_bp_name]
        else:
            obj = context.active_object
            
        wall_bp = fd.get_wall_bp(obj)
        
        children = fd.get_child_objects(wall_bp)
        
        for child in children:
            child.hide = True
        
        wall_bp.hide = True
        
        return {'FINISHED'}

class OPS_show_wall(Operator):
    bl_idname = "fd_assembly.show_wall"
    bl_label = "Show Wall"
    
    wall_bp_name = StringProperty("Wall BP Name",default="")
    
    def execute(self, context):
        if self.wall_bp_name in context.scene.objects:
            obj = context.scene.objects[self.wall_bp_name]
        else:
            obj = context.active_object
            
        wall_bp = fd.get_wall_bp(obj)
        
        children = fd.get_child_objects(wall_bp)
        
        for child in children:
            if child.type != 'EMPTY':
                child.hide = False
        
        wall_bp.hide = False
        
        return {'FINISHED'}

class OPS_display_all_walls(Operator):
    bl_idname = "fd_assembly.display_all_walls"
    bl_label = "Display All Walls"
    
    def execute(self, context):
        wall_bps = []
        for obj in bpy.data.objects:
            if obj.mv.type == 'BPWALL':
                wall_bps.append(obj)
                
        for wall in wall_bps:
            children = fd.get_child_objects(wall)
            
            for child in children:
                if child.type == 'MESH' and not child.mv.type == 'CAGE':
                    child.hide = False
            wall.location = wall.location
        return {'FINISHED'}
    
#------REGISTER
classes = [
           OPS_add_wall,
           OPS_draw_walls,
           OPS_add_assembly,
           OPS_add_mesh_to_assembly,
           OPS_add_empty_to_assembly,
           OPS_add_curve_to_assembly,
           OPS_add_text_to_assembly,
           OPS_make_group_from_selected_assembly,
           OPS_select_selected_assembly_base_point,
           OPS_delete_object_in_assembly,
           OPS_load_active_assembly_objects,
           OPS_rename_assembly,
           OPS_delete_selected_assembly,
           OPS_copy_selected_assembly,
           OPS_connect_mesh_to_hooks_in_assembly,
           OPS_make_static_product,
           OPS_select_product,
           OPS_display_selected_wall,
           OPS_display_all_walls,
           OPS_hide_wall,
           OPS_show_wall
           ]

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

if __name__ == "__main__":
    register()
