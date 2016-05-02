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
import bmesh
from bpy_extras import view3d_utils, object_utils

import math
import mathutils
import os
import blf
import bgl
import inspect
from bpy.app.translations import pgettext_iface as iface_ #for decimate modifier
#Dimension Rendering
import sys
import bpy_extras.image_utils as img_utils

import xml.etree.ElementTree as ET

from bpy.types import PropertyGroup

LIBRARY_PATH_FILENAME = "fd_paths.xml"

class enums():
    enum_library_types = [('SCENE',"Scenes","Scenes"),
                          ('PRODUCT',"Products","Products"),
                          ('INSERT',"Inserts","Inserts"),
                          ('ASSEMBLY',"Assemblies","Assemblies"),
                          ('OBJECT',"Objects","Objects"),
                          ('MATERIAL',"Materials","Materials"),
                          ('WORLD',"Worlds","Worlds")]
    
    enum_object_tabs = [('INFO',"","Show the Main Information"),
                        ('DISPLAY',"","Show Options for how the Object is Displayed"),
                        ('MATERIAL',"","Show the materials assign to the object"),
                        ('CONSTRAINTS',"","Show the constraints assigned to the object"),
                        ('MODIFIERS',"","Show the modifiers assigned to the object"),
                        ('MESHDATA',"","Show the Mesh Data Information"),
                        ('CURVEDATA',"","Show the Curve Data Information"),
                        ('TEXTDATA',"","Show the Text Data Information"),
                        ('EMPTYDATA',"","Show the Empty Data Information"),
                        ('LIGHTDATA',"","Show the Light Data Information"),
                        ('CAMERADATA',"","Show the Camera Data Information"),
                        ('DRIVERS',"","Show the Drivers assigned to the Object"),
                        ('TOKENS',"","Show the Tokens that are assigned to the Object")]

    enum_group_tabs = [('INFO',"Main","Show the Main Info Page"),
                       ('SETTINGS',"","Show the Settings Page"),
                       ('PROMPTS',"Prompts","Show the Prompts Page"),
                       ('OBJECTS',"Objects","Show Objects"),
                       ('DRIVERS',"Drivers","Show the Driver Formulas")]
    
    enum_calculator_type = [('XDIM',"X Dimension","Calculate the X Dimension"),
                            ('YDIM',"Y Dimension","Calculate the Y Dimension"),
                            ('ZDIM',"Z Dimension","Calculate the Z Dimension")]
    
    enum_prompt_tab_types = [('VISIBLE',"Visible","Visible tabs are always displayed"),
                             ('HIDDEN',"Hidden","Hidden tabs are not shown in the right click menu"),
                             ('CALCULATOR',"Calculator","Use to calculate sizes of opening")]
    
    enum_prompt_types = [('NUMBER',"Number","Number"),
                         ('QUANTITY',"Quantity","Quantity"),
                         ('COMBOBOX',"Combo Box","Combo Box"),
                         ('CHECKBOX',"Check Box","Check Box"),
                         ('TEXT',"Text","Text"),
                         ('DISTANCE',"Distance","Distance"),
                         ('ANGLE',"Angle","Angle"),
                         ('PERCENTAGE',"Percentage","Percentage"),
                         ('PRICE',"Price","Enter Price Prompt")]

    enum_object_types = [('NONE',"None","None"),
                         ('CAGE',"CAGE","Cage used to represent the bounding area of an assembly"),
                         ('VPDIMX',"Visible Prompt X Dimension","Visible prompt control in the 3D viewport"),
                         ('VPDIMY',"Visible Prompt Y Dimension","Visible prompt control in the 3D viewport"),
                         ('VPDIMZ',"Visible Prompt Z Dimension","Visible prompt control in the 3D viewport"),
                         ('EMPTY1',"Empty1","EMPTY1"),
                         ('EMPTY2',"Empty2","EMPTY2"),
                         ('EMPTY3',"Empty3","EMPTY3"),
                         ('BPWALL',"Wall Base Point","Parent object of a wall"),
                         ('BPASSEMBLY',"Base Point","Parent object of an assembly"),
                         ('VISDIM_A', "Visual Dimension A", "Anchor Point for Visual Dimension"),
                         ('VISDIM_B', "Visual Dimension B", "End Point for Visual Dimension")]
    
    enum_group_drivers_tabs = [('LOC_X',"Location X","Location X"),
                               ('LOC_Y',"Location Y","Location Y"),
                               ('LOC_Z',"Location Z","Location Z"),
                               ('ROT_X',"Rotation X","Rotation X"),
                               ('ROT_Y',"Rotation Y","Rotation Y"),
                               ('ROT_Z',"Rotation Z","Rotation Z"),
                               ('DIM_X',"Dimension X","Dimension X"),
                               ('DIM_Y',"Dimension Y","Dimension Y"),
                               ('DIM_Z',"Dimension Z","Dimension Z"),
                               ('PROMPTS',"Prompts","Prompts")]

    enum_render_type = [('PRR','Photo Realistic Render','Photo Realistic Render'),
                        ('NPR','Line Drawing','Non-Photo Realistic Render')]    
    
    enum_modifiers = [('ARRAY', "Array Modifier", "Array Modifier", 'MOD_ARRAY', 0),
                      ('BEVEL', "Bevel Modifier", "Bevel Modifier", 'MOD_BEVEL', 1),
                      ('BOOLEAN', "Boolean Modifier", "Boolean Modifier", 'MOD_BOOLEAN', 2),
                      ('CURVE', "Curve Modifier", "Curve Modifier", 'MOD_CURVE', 3),
                      ('DECIMATE', "Decimate Modifier", "Decimate Modifier", 'MOD_DECIM', 4),
                      ('EDGE_SPLIT', "Edge Split Modifier", "Edge Split Modifier", 'MOD_EDGESPLIT', 5),
                      ('HOOK', "Hook Modifier", "Hook Modifier", 'HOOK', 6),
                      ('MASK', "Mask Modifier", "Mask Modifier", 'MOD_MASK', 7),
                      ('MIRROR', "Mirror Modifier", "Mirror Modifier", 'MOD_MIRROR', 8),
                      ('SOLIDIFY', "Solidify Modifier", "Solidify Modifier", 'MOD_SOLIDIFY', 9),
                      ('SUBSURF', "Subsurf Modifier", "Subsurf Modifier", 'MOD_SUBSURF', 10),
                      ('SKIN', "Skin Modifier", "Skin Modifier", 'MOD_SKIN', 11),
                      ('SIMPLE_DEFORM', "Simple Deform Modifier", "Simple Deform Modifier", 'MOD_SIMPLEDEFORM', 12),
                      ('TRIANGULATE', "Triangulate Modifier", "Triangulate Modifier", 'MOD_TRIANGULATE', 13),
                      ('WIREFRAME', "Wireframe Modifier", "Wireframe Modifier", 'MOD_WIREFRAME', 14)]
    
    enum_constraints = [('COPY_LOCATION', "Copy Location", "Copy Location", 'CONSTRAINT_DATA', 0),
                        ('COPY_ROTATION', "Copy Rotation", "Copy Rotation", 'CONSTRAINT_DATA', 1),
                        ('COPY_SCALE', "Copy Scale", "Copy Scale", 'CONSTRAINT_DATA', 2),
                        ('COPY_TRANSFORMS', "Copy Transforms", "Copy Transforms", 'CONSTRAINT_DATA', 3),
                        ('LIMIT_DISTANCE', "Limit Distance", "Limit Distance", 'CONSTRAINT_DATA', 4),
                        ('LIMIT_LOCATION', "Limit Location", "Limit Location", 'CONSTRAINT_DATA', 5),
                        ('LIMIT_ROTATION', "Limit Rotation", "Limit Rotation", 'CONSTRAINT_DATA', 6),
                        ('LIMIT_SCALE', "Limit Scale", "Limit Scale", 'CONSTRAINT_DATA', 7)]  
    
    enum_machine_tokens = [('NONE',"None","None",'SCULPTMODE_HLT', 0),
                           ('CONST',"CONST","CONST", 'SCULPTMODE_HLT', 1),
                           ('HOLES',"HOLES","HOLES", 'SCULPTMODE_HLT', 2),
                           ('SHLF',"SHLF","SHLF", 'SCULPTMODE_HLT', 3),
                           ('SHELF',"SHELF","SHELF", 'SCULPTMODE_HLT', 4),
                           ('SHELFSTD',"SHELFSTD","SHELFSTD", 'SCULPTMODE_HLT', 5),
                           ('DADO',"DADO","DADO", 'SCULPTMODE_HLT', 6),
                           ('SAW',"SAW","SAW", 'SCULPTMODE_HLT', 7),
                           ('SLIDE',"SLIDE","SLIDE", 'SCULPTMODE_HLT', 8),
                           ('CAMLOCK',"CAMLOCK","CAMLOCK", 'SCULPTMODE_HLT', 9),
                           ('MITER',"MITER","MITER", 'SCULPTMODE_HLT', 10),
                           ('BORE',"BORE","BORE", 'SCULPTMODE_HLT', 11)]   
    
class Assembly():
    
    """ Type:bpy.types.Object - base point of the assembly """
    obj_bp = None
    
    """ Type:bpy.types.Object - x dimension of the assembly """
    obj_x = None
    
    """ Type:bpy.types.Object - y dimension of the assembly """
    obj_y = None
    
    """ Type:bpy.types.Object - z dimension of the assembly """
    obj_z = None

    def __init__(self,obj_bp=None):
        """ Assembly Constructor. If you want to create an instance of
            an existing Assembly then pass in the base point of the assembly 
            in the obj_bp parameter
        """
        if obj_bp:
            self.obj_bp = obj_bp
            for child in obj_bp.children:
                if child.mv.type == 'VPDIMX':
                    self.obj_x = child
                if child.mv.type == 'VPDIMY':
                    self.obj_y = child
                if child.mv.type == 'VPDIMZ':
                    self.obj_z = child
                if self.obj_bp and self.obj_x and self.obj_y and self.obj_z:
                    break

    def create_assembly(self):
        """ This creates the basic structure for an assembly
            This must be called first when creating an assembly 
            from a script
        """
        bpy.ops.object.select_all(action='DESELECT')
        verts = [(0, 0, 0)]
        mesh = bpy.data.meshes.new("Base Point")
        bm = bmesh.new()
        for v_co in verts:
            bm.verts.new(v_co)
        bm.to_mesh(mesh)
        mesh.update()
        obj_base = object_utils.object_data_add(bpy.context,mesh)
        obj_parent = obj_base.object
        obj_parent.location = (0,0,0)
        obj_parent.mv.type = 'BPASSEMBLY'
        obj_parent.mv.name_object = 'New Assembly'

        bpy.ops.object.empty_add()
        obj_x = bpy.context.active_object
        obj_x.name = "VPDIMX"
        obj_x.location = (0,0,0)
        obj_x.mv.type = 'VPDIMX'
        obj_x.lock_location[1] = True
        obj_x.lock_location[2] = True
        obj_x.parent = obj_parent

        bpy.ops.object.empty_add()
        obj_y = bpy.context.active_object
        obj_y.name = "VPDIMY"
        obj_y.location = (0,0,0)
        obj_y.mv.type = 'VPDIMY'
        obj_y.lock_location[0] = True
        obj_y.lock_location[2] = True
        obj_y.parent = obj_parent

        bpy.ops.object.empty_add()
        obj_z = bpy.context.active_object
        obj_z.name = "VPDIMZ"
        obj_z.location = (0,0,0)
        obj_z.mv.type = 'VPDIMZ'
        obj_z.lock_location[0] = True
        obj_z.lock_location[1] = True
        obj_z.parent = obj_parent
        
        self.obj_bp = obj_parent
        self.obj_x = obj_x
        self.obj_y = obj_y
        self.obj_z = obj_z
        
        obj_x.location.x = inches(10)
        obj_y.location.y = inches(10)
        obj_z.location.z = inches(10)
        
        self.set_object_names()
    
    def build_cage(self):
        """ This builds the cage object which is a cube that
            visually represents volume of the assembly.
        """
        if self.obj_bp and self.obj_x and self.obj_y and self.obj_z:
            size = (self.obj_x.location.x, self.obj_y.location.y, self.obj_z.location.z)
            obj_cage = create_cube_mesh('CAGE',size)
            obj_cage.mv.name_object = 'CAGE'
            obj_cage.location = (0,0,0)
            obj_cage.parent = self.obj_bp
            obj_cage.mv.type = 'CAGE'

            create_vertex_group_for_hooks(obj_cage,[2,3,6,7],'X Dimension')
            create_vertex_group_for_hooks(obj_cage,[1,2,5,6],'Y Dimension')
            create_vertex_group_for_hooks(obj_cage,[4,5,6,7],'Z Dimension')
            hook_vertex_group_to_object(obj_cage,'X Dimension',self.obj_x)
            hook_vertex_group_to_object(obj_cage,'Y Dimension',self.obj_y)
            hook_vertex_group_to_object(obj_cage,'Z Dimension',self.obj_z)
            
            obj_cage.draw_type = 'WIRE'
            obj_cage.hide_select = True
            obj_cage.lock_location = (True,True,True)
            obj_cage.lock_rotation = (True,True,True)
            obj_cage.cycles_visibility.camera = False
            obj_cage.cycles_visibility.diffuse = False
            obj_cage.cycles_visibility.glossy = False
            obj_cage.cycles_visibility.transmission = False
            obj_cage.cycles_visibility.shadow = False
            return obj_cage

    def get_cage(self):
        """ This gets the cage for an assembly. If the cage cannot be found
            then a new one is create and returned by the function
        """
        for child in self.obj_bp.children:
            if child.mv.type == 'CAGE':
                return child
        return self.build_cage()

    def get_var(self,data_path,var_name="",transform_space='WORLD_SPACE',transform_type='LOC_X'):
        """ This returns a variable which can be used in python expressions
            arg1: data_path the data path to retrieve the variable from there are 
                  reserved names that can be used.
                  dim_x = X Dimension of the Assembly
                  dim_y = Y Dimension of the Assembly
                  dim_z = Z Dimension of the Assembly
                  loc_x = X Location of the Assembly
                  loc_y = Y Location of the Assembly
                  loc_z = Z Location of the Assembly
                  rot_x = X Rotation of the Assembly
                  rot_y = Y Rotation of the Assembly
                  rot_z = Z Rotation of the Assembly
                  world_loc_x = X Location of the Assembly in world space
                  world_loc_y = Y Location of the Assembly in world space
                  world_loc_z = Z Location of the Assembly in world space
            arg2: var_name the variable name to use for the returned variable. If 
                  an empty string is passed in then the data_path is used as the
                  variable name. all spaces are replaced with the underscore charcter
            arg3: (TODO: DELETE THIS IS BEING PASSED IN THE DATAPATH) transform_space ENUM in ('WORLD_SPACE','TRANSFORM_SPACE','LOCAL_SPACE')
                  only used if calculating world space
            arg4: (TODO: DELETE THIS IS BEING PASSED IN THE DATAPATH)
        """
        if var_name == "":
            var_name = data_path.replace(" ","_")
        if data_path == 'dim_x':
            return Variable(self.obj_x,'location.x',var_name)
        elif data_path == 'dim_y':
            return Variable(self.obj_y,'location.y',var_name)
        elif data_path == 'dim_z':
            return Variable(self.obj_z,'location.z',var_name)
        elif data_path == 'loc_x':
            return Variable(self.obj_bp,'location.x',var_name)
        elif data_path == 'loc_y':
            return Variable(self.obj_bp,'location.y',var_name)
        elif data_path == 'loc_z':
            return Variable(self.obj_bp,'location.z',var_name)
        elif data_path == 'world_loc_x':
            return Variable(self.obj_bp,'matrix_world[0][3]',var_name,var_type='TRANSFORMS',transform_space=transform_space,transform_type=transform_type)
        elif data_path == 'world_loc_y':
            return Variable(self.obj_bp,'matrix_world[1][3]',var_name,var_type='TRANSFORMS',transform_space=transform_space,transform_type=transform_type)
        elif data_path == 'world_loc_z':
            return Variable(self.obj_bp,'matrix_world[2][3]',var_name,var_type='TRANSFORMS',transform_space=transform_space,transform_type=transform_type)
        elif data_path == 'rot_x':
            return Variable(self.obj_bp,'rotation_euler.x',var_name)
        elif data_path == 'rot_y':
            return Variable(self.obj_bp,'rotation_euler.y',var_name)
        elif data_path == 'rot_z':
            return Variable(self.obj_bp,'rotation_euler.z',var_name)
        else:
            prompt_path = self.get_prompt_data_path(data_path)
            if prompt_path:
                return Variable(self.obj_bp,prompt_path,var_name)
            else:
                return Variable(self.obj_bp,data_path,var_name)
        
    def get_prompt_data_path(self,prompt_name):
        for prompt in self.obj_bp.mv.PromptPage.COL_Prompt:
            if prompt.name == prompt_name:
                if prompt.Type == 'NUMBER':
                    return 'mv.PromptPage.COL_Prompt["' + prompt_name + '"].NumberValue'
                if prompt.Type == 'QUANTITY':
                    return 'mv.PromptPage.COL_Prompt["' + prompt_name + '"].QuantityValue'
                if prompt.Type == 'COMBOBOX':
                    return 'mv.PromptPage.COL_Prompt["' + prompt_name + '"].EnumIndex'
                if prompt.Type == 'CHECKBOX':
                    return 'mv.PromptPage.COL_Prompt["' + prompt_name + '"].CheckBoxValue'
                if prompt.Type == 'TEXT':
                    return 'mv.PromptPage.COL_Prompt["' + prompt_name + '"].TextValue'
                if prompt.Type == 'DISTANCE':
                    return 'mv.PromptPage.COL_Prompt["' + prompt_name + '"].DistanceValue'
                if prompt.Type == 'ANGLE':
                    return 'mv.PromptPage.COL_Prompt["' + prompt_name + '"].AngleValue'
                if prompt.Type == 'PERCENTAGE':
                    return 'mv.PromptPage.COL_Prompt["' + prompt_name + '"].PercentageValue'
                if prompt.Type == 'PRICE':
                    return 'mv.PromptPage.COL_Prompt["' + prompt_name + '"].PriceValue'
        
    def delete_cage(self):
        list_obj_cage = []
        for child in self.obj_bp.children:
            if child.mv.type == 'CAGE':
                list_obj_cage.append(child)
                
        delete_obj_list(list_obj_cage)

    def replace(self,smart_group):
        copy_drivers(self.obj_bp,smart_group.obj_bp)
        copy_drivers(self.obj_x,smart_group.obj_x)
        copy_drivers(self.obj_y,smart_group.obj_y)
        copy_drivers(self.obj_z,smart_group.obj_z)
        obj_list = []
        obj_list.append(self.obj_bp)
        for child in self.obj_bp.children:
            obj_list.append(child)
        delete_obj_list(obj_list)

    def set_object_names(self):
        group_name = self.obj_bp.mv.name_object
        self.obj_bp.name = self.obj_bp.mv.type + "." + self.obj_bp.mv.name_object
        for child in self.obj_bp.children:
            if child.mv.type != 'NONE':
                if child.mv.name_object != "":
                    child.name = child.mv.type + "." + group_name + "." + child.mv.name_object
                else:
                    child.name = child.mv.type + "." + group_name
            else:
                if child.mv.name_object != "":
                    child.name = child.type + "." + group_name + "." + child.mv.name_object
                else:
                    child.name = child.type + "." + group_name

    def add_tab(self,name="",tab_type='VISIBLE',calc_type="XDIM"):
        tab = self.obj_bp.mv.PromptPage.COL_MainTab.add()
        tab.name = name
        tab.type = tab_type
        if tab_type == 'CALCULATOR':
            tab.calculator_type = calc_type

    def number_of_visible_prompt_tabs(self):
        number_of_tabs = 0
        for tab in self.obj_bp.mv.PromptPage.COL_MainTab:
            if tab.type == 'VISIBLE':
                number_of_tabs += 1
        return number_of_tabs

    def get_prompt(self,prompt_name):
        if prompt_name in self.obj_bp.mv.PromptPage.COL_Prompt:
            return self.obj_bp.mv.PromptPage.COL_Prompt[prompt_name]

    def add_prompt(self,name="",prompt_type='DISTANCE',value=False,lock=False,tab_index=0,items=[],columns=1,equal=False,export=False):
        prompt = self.obj_bp.mv.PromptPage.COL_Prompt.add()
        prompt.name = name
        prompt.Type = prompt_type
        prompt.lock_value = lock
        prompt.TabIndex = tab_index
        prompt.equal = equal # Only for calculators
        prompt.export = export
        if prompt.Type == 'NUMBER':
            prompt.NumberValue = value
        if prompt.Type == 'QUANTITY':
            prompt.QuantityValue = value
        if prompt.Type == 'COMBOBOX':
            prompt.EnumIndex = value
            for combo_box_item in items:
                enum_item = prompt.COL_EnumItem.add()
                enum_item.name = combo_box_item
            prompt.columns =  columns
        if prompt.Type == 'CHECKBOX':
            prompt.CheckBoxValue = value
        if prompt.Type == 'TEXT':
            prompt.TextValue = value
        if prompt.Type == 'DISTANCE':
            prompt.DistanceValue = value
        if prompt.Type == 'ANGLE':
            prompt.AngleValue = value
        if prompt.Type == 'PERCENTAGE':
            prompt.PercentageValue = value
        if prompt.Type == 'PRICE':
            prompt.PriceValue = value

    def calc_width(self):
        """ Calculates the width of the group based on the rotation
            Used to determine collisions for rotated groups
        """
        return math.cos(self.obj_bp.rotation_euler.z) * self.obj_x.location.x
    
    def calc_depth(self):
        """ Calculates the depth of the group based on the rotation
            Used to determine collisions for rotated groups
        """
        #TODO: This not correct
        if self.obj_bp.rotation_euler.z < 0:
            return math.fabs(self.obj_x.location.x)
        else:
            return math.fabs(self.obj_y.location.y)
    
    def calc_x(self):
        """ Calculates the x location of the group based on the rotation
            Used to determine collisions for rotated groups
        """
        return math.sin(self.obj_bp.rotation_euler.z) * self.obj_y.location.y

    def refresh_hook_modifiers(self):
        for child in self.obj_bp.children:
            if child.type == 'MESH':
                bpy.ops.fd_object.apply_hook_modifiers(object_name=child.name)
                bpy.ops.fd_assembly.connect_meshes_to_hooks_in_assembly(object_name=child.name)

    def has_height_collision(self,group):
        """ Determines if this group will collide in the z with 
            the group that is passed in arg 2
        """

        if self.obj_bp.matrix_world[2][3] > self.obj_z.matrix_world[2][3]:
            grp1_z_1 = self.obj_z.matrix_world[2][3]
            grp1_z_2 = self.obj_bp.matrix_world[2][3]
        else:
            grp1_z_1 = self.obj_bp.matrix_world[2][3]
            grp1_z_2 = self.obj_z.matrix_world[2][3]
        
        if group.obj_bp.matrix_world[2][3] > group.obj_z.matrix_world[2][3]:
            grp2_z_1 = group.obj_z.matrix_world[2][3]
            grp2_z_2 = group.obj_bp.matrix_world[2][3]
        else:
            grp2_z_1 = group.obj_bp.matrix_world[2][3]
            grp2_z_2 = group.obj_z.matrix_world[2][3]
    
        if grp1_z_1 >= grp2_z_1 and grp1_z_1 <= grp2_z_2:
            return True
            
        if grp1_z_2 >= grp2_z_1 and grp1_z_2 <= grp2_z_2:
            return True
    
        if grp2_z_1 >= grp1_z_1 and grp2_z_1 <= grp1_z_2:
            return True
            
        if grp2_z_2 >= grp1_z_1 and grp2_z_2 <= grp1_z_2:
            return True

    def has_width_collision(self,group):
        grp1_x_1 = self.obj_bp.matrix_world[0][3]
        grp1_x_2 = self.obj_x.matrix_world[0][3]

        grp2_x_1 = group.obj_bp.matrix_world[0][3]
        grp2_x_2 = group.obj_x.matrix_world[0][3]
        
        if grp1_x_1 >= grp2_x_1 and grp1_x_1 <= grp2_x_2:
            return True
            
        if grp1_x_1 <= grp2_x_1 and grp1_x_2 >= grp2_x_1:
            return True

    def get_adjacent_assembly(self,direction='LEFT'):
        if self.obj_bp.parent:
            wall = Wall(self.obj_bp.parent)
        list_obj_bp = wall.get_wall_groups()
        list_obj_left_bp = []
        list_obj_right_bp = []
        
        list_obj_bp_z = wall.get_wall_groups(loc_sort='Z')
        list_obj_above_bp = []
        list_obj_below_bp = []
        
        for index, obj_bp in enumerate(list_obj_bp):
            if obj_bp.name == self.obj_bp.name:
                list_obj_left_bp = list_obj_bp[:index]
                list_obj_right_bp = list_obj_bp[index + 1:]
                break
            
        for index, obj_bp in enumerate(list_obj_bp_z):
            if obj_bp.name == self.obj_bp.name:
                list_obj_above_bp = list_obj_bp_z[index + 1:]
                list_obj_below_bp = list_obj_bp_z[:index]
            
        if direction == 'LEFT':
            list_obj_left_bp.reverse()
            for obj_bp in list_obj_left_bp:
                prev_group = Assembly(obj_bp)
                if self.has_height_collision(prev_group):
                    return Assembly(obj_bp)
             
            # CHECK NEXT WALL
    #         if math.radians(wall.obj_bp.rotation_euler.z) < 0:
