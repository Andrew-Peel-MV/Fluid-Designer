from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class SketchfabProps(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def token(self):
        '''(String) You can find this on your dashboard at the Sketchfab website'''
        return str()
    @property
    def private(self):
        '''(Boolean) Upload as private (requires a pro account)'''
        return bool()
    @property
    def password(self):
        '''(String) Password-protect your model (requires a pro account)'''
        return str()
    @property
    def models(self):
        '''(Enum) Determines which meshes are exported
        
        [ALL, SELECTION]'''
        return str()
    @property
    def description(self):
        '''(String) Description of the model (optional)'''
        return str()
    @property
    def lamps(self):
        '''(Enum) Determines which lamps are exported
        
        [ALL, NONE, SELECTION]'''
        return str()
    @property
    def filepath(self):
        '''(String) internal use'''
        return str()
    @property
    def tabs(self):
        '''(Enum) Determines which lamps are exported
        
        [EXPORT, ACCOUNT]'''
        return str()
    @property
    def tags(self):
        '''(String) List of tags, separated by spaces (optional)'''
        return str()
    @property
    def title(self):
        '''(String) Title of the model (determined automatically if left empty)'''
        return str()