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
from bpy.types import Header, Menu, Panel
import os
import fd

def is_hidden_library(library_name):
    """ Determines if a library should be displayed
        in the interface. Some items in the library are
        only used in the product and insert librarys
    """
    if '_HIDDEN' in library_name:
        return True
    else:
        return False

class FILEBROWSER_HT_fluidheader(Header):
    bl_space_type = 'FILE_BROWSER'

    def draw(self, context):
        layout = self.layout
        layout.menu('MENU_File_Browser_Options',icon='COLLAPSEMENU',text="")
        library_tabs = context.scene.mv.ui.library_tabs
    
        if library_tabs == 'SCENE':
            if context.scene.mv.scene_library_name == "":
                layout.operator("fd_general.reload_library",'Click Here to Load Library',icon='FILE_REFRESH')
            else:
                layout.menu('FILEBROWSER_MT_active_scene_libraries',icon='SCENE_DATA',text="  " + context.scene.mv.scene_library_name)
                if context.scene.mv.scene_category_name != "":
                    layout.menu('FILEBROWSER_MT_active_scene_categories',icon='FILESEL',text="  " + context.scene.mv.scene_category_name)            
        
        if library_tabs == 'PRODUCT':
            if context.scene.mv.product_library_name == "":
                layout.operator("fd_general.reload_library",'Click Here to Load Library',icon='FILE_REFRESH')
            else:
                layout.menu('FILEBROWSER_MT_active_product_libraries',icon='OUTLINER_OB_LATTICE',text="  " + context.scene.mv.product_library_name)
                if context.scene.mv.product_category_name != "":
                    layout.menu('FILEBROWSER_MT_active_product_categories',icon='FILESEL',text="  " + context.scene.mv.product_category_name)
        
        elif library_tabs == 'INSERT':
            if context.scene.mv.insert_library_name == "":
                layout.operator("fd_general.reload_library",'Click Here to Load Library',icon='FILE_REFRESH')
            else:
                layout.menu('FILEBROWSER_MT_active_insert_libraries',icon='STICKY_UVS_LOC',text="  " + context.scene.mv.insert_library_name)
                if context.scene.mv.insert_category_name != "":
                    layout.menu('FILEBROWSER_MT_active_insert_categories',icon='FILESEL',text="  " + context.scene.mv.insert_category_name)
        
        elif library_tabs == 'ASSEMBLY':
            if context.scene.mv.assembly_library_name == "":
                layout.operator("fd_general.reload_library",'Click Here to Load Library',icon='FILE_REFRESH')
            else:
                layout.menu('FILEBROWSER_MT_active_assembly_libraries',icon='OUTLINER_DATA_LATTICE',text="  " + context.scene.mv.assembly_library_name)
                if context.scene.mv.assembly_category_name != "":
                    layout.menu('FILEBROWSER_MT_active_assembly_categories',icon='FILESEL',text="  " + context.scene.mv.assembly_category_name)
        
        elif library_tabs == 'OBJECT':
            if context.scene.mv.object_library_name == "":
                layout.operator("fd_general.reload_library",'Click Here to Load Library',icon='FILE_REFRESH')
            else:
                layout.menu('FILEBROWSER_MT_active_object_libraries',icon='OBJECT_DATA',text="  " + context.scene.mv.object_library_name)
                if context.scene.mv.object_category_name != "":
                    layout.menu('FILEBROWSER_MT_active_object_categories',icon='FILESEL',text="  " + context.scene.mv.object_category_name)
        
        elif library_tabs == 'MATERIAL':
            if context.scene.mv.material_library_name == "":
                layout.operator("fd_general.reload_library",'Click Here to Load Library',icon='FILE_REFRESH')
            else:
                layout.menu('FILEBROWSER_MT_active_material_libraries',icon='MATERIAL',text="  " + context.scene.mv.material_library_name)
                if context.scene.mv.material_category_name != "":
                    layout.menu('FILEBROWSER_MT_active_material_categories',icon='FILESEL',text="  " + context.scene.mv.material_category_name)
        
        elif library_tabs == 'WORLD':
            if context.scene.mv.world_library_name == "":
                layout.operator("fd_general.reload_library",'Click Here to Load Library',icon='FILE_REFRESH')
            else:
                layout.menu('FILEBROWSER_MT_active_world_libraries',icon='MATERIAL',text="  " + context.scene.mv.world_library_name)
                if context.scene.mv.world_category_name != "":
                    layout.menu('FILEBROWSER_MT_active_world_categories',icon='FILESEL',text="  " + context.scene.mv.world_category_name)
        
        else:
            icon = 'X'

