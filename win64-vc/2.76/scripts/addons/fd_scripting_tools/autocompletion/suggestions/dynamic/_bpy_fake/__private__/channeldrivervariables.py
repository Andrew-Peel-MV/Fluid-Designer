from . drivervariable import DriverVariable
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class ChannelDriverVariables(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self):
        '''Add a new variable for the driver
        
        Returns:
          var: (DriverVariable) Newly created Driver Variable'''
        return DriverVariable()
    def remove(self, variable):
        '''Remove an existing variable from the driver
        
        Parameter:
          variable: (DriverVariable) Variable to remove from the driver'''
        return 
    def get(key): return DriverVariable()
    def __getitem__(key): return DriverVariable()
    def __iter__(key): yield DriverVariable()