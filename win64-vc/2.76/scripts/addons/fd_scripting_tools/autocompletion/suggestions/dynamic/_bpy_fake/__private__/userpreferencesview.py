from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class UserPreferencesView(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def show_tooltips(self):
        '''(Boolean) Display tooltips (when off hold Alt to force display)'''
        return bool()
    @property
    def show_tooltips_python(self):
        '''(Boolean) Show Python references in tooltips'''
        return bool()
    @property
    def show_object_info(self):
        '''(Boolean) Display objects name and frame number in 3D view'''
        return bool()
    @property
    def use_global_scene(self):
        '''(Boolean) Force the current Scene to be displayed in all Screens'''
        return bool()
    @property
    def show_large_cursors(self):
        '''(Boolean) Use large mouse cursors when available'''
        return bool()
    @property
    def show_view_name(self):
        '''(Boolean) Show the name of the view's direction in each 3D View'''
        return bool()
    @property
    def show_splash(self):
        '''(Boolean) Display splash screen on startup'''
        return bool()
    @property
    def show_playback_fps(self):
        '''(Boolean) Show the frames per second screen refresh rate, while
        animation is played back'''
        return bool()
    @property
    def use_mouse_over_open(self):
        '''(Boolean) Open menu buttons and pulldowns automatically when the mouse
        is hovering'''
        return bool()
    @property
    def open_toplevel_delay(self):
        '''(Integer) Time delay in 1/10 seconds before automatically opening top
        level menus'''
        return int()
    @property
    def open_sublevel_delay(self):
        '''(Integer) Time delay in 1/10 seconds before automatically opening sub
        level menus'''
        return int()
    @property
    def pie_initial_timeout(self):
        '''(Integer) Pie menus will use the initial mouse position as center for
        this amount of time (in 1/100ths of sec)'''
        return int()
    @property
    def pie_animation_timeout(self):
        '''(Integer) Time needed to fully animate the pie to unfolded state (in
        1/100ths of sec)'''
        return int()
    @property
    def pie_menu_radius(self):
        '''(Integer) Pie menu size in pixels'''
        return int()
    @property
    def pie_menu_threshold(self):
        '''(Integer) Distance from center needed before a selection can be made'''
        return int()
    @property
    def pie_menu_confirm(self):
        '''(Integer) Distance threshold after which selection is made (zero to
        disable)'''
        return int()
    @property
    def use_quit_dialog(self):
        '''(Boolean) Ask for confirmation when quitting through the window close
        button'''
        return bool()
    @property
    def use_gl_warn_support(self):
        '''(Boolean) Pop up a warning when an old OpenGL version is detected'''
        return bool()
    @property
    def open_left_mouse_delay(self):
        '''(Integer) Time in 1/10 seconds to hold the Left Mouse Button before
        opening the toolbox'''
        return int()
    @property
    def open_right_mouse_delay(self):
        '''(Integer) Time in 1/10 seconds to hold the Right Mouse Button before
        opening the toolbox'''
        return int()
    @property
    def show_column_layout(self):
        '''(Boolean) Use a column layout for toolbox'''
        return bool()
    @property
    def use_directional_menus(self):
        '''(Boolean) Otherwise menus, etc will always be top to bottom, left to
        right, no matter opening direction'''
        return bool()
    @property
    def use_global_pivot(self):
        '''(Boolean) Lock the same rotation/scaling pivot in all 3D Views'''
        return bool()
    @property
    def use_mouse_depth_navigate(self):
        '''(Boolean) Use the depth under the mouse to improve view
        pan/rotate/zoom functionality'''
        return bool()
    @property
    def use_mouse_depth_cursor(self):
        '''(Boolean) Use the depth under the mouse when placing the cursor'''
        return bool()
    @property
    def use_camera_lock_parent(self):
        '''(Boolean) When the camera is locked to the view and in fly mode,
        transform the parent rather than the camera'''
        return bool()
    @property
    def use_zoom_to_mouse(self):
        '''(Boolean) Zoom in towards the mouse pointer's position in the 3D view,
        rather than the 2D window center'''
        return bool()
    @property
    def use_auto_perspective(self):
        '''(Boolean) Automatically switch between orthographic and perspective
        when changing from top/front/side views'''
        return bool()
    @property
    def use_rotate_around_active(self):
        '''(Boolean) Use selection as the pivot point'''
        return bool()
    @property
    def show_mini_axis(self):
        '''(Boolean) Show a small rotating 3D axes in the bottom left corner of
        the 3D View'''
        return bool()
    @property
    def mini_axis_size(self):
        '''(Integer) The axes icon's size'''
        return int()
    @property
    def mini_axis_brightness(self):
        '''(Integer) Brightness of the icon'''
        return int()
    @property
    def smooth_view(self):
        '''(Integer) Time to animate the view in milliseconds, zero to disable'''
        return int()
    @property
    def rotation_angle(self):
        '''(Float) Rotation step for numerical pad keys (2 4 6 8)'''
        return float()
    @property
    def show_manipulator(self):
        '''(Boolean) Use 3D transform manipulator'''
        return bool()
    @property
    def manipulator_size(self):
        '''(Integer) Diameter of the manipulator'''
        return int()
    @property
    def manipulator_handle_size(self):
        '''(Integer) Size of manipulator handles as percentage of the radius'''
        return int()
    @property
    def manipulator_hotspot(self):
        '''(Integer) Distance around the handles to accept mouse clicks'''
        return int()
    @property
    def object_origin_size(self):
        '''(Integer) Diameter in Pixels for Object/Lamp origin display'''
        return int()
    @property
    def view2d_grid_spacing_min(self):
        '''(Integer) Minimum number of pixels between each gridline in 2D
        Viewports'''
        return int()
    @property
    def timecode_style(self):
        '''(Enum) Format of Time Codes displayed when not displaying timing in
        terms of frames
        
        [MINIMAL, SMPTE, SMPTE_COMPACT, MILLISECONDS, SECONDS_ONLY]'''
        return str()
    @property
    def view_frame_type(self):
        '''(Enum) How zooming to frame focuses around current frame
        
        [KEEP_RANGE, SECONDS, KEYFRAMES]'''
        return str()
    @property
    def view_frame_keyframes(self):
        '''(Integer) Keyframes around cursor that we zoom around'''
        return int()
    @property
    def view_frame_seconds(self):
        '''(Float) Seconds around cursor that we zoom around'''
        return float()