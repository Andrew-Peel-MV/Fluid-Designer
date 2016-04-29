from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class SceneGameRecastData(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def cell_size(self):
        '''(Float) Rasterized cell size'''
        return float()
    @property
    def cell_height(self):
        '''(Float) Rasterized cell height'''
        return float()
    @property
    def agent_height(self):
        '''(Float) Minimum height where the agent can still walk'''
        return float()
    @property
    def agent_radius(self):
        '''(Float) Radius of the agent'''
        return float()
    @property
    def climb_max(self):
        '''(Float) Maximum height between grid cells the agent can climb'''
        return float()
    @property
    def slope_max(self):
        '''(Float) Maximum walkable slope angle'''
        return float()
    @property
    def region_min_size(self):
        '''(Float) Minimum regions size (smaller regions will be deleted)'''
        return float()
    @property
    def region_merge_size(self):
        '''(Float) Minimum regions size (smaller regions will be merged)'''
        return float()
    @property
    def edge_max_len(self):
        '''(Float) Maximum contour edge length'''
        return float()
    @property
    def edge_max_error(self):
        '''(Float) Maximum distance error from contour to cells'''
        return float()
    @property
    def verts_per_poly(self):
        '''(Integer) Max number of vertices per polygon'''
        return int()
    @property
    def sample_dist(self):
        '''(Float) Detail mesh sample spacing'''
        return float()
    @property
    def sample_max_error(self):
        '''(Float) Detail mesh simplification max sample error'''
        return float()