from . struct import Struct
from . walknavigation import WalkNavigation
from . bpy_struct import bpy_struct
import mathutils

class UserPreferencesInput(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def select_mouse(self):
        '''(Enum) Mouse button used for selection
        
        [LEFT, RIGHT]'''
        return str()
    @property
    def view_zoom_method(self):
        '''(Enum) Which style to use for viewport scaling
        
        [CONTINUE, DOLLY, SCALE]'''
        return str()
    @property
    def view_zoom_axis(self):
        '''(Enum) Axis of mouse movement to zoom in or out on
        
        [VERTICAL, HORIZONTAL]'''
        return str()
    @property
    def invert_mouse_zoom(self):
        '''(Boolean) Invert the axis of mouse movement for zooming'''
        return bool()
    @property
    def view_rotate_method(self):
        '''(Enum) Rotation style in the viewport
        
        [TURNTABLE, TRACKBALL]'''
        return str()
    @property
    def use_mouse_continuous(self):
        '''(Boolean) Allow moving the mouse outside the view on some
        manipulations (transform, ui control drag)'''
        return bool()
    @property
    def navigation_mode(self):
        '''(Enum) Which method to use for viewport navigation
        
        [WALK, FLY]'''
        return str()
    @property
    def walk_navigation(self):
        '''(WalkNavigation) Settings for walk navigation mode'''
        return WalkNavigation()
    @property
    def drag_threshold(self):
        '''(Integer) Amount of pixels you have to drag before dragging UI items
        happens'''
        return int()
    @property
    def tweak_threshold(self):
        '''(Integer) Number of pixels you have to drag before tweak event is
        triggered'''
        return int()
    @property
    def ndof_sensitivity(self):
        '''(Float) Overall sensitivity of the 3D Mouse for panning'''
        return float()
    @property
    def ndof_orbit_sensitivity(self):
        '''(Float) Overall sensitivity of the 3D Mouse for orbiting'''
        return float()
    @property
    def ndof_deadzone(self):
        '''(Float) Deadzone of the 3D Mouse'''
        return float()
    @property
    def ndof_pan_yz_swap_axis(self):
        '''(Boolean) Pan using up/down on the device (otherwise forward/backward)'''
        return bool()
    @property
    def ndof_zoom_invert(self):
        '''(Boolean) Zoom using opposite direction'''
        return bool()
    @property
    def ndof_show_guide(self):
        '''(Boolean) Display the center and axis during rotation'''
        return bool()
    @property
    def ndof_view_navigate_method(self):
        '''(Enum) Navigation style in the viewport
        
        [FREE, ORBIT]'''
        return str()
    @property
    def ndof_view_rotate_method(self):
        '''(Enum) Rotation style in the viewport
        
        [TURNTABLE, TRACKBALL]'''
        return str()
    @property
    def ndof_rotx_invert_axis(self):
        '''(Boolean)'''
        return bool()
    @property
    def ndof_roty_invert_axis(self):
        '''(Boolean)'''
        return bool()
    @property
    def ndof_rotz_invert_axis(self):
        '''(Boolean)'''
        return bool()
    @property
    def ndof_panx_invert_axis(self):
        '''(Boolean)'''
        return bool()
    @property
    def ndof_pany_invert_axis(self):
        '''(Boolean)'''
        return bool()
    @property
    def ndof_panz_invert_axis(self):
        '''(Boolean)'''
        return bool()
    @property
    def ndof_lock_horizon(self):
        '''(Boolean) Keep horizon level while flying with 3D Mouse'''
        return bool()
    @property
    def ndof_fly_helicopter(self):
        '''(Boolean) Device up/down directly controls your Z position'''
        return bool()
    @property
    def mouse_double_click_time(self):
        '''(Integer) Time/delay (in ms) for a double click'''
        return int()
    @property
    def use_mouse_emulate_3_button(self):
        '''(Boolean) Emulate Middle Mouse with Alt+Left Mouse (doesn't work with
        Left Mouse Select option)'''
        return bool()
    @property
    def use_emulate_numpad(self):
        '''(Boolean) Main 1 to 0 keys act as the numpad ones (useful for laptops)'''
        return bool()
    @property
    def use_mouse_mmb_paste(self):
        '''(Boolean) In text window, paste with middle mouse button instead of
        panning'''
        return bool()
    @property
    def invert_zoom_wheel(self):
        '''(Boolean) Swap the Mouse Wheel zoom direction'''
        return bool()
    @property
    def wheel_scroll_lines(self):
        '''(Integer) Number of lines scrolled at a time with the mouse wheel'''
        return int()
    @property
    def use_trackpad_natural(self):
        '''(Boolean) If your system uses 'natural' scrolling, this option keeps
        consistent trackpad usage throughout the UI'''
        return bool()
    @property
    def active_keyconfig(self):
        '''(String) The name of the active key configuration'''
        return str()