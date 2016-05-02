from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class Machine_Token(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def associative_depth(self):
        '''(Float)'''
        return float()
    @property
    def dim_to_first_const_hole(self):
        '''(Float)'''
        return float()
    @property
    def lead_out(self):
        '''(Float)'''
        return float()
    @property
    def end_dim_in_y(self):
        '''(Float)'''
        return float()
    @property
    def edge_bore_depth(self):
        '''(Float)'''
        return float()
    @property
    def beginning_depth(self):
        '''(Float)'''
        return float()
    @property
    def face_bore_depth(self):
        '''(Float)'''
        return float()
    @property
    def dim_in_x(self):
        '''(Float)'''
        return float()
    @property
    def face(self):
        '''(Enum) Select the face to assign the machine token to.
        
        [1, 2, 3, 4, 5, 6]'''
        return str()
    @property
    def dim_to_first_row(self):
        '''(Float)'''
        return float()
    @property
    def face_bore_dia_2(self):
        '''(Float)'''
        return float()
    @property
    def dim_to_second_row(self):
        '''(Float)'''
        return float()
    @property
    def panel_penetration(self):
        '''(Float)'''
        return float()
    @property
    def edge_bore_dia(self):
        '''(Float)'''
        return float()
    @property
    def z_value(self):
        '''(Float)'''
        return float()
    @property
    def tool_number(self):
        '''(String)'''
        return str()
    @property
    def end_dim_in_x(self):
        '''(Float)'''
        return float()
    @property
    def lead_in(self):
        '''(Float)'''
        return float()
    @property
    def cam_face(self):
        '''(Enum) The face number the cam is assigned to.
        
        [5, 6]'''
        return str()
    @property
    def backset(self):
        '''(Float)'''
        return float()
    @property
    def show_expanded(self):
        '''(Boolean)'''
        return bool()
    @property
    def distance_between_holes(self):
        '''(Float)'''
        return float()
    @property
    def associative_dia(self):
        '''(Float)'''
        return float()
    @property
    def shelf_hole_spacing(self):
        '''(Float)'''
        return float()
    @property
    def double_pass(self):
        '''(Float)'''
        return float()
    @property
    def space_from_top(self):
        '''(Float)'''
        return float()
    @property
    def shelf_clip_gap(self):
        '''(Float)'''
        return float()
    @property
    def dim_in_y(self):
        '''(Float)'''
        return float()
    @property
    def dim_to_last_const_hole(self):
        '''(Float)'''
        return float()
    @property
    def face_bore_depth_2(self):
        '''(Float)'''
        return float()
    @property
    def face_bore_dia(self):
        '''(Float)'''
        return float()
    @property
    def hole_locations(self):
        '''(Float[15])'''
        return ''
    @property
    def type_token(self):
        '''(Enum) Select the Machine Token Type.
        
        [NONE, CONST, HOLES, SHLF, SHELF, SHELFSTD, DADO, SAW, SLIDE, CAMLOCK,
        MITER, BORE]'''
        return str()
    @property
    def dim_in_z(self):
        '''(Float)'''
        return float()
    @property
    def angle(self):
        '''(Float)'''
        return float()
    @property
    def drill_from_opposite_side(self):
        '''(Boolean)'''
        return bool()
    @property
    def second_hole_at_32mm(self):
        '''(Boolean)'''
        return bool()
    @property
    def space_from_bottom(self):
        '''(Float)'''
        return float()
    @property
    def edge(self):
        '''(Enum) Select the edge to assign the machine token to.
        
        [1, 2, 3, 4, 5, 6]'''
        return str()
    @property
    def lock_joint(self):
        '''(Float)'''
        return float()
    @property
    def reverse_direction(self):
        '''(Boolean)'''
        return bool()
    @property
    def tongue_tool_number(self):
        '''(String)'''
        return str()