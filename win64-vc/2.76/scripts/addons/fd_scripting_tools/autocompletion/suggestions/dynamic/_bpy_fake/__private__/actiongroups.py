from . actiongroup import ActionGroup
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class ActionGroups(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self, name):
        '''Create a new action group and add it to the action
        
        Parameter:
          name: (String) New name for the action group
        
        Returns:
          action_group: (ActionGroup) Newly created action group'''
        return ActionGroup()
    def remove(self, action_group):
        '''Remove action group
        
        Parameter:
          action_group: (ActionGroup) Action group to remove'''
        return 
    def get(key): return ActionGroup()
    def __getitem__(key): return ActionGroup()
    def __iter__(key): yield ActionGroup()