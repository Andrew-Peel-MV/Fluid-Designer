from . struct import Struct
from . controller import Controller
from . bpy_struct import bpy_struct
import mathutils

class Actuator(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String)'''
        return str()
    @property
    def type(self):
        '''(Enum)
        
        [ACTION, ARMATURE, CAMERA, CONSTRAINT, EDIT_OBJECT, FILTER_2D, GAME,
        MESSAGE, MOTION, MOUSE, PARENT, PROPERTY, RANDOM, SCENE, SOUND, STATE,
        STEERING, VISIBILITY]'''
        return str()
    @property
    def pin(self):
        '''(Boolean) Display when not linked to a visible states controller'''
        return bool()
    @property
    def show_expanded(self):
        '''(Boolean) Set actuator expanded in the user interface'''
        return bool()
    @property
    def active(self):
        '''(Boolean) Set the active state of the actuator'''
        return bool()
    def link(self, controller):
        '''Link the actuator to a controller
        
        Parameter:
          controller: (Controller) Controller to link to'''
        return 
    def unlink(self, controller):
        '''Unlink the actuator from a controller
        
        Parameter:
          controller: (Controller) Controller to unlink from'''
        return 