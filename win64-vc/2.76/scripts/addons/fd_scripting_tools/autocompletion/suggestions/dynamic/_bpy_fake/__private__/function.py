from . struct import Struct
from . property import Property
from . bpy_struct import bpy_struct
import mathutils

class Function(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def identifier(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def description(self):
        '''(String) Description of the Function's purpose'''
        return str()
    @property
    def parameters(self):
        '''(Sequence of Property) Parameters for the function'''
        return (Property(),)
    @property
    def is_registered(self):
        '''(Boolean) Function is registered as callback as part of type
        registration'''
        return bool()
    @property
    def is_registered_optional(self):
        '''(Boolean) Function is optionally registered as callback part of type
        registration'''
        return bool()
    @property
    def use_self(self):
        '''(Boolean) Function does not pass its self as an argument (becomes a
        static method in python)'''
        return bool()
    @property
    def use_self_type(self):
        '''(Boolean) Function passes its self type as an argument (becomes a
        class method in python if use_self is false)'''
        return bool()