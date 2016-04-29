from . fcurve import FCurve
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class AnimDataDrivers(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def from_existing(self, src_driver):
        '''Add a new driver given an existing one
        
        Parameter:
          src_driver: (FCurve) Existing Driver F-Curve to use as template for a new one
        
        Returns:
          driver: (FCurve) New Driver F-Curve'''
        return FCurve()
    def get(key): return FCurve()
    def __getitem__(key): return FCurve()
    def __iter__(key): yield FCurve()