from . scene import Scene
from . mesh import Mesh
from . struct import Struct
from . object import Object
from . bpy_struct import bpy_struct
import mathutils

class BlendDataMeshes(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def is_updated(self):
        '''(Boolean)'''
        return bool()
    def new(self, name):
        '''Add a new mesh to the main database
        
        Parameter:
          name: (String) New name for the datablock
        
        Returns:
          mesh: (Mesh) New mesh datablock'''
        return Mesh()
    def new_from_object(self, scene, object, apply_modifiers, settings, calc_tessface, calc_undeformed):
        '''Add a new mesh created from object with modifiers applied
        
        Parameter:
          scene: (Scene) Scene within which to evaluate modifiers
          object: (Object) Object to create mesh from
          apply_modifiers: (Boolean) Apply modifiers
          settings: (Enum) Modifier settings to apply
          calc_tessface: (Boolean) Calculate tessellation faces
          calc_undeformed: (Boolean) Calculate undeformed vertex coordinates
        
        Returns:
          mesh:
            (Mesh) Mesh created from object, remove it if it is only used for
            export'''
        return Mesh()
    def remove(self, mesh):
        '''Remove a mesh from the current blendfile
        
        Parameter:
          mesh: (Mesh) Mesh to remove'''
        return 
    def tag(self, value):
        '''tag
        
        Parameter:
          value: (Boolean)'''
        return 
    def get(key): return Mesh()
    def __getitem__(key): return Mesh()
    def __iter__(key): yield Mesh()