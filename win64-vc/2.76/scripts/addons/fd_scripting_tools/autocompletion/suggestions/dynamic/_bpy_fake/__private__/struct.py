from . function import Function
from . stringproperty import StringProperty
from . struct import Struct
from . property import Property
from . bpy_struct import bpy_struct
import mathutils

class Struct(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Human readable name'''
        return str()
    @property
    def identifier(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def description(self):
        '''(String) Description of the Struct's purpose'''
        return str()
    @property
    def translation_context(self):
        '''(String) Translation context of the struct's name'''
        return str()
    @property
    def base(self):
        '''(Struct) Struct definition this is derived from'''
        return Struct()
    @property
    def nested(self):
        '''(Struct) Struct in which this struct is always nested, and to which it
        logically belongs'''
        return Struct()
    @property
    def name_property(self):
        '''(StringProperty) Property that gives the name of the struct'''
        return StringProperty()
    @property
    def properties(self):
        '''(Sequence of Property) Properties in the struct'''
        return (Property(),)
    @property
    def functions(self):
        '''(Sequence of Function)'''
        return (Function(),)