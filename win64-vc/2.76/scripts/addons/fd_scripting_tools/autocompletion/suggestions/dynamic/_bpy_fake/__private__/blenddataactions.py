from . action import Action
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class BlendDataActions(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def is_updated(self):
        '''(Boolean)'''
        return bool()
    def new(self, name):
        '''Add a new action to the main database
        
        Parameter:
          name: (String) New name for the datablock
        
        Returns:
          action: (Action) New action datablock'''
        return Action()
    def remove(self, action):
        '''Remove a action from the current blendfile
        
        Parameter:
          action: (Action) Action to remove'''
        return 
    def tag(self, value):
        '''tag
        
        Parameter:
          value: (Boolean)'''
        return 
    def get(key): return Action()
    def __getitem__(key): return Action()
    def __iter__(key): yield Action()