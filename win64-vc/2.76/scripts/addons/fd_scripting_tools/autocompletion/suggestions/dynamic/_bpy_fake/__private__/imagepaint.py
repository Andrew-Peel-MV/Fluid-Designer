from . brush import Brush
from . curvemapping import CurveMapping
from . struct import Struct
from . palette import Palette
from . image import Image
from . bpy_struct import bpy_struct
import mathutils

class ImagePaint(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def brush(self):
        '''(Brush) Active Brush'''
        return Brush()
    @property
    def palette(self):
        '''(Palette) Active Palette'''
        return Palette()
    @property
    def show_brush(self):
        '''(Boolean)'''
        return bool()
    @property
    def show_brush_on_surface(self):
        '''(Boolean)'''
        return bool()
    @property
    def show_low_resolution(self):
        '''(Boolean) For multires, show low resolution while navigating the view'''
        return bool()
    @property
    def input_samples(self):
        '''(Integer) Average multiple input samples together to smooth the brush
        stroke'''
        return int()
    @property
    def use_symmetry_x(self):
        '''(Boolean) Mirror brush across the X axis'''
        return bool()
    @property
    def use_symmetry_y(self):
        '''(Boolean) Mirror brush across the Y axis'''
        return bool()
    @property
    def use_symmetry_z(self):
        '''(Boolean) Mirror brush across the Z axis'''
        return bool()
    @property
    def use_symmetry_feather(self):
        '''(Boolean) Reduce the strength of the brush where it overlaps
        symmetrical daubs'''
        return bool()
    @property
    def cavity_curve(self):
        '''(CurveMapping) Editable cavity curve'''
        return CurveMapping()
    @property
    def use_cavity(self):
        '''(Boolean) Mask painting according to mesh geometry cavity'''
        return bool()
    @property
    def tile_offset(self):
        '''(Vector 3D) Stride at which tiled strokes are copied'''
        return mathutils.Vector()
    @property
    def tile_x(self):
        '''(Boolean) Tile along X axis'''
        return bool()
    @property
    def tile_y(self):
        '''(Boolean) Tile along Y axis'''
        return bool()
    @property
    def tile_z(self):
        '''(Boolean) Tile along Z axis'''
        return bool()
    @property
    def use_occlude(self):
        '''(Boolean) Only paint onto the faces directly under the brush (slower)'''
        return bool()
    @property
    def use_backface_culling(self):
        '''(Boolean) Ignore faces pointing away from the view (faster)'''
        return bool()
    @property
    def use_normal_falloff(self):
        '''(Boolean) Paint most on faces pointing towards the view'''
        return bool()
    @property
    def use_stencil_layer(self):
        '''(Boolean) Set the mask layer from the UV map buttons'''
        return bool()
    @property
    def invert_stencil(self):
        '''(Boolean) Invert the stencil layer'''
        return bool()
    @property
    def stencil_image(self):
        '''(Image) Image used as stencil'''
        return Image()
    @property
    def canvas(self):
        '''(Image) Image used as canvas'''
        return Image()
    @property
    def clone_image(self):
        '''(Image) Image used as clone source'''
        return Image()
    @property
    def stencil_color(self):
        '''(Vector 3D) Stencil color in the viewport'''
        return mathutils.Vector()
    @property
    def dither(self):
        '''(Float) Amount of dithering when painting on byte images'''
        return float()
    @property
    def use_clone_layer(self):
        '''(Boolean) Use another UV map as clone source, otherwise use the 3D
        cursor as the source'''
        return bool()
    @property
    def seam_bleed(self):
        '''(Integer) Extend paint beyond the faces UVs to reduce seams (in
        pixels, slower)'''
        return int()
    @property
    def normal_angle(self):
        '''(Integer) Paint most on faces pointing towards the view according to
        this angle'''
        return int()
    @property
    def screen_grab_size(self):
        '''(Integer[2]) Size to capture the image for re-projecting'''
        return int()
    @property
    def mode(self):
        '''(Enum) Mode of operation for projection painting
        
        [MATERIAL, IMAGE]'''
        return str()
    @property
    def missing_uvs(self):
        '''(Boolean) A UV layer is missing on the mesh'''
        return bool()
    @property
    def missing_materials(self):
        '''(Boolean) The mesh is missing materials'''
        return bool()
    @property
    def missing_stencil(self):
        '''(Boolean) Image Painting does not have a stencil'''
        return bool()
    @property
    def missing_texture(self):
        '''(Boolean) Image Painting does not have a texture to paint on'''
        return bool()
    def detect_data(self):
        '''Check if required texpaint data exist
        
        Returns:
          ok: (Boolean)'''
        return bool()