from . struct import Struct
from . object import Object
from . texture import Texture
from . bpy_struct import bpy_struct
import mathutils

class FieldSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def type(self):
        '''(Enum) Type of field
        
        [NONE, FORCE, WIND, VORTEX, MAGNET, HARMONIC, CHARGE, LENNARDJ,
        TEXTURE, GUIDE, BOID, TURBULENCE, DRAG, SMOKE_FLOW]'''
        return str()
    @property
    def shape(self):
        '''(Enum) Which direction is used to calculate the effector force
        
        [POINT, PLANE, SURFACE, POINTS]'''
        return str()
    @property
    def falloff_type(self):
        '''(Enum)
        
        [SPHERE, TUBE, CONE]'''
        return str()
    @property
    def texture_mode(self):
        '''(Enum) How the texture effect is calculated (RGB & Curl need a RGB
        texture, else Gradient will be used instead)
        
        [RGB, GRADIENT, CURL]'''
        return str()
    @property
    def z_direction(self):
        '''(Enum) Effect in full or only positive/negative Z direction
        
        [BOTH, POSITIVE, NEGATIVE]'''
        return str()
    @property
    def strength(self):
        '''(Float) Strength of force field'''
        return float()
    @property
    def linear_drag(self):
        '''(Float) Drag component proportional to velocity'''
        return float()
    @property
    def harmonic_damping(self):
        '''(Float) Damping of the harmonic force'''
        return float()
    @property
    def quadratic_drag(self):
        '''(Float) Drag component proportional to the square of velocity'''
        return float()
    @property
    def flow(self):
        '''(Float) Convert effector force into air flow velocity'''
        return float()
    @property
    def inflow(self):
        '''(Float) Inwards component of the vortex force'''
        return float()
    @property
    def size(self):
        '''(Float) Size of the turbulence'''
        return float()
    @property
    def rest_length(self):
        '''(Float) Rest length of the harmonic force'''
        return float()
    @property
    def falloff_power(self):
        '''(Float) Falloff power (real gravitational falloff = 2)'''
        return float()
    @property
    def distance_min(self):
        '''(Float) Minimum distance for the field's fall-off'''
        return float()
    @property
    def distance_max(self):
        '''(Float) Maximum distance for the field to work'''
        return float()
    @property
    def radial_min(self):
        '''(Float) Minimum radial distance for the field's fall-off'''
        return float()
    @property
    def radial_max(self):
        '''(Float) Maximum radial distance for the field to work'''
        return float()
    @property
    def radial_falloff(self):
        '''(Float) Radial falloff power (real gravitational falloff = 2)'''
        return float()
    @property
    def texture_nabla(self):
        '''(Float) Defines size of derivative offset used for calculating
        gradient and curl'''
        return float()
    @property
    def noise(self):
        '''(Float) Amount of noise for the force strength'''
        return float()
    @property
    def seed(self):
        '''(Integer) Seed of the noise'''
        return int()
    @property
    def use_min_distance(self):
        '''(Boolean) Use a minimum distance for the field's fall-off'''
        return bool()
    @property
    def use_max_distance(self):
        '''(Boolean) Use a maximum distance for the field to work'''
        return bool()
    @property
    def use_radial_min(self):
        '''(Boolean) Use a minimum radial distance for the field's fall-off'''
        return bool()
    @property
    def use_radial_max(self):
        '''(Boolean) Use a maximum radial distance for the field to work'''
        return bool()
    @property
    def use_object_coords(self):
        '''(Boolean) Use object/global coordinates for texture'''
        return bool()
    @property
    def use_global_coords(self):
        '''(Boolean) Use effector/global coordinates for turbulence'''
        return bool()
    @property
    def use_2d_force(self):
        '''(Boolean) Apply force only in 2D'''
        return bool()
    @property
    def use_root_coords(self):
        '''(Boolean) Texture coordinates from root particle locations'''
        return bool()
    @property
    def apply_to_location(self):
        '''(Boolean) Effect particles' location'''
        return bool()
    @property
    def apply_to_rotation(self):
        '''(Boolean) Effect particles' dynamic rotation'''
        return bool()
    @property
    def use_absorption(self):
        '''(Boolean) Force gets absorbed by collision objects'''
        return bool()
    @property
    def use_multiple_springs(self):
        '''(Boolean) Every point is effected by multiple springs'''
        return bool()
    @property
    def use_smoke_density(self):
        '''(Boolean) Adjust force strength based on smoke density'''
        return bool()
    @property
    def texture(self):
        '''(Texture) Texture to use as force'''
        return Texture()
    @property
    def source_object(self):
        '''(Object) Select domain object of the smoke simulation'''
        return Object()
    @property
    def guide_minimum(self):
        '''(Float) The distance from which particles are affected fully'''
        return float()
    @property
    def guide_free(self):
        '''(Float) Guide-free time from particle life's end'''
        return float()
    @property
    def use_guide_path_add(self):
        '''(Boolean) Based on distance/falloff it adds a portion of the entire
        path'''
        return bool()
    @property
    def use_guide_path_weight(self):
        '''(Boolean) Use curve weights to influence the particle influence along
        the curve'''
        return bool()
    @property
    def guide_clump_amount(self):
        '''(Float) Amount of clumping'''
        return float()
    @property
    def guide_clump_shape(self):
        '''(Float) Shape of clumping'''
        return float()
    @property
    def guide_kink_type(self):
        '''(Enum) Type of periodic offset on the curve
        
        [NONE, CURL, RADIAL, WAVE, BRAID, ROTATION, ROLL]'''
        return str()
    @property
    def guide_kink_axis(self):
        '''(Enum) Which axis to use for offset
        
        [X, Y, Z]'''
        return str()
    @property
    def guide_kink_frequency(self):
        '''(Float) The frequency of the offset (1/total length)'''
        return float()
    @property
    def guide_kink_shape(self):
        '''(Float) Adjust the offset to the beginning/end'''
        return float()
    @property
    def guide_kink_amplitude(self):
        '''(Float) The amplitude of the offset'''
        return float()