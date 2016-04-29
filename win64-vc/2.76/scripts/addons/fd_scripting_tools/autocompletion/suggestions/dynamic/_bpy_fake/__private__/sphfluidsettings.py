from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class SPHFluidSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def solver(self):
        '''(Enum) The code used to calculate internal forces on particles
        
        [DDR, CLASSICAL]'''
        return str()
    @property
    def spring_force(self):
        '''(Float) Spring force'''
        return float()
    @property
    def fluid_radius(self):
        '''(Float) Fluid interaction radius'''
        return float()
    @property
    def rest_length(self):
        '''(Float) Spring rest length (factor of particle radius)'''
        return float()
    @property
    def use_viscoelastic_springs(self):
        '''(Boolean) Use viscoelastic springs instead of Hooke's springs'''
        return bool()
    @property
    def use_initial_rest_length(self):
        '''(Boolean) Use the initial length as spring rest length instead of 2 *
        particle size'''
        return bool()
    @property
    def plasticity(self):
        '''(Float) How much the spring rest length can change after the elastic
        limit is crossed'''
        return float()
    @property
    def yield_ratio(self):
        '''(Float) How much the spring has to be stretched/compressed in order to
        change it's rest length'''
        return float()
    @property
    def spring_frames(self):
        '''(Integer) Create springs for this number of frames since particles
        birth (0 is always)'''
        return int()
    @property
    def linear_viscosity(self):
        '''(Float) Linear viscosity'''
        return float()
    @property
    def stiff_viscosity(self):
        '''(Float) Creates viscosity for expanding fluid'''
        return float()
    @property
    def stiffness(self):
        '''(Float) How incompressible the fluid is (speed of sound)'''
        return float()
    @property
    def repulsion(self):
        '''(Float) How strongly the fluid tries to keep from clustering (factor
        of stiffness)'''
        return float()
    @property
    def rest_density(self):
        '''(Float) Fluid rest density'''
        return float()
    @property
    def buoyancy(self):
        '''(Float) Artificial buoyancy force in negative gravity direction based
        on pressure differences inside the fluid'''
        return float()
    @property
    def factor_repulsion(self):
        '''(Boolean) Repulsion is a factor of stiffness'''
        return bool()
    @property
    def use_factor_density(self):
        '''(Boolean) Density is calculated as a factor of default density
        (depends on particle size)'''
        return bool()
    @property
    def factor_radius(self):
        '''(Boolean) Interaction radius is a factor of 4 * particle size'''
        return bool()
    @property
    def factor_stiff_viscosity(self):
        '''(Boolean) Stiff viscosity is a factor of normal viscosity'''
        return bool()
    @property
    def factor_rest_length(self):
        '''(Boolean) Spring rest length is a factor of 2 * particle size'''
        return bool()