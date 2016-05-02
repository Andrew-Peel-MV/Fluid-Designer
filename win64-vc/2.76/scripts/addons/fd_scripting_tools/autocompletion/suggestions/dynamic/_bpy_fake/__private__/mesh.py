from . vertexcolors import VertexColors
from . polygonintproperties import PolygonIntProperties
from . tessfaceuvtextures import TessfaceUVTextures
from . imagepreview import ImagePreview
from . polygonstringproperties import PolygonStringProperties
from . id import ID
from . mesh import Mesh
from . meshuvlooplayer import MeshUVLoopLayer
from . vertexstringproperties import VertexStringProperties
from . vertexintproperties import VertexIntProperties
from . animdata import AnimData
from . key import Key
from . uvlooplayers import UVLoopLayers
from . meshedges import MeshEdges
from . loopcolors import LoopColors
from . cyclesmeshsettings import CyclesMeshSettings
from . meshpolygons import MeshPolygons
from . uvtextures import UVTextures
from . meshskinvertexlayer import MeshSkinVertexLayer
from . meshtessfaces import MeshTessFaces
from . library import Library
from . meshloops import MeshLoops
from . vertexfloatproperties import VertexFloatProperties
from . struct import Struct
from . polygonfloatproperties import PolygonFloatProperties
from . meshpaintmasklayer import MeshPaintMaskLayer
from . idmaterials import IDMaterials
from . meshtexturepolylayer import MeshTexturePolyLayer
from . meshvertices import MeshVertices
from . bpy_struct import bpy_struct
import mathutils

