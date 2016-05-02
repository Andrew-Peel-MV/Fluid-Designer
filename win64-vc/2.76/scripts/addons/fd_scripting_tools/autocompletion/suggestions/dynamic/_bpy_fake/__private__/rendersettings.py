from . renderlayers import RenderLayers
from . struct import Struct
from . bakesettings import BakeSettings
from . imageformatsettings import ImageFormatSettings
from . scenerenderview import SceneRenderView
from . renderviews import RenderViews
from . ffmpegsettings import FFmpegSettings
from . bpy_struct import bpy_struct
import mathutils

class RenderSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def image_settings(self):
        '''(ImageFormatSettings)'''
        return ImageFormatSettings()
    @property
    def resolution_x(self):
        '''(Integer) Number of horizontal pixels in the rendered image'''
        return int()
    @property
    def resolution_y(self):
        '''(Integer) Number of vertical pixels in the rendered image'''
        return int()
    @property
    def resolution_percentage(self):
        '''(Integer) Percentage scale for render resolution'''
        return int()
    @property
    def tile_x(self):
        '''(Integer) Horizontal tile size to use while rendering'''
        return int()
    @property
    def tile_y(self):
        '''(Integer) Vertical tile size to use while rendering'''
        return int()
    @property
    def preview_start_resolution(self):
        '''(Integer) Resolution to start rendering preview at, progressively
        increasing it to the full viewport size'''
        return int()
    @property
    def pixel_aspect_x(self):
        '''(Float) Horizontal aspect ratio - for anamorphic or non-square pixel
        output'''
        return float()
    @property
    def pixel_aspect_y(self):
        '''(Float) Vertical aspect ratio - for anamorphic or non-square pixel
        output'''
        return float()
    @property
    def ffmpeg(self):
        '''(FFmpegSettings) FFmpeg related settings for the scene'''
        return FFmpegSettings()
    @property
    def fps(self):
        '''(Integer) Framerate, expressed in frames per second'''
        return int()
    @property
    def fps_base(self):
        '''(Float) Framerate base'''
        return float()
    @property
    def frame_map_old(self):
        '''(Integer) Old mapping value in frames'''
        return int()
    @property
    def frame_map_new(self):
        '''(Integer) How many frames the Map Old will last'''
        return int()
    @property
    def dither_intensity(self):
        '''(Float) Amount of dithering noise added to the rendered image to break
        up banding'''
        return float()
    @property
    def pixel_filter_type(self):
        '''(Enum) Reconstruction filter used for combining anti-aliasing samples
        
        [BOX, TENT, QUADRATIC, CUBIC, CATMULLROM, GAUSSIAN, MITCHELL]'''
        return str()
    @property
    def filter_size(self):
        '''(Float) Width over which the reconstruction filter combines samples'''
        return float()
    @property
    def alpha_mode(self):
        '''(Enum) Representation of alpha information in the RGBA pixels
        
        [SKY, TRANSPARENT]'''
        return str()
    @property
    def octree_resolution(self):
        '''(Enum) Resolution of raytrace accelerator, use higher resolutions for
        larger scenes
        
        [64, 128, 256, 512]'''
        return str()
    @property
    def raytrace_method(self):
        '''(Enum) Type of raytrace accelerator structure
        
        [AUTO, OCTREE, VBVH, SIMD_SVBVH, SIMD_QBVH]'''
        return str()
    @property
    def use_instances(self):
        '''(Boolean) Instance support leads to effective memory reduction when
        using duplicates'''
        return bool()
    @property
    def use_local_coords(self):
        '''(Boolean) Vertex coordinates are stored locally on each primitive
        (increases memory usage, but may have impact on speed)'''
        return bool()
    @property
    def use_antialiasing(self):
        '''(Boolean) Render and combine multiple samples per pixel to prevent
        jagged edges'''
        return bool()
    @property
    def antialiasing_samples(self):
        '''(Enum) Amount of anti-aliasing samples per pixel
        
        [5, 8, 11, 16]'''
        return str()
    @property
    def use_fields(self):
        '''(Boolean) Render image to two fields per frame, for interlaced TV
        output'''
        return bool()
    @property
    def field_order(self):
        '''(Enum) Order of video fields (select which lines get rendered first,
        to create smooth motion for TV output)
        
        [EVEN_FIRST, ODD_FIRST]'''
        return str()
    @property
    def use_fields_still(self):
        '''(Boolean) Disable the time difference between fields'''
        return bool()
    @property
    def use_shadows(self):
        '''(Boolean) Calculate shadows while rendering'''
        return bool()
    @property
    def use_envmaps(self):
        '''(Boolean) Calculate environment maps while rendering'''
        return bool()
    @property
    def use_sss(self):
        '''(Boolean) Calculate sub-surface scattering in materials rendering'''
        return bool()
    @property
    def use_raytrace(self):
        '''(Boolean) Pre-calculate the raytrace accelerator and render raytracing
        effects'''
        return bool()
    @property
    def use_textures(self):
        '''(Boolean) Use textures to affect material properties'''
        return bool()
    @property
    def use_edge_enhance(self):
        '''(Boolean) Create a toon outline around the edges of geometry'''
        return bool()
    @property
    def edge_threshold(self):
        '''(Integer) Threshold for drawing outlines on geometry edges'''
        return int()
    @property
    def edge_color(self):
        '''(Vector 3D) Edge color'''
        return mathutils.Vector()
    @property
    def use_freestyle(self):
        '''(Boolean) Draw stylized strokes using Freestyle'''
        return bool()
    @property
    def threads(self):
        '''(Integer) Number of CPU threads to use simultaneously while rendering
        (for multi-core/CPU systems)'''
        return int()
    @property
    def threads_mode(self):
        '''(Enum) Determine the amount of render threads used
        
        [AUTO, FIXED]'''
        return str()
    @property
    def use_motion_blur(self):
        '''(Boolean) Use multi-sampled 3D scene motion blur'''
        return bool()
    @property
    def motion_blur_samples(self):
        '''(Integer) Number of scene samples to take with motion blur'''
        return int()
    @property
    def motion_blur_shutter(self):
        '''(Float) Time taken in frames between shutter open and close'''
        return float()
    @property
    def use_border(self):
        '''(Boolean) Render a user-defined border region, within the frame size
        (note that this disables save_buffers and full_sample)'''
        return bool()
    @property
    def border_min_x(self):
        '''(Float) Minimum X value for the render border'''
        return float()
    @property
    def border_min_y(self):
        '''(Float) Minimum Y value for the render border'''
        return float()
    @property
    def border_max_x(self):
        '''(Float) Maximum X value for the render border'''
        return float()
    @property
    def border_max_y(self):
        '''(Float) Maximum Y value for the render border'''
        return float()
    @property
    def use_crop_to_border(self):
        '''(Boolean) Crop the rendered frame to the defined border size'''
        return bool()
    @property
    def use_placeholder(self):
        '''(Boolean) Create empty placeholder files while rendering frames
        (similar to Unix 'touch')'''
        return bool()
    @property
    def use_overwrite(self):
        '''(Boolean) Overwrite existing files while rendering'''
        return bool()
    @property
    def use_compositing(self):
        '''(Boolean) Process the render result through the compositing pipeline,
        if compositing nodes are enabled'''
        return bool()
    @property
    def use_sequencer(self):
        '''(Boolean) Process the render (and composited) result through the video
        sequence editor pipeline, if sequencer strips exist'''
        return bool()
    @property
    def use_file_extension(self):
        '''(Boolean) Add the file format extensions to the rendered file name
        (eg: filename + .jpg)'''
        return bool()
    @property
    def file_extension(self):
        '''(String) The file extension used for saving renders'''
        return str()
    @property
    def is_movie_format(self):
        '''(Boolean) When true the format is a movie'''
        return bool()
    @property
    def use_free_image_textures(self):
        '''(Boolean) Free all image textures from memory after render, to save
        memory before compositing'''
        return bool()
    @property
    def use_free_unused_nodes(self):
        '''(Boolean) Free Nodes that are not used while compositing, to save
        memory'''
        return bool()
    @property
    def use_save_buffers(self):
        '''(Boolean) Save tiles for all RenderLayers and SceneNodes to files in
        the temp directory (saves memory, required for Full Sample)'''
        return bool()
    @property
    def use_full_sample(self):
        '''(Boolean) Save for every anti-aliasing sample the entire RenderLayer
        results (this solves anti-aliasing issues with compositing)'''
        return bool()
    @property
    def display_mode(self):
        '''(Enum) Select where rendered images will be displayed
        
        [SCREEN, AREA, WINDOW, NONE]'''
        return str()
    @property
    def use_lock_interface(self):
        '''(Boolean) Lock interface during rendering in favor of giving more
        memory to the renderer'''
        return bool()
    @property
    def filepath(self):
        '''(String) Directory/name to save animations, # characters defines the
        position and length of frame numbers'''
        return str()
    @property
    def use_render_cache(self):
        '''(Boolean) Save render cache to EXR files (useful for heavy
        compositing, Note: affects indirectly rendered scenes)'''
        return bool()
    @property
    def bake_type(self):
        '''(Enum) Choose shading information to bake into the image
        
        [FULL, AO, SHADOW, NORMALS, TEXTURE, DISPLACEMENT, DERIVATIVE,
        VERTEX_COLORS, EMIT, ALPHA, MIRROR_INTENSITY, MIRROR_COLOR,
        SPEC_INTENSITY, SPEC_COLOR]'''
        return str()
    @property
    def bake_normal_space(self):
        '''(Enum) Choose normal space for baking
        
        [CAMERA, WORLD, OBJECT, TANGENT]'''
        return str()
    @property
    def bake_quad_split(self):
        '''(Enum) Choose the method used to split a quad into 2 triangles for
        baking
        
        [AUTO, FIXED, FIXED_ALT]'''
        return str()
    @property
    def bake_aa_mode(self):
        '''(Enum)
        
        [5, 8, 11, 16]'''
        return str()
    @property
    def use_bake_selected_to_active(self):
        '''(Boolean) Bake shading on the surface of selected objects to the
        active object'''
        return bool()
    @property
    def use_bake_normalize(self):
        '''(Boolean) With displacement normalize to the distance, with ambient
        occlusion normalize without using material settings'''
        return bool()
    @property
    def use_bake_clear(self):
        '''(Boolean) Clear Images before baking'''
        return bool()
    @property
    def use_bake_antialiasing(self):
        '''(Boolean) Enables Anti-aliasing'''
        return bool()
    @property
    def bake_margin(self):
        '''(Integer) Extends the baked result as a post process filter'''
        return int()
    @property
    def bake_distance(self):
        '''(Float) Maximum distance from active object to other object (in
        blender units)'''
        return float()
    @property
    def bake_bias(self):
        '''(Float) Bias towards faces further away from the object (in blender
        units)'''
        return float()
    @property
    def use_bake_multires(self):
        '''(Boolean) Bake directly from multires object'''
        return bool()
    @property
    def use_bake_lores_mesh(self):
        '''(Boolean) Calculate heights against unsubdivided low resolution mesh'''
        return bool()
    @property
    def bake_samples(self):
        '''(Integer) Number of samples used for ambient occlusion baking from
        multires'''
        return int()
    @property
    def use_bake_to_vertex_color(self):
        '''(Boolean) Bake to vertex colors instead of to a UV-mapped image'''
        return bool()
    @property
    def use_bake_user_scale(self):
        '''(Boolean) Use a user scale for the derivative map'''
        return bool()
    @property
    def bake_user_scale(self):
        '''(Float) Instead of automatically normalizing to 0..1, apply a user
        scale to the derivative map'''
        return float()
    @property
    def use_stamp_time(self):
        '''(Boolean) Include the rendered frame timecode as HH:MM:SS.FF in image
        metadata'''
        return bool()
    @property
    def use_stamp_date(self):
        '''(Boolean) Include the current date in image metadata'''
        return bool()
    @property
    def use_stamp_frame(self):
        '''(Boolean) Include the frame number in image metadata'''
        return bool()
    @property
    def use_stamp_camera(self):
        '''(Boolean) Include the name of the active camera in image metadata'''
        return bool()
    @property
    def use_stamp_lens(self):
        '''(Boolean) Include the active camera's lens in image metadata'''
        return bool()
    @property
    def use_stamp_scene(self):
        '''(Boolean) Include the name of the active scene in image metadata'''
        return bool()
    @property
    def use_stamp_note(self):
        '''(Boolean) Include a custom note in image metadata'''
        return bool()
    @property
    def use_stamp_marker(self):
        '''(Boolean) Include the name of the last marker in image metadata'''
        return bool()
    @property
    def use_stamp_filename(self):
        '''(Boolean) Include the .blend filename in image metadata'''
        return bool()
    @property
    def use_stamp_sequencer_strip(self):
        '''(Boolean) Include the name of the foreground sequence strip in image
        metadata'''
        return bool()
    @property
    def use_stamp_render_time(self):
        '''(Boolean) Include the render time in image metadata'''
        return bool()
    @property
    def stamp_note_text(self):
        '''(String) Custom text to appear in the stamp note'''
        return str()
    @property
    def use_stamp(self):
        '''(Boolean) Render the stamp info text in the rendered image'''
        return bool()
    @property
    def use_stamp_strip_meta(self):
        '''(Boolean) Use metadata from the strips in the sequencer'''
        return bool()
    @property
    def stamp_font_size(self):
        '''(Integer) Size of the font used when rendering stamp text'''
        return int()
    @property
    def stamp_foreground(self):
        '''(Float[4]) Color to use for stamp text'''
        return ''
    @property
    def stamp_background(self):
        '''(Float[4]) Color to use behind stamp text'''
        return ''
    @property
    def use_sequencer_gl_preview(self):
        '''(Boolean)'''
        return bool()
    @property
    def sequencer_gl_preview(self):
        '''(Enum) Method to draw in the sequencer view
        
        [BOUNDBOX, WIREFRAME, SOLID, TEXTURED, MATERIAL, RENDERED]'''
        return str()
    @property
    def sequencer_gl_render(self):
        '''(Enum) Method to draw in the sequencer view
        
        [BOUNDBOX, WIREFRAME, SOLID, TEXTURED, MATERIAL, RENDERED]'''
        return str()
    @property
    def use_sequencer_gl_textured_solid(self):
        '''(Boolean) Draw face-assigned textures in solid draw method'''
        return bool()
    @property
    def layers(self):
        '''(Sequence of SceneRenderLayer)'''
        return RenderLayers()
    @property
    def use_single_layer(self):
        '''(Boolean) Only render the active layer'''
        return bool()
    @property
    def views(self):
        '''(Sequence of SceneRenderView)'''
        return RenderViews()
    @property
    def stereo_views(self):
        '''(Sequence of SceneRenderView)'''
        return (SceneRenderView(),)
    @property
    def use_multiview(self):
        '''(Boolean) Use multiple views in the scene'''
        return bool()
    @property
    def views_format(self):
        '''(Enum)
        
        [STEREO_3D, MULTIVIEW]'''
        return str()
    @property
    def engine(self):
        '''(Enum) Engine to use for rendering
        
        [BLENDER_RENDER]'''
        return str()
    @property
    def has_multiple_engines(self):
        '''(Boolean) More than one rendering engine is available'''
        return bool()
    @property
    def use_shading_nodes(self):
        '''(Boolean) Active render engine uses new shading nodes system'''
        return bool()
    @property
    def use_game_engine(self):
        '''(Boolean) Current rendering engine is a game engine'''
        return bool()
    @property
    def use_simplify(self):
        '''(Boolean) Enable simplification of scene for quicker preview renders'''
        return bool()
    @property
    def simplify_subdivision(self):
        '''(Integer) Global maximum subdivision level'''
        return int()
    @property
    def simplify_child_particles(self):
        '''(Float) Global child particles percentage'''
        return float()
    @property
    def simplify_subdivision_render(self):
        '''(Integer) Global maximum subdivision level during rendering'''
        return int()
    @property
    def simplify_child_particles_render(self):
        '''(Float) Global child particles percentage during rendering'''
        return float()
    @property
    def simplify_shadow_samples(self):
        '''(Integer) Global maximum shadow samples'''
        return int()
    @property
    def simplify_ao_sss(self):
        '''(Float) Global approximate AO and SSS quality factor'''
        return float()
    @property
    def use_simplify_triangulate(self):
        '''(Boolean) Disable non-planar quads being triangulated'''
        return bool()
    @property
    def use_persistent_data(self):
        '''(Boolean) Keep render data around for faster re-renders'''
        return bool()
    @property
    def line_thickness_mode(self):
        '''(Enum) Line thickness mode for Freestyle line drawing
        
        [ABSOLUTE, RELATIVE]'''
        return str()
    @property
    def line_thickness(self):
        '''(Float) Line thickness in pixels'''
        return float()
    @property
    def bake(self):
        '''(BakeSettings)'''
        return BakeSettings()
    def frame_path(self, frame, preview, view):
        '''Return the absolute path to the filename to be written for a given
        frame
        
        Parameter:
          frame: (Integer) Frame number to use, if unset the current frame will be used
          preview: (Boolean) Use preview range
          view: (String) The name of the view to use to replace the "%" chars
        
        Returns:
          filepath: (String) The resulting filepath from the scenes render settings'''
        return str()