class FILEBROWSER_MT_active_scene_libraries(Menu):
    bl_label = "Active Scene Libraries"

    def draw(self, context):
        layout = self.layout
        path = fd.get_library_dir("scenes")
        dirs =  os.listdir(path)
        for lib in dirs:
            if not is_hidden_library(lib):
                lib_path = os.path.join(path,lib)
                if os.path.isdir(lib_path):
                    if lib == context.scene.mv.scene_library_name:
                        layout.operator('fd_general.change_library',text=lib,icon='LAYER_ACTIVE').library_name = lib
                    else:
                        layout.operator('fd_general.change_library',text=lib,icon='LAYER_USED').library_name = lib
        
class FILEBROWSER_MT_active_scene_categories(Menu):
    bl_label = "Active Scene Libraries"
     
    def draw(self, context):
        layout = self.layout
         
        path = fd.get_library_dir("scenes")
        lib_path = os.path.join(path,context.scene.mv.scene_library_name)
        categories =  os.listdir(lib_path)
        for category in categories:
            cat_path = os.path.join(lib_path,category)
            if os.path.isdir(cat_path):
                if category == context.scene.mv.scene_category_name:
                    layout.operator('fd_general.change_category',text=category,icon='LAYER_ACTIVE').category_name = category
                else:
                    layout.operator('fd_general.change_category',text=category,icon='LAYER_USED').category_name = category

class FILEBROWSER_MT_active_product_libraries(Menu):
    bl_label = "Active Product Libraries"

    def draw(self, context):
        layout = self.layout
        path = fd.get_library_dir("products")
        dirs =  os.listdir(path)
        for lib in dirs:
            if not is_hidden_library(lib):
                lib_path = os.path.join(path,lib)
                if os.path.isdir(lib_path):
                    if lib == context.scene.mv.product_library_name:
                        layout.operator('fd_general.change_library',text=lib,icon='LAYER_ACTIVE').library_name = lib
                    else:
                        layout.operator('fd_general.change_library',text=lib,icon='LAYER_USED').library_name = lib
        
class FILEBROWSER_MT_active_product_categories(Menu):
    bl_label = "Active Product Libraries"
     
    def draw(self, context):
        layout = self.layout
         
        path = fd.get_library_dir("products")
        lib_path = os.path.join(path,context.scene.mv.product_library_name)
        categories =  os.listdir(lib_path)
        for category in categories:
            cat_path = os.path.join(lib_path,category)
            if os.path.isdir(cat_path):
                if category == context.scene.mv.product_category_name:
                    layout.operator('fd_general.change_category',text=category,icon='LAYER_ACTIVE').category_name = category
                else:
                    layout.operator('fd_general.change_category',text=category,icon='LAYER_USED').category_name = category
            
class FILEBROWSER_MT_active_insert_libraries(Menu):
    bl_label = "Active Insert Libraries"

    def draw(self, context):
        layout = self.layout
        path = fd.get_library_dir("inserts")
        dirs =  os.listdir(path)
        for lib in dirs:
            if not is_hidden_library(lib):
                lib_path = os.path.join(path,lib)
                if os.path.isdir(lib_path):
                    if lib == context.scene.mv.insert_library_name:
                        layout.operator('fd_general.change_library',text=lib,icon='LAYER_ACTIVE').library_name = lib
                    else:
                        layout.operator('fd_general.change_library',text=lib,icon='LAYER_USED').library_name = lib
        
class FILEBROWSER_MT_active_insert_categories(Menu):
    bl_label = "Active Insert Libraries"

    def draw(self, context):
        layout = self.layout
        path = fd.get_library_dir("inserts")
        lib_path = os.path.join(path,context.scene.mv.insert_library_name)
        categories =  os.listdir(lib_path)
        for category in categories:
            cat_path = os.path.join(lib_path,category)
            if os.path.isdir(cat_path):
                if category == context.scene.mv.insert_category_name:
                    layout.operator('fd_general.change_category',text=category,icon='LAYER_ACTIVE').category_name = category
                else:
                    layout.operator('fd_general.change_category',text=category,icon='LAYER_USED').category_name = category
            
