from . struct import Struct
from . movieclip import MovieClip
from . bpy_struct import bpy_struct
import mathutils

class BlendDataMovieClips(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def tag(self, value):
        '''tag
        
        Parameter:
          value: (Boolean)'''
        return 
    def remove(self, clip):
        '''Remove a movie clip from the current blendfile.
        
        Parameter:
          clip: (MovieClip) Movie clip to remove'''
        return 
    def load(self, filepath):
        '''Add a new movie clip to the main database from a file
        
        Parameter:
          filepath: (String) path for the datablock
        
        Returns:
          clip: (MovieClip) New movie clip datablock'''
        return MovieClip()
    def get(key): return MovieClip()
    def __getitem__(key): return MovieClip()
    def __iter__(key): yield MovieClip()