from . struct import Struct
from . lattice import Lattice
from . bpy_struct import bpy_struct
import mathutils

class BlendDataLattices(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def is_updated(self):
        '''(Boolean)'''
        return bool()
    def new(self, name):
        '''Add a new lattice to the main database
        
        Parameter:
          name: (String) New name for the datablock
        
        Returns:
          lattice: (Lattice) New lattices datablock'''
        return Lattice()
    def remove(self, lattice):
        '''Remove a lattice from the current blendfile
        
        Parameter:
          lattice: (Lattice) Lattice to remove'''
        return 
    def tag(self, value):
        '''tag
        
        Parameter:
          value: (Boolean)'''
        return 
    def get(key): return Lattice()
    def __getitem__(key): return Lattice()
    def __iter__(key): yield Lattice()