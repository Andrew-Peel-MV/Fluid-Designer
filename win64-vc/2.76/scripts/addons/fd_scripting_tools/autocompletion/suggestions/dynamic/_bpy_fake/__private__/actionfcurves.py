from . fcurve import FCurve
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class ActionFCurves(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self, data_path, index, action_group):
        '''Add an F-Curve to the action
        
        Parameter:
          data_path: (String) F-Curve data path to use
          index: (Integer) Array index
          action_group: (String) Acton group to add this F-Curve into
        
        Returns:
          fcurve: (FCurve) Newly created F-Curve'''
        return FCurve()
    def find(self, data_path, index):
        '''Find an F-Curve. Note that this function performs a linear scan of all
        F-Curves in the action.
        
        Parameter:
          data_path: (String) F-Curve data path
          index: (Integer) Array index
        
        Returns:
          fcurve: (FCurve) The found F-Curve, or None if it doesn't exist'''
        return FCurve()
    def remove(self, fcurve):
        '''Remove action group
        
        Parameter:
          fcurve: (FCurve) F-Curve to remove'''
        return 
    def get(key): return FCurve()
    def __getitem__(key): return FCurve()
    def __iter__(key): yield FCurve()