#             left_wall =  wall.get_connected_wall('LEFT')
#             if left_wall:
#                 rotation_difference = wall.obj_bp.rotation_euler.z - left_wall.obj_bp.rotation_euler.z
#                 if rotation_difference < 0:
#                     list_obj_bp = left_wall.get_wall_groups()
#                     for obj in list_obj_bp:
#                         prev_group = Assembly(obj)
#                         product_x = obj.location.x
#                         product_width = prev_group.calc_width()
#                         x_dist = left_wall.obj_x.location.x  - (product_x + product_width)
#                         product_depth = math.fabs(self.obj_y.location.y)
#                         if x_dist <= product_depth:
#                             if self.has_height_collision(prev_group):
#                                 return prev_group.calc_depth()
         
        if direction == 'RIGHT':
            for obj_bp in list_obj_right_bp:
                next_group = Assembly(obj_bp)
                if self.has_height_collision(next_group):
                    return Assembly(obj_bp)
     
#             # CHECK NEXT WALL
#             right_wall =  wall.get_connected_wall('RIGHT')
#             if right_wall:
#                 rotation_difference = wall.obj_bp.rotation_euler.z - right_wall.obj_bp.rotation_euler.z
#                 if rotation_difference > 0:
#                     list_obj_bp = right_wall.get_wall_groups()
#                     for obj in list_obj_bp:
#                         next_group = Assembly(obj)
#                         product_x = obj.location.x
#                         product_width = next_group.calc_width()
#                         product_depth = math.fabs(self.obj_y.location.y)
#                         if product_x <= product_depth:
#                             if self.has_height_collision(next_group):
#                                 wall_length = wall.obj_x.location.x
#                                 product_depth = next_group.calc_depth()
#                                 return wall_length - product_depth
#     
#             return wall.obj_x.location.x

        if direction == 'ABOVE':
            for obj_bp in list_obj_above_bp:
                above_group = Assembly(obj_bp)
                if self.has_width_collision(above_group):
                    return Assembly(obj_bp)
        
        if direction == 'BELOW':
            for obj_bp in list_obj_below_bp:
                below_group = Assembly(obj_bp)
                if self.has_width_collision(below_group):
                    return Assembly(obj_bp)

    def set_name(self,name):
        self.obj_bp.mv.name = name
        self.obj_bp.mv.name_object = name

    def set_prompts(self,dict_prompts):
        for key in dict_prompts:
            if key in self.obj_bp.mv.PromptPage.COL_Prompt:
                prompt = self.obj_bp.mv.PromptPage.COL_Prompt[key]
                if prompt.Type == 'NUMBER':
                    prompt.NumberValue = dict_prompts[key]
                if prompt.Type == 'QUANTITY':
                    prompt.QuantityValue = dict_prompts[key]
                if prompt.Type == 'COMBOBOX':
                    prompt.EnumIndex = dict_prompts[key]
                if prompt.Type == 'CHECKBOX':
                    prompt.CheckBoxValue = dict_prompts[key]
                if prompt.Type == 'TEXT':
                    prompt.TextValue = dict_prompts[key]
                if prompt.Type == 'DISTANCE':
                    prompt.DistanceValue = dict_prompts[key]
                if prompt.Type == 'ANGLE':
                    prompt.AngleValue = dict_prompts[key]
                if prompt.Type == 'PERCENTAGE':
                    prompt.PercentageValue = dict_prompts[key]
                if prompt.Type == 'PRICE':
                    prompt.PriceValue = dict_prompts[key]

    def x_loc(self,expression="",driver_vars=[],value=0):
        if expression == "":
            self.obj_bp.location.x = value
        else:
            driver = self.obj_bp.driver_add('location',0)
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression

    def y_loc(self,expression="",driver_vars=[],value=0):
        if expression == "":
            self.obj_bp.location.y = value
        else:
            driver = self.obj_bp.driver_add('location',1)
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression

    def z_loc(self,expression="",driver_vars=[],value=0):
        if expression == "":
            self.obj_bp.location.z = value
        else:
            driver = self.obj_bp.driver_add('location',2)
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression

    def x_rot(self,expression="",driver_vars=[],value=0):
        if expression == "":
            self.obj_bp.rotation_euler.x = math.radians(value)
        else:
            driver = self.obj_bp.driver_add('rotation_euler',0)
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression

    def y_rot(self,expression="",driver_vars=[],value=0):
        if expression == "":
            self.obj_bp.rotation_euler.y = math.radians(value)
        else:
            driver = self.obj_bp.driver_add('rotation_euler',1)
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression
                
    def z_rot(self,expression="",driver_vars=[],value=0):
        if expression == "":
            self.obj_bp.rotation_euler.z = math.radians(value)
        else:
            driver = self.obj_bp.driver_add('rotation_euler',2)
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression

    def x_dim(self,expression="",driver_vars=[],value=0):
        if expression == "":
            self.obj_x.location.x = value
        else:
            driver = self.obj_x.driver_add('location',0)
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression

    def y_dim(self,expression="",driver_vars=[],value=0):
        if expression == "":
            self.obj_y.location.y = value
        else:
            driver = self.obj_y.driver_add('location',1)
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression
                          
    def z_dim(self,expression="",driver_vars=[],value=0):
        if expression == "":
            self.obj_z.location.z = value
        else:
            driver = self.obj_z.driver_add('location',2)
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression
    
    def calculator_deduction(self,expression,driver_vars):
        for tab in self.obj_bp.mv.PromptPage.COL_MainTab:
            if tab.type == 'CALCULATOR':
                data_path = 'mv.PromptPage.COL_MainTab["' + tab.name + '"].calculator_deduction'
                driver = self.obj_bp.driver_add(data_path)
                add_variables_to_driver(driver,driver_vars)
                driver.driver.expression = expression

    def prompt(self,prompt_name,expression="",driver_vars=[],value=0):
        if expression == "":
            if prompt_name in self.obj_bp.mv.PromptPage.COL_Prompt:
                prompt = self.obj_bp.mv.PromptPage.COL_Prompt[prompt_name]
                prompt.set_value(value)
        else:
            driver = None
            for prompt in self.obj_bp.mv.PromptPage.COL_Prompt:
                if prompt.name == prompt_name:
                    if prompt.Type == 'NUMBER':
                        data_path = 'mv.PromptPage.COL_Prompt["' + prompt.name + '"].NumberValue'
                        driver = self.obj_bp.driver_add(data_path)
                    if prompt.Type == 'QUANTITY':
                        data_path = 'mv.PromptPage.COL_Prompt["' + prompt.name + '"].QuantityValue'
                        driver = self.obj_bp.driver_add(data_path)
                    if prompt.Type == 'COMBOBOX':
                        data_path = 'mv.PromptPage.COL_Prompt["' + prompt.name + '"].EnumIndex'
                        driver = self.obj_bp.driver_add(data_path)
                    if prompt.Type == 'CHECKBOX':
                        data_path = 'mv.PromptPage.COL_Prompt["' + prompt.name + '"].CheckBoxValue'
                        driver = self.obj_bp.driver_add(data_path)
                    if prompt.Type == 'DISTANCE':
                        data_path = 'mv.PromptPage.COL_Prompt["' + prompt.name + '"].DistanceValue'
                        driver = self.obj_bp.driver_add(data_path)
                    if prompt.Type == 'ANGLE':
                        data_path = 'mv.PromptPage.COL_Prompt["' + prompt.name + '"].AngleValue'
                        driver = self.obj_bp.driver_add(data_path)
                    if prompt.Type == 'PERCENTAGE':
                        data_path = 'mv.PromptPage.COL_Prompt["' + prompt.name + '"].PercentageValue'
                        driver = self.obj_bp.driver_add(data_path)
                    if prompt.Type == 'PRICE':
                        data_path = 'mv.PromptPage.COL_Prompt["' + prompt.name + '"].PriceValue'
                        driver = self.obj_bp.driver_add(data_path)
                    break
            if driver:
                add_variables_to_driver(driver,driver_vars)
                driver.driver.expression = expression
            else:
                print("Error: '" + prompt_name + "' not found while setting expression '" + expression + "'")

    def draw_properties(self,layout):
        ui = bpy.context.scene.mv.ui
        col = layout.column(align=True)
        box = col.box()
        row = box.row(align=True)
        row.prop_enum(ui, "group_tabs", enums.enum_group_tabs[0][0], icon='INFO', text="") 
        row.prop_enum(ui, "group_tabs", enums.enum_group_tabs[2][0], icon='SETTINGS', text="")    
        row.prop_enum(ui, "group_tabs", enums.enum_group_tabs[3][0], icon='GROUP', text="")
        row.prop_enum(ui, "group_tabs", enums.enum_group_tabs[4][0], icon='AUTO', text="")
        row.separator()
        row.operator('fd_assembly.delete_selected_assembly',text="",icon='X').object_name = self.obj_bp.name
        if ui.group_tabs == 'INFO':
            box = col.box()
            self.draw_transform(box)
        if ui.group_tabs == 'PROMPTS':
            box = col.box()
            self.obj_bp.mv.PromptPage.draw_prompt_page(box,self.obj_bp,allow_edit=True)
        if ui.group_tabs == 'OBJECTS':
            box = col.box()
            self.draw_objects(box)
        if ui.group_tabs == 'DRIVERS':
            box = col.box()
            self.draw_drivers(box)
    
    def draw_transform(self,layout,show_prompts=False):
        row = layout.row()
        row.operator('fd_assembly.rename_assembly',text=self.obj_bp.mv.name_object,icon='GROUP').object_name = self.obj_bp.name
        if show_prompts and self.number_of_visible_prompt_tabs() > 0:
            if self.number_of_visible_prompt_tabs() == 1:
                for index, tab in enumerate(self.obj_bp.mv.PromptPage.COL_MainTab):
                    if tab.type in {'VISIBLE','CALCULATOR'}:
                        props = row.operator("fd_prompts.show_object_prompts",icon='SETTINGS',text="")
                        props.object_bp_name = self.obj_bp.name
                        props.tab_name = tab.name
                        props.index = index
            else:
                row.menu('MENU_active_group_options',text="",icon='SETTINGS')

        row = layout.row(align=True)
        row.label('Dimension X:')
        row.prop(self.obj_x,"lock_location",index=0,text='')
        if self.obj_x.lock_location[0]:
            row.label(str(round(meter_to_unit(self.obj_x.location.x),4)))
        else:
            row.prop(self.obj_x,"location",index=0,text="")
            row.prop(self.obj_x,'hide',text="")
        
        row = layout.row(align=True)
        row.label('Dimension Y:')
        row.prop(self.obj_y,"lock_location",index=1,text='')
        if self.obj_y.lock_location[1]:
            row.label(str(round(meter_to_unit(self.obj_y.location.y),4)))
        else:
            row.prop(self.obj_y,"location",index=1,text="")
            row.prop(self.obj_y,'hide',text="")
        
        row = layout.row(align=True)
        row.label('Dimension Z:')
        row.prop(self.obj_z,"lock_location",index=2,text='')
        if self.obj_z.lock_location[2]:
            row.label(str(round(meter_to_unit(self.obj_z.location.z),4)))
        else:
            row.prop(self.obj_z,"location",index=2,text="")
            row.prop(self.obj_z,'hide',text="")
        
        col1 = layout.row()
        if self.obj_bp:
            col2 = col1.split()
            col = col2.column(align=True)
            col.label('Location:')
            
            if self.obj_bp.lock_location[0]:
                row = col.row(align=True)
                row.prop(self.obj_bp,"lock_location",index=0,text="")
                row.label(str(round(meter_to_unit(self.obj_bp.location.x),4)))
            else:
                row = col.row(align=True)
                row.prop(self.obj_bp,"lock_location",index=0,text="")
                row.prop(self.obj_bp,"location",index=0,text="X")
                
            if self.obj_bp.lock_location[1]:
                row = col.row(align=True)
                row.prop(self.obj_bp,"lock_location",index=1,text="")
                row.label(str(round(meter_to_unit(self.obj_bp.location.y),4)))
            else:
                row = col.row(align=True)
                row.prop(self.obj_bp,"lock_location",index=1,text="")
                row.prop(self.obj_bp,"location",index=1,text="Y")
                
            if self.obj_bp.lock_location[2]:
                row = col.row(align=True)
                row.prop(self.obj_bp,"lock_location",index=2,text="")
                row.label(str(round(meter_to_unit(self.obj_bp.location.z),4)))
            else:
                row = col.row(align=True)
                row.prop(self.obj_bp,"lock_location",index=2,text="")
                row.prop(self.obj_bp,"location",index=2,text="Z")
                
            col2 = col1.split()
            col = col2.column(align=True)
            col.label('Rotation:')
            
            if self.obj_bp.lock_rotation[0]:
                row = col.row(align=True)
                row.prop(self.obj_bp,"lock_rotation",index=0,text="")
                row.label(str(round(math.degrees(self.obj_bp.rotation_euler.x),4)))
            else:
                row = col.row(align=True)
                row.prop(self.obj_bp,"lock_rotation",index=0,text="")
                row.prop(self.obj_bp,"rotation_euler",index=0,text="X")
                
            if self.obj_bp.lock_rotation[1]:
                row = col.row(align=True)
                row.prop(self.obj_bp,"lock_rotation",index=1,text="")
                row.label(str(round(math.degrees(self.obj_bp.rotation_euler.y),4)))
            else:
                row = col.row(align=True)
                row.prop(self.obj_bp,"lock_rotation",index=1,text="")
                row.prop(self.obj_bp,"rotation_euler",index=1,text="Y")
                
            if self.obj_bp.lock_rotation[2]:
                row = col.row(align=True)
                row.prop(self.obj_bp,"lock_rotation",index=2,text="")
                row.label(str(round(math.degrees(self.obj_bp.rotation_euler.z),4)))
            else:
                row = col.row(align=True)
                row.prop(self.obj_bp,"lock_rotation",index=2,text="")
                row.prop(self.obj_bp,"rotation_euler",index=2,text="Z")
                
    def draw_objects(self,layout):
        scene = bpy.context.scene
        row = layout.row()
        row.operator('fd_assembly.load_active_assembly_objects',text="Load Child Objects",icon='FILE_REFRESH').object_name = self.obj_bp.name
        row.menu('MENU_add_assembly_object',text="",icon='ZOOMIN')
        if self.obj_bp.name == scene.mv.active_object_name:
            col = layout.column(align=True)
            col.template_list("FD_UL_objects", " ", scene.mv, "children_objects", scene.mv, "active_object_index")
            if scene.mv.active_object_index <= len(scene.mv.children_objects) + 1:
                box = col.box()
                obj = bpy.data.objects[scene.mv.children_objects[scene.mv.active_object_index].name]
                box.prop(obj.mv,'name_object')
                if obj.type == 'MESH':
                    box.prop(obj.mv,'use_as_bool_obj')
                box.prop(obj.mv,'use_as_mesh_hook')
            
    def draw_drivers(self,layout):
        ui = bpy.context.scene.mv.ui
        row = layout.row(align=True)
        row.operator('fd_driver.turn_on_driver',text="",icon='QUIT').object_name = self.obj_bp.name
        row.prop(ui,'group_driver_tabs',text='')
        box = layout.box()
        
        if ui.group_driver_tabs == 'LOC_X':
            box.prop(self.obj_bp,'location',index=0,text="Location X")
            driver = get_driver(self.obj_bp,'location',0)
            if driver:
                draw_driver_expression(box,driver)
                draw_add_variable_operators(layout,self.obj_bp.name,'location',0)
                draw_driver_variables(layout,driver,self.obj_bp.name)
    
        if ui.group_driver_tabs == 'LOC_Y':
            box.prop(self.obj_bp,'location',index=1,text="Location Y")
            driver = get_driver(self.obj_bp,'location',1)
            if driver:
                draw_driver_expression(box,driver)
                draw_add_variable_operators(layout,self.obj_bp.name,'location',1)
                draw_driver_variables(layout,driver,self.obj_bp.name)
                
        if ui.group_driver_tabs == 'LOC_Z':
            box.prop(self.obj_bp,'location',index=2,text="Location Z")
            driver = get_driver(self.obj_bp,'location',2)
            if driver:
                draw_driver_expression(box,driver)
                draw_add_variable_operators(layout,self.obj_bp.name,'location',2)
                draw_driver_variables(layout,driver,self.obj_bp.name)
                
        if ui.group_driver_tabs == 'ROT_X':
            box.prop(self.obj_bp,'rotation_euler',index=0,text="Rotation X")
            driver = get_driver(self.obj_bp,'rotation_euler',0)
            if driver:
                draw_driver_expression(box,driver)
                draw_add_variable_operators(layout,self.obj_bp.name,'rotation_euler',0)
                draw_driver_variables(layout,driver,self.obj_bp.name)
                
        if ui.group_driver_tabs == 'ROT_Y':
            box.prop(self.obj_bp,'rotation_euler',index=1,text="Rotation Y")
            driver = get_driver(self.obj_bp,'rotation_euler',1)
            if driver:
                draw_driver_expression(box,driver)
                draw_add_variable_operators(layout,self.obj_bp.name,'rotation_euler',1)
                draw_driver_variables(layout,driver,self.obj_bp.name)
    
        if ui.group_driver_tabs == 'ROT_Z':
            box.prop(self.obj_bp,'rotation_euler',index=2,text="Rotation Z")
            driver = get_driver(self.obj_bp,'rotation_euler',2)
            if driver:
                draw_driver_expression(box,driver)
                draw_add_variable_operators(layout,self.obj_bp.name,'rotation_euler',2)
                draw_driver_variables(layout,driver,self.obj_bp.name)
    
        if ui.group_driver_tabs == 'DIM_X':
            box.prop(self.obj_x,'location',index=0,text="Dimension X")
            driver = get_driver(self.obj_x,'location',0)
            if driver:
                draw_driver_expression(box,driver)
                draw_add_variable_operators(layout,self.obj_x.name,'location',0)
                draw_driver_variables(layout,driver,self.obj_x.name)
    
        if ui.group_driver_tabs == 'DIM_Y':
            box.prop(self.obj_y,'location',index=1,text="Dimension Y")
            driver = get_driver(self.obj_y,'location',1)
            if driver:
                draw_driver_expression(box,driver)
                draw_add_variable_operators(layout,self.obj_y.name,'location',1)
                draw_driver_variables(layout,driver,self.obj_y.name)
                        
        if ui.group_driver_tabs == 'DIM_Z':
            box.prop(self.obj_z,'location',index=2,text="Dimension Z")
            driver = get_driver(self.obj_z,'location',2)
            if driver:
                draw_driver_expression(box,driver)
                draw_add_variable_operators(layout,self.obj_z.name,'location',2)
                draw_driver_variables(layout,driver,self.obj_z.name)
                
        if ui.group_driver_tabs == 'PROMPTS':
            if len(self.obj_bp.mv.PromptPage.COL_Prompt) < 1:
                box.label('No Prompts')
            else:
                box.template_list("FD_UL_promptitems"," ", self.obj_bp.mv.PromptPage, "COL_Prompt", self.obj_bp.mv.PromptPage, "PromptIndex",rows=5,type='DEFAULT')
                prompt = self.obj_bp.mv.PromptPage.COL_Prompt[self.obj_bp.mv.PromptPage.PromptIndex]
                
                if prompt.Type == 'DISTANCE':
                    driver = get_driver(self.obj_bp,'mv.PromptPage.COL_Prompt["' + prompt.name + '"].DistanceValue',0)
                    if driver:
                        box.operator('fd_driver.turn_off_driver').object_name = self.obj_bp.name
                        draw_driver_expression(box,driver)
                        draw_add_variable_operators(layout,self.obj_bp.name,'mv.PromptPage.COL_Prompt["' +  prompt.name + '"].DistanceValue',0)
                        draw_driver_variables(layout,driver,self.obj_bp.name)
                        
                if prompt.Type == 'ANGLE':
                    driver = get_driver(self.obj_bp,'mv.PromptPage.COL_Prompt["' + prompt.name + '"].AngleValue',0)
                    if driver:
                        box.operator('fd_driver.turn_off_driver').object_name = self.obj_bp.name
                        draw_driver_expression(box,driver)
                        draw_add_variable_operators(layout,self.obj_bp.name,'mv.PromptPage.COL_Prompt["' + prompt.name + '"].AngleValue',0)
                        draw_driver_variables(layout,driver,self.obj_bp.name)
                        
                if prompt.Type == 'PRICE':
                    driver = get_driver(self.obj_bp,'mv.PromptPage.COL_Prompt["' + prompt.name + '"].PriceValue',0)
                    if driver:
                        box.operator('fd_driver.turn_off_driver').object_name = self.obj_bp.name
                        draw_driver_expression(box,driver)
                        draw_add_variable_operators(layout,self.obj_bp.name,'mv.PromptPage.COL_Prompt["' + prompt.name + '"].PriceValue',0)
                        draw_driver_variables(layout,driver,self.obj_bp.name)
                        
                if prompt.Type == 'PERCENTAGE':
                    driver = get_driver(self.obj_bp,'mv.PromptPage.COL_Prompt["' + prompt.name + '"].PercentageValue',0)
                    if driver:
                        box.operator('fd_driver.turn_off_driver').object_name = self.obj_bp.name
                        draw_driver_expression(box,driver)
                        draw_add_variable_operators(layout,self.obj_bp.name,'mv.PromptPage.COL_Prompt["' + prompt.name + '"].PercentageValue',0)
                        draw_driver_variables(layout,driver,self.obj_bp.name)
                
                if prompt.Type == 'NUMBER':
                    driver = get_driver(self.obj_bp,'mv.PromptPage.COL_Prompt["' + prompt.name + '"].NumberValue',0)
                    if driver:
                        box.operator('fd_driver.turn_off_driver').object_name = self.obj_bp.name
                        draw_driver_expression(box,driver)
                        draw_add_variable_operators(layout,self.obj_bp.name,'mv.PromptPage.COL_Prompt["' + prompt.name + '"].NumberValue',0)
                        draw_driver_variables(layout,driver,self.obj_bp.name)
                        
                if prompt.Type == 'QUANTITY':
                    driver = get_driver(self.obj_bp,'mv.PromptPage.COL_Prompt["' + prompt.name + '"].QuantityValue',0)
                    if driver:
                        box.operator('fd_driver.turn_off_driver').object_name = self.obj_bp.name
                        draw_driver_expression(box,driver)
                        draw_add_variable_operators(layout,self.obj_bp.name,'mv.PromptPage.COL_Prompt["' + prompt.name + '"].QuantityValue',0)
                        draw_driver_variables(layout,driver,self.obj_bp.name)
    
                if prompt.Type == 'COMBOBOX':
                    driver = get_driver(self.obj_bp,'mv.PromptPage.COL_Prompt["' + prompt.name + '"].EnumIndex',0)
                    if driver:
                        box.operator('fd_driver.turn_off_driver').object_name = self.obj_bp.name
                        draw_driver_expression(box,driver)
                        draw_add_variable_operators(layout,self.obj_bp.name,'mv.PromptPage.COL_Prompt["' + prompt.name + '"].EnumIndex',0)
                        draw_driver_variables(layout,driver,self.obj_bp.name)
    
                if prompt.Type == 'CHECKBOX':
                    driver = get_driver(self.obj_bp,'mv.PromptPage.COL_Prompt["' + prompt.name + '"].CheckBoxValue',0)
                    if driver:
                        box.operator('fd_driver.turn_off_driver').object_name = self.obj_bp.name
                        draw_driver_expression(box,driver)
                        draw_add_variable_operators(layout,self.obj_bp.name,'mv.PromptPage.COL_Prompt["' + prompt.name + '"].CheckBoxValue',0)
                        draw_driver_variables(layout,driver,self.obj_bp.name)