class Mesh(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique datablock ID name'''
        return str()
    @property
    def users(self):
        '''(Integer) Number of times this datablock is referenced'''
        return int()
    @property
    def use_fake_user(self):
        '''(Boolean) Save this datablock even if it has no users'''
        return bool()
    @property
    def tag(self):
        '''(Boolean) Tools can use this to tag data for their own purposes
        (initial state is undefined)'''
        return bool()
    @property
    def is_updated(self):
        '''(Boolean) Datablock is tagged for recalculation'''
        return bool()
    @property
    def is_updated_data(self):
        '''(Boolean) Datablock data is tagged for recalculation'''
        return bool()
    @property
    def is_library_indirect(self):
        '''(Boolean) Is this ID block linked indirectly'''
        return bool()
    @property
    def library(self):
        '''(Library) Library file the datablock is linked from'''
        return Library()
    @property
    def preview(self):
        '''(ImagePreview) Preview image and icon of this datablock (None if not
        supported for this type of data)'''
        return ImagePreview()
    @property
    def vertices(self):
        '''(Sequence of MeshVertex) Vertices of the mesh'''
        return MeshVertices()
    @property
    def edges(self):
        '''(Sequence of MeshEdge) Edges of the mesh'''
        return MeshEdges()
    @property
    def tessfaces(self):
        '''(Sequence of MeshTessFace) Tessellated faces of the mesh (derived from
        polygons)'''
        return MeshTessFaces()
    @property
    def loops(self):
        '''(Sequence of MeshLoop) Loops of the mesh (polygon corners)'''
        return MeshLoops()
    @property
    def polygons(self):
        '''(Sequence of MeshPolygon) Polygons of the mesh'''
        return MeshPolygons()
    @property
    def texture_mesh(self):
        '''(Mesh) Use another mesh for texture indices (vertex indices must be
        aligned)'''
        return Mesh()
    @property
    def uv_layers(self):
        '''(Sequence of MeshUVLoopLayer) All UV loop layers'''
        return UVLoopLayers()
    @property
    def uv_layer_clone(self):
        '''(MeshUVLoopLayer) UV loop layer to be used as cloning source'''
        return MeshUVLoopLayer()
    @property
    def uv_layer_clone_index(self):
        '''(Integer) Clone UV loop layer index'''
        return int()
    @property
    def uv_layer_stencil(self):
        '''(MeshUVLoopLayer) UV loop layer to mask the painted area'''
        return MeshUVLoopLayer()
    @property
    def uv_layer_stencil_index(self):
        '''(Integer) Mask UV loop layer index'''
        return int()
    @property
    def tessface_uv_textures(self):
        '''(Sequence of MeshTextureFaceLayer) All UV maps for tessellated faces
        (read-only, for use by renderers)'''
        return TessfaceUVTextures()
    @property
    def uv_textures(self):
        '''(Sequence of MeshTexturePolyLayer) All UV maps'''
        return UVTextures()
    @property
    def uv_texture_clone(self):
        '''(MeshTexturePolyLayer) UV map to be used as cloning source'''
        return MeshTexturePolyLayer()
    @property
    def uv_texture_clone_index(self):
        '''(Integer) Clone UV map index'''
        return int()
    @property
    def uv_texture_stencil(self):
        '''(MeshTexturePolyLayer) UV map to mask the painted area'''
        return MeshTexturePolyLayer()
    @property
    def uv_texture_stencil_index(self):
        '''(Integer) Mask UV map index'''
        return int()
    @property
    def tessface_vertex_colors(self):
        '''(Sequence of MeshColorLayer) All tessellated face colors (read-only,
        for use by renderers)'''
        return VertexColors()
    @property
    def vertex_colors(self):
        '''(Sequence of MeshLoopColorLayer) All vertex colors'''
        return LoopColors()
    @property
    def vertex_layers_float(self):
        '''(Sequence of MeshVertexFloatPropertyLayer)'''
        return VertexFloatProperties()
    @property
    def vertex_layers_int(self):
        '''(Sequence of MeshVertexIntPropertyLayer)'''
        return VertexIntProperties()
    @property
    def vertex_layers_string(self):
        '''(Sequence of MeshVertexStringPropertyLayer)'''
        return VertexStringProperties()
    @property
    def polygon_layers_float(self):
        '''(Sequence of MeshPolygonFloatPropertyLayer)'''
        return PolygonFloatProperties()
    @property
    def polygon_layers_int(self):
        '''(Sequence of MeshPolygonIntPropertyLayer)'''
        return PolygonIntProperties()
    @property
    def polygon_layers_string(self):
        '''(Sequence of MeshPolygonStringPropertyLayer)'''
        return PolygonStringProperties()
    @property
    def skin_vertices(self):
        '''(Sequence of MeshSkinVertexLayer) All skin vertices'''
        return (MeshSkinVertexLayer(),)
    @property
    def vertex_paint_masks(self):
        '''(Sequence of MeshPaintMaskLayer) Vertex paint mask'''
        return (MeshPaintMaskLayer(),)
    @property
    def use_auto_smooth(self):
        '''(Boolean) Auto smooth (based on smooth/sharp faces/edges and angle
        between faces), or use custom split normals data if available'''
        return bool()
    @property
    def auto_smooth_angle(self):
        '''(Float) Maximum angle between face normals that will be considered as
        smooth (unused if custom split normals data are available)'''
        return float()
    @property
    def has_custom_normals(self):
        '''(Boolean) True if there are custom split normals data in this mesh'''
        return bool()
    @property
    def show_double_sided(self):
        '''(Boolean) Display the mesh with double or single sided lighting
        (OpenGL only)'''
        return bool()
    @property
    def texco_mesh(self):
        '''(Mesh) Derive texture coordinates from another mesh'''
        return Mesh()
    @property
    def shape_keys(self):
        '''(Key)'''
        return Key()
    @property
    def use_auto_texspace(self):
        '''(Boolean) Adjust active object's texture space automatically when
        transforming object'''
        return bool()
    @property
    def show_edges(self):
        '''(Boolean) Display selected edges using highlights in the 3D view and
        UV editor'''
        return bool()
    @property
    def show_faces(self):
        '''(Boolean) Display all faces as shades in the 3D view and UV editor'''
        return bool()
    @property
    def show_normal_face(self):
        '''(Boolean) Display face normals as lines'''
        return bool()
    @property
    def show_normal_loop(self):
        '''(Boolean) Display vertex-per-face normals as lines'''
        return bool()
    @property
    def show_normal_vertex(self):
        '''(Boolean) Display vertex normals as lines'''
        return bool()
    @property
    def show_weight(self):
        '''(Boolean) Draw weights in editmode'''
        return bool()
    @property
    def show_edge_crease(self):
        '''(Boolean) Display creases created for subsurf weighting'''
        return bool()
    @property
    def show_edge_bevel_weight(self):
        '''(Boolean) Display weights created for the Bevel modifier'''
        return bool()
    @property
    def show_edge_seams(self):
        '''(Boolean) Display UV unwrapping seams'''
        return bool()
    @property
    def show_edge_sharp(self):
        '''(Boolean) Display sharp edges, used with the EdgeSplit modifier'''
        return bool()
    @property
    def show_freestyle_edge_marks(self):
        '''(Boolean) Display Freestyle edge marks, used with the Freestyle
        renderer'''
        return bool()
    @property
    def show_freestyle_face_marks(self):
        '''(Boolean) Display Freestyle face marks, used with the Freestyle
        renderer'''
        return bool()
    @property
    def show_statvis(self):
        '''(Boolean) Display statistical information about the mesh'''
        return bool()
    @property
    def show_extra_edge_length(self):
        '''(Boolean) Display selected edge lengths, using global values when set
        in the transform panel'''
        return bool()
    @property
    def show_extra_edge_angle(self):
        '''(Boolean) Display selected edge angle, using global values when set in
        the transform panel'''
        return bool()
    @property
    def show_extra_face_angle(self):
        '''(Boolean) Display the angles in the selected edges, using global
        values when set in the transform panel'''
        return bool()
    @property
    def show_extra_face_area(self):
        '''(Boolean) Display the area of selected faces, using global values when
        set in the transform panel'''
        return bool()
    @property
    def show_extra_indices(self):
        '''(Boolean) Display the index numbers of selected vertices, edges, and
        faces'''
        return bool()
    @property
    def use_mirror_x(self):
        '''(Boolean) X Axis mirror editing'''
        return bool()
    @property
    def use_mirror_topology(self):
        '''(Boolean) Use topology based mirroring (for when both sides of mesh
        have matching, unique topology)'''
        return bool()
    @property
    def use_paint_mask(self):
        '''(Boolean) Face selection masking for painting'''
        return bool()
    @property
    def use_paint_mask_vertex(self):
        '''(Boolean) Vertex selection masking for painting (weight paint only)'''
        return bool()
    @property
    def use_customdata_vertex_bevel(self):
        '''(Boolean)'''
        return bool()
    @property
    def use_customdata_edge_bevel(self):
        '''(Boolean)'''
        return bool()
    @property
    def use_customdata_edge_crease(self):
        '''(Boolean)'''
        return bool()
    @property
    def total_vert_sel(self):
        '''(Integer) Selected vertex count in editmode'''
        return int()
    @property
    def total_edge_sel(self):
        '''(Integer) Selected edge count in editmode'''
        return int()
    @property
    def total_face_sel(self):
        '''(Integer) Selected face count in editmode'''
        return int()
    @property
    def is_editmode(self):
        '''(Boolean) True when used in editmode'''
        return bool()
    @property
    def animation_data(self):
        '''(AnimData) Animation data for this datablock'''
        return AnimData()
    @property
    def auto_texspace(self):
        '''(Boolean) Adjust active object's texture space automatically when
        transforming object'''
        return bool()
    @property
    def texspace_location(self):
        '''(Vector 3D) Texture space location'''
        return mathutils.Vector()
    @property
    def texspace_size(self):
        '''(Vector 3D) Texture space size'''
        return mathutils.Vector()
    @property
    def materials(self):
        '''(Sequence of Material)'''
        return IDMaterials()
    @property
    def cycles(self):
        '''(CyclesMeshSettings) Cycles mesh settings'''
        return CyclesMeshSettings()
    def copy(self):
        '''Create a copy of this datablock (not supported for all datablocks)
        
        Returns:
          id: (ID) New copy of the ID'''
        return ID()
    def user_clear(self):
        '''Clear the user count of a datablock so its not saved, on reload the
        data will be removed'''
        return 
    def animation_data_create(self):
        '''Create animation data to this ID, note that not all ID types support
        this
        
        Returns:
          anim_data: (AnimData) New animation data or NULL'''
        return AnimData()
    def animation_data_clear(self):
        '''Clear animation on this this ID'''
        return 
    def update_tag(self, refresh):
        '''Tag the ID to update its display data, e.g. when calling
        :class:`bpy.types.Scene.update`
        
        Parameter:
          refresh: (Enum) Type of updates to perform'''
        return 
    def transform(self, matrix, shape_keys):
        '''Transform mesh vertices by a matrix
        
        Parameter:
          matrix: (Matrix) Matrix
          shape_keys: (Boolean) Transform Shape Keys'''
        return 
    def calc_normals(self):
        '''Calculate vertex normals'''
        return 
    def create_normals_split(self):
        '''Empty split vertex normals'''
        return 
    def calc_normals_split(self):
        '''Calculate split vertex normals, which preserve sharp edges'''
        return 
    def free_normals_split(self):
        '''Free split vertex normals'''
        return 
    def calc_tangents(self, uvmap):
        '''Compute tangents and bitangent signs, to be used together with the
        split normals to get a complete tangent space for normal mapping
        (split normals are also computed if not yet present)
        
        Parameter:
          uvmap: (String) Name of the UV map to use for tangent space computation'''
        return 
    def free_tangents(self):
        '''Free tangents'''
        return 
    def calc_tessface(self, free_mpoly):
        '''Calculate face tessellation (supports editmode too)
        
        Parameter:
          free_mpoly:
            (Boolean) Free data used by polygons and loops. WARNING: This
            destructive operation removes regular faces, only used on temporary
            mesh data-blocks to reduce memory footprint of render engines and
            export scripts'''
        return 
    def calc_smooth_groups(self, use_bitflags):
        '''Calculate smooth groups from sharp edges
        
        Parameter:
          use_bitflags: (Boolean) Produce bitflags groups instead of simple numeric values
        
        Returns:
          poly_groups: (Integer) Smooth Groups
          groups: (Integer) Total number of groups'''
        return int(), int()
    def normals_split_custom_set(self, normals):
        '''Define custom split normals of this mesh (use zero-vectors to keep
        auto ones)
        
        Parameter:
          normals: (Vector 3D) Normals'''
        return 
    def normals_split_custom_set_from_vertices(self, normals):
        '''Define custom split normals of this mesh, from vertices' normals (use
        zero-vectors to keep auto ones)
        
        Parameter:
          normals: (Vector 3D) Normals'''
        return 
    def update(self, calc_edges, calc_tessface):
        '''update
        
        Parameter:
          calc_edges: (Boolean) Force recalculation of edges
          calc_tessface: (Boolean) Force recalculation of tessellation faces'''
        return 
    def unit_test_compare(self, mesh):
        '''unit_test_compare
        
        Parameter:
          mesh: (Mesh) Mesh to compare to
        
        Returns:
          result: (String) String description of result of comparison'''
        return str()
    def validate(self, verbose, clean_customdata):
        '''Validate geometry, return True when the mesh has had invalid geometry
        corrected/removed
        
        Parameter:
          verbose: (Boolean) Output information about the errors found
          clean_customdata: (Boolean) Remove temp/cached custom-data layers, like e.g. normals...
        
        Returns:
          result: (Boolean)'''
        return bool()
    def validate_material_indices(self):
        '''Validate material indices of polygons, return True when the mesh has
        had invalid indices corrected (to default 0)
        
        Returns:
          result: (Boolean)'''
        return bool()