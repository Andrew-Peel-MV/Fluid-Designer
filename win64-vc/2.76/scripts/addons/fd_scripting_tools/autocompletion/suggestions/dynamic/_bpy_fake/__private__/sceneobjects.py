from . objectbase import ObjectBase
from . object import Object
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class SceneObjects(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(Object) Active object for this scene'''
        return Object()
    def link(self, object):
        '''Link object to scene, run scene.update() after
        
        Parameter:
          object: (Object) Object to add to scene
        
        Returns:
          base: (ObjectBase) The newly created base'''
        return ObjectBase()
    def unlink(self, object):
        '''Unlink object from scene
        
        Parameter:
          object: (Object) Object to remove from scene'''
        return 
    def get(key): return Object()
    def __getitem__(key): return Object()
    def __iter__(key): yield Object()