class FILEBROWSER_MT_active_assembly_libraries(Menu):
    bl_label = "Active Assembly Libraries"

    def draw(self, context):
        layout = self.layout
        path = fd.get_library_dir("assemblies")
        dirs =  os.listdir(path)
        for lib in dirs:
            if not is_hidden_library(lib):
                lib_path = os.path.join(path,lib)
                if os.path.isdir(lib_path):
                    if lib == context.scene.mv.assembly_library_name:
                        layout.operator('fd_general.change_library',text=lib,icon='LAYER_ACTIVE').library_name = lib
                    else:
                        layout.operator('fd_general.change_library',text=lib,icon='LAYER_USED').library_name = lib
        
class FILEBROWSER_MT_active_assembly_categories(Menu):
    bl_label = "Active Assembly Libraries"

    def draw(self, context):
        layout = self.layout
        path = fd.get_library_dir("assemblies")
        lib_path = os.path.join(path,context.scene.mv.assembly_library_name)
        categories =  os.listdir(lib_path)
        for category in categories:
            cat_path = os.path.join(lib_path,category)
            if os.path.isdir(cat_path):
                if category == context.scene.mv.assembly_category_name:
                    layout.operator('fd_general.change_category',text=category,icon='LAYER_ACTIVE').category_name = category
                else:
                    layout.operator('fd_general.change_category',text=category,icon='LAYER_USED').category_name = category
            
class FILEBROWSER_MT_active_object_libraries(Menu):
    bl_label = "Active Object Libraries"

    def draw(self, context):
        layout = self.layout
        path = fd.get_library_dir("objects")
        dirs =  os.listdir(path)
        for lib in dirs:
            if not is_hidden_library(lib):
                lib_path = os.path.join(path,lib)
                if os.path.isdir(lib_path):
                    if lib == context.scene.mv.object_library_name:
                        layout.operator('fd_general.change_library',text=lib,icon='LAYER_ACTIVE').library_name = lib
                    else:
                        layout.operator('fd_general.change_library',text=lib,icon='LAYER_USED').library_name = lib
        
class FILEBROWSER_MT_active_object_categories(Menu):
    bl_label = "Active Object Categories"

    def draw(self, context):
        layout = self.layout
        path = fd.get_library_dir("objects")
        lib_path = os.path.join(path,context.scene.mv.object_library_name)
        categories =  os.listdir(lib_path)
        for category in categories:
            cat_path = os.path.join(lib_path,category)
            if os.path.isdir(cat_path):
                if category == context.scene.mv.object_category_name:
                    layout.operator('fd_general.change_category',text=category,icon='LAYER_ACTIVE').category_name = category
                else:
                    layout.operator('fd_general.change_category',text=category,icon='LAYER_USED').category_name = category
            
class FILEBROWSER_MT_active_material_libraries(Menu):
    bl_label = "Active Material Libraries"

    def draw(self, context):
        layout = self.layout
        path = fd.get_library_dir("materials")
        dirs =  os.listdir(path)
        for lib in dirs:
            if not is_hidden_library(lib):
                lib_path = os.path.join(path,lib)
                if os.path.isdir(lib_path):
                    if lib == context.scene.mv.material_library_name:
                        layout.operator('fd_general.change_library',text=lib,icon='LAYER_ACTIVE').library_name = lib
                    else:
                        layout.operator('fd_general.change_library',text=lib,icon='LAYER_USED').library_name = lib
        
class FILEBROWSER_MT_active_material_categories(Menu):
    bl_label = "Active Material Categories"

    def draw(self, context):
        layout = self.layout
        path = fd.get_library_dir("materials")
        lib_path = os.path.join(path,context.scene.mv.material_library_name)
        categories =  os.listdir(lib_path)
        for category in categories:
            cat_path = os.path.join(lib_path,category)
            if os.path.isdir(cat_path):
                if category == context.scene.mv.material_category_name:
                    layout.operator('fd_general.change_category',text=category,icon='LAYER_ACTIVE').category_name = category
                else:
                    layout.operator('fd_general.change_category',text=category,icon='LAYER_USED').category_name = category
            
