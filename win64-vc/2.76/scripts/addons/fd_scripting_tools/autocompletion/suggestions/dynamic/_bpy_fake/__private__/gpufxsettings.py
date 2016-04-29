from . gpussaosettings import GPUSSAOSettings
from . gpudofsettings import GPUDOFSettings
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class GPUFXSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def dof(self):
        '''(GPUDOFSettings)'''
        return GPUDOFSettings()
    @property
    def use_dof(self):
        '''(Boolean) Use depth of field on viewport using the values from active
        camera'''
        return bool()
    @property
    def ssao(self):
        '''(GPUSSAOSettings)'''
        return GPUSSAOSettings()
    @property
    def use_ssao(self):
        '''(Boolean) Use screen space ambient occlusion of field on viewport'''
        return bool()