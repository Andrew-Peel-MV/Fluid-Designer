from . struct import Struct
from . mvprompt import mvPrompt
from . fd_tab import fd_tab
from . bpy_struct import bpy_struct
import mathutils

class mvPromptPage(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def MainTabIndex(self):
        '''(Integer)'''
        return int()
    @property
    def COL_Prompt(self):
        '''(Sequence of mvPrompt)'''
        return (mvPrompt(),)
    @property
    def PromptIndex(self):
        '''(Integer)'''
        return int()
    @property
    def COL_MainTab(self):
        '''(Sequence of fd_tab)'''
        return (fd_tab(),)