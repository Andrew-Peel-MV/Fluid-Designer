from . struct import Struct
from . text import Text
from . bpy_struct import bpy_struct
import mathutils

class BlendDataTexts(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def is_updated(self):
        '''(Boolean)'''
        return bool()
    def new(self, name):
        '''Add a new text to the main database
        
        Parameter:
          name: (String) New name for the datablock
        
        Returns:
          text: (Text) New text datablock'''
        return Text()
    def remove(self, text):
        '''Remove a text from the current blendfile
        
        Parameter:
          text: (Text) Text to remove'''
        return 
    def load(self, filepath, internal):
        '''Add a new text to the main database from a file
        
        Parameter:
          filepath: (String) path for the datablock
          internal: (Boolean) Make text file internal after loading
        
        Returns:
          text: (Text) New text datablock'''
        return Text()
    def tag(self, value):
        '''tag
        
        Parameter:
          value: (Boolean)'''
        return 
    def get(key): return Text()
    def __getitem__(key): return Text()
    def __iter__(key): yield Text()