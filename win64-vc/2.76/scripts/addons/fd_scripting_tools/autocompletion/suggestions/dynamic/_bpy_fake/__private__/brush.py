from . paintcurve import PaintCurve
from . texture import Texture
from . brushcapabilities import BrushCapabilities
from . imagepreview import ImagePreview
from . curvemapping import CurveMapping
from . brushtextureslot import BrushTextureSlot
from . struct import Struct
from . sculpttoolcapabilities import SculptToolCapabilities
from . id import ID
from . library import Library
from . image import Image
from . animdata import AnimData
from . colorramp import ColorRamp
from . imapainttoolcapabilities import ImapaintToolCapabilities
from . bpy_struct import bpy_struct
import mathutils

class Brush(bpy_struct):
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
    def blend(self):
        '''(Enum) Brush blending mode
        
        [MIX, ADD, SUB, MUL, LIGHTEN, DARKEN, ERASE_ALPHA, ADD_ALPHA, OVERLAY,
        HARDLIGHT, COLORBURN, LINEARBURN, COLORDODGE, SCREEN, SOFTLIGHT,
        PINLIGHT, VIVIDLIGHT, LINEARLIGHT, DIFFERENCE, EXCLUSION, HUE,
        SATURATION, LUMINOSITY, COLOR]'''
        return str()
    @property
    def sculpt_tool(self):
        '''(Enum)
        
        [BLOB, CLAY, CLAY_STRIPS, CREASE, DRAW, FILL, FLATTEN, GRAB, INFLATE,
        LAYER, MASK, NUDGE, PINCH, ROTATE, SCRAPE, SIMPLIFY, SMOOTH,
        SNAKE_HOOK, THUMB]'''
        return str()
    @property
    def vertex_tool(self):
        '''(Enum) Brush blending mode
        
        [MIX, ADD, SUB, MUL, BLUR, LIGHTEN, DARKEN]'''
        return str()
    @property
    def image_tool(self):
        '''(Enum)
        
        [DRAW, SOFTEN, SMEAR, CLONE, FILL, MASK]'''
        return str()
    @property
    def direction(self):
        '''(Enum)
        
        [ADD, SUBTRACT]'''
        return str()
    @property
    def stroke_method(self):
        '''(Enum)
        
        [DOTS, DRAG_DOT, SPACE, AIRBRUSH, ANCHORED, LINE, CURVE]'''
        return str()
    @property
    def sculpt_plane(self):
        '''(Enum)
        
        [AREA, VIEW, X, Y, Z]'''
        return str()
    @property
    def mask_tool(self):
        '''(Enum)
        
        [DRAW, SMOOTH]'''
        return str()
    @property
    def size(self):
        '''(Integer) Radius of the brush in pixels'''
        return int()
    @property
    def unprojected_radius(self):
        '''(Float) Radius of brush in Blender units'''
        return float()
    @property
    def jitter(self):
        '''(Float) Jitter the position of the brush while painting'''
        return float()
    @property
    def jitter_absolute(self):
        '''(Integer) Jitter the position of the brush in pixels while painting'''
        return int()
    @property
    def spacing(self):
        '''(Integer) Spacing between brush daubs as a percentage of brush
        diameter'''
        return int()
    @property
    def grad_spacing(self):
        '''(Integer) Spacing before brush gradient goes full circle'''
        return int()
    @property
    def smooth_stroke_radius(self):
        '''(Integer) Minimum distance from last point before stroke continues'''
        return int()
    @property
    def smooth_stroke_factor(self):
        '''(Float) Higher values give a smoother stroke'''
        return float()
    @property
    def rate(self):
        '''(Float) Interval between paints for Airbrush'''
        return float()
    @property
    def color(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def secondary_color(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def weight(self):
        '''(Float) Vertex weight when brush is applied'''
        return float()
    @property
    def strength(self):
        '''(Float) How powerful the effect of the brush is when applied'''
        return float()
    @property
    def plane_offset(self):
        '''(Float) Adjust plane on which the brush acts towards or away from the
        object surface'''
        return float()
    @property
    def plane_trim(self):
        '''(Float) If a vertex is further away from offset plane than this, then
        it is not affected'''
        return float()
    @property
    def height(self):
        '''(Float) Affectable height of brush (layer height for layer tool, i.e.)'''
        return float()
    @property
    def texture_sample_bias(self):
        '''(Float) Value added to texture samples'''
        return float()
    @property
    def normal_weight(self):
        '''(Float) How much grab will pull vertexes out of surface during a grab'''
        return float()
    @property
    def crease_pinch_factor(self):
        '''(Float) How much the crease brush pinches'''
        return float()
    @property
    def auto_smooth_factor(self):
        '''(Float) Amount of smoothing to automatically apply to each stroke'''
        return float()
    @property
    def stencil_pos(self):
        '''(Vector 2D) Position of stencil in viewport'''
        return mathutils.Vector()
    @property
    def stencil_dimension(self):
        '''(Vector 2D) Dimensions of stencil in viewport'''
        return mathutils.Vector()
    @property
    def mask_stencil_pos(self):
        '''(Vector 2D) Position of mask stencil in viewport'''
        return mathutils.Vector()
    @property
    def mask_stencil_dimension(self):
        '''(Vector 2D) Dimensions of mask stencil in viewport'''
        return mathutils.Vector()
    @property
    def sharp_threshold(self):
        '''(Float) Threshold below which, no sharpening is done'''
        return float()
    @property
    def fill_threshold(self):
        '''(Float) Threshold above which filling is not propagated'''
        return float()
    @property
    def blur_kernel_radius(self):
        '''(Integer) Radius of kernel used for soften and sharpen in pixels'''
        return int()
    @property
    def blur_mode(self):
        '''(Enum)
        
        [BOX, GAUSSIAN]'''
        return str()
    @property
    def use_airbrush(self):
        '''(Boolean) Keep applying paint effect while holding mouse (spray)'''
        return bool()
    @property
    def use_original_normal(self):
        '''(Boolean) When locked keep using normal of surface where stroke was
        initiated'''
        return bool()
    @property
    def use_pressure_strength(self):
        '''(Boolean) Enable tablet pressure sensitivity for strength'''
        return bool()
    @property
    def use_offset_pressure(self):
        '''(Boolean) Enable tablet pressure sensitivity for offset'''
        return bool()
    @property
    def use_pressure_size(self):
        '''(Boolean) Enable tablet pressure sensitivity for size'''
        return bool()
    @property
    def use_gradient(self):
        '''(Boolean) Use Gradient by utilizing a sampling method'''
        return bool()
    @property
    def use_pressure_jitter(self):
        '''(Boolean) Enable tablet pressure sensitivity for jitter'''
        return bool()
    @property
    def use_pressure_spacing(self):
        '''(Boolean) Enable tablet pressure sensitivity for spacing'''
        return bool()
    @property
    def use_pressure_masking(self):
        '''(Enum) Pen pressure makes texture influence smaller
        
        [NONE, RAMP, CUTOFF]'''
        return str()
    @property
    def use_inverse_smooth_pressure(self):
        '''(Boolean) Lighter pressure causes more smoothing to be applied'''
        return bool()
    @property
    def use_relative_jitter(self):
        '''(Boolean) Jittering happens in screen space, not relative to brush
        size'''
        return bool()
    @property
    def use_plane_trim(self):
        '''(Boolean) Enable Plane Trim'''
        return bool()
    @property
    def use_frontface(self):
        '''(Boolean) Brush only affects vertexes that face the viewer'''
        return bool()
    @property
    def use_anchor(self):
        '''(Boolean) Keep the brush anchored to the initial location'''
        return bool()
    @property
    def use_space(self):
        '''(Boolean) Limit brush application to the distance specified by spacing'''
        return bool()
    @property
    def use_line(self):
        '''(Boolean) Draw a line with dabs separated according to spacing'''
        return bool()
    @property
    def use_curve(self):
        '''(Boolean) Define the stroke curve with a bezier curve. Dabs are
        separated according to spacing'''
        return bool()
    @property
    def use_smooth_stroke(self):
        '''(Boolean) Brush lags behind mouse and follows a smoother path'''
        return bool()
    @property
    def use_persistent(self):
        '''(Boolean) Sculpt on a persistent layer of the mesh'''
        return bool()
    @property
    def use_accumulate(self):
        '''(Boolean) Accumulate stroke daubs on top of each other'''
        return bool()
    @property
    def use_space_attenuation(self):
        '''(Boolean) Automatically adjust strength to give consistent results for
        different spacings'''
        return bool()
    @property
    def use_adaptive_space(self):
        '''(Boolean) Space daubs according to surface orientation instead of
        screen space'''
        return bool()
    @property
    def use_locked_size(self):
        '''(Boolean) When locked brush stays same size relative to object; when
        unlocked brush size is given in pixels'''
        return bool()
    @property
    def use_edge_to_edge(self):
        '''(Boolean) Drag anchor brush from edge-to-edge'''
        return bool()
    @property
    def use_restore_mesh(self):
        '''(Boolean) Allow a single dot to be carefully positioned'''
        return bool()
    @property
    def use_alpha(self):
        '''(Boolean) When this is disabled, lock alpha while painting'''
        return bool()
    @property
    def curve(self):
        '''(CurveMapping) Editable falloff curve'''
        return CurveMapping()
    @property
    def paint_curve(self):
        '''(PaintCurve) Active Paint Curve'''
        return PaintCurve()
    @property
    def gradient(self):
        '''(ColorRamp)'''
        return ColorRamp()
    @property
    def gradient_stroke_mode(self):
        '''(Enum)
        
        [PRESSURE, SPACING_REPEAT, SPACING_CLAMP]'''
        return str()
    @property
    def gradient_fill_mode(self):
        '''(Enum)
        
        [LINEAR, RADIAL]'''
        return str()
    @property
    def use_primary_overlay(self):
        '''(Boolean) Show texture in viewport'''
        return bool()
    @property
    def use_secondary_overlay(self):
        '''(Boolean) Show texture in viewport'''
        return bool()
    @property
    def use_cursor_overlay(self):
        '''(Boolean) Show cursor in viewport'''
        return bool()
    @property
    def use_cursor_overlay_override(self):
        '''(Boolean) Don't show overlay during a stroke'''
        return bool()
    @property
    def use_primary_overlay_override(self):
        '''(Boolean) Don't show overlay during a stroke'''
        return bool()
    @property
    def use_secondary_overlay_override(self):
        '''(Boolean) Don't show overlay during a stroke'''
        return bool()
    @property
    def use_paint_sculpt(self):
        '''(Boolean) Use this brush in sculpt mode'''
        return bool()
    @property
    def use_paint_vertex(self):
        '''(Boolean) Use this brush in vertex paint mode'''
        return bool()
    @property
    def use_paint_weight(self):
        '''(Boolean) Use this brush in weight paint mode'''
        return bool()
    @property
    def use_paint_image(self):
        '''(Boolean) Use this brush in texture paint mode'''
        return bool()
    @property
    def texture_slot(self):
        '''(BrushTextureSlot)'''
        return BrushTextureSlot()
    @property
    def texture(self):
        '''(Texture)'''
        return Texture()
    @property
    def mask_texture_slot(self):
        '''(BrushTextureSlot)'''
        return BrushTextureSlot()
    @property
    def mask_texture(self):
        '''(Texture)'''
        return Texture()
    @property
    def texture_overlay_alpha(self):
        '''(Integer)'''
        return int()
    @property
    def mask_overlay_alpha(self):
        '''(Integer)'''
        return int()
    @property
    def cursor_overlay_alpha(self):
        '''(Integer)'''
        return int()
    @property
    def cursor_color_add(self):
        '''(Vector 3D) Color of cursor when adding'''
        return mathutils.Vector()
    @property
    def cursor_color_subtract(self):
        '''(Vector 3D) Color of cursor when subtracting'''
        return mathutils.Vector()
    @property
    def use_custom_icon(self):
        '''(Boolean) Set the brush icon from an image file'''
        return bool()
    @property
    def icon_filepath(self):
        '''(String) File path to brush icon'''
        return str()
    @property
    def clone_image(self):
        '''(Image) Image for clone tool'''
        return Image()
    @property
    def clone_alpha(self):
        '''(Float) Opacity of clone image display'''
        return float()
    @property
    def clone_offset(self):
        '''(Vector 2D)'''
        return mathutils.Vector()
    @property
    def brush_capabilities(self):
        '''(BrushCapabilities) Brush's capabilities'''
        return BrushCapabilities()
    @property
    def sculpt_capabilities(self):
        '''(SculptToolCapabilities) Brush's capabilities in sculpt mode'''
        return SculptToolCapabilities()
    @property
    def image_paint_capabilities(self):
        '''(ImapaintToolCapabilities) Brush's capabilities in image paint mode'''
        return ImapaintToolCapabilities()
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