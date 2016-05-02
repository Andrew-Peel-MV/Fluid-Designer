from . imagepreview import ImagePreview
from . id import ID
from . animdata import AnimData
from . image import Image
from . colorramp import ColorRamp
from . nodetree import NodeTree
from . materialsubsurfacescattering import MaterialSubsurfaceScattering
from . materialgamesettings import MaterialGameSettings
from . materialhalo import MaterialHalo
from . materialvolume import MaterialVolume
from . materialraytracemirror import MaterialRaytraceMirror
from . cyclesmaterialsettings import CyclesMaterialSettings
from . material import Material
from . materialtextureslots import MaterialTextureSlots
from . materialphysics import MaterialPhysics
from . library import Library
from . texpaintslot import TexPaintSlot
from . materialraytracetransparency import MaterialRaytraceTransparency
from . materialstrand import MaterialStrand
from . texture import Texture
from . struct import Struct
from . group import Group
from . bpy_struct import bpy_struct
import mathutils

class Material(bpy_struct):
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
    def type(self):
        '''(Enum) Material type defining how the object is rendered
        
        [SURFACE, WIRE, VOLUME, HALO]'''
        return str()
    @property
    def use_transparency(self):
        '''(Boolean) Render material as transparent'''
        return bool()
    @property
    def transparency_method(self):
        '''(Enum) Method to use for rendering transparency
        
        [MASK, Z_TRANSPARENCY, RAYTRACE]'''
        return str()
    @property
    def preview_render_type(self):
        '''(Enum) Type of preview render
        
        [FLAT, SPHERE, CUBE, MONKEY, HAIR, SPHERE_A]'''
        return str()
    @property
    def ambient(self):
        '''(Float) Amount of global ambient color the material receives'''
        return float()
    @property
    def emit(self):
        '''(Float) Amount of light to emit'''
        return float()
    @property
    def translucency(self):
        '''(Float) Amount of diffuse shading on the back side'''
        return float()
    @property
    def use_cubic(self):
        '''(Boolean) Use cubic interpolation for diffuse values, for smoother
        transitions'''
        return bool()
    @property
    def use_object_color(self):
        '''(Boolean) Modulate the result with a per-object color'''
        return bool()
    @property
    def shadow_ray_bias(self):
        '''(Float) Shadow raytracing bias to prevent terminator problems on
        shadow boundary'''
        return float()
    @property
    def shadow_buffer_bias(self):
        '''(Float) Factor to multiply shadow buffer bias with (0 is ignore)'''
        return float()
    @property
    def shadow_cast_alpha(self):
        '''(Float) Shadow casting alpha, in use for Irregular and Deep shadow
        buffer'''
        return float()
    @property
    def light_group(self):
        '''(Group) Limit lighting to lamps in this Group'''
        return Group()
    @property
    def pass_index(self):
        '''(Integer) Index number for the IndexMA render pass'''
        return int()
    @property
    def use_light_group_exclusive(self):
        '''(Boolean) Material uses the light group exclusively - these lamps are
        excluded from other scene lighting'''
        return bool()
    @property
    def use_light_group_local(self):
        '''(Boolean) When linked in, material uses local light group with the
        same name'''
        return bool()
    @property
    def use_raytrace(self):
        '''(Boolean) Include this material and geometry that uses it in
        raytracing calculations'''
        return bool()
    @property
    def use_shadows(self):
        '''(Boolean) Allow this material to receive shadows'''
        return bool()
    @property
    def use_shadeless(self):
        '''(Boolean) Make this material insensitive to light or shadow'''
        return bool()
    @property
    def use_vertex_color_light(self):
        '''(Boolean) Add vertex colors as additional lighting'''
        return bool()
    @property
    def use_vertex_color_paint(self):
        '''(Boolean) Replace object base color with vertex colors (multiply with
        'texture face' face assigned textures)'''
        return bool()
    @property
    def invert_z(self):
        '''(Boolean) Render material's faces with an inverted Z buffer (scanline
        only)'''
        return bool()
    @property
    def offset_z(self):
        '''(Float) Give faces an artificial offset in the Z buffer for Z
        transparency'''
        return float()
    @property
    def use_sky(self):
        '''(Boolean) Render this material with zero alpha, with sky background in
        place (scanline only)'''
        return bool()
    @property
    def use_only_shadow(self):
        '''(Boolean) Render shadows as the material's alpha value, making the
        material transparent except for shadowed areas'''
        return bool()
    @property
    def shadow_only_type(self):
        '''(Enum) How to draw shadows
        
        [SHADOW_ONLY_OLD, SHADOW_ONLY, SHADOW_ONLY_SHADED]'''
        return str()
    @property
    def use_face_texture(self):
        '''(Boolean) Replace the object's base color with color from UV map image
        textures'''
        return bool()
    @property
    def use_face_texture_alpha(self):
        '''(Boolean) Replace the object's base alpha value with alpha from UV map
        image textures'''
        return bool()
    @property
    def use_cast_shadows(self):
        '''(Boolean) Allow this material to cast shadows'''
        return bool()
    @property
    def use_cast_shadows_only(self):
        '''(Boolean) Make objects with this material appear invisible (not
        rendered), only casting shadows'''
        return bool()
    @property
    def use_mist(self):
        '''(Boolean) Use mist with this material (in world settings)'''
        return bool()
    @property
    def use_transparent_shadows(self):
        '''(Boolean) Allow this object to receive transparent shadows cast
        through other objects'''
        return bool()
    @property
    def use_ray_shadow_bias(self):
        '''(Boolean) Prevent raytraced shadow errors on surfaces with smooth
        shaded normals (terminator problem)'''
        return bool()
    @property
    def use_full_oversampling(self):
        '''(Boolean) Force this material to render full shading/textures for all
        anti-aliasing samples'''
        return bool()
    @property
    def use_cast_buffer_shadows(self):
        '''(Boolean) Allow this material to cast shadows from shadow buffer lamps'''
        return bool()
    @property
    def use_cast_approximate(self):
        '''(Boolean) Allow this material to cast shadows when using approximate
        ambient occlusion'''
        return bool()
    @property
    def use_tangent_shading(self):
        '''(Boolean) Use the material's tangent vector instead of the normal for
        shading - for anisotropic shading effects'''
        return bool()
    @property
    def use_uv_project(self):
        '''(Boolean) Use to ensure UV interpolation is correct for camera
        projections (use with UV project modifier)'''
        return bool()
    @property
    def raytrace_mirror(self):
        '''(MaterialRaytraceMirror) Raytraced reflection settings for the
        material'''
        return MaterialRaytraceMirror()
    @property
    def raytrace_transparency(self):
        '''(MaterialRaytraceTransparency) Raytraced transparency settings for the
        material'''
        return MaterialRaytraceTransparency()
    @property
    def volume(self):
        '''(MaterialVolume) Volume settings for the material'''
        return MaterialVolume()
    @property
    def halo(self):
        '''(MaterialHalo) Halo settings for the material'''
        return MaterialHalo()
    @property
    def subsurface_scattering(self):
        '''(MaterialSubsurfaceScattering) Subsurface scattering settings for the
        material'''
        return MaterialSubsurfaceScattering()
    @property
    def strand(self):
        '''(MaterialStrand) Strand settings for the material'''
        return MaterialStrand()
    @property
    def physics(self):
        '''(MaterialPhysics) Game physics settings'''
        return MaterialPhysics()
    @property
    def game_settings(self):
        '''(MaterialGameSettings) Game material settings'''
        return MaterialGameSettings()
    @property
    def node_tree(self):
        '''(NodeTree) Node tree for node based materials'''
        return NodeTree()
    @property
    def use_nodes(self):
        '''(Boolean) Use shader nodes to render the material'''
        return bool()
    @property
    def active_node_material(self):
        '''(Material) Active node material'''
        return Material()
    @property
    def animation_data(self):
        '''(AnimData) Animation data for this datablock'''
        return AnimData()
    @property
    def texture_slots(self):
        '''(Sequence of MaterialTextureSlot) Texture slots defining the mapping
        and influence of textures'''
        return MaterialTextureSlots()
    @property
    def active_texture(self):
        '''(Texture) Active texture slot being displayed'''
        return Texture()
    @property
    def active_texture_index(self):
        '''(Integer) Index of active texture slot'''
        return int()
    @property
    def texture_paint_images(self):
        '''(Sequence of Image) Texture images used for texture painting'''
        return (Image(),)
    @property
    def texture_paint_slots(self):
        '''(Sequence of TexPaintSlot) Texture slots defining the mapping and
        influence of textures'''
        return (TexPaintSlot(),)
    @property
    def paint_active_slot(self):
        '''(Integer) Index of active texture paint slot'''
        return int()
    @property
    def paint_clone_slot(self):
        '''(Integer) Index of clone texture paint slot'''
        return int()
    @property
    def use_textures(self):
        '''(Boolean[18]) Enable/Disable each texture'''
        return bool()
    @property
    def diffuse_color(self):
        '''(Vector 3D) Diffuse color of the material'''
        return mathutils.Vector()
    @property
    def specular_color(self):
        '''(Vector 3D) Specular color of the material'''
        return mathutils.Vector()
    @property
    def mirror_color(self):
        '''(Vector 3D) Mirror color of the material'''
        return mathutils.Vector()
    @property
    def alpha(self):
        '''(Float) Alpha transparency of the material'''
        return float()
    @property
    def specular_alpha(self):
        '''(Float) Alpha transparency for specular areas'''
        return float()
    @property
    def use_diffuse_ramp(self):
        '''(Boolean) Toggle diffuse ramp operations'''
        return bool()
    @property
    def diffuse_ramp(self):
        '''(ColorRamp) Color ramp used to affect diffuse shading'''
        return ColorRamp()
    @property
    def use_specular_ramp(self):
        '''(Boolean) Toggle specular ramp operations'''
        return bool()
    @property
    def specular_ramp(self):
        '''(ColorRamp) Color ramp used to affect specular shading'''
        return ColorRamp()
    @property
    def diffuse_ramp_blend(self):
        '''(Enum) Blending method of the ramp and the diffuse color
        
        [MIX, ADD, MULTIPLY, SUBTRACT, SCREEN, DIVIDE, DIFFERENCE, DARKEN,
        LIGHTEN, OVERLAY, DODGE, BURN, HUE, SATURATION, VALUE, COLOR,
        SOFT_LIGHT, LINEAR_LIGHT]'''
        return str()
    @property
    def specular_ramp_blend(self):
        '''(Enum) Blending method of the ramp and the specular color
        
        [MIX, ADD, MULTIPLY, SUBTRACT, SCREEN, DIVIDE, DIFFERENCE, DARKEN,
        LIGHTEN, OVERLAY, DODGE, BURN, HUE, SATURATION, VALUE, COLOR,
        SOFT_LIGHT, LINEAR_LIGHT]'''
        return str()
    @property
    def diffuse_ramp_input(self):
        '''(Enum) How the ramp maps on the surface
        
        [SHADER, ENERGY, NORMAL, RESULT]'''
        return str()
    @property
    def specular_ramp_input(self):
        '''(Enum) How the ramp maps on the surface
        
        [SHADER, ENERGY, NORMAL, RESULT]'''
        return str()
    @property
    def diffuse_ramp_factor(self):
        '''(Float) Blending factor (also uses alpha in Colorband)'''
        return float()
    @property
    def specular_ramp_factor(self):
        '''(Float) Blending factor (also uses alpha in Colorband)'''
        return float()
    @property
    def line_color(self):
        '''(Float[4]) Line color used for Freestyle line rendering'''
        return ''
    @property
    def line_priority(self):
        '''(Integer) The line color of a higher priority is used at material
        boundaries'''
        return int()
    @property
    def diffuse_shader(self):
        '''(Enum)
        
        [LAMBERT, OREN_NAYAR, TOON, MINNAERT, FRESNEL]'''
        return str()
    @property
    def diffuse_intensity(self):
        '''(Float) Amount of diffuse reflection'''
        return float()
    @property
    def roughness(self):
        '''(Float) Oren-Nayar Roughness'''
        return float()
    @property
    def diffuse_toon_size(self):
        '''(Float) Size of diffuse toon area'''
        return float()
    @property
    def diffuse_toon_smooth(self):
        '''(Float) Smoothness of diffuse toon area'''
        return float()
    @property
    def diffuse_fresnel(self):
        '''(Float) Power of Fresnel'''
        return float()
    @property
    def diffuse_fresnel_factor(self):
        '''(Float) Blending factor of Fresnel'''
        return float()
    @property
    def darkness(self):
        '''(Float) Minnaert darkness'''
        return float()
    @property
    def specular_shader(self):
        '''(Enum)
        
        [COOKTORR, PHONG, BLINN, TOON, WARDISO]'''
        return str()
    @property
    def specular_intensity(self):
        '''(Float) How intense (bright) the specular reflection is'''
        return float()
    @property
    def specular_hardness(self):
        '''(Integer) How hard (sharp) the specular reflection is'''
        return int()
    @property
    def specular_ior(self):
        '''(Float) Specular index of refraction'''
        return float()
    @property
    def specular_toon_size(self):
        '''(Float) Size of specular toon area'''
        return float()
    @property
    def specular_toon_smooth(self):
        '''(Float) Smoothness of specular toon area'''
        return float()
    @property
    def specular_slope(self):
        '''(Float) The standard deviation of surface slope'''
        return float()
    @property
    def cycles(self):
        '''(CyclesMaterialSettings) Cycles material settings'''
        return CyclesMaterialSettings()
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