class Library_Assembly(Assembly):
    
    """ Type:string - The library folder name to save assembly to """
    library_name = ""
    
    """ Type:string - The category folder name to save assembly to """
    category_name = ""
    
    """ Type:string - The assembly name """
    assembly_name = ""
    
    """ Type:enum_string("","Corner") - Used for drag and drop from placement """
    placement_type = ""
    
    """ Type:enum_string("RECTANGLE",
                         "INSIDE_NOTCH",
                         "INSIDE_DIAGONAL",
                         "OUTSIDE_NOTCH",
                         "OUTSIDE_DIAGONAL",
                         "TRANSITION",
                         "CUSTOM") 
                         - Used for molding placement """
    product_shape = "RECTANGLE"
    
    """ Type:string - The Prompt Page Operator ID
                      This is the bl_id property  """
    property_id = ""

    """ Type:enum_string("PRODUCT",
                         "INSERT") 
                         - Determines if the library assembly is an insert or a product """
    type_assembly = "PRODUCT"
    
    """ Type:bool - Determines if the z dimension is mirrored. 
                    Typically used for upper/suspended cabinets  """
    mirror_z = False
    
    """ Type:bool - Determines if the y dimension is mirrored. 
                    Typically used for all cabinets  """
    mirror_y = True
    
    """ Type:float - The default x dimension of the assembly  """
    width = 0
    
    """ Type:float - The default z dimension of the assembly  """
    height = 0
    
    """ Type:float - The default y dimension of the assembly  """
    depth = 0
    
    """ Type:float - The default z location of the assembly  """
    height_above_floor = 0
    
    """ Type:dictionary - The list of prompts to overwrite when creating this assembly
                          key = prompt name
                          value = prompt value  """
    prompts = {}
    
    def add_assembly(self,path):
        """ Returns:Part - adds an assembly to this assembly
                           and returns it as a fd.Part
                              
            path:tuple of strings - The folder location to the assembly to add.
                                    split into strings.
                                    i.e ("Library Name","Category Name","Assembly Name")
        """
        assembly = get_assembly(path[:-1], path[-1])
        assembly.obj_bp.parent = self.obj_bp
        part = Part(assembly.obj_bp)
        return part
    
    def add_object(self,path):
        """ Returns:Assembly_Object - adds an assembly to this assembly
                                      and returns it as a fd.Part
                              
            path:tuple of strings - The folder location to the object to add.
                                    split into strings.
                                    i.e ("Library Name","Category Name","Object Name")
        """
        obj = get_object(path[:-1], path[-1])
        obj.parent = self.obj_bp
        ass_obj = Assembly_Object(obj)
        return ass_obj
        
    def add_opening(self):
        """ Returns:Assembly - creates an empty opening to this assembly
                               and returns it as an Assembly
        """
        opening = Assembly()
        opening.create_assembly()
        opening.obj_bp.parent = self.obj_bp
        opening.obj_bp.cabinetlib.type_group = 'OPENING'
        opening.obj_bp.mv.name_object = "Opening"
        return opening
    
    def set_property_id(self,obj,property_id):
        """ Returns:None - sets all of the property_id values for the assembly
                           and all of its children.
        """
        obj.mv.property_id = property_id
        for child in obj.children:
            self.set_property_id(child,property_id)

    def update(self,obj_bp=None):
        """ Returns:None - sets the specification group, 
                                    placement_type, 
                                    product_shape,
                                    mirror_z,
                                    mirror_y,
                                    name,
                                    product_id,
                                    height_above_floor,
                                    runs the calculators,
                                    and sets prompts based on the prompt dictionary property
        """
        if obj_bp:
            self.obj_bp = obj_bp
        for child in self.obj_bp.children:
            if child.mv.type == 'VPDIMX':
                self.obj_x = child
            if child.mv.type == 'VPDIMY':
                self.obj_y = child
            if child.mv.type == 'VPDIMZ':
                self.obj_z = child
                
        default_spec_group = bpy.context.scene.cabinetlib.spec_groups[bpy.context.scene.cabinetlib.spec_group_index]
        bpy.ops.cabinetlib.change_product_spec_group(object_name=self.obj_bp.name,spec_group_name=default_spec_group.name)
        
        self.obj_bp.cabinetlib.type_group = self.type_assembly
        self.obj_bp.cabinetlib.placement_type = self.placement_type
        self.obj_bp.cabinetlib.product_shape = self.product_shape
        self.obj_bp.cabinetlib.mirror_z = self.mirror_z
        self.obj_bp.cabinetlib.mirror_y = self.mirror_y
        self.set_name(self.assembly_name)
        self.set_property_id(self.obj_bp,self.property_id)
        
        self.x_dim(value = self.width)
        if self.mirror_y:
            self.y_dim(value = -self.depth)
        else:
            self.y_dim(value = self.depth)
            
        if self.mirror_z:
            self.z_dim(value = -self.height)
        else:
            self.z_dim(value = self.height)

        self.z_loc(value = self.height_above_floor)
        
        run_calculators(self.obj_bp)
        
        self.set_prompts(self.prompts)

class Part(Assembly):
    
    def material(self,material_pointer_name):
        """ Returns:None - sets the every material slot for every mesh
                           to the material_pointer_name
                           
            material_pointer_name:string - name of the material pointer 
                                           to assign
        """
        for slot in self.obj_bp.cabinetlib.material_slots:
            slot.pointer_name = material_pointer_name
        for child in self.obj_bp.children:
            if child.type == 'MESH':
                for slot in child.cabinetlib.material_slots:
                    slot.pointer_name = material_pointer_name

    def cutpart(self,cutpart_name):
        """ Returns:None - assigns the every mesh cut part 
                           to the cutpart_name
                           
            cutpart_name:string - name of the material pointer 
                                  to assign
        """
        for child in self.obj_bp.children:
            if child.type == 'MESH' and child.cabinetlib.type_mesh == 'CUTPART':
                child.cabinetlib.cutpart_name = cutpart_name

    def edgebanding(self,edgebanding_name,w1=False,l1=False,w2=False,l2=False):
        """ Returns:None - assigns every mesh cut part 
                           to the edgebanding_name
                           
            edgebanding_name:string - name of the edgepart pointer 
                                      to assign
                                      
            w1:bool - determines if to edgeband width 1 of the part
            
            w2:bool - determines if to edgeband width 2 of the part
            
            l1:bool - determines if to edgeband length 1 of the part
            
            l2:bool - determines if to edgeband length 2 of the part
        """
        for child in self.obj_bp.children:
            if child.type == 'MESH' and child.cabinetlib.type_mesh == 'EDGEBANDING':
                child.cabinetlib.edgepart_name = edgebanding_name
            if child.type == 'MESH' and child.cabinetlib.type_mesh == 'CUTPART':
                child.cabinetlib.edgepart_name = edgebanding_name
                if w1:
                    child.cabinetlib.edge_w1 = edgebanding_name
                if l1:
                    child.cabinetlib.edge_l1 = edgebanding_name
                if w2:
                    child.cabinetlib.edge_w2 = edgebanding_name
                if l2:
                    child.cabinetlib.edge_l2 = edgebanding_name
                 
    def add_machine_token(self,machining_name,machining_type,machining_face):
        """ Returns:tuple(bpy.types.Object,properties.Machining_Token) - adds a machine token
                                                                         to every cutpart mesh
                           
            edgebanding_name:string - name of the edgepart_pointer to assign
                                      
            w1:bool - edgeband width 1 of the part
            
            w2:bool - edgeband width 2 of the part
            
            l1:bool - edgeband length 1 of the part
            
            l2:bool - edgeband length 2 of the part
        """
        for child in self.obj_bp.children:
            if child.cabinetlib.type_mesh == 'CUTPART':
                token = child.cabinetlib.mp.add_machine_token(machining_name ,machining_type,machining_face)
                return child, token
                 
    def get_cutparts(self):
        """ Returns:list of bpy.types.Object - gets all mesh objects that are assigned as cutparts.
        """
        cutparts = []
        for child in self.obj_bp.children:
            if child.type == 'MESH' and child.cabinetlib.type_mesh == 'CUTPART':
                cutparts.append(child)
        return cutparts
    
    def recalculate_normals(self):
        pass
    
    def machine_token(self,obj,token,token_property,expression,driver_vars,index=None):
        """ Returns:None - sets a driver for a machine token that is passed in.
        """
        data_path = ""
        for m_token in obj.cabinetlib.mp.machine_tokens:
            if m_token == token:
                if index:
                    data_path = 'cabinetlib.mp.machine_tokens.["' + token.name + '"].' + token_property + '[' + str(index) + ']'
                else:
                    data_path = 'cabinetlib.mp.machine_tokens.["' + token.name + '"].' + token_property
                obj.driver_add(data_path)
                 
        if data_path != "":
            for var in driver_vars:
                if obj.animation_data:
                    for DR in obj.animation_data.drivers:
                        if data_path in DR.data_path:
                            new_var = DR.driver.variables.new()
                            new_var.name = var.var_name
                            new_var.targets[0].data_path = var.data_path
                            new_var.targets[0].id = var.obj
                            DR.driver.expression = expression
                            break
        else:
            print("Error: '" + token.name + "' not found while setting expression '" + expression + "'")


class Assembly_Object():
    
    obj = None
    
    def __init__(self,obj):
        self.obj = obj

    def set_name(self,name):
        self.obj.mv.name = name
        self.obj.mv.name_object = name

    def x_loc(self,expression="",driver_vars=[],value=0):
        if expression == "":
            self.obj.location.x = value
        else:
            driver = self.obj.driver_add('location',0)
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression

    def y_loc(self,expression="",driver_vars=[],value=0):
        if expression == "":
            self.obj.location.y = value
        else:
            driver = self.obj.driver_add('location',1)
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression

    def z_loc(self,expression="",driver_vars=[],value=0):
        if expression == "":
            self.obj.location.z = value
        else:
            driver = self.obj.driver_add('location',2)
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression
            
    def x_rot(self,expression="",driver_vars=[],value=0):
        if expression == "":
            self.obj.rotation_euler.x = math.radians(value)
        else:
            driver = self.obj.driver_add('rotation_euler',0)
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression

    def y_rot(self,expression="",driver_vars=[],value=0):
        if expression == "":
            self.obj.rotation_euler.y = math.radians(value)
        else:
            driver = self.obj.driver_add('rotation_euler',1)
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression
                
    def z_rot(self,expression="",driver_vars=[],value=0):
        if expression == "":
            self.obj.rotation_euler.z = math.radians(value)
        else:
            driver = self.obj.driver_add('rotation_euler',2)
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression
            
    def x_dim(self,expression="",driver_vars=[],value=0):
        if expression == "":
            self.obj.location.x = value
        else:
            driver = self.obj.driver_add('dimensions',0)
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression

    def y_dim(self,expression="",driver_vars=[],value=0):
        if expression == "":
            self.obj.location.y = value
        else:
            driver = self.obj.driver_add('dimensions',1)
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression

    def z_dim(self,expression="",driver_vars=[],value=0):
        if expression == "":
            self.obj.location.z = value
        else:
            driver = self.obj.driver_add('dimensions',2)
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression
            
    def hide(self,expression="",driver_vars=[],value=False):
        if expression == "":
            self.obj.hide = value
            self.obj.hide_render = value
        else:
            driver = self.obj.driver_add('hide')
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression
            
            driver = self.obj.driver_add('hide_render')
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression
            
    def material(self,material_pointer_name):
        for slot in self.obj.cabinetlib.material_slots:
            slot.pointer_name = material_pointer_name


class Material_Pointer():
    
    name = ""
    library_name = ""
    category_name = ""
    item_name = ""
    
    def __init__(self,library_path):
        self.library_name = library_path[0]
        self.item_name = library_path[-1]
        if len(library_path) > 2:
            self.category_name = library_path[1]


class Cutpart_Pointer():
    
    name = ""
    thickness = 0.0
    core = ""
    top = ""
    bottom = ""
    mv_pointer_name = ""
    
    def __init__(self,thickness,core,top,bottom,mv_pointer_name = ""):
        self.thickness = thickness
        self.core = core
        self.top = top
        self.bottom = bottom
        self.mv_pointer_name = mv_pointer_name


class Edgepart_Pointer():
    
    name = ""
    thickness = 0.0
    material = ""
    mv_pointer_name = ""
    
    def __init__(self,thickness,material,mv_pointer_name = ""):
        self.thickness = thickness
        self.material = material
        self.mv_pointer_name = mv_pointer_name


class Dimension():
    
    anchor = None
    end_point = None
    label = ""   
    opengl_dim = None
    
    def __init__(self):
        scene = bpy.context.scene
        self.draw()
 
        self.opengl_dim = self.anchor.mv.opengl_dim
        self.opengl_dim.glpointa = 0
        self.opengl_dim.glpointb = 0  
        self.opengl_dim.gl_label = scene.mv.opengl_dim.gl_label
        self.opengl_dim.gl_font_size = scene.mv.opengl_dim.gl_font_size     
    
    def draw(self):
        context = bpy.context
        bpy.ops.object.add(type='EMPTY')
        self.anchor = context.object
        self.anchor.mv.type = 'VISDIM_A'
        self.anchor.mv.name_object = "Anchor"
        self.anchor.hide = True
        
        bpy.ops.object.add(type='EMPTY')
        self.end_point = context.object
        self.end_point.mv.type = 'VISDIM_B'
        self.end_point.mv.name_object = "End Point"
        self.end_point.parent = self.anchor
        self.end_point.hide = True
    
    def parent(self, obj_bp):
        self.anchor.parent = obj_bp
    
    def start_x(self,expression="",driver_vars=[],value=0):
        if expression == "":
            self.anchor.location.x = value
        else:
            driver = self.anchor.driver_add('location',0)
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression        
    
    def start_y(self,expression="",driver_vars=[],value=0):
        if expression == "":
            self.anchor.location.y = value
        else:
            driver = self.anchor.driver_add('location',1)
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression 
    
    def start_z(self,expression="",driver_vars=[],value=0):
        if expression == "":
            self.anchor.location.z = value
        else:
            driver = self.anchor.driver_add('location',2)
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression 
    
    def end_x(self,expression="",driver_vars=[],value=0):
        if expression == "":
            self.end_point.location.x = value
        else:
            driver = self.end_point.driver_add('location',0)
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression 
    
    def end_y(self,expression="",driver_vars=[],value=0):
        if expression == "":
            self.end_point.location.y = value
        else:
            driver = self.end_point.driver_add('location',1)
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression 
    
    def end_z(self,expression="",driver_vars=[],value=0):
        if expression == "":
            self.end_point.location.z = value
        else:
            driver = self.end_point.driver_add('location',2)
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression 
    
    def hide(self,expression="",driver_vars=[],value=True):
        if expression == "":
            self.opengl_dim.hide = value
        else:
            driver = self.anchor.driver_add('mv.opengl_dim.hide')
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression 
            
    def set_color(self,expression="",driver_vars=[],value=0):  
        if expression == "":
            self.opengl_dim.gl_color = value
        else:
            driver = self.anchor.driver_add('mv.opengl_dim.gl_color')
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression                      
            
    def set_label(self, text, new_line=False):
        if new_line:
            self.opengl_dim.gl_label = " | " + text
        else:
            self.opengl_dim.gl_label = text
    
    def set_text_offset_x(self,expression="",driver_vars=[],value=0):
        if expression == "":
            self.opengl_dim.gl_text_x = value
        else:
            driver = self.anchor.driver_add('cabinetlib.opengl_dim.gl_text_x')
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression 
    
    def set_text_offset_y(self,expression="",driver_vars=[],value=0):
        if expression == "":
            self.opengl_dim.gl_text_y = value
        else:
            driver = self.anchor.driver_add('cabinetlib.opengl_dim.gl_text_y')
            add_variables_to_driver(driver,driver_vars)
            driver.driver.expression = expression            
    
    
class Wall(Assembly):
    
    def __init__(self,obj_bp=None):
        if obj_bp:
            self.obj_bp = obj_bp
            for child in obj_bp.children:
                if child.mv.type == 'VPDIMX':
                    self.obj_x = child
                if child.mv.type == 'VPDIMY':
                    self.obj_y = child
                if child.mv.type == 'VPDIMZ':
                    self.obj_z = child
                if self.obj_bp and self.obj_x and self.obj_y and self.obj_z:
                    break

    def create_wall(self):
        self.create_assembly()
        self.obj_bp.mv.type = 'BPWALL'
        self.obj_bp.mv.name_object = 'Wall'
        self.set_object_names()

    def build_wall_mesh(self):
        self.obj_bp.mv.name = "BPWALL.Wall"
        obj_mesh = self.build_cage()
        obj_mesh.mv.name = 'Wall Mesh'
        obj_mesh.name = "Wall Mesh"
        obj_mesh.mv.type = 'NONE'
        obj_mesh.draw_type = 'TEXTURED'
        obj_mesh.hide_select = False
        obj_mesh.cycles_visibility.camera = True
        obj_mesh.cycles_visibility.diffuse = True
        obj_mesh.cycles_visibility.glossy = True
        obj_mesh.cycles_visibility.transmission = True
        obj_mesh.cycles_visibility.shadow = True
        return obj_mesh
        
    def get_wall_mesh(self):
        for child in self.obj_bp.children:
            if child.type == 'MESH' and child.mv.type == 'NONE':
                return child
    
    def create_wall_group(self):
        wall_group = bpy.data.groups.new(self.obj_bp.name)
        return self.group_children(wall_group,self.obj_bp)
    
    def group_children(self,grp,obj):
        objs = []

        objs.append(obj)
    
        for child in obj.children:
            if len(child.children) > 0:
                self.group_children(grp,child)
            else:
                objs.append(child)              

        for obj in objs:
            grp.objects.link(obj)        
            
        return grp
        
    def get_wall_groups(self, loc_sort='X'):
        """ This returns a sorted list of all of the groups base points
            parented to the wall
        """
        list_obj_bp = []
        for child in self.obj_bp.children:
            if child.mv.type == 'BPASSEMBLY':
                list_obj_bp.append(child)
        if loc_sort == 'X':
            list_obj_bp.sort(key=lambda obj: obj.location.x, reverse=False)
        if loc_sort == 'Y':
            list_obj_bp.sort(key=lambda obj: obj.location.y, reverse=False)            
        if loc_sort == 'Z':
            list_obj_bp.sort(key=lambda obj: obj.location.z, reverse=False)
        return list_obj_bp
        
    def get_connected_wall(self,direction):
        if direction == 'LEFT':
            for con in self.obj_bp.constraints:
                if con.type == 'COPY_LOCATION':
                    if con.target:
                        return Wall(con.target.parent)
    
        if direction == 'RIGHT':
            for obj in bpy.context.visible_objects:
                if obj.mv.type == 'BPWALL':
                    next_wall = Wall(obj)
                    for con in next_wall.obj_bp.constraints:
                        if con.type == 'COPY_LOCATION':
                            if con.target == self.obj_x:
                                return next_wall


