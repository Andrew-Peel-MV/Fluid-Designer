from . blenddatagroups import BlendDataGroups
from . blenddataobjects import BlendDataObjects
from . id import ID
from . blenddatanodetrees import BlendDataNodeTrees
from . blenddatafonts import BlendDataFonts
from . blenddatalinestyles import BlendDataLineStyles
from . blenddatameshes import BlendDataMeshes
from . blenddataworlds import BlendDataWorlds
from . blenddatamaterials import BlendDataMaterials
from . blenddatalamps import BlendDataLamps
from . blenddatatexts import BlendDataTexts
from . blenddataarmatures import BlendDataArmatures
from . blenddatascreens import BlendDataScreens
from . key import Key
from . blenddatagreasepencils import BlendDataGreasePencils
from . blenddatamasks import BlendDataMasks
from . blenddatascenes import BlendDataScenes
from . blenddatalibraries import BlendDataLibraries
from . blenddataparticles import BlendDataParticles
from . blenddataactions import BlendDataActions
from . blenddataspeakers import BlendDataSpeakers
from . blenddatawindowmanagers import BlendDataWindowManagers
from . blenddataimages import BlendDataImages
from . blenddatacurves import BlendDataCurves
from . blenddatamovieclips import BlendDataMovieClips
from . struct import Struct
from . blenddatapalettes import BlendDataPalettes
from . blenddatacameras import BlendDataCameras
from . blenddatalattices import BlendDataLattices
from . blenddatametaballs import BlendDataMetaBalls
from . blenddatatextures import BlendDataTextures
from . blenddatasounds import BlendDataSounds
from . blenddatabrushes import BlendDataBrushes
from . bpy_struct import bpy_struct
import mathutils

class BlendData(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def filepath(self):
        '''(String) Path to the .blend file'''
        return str()
    @property
    def is_dirty(self):
        '''(Boolean) Have recent edits been saved to disk'''
        return bool()
    @property
    def is_saved(self):
        '''(Boolean) Has the current session been saved to disk as a .blend file'''
        return bool()
    @property
    def use_autopack(self):
        '''(Boolean) Automatically pack all external data into .blend file'''
        return bool()
    @property
    def version(self):
        '''(Integer[3]) Version of the blender the .blend was saved with'''
        return int()
    @property
    def cameras(self):
        '''(Sequence of Camera) Camera datablocks'''
        return BlendDataCameras()
    @property
    def scenes(self):
        '''(Sequence of Scene) Scene datablocks'''
        return BlendDataScenes()
    @property
    def objects(self):
        '''(Sequence of Object) Object datablocks'''
        return BlendDataObjects()
    @property
    def materials(self):
        '''(Sequence of Material) Material datablocks'''
        return BlendDataMaterials()
    @property
    def node_groups(self):
        '''(Sequence of NodeTree) Node group datablocks'''
        return BlendDataNodeTrees()
    @property
    def meshes(self):
        '''(Sequence of Mesh) Mesh datablocks'''
        return BlendDataMeshes()
    @property
    def lamps(self):
        '''(Sequence of Lamp) Lamp datablocks'''
        return BlendDataLamps()
    @property
    def libraries(self):
        '''(Sequence of Library) Library datablocks'''
        return BlendDataLibraries()
    @property
    def screens(self):
        '''(Sequence of Screen) Screen datablocks'''
        return BlendDataScreens()
    @property
    def window_managers(self):
        '''(Sequence of WindowManager) Window manager datablocks'''
        return BlendDataWindowManagers()
    @property
    def images(self):
        '''(Sequence of Image) Image datablocks'''
        return BlendDataImages()
    @property
    def lattices(self):
        '''(Sequence of Lattice) Lattice datablocks'''
        return BlendDataLattices()
    @property
    def curves(self):
        '''(Sequence of Curve) Curve datablocks'''
        return BlendDataCurves()
    @property
    def metaballs(self):
        '''(Sequence of MetaBall) Metaball datablocks'''
        return BlendDataMetaBalls()
    @property
    def fonts(self):
        '''(Sequence of VectorFont) Vector font datablocks'''
        return BlendDataFonts()
    @property
    def textures(self):
        '''(Sequence of Texture) Texture datablocks'''
        return BlendDataTextures()
    @property
    def brushes(self):
        '''(Sequence of Brush) Brush datablocks'''
        return BlendDataBrushes()
    @property
    def worlds(self):
        '''(Sequence of World) World datablocks'''
        return BlendDataWorlds()
    @property
    def groups(self):
        '''(Sequence of Group) Group datablocks'''
        return BlendDataGroups()
    @property
    def shape_keys(self):
        '''(Sequence of Key) Shape Key datablocks'''
        return (Key(),)
    @property
    def scripts(self):
        '''(Sequence of ID) Script datablocks (DEPRECATED)'''
        return (ID(),)
    @property
    def texts(self):
        '''(Sequence of Text) Text datablocks'''
        return BlendDataTexts()
    @property
    def speakers(self):
        '''(Sequence of Speaker) Speaker datablocks'''
        return BlendDataSpeakers()
    @property
    def sounds(self):
        '''(Sequence of Sound) Sound datablocks'''
        return BlendDataSounds()
    @property
    def armatures(self):
        '''(Sequence of Armature) Armature datablocks'''
        return BlendDataArmatures()
    @property
    def actions(self):
        '''(Sequence of Action) Action datablocks'''
        return BlendDataActions()
    @property
    def particles(self):
        '''(Sequence of ParticleSettings) Particle datablocks'''
        return BlendDataParticles()
    @property
    def palettes(self):
        '''(Sequence of Palette) Palette datablocks'''
        return BlendDataPalettes()
    @property
    def grease_pencil(self):
        '''(Sequence of GreasePencil) Grease Pencil datablocks'''
        return BlendDataGreasePencils()
    @property
    def movieclips(self):
        '''(Sequence of MovieClip) Movie Clip datablocks'''
        return BlendDataMovieClips()
    @property
    def masks(self):
        '''(Sequence of Mask) Masks datablocks'''
        return BlendDataMasks()
    @property
    def linestyles(self):
        '''(Sequence of FreestyleLineStyle) Line Style datablocks'''
        return BlendDataLineStyles()