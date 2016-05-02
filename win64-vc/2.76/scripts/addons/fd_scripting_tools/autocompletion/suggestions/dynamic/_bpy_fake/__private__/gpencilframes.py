from . struct import Struct
from . gpencilframe import GPencilFrame
from . bpy_struct import bpy_struct
import mathutils

class GPencilFrames(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self, frame_number):
        '''Add a new grease pencil frame
        
        Parameter:
          frame_number: (Integer) The frame on which this sketch appears
        
        Returns:
          frame: (GPencilFrame) The newly created frame'''
        return GPencilFrame()
    def remove(self, frame):
        '''Remove a grease pencil frame
        
        Parameter:
          frame: (GPencilFrame) The frame to remove'''
        return 
    def copy(self, source):
        '''Copy a grease pencil frame
        
        Parameter:
          source: (GPencilFrame) The source frame
        
        Returns:
          copy: (GPencilFrame) The newly copied frame'''
        return GPencilFrame()
    def get(key): return GPencilFrame()
    def __getitem__(key): return GPencilFrame()
    def __iter__(key): yield GPencilFrame()