class Variable():
    
    var_name = ""
    obj = None
    data_path = ""
    var_type = ""
    transform_space = 'WORLD_SPACE'
    transform_type = 'LOC_X'
    
    def __init__(self,obj,data_path,var_name,var_type='SINGLE_PROP',transform_space='WORLD_SPACE',transform_type='LOC_X'):
        self.obj = obj
        self.data_path = data_path
        self.var_name = var_name
        self.var_type = var_type
        if var_type == 'TRANSFORMS':
            self.transform_space = transform_space
            self.transform_type = transform_type
            
class MV_XML():
    
    tree = None
    
    def __init__(self):
        pass
    
    def create_tree(self):
        root = ET.Element('Root',{'Application':'Microvellum','ApplicationVersion':'7.0'})
        self.tree = ET.ElementTree(root)
        return root
    
    def add_element(self,root,elm_name,attrib_name=""):
        if attrib_name == "":
            elm = ET.Element(elm_name)
        else:
            elm = ET.Element(elm_name,{'Name':attrib_name})
        root.append(elm)
        return elm
    
    def add_element_with_text(self,root,elm_name,text):
        field = ET.Element(elm_name)
        field.text = text
        root.append(field)
    
    def format_xml_file(self,path):
        """ This makes the xml file readable as a txt doc.
            For some reason the xml.toprettyxml() function
            adds extra blank lines. This makes the xml file
            unreadable. This function just removes
            all of the blank lines.
            arg1: path to xml file
        """
        from xml.dom.minidom import parse
        
        xml = parse(path)
        pretty_xml = xml.toprettyxml()
        
        file = open(path,'w')
        file.write(pretty_xml)
        file.close()
        
        cleaned_lines = []
        with open(path,"r") as f:
            lines = f.readlines()
            for l in lines:
                l.strip()
                if "<" in l:
                    cleaned_lines.append(l)
            
        with open (path,"w") as f:
            f.writelines(cleaned_lines)
    
    def write(self,path):
        with open(path, 'w',encoding='utf-8') as file:
            self.tree.write(file,encoding='unicode')
            
        self.format_xml_file(path)

    
#-------OBJECT CREATION

def create_cube_mesh(name,size):
    
    verts = [(0.0, 0.0, 0.0),
             (0.0, size[1], 0.0),
             (size[0], size[1], 0.0),
             (size[0], 0.0, 0.0),
             (0.0, 0.0, size[2]),
             (0.0, size[1], size[2]),
             (size[0], size[1], size[2]),
             (size[0], 0.0, size[2]),
             ]

    faces = [(0, 1, 2, 3),
             (4, 7, 6, 5),
             (0, 4, 5, 1),
             (1, 5, 6, 2),
             (2, 6, 7, 3),
             (4, 0, 3, 7),
            ]
    
    return create_object_from_verts_and_faces(verts,faces,name)

def create_floor_mesh(name,size):
    
    verts = [(0.0, 0.0, 0.0),
             (0.0, size[1], 0.0),
             (size[0], size[1], 0.0),
             (size[0], 0.0, 0.0),
            ]

    faces = [(0, 1, 2, 3),
            ]

    return create_object_from_verts_and_faces(verts,faces,name)

def create_object_from_verts_and_faces(verts,faces,name):
    """ Creates an object from Verties and Faces
        arg1: Verts List of tuples [(float,float,float)]
        arg2: Faces List of ints
        arg3: name of object
    """
    mesh = bpy.data.meshes.new(name)
    
    bm = bmesh.new()

    for v_co in verts:
        bm.verts.new(v_co)
    
    for f_idx in faces:
        bm.verts.ensure_lookup_table()
        bm.faces.new([bm.verts[i] for i in f_idx])
    
    bm.to_mesh(mesh)
    
    mesh.update()
    
    obj_new = bpy.data.objects.new(mesh.name, mesh)
    
    bpy.context.scene.objects.link(obj_new)
    return obj_new
    
#-------OBJECT MODIFICATIONS

def apply_hook_modifiers(obj):
    """ This function applies all of the hook modifers on an object
    """
    obj.hide = False
    obj.select = True
    bpy.context.scene.objects.active = obj
    for mod in obj.modifiers:
        if mod.type == 'HOOK':
            bpy.ops.object.modifier_apply(modifier=mod.name)

def connect_objects_location(anchor_obj,obj):
    """ This function adds a copy location constraint to the obj
        add sets the target to the anchor_obj
    """
    constraint = obj.constraints.new('COPY_LOCATION')
    constraint.target = anchor_obj
    constraint.use_x = True
    constraint.use_y = True
    constraint.use_z = True

def create_vertex_group_for_hooks(obj_mesh,vert_list,vgroupname):
    """ Adds a new vertex group to a mesh. If the group already exists
        Then no group is added. The second parameter allows you to assign
        verts to the vertex group.
        Arg1: bpy.data.Object | Mesh Object to operate on
        Arg2: [] of int | vertext indexs to assign to group
        Arg3: string | vertex group name
    """
    if vgroupname not in obj_mesh.vertex_groups:
        obj_mesh.vertex_groups.new(name=vgroupname)
        
    vgroup = obj_mesh.vertex_groups[vgroupname]
    vgroup.add(vert_list,1,'ADD')

def delete_obj_list(obj_list):
    """ This function deletes every object in the list
    """
    bpy.ops.object.select_all(action='DESELECT')
    
    for obj in obj_list:
        if obj.animation_data:
            for driver in obj.animation_data.drivers:
                if driver.data_path in {'hide','hide_select'}: # THESE DRIVERS MUST BE REMOVED TO DELETE OBJECTS
                    obj.driver_remove(driver.data_path) 
        
        obj.parent = None
        obj.hide_select = False
        obj.hide = False
        obj.select = True
        
        if obj.name in bpy.context.scene.objects:
            bpy.context.scene.objects.unlink(obj)

#     TODO: I HAVE HAD PROBLEMS WITH THIS CRASHING BLENDER    
#           FIGURE OUT HOW TO REMOVE DATA FROM THE BLEND FILE.
#     for obj in obj_list:
#         obj.user_clear()
#         bpy.data.objects.remove(obj)
        
def delete_object_and_children(obj_bp):
    """ Deletes a object and all it's children
    """
    obj_list = []
    obj_list.append(obj_bp)
    for child in obj_bp.children:
        if len(child.children) > 0:
            delete_object_and_children(child)
        else:
            obj_list.append(child)
    delete_obj_list(obj_list)

def hook_vertex_group_to_object(obj_mesh,vertex_group,obj_hook):
    """ This function adds a hook modifier to the verties 
        in the vertex_group to the obj_hook
    """
    bpy.ops.object.select_all(action = 'DESELECT')
    obj_hook.hide = False
    obj_hook.hide_select = False
    obj_hook.select = True
    obj_mesh.hide = False
    obj_mesh.hide_select = False
    if vertex_group in obj_mesh.vertex_groups:
        vgroup = obj_mesh.vertex_groups[vertex_group]
        obj_mesh.vertex_groups.active_index = vgroup.index
        bpy.context.scene.objects.active = obj_mesh
        bpy.ops.fd_object.toggle_edit_mode(object_name=obj_mesh.name)
        bpy.ops.mesh.select_all(action = 'DESELECT')
        bpy.ops.object.vertex_group_select()
        if obj_mesh.data.total_vert_sel > 0:
            bpy.ops.object.hook_add_selob()
        bpy.ops.mesh.select_all(action = 'DESELECT')
        bpy.ops.fd_object.toggle_edit_mode(object_name=obj_mesh.name)
        
def link_objects_to_scene(obj_bp,scene):
    """ This Function links an object and all of it's children
        to the scene
    """
    scene.objects.link(obj_bp)
    for child in obj_bp.children:
        child.draw_type = 'WIRE' #THIS IS USED FOR DRAG AND DROP
        child.select = False
        # This was needed for modal placement to work, 
        # but i dont think it is needed any more
        # I will leave it in as a reminder for now.
#         if child.parent is not None:
#             child.parent = child.parent
        if len(child.children) > 0:
            link_objects_to_scene(child,scene)
        else:
            scene.objects.link(child)
            if child.type == 'EMPTY':
                child.hide = True
    
def run_calculators(obj_bp):
    """ Runs all calculators for an assembly and all it's children assemblies
    """
    for index, page in enumerate(obj_bp.mv.PromptPage.COL_MainTab):
        if page.type == 'CALCULATOR':
            bpy.ops.fd_prompts.run_calculator(tab_index=index,data_name=obj_bp.name,data_type='OBJECT')
    for child in obj_bp.children:
        if child.mv.type == 'BPASSEMBLY':
            run_calculators(child)
    
#-------DRIVER FUNCTIONS
    
def copy_drivers(obj,obj_target):
    """ This Function copies all drivers from obj
        To obj_target. This doesn't include prompt drivers
    """
    if obj.animation_data:
        for driver in obj.animation_data.drivers:
            if 'mv.PromptPage' not in driver.data_path:
                newdriver = None
                try:
                    newdriver = obj_target.driver_add(driver.data_path,driver.array_index)
                except Exception:
                    try:
                        newdriver = obj_target.driver_add(driver.data_path)
                    except Exception:
                        print("Unable to Copy Prompt Driver", driver.data_path)
                if newdriver:
                    newdriver.driver.expression = driver.driver.expression
                    newdriver.driver.type = driver.driver.type
                    for var in driver.driver.variables:
                        if var.name not in newdriver.driver.variables:
                            newvar = newdriver.driver.variables.new()
                            newvar.name = var.name
                            newvar.type = var.type
                            for index, target in enumerate(var.targets):
                                newtarget = newvar.targets[index]
                                if target.id is obj:
                                    newtarget.id = obj_target #CHECK SELF REFERENCE FOR PROMPTS
                                else:
                                    newtarget.id = target.id
                                newtarget.transform_space = target.transform_space
                                newtarget.transform_type = target.transform_type
                                newtarget.data_path = target.data_path

def copy_prompt_drivers(obj,obj_target):
    """ This Function copies all drivers that are 
        assigned to prompts from obj to obj_target.
    """
    if obj.animation_data:
        for driver in obj.animation_data.drivers:
            if 'mv.PromptPage' in driver.data_path:
                for prompt in obj_target.mv.PromptPage.COL_Prompt:
                    newdriver = None
                    if prompt.name in driver.data_path:
                        newdriver = None
                        try:
                            newdriver = obj_target.driver_add(driver.data_path,driver.array_index)
                        except Exception:
                            try:
                                newdriver = obj_target.driver_add(driver.data_path)
                            except Exception:
                                print("Unable to Copy Prompt Driver", driver.data_path)
                    if newdriver:
                        newdriver.driver.expression = driver.driver.expression
                        newdriver.driver.type = driver.driver.type
                        for var in driver.driver.variables:
                            if var.name not in newdriver.driver.variables:
                                newvar = newdriver.driver.variables.new()
                                newvar.name = var.name
                                newvar.type = var.type
                                for index, target in enumerate(var.targets):
                                    newtarget = newvar.targets[index]
                                    if target.id is obj:
                                        newtarget.id = obj_target #CHECK SELF REFERENCE FOR PROMPTS
                                    else:
                                        newtarget.id = target.id
                                    newtarget.transform_space = target.transform_space
                                    newtarget.transform_type = target.transform_type
                                    newtarget.data_path = target.data_path

def add_variables_to_driver(driver,driver_vars):
    """ This function adds the driver_vars to the driver
    """
    for var in driver_vars:
        new_var = driver.driver.variables.new()
        new_var.type = var.var_type
        new_var.name = var.var_name
        new_var.targets[0].data_path = var.data_path
        new_var.targets[0].id = var.obj
        if var.var_type == 'TRANSFORMS':
            new_var.targets[0].transform_space = var.transform_space
            new_var.targets[0].transform_type = var.transform_type

def copy_assembly_drivers(template_assembly,copy_assembly):
    copy_drivers(template_assembly.obj_bp,copy_assembly.obj_bp)
    copy_drivers(template_assembly.obj_x,copy_assembly.obj_x)
    copy_drivers(template_assembly.obj_y,copy_assembly.obj_y)
    copy_drivers(template_assembly.obj_z,copy_assembly.obj_z)
    copy_prompt_drivers(template_assembly.obj_bp,copy_assembly.obj_bp)

#-------UPDATE FILE BROWSER

def update_file_browser_space(context,path):
    """ This function refreshes the file browser space
        with the path that is passed in
    """
    for area in context.screen.areas:
        if area.type == 'FILE_BROWSER':
            for space in area.spaces:
                if space.type == 'FILE_BROWSER':
                    params = space.params
                    params.directory = path
                    if not context.screen.show_fullscreen:
                        params.use_filter = True
                        params.display_type = 'FILE_IMGDISPLAY'
                        params.use_filter_movie = False
                        params.use_filter_script = False
                        params.use_filter_sound = False
                        params.use_filter_text = False
                        params.use_filter_font = False
                        params.use_filter_folder = False
                        params.use_filter_blender = False
                        params.use_filter_image = True
    bpy.ops.file.next() #REFRESH FILEBROWSER INTERFACE


#------- MATERIAL FUNCTIONS

def assign_materials_from_pointers(obj):
    library = bpy.context.scene.cabinetlib
    spec_group = library.spec_groups[obj.cabinetlib.spec_group_index]
    #ASSIGN POINTERS TO MESH BASED ON MESH TYPE
    if obj.cabinetlib.type_mesh == 'CUTPART':
        
        if spec_group:
            if obj.cabinetlib.cutpart_name in spec_group.cutparts:
                cutpart = spec_group.cutparts[obj.cabinetlib.cutpart_name]
                for index, slot in enumerate(obj.cabinetlib.material_slots):
                    if slot.name == 'Core':
                        slot.pointer_name = cutpart.core
                    elif slot.name in {'Top','Exterior'}:
                        slot.pointer_name = cutpart.top
                    elif slot.name in {'Bottom','Interior'}:
                        slot.pointer_name = cutpart.bottom
                    else:
                        if obj.cabinetlib.edgepart_name in spec_group.edgeparts:
                            edgepart = spec_group.edgeparts[obj.cabinetlib.edgepart_name]
                            slot.pointer_name = edgepart.material

                    if slot.pointer_name in spec_group.materials:
                        material_pointer = spec_group.materials[slot.pointer_name]
                        slot.library_name = material_pointer.library_name
                        slot.category_name = material_pointer.category_name
                        slot.item_name = material_pointer.item_name

    elif obj.cabinetlib.type_mesh == 'EDGEBANDING':
        obj.show_bounds = False
        if spec_group:
            if obj.cabinetlib.edgepart_name in spec_group.edgeparts:
                edgepart = spec_group.edgeparts[obj.cabinetlib.edgepart_name]
                for index, slot in enumerate(obj.cabinetlib.material_slots):
                    slot.pointer_name = edgepart.material

                    if slot.pointer_name in spec_group.materials:
                        material_pointer = spec_group.materials[slot.pointer_name]
                        slot.library_name = material_pointer.library_name
                        slot.category_name = material_pointer.category_name
                        slot.item_name = material_pointer.item_name

    elif obj.cabinetlib.type_mesh == 'MACHINING':
        # MAKE A SIMPLE BLACK MATERIAL FOR MACHINING
        for slot in obj.cabinetlib.material_slots:
            slot.library_name = "Plastics"
            slot.category_name = ""
            slot.item_name = "Gloss Black Plastic"
            
    else:
        if spec_group:
            for index, slot in enumerate(obj.cabinetlib.material_slots):
                if slot.pointer_name in spec_group.materials:
                    material_pointer = spec_group.materials[slot.pointer_name]
                    slot.library_name = material_pointer.library_name
                    slot.category_name = material_pointer.category_name
                    slot.item_name = material_pointer.item_name

    #RETRIEVE MATERIAL FROM CATEGORY NAME AND ITEM NAME AND ASSIGN TO SLOT
    for index, slot in enumerate(obj.cabinetlib.material_slots):
        material = get_material((slot.library_name,slot.category_name),slot.item_name)
        if material:
            obj.material_slots[index].material = material

    #MAKE SURE OBJECT IS TEXTURED
    if obj.mv.type == 'CAGE':
        obj.draw_type = 'WIRE'
    else:
        obj.draw_type = 'TEXTURED'



def format_material_name(thickness,core,exterior,interior):
    if core == exterior:
        exterior = "-"
    
    if core == interior:
        interior = "-"
        
    return thickness + " " + core + " _ " + exterior + " _ " + interior

def get_material_name_from_pointer(pointer,spec_group):
    
    thickness = str(round(meter_to_unit(pointer.thickness),4))
    if pointer.core in spec_group.materials:
        core_material = spec_group.materials[pointer.core].item_name
    else:
        core_material = "NA"
    if pointer.top in spec_group.materials:
        top_material = spec_group.materials[pointer.top].item_name
    else:
        top_material = "NA"
    if pointer.bottom in spec_group.materials:
        bottom_material = spec_group.materials[pointer.bottom].item_name
    else:
        bottom_material = "NA"
    return format_material_name(thickness,core_material,top_material,bottom_material)

def get_edgebanding_name_from_pointer_name(pointer_name,spec_group):
    if pointer_name in spec_group.edgeparts:
        pointer = spec_group.edgeparts[pointer_name]
        thickness = str(round(meter_to_unit(pointer.thickness),4))
        material = spec_group.materials[pointer.material].item_name
        return thickness + " " + material
    else:
        return ""

def get_part_thickness(obj):
    if obj.cabinetlib.type_mesh == 'CUTPART':
        spec_group = bpy.context.scene.cabinetlib.spec_groups[obj.cabinetlib.spec_group_index]
        if obj.cabinetlib.cutpart_name in spec_group.cutparts:
            return spec_group.cutparts[obj.cabinetlib.cutpart_name].thickness
        else:
            if obj.parent:
                for child in obj.parent.children:
                    if child.mv.type == 'VPDIMZ':
                        return math.fabs(child.location.z)
    if obj.cabinetlib.type_mesh == 'EDGEBANDING':
        for mod in obj.modifiers:
            if mod.type == 'SOLIDIFY':
                return mod.thickness

def get_material_name(obj):
    if obj.cabinetlib.type_mesh in {'CUTPART','EDGEBANDING'}:
        thickness = str(round(meter_to_unit(get_part_thickness(obj)),4))
        core = ""
        exterior = ""
        interior = ""
        for mv_slot in obj.cabinetlib.material_slots:
            if mv_slot.name == 'Core':
                core = mv_slot.item_name
            if mv_slot.name in {'Top','Exterior'}:
                exterior = mv_slot.item_name
            if mv_slot.name in {'Bottom','Interior'}:
                interior = mv_slot.item_name
                
        return format_material_name(thickness,core,exterior,interior)
    
#-------LIBRARY DATA

def get_library_path_file():
    """ Returns the path to the file that stores all of the library paths.
    """
    path = os.path.join(bpy.utils.user_resource('SCRIPTS'), "fluid_designer")

    if not os.path.exists(path):
        os.makedirs(path)
        
    return os.path.join(path,LIBRARY_PATH_FILENAME)

def get_library_scripts_dir():
    if os.path.exists(bpy.context.window_manager.mv.library_module_path):
        return bpy.context.window_manager.mv.library_module_path
    else:
        return os.path.join(os.path.dirname(bpy.app.binary_path),str(bpy.app.version[0]) + "." + str(bpy.app.version[1]),"scripts","libraries")

def get_library_modules():
    modules = []
    if os.path.exists(bpy.context.window_manager.mv.library_module_path):
        path = bpy.context.window_manager.mv.library_module_path
    else:
        path = get_library_scripts_dir()
        
    if os.path.exists(path):
        files = os.listdir(path)
        for file in files:
            module_name, ext = os.path.splitext(file)
            if ext == ".py": #Look For Library Modules
                modules.append(module_name)  
            
    return modules

def get_library_dir(lib_type = ""):
    if lib_type == 'scenes':
        if os.path.exists(bpy.context.window_manager.mv.scene_library_path):
            return bpy.context.window_manager.mv.scene_library_path
    if lib_type == 'projects':
        if os.path.exists(bpy.context.window_manager.mv.project_path):
            return bpy.context.window_manager.mv.project_path
    if lib_type == 'project_templates':
        if os.path.exists(bpy.context.window_manager.mv.project_template_path):
            return bpy.context.window_manager.mv.project_template_path
    if lib_type == 'products':
        if os.path.exists(bpy.context.window_manager.mv.product_library_path):
            return bpy.context.window_manager.mv.product_library_path
    if lib_type == 'inserts':
        if os.path.exists(bpy.context.window_manager.mv.insert_library_path):
            return bpy.context.window_manager.mv.insert_library_path
    if lib_type == 'assemblies':
        if os.path.exists(bpy.context.window_manager.mv.assembly_library_path):
            return bpy.context.window_manager.mv.assembly_library_path
    if lib_type == 'objects':
        if os.path.exists(bpy.context.window_manager.mv.object_library_path):
            return bpy.context.window_manager.mv.object_library_path
    if lib_type == 'materials':
        if os.path.exists(bpy.context.window_manager.mv.material_library_path):
            return bpy.context.window_manager.mv.material_library_path
    if lib_type == 'worlds':
        if os.path.exists(bpy.context.window_manager.mv.world_library_path):
            return bpy.context.window_manager.mv.world_library_path
        
    # Get Default Path
    app_path = os.path.dirname(bpy.app.binary_path)
    root_path = os.path.join(app_path,"data")
    if lib_type == "":
        return root_path
    else:
        return os.path.join(root_path,lib_type)

def get_product_class(library_name,category_name,product_name):
    modules = get_library_modules()
    for module in modules:
        mod = __import__(module)
        for name, obj in inspect.getmembers(mod):
            if inspect.isclass(obj) and "PRODUCT_" in name:
                product = obj()
                if product.library_name == library_name and product.category_name == category_name and product.assembly_name == product_name:
                    return product

def get_insert_class(library_name,category_name,product_name):
    modules = get_library_modules()
    for module in modules:
        mod = __import__(module)
        for name, obj in inspect.getmembers(mod):
            if inspect.isclass(obj) and "INSERT_" in name:
                product = obj()
                if product.library_name == library_name and product.category_name == category_name and product.assembly_name == product_name:
                    return product

def get_assembly(folders,assembly_name):
    search_directory = get_library_dir("assemblies")
    for folder in folders:
        search_directory = os.path.join(search_directory,folder)
    files = os.listdir(search_directory)
    possible_files = []

    # Add the blend file with the same name to the list first so it is searched first
    if assembly_name + ".blend" in files:
        possible_files.append(os.path.join(search_directory,assembly_name + ".blend"))
      
    for file in files:
        blendname, ext = os.path.splitext(file)
        if ext == ".blend":
            possible_files.append(os.path.join(search_directory,file))
              
    for file in possible_files:
        with bpy.data.libraries.load(file, False, False) as (data_from, data_to):
            for group in data_from.groups:
                if group == assembly_name:
                    data_to.groups = [group]
                    break
  
        for grp in data_to.groups:
            assembly = Assembly(get_assembly_bp(grp.objects[0]))
            link_objects_to_scene(assembly.obj_bp,bpy.context.scene)
            bpy.data.groups.remove(grp)
            return assembly

