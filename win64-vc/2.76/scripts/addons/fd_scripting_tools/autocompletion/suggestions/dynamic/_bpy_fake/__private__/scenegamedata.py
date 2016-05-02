from . scenegamerecastdata import SceneGameRecastData
from . struct import Struct
from . text import Text
from . bpy_struct import bpy_struct
import mathutils

class SceneGameData(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def resolution_x(self):
        '''(Integer) Number of horizontal pixels in the screen'''
        return int()
    @property
    def resolution_y(self):
        '''(Integer) Number of vertical pixels in the screen'''
        return int()
    @property
    def vsync(self):
        '''(Enum) Change vsync settings
        
        [OFF, ON, ADAPTIVE]'''
        return str()
    @property
    def samples(self):
        '''(Enum) The number of AA Samples to use for MSAA
        
        [SAMPLES_0, SAMPLES_2, SAMPLES_4, SAMPLES_8, SAMPLES_16]'''
        return str()
    @property
    def depth(self):
        '''(Integer) Display bit depth of full screen display'''
        return int()
    @property
    def exit_key(self):
        '''(Enum) The key that exits the Game Engine
        
        [NONE, LEFTMOUSE, MIDDLEMOUSE, RIGHTMOUSE, BUTTON4MOUSE, BUTTON5MOUSE,
        BUTTON6MOUSE, BUTTON7MOUSE, ACTIONMOUSE, SELECTMOUSE, MOUSEMOVE,
        INBETWEEN_MOUSEMOVE, TRACKPADPAN, TRACKPADZOOM, MOUSEROTATE,
        WHEELUPMOUSE, WHEELDOWNMOUSE, WHEELINMOUSE, WHEELOUTMOUSE,
        EVT_TWEAK_L, EVT_TWEAK_M, EVT_TWEAK_R, EVT_TWEAK_A, EVT_TWEAK_S, A, B,
        C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y,
        Z, ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE,
        LEFT_CTRL, LEFT_ALT, LEFT_SHIFT, RIGHT_ALT, RIGHT_CTRL, RIGHT_SHIFT,
        OSKEY, GRLESS, ESC, TAB, RET, SPACE, LINE_FEED, BACK_SPACE, DEL,
        SEMI_COLON, PERIOD, COMMA, QUOTE, ACCENT_GRAVE, MINUS, SLASH,
        BACK_SLASH, EQUAL, LEFT_BRACKET, RIGHT_BRACKET, LEFT_ARROW,
        DOWN_ARROW, RIGHT_ARROW, UP_ARROW, NUMPAD_2, NUMPAD_4, NUMPAD_6,
        NUMPAD_8, NUMPAD_1, NUMPAD_3, NUMPAD_5, NUMPAD_7, NUMPAD_9,
        NUMPAD_PERIOD, NUMPAD_SLASH, NUMPAD_ASTERIX, NUMPAD_0, NUMPAD_MINUS,
        NUMPAD_ENTER, NUMPAD_PLUS, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10,
        F11, F12, F13, F14, F15, F16, F17, F18, F19, PAUSE, INSERT, HOME,
        PAGE_UP, PAGE_DOWN, END, MEDIA_PLAY, MEDIA_STOP, MEDIA_FIRST,
        MEDIA_LAST, TEXTINPUT, WINDOW_DEACTIVATE, TIMER, TIMER0, TIMER1,
        TIMER2, TIMER_JOBS, TIMER_AUTOSAVE, TIMER_REPORT, TIMERREGION,
        NDOF_MOTION, NDOF_BUTTON_MENU, NDOF_BUTTON_FIT, NDOF_BUTTON_TOP,
        NDOF_BUTTON_BOTTOM, NDOF_BUTTON_LEFT, NDOF_BUTTON_RIGHT,
        NDOF_BUTTON_FRONT, NDOF_BUTTON_BACK, NDOF_BUTTON_ISO1,
        NDOF_BUTTON_ISO2, NDOF_BUTTON_ROLL_CW, NDOF_BUTTON_ROLL_CCW,
        NDOF_BUTTON_SPIN_CW, NDOF_BUTTON_SPIN_CCW, NDOF_BUTTON_TILT_CW,
        NDOF_BUTTON_TILT_CCW, NDOF_BUTTON_ROTATE, NDOF_BUTTON_PANZOOM,
        NDOF_BUTTON_DOMINANT, NDOF_BUTTON_PLUS, NDOF_BUTTON_MINUS,
        NDOF_BUTTON_ESC, NDOF_BUTTON_ALT, NDOF_BUTTON_SHIFT, NDOF_BUTTON_CTRL,
        NDOF_BUTTON_1, NDOF_BUTTON_2, NDOF_BUTTON_3, NDOF_BUTTON_4,
        NDOF_BUTTON_5, NDOF_BUTTON_6, NDOF_BUTTON_7, NDOF_BUTTON_8,
        NDOF_BUTTON_9, NDOF_BUTTON_10, NDOF_BUTTON_A, NDOF_BUTTON_B,
        NDOF_BUTTON_C]'''
        return str()
    @property
    def raster_storage(self):
        '''(Enum) Set the storage mode used by the rasterizer
        
        [AUTO, IMMEDIATE, VERTEX_ARRAY]'''
        return str()
    @property
    def frequency(self):
        '''(Integer) Display clock frequency of fullscreen display'''
        return int()
    @property
    def show_fullscreen(self):
        '''(Boolean) Start player in a new fullscreen display'''
        return bool()
    @property
    def use_desktop(self):
        '''(Boolean) Use the current desktop resolution in fullscreen mode'''
        return bool()
    @property
    def frame_type(self):
        '''(Enum) Select the type of Framing you want
        
        [LETTERBOX, EXTEND, SCALE]'''
        return str()
    @property
    def frame_color(self):
        '''(Vector 3D) Set color of the bars'''
        return mathutils.Vector()
    @property
    def stereo(self):
        '''(Enum)
        
        [NONE, STEREO, DOME]'''
        return str()
    @property
    def stereo_mode(self):
        '''(Enum) Stereographic techniques
        
        [QUADBUFFERED, ABOVEBELOW, INTERLACED, ANAGLYPH, SIDEBYSIDE,
        VINTERLACE, 3DTVTOPBOTTOM]'''
        return str()
    @property
    def stereo_eye_separation(self):
        '''(Float) Set the distance between the eyes - the camera focal
        distance/30 should be fine'''
        return float()
    @property
    def dome_mode(self):
        '''(Enum) Dome physical configurations
        
        [FISHEYE, TRUNCATED_FRONT, TRUNCATED_REAR, ENVMAP, PANORAM_SPH]'''
        return str()
    @property
    def dome_tessellation(self):
        '''(Integer) Tessellation level - check the generated mesh in wireframe
        mode'''
        return int()
    @property
    def dome_buffer_resolution(self):
        '''(Float) Buffer Resolution - decrease it to increase speed'''
        return float()
    @property
    def dome_angle(self):
        '''(Integer) Field of View of the Dome - it only works in mode Fisheye
        and Truncated'''
        return int()
    @property
    def dome_tilt(self):
        '''(Integer) Camera rotation in horizontal axis'''
        return int()
    @property
    def dome_text(self):
        '''(Text) Custom Warp Mesh data file'''
        return Text()
    @property
    def physics_engine(self):
        '''(Enum) Physics engine used for physics simulation in the game engine
        
        [NONE, BULLET]'''
        return str()
    @property
    def physics_gravity(self):
        '''(Float) Gravitational constant used for physics simulation in the game
        engine'''
        return float()
    @property
    def occlusion_culling_resolution(self):
        '''(Integer) Size of the occlusion buffer, use higher value for better
        precision (slower)'''
        return int()
    @property
    def fps(self):
        '''(Integer) Nominal number of game frames per second (physics fixed
        timestep = 1/fps, independently of actual frame rate)'''
        return int()
    @property
    def logic_step_max(self):
        '''(Integer) Maximum number of logic frame per game frame if graphics
        slows down the game, higher value allows better synchronization with
        physics'''
        return int()
    @property
    def physics_step_max(self):
        '''(Integer) Maximum number of physics step per game frame if graphics
        slows down the game, higher value allows physics to keep up with
        realtime'''
        return int()
    @property
    def physics_step_sub(self):
        '''(Integer) Number of simulation substep per physic timestep, higher
        value give better physics precision'''
        return int()
    @property
    def deactivation_linear_threshold(self):
        '''(Float) Linear velocity that an object must be below before the
        deactivation timer can start'''
        return float()
    @property
    def deactivation_angular_threshold(self):
        '''(Float) Angular velocity that an object must be below before the
        deactivation timer can start'''
        return float()
    @property
    def deactivation_time(self):
        '''(Float) Amount of time (in seconds) after which objects with a
        velocity less than the given threshold will deactivate (0.0 means no
        deactivation)'''
        return float()
    @property
    def use_occlusion_culling(self):
        '''(Boolean) Use optimized Bullet DBVT tree for view frustum and
        occlusion culling (more efficient, but it can waste unnecessary CPU if
        the scene doesn't have occluder objects)'''
        return bool()
    @property
    def use_activity_culling(self):
        '''(Boolean) Activity culling is enabled'''
        return bool()
    @property
    def activity_culling_box_radius(self):
        '''(Float) Radius of the activity bubble, in Manhattan length (objects
        outside the box are activity-culled)'''
        return float()
    @property
    def show_debug_properties(self):
        '''(Boolean) Show properties marked for debugging while the game runs'''
        return bool()
    @property
    def show_framerate_profile(self):
        '''(Boolean) Show framerate and profiling information while the game runs'''
        return bool()
    @property
    def show_physics_visualization(self):
        '''(Boolean) Show a visualization of physics bounds and interactions'''
        return bool()
    @property
    def show_mouse(self):
        '''(Boolean) Start player with a visible mouse cursor'''
        return bool()
    @property
    def use_frame_rate(self):
        '''(Boolean) Respect the frame rate from the Physics panel in the world
        properties rather than rendering as many frames as possible'''
        return bool()
    @property
    def use_display_lists(self):
        '''(Boolean) Use display lists to speed up rendering by keeping geometry
        on the GPU'''
        return bool()
    @property
    def use_deprecation_warnings(self):
        '''(Boolean) Print warnings when using deprecated features in the python
        API'''
        return bool()
    @property
    def use_animation_record(self):
        '''(Boolean) Record animation to F-Curves'''
        return bool()
    @property
    def use_auto_start(self):
        '''(Boolean) Automatically start game at load time'''
        return bool()
    @property
    def use_restrict_animation_updates(self):
        '''(Boolean) Restrict the number of animation updates to the animation
        FPS (this is better for performance, but can cause issues with smooth
        playback)'''
        return bool()
    @property
    def material_mode(self):
        '''(Enum) Material mode to use for rendering
        
        [MULTITEXTURE, GLSL]'''
        return str()
    @property
    def use_glsl_lights(self):
        '''(Boolean) Use lights for GLSL rendering'''
        return bool()
    @property
    def use_glsl_shaders(self):
        '''(Boolean) Use shaders for GLSL rendering'''
        return bool()
    @property
    def use_glsl_shadows(self):
        '''(Boolean) Use shadows for GLSL rendering'''
        return bool()
    @property
    def use_glsl_ramps(self):
        '''(Boolean) Use ramps for GLSL rendering'''
        return bool()
    @property
    def use_glsl_nodes(self):
        '''(Boolean) Use nodes for GLSL rendering'''
        return bool()
    @property
    def use_glsl_color_management(self):
        '''(Boolean) Use color management for GLSL rendering'''
        return bool()
    @property
    def use_glsl_extra_textures(self):
        '''(Boolean) Use extra textures like normal or specular maps for GLSL
        rendering'''
        return bool()
    @property
    def use_material_caching(self):
        '''(Boolean) Cache materials in the converter (this is faster, but can
        cause problems with older Singletexture and Multitexture games)'''
        return bool()
    @property
    def obstacle_simulation(self):
        '''(Enum) Simulation used for obstacle avoidance in the game engine
        
        [NONE, RVO_RAYS, RVO_CELLS]'''
        return str()
    @property
    def level_height(self):
        '''(Float) Max difference in heights of obstacles to enable their
        interaction'''
        return float()
    @property
    def show_obstacle_simulation(self):
        '''(Boolean) Enable debug visualization for obstacle simulation'''
        return bool()
    @property
    def recast_data(self):
        '''(SceneGameRecastData)'''
        return SceneGameRecastData()
    @property
    def use_scene_hysteresis(self):
        '''(Boolean) Use LoD Hysteresis setting for the scene'''
        return bool()
    @property
    def scene_hysteresis_percentage(self):
        '''(Integer) Minimum distance change required to transition to the
        previous level of detail'''
        return int()