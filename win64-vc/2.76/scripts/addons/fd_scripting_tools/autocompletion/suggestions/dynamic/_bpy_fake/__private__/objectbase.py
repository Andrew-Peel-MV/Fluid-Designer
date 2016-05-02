from . struct import Struct
from . object import Object
from . spaceview3d import SpaceView3D
from . bpy_struct import bpy_struct
import mathutils

class ObjectBase(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def object(self):
        '''(Object) Object this base links to'''
        return Object()
    @property
    def layers(self):
        '''(Boolean[20]) Layers the object base is on'''
        return bool()
    @property
    def layers_local_view(self):
        '''(Boolean[8]) 3D local view layers the object base is on'''
        return bool()
    @property
    def select(self):
        '''(Boolean) Object base selection state'''
        return bool()
    def layers_from_view(self, view):
        '''Sets the object layers from a 3D View (use when adding an object in
        local view)
        
        Parameter:
          view: (SpaceView3D)'''
        return 