class FILEBROWSER_MT_active_world_libraries(Menu):
    bl_label = "Active World Libraries"

    def draw(self, context):
        layout = self.layout
        path = fd.get_library_dir("worlds")
        dirs =  os.listdir(path)
        for lib in dirs:
            if not is_hidden_library(lib):
                lib_path = os.path.join(path,lib)
                if os.path.isdir(lib_path):
                    if lib == context.scene.mv.world_library_name:
                        layout.operator('fd_general.change_library',text=lib,icon='LAYER_ACTIVE').library_name = lib
                    else:
                        layout.operator('fd_general.change_library',text=lib,icon='LAYER_USED').library_name = lib
        
class FILEBROWSER_MT_active_world_categories(Menu):
    bl_label = "Active World Categories"

    def draw(self, context):
        layout = self.layout
        path = fd.get_library_dir("worlds")
        lib_path = os.path.join(path,context.scene.mv.world_library_name)
        categories =  os.listdir(lib_path)
        for category in categories:
            cat_path = os.path.join(lib_path,category)
            if os.path.isdir(cat_path):
                if category == context.scene.mv.world_category_name:
                    layout.operator('fd_general.change_category',text=category,icon='LAYER_ACTIVE').category_name = category
                else:
                    layout.operator('fd_general.change_category',text=category,icon='LAYER_USED').category_name = category
            
class FILEBROWSER_MT_fd_filters(Menu):
    bl_label = "View"

    def draw(self, context):
        layout = self.layout
        st = context.space_data
        params = st.params
        
        if params:
            layout.prop(params, "use_filter", text="Use Filters", icon='FILTER')
            layout.separator()
            layout.operator("fd_general.dialog_show_filters",icon='INFO')

class FILEBROWSER_MT_fd_tools(Menu):
    bl_label = "View"

    def draw(self, context):
        layout = self.layout
        layout.operator("fd_library.draw_items_in_category", icon='BRUSH_DATA')

class FILEBROWSER_MT_fd_view(Menu):
    bl_label = "View"

    def draw(self, context):
        layout = self.layout
        layout.operator("fd_library.open_active_library_path", text="Open Current Category in Windows Explorer", icon='FILE_FOLDER')
        layout.operator("fd_library.refresh_library", text="Refresh Library", icon='FILE_REFRESH')
        layout.separator()
        layout.operator("file.previous", text="Back to Previous", icon='BACK')
        layout.operator("file.parent", text="Go to Parent", icon='FILE_PARENT')
        layout.separator()
        layout.operator_context = "EXEC_DEFAULT"
        layout.operator("file.directory_new", icon='NEWFOLDER')

class FILEBROWSER_MT_fd_save(Menu):
    bl_label = "Save"

    def draw(self, context):
        layout = self.layout
        layout.operator("fd_ops.save_file_to_active_category", text="Save To Category", icon='SAVE_COPY')

class FILEBROWSER_MT_fd_navigation(Menu):
    bl_label = "Navigation"

    def draw(self, context):
        layout = self.layout
        st = context.space_data
        params = st.params
        if params:
            layout.prop(params, "use_filter", text="Use Filters", icon='FILTER')
            layout.prop(params, "use_filter_folder", text="Show Folders")
            layout.prop(params, "use_filter_blender", text="Show Blender Files")
            layout.prop(params, "use_filter_backup", text="Show Backup Files")
            layout.prop(params, "use_filter_image", text="Show Image Files")
            layout.prop(params, "use_filter_movie", text="Show Video Files")
            layout.prop(params, "use_filter_script", text="Show Script Files")
            layout.prop(params, "use_filter_font", text="Show Font Files")
            layout.prop(params, "use_filter_text", text="Show Text Files")

class FILE_MT_fd_menus(Menu):
    bl_space_type = 'VIEW3D_MT_editor_menus'
    bl_label = ""

    def draw(self, context):
        self.draw_menus(self.layout, context)

    @staticmethod
    def draw_menus(layout, context):
        layout.menu("FILEBROWSER_MT_fd_view",icon='VIEWZOOM',text="     View     ")
        layout.menu("FILEBROWSER_MT_fd_filters",icon='FILTER',text="     Filters     ")
        layout.menu("FILEBROWSER_MT_fd_save",icon='FILE_TICK',text="     Save     ")
        layout.menu("FILEBROWSER_MT_fd_tools",icon='MODIFIER',text="     Tools     ")
        
