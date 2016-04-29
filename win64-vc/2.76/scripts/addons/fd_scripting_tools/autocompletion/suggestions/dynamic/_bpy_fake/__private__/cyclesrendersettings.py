from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class CyclesRenderSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def device(self):
        '''(Enum) Device to use for rendering
        
        [CPU, GPU]'''
        return str()
    @property
    def feature_set(self):
        '''(Enum) Feature set to use for rendering
        
        [SUPPORTED, EXPERIMENTAL]'''
        return str()
    @property
    def shading_system(self):
        '''(Boolean) Use Open Shading Language (CPU rendering only)'''
        return bool()
    @property
    def progressive(self):
        '''(Enum) Method to sample lights and materials
        
        [BRANCHED_PATH, PATH]'''
        return str()
    @property
    def use_square_samples(self):
        '''(Boolean) Square sampling values for easier artist control'''
        return bool()
    @property
    def samples(self):
        '''(Integer) Number of samples to render for each pixel'''
        return int()
    @property
    def preview_samples(self):
        '''(Integer) Number of samples to render in the viewport, unlimited if 0'''
        return int()
    @property
    def preview_pause(self):
        '''(Boolean) Pause all viewport preview renders'''
        return bool()
    @property
    def preview_active_layer(self):
        '''(Boolean) Preview active render layer in viewport'''
        return bool()
    @property
    def aa_samples(self):
        '''(Integer) Number of antialiasing samples to render for each pixel'''
        return int()
    @property
    def preview_aa_samples(self):
        '''(Integer) Number of antialiasing samples to render in the viewport,
        unlimited if 0'''
        return int()
    @property
    def diffuse_samples(self):
        '''(Integer) Number of diffuse bounce samples to render for each AA
        sample'''
        return int()
    @property
    def glossy_samples(self):
        '''(Integer) Number of glossy bounce samples to render for each AA sample'''
        return int()
    @property
    def transmission_samples(self):
        '''(Integer) Number of transmission bounce samples to render for each AA
        sample'''
        return int()
    @property
    def ao_samples(self):
        '''(Integer) Number of ambient occlusion samples to render for each AA
        sample'''
        return int()
    @property
    def mesh_light_samples(self):
        '''(Integer) Number of mesh emission light samples to render for each AA
        sample'''
        return int()
    @property
    def subsurface_samples(self):
        '''(Integer) Number of subsurface scattering samples to render for each
        AA sample'''
        return int()
    @property
    def volume_samples(self):
        '''(Integer) Number of volume scattering samples to render for each AA
        sample'''
        return int()
    @property
    def sampling_pattern(self):
        '''(Enum) Random sampling pattern used by the integrator
        
        [SOBOL, CORRELATED_MUTI_JITTER]'''
        return str()
    @property
    def use_layer_samples(self):
        '''(Enum) How to use per render layer sample settings
        
        [USE, BOUNDED, IGNORE]'''
        return str()
    @property
    def sample_all_lights_direct(self):
        '''(Boolean) Sample all lights (for direct samples), rather than randomly
        picking one'''
        return bool()
    @property
    def sample_all_lights_indirect(self):
        '''(Boolean) Sample all lights (for indirect samples), rather than
        randomly picking one'''
        return bool()
    @property
    def caustics_reflective(self):
        '''(Boolean) Use reflective caustics, resulting in a brighter image (more
        noise but added realism)'''
        return bool()
    @property
    def caustics_refractive(self):
        '''(Boolean) Use refractive caustics, resulting in a brighter image (more
        noise but added realism)'''
        return bool()
    @property
    def blur_glossy(self):
        '''(Float) Adaptively blur glossy shaders after blurry bounces, to reduce
        noise at the cost of accuracy'''
        return float()
    @property
    def min_bounces(self):
        '''(Integer) Minimum number of bounces, setting this lower than the
        maximum enables probabilistic path termination (faster but noisier)'''
        return int()
    @property
    def max_bounces(self):
        '''(Integer) Total maximum number of bounces'''
        return int()
    @property
    def diffuse_bounces(self):
        '''(Integer) Maximum number of diffuse reflection bounces, bounded by
        total maximum'''
        return int()
    @property
    def glossy_bounces(self):
        '''(Integer) Maximum number of glossy reflection bounces, bounded by
        total maximum'''
        return int()
    @property
    def transmission_bounces(self):
        '''(Integer) Maximum number of transmission bounces, bounded by total
        maximum'''
        return int()
    @property
    def volume_bounces(self):
        '''(Integer) Maximum number of volumetric scattering events'''
        return int()
    @property
    def transparent_min_bounces(self):
        '''(Integer) Minimum number of transparent bounces, setting this lower
        than the maximum enables probabilistic path termination (faster but
        noisier)'''
        return int()
    @property
    def transparent_max_bounces(self):
        '''(Integer) Maximum number of transparent bounces'''
        return int()
    @property
    def use_transparent_shadows(self):
        '''(Boolean) Use transparency of surfaces for rendering shadows'''
        return bool()
    @property
    def volume_step_size(self):
        '''(Float) Distance between volume shader samples when rendering the
        volume (lower values give more accurate and detailed results, but also
        increased render time)'''
        return float()
    @property
    def volume_max_steps(self):
        '''(Integer) Maximum number of steps through the volume before giving up,
        to avoid extremely long render times with big objects or small step
        sizes'''
        return int()
    @property
    def film_exposure(self):
        '''(Float) Image brightness scale'''
        return float()
    @property
    def film_transparent(self):
        '''(Boolean) World background is transparent with premultiplied alpha'''
        return bool()
    @property
    def filter_type(self):
        '''(Enum) Pixel filter type
        
        [BOX, GAUSSIAN]'''
        return str()
    @property
    def filter_width(self):
        '''(Float) Pixel filter width'''
        return float()
    @property
    def seed(self):
        '''(Integer) Seed value for integrator to get different noise patterns'''
        return int()
    @property
    def use_animated_seed(self):
        '''(Boolean) Use different seed values (and hence noise patterns) at
        different frames'''
        return bool()
    @property
    def sample_clamp_direct(self):
        '''(Float) If non-zero, the maximum value for a direct sample, higher
        values will be scaled down to avoid too much noise and slow
        convergence at the cost of accuracy'''
        return float()
    @property
    def sample_clamp_indirect(self):
        '''(Float) If non-zero, the maximum value for an indirect sample, higher
        values will be scaled down to avoid too much noise and slow
        convergence at the cost of accuracy'''
        return float()
    @property
    def debug_tile_size(self):
        '''(Integer)'''
        return int()
    @property
    def preview_start_resolution(self):
        '''(Integer) Resolution to start rendering preview at, progressively
        increasing it to the full viewport size'''
        return int()
    @property
    def debug_reset_timeout(self):
        '''(Float)'''
        return float()
    @property
    def debug_cancel_timeout(self):
        '''(Float)'''
        return float()
    @property
    def debug_text_timeout(self):
        '''(Float)'''
        return float()
    @property
    def debug_bvh_type(self):
        '''(Enum) Choose between faster updates, or faster render
        
        [DYNAMIC_BVH, STATIC_BVH]'''
        return str()
    @property
    def debug_use_spatial_splits(self):
        '''(Boolean) Use BVH spatial splits: longer builder time, faster render'''
        return bool()
    @property
    def use_cache(self):
        '''(Boolean) Cache last built BVH to disk for faster re-render if no
        geometry changed'''
        return bool()
    @property
    def tile_order(self):
        '''(Enum) Tile order for rendering
        
        [CENTER, RIGHT_TO_LEFT, LEFT_TO_RIGHT, TOP_TO_BOTTOM, BOTTOM_TO_TOP]'''
        return str()
    @property
    def use_progressive_refine(self):
        '''(Boolean) Instead of rendering each tile until it is finished, refine
        the whole image progressively (this renders somewhat slower, but time
        can be saved by manually stopping the render when the noise is low
        enough)'''
        return bool()
    @property
    def bake_type(self):
        '''(Enum) Type of pass to bake
        
        [COMBINED, AO, SHADOW, NORMAL, UV, EMIT, ENVIRONMENT, DIFFUSE_DIRECT,
        DIFFUSE_INDIRECT, DIFFUSE_COLOR, GLOSSY_DIRECT, GLOSSY_INDIRECT,
        GLOSSY_COLOR, TRANSMISSION_DIRECT, TRANSMISSION_INDIRECT,
        TRANSMISSION_COLOR, SUBSURFACE_DIRECT, SUBSURFACE_INDIRECT,
        SUBSURFACE_COLOR]'''
        return str()
    @property
    def use_camera_cull(self):
        '''(Boolean) Allow objects to be culled based on the camera frustum'''
        return bool()
    @property
    def camera_cull_margin(self):
        '''(Float) Margin for the camera space culling'''
        return float()