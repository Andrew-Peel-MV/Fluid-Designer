from . struct import Struct
from . curve import Curve
from . bpy_struct import bpy_struct
import mathutils

class BlendDataCurves(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def is_updated(self):
        '''(Boolean)'''
        return bool()
    def new(self, name, type):
        '''Add a new curve to the main database
        
        Parameter:
          name: (String) New name for the datablock
          type: (Enum) The type of curve to add
        
        Returns:
          curve: (Curve) New curve datablock'''
        return Curve()
    def remove(self, curve):
        '''Remove a curve from the current blendfile
        
        Parameter:
          curve: (Curve) Curve to remove'''
        return 
    def tag(self, value):
        '''tag
        
        Parameter:
          value: (Boolean)'''
        return 
    def get(key): return Curve()
    def __getitem__(key): return Curve()
    def __iter__(key): yield Curve()