def get_material(folders,material_name):
    if material_name in bpy.data.materials:
        return bpy.data.materials[material_name]
    search_directory = get_library_dir("materials")
    for folder in folders:
        search_directory = os.path.join(search_directory,folder)

    if os.path.isdir(search_directory):
        files = os.listdir(search_directory)
        possible_files = []
        # Add the blend file with the same name to the list first so it is searched first
        if material_name + ".blend" in files:
            possible_files.append(os.path.join(search_directory,material_name + ".blend"))
          
        for file in files:
            blendname, ext = os.path.splitext(file)
            if ext == ".blend":
                possible_files.append(os.path.join(search_directory,file))
                  
        for file in possible_files:
            with bpy.data.libraries.load(file, False, False) as (data_from, data_to):
                for mat in data_from.materials:
                    if mat == material_name:
                        data_to.materials = [mat]
                        break
      
            for mat in data_to.materials:
                return mat

def get_object(folders,object_name):
    search_directory = get_library_dir("objects")
    for folder in folders:
        search_directory = os.path.join(search_directory,folder)
    files = os.listdir(search_directory)
    possible_files = []
    # Add the blend file with the same name to the list first so it is searched first
    if object_name + ".blend" in files:
        possible_files.append(os.path.join(search_directory,object_name + ".blend"))
      
    for file in files:
        blendname, ext = os.path.splitext(file)
        if ext == ".blend":
            possible_files.append(os.path.join(search_directory,file))
              
    for file in possible_files:
        with bpy.data.libraries.load(file, False, False) as (data_from, data_to):
            for obj in data_from.objects:
                if obj == object_name:
                    data_to.objects = [obj]
                    break
  
        for obj in data_to.objects:
            link_objects_to_scene(obj,bpy.context.scene)
            return obj

def render_thumbnail(assembly):
    if assembly.obj_bp.cabinetlib.type_group == 'PRODUCT':
        library_path = os.path.join(get_library_dir("products"),assembly.library_name,assembly.category_name)
    if assembly.obj_bp.cabinetlib.type_group == 'INSERT':
        library_path = os.path.join(get_library_dir("inserts"),assembly.library_name,assembly.category_name)
    thumbnail_path = os.path.join(library_path,assembly.assembly_name)

    rendering_space = inches(10)

    renderbox = Assembly()
    renderbox.create_assembly()
    renderbox.obj_bp.location = assembly.obj_bp.location
    renderbox.obj_x.location.x = assembly.obj_x.location.x + rendering_space
    renderbox.obj_y.location.y = assembly.obj_y.location.y - rendering_space

    if assembly.obj_z.location.z > 0:
        renderbox.obj_z.location.z = assembly.obj_z.location.z + rendering_space
    else:
        renderbox.obj_bp.location.z += rendering_space/2
        renderbox.obj_z.location.z = assembly.obj_z.location.z - rendering_space
      
    cage = renderbox.get_cage()
    cage.hide_select = False
    cage.select = True
    bpy.ops.view3d.camera_to_view_selected()
    renderbox.delete_cage()
       
#     self.group.set_prompt('Door Rotation',math.radians(40))
    
    init_objects(assembly.obj_bp)
    
    render = bpy.context.scene.render
    render.use_file_extension = True
    render.filepath = thumbnail_path
    bpy.ops.render.render(write_still=True)

def set_object_name(obj):
    """ This function sets the name of an object to make the outliner easier to navigate
    """
    counter = str(obj.cabinetlib.item_number)
    if obj.mv.type in {'VPDIMX','VPDIMY','VPDIMZ'}:
        obj.name = counter + '.' + obj.mv.type + '.' + obj.parent.mv.name_object if obj.parent else obj.mv.name_object
    elif obj.mv.type == 'BPASSEMBLY':
        if obj.cabinetlib.type_group in {'PRODUCT','INSERT','OPENING'}:
            obj.name = counter + '.' + obj.cabinetlib.type_group + '.' + obj.mv.name_object   
        else:
            obj.name = counter + '.BPASSEMBLY.' + obj.mv.name_object   
    elif obj.cabinetlib.type_mesh != 'NONE':
        obj.name = counter + '.' + obj.cabinetlib.type_mesh + '.' + obj.parent.mv.name_object + '.' + obj.mv.name_object
    elif obj.mv.type in {'VISDIM_A','VISDIM_B'}:
        obj.name = counter + '.DIMENSION.' + obj.parent.mv.name_object + '.' + obj.mv.name_object
    else:
        obj.name = counter + '.' + obj.type + '.' + obj.mv.name_object

def init_objects(obj_bp):
    """ This Function is used to init all of the objects in a smart group
            -Sets the names of the children
            -Hides all of the empties
            -Deletes the cage objects
            -Sets the materials
    """
    obj_cages = []
    set_object_name(obj_bp)
    for child in obj_bp.children:
        set_object_name(child)

        if child.type == 'EMPTY':
            child.hide = True
            
        if child.mv.type == 'CAGE':
            obj_cages.append(child)
            
        if child.type == 'MESH':
            assign_materials_from_pointers(child)

        if child.mv.type == 'VISDIM_A':
            child.hide = True
            for dim_child in child.children:
                dim_child.hide = True

        if child.mv.type == 'BPASSEMBLY':
            init_objects(child)
         
        if child.mv.use_as_bool_obj:
            print('WIRE',child)
            child.draw_type = 'WIRE'
         
    if len(obj_cages) > 0:
        delete_obj_list(obj_cages)

def get_previews(path,key):
    enum_items = []
    if len(key.my_previews) > 0:
        return key.my_previews
    
    if path and os.path.exists(path):
        image_paths = []
        for fn in os.listdir(path):
            if fn.lower().endswith(".png"):
                image_paths.append(fn)

        for i, name in enumerate(image_paths):
            filepath = os.path.join(path, name)
            thumb = key.load(filepath, filepath, 'IMAGE')
            filename, ext = os.path.splitext(name)
            enum_items.append((filename, filename, filename, thumb.icon_id, i))
#             enum_items.append((filename, filename, filepath, thumb.icon_id, i))
    
    key.my_previews = enum_items
    key.my_previews_dir = path
    return key.my_previews

#-------DATA GETTERS
def get_version_string():
    version = bpy.app.version
    return str(version[0]) + "." + str(version[1])

def get_bp(obj,group_type):
    if obj:
        if obj.cabinetlib.type_group == group_type and obj.mv.type == 'BPASSEMBLY':
            return obj
        else:
            if obj.parent:
                return get_bp(obj.parent,group_type)

def get_wall_bp(obj):
    """ This will get the wall base point from the passed in object
    """
    if obj:
        if obj.mv.type == 'BPWALL':
            return obj
        else:
            if obj.parent:
                return get_wall_bp(obj.parent)
            
def get_parent_assembly_bp(obj):
    """ This will get the top level group base point from the passed in object
    """
    if obj:
        if obj.parent:
            if obj.parent.mv.type == 'BPASSEMBLY':
                return get_parent_assembly_bp(obj.parent)
            else:
                if obj.parent.mv.type == 'BPWALL' and obj.mv.type == 'BPASSEMBLY':
                    return obj
        else:
            if obj.mv.type == 'BPASSEMBLY':
                return obj
            
def get_assembly_bp(obj):
    """ This will get the group base point from the passed in object
    """
    if obj:
        if obj.mv.type == 'BPASSEMBLY':
            return obj
        else:
            if obj.parent:
                return get_assembly_bp(obj.parent)

def get_insert_bp_list(obj_bp,insert_list):
    for child in obj_bp.children:
        if child.mv.type == 'BPASSEMBLY' and child.cabinetlib.type_group == 'INSERT':
            insert_list.append(child)
            get_insert_bp_list(child,insert_list)

    if len(insert_list) > 0:
        insert_list.sort(key=lambda obj: obj.location.z, reverse=True)
    return insert_list

#TODO: THIS SHOULD BE MOVED TO THE GROUP CLASS
def get_collision_location(obj_product_bp,direction='LEFT',get_product_bp=None):
    group = Assembly(obj_product_bp)
    if group.obj_bp.parent:
        wall = Wall(group.obj_bp.parent)
    list_obj_bp = wall.get_wall_groups()
    list_obj_left_bp = []
    list_obj_right_bp = []
    for index, obj_bp in enumerate(list_obj_bp):
        if obj_bp.name == group.obj_bp.name:
            list_obj_left_bp = list_obj_bp[:index]
            list_obj_right_bp = list_obj_bp[index + 1:]
            break
    if direction == 'LEFT':
        list_obj_left_bp.reverse()
        for obj_bp in list_obj_left_bp:
            prev_group = Assembly(obj_bp)
            if group.has_height_collision(prev_group):
                return obj_bp.location.x + prev_group.calc_width()
        
        # CHECK NEXT WALL
#         if math.radians(wall.obj_bp.rotation_euler.z) < 0:
        left_wall =  wall.get_connected_wall('LEFT')
        if left_wall:
            rotation_difference = wall.obj_bp.rotation_euler.z - left_wall.obj_bp.rotation_euler.z
            if rotation_difference < 0:
                list_obj_bp = left_wall.get_wall_groups()
                for obj in list_obj_bp:
                    prev_group = Assembly(obj)
                    product_x = obj.location.x
                    product_width = prev_group.calc_width()
                    x_dist = left_wall.obj_x.location.x  - (product_x + product_width)
                    product_depth = math.fabs(group.obj_y.location.y)
                    if x_dist <= product_depth:
                        if group.has_height_collision(prev_group):
                            return prev_group.calc_depth()
        return 0
    
    if direction == 'RIGHT':
        for obj_bp in list_obj_right_bp:
            next_group = Assembly(obj_bp)
            if group.has_height_collision(next_group):
                return obj_bp.location.x - next_group.calc_x()

        # CHECK NEXT WALL
        right_wall =  wall.get_connected_wall('RIGHT')
        if right_wall:
            rotation_difference = wall.obj_bp.rotation_euler.z - right_wall.obj_bp.rotation_euler.z
            if rotation_difference > 0:
                list_obj_bp = right_wall.get_wall_groups()
                for obj in list_obj_bp:
                    next_group = Assembly(obj)
                    product_x = obj.location.x
                    product_width = next_group.calc_width()
                    product_depth = math.fabs(group.obj_y.location.y)
                    if product_x <= product_depth:
                        if group.has_height_collision(next_group):
                            wall_length = wall.obj_x.location.x
                            product_depth = next_group.calc_depth()
                            return wall_length - product_depth

        return wall.obj_x.location.x

def get_driver(obj,data_path,array_index):
    if obj.animation_data:
        for DR in obj.animation_data.drivers:
            if DR.data_path == data_path and DR.array_index == array_index:
                return DR

def get_child_objects(obj,obj_list=None):
    #USED IN CABINET LIBRARY
    if not obj_list:
        obj_list = []
    if obj not in obj_list:
        obj_list.append(obj)
    for child in obj.children:
        obj_list.append(child)
        get_child_objects(child,obj_list)
    return obj_list

def get_selected_file_from_file_browser(context):
    #THIS IS USED BY THE CABINET LIBRARY
    window = context.window
    for area in window.screen.areas:
        if area.type == 'FILE_BROWSER':
            for space in area.spaces:
                if space.type == 'FILE_BROWSER':
                    return os.path.join(space.params.directory,space.params.filename)
                
def get_file_browser_path(context):
    for area in context.screen.areas:
        if area.type == 'FILE_BROWSER':
            for space in area.spaces:
                if space.type == 'FILE_BROWSER':
                    params = space.params
                    return params.directory
                
def get_prop_dialog_width(width):
    """ This function returns the width of a property dialog box in pixels
        This is needed to fix scaling issues with 4k monitors
        TODO: test if this works on the linux and apple OS
    """
    import ctypes
    screen_resolution_width = ctypes.windll.user32.GetSystemMetrics(0)
    if screen_resolution_width > 3000: # There is probably a beter way to check if the monitor is 4K
        return width * 2
    else:
        return width
                
def get_next_wall(assembly,placement):
    """ This gets the next LEFT or RIGHT wall that this product is connected to
        This is used for placing product on corner cabinets that are in corners
    """
    if assembly.obj_bp.parent:
        wall = Wall(assembly.obj_bp.parent)
        
        if placement == 'LEFT':
            # Check if base the closer than 1" to the left side 
            if assembly.obj_bp.location.x < inches(1):
                left_wall = wall.get_connected_wall('LEFT')
                if left_wall:
                    rotation_difference = wall.obj_bp.rotation_euler.z - left_wall.obj_bp.rotation_euler.z
                    if rotation_difference < 0:
                        return left_wall

        if placement == 'RIGHT':
            # Check if base the closer than 1" to the right side 
            if (wall.obj_x.location.x - assembly.obj_bp.location.x) < inches(1):
                right_wall = wall.get_connected_wall('RIGHT')
                if right_wall:
                    rotation_difference = wall.obj_bp.rotation_euler.z - right_wall.obj_bp.rotation_euler.z
                    if rotation_difference > 0:
                        return right_wall
                
#-------MATH & GEO FUNCTIONS

def calc_distance(point1,point2):
    """ This gets the distance between two points (X,Y,Z)
    """
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2 + (point1[2]-point2[2])**2) 

#-------MODAL CALLBACKS
    
def get_selection_point(context, event, ray_max=10000.0,objects=None):
    """Gets the point to place an object based on selection"""
    # get the context arguments
    scene = context.scene
    region = context.region
    rv3d = context.region_data
    coord = event.mouse_region_x, event.mouse_region_y

    # get the ray from the viewport and mouse
    view_vector = view3d_utils.region_2d_to_vector_3d(region, rv3d, coord)
    ray_origin = view3d_utils.region_2d_to_origin_3d(region, rv3d, coord)
    ray_target = ray_origin + (view_vector * ray_max)

    def visible_objects_and_duplis():
        """Loop over (object, matrix) pairs (mesh only)"""

        for obj in context.visible_objects:
            
            if objects:
                if obj in objects:
                    yield (obj, obj.matrix_world.copy())
            
            else:
                if obj.draw_type != 'WIRE':
                    if obj.type == 'MESH':
                        if obj.mv.type not in {'BPASSEMBLY','BPWALL'}:
                            yield (obj, obj.matrix_world.copy())
        
                    if obj.dupli_type != 'NONE':
                        obj.dupli_list_create(scene)
                        for dob in obj.dupli_list:
                            obj_dupli = dob.object
                            if obj_dupli.type == 'MESH':
                                yield (obj_dupli, dob.matrix.copy())

            obj.dupli_list_clear()

    def obj_ray_cast(obj, matrix):
        """Wrapper for ray casting that moves the ray into object space"""
        try:
            # get the ray relative to the object
            matrix_inv = matrix.inverted()
            ray_origin_obj = matrix_inv * ray_origin
            ray_target_obj = matrix_inv * ray_target
    
            # cast the ray
            hit, normal, face_index = obj.ray_cast(ray_origin_obj, ray_target_obj)
    
            if face_index != -1:
                return hit, normal, face_index
            else:
                return None, None, None
        except:
            print("ERROR IN obj_ray_cast",obj)
            return None, None, None
            
    best_length_squared = ray_max * ray_max
    best_obj = None
    best_hit = scene.cursor_location
    for obj, matrix in visible_objects_and_duplis():
        if obj.type == 'MESH':
            if obj.data:
                hit, normal, face_index = obj_ray_cast(obj, matrix)
                if hit is not None:
                    hit_world = matrix * hit
                    length_squared = (hit_world - ray_origin).length_squared
                    if length_squared < best_length_squared:
                        best_hit = hit_world
                        best_length_squared = length_squared
                        best_obj = obj
                        
    return best_hit, best_obj
    
def draw_callback_px(self, context):
    font_id = 0  # XXX, need to find out how best to get this.

    offset = 10
    text_height = 10
    text_length = int(len(self.mouse_text) * 7.3)
    
    if self.header_text != "":
        blf.size(font_id, 17, 72)
        text_w, text_h = blf.dimensions(font_id,self.header_text)
        blf.position(font_id, context.area.width/2 - text_w/2, context.area.height - 50, 0)
        blf.draw(font_id, self.header_text)

    # 50% alpha, 2 pixel width line
    if self.mouse_text != "":
        bgl.glEnable(bgl.GL_BLEND)
        bgl.glColor4f(0.0, 0.0, 0.0, 0.5)
        bgl.glLineWidth(10)
    
        bgl.glBegin(bgl.GL_LINE_STRIP)
        bgl.glVertex2i(self.mouse_loc[0]-offset-5, self.mouse_loc[1]+offset)
        bgl.glVertex2i(self.mouse_loc[0]+text_length-offset, self.mouse_loc[1]+offset)
        bgl.glVertex2i(self.mouse_loc[0]+text_length-offset, self.mouse_loc[1]+offset+text_height)
        bgl.glVertex2i(self.mouse_loc[0]-offset-5, self.mouse_loc[1]+offset+text_height)
        bgl.glEnd()
        
        bgl.glColor4f(1.0, 1.0, 1.0, 1.0)
        blf.position(font_id, self.mouse_loc[0]-offset, self.mouse_loc[1]+offset, 0)
        blf.size(font_id, 15, 72)
        blf.draw(font_id, self.mouse_text)
        
    # restore opengl defaults
    bgl.glLineWidth(1)
    bgl.glDisable(bgl.GL_BLEND)
    bgl.glColor4f(0.0, 0.0, 0.0, 1.0)
    
def draw_opengl(self,context):
    context = bpy.context
    if context.window_manager.mv.use_opengl_dimensions:
        region = bpy.context.region
        #---------- if Quadview
        if not context.space_data.region_quadviews:
            rv3d = bpy.context.space_data.region_3d
        else:
            if context.area.type != 'VIEW_3D' or context.space_data.type != 'VIEW_3D':
                return
            i = -1
            for region in context.area.regions:
                if region.type == 'WINDOW':
                    i += 1
                    if context.region.id == region.id:
                        break
            else:
                return
    
            rv3d = context.space_data.region_quadviews[i]
        
        layers = []
        for x in range(0, 20):
            if bpy.context.scene.layers[x] is True:
                layers.extend([x])
    
        objlist = context.scene.objects
    
        bgl.glEnable(bgl.GL_BLEND)
    
        for obj in objlist:
            if obj.mv.type == 'VISDIM_A':
                for x in range(0, 20):
                    if obj.layers[x] is True:
                        if x in layers:
                            opengl_dim = obj.mv.opengl_dim
                            if not opengl_dim.hide:
                                draw_dimensions(context, obj, opengl_dim, region, rv3d)
                        break
    
        #---------- restore opengl defaults
        bgl.glLineWidth(1)
        bgl.glDisable(bgl.GL_BLEND)
        bgl.glColor4f(0.0, 0.0, 0.0, 1.0)    
    
    else:
        return
    
#-------UNIT CONVERSION

def unit(number):
    # THIS IS USED BY THE CABINET LIBRARY FOR EXPORTING XML DATA
    if bpy.context.scene.unit_settings.system == 'METRIC':
        number = number * 1000 #METER TO MILLIMETER
    else:
        number = meter_to_unit(number) #METER TO INCH
    return number

def meter_to_unit(number):
    """ converts meter to current unit
    """
    if bpy.context.scene.unit_settings.system == 'METRIC':
        return number * 100
    else:
        return round(number * 39.3700787,4)

def inches(number):
    """ Converts Inch to meter
    """
    return round(number / 39.3700787,6)

def millimeters(number):
    """ Converts Millimeter to meter
    """
    return number * .001

#----------- OpenGL Drawing

def draw_dimensions(context, obj, opengl_dim, region, rv3d):
    scene_ogl_dim_props = bpy.context.scene.mv.opengl_dim
    pr = scene_ogl_dim_props.gl_precision
    fmt = "%1." + str(pr) + "f"
    units = scene_ogl_dim_props.gl_dim_units
    fsize = scene_ogl_dim_props.gl_font_size    
    a_size = scene_ogl_dim_props.gl_arrow_size
    a_type = scene_ogl_dim_props.gl_arrow_type
    b_type = scene_ogl_dim_props.gl_arrow_type
    
    if opengl_dim.gl_color == 0:
        rgb = scene_ogl_dim_props.gl_default_color
    elif opengl_dim.gl_color == 1:
        #WHITE
        rgb = (0.8,0.8,0.8,1.0)
    elif opengl_dim.gl_color == 2:
        #BLACK
        rgb = (0.1,0.1,0.1,1.0)        
    elif opengl_dim.gl_color == 3:
        #RED
        rgb = (0.8,0.0,0.0,1.0)
    elif opengl_dim.gl_color == 4:
        #GREEN
        rgb = (0.0,0.8,0.0,1.0)
    elif opengl_dim.gl_color == 5:
        #BLUE
        rgb = (0.0,0.0,0.8,1.0)
    elif opengl_dim.gl_color == 6:
        #YELLOW
        rgb = (0.8,0.8,0.0,1.0)          
    elif opengl_dim.gl_color == 7:
        #AQUA
        rgb = (0.0,0.8,0.8,1.0) 
    elif opengl_dim.gl_color == 8:
        #VIOLET
        rgb = (0.8,0.0,0.8,1.0)                               

    a_p1 = get_location(obj)
    
    for child in obj.children:
        if child.mv.type == 'VISDIM_B':
            b_p1 = get_location(child)

    dist = calc_distance(a_p1, b_p1)  

    loc = get_location(obj)
    midpoint3d = interpolate3d(a_p1, b_p1, math.fabs(dist / 2))
    vn = mathutils.Vector((midpoint3d[0] - loc[0],
                           midpoint3d[1] - loc[1],
                           midpoint3d[2] - loc[2]))

    vn.normalize()
    
    v1 = [a_p1[0], a_p1[1], a_p1[2]]
    v2 = [b_p1[0], b_p1[1], b_p1[2]]    
    
    screen_point_ap1 = get_2d_point(region, rv3d, a_p1)
    screen_point_bp1 = get_2d_point(region, rv3d, b_p1)
    
    if None in (screen_point_ap1,screen_point_bp1):
        return
    
    bgl.glLineWidth(opengl_dim.gl_width)
    bgl.glColor4f(rgb[0], rgb[1], rgb[2], rgb[3])
        
    midpoint3d = interpolate3d(v1, v2, math.fabs(dist / 2))
    gap3d = (midpoint3d[0], midpoint3d[1], midpoint3d[2] + 0.014)
    txtpoint2d = get_2d_point(region, rv3d, gap3d)
    
    if opengl_dim.gl_label == "":
        txt_dist = str(format_distance(fmt, units, dist))
    else:
        txt_dist = opengl_dim.gl_label

    draw_text(txtpoint2d[0] + opengl_dim.gl_text_x, 
              txtpoint2d[1] + opengl_dim.gl_text_y,
              txt_dist, 
              rgb, 
              fsize)

    bgl.glEnable(bgl.GL_BLEND)
    bgl.glColor4f(rgb[0], rgb[1], rgb[2], rgb[3])      

    draw_arrow(screen_point_ap1, screen_point_bp1, a_size, a_type, b_type)  
    
    draw_extension_lines(screen_point_ap1, screen_point_bp1, a_size)

