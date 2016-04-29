from . particlesettings import ParticleSettings
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class BlendDataParticles(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def is_updated(self):
        '''(Boolean)'''
        return bool()
    def new(self, name):
        '''Add a new particle settings instance to the main database
        
        Parameter:
          name: (String) New name for the datablock
        
        Returns:
          particle: (ParticleSettings) New particle settings datablock'''
        return ParticleSettings()
    def remove(self, particle):
        '''Remove a particle settings instance from the current blendfile
        
        Parameter:
          particle: (ParticleSettings) Particle Settings to remove'''
        return 
    def tag(self, value):
        '''tag
        
        Parameter:
          value: (Boolean)'''
        return 
    def get(key): return ParticleSettings()
    def __getitem__(key): return ParticleSettings()
    def __iter__(key): yield ParticleSettings()