class PANEL_fluid_libraries(Panel):
    bl_space_type = "FILE_BROWSER"
    bl_region_type = "TOOLS"
    bl_label = " "
    bl_options = {'HIDE_HEADER'}

    @classmethod
    def poll(cls, context):
        return True

    def draw_header(self, context):
        layout = self.layout
        layout.label(" ",icon='EXTERNAL_DATA')

    def draw(self, context):
        ui = context.scene.mv.ui
        layout = self.layout
        col = layout.column(align=True)
#         col.prop_enum(ui, "library_tabs", 'SCENE', icon='SCENE_DATA', text="  Scenes")
        col.prop_enum(ui, "library_tabs", 'PRODUCT', icon='OUTLINER_OB_LATTICE', text="  Products") 
        col.prop_enum(ui, "library_tabs", 'INSERT', icon='STICKY_UVS_LOC', text="  Inserts") 
        col.separator()
        col.prop_enum(ui, "library_tabs", 'ASSEMBLY', icon='OUTLINER_DATA_LATTICE', text="  Assemblies") 
        col.prop_enum(ui, "library_tabs", 'OBJECT', icon='OBJECT_DATA', text="  Objects") 
        col.prop_enum(ui, "library_tabs", 'MATERIAL', icon='MATERIAL', text="  Materials") 
        col.prop_enum(ui, "library_tabs", 'WORLD', icon='WORLD', text="  Worlds") 

class MENU_File_Browser_Options(Menu):
    bl_label = "File Browser Options"

    def draw(self, context):
        layout = self.layout
        st = context.space_data
        #TODO file browser options
        #layout.operator("fd_general.open_browser_window",text="File Browser Options",icon='INFO').path = fd.get_file_browser_path(context) #TODO
        layout.operator("fd_general.open_browser_window",text="Open Location in Browser",icon='FILE_FOLDER').path = fd.get_file_browser_path(context)
        layout.separator()
        layout.operator("fd_general.create_thumbnails",text="Create Thumbnails",icon='EXTERNAL_DATA')
        layout.operator("fd_general.append_items",text="Append Items",icon='EXTERNAL_DATA')
        
class INFO_MT_addons(Menu):
    bl_idname = "INFO_MT_addons"
    bl_label = "Microvellum Add-ons"

    def draw(self, context):
        import addon_utils
        
        layout = self.layout
        
        userpref = context.user_preferences
        used_ext = {ext.module for ext in userpref.addons}
        
        for mod in addon_utils.modules(refresh=False):
            if mod.bl_info['category'] == 'Library Add-on':
                if mod.__name__ in used_ext:
                    layout.operator('wm.addon_disable',text=mod.bl_info["name"],icon='CHECKBOX_HLT').module = mod.__name__
                else:
                    layout.operator('wm.addon_enable',text=mod.bl_info["name"],icon='CHECKBOX_DEHLT').module = mod.__name__
        layout.separator()
        layout.operator('wm.save_userpref',text="Save User Preferences",icon='FILE_TICK')

#------REGISTER
classes = [
           FILEBROWSER_HT_fluidheader,
           FILE_MT_fd_menus,
           FILEBROWSER_MT_active_scene_libraries,
           FILEBROWSER_MT_active_scene_categories,
           FILEBROWSER_MT_active_product_libraries,
           FILEBROWSER_MT_active_product_categories,
           FILEBROWSER_MT_active_insert_libraries,
           FILEBROWSER_MT_active_insert_categories,
           FILEBROWSER_MT_active_assembly_libraries,
           FILEBROWSER_MT_active_assembly_categories,
           FILEBROWSER_MT_active_object_libraries,
           FILEBROWSER_MT_active_object_categories,
           FILEBROWSER_MT_active_material_libraries,
           FILEBROWSER_MT_active_material_categories,
           FILEBROWSER_MT_active_world_libraries,
           FILEBROWSER_MT_active_world_categories,
           FILEBROWSER_MT_fd_filters,
           FILEBROWSER_MT_fd_view,
           FILEBROWSER_MT_fd_navigation,
           FILEBROWSER_MT_fd_save,
           MENU_File_Browser_Options,
           INFO_MT_addons,
           PANEL_fluid_libraries,
           FILEBROWSER_MT_fd_tools
           ]

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

if __name__ == "__main__":
    register()