def draw_text(x_pos, y_pos, display_text, rgb, fsize):
    font_id = 0
    blf.size(font_id, fsize, 72)
    #- height of one line
    mwidth, mheight = blf.dimensions(font_id, "Tp")  # uses high/low letters

    # split lines
    mylines = display_text.split("|")
    idx = len(mylines) - 1
    maxwidth = 0
    maxheight = len(mylines) * mheight

    #---------- Draw all lines-+
    for line in mylines:
        text_width, text_height = blf.dimensions(font_id, line)
            
        # calculate new Y position
        new_y = y_pos + (mheight * idx)
        # Draw
        blf.position(font_id, x_pos - (text_width/2), new_y, 0)
        bgl.glColor4f(rgb[0], rgb[1], rgb[2], rgb[3])
        blf.draw(font_id, " " + line)
        
        # sub line
        idx -= 1
        # saves max width
        if maxwidth < text_width:
            maxwidth = text_width

    return maxwidth, maxheight

def format_distance(fmt, units, value, factor=1):
    s_code = "\u00b2"  # Superscript two
    #---------- Units automatic
    if units == "1":
        # Units
        if bpy.context.scene.unit_settings.system == "IMPERIAL":
            feet = value * (3.2808399 ** factor)
            if round(feet, 2) >= 1.0:
                fmt += "'"
                if factor == 2:
                    fmt += s_code
                tx_dist = fmt % feet
            else:
                inches = value * (39.3700787 ** factor)
                fmt += '"'
                if factor == 2:
                    fmt += s_code
                tx_dist = fmt % inches
        elif bpy.context.scene.unit_settings.system == "METRIC":
            if round(value, 2) >= 1.0:
                fmt += " m"
                if factor == 2:
                    fmt += s_code
                tx_dist = fmt % value
            else:
                if round(value, 2) >= 0.01:
                    fmt += " cm"
                    if factor == 2:
                        fmt += s_code
                    d_cm = value * (100 ** factor)
                    tx_dist = fmt % d_cm
                else:
                    fmt += " mm"
                    if factor == 2:
                        fmt += s_code
                    d_mm = value * (1000 ** factor)
                    tx_dist = fmt % d_mm
        else:
            tx_dist = fmt % value

    #---------- Units meters
    elif units == "2":
        fmt += " m"
        if factor == 2:
            fmt += s_code
        tx_dist = fmt % value

    #---------- Units centimeters
    elif units == "3":
        fmt += " cm"
        if factor == 2:
            fmt += s_code
        d_cm = value * (100 ** factor)
        tx_dist = fmt % d_cm

    #---------- Units millimeters
    elif units == "4":
        fmt += " mm"
        if factor == 2:
            fmt += s_code
        d_mm = value * (1000 ** factor)
        tx_dist = fmt % d_mm

    #---------- Units feet
    elif units == "5":
        fmt += "'"
        if factor == 2:
            fmt += s_code
        feet = value * (3.2808399 ** factor)
        tx_dist = fmt % feet

    #---------- Units inches
    elif units == "6":
        fmt += '"'
        if factor == 2:
            fmt += s_code
        inches = value * (39.3700787 ** factor)
        tx_dist = fmt % inches
        
    #--------------- Default
    else:
        tx_dist = fmt % value

    return tx_dist

def draw_extension_lines(v1, v2, size=20):
    rad_a = math.radians(90)
    rad_b = math.radians(270)

    v = interpolate3d((v1[0], v1[1], 0.0), (v2[0], v2[1], 0.0), size)
    v1i = (v[0] - v1[0], v[1] - v1[1])

    v = interpolate3d((v2[0], v2[1], 0.0), (v1[0], v1[1], 0.0), size)
    v2i = (v[0] - v2[0], v[1] - v2[1])

    v1a = (int(v1i[0] * math.cos(rad_a) - v1i[1] * math.sin(rad_a) + v1[0]),
           int(v1i[1] * math.cos(rad_a) + v1i[0] * math.sin(rad_a)) + v1[1])
    v1b = (int(v1i[0] * math.cos(rad_b) - v1i[1] * math.sin(rad_b) + v1[0]),
           int(v1i[1] * math.cos(rad_b) + v1i[0] * math.sin(rad_b) + v1[1]))

    v2a = (int(v2i[0] * math.cos(rad_a) - v2i[1] * math.sin(rad_a) + v2[0]),
           int(v2i[1] * math.cos(rad_a) + v2i[0] * math.sin(rad_a)) + v2[1])
    v2b = (int(v2i[0] * math.cos(rad_b) - v2i[1] * math.sin(rad_b) + v2[0]),
           int(v2i[1] * math.cos(rad_b) + v2i[0] * math.sin(rad_b) + v2[1]))
    
    draw_line(v1, v1a)
    draw_line(v1, v1b)
    
    draw_line(v2, v2a)
    draw_line(v2, v2b)

def draw_arrow(v1, v2, size=20, a_typ="1", b_typ="1"):
    rad45 = math.radians(45)
    rad315 = math.radians(315)
    rad90 = math.radians(90)
    rad270 = math.radians(270)

    v = interpolate3d((v1[0], v1[1], 0.0), (v2[0], v2[1], 0.0), size)

    v1i = (v[0] - v1[0], v[1] - v1[1])

    v = interpolate3d((v2[0], v2[1], 0.0), (v1[0], v1[1], 0.0), size)
    v2i = (v[0] - v2[0], v[1] - v2[1])

    if a_typ == "3":
        rad_a = rad90
        rad_b = rad270
    else:
        rad_a = rad45
        rad_b = rad315

    v1a = (int(v1i[0] * math.cos(rad_a) - v1i[1] * math.sin(rad_a) + v1[0]),
           int(v1i[1] * math.cos(rad_a) + v1i[0] * math.sin(rad_a)) + v1[1])
    v1b = (int(v1i[0] * math.cos(rad_b) - v1i[1] * math.sin(rad_b) + v1[0]),
           int(v1i[1] * math.cos(rad_b) + v1i[0] * math.sin(rad_b) + v1[1]))

    if b_typ == "3":
        rad_a = rad90
        rad_b = rad270
    else:
        rad_a = rad45
        rad_b = rad315

    v2a = (int(v2i[0] * math.cos(rad_a) - v2i[1] * math.sin(rad_a) + v2[0]),
           int(v2i[1] * math.cos(rad_a) + v2i[0] * math.sin(rad_a)) + v2[1])
    v2b = (int(v2i[0] * math.cos(rad_b) - v2i[1] * math.sin(rad_b) + v2[0]),
           int(v2i[1] * math.cos(rad_b) + v2i[0] * math.sin(rad_b) + v2[1]))

    if a_typ == "1" or a_typ == "3":
        draw_line(v1, v1a)
        draw_line(v1, v1b)

    if b_typ == "1" or b_typ == "3":
        draw_line(v2, v2a)
        draw_line(v2, v2b)

    if a_typ == "2":
        draw_triangle(v1, v1a, v1b)
    if b_typ == "2":
        draw_triangle(v2, v2a, v2b)

    draw_line(v1, v2)

def draw_line(v1, v2):
    # noinspection PyBroadException
    try:
        if v1 is not None and v2 is not None:
            bgl.glBegin(bgl.GL_LINES)
            bgl.glVertex2f(*v1)
            bgl.glVertex2f(*v2)
            bgl.glEnd()
    except:
        pass

def draw_triangle(v1, v2, v3):
    # noinspection PyBroadException
    try:
        if v1 is not None and v2 is not None and v3 is not None:
            bgl.glBegin(bgl.GL_TRIANGLES)
            bgl.glVertex2f(*v1)
            bgl.glVertex2f(*v2)
            bgl.glVertex2f(*v3)
            bgl.glEnd()
    except:
        pass

def get_2d_point(region, rv3d, point3d):
    if rv3d is not None and region is not None:
        return view3d_utils.location_3d_to_region_2d(region, rv3d, point3d)
    else:
        return get_render_location(point3d)

def get_render_location(mypoint):
    v1 = mathutils.Vector(mypoint)
    scene = bpy.context.scene
    co_2d = object_utils.world_to_camera_view(scene, scene.camera, v1)
    # Get pixel coords
    render_scale = scene.render.resolution_percentage / 100
    render_size = (int(scene.render.resolution_x * render_scale),
                   int(scene.render.resolution_y * render_scale))

    return [round(co_2d.x * render_size[0]), round(co_2d.y * render_size[1])]

def interpolate3d(v1, v2, d1):
    # calculate vector
    v = (v2[0] - v1[0], v2[1] - v1[1], v2[2] - v1[2])
    # calculate distance between points
    d0 = calc_distance(v1, v2)

    # calculate interpolate factor (distance from origin / distance total)
    # if d1 > d0, the point is projected in 3D space
    if d0 > 0:
        x = d1 / d0
    else:
        x = d1

    final = (v1[0] + (v[0] * x), v1[1] + (v[1] * x), v1[2] + (v[2] * x))
    return final

def get_location(mainobject):
    # Using World Matrix
    m4 = mainobject.matrix_world

    return [m4[0][3], m4[1][3], m4[2][3]]

def render_opengl(self, context):
    from math import ceil

    layers = []
    scene = context.scene
    for x in range(0, 20):
        if scene.layers[x] is True:
            layers.extend([x])

    objlist = context.scene.objects
    render_scale = scene.render.resolution_percentage / 100

    width = int(scene.render.resolution_x * render_scale)
    height = int(scene.render.resolution_y * render_scale)
    
    file_format = context.scene.render.image_settings.file_format.lower()
    
    ren_path = bpy.path.abspath(bpy.context.scene.render.filepath) + "." + file_format
    
#     if len(ren_path) > 0:
#         if ren_path.endswith(os.path.sep):
#             initpath = os.path.realpath(ren_path) + os.path.sep
#         else:
#             (initpath, filename) = os.path.split(ren_path)
#         outpath = os.path.join(initpath, "ogl_tmp.png")
#     else:
#         self.report({'ERROR'}, "Invalid render path")
#         return False

    img = get_render_image(ren_path)
    
    if img is None:
        self.report({'ERROR'}, "Invalid render path")
        return False

    tile_x = 240
    tile_y = 216
    row_num = ceil(height / tile_y)
    col_num = ceil(width / tile_x)
    
    cut4 = (col_num * tile_x * 4) - width * 4  
    totpixel4 = width * height * 4 

    viewport_info = bgl.Buffer(bgl.GL_INT, 4)
    bgl.glGetIntegerv(bgl.GL_VIEWPORT, viewport_info)
    
    img.gl_load(0, bgl.GL_NEAREST, bgl.GL_NEAREST)

    tex = img.bindcode
    
    if context.scene.name in bpy.data.images:
        old_img = bpy.data.images[context.scene.name]
        old_img.user_clear()
        bpy.data.images.remove(old_img)
             
    img_result = bpy.data.images.new(context.scene.name, width, height)        
    
    tmp_pixels = [1] * totpixel4

    #---------- Loop for all tiles
    for row in range(0, row_num):
        for col in range(0, col_num):
            buffer = bgl.Buffer(bgl.GL_FLOAT, width * height * 4)
            bgl.glDisable(bgl.GL_SCISSOR_TEST)  # if remove this line, get blender screenshot not image
            bgl.glViewport(0, 0, tile_x, tile_y)

            bgl.glMatrixMode(bgl.GL_PROJECTION)
            bgl.glLoadIdentity()

            # defines ortographic view for single tile
            x1 = tile_x * col
            y1 = tile_y * row
            bgl.gluOrtho2D(x1, x1 + tile_x, y1, y1 + tile_y)

            # Clear
            bgl.glClearColor(0.0, 0.0, 0.0, 0.0)
            bgl.glClear(bgl.GL_COLOR_BUFFER_BIT | bgl.GL_DEPTH_BUFFER_BIT)

            bgl.glEnable(bgl.GL_TEXTURE_2D)
            bgl.glBindTexture(bgl.GL_TEXTURE_2D, tex)

            # defines drawing area
            bgl.glBegin(bgl.GL_QUADS)

            bgl.glColor3f(1.0, 1.0, 1.0)
            bgl.glTexCoord2f(0.0, 0.0)
            bgl.glVertex2f(0.0, 0.0)

            bgl.glTexCoord2f(1.0, 0.0)
            bgl.glVertex2f(width, 0.0)

            bgl.glTexCoord2f(1.0, 1.0)
            bgl.glVertex2f(width, height)

            bgl.glTexCoord2f(0.0, 1.0)
            bgl.glVertex2f(0.0, height)

            bgl.glEnd()

            for obj in objlist:
                if obj.mv.type == 'VISDIM_A':
                    for x in range(0, 20):
                        if obj.layers[x] is True:
                            if x in layers:
                                opengl_dim = obj.mv.opengl_dim
                                if not opengl_dim.hide:
                                    draw_dimensions(context, obj, opengl_dim, None, None)
                            break 

            #---------- copy pixels to temporary area
            bgl.glFinish()
            bgl.glReadPixels(0, 0, width, height, bgl.GL_RGBA, bgl.GL_FLOAT, buffer)  # read image data
            for y in range(0, tile_y):
                # final image pixels position
                p1 = (y * width * 4) + (row * tile_y * width * 4) + (col * tile_x * 4)
                p2 = p1 + (tile_x * 4)
                # buffer pixels position
                b1 = y * width * 4
                b2 = b1 + (tile_x * 4)

                if p1 < totpixel4:  # avoid pixel row out of area
                    if col == col_num - 1:  # avoid pixel columns out of area
                        p2 -= cut4
                        b2 -= cut4

                    tmp_pixels[p1:p2] = buffer[b1:b2]

    img_result.pixels = tmp_pixels[:]
    img.gl_free()

    img.user_clear()
    bpy.data.images.remove(img)
    os.remove(ren_path)
    bgl.glEnable(bgl.GL_SCISSOR_TEST)

    #---------- restore opengl defaults
    bgl.glLineWidth(1)
    bgl.glDisable(bgl.GL_BLEND)
    bgl.glColor4f(0.0, 0.0, 0.0, 1.0)
    
    if img_result is not None:            
        return img_result

def get_render_image(outpath):
    saved = False
    try:
        try:
            result = bpy.data.images['Render Result']
            if result.has_data is False:
                result.save_render(outpath)
                saved = True
        except:
            print("No render image found")
            return None

        if saved is False:
            result.save_render(outpath)

        img = img_utils.load_image(outpath)

        return img
    except:
        print("Unexpected render image error")
        return None

#----------- COMMON INTERFACES

