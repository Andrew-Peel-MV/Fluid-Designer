from . wm_properties import WM_PROPERTIES
from . uipiemenu import UIPieMenu
from . fd_window_manager import fd_window_manager
from . uipopupmenu import UIPopupMenu
from . imagepreview import ImagePreview
from . id import ID
from . struct import Struct
from . library import Library
from . keyconfigurations import KeyConfigurations
from . animdata import AnimData
from . event import Event
from . operator import Operator
from . window import Window
from . timer import Timer
from . bpy_struct import bpy_struct
import mathutils

class WindowManager(bpy_struct):
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
    def operators(self):
        '''(Sequence of Operator) Operator registry'''
        return (Operator(),)
    @property
    def windows(self):
        '''(Sequence of Window) Open windows'''
        return (Window(),)
    @property
    def keyconfigs(self):
        '''(Sequence of KeyConfig) Registered key configurations'''
        return KeyConfigurations()
    @property
    def clipboard(self):
        '''(String)'''
        return str()
    @property
    def addon_search(self):
        '''(String) Search within the selected filter'''
        return str()
    @property
    def addon_filter(self):
        '''(Enum) Filter addons by category'''
        return str()
    @property
    def addon_support(self):
        '''(Enum) Display support level
        
        [OFFICIAL, COMMUNITY, TESTING]'''
        return str()
    @property
    def mv(self):
        '''(fd_window_manager)'''
        return fd_window_manager()
    @property
    def cabinetlib(self):
        '''(WM_PROPERTIES)'''
        return WM_PROPERTIES()
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
    def fileselect_add(self, operator):
        '''Opens a file selector with an operator. The string properties
        'filepath', 'filename', 'directory' and a 'files' collection are
        assigned when present in the operator
        
        Parameter:
          operator: (Operator) Operator to call'''
        return 
    def modal_handler_add(self, operator):
        '''modal_handler_add
        
        Parameter:
          operator: (Operator) Operator to call
        
        Returns:
          handle: (Boolean)'''
        return bool()
    def event_timer_add(self, time_step, window):
        '''event_timer_add
        
        Parameter:
          time_step: (Float) Interval in seconds between timer events
          window: (Window) Window to attach the timer to or None
        
        Returns:
          result: (Timer)'''
        return Timer()
    def event_timer_remove(self, timer):
        '''event_timer_remove
        
        Parameter:
          timer: (Timer)'''
        return 
    def progress_begin(self, min, max):
        '''Start Progress bar
        
        Parameter:
          min: (Float) any value in range [0,9999]
          max: (Float) any value in range [min+1,9998]'''
        return 
    def progress_update(self, value):
        '''progress_update
        
        Parameter:
          value: (Float) any value between min and max as set in progress_begin()'''
        return 
    def progress_end(self):
        '''Terminate Progress bar'''
        return 
    def invoke_props_popup(self, operator, event):
        '''Operator popup invoke
        
        Parameter:
          operator: (Operator) Operator to call
          event: (Event) Event
        
        Returns:
          result: (Enum)'''
        return str()
    def invoke_props_dialog(self, operator, width, height):
        '''Operator dialog (non-autoexec popup) invoke
        
        Parameter:
          operator: (Operator) Operator to call
          width: (Integer) Width of the popup
          height: (Integer) Height of the popup
        
        Returns:
          result: (Enum)'''
        return str()
    def invoke_search_popup(self, operator):
        '''invoke_search_popup
        
        Parameter:
          operator: (Operator) Operator to call'''
        return 
    def invoke_popup(self, operator, width, height):
        '''Operator popup invoke
        
        Parameter:
          operator: (Operator) Operator to call
          width: (Integer) Width of the popup
          height: (Integer) Height of the popup
        
        Returns:
          result: (Enum)'''
        return str()
    def invoke_confirm(self, operator, event):
        '''Operator confirmation
        
        Parameter:
          operator: (Operator) Operator to call
          event: (Event) Event
        
        Returns:
          result: (Enum)'''
        return str()
    def pupmenu_begin__internal(self, title, icon):
        '''pupmenu_begin__internal
        
        Parameter:
          title: (String)
          icon: (Enum)
        
        Returns:
          menu: (UIPopupMenu)'''
        return UIPopupMenu()
    def pupmenu_end__internal(self, menu):
        '''pupmenu_end__internal
        
        Parameter:
          menu: (UIPopupMenu)'''
        return 
    def piemenu_begin__internal(self, title, icon, event):
        '''piemenu_begin__internal
        
        Parameter:
          title: (String)
          icon: (Enum)
          event: (Event)
        
        Returns:
          menu_pie: (UIPieMenu)'''
        return UIPieMenu()
    def piemenu_end__internal(self, menu):
        '''piemenu_end__internal
        
        Parameter:
          menu: (UIPieMenu)'''
        return 