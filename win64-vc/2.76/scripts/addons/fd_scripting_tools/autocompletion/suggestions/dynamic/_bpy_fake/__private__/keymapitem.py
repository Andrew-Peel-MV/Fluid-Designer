from . struct import Struct
from . keymapitem import KeyMapItem
from . operatorproperties import OperatorProperties
from . bpy_struct import bpy_struct
import mathutils

class KeyMapItem(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def idname(self):
        '''(String) Identifier of operator to call on input event'''
        return str()
    @property
    def name(self):
        '''(String) Name of operator (translated) to call on input event'''
        return str()
    @property
    def properties(self):
        '''(OperatorProperties) Properties to set when the operator is called'''
        return OperatorProperties()
    @property
    def map_type(self):
        '''(Enum) Type of event mapping
        
        [KEYBOARD, TWEAK, MOUSE, NDOF, TEXTINPUT, TIMER]'''
        return str()
    @property
    def type(self):
        '''(Enum) Type of event
        
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
    def value(self):
        '''(Enum)
        
        [ANY, NOTHING, PRESS, RELEASE, CLICK, DOUBLE_CLICK, NORTH, NORTH_EAST,
        EAST, SOUTH_EAST, SOUTH, SOUTH_WEST, WEST, NORTH_WEST]'''
        return str()
    @property
    def id(self):
        '''(Integer) ID of the item'''
        return int()
    @property
    def any(self):
        '''(Boolean) Any modifier keys pressed'''
        return bool()
    @property
    def shift(self):
        '''(Boolean) Shift key pressed'''
        return bool()
    @property
    def ctrl(self):
        '''(Boolean) Control key pressed'''
        return bool()
    @property
    def alt(self):
        '''(Boolean) Alt key pressed'''
        return bool()
    @property
    def oskey(self):
        '''(Boolean) Operating system key pressed'''
        return bool()
    @property
    def key_modifier(self):
        '''(Enum) Regular key pressed as a modifier
        
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
    def show_expanded(self):
        '''(Boolean) Show key map event and property details in the user
        interface'''
        return bool()
    @property
    def propvalue(self):
        '''(Enum) The value this event translates to in a modal keymap
        
        [NONE]'''
        return str()
    @property
    def active(self):
        '''(Boolean) Activate or deactivate item'''
        return bool()
    @property
    def is_user_modified(self):
        '''(Boolean) Is this keymap item modified by the user'''
        return bool()
    @property
    def is_user_defined(self):
        '''(Boolean) Is this keymap item user defined (doesn't just replace a
        builtin item)'''
        return bool()
    def compare(self, item):
        '''compare
        
        Parameter:
          item: (KeyMapItem)
        
        Returns:
          result: (Boolean)'''
        return bool()