def draw_modifier(mod,layout,obj):
    
    def draw_show_expanded(mod,layout):
        if mod.show_expanded:
            layout.prop(mod,'show_expanded',text="",emboss=False)
        else:
            layout.prop(mod,'show_expanded',text="",emboss=False)
    
    def draw_apply_close(layout,mod_name):
        layout.operator('object.modifier_apply',text="",icon='EDIT_VEC',emboss=False).modifier = mod.name
        layout.operator('object.modifier_remove',text="",icon='PANEL_CLOSE',emboss=False).modifier = mod.name
    
    def draw_array_modifier(layout):
        col = layout.column(align=True)
        box = col.box()
        row = box.row()
        draw_show_expanded(mod,row)
        row.prop(mod,'name',text="",icon='MOD_ARRAY')
        draw_apply_close(row,mod.name)
        
        if mod.show_expanded:
            box = col.box()
            box.prop(mod, "fit_type")
    
            if mod.fit_type == 'FIXED_COUNT':
                box.prop(mod, "count")
            elif mod.fit_type == 'FIT_LENGTH':
                box.prop(mod, "fit_length")
            elif mod.fit_type == 'FIT_CURVE':
                box.prop(mod, "curve")
    
            box.separator()
    
            split = box.split()
    
            col = split.column()
            col.prop(mod, "use_constant_offset")
            sub = col.column()
            sub.active = mod.use_constant_offset
            sub.prop(mod, "constant_offset_displace", text="")
    
            col.separator()
    
            col.prop(mod, "use_merge_vertices", text="Merge")
            sub = col.column()
            sub.active = mod.use_merge_vertices
            sub.prop(mod, "use_merge_vertices_cap", text="First Last")
            sub.prop(mod, "merge_threshold", text="Distance")
    
            col = split.column()
            col.prop(mod, "use_relative_offset")
            sub = col.column()
            sub.active = mod.use_relative_offset
            sub.prop(mod, "relative_offset_displace", text="")
    
            col.separator()
    
            col.prop(mod, "use_object_offset")
            sub = col.column()
            sub.active = mod.use_object_offset
            sub.prop(mod, "offset_object", text="")
    
            box.separator()
    
            box.prop(mod, "start_cap")
            box.prop(mod, "end_cap")
            
    def draw_bevel_modifier(layout):
        col = layout.column(align=True)
        box = col.box()
        row = box.row()
        draw_show_expanded(mod,row)
        row.prop(mod,'name',text="",icon='MOD_BEVEL')
        draw_apply_close(row,mod.name)
        if mod.show_expanded:
            box = col.box()
            split = box.split()
    
            col = split.column()
            col.prop(mod, "width")
            col.prop(mod, "segments")
            col.prop(mod, "profile")
    
            col = split.column()
            col.prop(mod, "use_only_vertices")
            col.prop(mod, "use_clamp_overlap")
    
            box.label(text="Limit Method:")
            box.row().prop(mod, "limit_method", expand=True)
            if mod.limit_method == 'ANGLE':
                box.prop(mod, "angle_limit")
            elif mod.limit_method == 'VGROUP':
                box.label(text="Vertex Group:")
                box.prop_search(mod, "vertex_group", obj, "vertex_groups", text="")
    
            box.label(text="Width Method:")
            box.row().prop(mod, "offset_type", expand=True)
    
    def draw_boolean_modifier(layout):
        col = layout.column(align=True)
        box = col.box()
        row = box.row()
        draw_show_expanded(mod,row)
        row.prop(mod,'name',text="",icon='MOD_BOOLEAN')
        draw_apply_close(row,mod.name)
        if mod.show_expanded:
            box = col.box()
            split = box.split()
    
            col = split.column()
            col.label(text="Operation:")
            col.prop(mod, "operation", text="")
    
            col = split.column()
            col.label(text="Object:")
            col.prop(mod, "object", text="")
    
    def draw_curve_modifier(layout):
        col = layout.column(align=True)
        box = col.box()
        row = box.row()
        draw_show_expanded(mod,row)
        row.prop(mod,'name',text="",icon='MOD_CURVE')
        draw_apply_close(row,mod.name)
        if mod.show_expanded:
            box = col.box()
            split = box.split()
    
            col = split.column()
            col.label(text="Object:")
            col.prop(mod, "object", text="")
            col = split.column()
            col.label(text="Vertex Group:")
            col.prop_search(mod, "vertex_group", obj, "vertex_groups", text="")
            box.label(text="Deformation Axis:")
            box.row().prop(mod, "deform_axis", expand=True)
    
    def draw_decimate_modifier(layout):
        col = layout.column(align=True)
        box = col.box()
        row = box.row()
        draw_show_expanded(mod,row)
        row.prop(mod,'name',text="",icon='MOD_DECIM')
        draw_apply_close(row,mod.name)
        if mod.show_expanded:
            box = col.box()
            decimate_type = mod.decimate_type
    
            row = box.row()
            row.prop(mod, "decimate_type", expand=True)
    
            if decimate_type == 'COLLAPSE':
                box.prop(mod, "ratio")
    
                split = box.split()
                row = split.row(align=True)
                row.prop_search(mod, "vertex_group", obj, "vertex_groups", text="")
                row.prop(mod, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')
    
                split.prop(mod, "use_collapse_triangulate")
            elif decimate_type == 'UNSUBDIV':
                box.prop(mod, "iterations")
            else:  # decimate_type == 'DISSOLVE':
                box.prop(mod, "angle_limit")
                box.prop(mod, "use_dissolve_boundaries")
                box.label("Delimit:")
                row = box.row()
                row.prop(mod, "delimit")
    
            box.label(text=iface_("Face Count: %d") % mod.face_count, translate=False)
    
    def draw_edge_split_modifier(layout):
        col = layout.column(align=True)
        box = col.box()
        row = box.row()
        draw_show_expanded(mod,row)
        row.prop(mod,'name',text="",icon='MOD_EDGESPLIT')
        draw_apply_close(row,mod.name)
        if mod.show_expanded:
            box = col.box()
            split = box.split()
    
            col = split.column()
            col.prop(mod, "use_edge_angle", text="Edge Angle")
            sub = col.column()
            sub.active = mod.use_edge_angle
            sub.prop(mod, "split_angle")
    
            split.prop(mod, "use_edge_sharp", text="Sharp Edges")
    
    def draw_hook_modifier(layout):
        col = layout.column(align=True)
        box = col.box()
        row = box.row()
        draw_show_expanded(mod,row)
        row.prop(mod,'name',text="",icon='HOOK')
        draw_apply_close(row,mod.name)
        if mod.show_expanded:
            box = col.box()
            split = box.split()
    
            col = split.column()
            col.label(text="Object:")
            col.prop(mod, "object", text="")
            if mod.object and mod.object.type == 'ARMATURE':
                col.label(text="Bone:")
                col.prop_search(mod, "subtarget", mod.object.data, "bones", text="")
            col = split.column()
            col.label(text="Vertex Group:")
            col.prop_search(mod, "vertex_group", obj, "vertex_groups", text="")
    
            layout.separator()
    
            split = box.split()
    
#             col = split.column()
#             col.prop(mod, "falloff")
#             col.prop(mod, "force", slider=True)
    
            col = split.column()
            col.operator("object.hook_reset", text="Reset")
            col.operator("object.hook_recenter", text="Recenter")
    
            if obj.mode == 'EDIT':
                layout.separator()
                row = layout.row()
                row.operator("object.hook_select", text="Select")
                row.operator("object.hook_assign", text="Assign")
    
    def draw_mask_modifier(layout):
        col = layout.column(align=True)
        box = col.box()
        row = box.row()
        draw_show_expanded(mod,row)
        row.prop(mod,'name',text="",icon='MOD_MASK')
        draw_apply_close(row,mod.name)
        if mod.show_expanded:
            box = col.box()
            split = box.split()
    
            col = split.column()
            col.label(text="Mode:")
            col.prop(mod, "mode", text="")
    
            col = split.column()
            if mod.mode == 'ARMATURE':
                col.label(text="Armature:")
                col.prop(mod, "armature", text="")
            elif mod.mode == 'VERTEX_GROUP':
                col.label(text="Vertex Group:")
                row = col.row(align=True)
                row.prop_search(mod, "vertex_group", obj, "vertex_groups", text="")
                sub = row.row(align=True)
                sub.active = bool(mod.vertex_group)
                sub.prop(mod, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')
    
    def draw_mirror_modifier(layout):
        col = layout.column(align=True)
        box = col.box()
        row = box.row()
        draw_show_expanded(mod,row)
        row.prop(mod,'name',text="",icon='MOD_MIRROR')
        draw_apply_close(row,mod.name)
        if mod.show_expanded:
            box = col.box()
            split = box.split(percentage=0.25)
    
            col = split.column()
            col.label(text="Axis:")
            col.prop(mod, "use_x")
            col.prop(mod, "use_y")
            col.prop(mod, "use_z")
    
            col = split.column()
            col.label(text="Options:")
            col.prop(mod, "use_mirror_merge", text="Merge")
            col.prop(mod, "use_clip", text="Clipping")
            col.prop(mod, "use_mirror_vertex_groups", text="Vertex Groups")
    
            col = split.column()
            col.label(text="Textures:")
            col.prop(mod, "use_mirror_u", text="U")
            col.prop(mod, "use_mirror_v", text="V")
    
            col = box.column()
    
            if mod.use_mirror_merge is True:
                col.prop(mod, "merge_threshold")
            col.label(text="Mirror Object:")
            col.prop(mod, "mirror_object", text="") 
    
    def draw_solidify_modifier(layout):
        col = layout.column(align=True)
        box = col.box()
        row = box.row()
        draw_show_expanded(mod,row)
        row.prop(mod,'name',text="",icon='MOD_SOLIDIFY')
        draw_apply_close(row,mod.name)
        if mod.show_expanded:
            box = col.box()
            split = box.split()
    
            col = split.column()
            col.prop(mod, "thickness")
            col.prop(mod, "thickness_clamp")
    
            col.separator()
    
            row = col.row(align=True)
            row.prop_search(mod, "vertex_group", obj, "vertex_groups", text="")
            sub = row.row(align=True)
            sub.active = bool(mod.vertex_group)
            sub.prop(mod, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')
    
            sub = col.row()
            sub.active = bool(mod.vertex_group)
            sub.prop(mod, "thickness_vertex_group", text="Factor")
    
            col.label(text="Crease:")
            col.prop(mod, "edge_crease_inner", text="Inner")
            col.prop(mod, "edge_crease_outer", text="Outer")
            col.prop(mod, "edge_crease_rim", text="Rim")
    
            col = split.column()
    
            col.prop(mod, "offset")
            col.prop(mod, "use_flip_normals")
    
            col.prop(mod, "use_even_offset")
            col.prop(mod, "use_quality_normals")
            col.prop(mod, "use_rim")
    
            col.separator()
    
            col.label(text="Material Index Offset:")
    
            sub = col.column()
            row = sub.split(align=True, percentage=0.4)
            row.prop(mod, "material_offset", text="")
            row = row.row(align=True)
            row.active = mod.use_rim
            row.prop(mod, "material_offset_rim", text="Rim")
    
    def draw_subsurf_modifier(layout):
        col = layout.column(align=True)
        box = col.box()
        row = box.row()
        draw_show_expanded(mod,row)
        row.prop(mod,'name',text="",icon='MOD_SUBSURF')
        draw_apply_close(row,mod.name)
        if mod.show_expanded:
            box = col.box()
            box.row().prop(mod, "subdivision_type", expand=True)
    
            split = box.split()
            col = split.column()
            col.label(text="Subdivisions:")
            col.prop(mod, "levels", text="View")
            col.prop(mod, "render_levels", text="Render")
    
            col = split.column()
            col.label(text="Options:")
            col.prop(mod, "use_subsurf_uv")
            col.prop(mod, "show_only_control_edges")
    
    def draw_skin_modifier(layout):
        col = layout.column(align=True)
        box = col.box()
        row = box.row()
        draw_show_expanded(mod,row)
        row.prop(mod,'name',text="",icon='MOD_SKIN')
        draw_apply_close(row,mod.name)
        if mod.show_expanded:
            box = col.box()
            box.operator("object.skin_armature_create", text="Create Armature")
    
            box.separator()
    
            col = box.column(align=True)
            col.prop(mod, "branch_smoothing")
            col.prop(mod, "use_smooth_shade")
    
            split = box.split()
    
            col = split.column()
            col.label(text="Selected Vertices:")
            sub = col.column(align=True)
            sub.operator("object.skin_loose_mark_clear", text="Mark Loose").action = 'MARK'
            sub.operator("object.skin_loose_mark_clear", text="Clear Loose").action = 'CLEAR'
    
            sub = col.column()
            sub.operator("object.skin_root_mark", text="Mark Root")
            sub.operator("object.skin_radii_equalize", text="Equalize Radii")
    
            col = split.column()
            col.label(text="Symmetry Axes:")
            col.prop(mod, "use_x_symmetry")
            col.prop(mod, "use_y_symmetry")
            col.prop(mod, "use_z_symmetry")
    
    def draw_triangulate_modifier(layout):
        col = layout.column(align=True)
        box = col.box()
        row = box.row()
        draw_show_expanded(mod,row)
        row.prop(mod,'name',text="",icon='MOD_TRIANGULATE')
        draw_apply_close(row,mod.name)
        if mod.show_expanded:
            box = col.box()
            row = box.row()
    
            col = row.column()
            col.label(text="Quad Method:")
            col.prop(mod, "quad_method", text="")
            col = row.column()
            col.label(text="Ngon Method:")
            col.prop(mod, "ngon_method", text="")  
    
    def draw_simple_deform_modifier(layout):
        col = layout.column(align=True)
        box = col.box()
        row = box.row()
        draw_show_expanded(mod,row)
        row.prop(mod,'name',text="",icon='MOD_SIMPLEDEFORM')
        draw_apply_close(row,mod.name)
        if mod.show_expanded:
            box = col.box()
            box.row().prop(mod, "deform_method", expand=True)
    
            split = box.split()
    
            col = split.column()
            col.label(text="Vertex Group:")
            col.prop_search(mod, "vertex_group", obj, "vertex_groups", text="")
    
            split = box.split()
    
            col = split.column()
            col.label(text="Origin:")
            col.prop(mod, "origin", text="")
    
            if mod.deform_method in {'TAPER', 'STRETCH', 'TWIST'}:
                col.label(text="Lock:")
                col.prop(mod, "lock_x")
                col.prop(mod, "lock_y")
    
            col = split.column()
            col.label(text="Deform:")
            if mod.deform_method in {'TAPER', 'STRETCH'}:
                col.prop(mod, "factor")
            else:
                col.prop(mod, "angle")
            col.prop(mod, "limits", slider=True)
    
    def draw_wireframe_modifier(layout):
        col = layout.column(align=True)
        box = col.box()
        row = box.row()
        draw_show_expanded(mod,row)
        row.prop(mod,'name',text="",icon='MOD_WIREFRAME')
        draw_apply_close(row,mod.name)
        if mod.show_expanded:
            box = col.box()
            has_vgroup = bool(mod.vertex_group)
    
            split = box.split()
    
            col = split.column()
            col.prop(mod, "thickness", text="Thickness")
    
            row = col.row(align=True)
            row.prop_search(mod, "vertex_group", obj, "vertex_groups", text="")
            sub = row.row(align=True)
            sub.active = has_vgroup
            sub.prop(mod, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')
            row = col.row(align=True)
            row.active = has_vgroup
            row.prop(mod, "thickness_vertex_group", text="Factor")
    
            col.prop(mod, "use_crease", text="Crease Edges")
            col.prop(mod, "crease_weight", text="Crease Weight")
    
            col = split.column()
    
            col.prop(mod, "offset")
            col.prop(mod, "use_even_offset", text="Even Thickness")
            col.prop(mod, "use_relative_offset", text="Relative Thickness")
            col.prop(mod, "use_boundary", text="Boundary")
            col.prop(mod, "use_replace", text="Replace Original")
    
            col.prop(mod, "material_offset", text="Material Offset")                            
    
    if mod.type == 'ARRAY':
        draw_array_modifier(layout)
    elif mod.type == 'BEVEL':
        draw_bevel_modifier(layout)
    elif mod.type == 'BOOLEAN':
        draw_boolean_modifier(layout)
    elif mod.type == 'CURVE':
        draw_curve_modifier(layout)
    elif mod.type == 'DECIMATE':
        draw_decimate_modifier(layout)
    elif mod.type == 'EDGE_SPLIT':
        draw_edge_split_modifier(layout)
    elif mod.type == 'HOOK':
        draw_hook_modifier(layout)
    elif mod.type == 'MASK':
        draw_mask_modifier(layout)
    elif mod.type == 'MIRROR':
        draw_mirror_modifier(layout)
    elif mod.type == 'SOLIDIFY':
        draw_solidify_modifier(layout)
    elif mod.type == 'SUBSURF':
        draw_subsurf_modifier(layout)
    elif mod.type == 'SKIN':
        draw_skin_modifier(layout)
    elif mod.type == 'SIMPLE_DEFORM':
        draw_simple_deform_modifier(layout)
    elif mod.type == 'TRIANGULATE':
        draw_triangulate_modifier(layout)
    elif mod.type == 'WIREFRAME':
        draw_wireframe_modifier(layout)
    else:
        row = layout.row()
        row.label(mod.name + " view ")
    
def draw_constraint(con,layout,obj):

    def draw_show_expanded(con,layout):
        if con.show_expanded:
            layout.prop(con,'show_expanded',text="",emboss=False)
        else:
            layout.prop(con,'show_expanded',text="",emboss=False)

    def space_template(layout, con, target=True, owner=True):
        if target or owner:

            split = layout.split(percentage=0.2)

            split.label(text="Space:")
            row = split.row()

            if target:
                row.prop(con, "target_space", text="")

            if target and owner:
                row.label(icon='ARROW_LEFTRIGHT')

            if owner:
                row.prop(con, "owner_space", text="")

    def target_template(layout, con, subtargets=True):
        layout.prop(con, "target")  # XXX limiting settings for only 'curves' or some type of object

        if con.target and subtargets:
            if con.target.type == 'ARMATURE':
                layout.prop_search(con, "subtarget", con.target.data, "bones", text="Bone")

                if hasattr(con, "head_tail"):
                    row = layout.row()
                    row.label(text="Head/Tail:")
                    row.prop(con, "head_tail", text="")
            elif con.target.type in {'MESH', 'LATTICE'}:
                layout.prop_search(con, "subtarget", con.target, "vertex_groups", text="Vertex Group")

    def draw_copy_location_constraint(layout):
        col = layout.column(align=True)
        box = col.template_constraint(con)

        if con.show_expanded:
            target_template(box, con)
            
            split = box.split()
    
            col = split.column()
            col.prop(con, "use_x", text="X")
            sub = col.column()
            sub.active = con.use_x
            sub.prop(con, "invert_x", text="Invert")
    
            col = split.column()
            col.prop(con, "use_y", text="Y")
            sub = col.column()
            sub.active = con.use_y
            sub.prop(con, "invert_y", text="Invert")
    
            col = split.column()
            col.prop(con, "use_z", text="Z")
            sub = col.column()
            sub.active = con.use_z
            sub.prop(con, "invert_z", text="Invert")
    
            box.prop(con, "use_offset")
    
            space_template(box, con)
            
            if con.type not in {'RIGID_BODY_JOINT', 'NULL'}:
                box.prop(con, "influence")            
     
    def draw_copy_rotation_constraint(layout):
        col = layout.column(align=True)
        box = col.template_constraint(con)

        if con.show_expanded:        
            target_template(box, con)
    
            split = box.split()
    
            col = split.column()
            col.prop(con, "use_x", text="X")
            sub = col.column()
            sub.active = con.use_x
            sub.prop(con, "invert_x", text="Invert")
    
            col = split.column()
            col.prop(con, "use_y", text="Y")
            sub = col.column()
            sub.active = con.use_y
            sub.prop(con, "invert_y", text="Invert")
    
            col = split.column()
            col.prop(con, "use_z", text="Z")
            sub = col.column()
            sub.active = con.use_z
            sub.prop(con, "invert_z", text="Invert")
    
            box.prop(con, "use_offset")
    
            space_template(box, con) 
            
            if con.type not in {'RIGID_BODY_JOINT', 'NULL'}:
                box.prop(con, "influence")            
    
    def draw_copy_scale_constraint(layout):
        col = layout.column(align=True)
        box = col.template_constraint(con)

        if con.show_expanded:        
            target_template(box, con)
    
            row = box.row(align=True)
            row.prop(con, "use_x", text="X")
            row.prop(con, "use_y", text="Y")
            row.prop(con, "use_z", text="Z")
    
            box.prop(con, "use_offset")
    
            space_template(box, con)
            
            if con.type not in {'RIGID_BODY_JOINT', 'NULL'}:
                box.prop(con, "influence")  
    
    def draw_copy_transforms_constraint(layout):
        col = layout.column(align=True)
        box = col.template_constraint(con)

        if con.show_expanded:        
            target_template(box, con)

            space_template(box, con)
            
            if con.type not in {'RIGID_BODY_JOINT', 'NULL'}:
                box.prop(con, "influence")  
    
    def draw_limit_distance_constraint(layout):
        col = layout.column(align=True)
        box = col.template_constraint(con)

        if con.show_expanded:        
            target_template(box, con)
    
            col = box.column(align=True)
            col.prop(con, "distance")
            col.operator("constraint.limitdistance_reset")
    
            row = box.row()
            row.label(text="Clamp Region:")
            row.prop(con, "limit_mode", text="")
    
            row = box.row()
            row.prop(con, "use_transform_limit")
            row.label()
    
            space_template(box, con) 
            
            if con.type not in {'RIGID_BODY_JOINT', 'NULL'}:
                box.prop(con, "influence")  
    
    def draw_limit_location_constraint(layout):
        col = layout.column(align=True)
        box = col.template_constraint(con)

        if con.show_expanded:        
            split = box.split()
    
            col = split.column()
            col.prop(con, "use_min_x")
            sub = col.column()
            sub.active = con.use_min_x
            sub.prop(con, "min_x", text="")
            col.prop(con, "use_max_x")
            sub = col.column()
            sub.active = con.use_max_x
            sub.prop(con, "max_x", text="")
    
            col = split.column()
            col.prop(con, "use_min_y")
            sub = col.column()
            sub.active = con.use_min_y
            sub.prop(con, "min_y", text="")
            col.prop(con, "use_max_y")
            sub = col.column()
            sub.active = con.use_max_y
            sub.prop(con, "max_y", text="")
    
            col = split.column()
            col.prop(con, "use_min_z")
            sub = col.column()
            sub.active = con.use_min_z
            sub.prop(con, "min_z", text="")
            col.prop(con, "use_max_z")
            sub = col.column()
            sub.active = con.use_max_z
            sub.prop(con, "max_z", text="")
    
            row = box.row()
            row.prop(con, "use_transform_limit")
            row.label()
    
            row = box.row()
            row.label(text="Convert:")
            row.prop(con, "owner_space", text="")
            
            if con.type not in {'RIGID_BODY_JOINT', 'NULL'}:
                box.prop(con, "influence")  
    
    def draw_limit_rotation_constraint(layout):
        col = layout.column(align=True)
        box = col.template_constraint(con)

        if con.show_expanded:        
            split = box.split()
    
            col = split.column(align=True)
            col.prop(con, "use_limit_x")
            sub = col.column(align=True)
            sub.active = con.use_limit_x
            sub.prop(con, "min_x", text="Min")
            sub.prop(con, "max_x", text="Max")
    
            col = split.column(align=True)
            col.prop(con, "use_limit_y")
            sub = col.column(align=True)
            sub.active = con.use_limit_y
            sub.prop(con, "min_y", text="Min")
            sub.prop(con, "max_y", text="Max")
    
            col = split.column(align=True)
            col.prop(con, "use_limit_z")
            sub = col.column(align=True)
            sub.active = con.use_limit_z
            sub.prop(con, "min_z", text="Min")
            sub.prop(con, "max_z", text="Max")
    
            box.prop(con, "use_transform_limit")
    
            row = box.row()
            row.label(text="Convert:")
            row.prop(con, "owner_space", text="")
            
            if con.type not in {'RIGID_BODY_JOINT', 'NULL'}:
                box.prop(con, "influence")   
    
    def draw_limit_scale_constraint(layout):
        col = layout.column(align=True)
        box = col.template_constraint(con)

        if con.show_expanded:        
            split = box.split()
    
            col = split.column()
            col.prop(con, "use_min_x")
            sub = col.column()
            sub.active = con.use_min_x
            sub.prop(con, "min_x", text="")
            col.prop(con, "use_max_x")
            sub = col.column()
            sub.active = con.use_max_x
            sub.prop(con, "max_x", text="")
    
            col = split.column()
            col.prop(con, "use_min_y")
            sub = col.column()
            sub.active = con.use_min_y
            sub.prop(con, "min_y", text="")
            col.prop(con, "use_max_y")
            sub = col.column()
            sub.active = con.use_max_y
            sub.prop(con, "max_y", text="")
    
            col = split.column()
            col.prop(con, "use_min_z")
            sub = col.column()
            sub.active = con.use_min_z
            sub.prop(con, "min_z", text="")
            col.prop(con, "use_max_z")
            sub = col.column()
            sub.active = con.use_max_z
            sub.prop(con, "max_z", text="")
    
            row = box.row()
            row.prop(con, "use_transform_limit")
            row.label()
    
            row = box.row()
            row.label(text="Convert:")
            row.prop(con, "owner_space", text="")
            
            if con.type not in {'RIGID_BODY_JOINT', 'NULL'}:
                box.prop(con, "influence")                     
            
    if con.type == 'COPY_LOCATION':
        draw_copy_location_constraint(layout)
    elif con.type == 'COPY_ROTATION':
        draw_copy_rotation_constraint(layout)
    elif con.type == 'COPY_SCALE':
        draw_copy_scale_constraint(layout)
    elif con.type == 'COPY_TRANSFORMS':
        draw_copy_transforms_constraint(layout)
    elif con.type == 'LIMIT_DISTANCE':
        draw_limit_distance_constraint(layout)
    elif con.type == 'LIMIT_LOCATION':
        draw_limit_location_constraint(layout)
    elif con.type == 'LIMIT_ROTATION':
        draw_limit_rotation_constraint(layout)
    elif con.type == 'LIMIT_SCALE':
        draw_limit_scale_constraint(layout)
    else:
        row = layout.row()
        row.label(con.name + " view ")            

def draw_object_properties(layout,obj):
    ui = bpy.context.scene.mv.ui
    col = layout.column(align=True)
    box = col.box()
    row = box.row(align=True)
    draw_object_tabs(row,obj)
    box = col.box()
    col = box.column()
    if ui.interface_object_tabs == 'INFO':
        draw_object_info(col,obj)
    if ui.interface_object_tabs == 'DISPLAY':
        box = col.box()
        row = box.row()
        row.prop(obj,'draw_type',expand=True)
        box.prop(obj,'hide_select')
        box.prop(obj,'hide')
        box.prop(obj,'hide_render')
        box.prop(obj,'show_x_ray',icon='GHOST_ENABLED',text='Show X-Ray')
        box.prop(obj.cycles_visibility,'camera',icon='CAMERA_DATA',text='Show in Viewport Render')
    if ui.interface_object_tabs == 'MATERIAL':
        draw_object_materials(col,obj)
    if ui.interface_object_tabs == 'CONSTRAINTS':
        row = col.row()
        row.operator_menu_enum("fd_object.add_constraint", "type", icon='CONSTRAINT_DATA')
        row.operator("fd_object.collapse_all_constraints",text="",icon='FULLSCREEN_EXIT')
        for con in obj.constraints:
            draw_constraint(con,layout,obj)
    if ui.interface_object_tabs == 'MODIFIERS':
        row = col.row()
        row.operator_menu_enum("fd_object.add_modifier", "type", icon='MODIFIER')
        row.operator("fd_object.collapse_all_modifiers",text="",icon='FULLSCREEN_EXIT')
        for mod in obj.modifiers:
            draw_modifier(mod,layout,obj)
    if ui.interface_object_tabs == 'MESHDATA':
        draw_object_data(col,obj)
    if ui.interface_object_tabs == 'CURVEDATA':
        draw_object_data(col,obj)
    if ui.interface_object_tabs == 'TEXTDATA':
        draw_object_data(col,obj)
    if ui.interface_object_tabs == 'EMPTYDATA':
        draw_object_data(col,obj)
    if ui.interface_object_tabs == 'LIGHTDATA':
        draw_object_data(col,obj)
    if ui.interface_object_tabs == 'CAMERADATA':
        draw_object_data(col,obj)
    if ui.interface_object_tabs == 'DRIVERS':
        draw_object_drivers(col,obj)
    if ui.interface_object_tabs == 'TOKENS':
        if obj.type == 'MESH':
            col.operator_menu_enum("cabinetlib.add_machine_token", "token_type", icon='SCULPTMODE_HLT')
            obj.cabinetlib.mp.draw_machine_tokens(col)
        
def draw_object_tabs(layout,obj):
    ui = bpy.context.scene.mv.ui
    if obj.type == 'MESH':
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[0][0], icon='INFO', text="") 
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[1][0], icon='RESTRICT_VIEW_OFF', text="") 
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[2][0], icon='MATERIAL', text="") 
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[3][0], icon='CONSTRAINT', text="") 
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[4][0], icon='MODIFIER', text="") 
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[5][0], icon='MESH_DATA', text="")  
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[11][0], icon='AUTO', text="")   
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[12][0], icon='SCULPTMODE_HLT', text="")   
    if obj.type == 'CURVE':
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[0][0], icon='INFO', text="") 
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[1][0], icon='RESTRICT_VIEW_OFF', text="") 
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[2][0], icon='MATERIAL', text="") 
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[3][0], icon='CONSTRAINT', text="") 
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[4][0], icon='MODIFIER', text="") 
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[6][0], icon='CURVE_DATA', text="")  
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[11][0], icon='AUTO', text="")  
    if obj.type == 'FONT':
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[0][0], icon='INFO', text="") 
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[1][0], icon='RESTRICT_VIEW_OFF', text="") 
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[2][0], icon='MATERIAL', text="") 
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[3][0], icon='CONSTRAINT', text="") 
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[4][0], icon='MODIFIER', text="") 
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[7][0], icon='FONT_DATA', text="")  
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[11][0], icon='AUTO', text="")  
    if obj.type == 'EMPTY':
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[0][0], icon='INFO', text="") 
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[1][0], icon='RESTRICT_VIEW_OFF', text="") 
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[3][0], icon='CONSTRAINT', text="") 
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[8][0], icon='EMPTY_DATA', text="")  
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[11][0], icon='AUTO', text="")  
    if obj.type == 'LAMP':
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[0][0], icon='INFO', text="") 
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[1][0], icon='RESTRICT_VIEW_OFF', text="") 
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[3][0], icon='CONSTRAINT', text="") 
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[9][0], icon='LAMP_SPOT', text="")  
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[11][0], icon='AUTO', text="")  
    if obj.type == 'CAMERA':
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[0][0], icon='INFO', text="") 
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[3][0], icon='CONSTRAINT', text="") 
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[10][0], icon='OUTLINER_DATA_CAMERA', text="")  
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[11][0], icon='AUTO', text="")  
    if obj.type == 'ARMATURE':
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[0][0], icon='INFO', text="") 
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[1][0], icon='RESTRICT_VIEW_OFF', text="") 
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[3][0], icon='CONSTRAINT', text="") 
        layout.prop_enum(ui, "interface_object_tabs", enums.enum_object_tabs[11][0], icon='AUTO', text="")  

