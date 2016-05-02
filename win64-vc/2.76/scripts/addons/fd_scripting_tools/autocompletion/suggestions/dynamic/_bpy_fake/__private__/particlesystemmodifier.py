from . struct import Struct
from . particlesystem import ParticleSystem
from . bpy_struct import bpy_struct
import mathutils

class ParticleSystemModifier(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Modifier name'''
        return str()
    @property
    def type(self):
        '''(Enum)
        
        [DATA_TRANSFER, MESH_CACHE, NORMAL_EDIT, UV_PROJECT, UV_WARP,
        VERTEX_WEIGHT_EDIT, VERTEX_WEIGHT_MIX, VERTEX_WEIGHT_PROXIMITY, ARRAY,
        BEVEL, BOOLEAN, BUILD, DECIMATE, EDGE_SPLIT, MASK, MIRROR, MULTIRES,
        REMESH, SCREW, SKIN, SOLIDIFY, SUBSURF, TRIANGULATE, WIREFRAME,
        ARMATURE, CAST, CORRECTIVE_SMOOTH, CURVE, DISPLACE, HOOK,
        LAPLACIANSMOOTH, LAPLACIANDEFORM, LATTICE, MESH_DEFORM, SHRINKWRAP,
        SIMPLE_DEFORM, SMOOTH, WARP, WAVE, CLOTH, COLLISION, DYNAMIC_PAINT,
        EXPLODE, FLUID_SIMULATION, OCEAN, PARTICLE_INSTANCE, PARTICLE_SYSTEM,
        SMOKE, SOFT_BODY, SURFACE]'''
        return str()
    @property
    def show_viewport(self):
        '''(Boolean) Display modifier in viewport'''
        return bool()
    @property
    def show_render(self):
        '''(Boolean) Use modifier during render'''
        return bool()
    @property
    def show_in_editmode(self):
        '''(Boolean) Display modifier in Edit mode'''
        return bool()
    @property
    def show_on_cage(self):
        '''(Boolean) Adjust edit cage to modifier result'''
        return bool()
    @property
    def show_expanded(self):
        '''(Boolean) Set modifier expanded in the user interface'''
        return bool()
    @property
    def use_apply_on_spline(self):
        '''(Boolean) Apply this and all preceding deformation modifiers on
        splines' points rather than on filled curve/surface'''
        return bool()
    @property
    def particle_system(self):
        '''(ParticleSystem) Particle System that this modifier controls'''
        return ParticleSystem()