from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MaterialHalo(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def size(self):
        '''(Float) Dimension of the halo'''
        return float()
    @property
    def hardness(self):
        '''(Integer) Hardness of the halo'''
        return int()
    @property
    def add(self):
        '''(Float) Strength of the add effect'''
        return float()
    @property
    def ring_count(self):
        '''(Integer) Number of rings rendered over the halo'''
        return int()
    @property
    def line_count(self):
        '''(Integer) Number of star shaped lines rendered over the halo'''
        return int()
    @property
    def star_tip_count(self):
        '''(Integer) Number of points on the star shaped halo'''
        return int()
    @property
    def seed(self):
        '''(Integer) Randomize ring dimension and line location'''
        return int()
    @property
    def use_flare_mode(self):
        '''(Boolean) Render halo as a lens flare'''
        return bool()
    @property
    def flare_size(self):
        '''(Float) Factor by which the flare is larger than the halo'''
        return float()
    @property
    def flare_subflare_size(self):
        '''(Float) Dimension of the sub-flares, dots and circles'''
        return float()
    @property
    def flare_boost(self):
        '''(Float) Give the flare extra strength'''
        return float()
    @property
    def flare_seed(self):
        '''(Integer) Offset in the flare seed table'''
        return int()
    @property
    def flare_subflare_count(self):
        '''(Integer) Number of sub-flares'''
        return int()
    @property
    def use_ring(self):
        '''(Boolean) Render rings over halo'''
        return bool()
    @property
    def use_lines(self):
        '''(Boolean) Render star shaped lines over halo'''
        return bool()
    @property
    def use_star(self):
        '''(Boolean) Render halo as a star'''
        return bool()
    @property
    def use_texture(self):
        '''(Boolean) Give halo a texture'''
        return bool()
    @property
    def use_vertex_normal(self):
        '''(Boolean) Use the vertex normal to specify the dimension of the halo'''
        return bool()
    @property
    def use_extreme_alpha(self):
        '''(Boolean) Use extreme alpha'''
        return bool()
    @property
    def use_shaded(self):
        '''(Boolean) Let halo receive light and shadows from external objects'''
        return bool()
    @property
    def use_soft(self):
        '''(Boolean) Soften the edges of halos at intersections with other
        geometry'''
        return bool()