def draw_object_info(layout,obj):
    box = layout.box()
    row = box.row()
    row.prop(obj,'name')
    if obj.type in {'MESH','CURVE','LATTICE','TEXT'}:
        row.operator('fd_object.toggle_edit_mode',text="",icon='EDITMODE_HLT').object_name = obj.name
    
    has_hook_modifier = False
    for mod in obj.modifiers:
        if mod.type == 'HOOK':
            has_hook_modifier =  True
    
    has_shape_keys = False
    if obj.type == 'MESH':
        if obj.data.shape_keys:
            if len(obj.data.shape_keys.key_blocks) > 0:
                has_shape_keys = True
    
    if has_hook_modifier or has_shape_keys:
        row = box.row()
        col = row.column(align=True)
        col.label("Dimension")
        col.label("X: " + str(round(meter_to_unit(obj.dimensions.x),4)))
        col.label("Y: " + str(round(meter_to_unit(obj.dimensions.y),4)))
        col.label("Z: " + str(round(meter_to_unit(obj.dimensions.z),4)))
        col = row.column(align=True)
        col.label("Location")
        col.label("X: " + str(round(meter_to_unit(obj.location.x),4)))
        col.label("Y: " + str(round(meter_to_unit(obj.location.y),4)))
        col.label("Z: " + str(round(meter_to_unit(obj.location.z),4)))
        col = row.column(align=True)
        col.label("Rotation")
        col.label("X: " + str(round(math.degrees(obj.rotation_euler.x),4)))
        col.label("Y: " + str(round(math.degrees(obj.rotation_euler.y),4)))
        col.label("Z: " + str(round(math.degrees(obj.rotation_euler.z),4)))
        if has_hook_modifier:
            box.operator("fd_object.apply_hook_modifiers",icon='HOOK').object_name = obj.name
        if has_shape_keys:
            box.operator("fd_object.apply_shape_keys",icon='SHAPEKEY_DATA').object_name = obj.name
    else:
        if obj.type not in {'EMPTY','CAMERA','LAMP'}:
            box.label('Dimensions:')
            col = box.column(align=True)
            #X
            row = col.row(align=True)
            row.prop(obj,"lock_scale",index=0,text="")
            if obj.lock_scale[0]:
                row.label("X: " + str(round(meter_to_unit(obj.dimensions.x),4)))
            else:
                row.prop(obj,"dimensions",index=0,text="X")
            #Y
            row = col.row(align=True)
            row.prop(obj,"lock_scale",index=1,text="")
            if obj.lock_scale[1]:
                row.label("Y: " + str(round(meter_to_unit(obj.dimensions.y),4)))
            else:
                row.prop(obj,"dimensions",index=1,text="Y")
            #Z
            row = col.row(align=True)
            row.prop(obj,"lock_scale",index=2,text="")
            if obj.lock_scale[2]:
                row.label("Z: " + str(round(meter_to_unit(obj.dimensions.z),4)))
            else:
                row.prop(obj,"dimensions",index=2,text="Z")
                
        col1 = box.row()
        if obj:
            col2 = col1.split()
            col = col2.column(align=True)
            col.label('Location:')
            #X
            row = col.row(align=True)
            row.prop(obj,"lock_location",index=0,text="")
            if obj.lock_location[0]:
                row.label("X: " + str(round(meter_to_unit(obj.location.x),4)))
            else:
                row.prop(obj,"location",index=0,text="X")
            #Y    
            row = col.row(align=True)
            row.prop(obj,"lock_location",index=1,text="")
            if obj.lock_location[1]:
                row.label("Y: " + str(round(meter_to_unit(obj.location.y),4)))
            else:
                row.prop(obj,"location",index=1,text="Y")
            #Z    
            row = col.row(align=True)
            row.prop(obj,"lock_location",index=2,text="")
            if obj.lock_location[2]:
                row.label("Z: " + str(round(meter_to_unit(obj.location.z),4)))
            else:
                row.prop(obj,"location",index=2,text="Z")
                
            col2 = col1.split()
            col = col2.column(align=True)
            col.label('Rotation:')
            #X
            row = col.row(align=True)
            row.prop(obj,"lock_rotation",index=0,text="")
            if obj.lock_rotation[0]:
                row.label("X: " + str(round(math.degrees(obj.rotation_euler.x),4)))
            else:
                row.prop(obj,"rotation_euler",index=0,text="X")
            #Y    
            row = col.row(align=True)
            row.prop(obj,"lock_rotation",index=1,text="")
            if obj.lock_rotation[1]:
                row.label("Y: " + str(round(math.degrees(obj.rotation_euler.y),4)))
            else:
                row.prop(obj,"rotation_euler",index=1,text="Y")
            #Z    
            row = col.row(align=True)
            row.prop(obj,"lock_rotation",index=2,text="")
            if obj.lock_rotation[2]:
                row.label("Y: " + str(round(math.degrees(obj.rotation_euler.z),4)))
            else:
                row.prop(obj,"rotation_euler",index=2,text="Z")
                
    row = box.row()
    row.prop(obj.cabinetlib,'comment')
    
def draw_object_materials(layout,obj):
    
    if obj.type in {'MESH','CURVE'}:
        spec_group = bpy.context.scene.cabinetlib.spec_groups[obj.cabinetlib.spec_group_index]
        layout.prop(obj.cabinetlib,'type_mesh')
        if obj.cabinetlib.type_mesh == 'CUTPART':
            row = layout.row(align=True)
            row.prop_search(obj.cabinetlib,"cutpart_name",spec_group,"cutparts",icon='MOD_UVPROJECT',text="")
            row = layout.row(align=True)
            row.prop_search(obj.cabinetlib,"edgepart_name",spec_group,"edgeparts",icon='EDGESEL',text="")

        if obj.cabinetlib.type_mesh == 'EDGEBANDING':
            row = layout.row(align=True)
            row.prop_search(obj.cabinetlib,"edgepart_name",spec_group,"edgeparts",icon='EDGESEL',text="")

        row = layout.row()
        row.label('Material Slots:')
        row.operator("object.material_slot_add", icon='ZOOMIN', text="")
        row.operator("object.material_slot_remove", icon='ZOOMOUT', text="")
        row.operator("cabinetlib.assign_materials_from_pointers", icon='FILE_REFRESH', text="").object_name = obj.name
        row.operator('fd_general.open_new_window',text="",icon='NODETREE').space_type = 'NODE_EDITOR'
        layout.template_list("FD_UL_materials", "", obj, "material_slots", obj, "active_material_index", rows=1)
        layout.template_ID(obj, "active_material", new="material.new")
        slot = None
        if len(obj.material_slots) > 0:
            slot = obj.material_slots[obj.active_material_index]

        if slot:
#             col = layout.column(align=True)
#             col.template_list("FD_UL_materials", "", obj, "material_slots", obj, "active_material_index", rows=1)
            if len(obj.cabinetlib.material_slots) != len(obj.material_slots):
                if obj.cabinetlib.type_mesh != "NONE":
                    layout.operator("cabinetlib.sync_material_slots", icon='ZOOMIN', text="Sync").object_name = obj.name
            else:
                if spec_group:
                    mvslot = obj.cabinetlib.material_slots[obj.active_material_index]
                    box = layout.box()
                    box.prop(mvslot,"name")
                    box.prop_search(mvslot,"pointer_name",spec_group,"materials",icon='HAND')
                    box.label("Category Name: " + mvslot.category_name)
                    box.label("Material Name: " + mvslot.item_name)
        else:
            if obj.cabinetlib.type_mesh == 'CUTPART':
                layout.operator("cabinetlib.create_cutpart_material_slots", icon='MATERIAL',text="Setup Materials").object_name = obj.name

    if obj.mode == 'EDIT':
        row = layout.row(align=True)
        row.operator("object.material_slot_assign", text="Assign")
        row.operator("object.material_slot_select", text="Select")
        row.operator("object.material_slot_deselect", text="Deselect")
    
def draw_object_data(layout,obj):
    
    if obj.type == 'MESH':
        obj_bp = get_assembly_bp(obj)
        obj_wall_bp = get_wall_bp(obj)
        box = layout.box()
        row = box.row()
        row.label("Vertex Groups:")
        row.operator("object.vertex_group_add", icon='ZOOMIN', text="")
        row.operator("object.vertex_group_remove", icon='ZOOMOUT', text="").all = False
        box.template_list("FD_UL_vgroups", "", obj, "vertex_groups", obj.vertex_groups, "active_index", rows=3)
        if len(obj.vertex_groups) > 0:
            if obj.mode == 'EDIT':
                row = box.row()
                sub = row.row(align=True)
                sub.operator("object.vertex_group_assign", text="Assign")
                sub.operator("object.vertex_group_remove_from", text="Remove")
    
                sub = row.row(align=True)
                
                sub.operator("fd_object.vertex_group_select", text="Select").object_name = obj.name
                sub.separator()
                sub.operator("fd_object.clear_vertex_groups", text="Clear All").object_name = obj.name
#                 sub.operator("object.vertex_group_select", text="Select")
#                 sub.operator("object.vertex_group_deselect", text="Deselect")
            else:
                group = obj.vertex_groups.active
                if obj_bp or obj_wall_bp:
                    box.operator("fd_assembly.connect_meshes_to_hooks_in_assembly",text="Connect Hooks",icon='HOOK').object_name = obj.name
                else:
                    box.prop(group,'name')

        key = obj.data.shape_keys
        kb = obj.active_shape_key
        
        box = layout.box()
        row = box.row()
        row.label("Shape Keys:")
        row.operator("object.shape_key_add", icon='ZOOMIN', text="").from_mix = False
        row.operator("object.shape_key_remove", icon='ZOOMOUT', text="").all = False
        box.template_list("MESH_UL_shape_keys", "", key, "key_blocks", obj, "active_shape_key_index", rows=3)
        if kb and obj.active_shape_key_index != 0:
            box.prop(kb,'name')
            if obj.mode != 'EDIT':
                row = box.row()
                row.prop(kb, "value")
        
    if obj.type == 'EMPTY':
        box = layout.box()
        box.label("Empty Data",icon='FONT_DATA')
        box.prop(obj,'empty_draw_type',text='Draw Type')
        box.prop(obj,'empty_draw_size')
        
    if obj.type == 'CURVE':
        box = layout.box()
        box.label("Curve Data",icon='CURVE_DATA')
        curve = obj.data
        box.prop(curve,"dimensions")
        box.prop(curve,"bevel_object")
        box.prop(curve,"bevel_depth")
        box.prop(curve,"extrude")
        box.prop(curve,"use_fill_caps")
        box.prop(curve.splines[0],"use_cyclic_u")         
    
    if obj.type == 'FONT':
        text = obj.data
        box = layout.box()
        row = box.row()
        row.label("Font Data:")
        if obj.mode == 'OBJECT':
            row.operator("fd_object.toggle_edit_mode",text="Edit Text",icon='OUTLINER_DATA_FONT').object_name = obj.name
        else:
            row.operator("fd_object.toggle_edit_mode",text="Exit Edit Mode",icon='OUTLINER_DATA_FONT').object_name = obj.name
        row = box.row()
        row.template_ID(text, "font", open="font.open", unlink="font.unlink")
        row = box.row()
        row.label("Text Size:")
        row.prop(text,"size",text="")
        row = box.row()
        row.prop(text,"align")
        
        box = layout.box()
        row = box.row()
        row.label("3D Font:")
        row = box.row()
        row.prop(text,"extrude")
        row = box.row()
        row.prop(text,"bevel_depth")
        
    if obj.type == 'LAMP':
        box = layout.box()
        lamp = obj.data
        clamp = lamp.cycles
        cscene = bpy.context.scene.cycles  
        
        emissionNode = None
        mathNode = None
        
        if "Emission" in lamp.node_tree.nodes:
            emissionNode = lamp.node_tree.nodes["Emission"]
        if "Math" in lamp.node_tree.nodes:
            mathNode = lamp.node_tree.nodes["Math"]

        type_box = box.box()
        type_box.label("Lamp Type:")     
        row = type_box.row()
        row.prop(lamp, "type", expand=True)
        
        if lamp.type in {'POINT', 'SUN', 'SPOT'}:
            type_box.prop(lamp, "shadow_soft_size", text="Shadow Size")
        elif lamp.type == 'AREA':
            type_box.prop(lamp, "shape", text="")
            sub = type_box.column(align=True)

            if lamp.shape == 'SQUARE':
                sub.prop(lamp, "size")
            elif lamp.shape == 'RECTANGLE':
                sub.prop(lamp, "size", text="Size X")
                sub.prop(lamp, "size_y", text="Size Y")

        if cscene.progressive == 'BRANCHED_PATH':
            type_box.prop(clamp, "samples")

        if lamp.type == 'HEMI':
            type_box.label(text="Not supported, interpreted as sun lamp")         

        options_box = box.box()
        options_box.label("Lamp Options:")
        if emissionNode:
            row = options_box.row()
            split = row.split(percentage=0.3)
            split.label("Lamp Color:")
            split.prop(emissionNode.inputs[0],"default_value",text="")  
            
        row = options_box.row()
        split = row.split(percentage=0.3)
        split.label("Lamp Strength:")            
        if mathNode:   
            split.prop(mathNode.inputs[0],"default_value",text="") 
        else:          
            split.prop(emissionNode.inputs[1], "default_value",text="")
            
        row = options_box.row()        
        split = row.split(percentage=0.4)     
        split.prop(clamp, "cast_shadow",text="Cast Shadows")
        split.prop(clamp, "use_multiple_importance_sampling")
            
    if obj.type == 'CAMERA':
        box = layout.box()
        cam = obj.data
        ccam = cam.cycles
        scene = bpy.context.scene
        rd = scene.render
        
        box.label("Camera Options:")           
        cam_opt_box_1 = box.box()
        row = cam_opt_box_1.row(align=True)
        row.label(text="Render Size:",icon='STICKY_UVS_VERT')        
        row.prop(rd, "resolution_x", text="X")
        row.prop(rd, "resolution_y", text="Y")
        cam_opt_box_1.prop(cam, "type", expand=False, text="Camera Type")
        split = cam_opt_box_1.split()
        col = split.column()
        if cam.type == 'PERSP':
            row = col.row()
            if cam.lens_unit == 'MILLIMETERS':
                row.prop(cam, "lens")
            elif cam.lens_unit == 'FOV':
                row.prop(cam, "angle")
            row.prop(cam, "lens_unit", text="")

        if cam.type == 'ORTHO':
            col.prop(cam, "ortho_scale")

        if cam.type == 'PANO':
            engine = bpy.context.scene.render.engine
            if engine == 'CYCLES':
                ccam = cam.cycles
                col.prop(ccam, "panorama_type", text="Panorama Type")
                if ccam.panorama_type == 'FISHEYE_EQUIDISTANT':
                    col.prop(ccam, "fisheye_fov")
                elif ccam.panorama_type == 'FISHEYE_EQUISOLID':
                    row = col.row()
                    row.prop(ccam, "fisheye_lens", text="Lens")
                    row.prop(ccam, "fisheye_fov")
            elif engine == 'BLENDER_RENDER':
                row = col.row()
                if cam.lens_unit == 'MILLIMETERS':
                    row.prop(cam, "lens")
                elif cam.lens_unit == 'FOV':
                    row.prop(cam, "angle")
                row.prop(cam, "lens_unit", text="")
        
        row = cam_opt_box_1.row()
#         row.menu("CAMERA_MT_presets", text=bpy.types.CAMERA_MT_presets.bl_label)         
        row.prop_menu_enum(cam, "show_guide")            
        row = cam_opt_box_1.row()
        split = row.split()
        col = split.column()
        col.prop(cam, "clip_start", text="Clipping Start")
        col.prop(cam, "clip_end", text="Clipping End")      
        col = row.column()         
        col.prop(bpy.context.scene.cycles,"film_transparent",text="Transparent Film")   
        
        box.label(text="Depth of Field:")
        dof_box = box.box()
        row = dof_box.row()
        row.label("Focus:")
        row = dof_box.row(align=True)
        row.prop(cam, "dof_object", text="")
        col = row.column()
        sub = col.row()
        sub.active = cam.dof_object is None
        sub.prop(cam, "dof_distance", text="Distance")
        
def draw_object_drivers(layout,obj):
    if obj:
        if not obj.animation_data:
            layout.label("There are no drivers assigned to the object",icon='ERROR')
        else:
            if len(obj.animation_data.drivers) == 0:
                layout.label("There are no drivers assigned to the object",icon='ERROR')
            for DR in obj.animation_data.drivers:
                box = layout.box()
                row = box.row()
                DriverName = DR.data_path
                if DriverName in {"location","rotation_euler","dimensions" ,"lock_scale",'lock_location','lock_rotation'}:
                    if DR.array_index == 0:
                        DriverName = DriverName + " X"
                    if DR.array_index == 1:
                        DriverName = DriverName + " Y"
                    if DR.array_index == 2:
                        DriverName = DriverName + " Z"                     
                value = eval('bpy.data.objects["' + obj.name + '"].' + DR.data_path)
                if type(value).__name__ == 'str':
                    row.label(DriverName + " = " + str(value),icon='AUTO')
                elif type(value).__name__ == 'float':
                    row.label(DriverName + " = " + str(unit(value)),icon='AUTO')
                elif type(value).__name__ == 'int':
                    row.label(DriverName + " = " + str(value),icon='AUTO')
                elif type(value).__name__ == 'bool':
                    row.label(DriverName + " = " + str(value),icon='AUTO')
                elif type(value).__name__ == 'bpy_prop_array':
                    row.label(DriverName + " = " + str(value[DR.array_index]),icon='AUTO')
                elif type(value).__name__ == 'Vector':
                    row.label(DriverName + " = " + str(unit(value[DR.array_index])),icon='AUTO')
                elif type(value).__name__ == 'Euler':
                    row.label(DriverName + " = " + str(unit(value[DR.array_index])),icon='AUTO')
                else:
                    row.label(DriverName + " = " + str(type(value)),icon='AUTO')

                props = row.operator("fd_driver.add_variable_to_object",text="",icon='ZOOMIN')
                props.object_name = obj.name
                props.data_path = DR.data_path
                props.array_index = DR.array_index
                obj_bp = get_assembly_bp(obj)
                if obj_bp:
                    props = row.operator('fd_driver.get_vars_from_object',text="",icon='DRIVER')
                    props.object_name = obj.name
                    props.var_object_name = obj_bp.name
                    props.data_path = DR.data_path
                    props.array_index = DR.array_index
                draw_driver_expression(box,DR)
#                 draw_add_variable_operators(box,obj.name,DR.data_path,DR.array_index)
                draw_driver_variables(box,DR,obj.name)

def draw_driver_expression(layout,driver):
    row = layout.row(align=True)
    row.prop(driver.driver,'show_debug_info',text="",icon='OOPS')
    if driver.driver.is_valid:
        row.prop(driver.driver,"expression",text="",expand=True,icon='FILE_TICK')
        if driver.mute:
            row.prop(driver,"mute",text="",icon='OUTLINER_DATA_SPEAKER')
        else:
            row.prop(driver,"mute",text="",icon='OUTLINER_OB_SPEAKER')
    else:
        row.prop(driver.driver,"expression",text="",expand=True,icon='ERROR')
        if driver.mute:
            row.prop(driver,"mute",text="",icon='OUTLINER_DATA_SPEAKER')
        else:
            row.prop(driver,"mute",text="",icon='OUTLINER_OB_SPEAKER')

def draw_driver_variables(layout,driver,object_name):
    
    for var in driver.driver.variables:
        col = layout.column()
        boxvar = col.box()
        row = boxvar.row(align=True)
        row.prop(var,"name",text="",icon='FORWARD')
        
        props = row.operator("fd_driver.remove_variable",text="",icon='X',emboss=False)
        props.object_name = object_name
        props.data_path = driver.data_path
        props.array_index = driver.array_index
        props.var_name = var.name
        for target in var.targets:
            if driver.driver.show_debug_info:
                row = boxvar.row()
                row.prop(var,"type",text="")
                row = boxvar.row()
                row.prop(target,"id",text="")
                row = boxvar.row(align=True)
                row.prop(target,"data_path",text="",icon='ANIM_DATA')
            if target.id and target.data_path != "":
                value = eval('bpy.data.objects["' + target.id.name + '"]'"." + target.data_path)
            else:
                value = "ERROR#"
            row = boxvar.row()
            row.label("",icon='BLANK1')
            row.label("",icon='BLANK1')
            if type(value).__name__ == 'str':
                row.label("Value: " + value)
            elif type(value).__name__ == 'float':
                row.label("Value: " + str(unit(value)))
            elif type(value).__name__ == 'int':
                row.label("Value: " + str(value))
            elif type(value).__name__ == 'bool':
                row.label("Value: " + str(value))
                
def draw_add_variable_operators(layout,object_name,data_path,array_index):
    #GLOBAL PROMPT
    obj = bpy.data.objects[object_name]
    obj_bp = get_assembly_bp(obj)
    box = layout.box()
    box.label("Quick Variables",icon='DRIVER')
    row = box.row()
    if obj_bp:
        props = row.operator('fd_driver.get_vars_from_object',text="Group Variables",icon='DRIVER')
        props.object_name = object_name
        props.var_object_name = obj_bp.name
        props.data_path = data_path
        props.array_index = array_index
