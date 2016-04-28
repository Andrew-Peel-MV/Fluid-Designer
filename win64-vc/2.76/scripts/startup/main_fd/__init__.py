# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy

from bpy.app.handlers import persistent
import os
from . import driver_functions
import inspect
import fd
import sys
import xml.etree.ElementTree as ET

@persistent
def update_library_paths(scene=None):
    """ Sets the library paths from the Library XML File
    """
    wm = bpy.context.window_manager.mv
    if os.path.exists(fd.get_library_path_file()):
        tree = ET.parse(fd.get_library_path_file())
        root = tree.getroot()
        for elm in root.findall("LibraryPaths"):
            items = elm.getchildren()
            for item in items:
                if item.tag == "Modules":
                    if os.path.exists(str(item.text)):
                        print('PATH FOUND',item.text)
                        wm.library_module_path = item.text
                    else:
                        wm.library_module_path = ""
                if item.tag == "Scenes":
                    if os.path.exists(str(item.text)):
                        wm.scene_library_path = item.text
                    else:
                        wm.scene_library_path = ""
                if item.tag == 'Projects':
                    if os.path.exists(str(item.text)):
                        wm.project_path = item.text
                    else:
                        wm.project_path = ""
                if item.tag == 'ProjectTemplates':
                    if os.path.exists(str(item.text)):
                        wm.project_template_path = item.text
                    else:
                        wm.project_template_path = ""
                if item.tag == 'Products':
                    if os.path.exists(str(item.text)):
                        wm.product_library_path = item.text
                    else:
                        wm.product_library_path = ""
                if item.tag == 'Inserts':
                    if os.path.exists(str(item.text)):
                        wm.insert_library_path = item.text
                    else:
                        wm.insert_library_path = ""
                if item.tag == 'Assemblies':
                    if os.path.exists(str(item.text)):
                        wm.assembly_library_path = item.text
                    else:
                        wm.assembly_library_path = ""
                if item.tag == 'Objects':
                    if os.path.exists(str(item.text)):
                        wm.object_library_path = item.text
                    else:
                        wm.object_library_path = ""
                if item.tag == 'Materials':
                    if os.path.exists(str(item.text)):
                        wm.material_library_path = item.text
                    else:
                        wm.material_library_path = ""
                if item.tag == 'Worlds':
                    if os.path.exists(str(item.text)):
                        wm.world_library_path = item.text
                    else:
                        wm.world_library_path = ""

@persistent
def set_default_user_prefs(scene):
    """ Always set specific user preferences
    """
    bpy.context.user_preferences.system.use_scripts_auto_execute = True

@persistent
def load_driver_functions(scene):
    """ Load Default Drivers
    """
    for name, obj in inspect.getmembers(driver_functions):
        if name not in bpy.app.driver_namespace:
            bpy.app.driver_namespace[name] = obj

# Register Startup Events
bpy.app.handlers.load_post.append(set_default_user_prefs)
bpy.app.handlers.load_post.append(load_driver_functions)
bpy.app.handlers.load_post.append(update_library_paths)

# Register the OpenGL Call back for dims
bpy.types.SpaceView3D.draw_handler_add(fd.draw_opengl, (None,None), 'WINDOW', 'POST_PIXEL')

# Add the tkinter directory as a valid system path
path = os.path.join(os.path.dirname(bpy.app.binary_path),str(bpy.app.version[0]) + "." + str(bpy.app.version[1]),"python","lib","tkinter")
sys.path.append(path)

def load_library_modules():
    """ Register Every Library Module on Startup
    """
    modules = fd.get_library_modules()
    for module in modules:
        mod = __import__(module)
        if hasattr(mod, "register"):
            mod.register()
    
def register():
    import sys
    import re
    from . import properties
    
    #Register All Fluid Properties with Blender
    properties.register()

    #Set Paths from Library XML to WM
    update_library_paths()
    
    #Add Library Module Scripts to PYTHON PATH
    sys.path.append(fd.get_library_scripts_dir())
    
    #Register All Library Modules
    load_library_modules()
    
    #Add/Overwrite Default Hot Key Commands
    wm = bpy.context.window_manager
    if wm.keyconfigs.addon:
    
        obj_km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
    
        kmi = obj_km.keymap_items.new('wm.console_toggle', 'HOME', 'PRESS', shift=True)
        
        kmi = obj_km.keymap_items.new('fd_general.properties', 'RIGHTMOUSE', 'PRESS')
        
        kmi = obj_km.keymap_items.new('wm.call_menu', 'A', 'PRESS', shift=True)
        kmi.properties.name = 'INFO_MT_fluidaddobject'
        
        edit_km = wm.keyconfigs.addon.keymaps.new(name='Mesh', space_type='EMPTY')
        
        kmi = edit_km.keymap_items.new('wm.call_menu', 'RIGHTMOUSE', 'PRESS')
        kmi.properties.name = 'MENU_right_click_menu_edit_mesh'
        
        edit_curve_km = wm.keyconfigs.addon.keymaps.new(name='Curve', space_type='EMPTY')
        
        kmi = edit_curve_km.keymap_items.new('wm.call_menu', 'RIGHTMOUSE', 'PRESS')
        kmi.properties.name = 'MENU_right_click_menu_edit_curve'
    
    # Look for eclipse bugging tools
    if os.path.exists(r'C:\Program Files\eclipse\plugins\org.python.pydev_2.8.2.2013090511\pysrc'):
        PYDEV_SOURCE_DIR = r'C:\Program Files\eclipse\plugins\org.python.pydev_2.8.2.2013090511\pysrc'
        if sys.path.count(PYDEV_SOURCE_DIR) < 1:
            sys.path.append(PYDEV_SOURCE_DIR)    
            
    elif os.path.exists(r'C:\Program Files (x86)\eclipse\plugins\org.python.pydev_2.8.2.2013090511\pysrc'):
        PYDEV_SOURCE_DIR = r'C:\Program Files (x86)\eclipse\plugins\org.python.pydev_2.8.2.2013090511\pysrc'
        if sys.path.count(PYDEV_SOURCE_DIR) < 1:
            sys.path.append(PYDEV_SOURCE_DIR) 
    #pydev 4.3, this could be changed to look for any version of pydev        
    if os.path.exists(r'C:\Program Files\eclipse\plugins\org.python.pydev_4.3.0.201508182223\pysrc'):
        PYDEV_SOURCE_DIR = r'C:\Program Files\eclipse\plugins\org.python.pydev_4.3.0.201508182223\pysrc'
        if sys.path.count(PYDEV_SOURCE_DIR) < 1:
            sys.path.append(PYDEV_SOURCE_DIR)             
               
    else:
        print("NO DEBUG ATTACHED")
    
def unregister():
    pass
