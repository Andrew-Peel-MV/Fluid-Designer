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

bl_info = {
    "name":        "Scripting Tools",
    "description": "Scripting tools for the text editor.",
    "author":      "Ryan Montes",
    "version":     (1, 0, 0),
    "blender":     (2, 7, 6),
    "location":    "Text Editor",
    "category":    "Fluid Designer"
    }

# append jedi package path to make 'import jedi' available
import os, sys
sys.path.append(os.path.join(__path__[0], "jedi")) 

import importlib
from . import developer_utils
importlib.reload(developer_utils)
modules = developer_utils.setup_addon_modules(__path__, __name__, "bpy" in locals())

# register
import bpy

addon_keymaps = []
def register_keymaps():
    global addon_keymaps
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name = "Text", space_type = "TEXT_EDITOR")
    kmi = km.keymap_items.new("fd_scripting_tools.select_whole_string", type = "Y", value = "PRESS", ctrl = True)
    kmi = km.keymap_items.new("wm.call_menu", type = "SPACE", value = "PRESS", ctrl = True)
    kmi.properties.name = "code_autocomplete_insert_template_menu"
    kmi = km.keymap_items.new("wm.call_menu", type = "TAB", value = "PRESS", ctrl = True)
    kmi.properties.name = "code_autocomplete_select_text_block"
    addon_keymaps.append(km)

def unregister_keymaps():
    wm = bpy.context.window_manager
    for km in addon_keymaps:
        for kmi in km.keymap_items:
            km.keymap_items.remove(kmi)
        wm.keyconfigs.addon.keymaps.remove(km)
    addon_keymaps.clear()

#from . addon_development import AddonDevelopmentSceneProperties
from . quick_operators import register_menus, unregister_menus
#from . code_templates.base import draw_template_menu

def register():
    bpy.utils.register_module(__name__)
    register_keymaps()
    #register_menus()
    #bpy.types.TEXT_MT_templates.append(draw_template_menu)
    #bpy.types.Scene.addon_development = bpy.props.PointerProperty(name = "Addon Development", type = AddonDevelopmentSceneProperties)

def unregister():
    bpy.utils.unregister_module(__name__)
    unregister_keymaps()
    #unregister_menus()
    #bpy.types.TEXT_MT_templates.remove(draw_template_menu)
