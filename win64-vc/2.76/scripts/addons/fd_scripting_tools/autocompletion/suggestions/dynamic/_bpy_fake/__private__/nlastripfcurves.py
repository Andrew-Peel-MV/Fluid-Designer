from . fcurve import FCurve
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class NlaStripFCurves(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def find(self, data_path, index):
        '''Find an F-Curve. Note that this function performs a linear scan of all
        F-Curves in the NLA strip.
        
        Parameter:
          data_path: (String) F-Curve data path
          index: (Integer) Array index
        
        Returns:
          fcurve: (FCurve) The found F-Curve, or None if it doesn't exist'''
        return FCurve()
    def get(key): return FCurve()
    def __getitem__(key): return FCurve()
    def __iter__(key): yield FCurve()