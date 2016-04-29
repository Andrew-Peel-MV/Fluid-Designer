"""
Microvellum 
Cabinet & Closet Designer
Stores the UI, Properties, and Operators for the cabinet and closet designer panel
the Panel definition is stored in an add-on.
"""

import bpy
import fd
import math
import os

from bpy.app.handlers import persistent

HIDDEN_FOLDER_NAME = "_HIDDEN"
CROWN_CATEGORY_NAME = "Crown Molding Profiles"
BASE_CATEGORY_NAME = "Base Molding Profiles"

DOOR_LIBRARY_NAME = "Cabinet Assemblies"
DOOR_CATEGORY_NAME = "Door Panels"

COLUMN_LIBRARY_NAME = "Cabinet Assemblies"
COLUMN_CATEGORY_NAME = "Columns"

CLOSET_MATERIAL_LIBRARY_NAME = "Laminates - Formica"
CLOSET_WOOD_MATERIAL_CATEGORY_NAME = "Formica Wood Grains"
CLOSET_SOLID_MATERIAL_CATEGORY_NAME = "Formica Solids"

PULL_CATEGORY_NAME = "Cabinet Pulls"
CLOSET_ACCESSORY_CATEGORY_NAME = "Closet Accessories"

preview_collections = {}

def enum_crown_molding(self,context):
    if context is None:
        return []
    
    icon_dir = os.path.join(fd.get_library_dir("objects"),HIDDEN_FOLDER_NAME,CROWN_CATEGORY_NAME)
    pcoll = preview_collections["crown_moldings"]
    return fd.get_previews(icon_dir,pcoll)

def enum_base_molding(self,context):
    if context is None:
        return []
    
    icon_dir = os.path.join(fd.get_library_dir("objects"),HIDDEN_FOLDER_NAME,BASE_CATEGORY_NAME)
    pcoll = preview_collections["base_moldings"]
    return fd.get_previews(icon_dir,pcoll)

def enum_door_styles(self,context):
    if context is None:
        return []
    
    icon_dir = os.path.join(fd.get_library_dir("assemblies"),HIDDEN_FOLDER_NAME,DOOR_LIBRARY_NAME,DOOR_CATEGORY_NAME)
    pcoll = preview_collections["door_styles"]
    return fd.get_previews(icon_dir,pcoll)

def enum_column_styles(self,context):
    if context is None:
        return []
    
    icon_dir = os.path.join(fd.get_library_dir("assemblies"),HIDDEN_FOLDER_NAME,COLUMN_LIBRARY_NAME,COLUMN_CATEGORY_NAME)
    pcoll = preview_collections["column_styles"]
    return fd.get_previews(icon_dir,pcoll)

def enum_closet_wood_materials(self,context):
    if context is None:
        return []
    
    icon_dir = os.path.join(fd.get_library_dir("materials"),CLOSET_MATERIAL_LIBRARY_NAME,CLOSET_WOOD_MATERIAL_CATEGORY_NAME)
    pcoll = preview_collections["closet_wood_materials"]
    return fd.get_previews(icon_dir,pcoll)

def enum_closet_solid_materials(self,context):
    if context is None:
        return []
    
    icon_dir = os.path.join(fd.get_library_dir("materials"),CLOSET_MATERIAL_LIBRARY_NAME,CLOSET_SOLID_MATERIAL_CATEGORY_NAME)
    pcoll = preview_collections["closet_solid_materials"]
    return fd.get_previews(icon_dir,pcoll)

def enum_pulls(self,context):
    if context is None:
        return []
    
    icon_dir = os.path.join(fd.get_library_dir("objects"),HIDDEN_FOLDER_NAME,PULL_CATEGORY_NAME)
    pcoll = preview_collections["pulls"]
    return fd.get_previews(icon_dir,pcoll)

def enum_closet_accessories(self,context):
    if context is None:
        return []
    
    icon_dir = os.path.join(fd.get_library_dir("objects"),HIDDEN_FOLDER_NAME,CLOSET_ACCESSORY_CATEGORY_NAME)
    pcoll = preview_collections["closet_accessories"]
    return fd.get_previews(icon_dir,pcoll)

class OPERATOR_Update_All_Doors(bpy.types.Operator):
    """ This will clear all the spec groups to save on file size.
    """
    bl_idname = "lm_cabinet_closet_designer.update_all_doors"
    bl_label = "Update All Doors"
    bl_description = "This will update the project with the selected door styles"
    bl_options = {'UNDO'}
    
    cabinet_type = bpy.props.StringProperty(name = "Cabinet Type")
    
    def execute(self, context):
        g = context.scene.lm_cabinet_closet_designer
        doors = []
        for obj in context.scene.objects:
            if obj.mv.type == 'BPASSEMBLY':
                if self.cabinet_type == "Drawer":
                    if "Drawer Front" in obj.mv.name_object:
                        doors.append(obj)
                else:
                    if "Cabinet Door" in obj.mv.name_object and self.cabinet_type in obj.mv.name_object:
                        print("self.cabinet_type: ",self.cabinet_type)
                        print("obj.mv.name_object: ",obj.mv.name_object)
                        doors.append(obj)
                
        if self.cabinet_type == "Base":
            door_name = g.base_door_styles
        if self.cabinet_type == "Tall":
            door_name = g.tall_door_styles
        if self.cabinet_type == "Upper":
            door_name = g.upper_door_styles
        if self.cabinet_type == "Drawer":
            door_name = g.drawer_front_styles

        for door in doors:
            door_assembly = fd.Assembly(door)
            new_door = fd.get_assembly((HIDDEN_FOLDER_NAME,DOOR_LIBRARY_NAME,DOOR_CATEGORY_NAME),assembly_name=door_name)
            new_door.obj_bp.mv.name_object = door_assembly.obj_bp.mv.name_object
            new_door.obj_bp.parent = door_assembly.obj_bp.parent
            new_door.obj_bp.location = door_assembly.obj_bp.location
            new_door.obj_bp.rotation_euler = door_assembly.obj_bp.rotation_euler
            
            property_id = door_assembly.obj_bp.mv.property_id
            
            fd.copy_drivers(door_assembly.obj_bp,new_door.obj_bp)
            fd.copy_prompt_drivers(door_assembly.obj_bp,new_door.obj_bp)
            fd.copy_drivers(door_assembly.obj_x,new_door.obj_x)
            fd.copy_drivers(door_assembly.obj_y,new_door.obj_y)
            fd.copy_drivers(door_assembly.obj_z,new_door.obj_z)
            obj_list = []
            obj_list.append(door_assembly.obj_bp)
            for child in door_assembly.obj_bp.children:
                obj_list.append(child)
            fd.delete_obj_list(obj_list)
            
            new_door.obj_bp.mv.property_id = property_id
            for child in new_door.obj_bp.children:
                child.mv.property_id = property_id
                if child.type == 'EMPTY':
                    child.hide
                if child.type == 'MESH':
                    child.draw_type = 'TEXTURED'
                    fd.assign_materials_from_pointers(child)
                if child.mv.type == 'CAGE':
                    child.hide = True
                
        return {'FINISHED'}

class OPERATOR_Update_Door_Selection(bpy.types.Operator):
    """ This will clear all the spec groups to save on file size.
    """
    bl_idname = "lm_cabinet_closet_designer.update_door_selection"
    bl_label = "Update Door Selection"
    bl_description = "This will change the selected door with the active door"
    bl_options = {'UNDO'}
    
    cabinet_type = bpy.props.StringProperty(name = "Cabinet Type")
    
    @classmethod
    def poll(cls, context):
        obj = context.active_object
        obj_bp = fd.get_assembly_bp(obj)
        if obj_bp:
            assembly = fd.Assembly(obj_bp)
            if "Drawer Front" in assembly.obj_bp.mv.name_object:
                return True
            elif "Cabinet Door" in assembly.obj_bp.mv.name_object:
                return True
            elif "Hamper Door" in assembly.obj_bp.mv.name_object:
                return True
            elif "False Front" in assembly.obj_bp.mv.name_object:
                return True
            else:
                return False
        return False
            
    def execute(self, context):
        g = context.scene.lm_cabinet_closet_designer
        obj = context.active_object
        obj_bp = fd.get_assembly_bp(obj)
        door_assembly = fd.Assembly(obj_bp)
        
        if self.cabinet_type == "Base":
            door_name = g.base_door_styles
        if self.cabinet_type == "Tall":
            door_name = g.tall_door_styles
        if self.cabinet_type == "Upper":
            door_name = g.upper_door_styles
        if self.cabinet_type == "Drawer":
            door_name = g.drawer_front_styles

        new_door = fd.get_assembly((HIDDEN_FOLDER_NAME,DOOR_LIBRARY_NAME,DOOR_CATEGORY_NAME),assembly_name=door_name)
        new_door.obj_bp.mv.name_object = door_assembly.obj_bp.mv.name_object
        new_door.obj_bp.parent = door_assembly.obj_bp.parent
        new_door.obj_bp.location = door_assembly.obj_bp.location
        new_door.obj_bp.rotation_euler = door_assembly.obj_bp.rotation_euler
        
        property_id = door_assembly.obj_bp.mv.property_id

        fd.copy_drivers(door_assembly.obj_bp,new_door.obj_bp)
        fd.copy_prompt_drivers(door_assembly.obj_bp,new_door.obj_bp)
        fd.copy_drivers(door_assembly.obj_x,new_door.obj_x)
        fd.copy_drivers(door_assembly.obj_y,new_door.obj_y)
        fd.copy_drivers(door_assembly.obj_z,new_door.obj_z)
        obj_list = []
        obj_list.append(door_assembly.obj_bp)
        for child in door_assembly.obj_bp.children:
            obj_list.append(child)
        fd.delete_obj_list(obj_list)

        new_door.obj_bp.mv.property_id = property_id
        for child in new_door.obj_bp.children:
            child.mv.property_id = property_id
            if child.type == 'EMPTY':
                child.hide
            if child.type == 'MESH':
                child.draw_type = 'TEXTURED'
                fd.assign_materials_from_pointers(child)
            if child.mv.type == 'CAGE':
                child.hide = True

        return {'FINISHED'}

class OPERATOR_Update_Pulls(bpy.types.Operator):
    bl_idname = "lm_cabinet_closet_designer.update_pulls"
    bl_label = "Change Pulls"
    bl_description = "This will update all of the doors pulls with the active pull"
    bl_options = {'UNDO'}
    
    cabinet_type = bpy.props.StringProperty(name = "Cabinet Type")

    def execute(self, context):
        g = context.scene.lm_cabinet_closet_designer
        pulls = []
        for obj in context.scene.objects:
            if self.cabinet_type + " Cabinet Pull" in obj.mv.name_object:
                pulls.append(obj)
                
        if self.cabinet_type == "Base":
            pull_name = g.base_pull_name
        if self.cabinet_type == "Tall":
            pull_name = g.tall_pull_name
        if self.cabinet_type == "Upper":
            pull_name = g.upper_pull_name
        if self.cabinet_type == "Drawer":
            pull_name = g.drawer_pull_name
        
        for pull in pulls:
            pull_assembly = fd.Assembly(fd.get_assembly_bp(pull))
            pull_length = pull_assembly.get_prompt("Pull Length")
            new_pull = fd.get_object((HIDDEN_FOLDER_NAME,PULL_CATEGORY_NAME),pull_name)
            new_pull.mv.name_object = pull.mv.name_object
            new_pull.parent = pull.parent
            new_pull.location = pull.location
            new_pull.rotation_euler = pull.rotation_euler
            fd.assign_materials_from_pointers(new_pull)
            pull_length.set_value(new_pull.dimensions.x)
            fd.copy_drivers(pull,new_pull)
            
        fd.delete_obj_list(pulls)
        return {'FINISHED'}

class OPERATOR_Update_Materials(bpy.types.Operator):
    bl_idname = "lm_cabinet_closet_designer.update_materials"
    bl_label = "Update Materials for Closet"
    bl_description = "This will update all of the materials for the scene"
    bl_options = {'UNDO'}
    
    cabinet_type = bpy.props.StringProperty(name = "Cabinet Type")

    def execute(self, context):
        g = context.scene.lm_cabinet_closet_designer
        
        for spec_group in bpy.context.scene.cabinetlib.spec_groups:
            
            edge_pointers = []
            surface_pointers = []
            
            surface_pointers.append(spec_group.materials["Exposed_Exterior_Surface"])
            surface_pointers.append(spec_group.materials["Exposed_Interior_Surface"])
            surface_pointers.append(spec_group.materials["Semi_Exposed_Surface"])
            surface_pointers.append(spec_group.materials["Door_Surface"])
            surface_pointers.append(spec_group.materials["Cabinet_Moldings"])
            
            edge_pointers.append(spec_group.materials["Door_Edge"])
            edge_pointers.append(spec_group.materials["Exposed_Exterior_Edge"])
            edge_pointers.append(spec_group.materials["Exposed_Interior_Edge"])
            edge_pointers.append(spec_group.materials["Semi_Exposed_Edge"])
            
            if g.surface_material_types == 'SOLID':
                surface_category = CLOSET_SOLID_MATERIAL_CATEGORY_NAME
                surface_material = g.closet_solid_surface_materials
            else:
                surface_category = CLOSET_WOOD_MATERIAL_CATEGORY_NAME
                surface_material = g.closet_wood_surface_materials
            
            if g.edge_material_types == 'SOLID':
                edge_category = CLOSET_SOLID_MATERIAL_CATEGORY_NAME
                edge_material = g.closet_solid_edge_materials
            else:
                edge_category = CLOSET_WOOD_MATERIAL_CATEGORY_NAME
                edge_material = g.closet_wood_edge_materials
                
            for s_pointer in surface_pointers:
                s_pointer.library_name = CLOSET_MATERIAL_LIBRARY_NAME
                s_pointer.category_name = surface_category
                s_pointer.item_name = surface_material
            
            for e_pointer in edge_pointers:
                e_pointer.library_name = CLOSET_MATERIAL_LIBRARY_NAME
                e_pointer.category_name = edge_category
                e_pointer.item_name = edge_material
                
            bpy.ops.cabinetlib.update_scene_from_pointers()
            
        return {'FINISHED'}

class OPERATOR_Update_Columns(bpy.types.Operator):
    bl_idname = "lm_cabinet_closet_designer.update_columns"
    bl_label = "Update Columns"
    bl_description = "This will update the project with the selected column style"
    bl_options = {'UNDO'}
    
    column_type = bpy.props.StringProperty(name = "Column Type")    
    
    def execute(self, context):
        g = context.scene.lm_cabinet_closet_designer
        columns = []
        for obj in context.scene.objects:
            if obj.mv.type == 'BPASSEMBLY':
                if "Column Style" in obj.mv.name_object and self.column_type in obj.mv.name_object:
                    columns.append(obj)
            
        if self.column_type == "Base":
            column_name = g.base_column_styles
        if self.column_type == "Tall":
            column_name = g.tall_column_styles
        if self.column_type == "Upper":
            column_name = g.upper_column_styles
            
        for column in columns:
            column_assembly = fd.Assembly(column)
            new_column = fd.get_assembly((HIDDEN_FOLDER_NAME,COLUMN_LIBRARY_NAME,COLUMN_CATEGORY_NAME),assembly_name=column_name)
            new_column.obj_bp.mv.name_object = column_assembly.obj_bp.mv.name_object
            new_column.obj_bp.parent = column_assembly.obj_bp.parent
            new_column.obj_bp.location = column_assembly.obj_bp.location
            new_column.obj_bp.rotation_euler = column_assembly.obj_bp.rotation_euler
            
            property_id = column_assembly.obj_bp.mv.property_id
            
            fd.copy_drivers(column_assembly.obj_bp,new_column.obj_bp)
            fd.copy_prompt_drivers(column_assembly.obj_bp,new_column.obj_bp)
            fd.copy_drivers(column_assembly.obj_x,new_column.obj_x)
            fd.copy_drivers(column_assembly.obj_y,new_column.obj_y)
            fd.copy_drivers(column_assembly.obj_z,new_column.obj_z)
            obj_list = []
            obj_list.append(column_assembly.obj_bp)
            for child in column_assembly.obj_bp.children:
                obj_list.append(child)
            fd.delete_obj_list(obj_list)
            
            new_column.obj_bp.mv.property_id = property_id
            for child in new_column.obj_bp.children:
                child.mv.property_id = property_id
                if child.type == 'EMPTY':
                    child.hide
                if child.type == 'MESH':
                    child.draw_type = 'TEXTURED'
                    fd.assign_materials_from_pointers(child)
                if child.mv.type == 'CAGE':
                    child.hide = True            
        
        return {'FINISHED'}    
        
class OPERATOR_Update_Column_Selection(bpy.types.Operator):
    bl_idname = "lm_cabinet_closet_designer.update_column_selection"
    bl_label = "Update Column"
    bl_description = "This will change the selected column style with the active column style"
    bl_options = {'UNDO'}     
    
    column_type = bpy.props.StringProperty(name = "Column Type")
    
    @classmethod
    def poll(cls, context):
        obj = context.active_object
        obj_bp = fd.get_assembly_bp(obj)
        if obj_bp:
            assembly = fd.Assembly(obj_bp)
            if "Column Style" in assembly.obj_bp.mv.name_object:
                return True
            else:
                return False
        return False
            
    def execute(self, context):
        g = context.scene.lm_cabinet_closet_designer
        obj = context.active_object
        obj_bp = fd.get_assembly_bp(obj)
        column_assembly = fd.Assembly(obj_bp)      
                
        if self.column_type == "Base":
            column_name = g.base_column_styles
        if self.column_type == "Tall":
            column_name = g.tall_column_styles
        if self.column_type == "Upper":
            column_name = g.upper_column_styles

        new_column = fd.get_assembly((HIDDEN_FOLDER_NAME,COLUMN_LIBRARY_NAME,COLUMN_CATEGORY_NAME),assembly_name=column_name)
        new_column.obj_bp.mv.name_object = column_assembly.obj_bp.mv.name_object
        new_column.obj_bp.parent = column_assembly.obj_bp.parent
        new_column.obj_bp.location = column_assembly.obj_bp.location
        new_column.obj_bp.rotation_euler = column_assembly.obj_bp.rotation_euler
        
        property_id = column_assembly.obj_bp.mv.property_id

        fd.copy_drivers(column_assembly.obj_bp,new_column.obj_bp)
        fd.copy_prompt_drivers(column_assembly.obj_bp,new_column.obj_bp)
        fd.copy_drivers(column_assembly.obj_x,new_column.obj_x)
        fd.copy_drivers(column_assembly.obj_y,new_column.obj_y)
        fd.copy_drivers(column_assembly.obj_z,new_column.obj_z)
        obj_list = []
        obj_list.append(column_assembly.obj_bp)
        for child in column_assembly.obj_bp.children:
            obj_list.append(child)
        fd.delete_obj_list(obj_list)

        new_column.obj_bp.mv.property_id = property_id
        for child in new_column.obj_bp.children:
            child.mv.property_id = property_id
            if child.type == 'EMPTY':
                child.hide
            if child.type == 'MESH':
                child.draw_type = 'TEXTURED'
                fd.assign_materials_from_pointers(child)
            if child.mv.type == 'CAGE':
                child.hide = True

        return {'FINISHED'}
        
class OPERATOR_Place_Applied_Panel(bpy.types.Operator):
    bl_idname = "lm_cabinet_closet_designer.place_applied_panel"
    bl_label = "Place Applied Panel"
    bl_description = "This will allow you to place the active panel on cabinets and closets for an applied panel"
    bl_options = {'UNDO'}
    
    #READONLY
    filepath = bpy.props.StringProperty(name="Material Name")
    type_insert = bpy.props.StringProperty(name="Type Insert")
    
    item_name = None
    dir_name = ""
    
    assembly = None
    
    cages = []
    
    def get_panel(self,context):
        g = context.scene.lm_cabinet_closet_designer
        self.assembly = fd.get_assembly((HIDDEN_FOLDER_NAME,DOOR_LIBRARY_NAME,DOOR_CATEGORY_NAME),assembly_name=g.applied_panels)
        
    def set_xray(self,turn_on=True):
        cages = []
        for child in self.assembly.obj_bp.children:
            child.show_x_ray = turn_on
            if turn_on:
                child.draw_type = 'WIRE'
            else:
                if child.mv.type == 'CAGE':
                    cages.append(child)
                child.draw_type = 'TEXTURED'
                fd.assign_materials_from_pointers(child)
        fd.delete_obj_list(cages)

    def invoke(self, context, event):
        self.get_panel(context)
        context.window.cursor_set('PAINT_BRUSH')
        context.scene.update() # THE SCENE MUST BE UPDATED FOR RAY CAST TO WORK
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def cancel_drop(self,context,event):
        if self.assembly:
            fd.delete_object_and_children(self.assembly.obj_bp)
        bpy.context.window.cursor_set('DEFAULT')
        fd.delete_obj_list(self.cages)
        return {'FINISHED'}

    def add_to_left(self,part,product):
        self.assembly.obj_bp.parent = product.obj_bp
        
        toe_kick_height = 0
        if product.get_prompt('Toe Kick Height'):
            toe_kick_height = product.get_prompt('Toe Kick Height')
        
        if product.obj_z.location.z > 0:
            self.assembly.obj_bp.location = (0,0,toe_kick_height)
        else:
            self.assembly.obj_bp.location = (0,0,product.obj_z.location.z)
        
        self.assembly.obj_bp.rotation_euler = (0,math.radians(-90),0)
        self.assembly.obj_x.location.x = math.fabs(product.obj_z.location.z) - toe_kick_height
        self.assembly.obj_y.location.y = product.obj_y.location.y
    
    def add_to_right(self,part,product):
        self.assembly.obj_bp.parent = product.obj_bp
        
        toe_kick_height = 0
        if product.get_prompt('Toe Kick Height'):
            toe_kick_height = product.get_prompt('Toe Kick Height')
        
        if product.obj_z.location.z > 0:
            self.assembly.obj_bp.location = (product.obj_x.location.x,0,toe_kick_height)
        else:
            self.assembly.obj_bp.location = (product.obj_x.location.x,0,product.obj_z.location.z)
            
        self.assembly.obj_bp.rotation_euler = (0,math.radians(-90),math.radians(180))
        self.assembly.obj_x.location.x = math.fabs(product.obj_z.location.z) - toe_kick_height
        self.assembly.obj_y.location.y = math.fabs(product.obj_y.location.y)
        
    def add_to_back(self,part,product):
        self.assembly.obj_bp.parent = product.obj_bp
        
        toe_kick_height = 0
        if product.get_prompt('Toe Kick Height'):
            toe_kick_height = product.get_prompt('Toe Kick Height')
        
        if product.obj_z.location.z > 0:
            self.assembly.obj_bp.location = (0,0,toe_kick_height)
        else:
            self.assembly.obj_bp.location = (0,0,product.obj_z.location.z)
            
        self.assembly.obj_bp.rotation_euler = (0,math.radians(-90),math.radians(-90))
        self.assembly.obj_x.location.x = math.fabs(product.obj_z.location.z) - toe_kick_height
        self.assembly.obj_y.location.y = product.obj_x.location.x
    
    def door_panel_drop(self,context,event):
        selected_point, selected_obj = fd.get_selection_point(context,event,objects=self.cages)
        bpy.ops.object.select_all(action='DESELECT')
        sel_product_bp = fd.get_bp(selected_obj,'PRODUCT')
        sel_assembly_bp = fd.get_assembly_bp(selected_obj)

        if sel_product_bp and sel_assembly_bp:
            product = fd.Library_Assembly(sel_product_bp)
            assembly = fd.Assembly(sel_assembly_bp)
            if product and assembly and 'Door' not in assembly.obj_bp.mv.name_object:
                self.assembly.obj_bp.parent = None
                if product.placement_type == 'Corner':
                    pass
                    #TODO: IMPLEMENT CORNER PLACEMENT
                else:
                    if 'Left' in assembly.obj_bp.mv.name_object:
                        self.add_to_left(assembly,product)
                    if 'Right' in assembly.obj_bp.mv.name_object:
                        self.add_to_right(assembly,product)
                    if 'Back' in assembly.obj_bp.mv.name_object:
                        self.add_to_back(assembly,product)
        else:
            self.assembly.obj_bp.parent = None
            self.assembly.obj_bp.location = selected_point

        if event.type == 'LEFTMOUSE' and event.value == 'PRESS':
            self.set_xray(False)
            fd.delete_obj_list(self.cages)
            bpy.context.window.cursor_set('DEFAULT')
            if event.shift:
                self.get_panel(context)
            else:
                bpy.ops.object.select_all(action='DESELECT')
                context.scene.objects.active = self.assembly.obj_bp
                self.assembly.obj_bp.select = True
                return {'FINISHED'}
        
        return {'RUNNING_MODAL'}
    
    def modal(self, context, event):
        context.area.tag_redraw()
        
        if event.type in {'MIDDLEMOUSE', 'WHEELUPMOUSE', 'WHEELDOWNMOUSE'}:
            return {'PASS_THROUGH'}
        
        if event.type in {'ESC'}:
            self.cancel_drop(context,event)
            return {'FINISHED'}    
        
        return self.door_panel_drop(context,event)

class OPERATOR_Place_Accessory(bpy.types.Operator):
    bl_idname = "lm_cabinet_closet_designer.place_accessory"
    bl_label = "Place Accessory"
    bl_options = {'UNDO'}
    
    #READONLY
    filepath = bpy.props.StringProperty(name="Material Name")
    
    item_name = None
    dir_name = ""
    
    obj = None
    
    cages = []
    
    header_text = "Place Object   (Esc, Right Click) = Cancel Command  :  (Left Click) = Place Object"
    
    def __del__(self):
        bpy.context.area.header_text_set()
    
    def get_object(self,context):
        g = context.scene.lm_cabinet_closet_designer
        self.obj = fd.get_object((HIDDEN_FOLDER_NAME,CLOSET_ACCESSORY_CATEGORY_NAME),g.closet_accessory)
        
    def invoke(self, context, event):
        self.get_object(context)
        self.obj.draw_type = 'WIRE'
        context.window.cursor_set('PAINT_BRUSH')
        context.scene.update() # THE SCENE MUST BE UPDATED FOR RAY CAST TO WORK
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def cancel_drop(self,context,event):
        objs  = []
        objs.append(self.obj)
        fd.delete_obj_list(objs)
        bpy.context.window.cursor_set('DEFAULT')
        return {'FINISHED'}

    def object_drop(self,context,event):
        selected_point, selected_obj = fd.get_selection_point(context,event)
        bpy.ops.object.select_all(action='DESELECT')
        obj_bp = fd.get_assembly_bp(selected_obj)
        wall_bp = fd.get_wall_bp(selected_obj)
        
        if wall_bp:
            self.obj.rotation_euler.z = wall_bp.rotation_euler.z
        
        elif obj_bp:
            
            ass = fd.Assembly(obj_bp)
            ass_world_loc = (ass.obj_bp.matrix_world[0][3],
                             ass.obj_bp.matrix_world[1][3],
                             ass.obj_bp.matrix_world[2][3])
            
            ass_z_world_loc = (ass.obj_z.matrix_world[0][3],
                               ass.obj_z.matrix_world[1][3],
                               ass.obj_z.matrix_world[2][3])
            
            dist_to_bp = math.fabs(fd.calc_distance(selected_point,ass_world_loc))
            dist_to_z = math.fabs(fd.calc_distance(selected_point,ass_z_world_loc))
            
            if "Panel" in ass.obj_bp.mv.name_object:
                if dist_to_bp > dist_to_z:
                    self.obj.rotation_euler.y = math.radians(0)
                else:
                    self.obj.rotation_euler.y = math.radians(180)
                    
            if "Left Side" in ass.obj_bp.mv.name_object:
                if dist_to_bp > dist_to_z:
                    self.obj.rotation_euler.y = math.radians(180)
                else:
                    self.obj.rotation_euler.y = math.radians(0)
        
        self.obj.location = selected_point

        if event.type == 'LEFTMOUSE' and event.value == 'PRESS':
            self.obj.draw_type = 'TEXTURED'
            bpy.context.window.cursor_set('DEFAULT')
            fd.assign_materials_from_pointers(self.obj)
            context.scene.objects.active = self.obj
            self.obj.select = True
            return {'FINISHED'}

        return {'RUNNING_MODAL'}

    def modal(self, context, event):
        context.area.tag_redraw()
        context.area.header_text_set(text=self.header_text)
        
        if event.type in {'MIDDLEMOUSE', 'WHEELUPMOUSE', 'WHEELDOWNMOUSE'}:
            return {'PASS_THROUGH'}
        
        if event.type in {'ESC'}:
            self.cancel_drop(context,event)
            return {'FINISHED'}
        
        return self.object_drop(context,event)

class OPERATOR_Update_Pricing(bpy.types.Operator):
    bl_idname = "lm_cabinet_closet_designer.update_pricing"
    bl_label = "Update Pricing"
    bl_description = "This will update all of the pricing"
    bl_options = {'UNDO'}
    
    def reset_values(self,g):
        g.total_price = 0
        g.cam_qty = 0
        g.hinge_qty = 0
        g.pull_qty = 0
        g.drawer_slide_qty = 0
        g.shelf_pin_qty = 0
        g.material_amount = 0
        g.hanging_amount = 0

    def calculate_totals(self,g):
        cam_total = g.price_per_cam * g.cam_qty
        hinge_total = g.price_per_hinge * g.hinge_qty
        pull_total = g.price_per_pull * g.pull_qty
        slide_total = g.price_per_drawer_slide * g.drawer_slide_qty
        pin_total = g.price_per_shelf_pin * g.shelf_pin_qty
        rod_total = g.price_per_ln_unit_of_rods * fd.unit(g.hanging_amount)
        material_total = g.price_per_sq_unit_of_material * (g.material_amount/144)
        
        g.material_cost = material_total
        g.hardware_cost = hinge_total + pull_total + slide_total + pin_total + rod_total + cam_total
        g.total_price = cam_total + hinge_total + pull_total + slide_total + pin_total + rod_total + material_total
        
    def execute(self, context):
        g = context.scene.lm_cabinet_closet_designer
        self.reset_values(g)
        for obj in context.scene.objects:
            if obj.mv.type == 'BPASSEMBLY':
                assembly = fd.Assembly(obj)
                hide_prompt = assembly.get_prompt("Hide")
                
                if hide_prompt:
                    if hide_prompt.value() == False:
                        cam_qty_prompt = assembly.get_prompt("Cam Quantity")
                        hinge_qty_prompt = assembly.get_prompt("Hinge Quantity")
                        pull_qty_prompt = assembly.get_prompt("Pull Quantity")
                        drw_slide_qty_prompt = assembly.get_prompt("Drawer Slide Quantity")
                        hanging_rod_qty_prompt = assembly.get_prompt("Hanging Rod Qty")
                        shelf_pin_qty_prompt = assembly.get_prompt("Shelf Pin Quantity")
                        
                        for child in assembly.obj_bp.children:
                            if child.cabinetlib.type_mesh == 'CUTPART':
                                g.material_amount += math.fabs(fd.unit(assembly.obj_x.location.x)) * math.fabs(fd.unit(assembly.obj_y.location.y))
                                break
                        
                        if cam_qty_prompt:
                            g.cam_qty += cam_qty_prompt.value()
                            
                        if pull_qty_prompt:
                            g.pull_qty += pull_qty_prompt.value()
                            
                        if hinge_qty_prompt:
                            g.hinge_qty += hinge_qty_prompt.value()
                            
                        if drw_slide_qty_prompt:
                            g.drawer_slide_qty += drw_slide_qty_prompt.value()
                            
                        if hanging_rod_qty_prompt:
                            g.hanging_amount += hanging_rod_qty_prompt.value() / 12
                            
                        if shelf_pin_qty_prompt:
                            g.shelf_pin_qty += shelf_pin_qty_prompt.value()
                        
        self.calculate_totals(g)
        return {'FINISHED'}

def set_room_prop(name,value):
    properties = bpy.context.scene.mv.project_properties
    if name in properties:
        prop = properties[name]
        prop.value = str(value)
    else:
        prop = properties.add()
        prop.name = name
        prop.value = str(value)

@persistent
def set_room_properties(scene=None):
    scene = bpy.context.scene
    g = scene.lm_cabinet_closet_designer
    properties = scene.mv.project_properties
    for prop in properties:
        properties.remove(0)
    bpy.ops.closet_designer.update_pricing()
    set_room_prop("Total Price",round(g.total_price,2))
    set_room_prop("Material (Square Footage)",round(g.material_amount/144,2))
    set_room_prop("Material Cost",round(g.material_cost,2))
    set_room_prop("Hardware Cost",round(g.hardware_cost,2))
    set_room_prop("Closet Rod Quantity (Linear Footage)",round(fd.unit(g.hanging_amount),2))
    set_room_prop("Closet Pull Quantity",g.pull_qty)
    set_room_prop("Closet Hinge Quantity",g.hinge_qty)
    set_room_prop("Closet Cam Quantity",g.cam_qty)
    set_room_prop("Closet Drawer Slide Quantity",g.drawer_slide_qty)
    set_room_prop("Closet Shelf Pin Quantity",g.shelf_pin_qty)

bpy.app.handlers.save_pre.append(set_room_properties)

class PROPERTIES_Scene_Properties(bpy.types.PropertyGroup):
    
    main_tabs = bpy.props.EnumProperty(name="Main Tabs",
                                       items=[('DEFAULTS',"Defaults",'Setup the default sizes and options for the products'),
                                              ('OPTIONS',"Options",'Show the available Cabinet & Closet Options'),
                                              ('PRICE',"Price",'Show the price of the closet')],
                                       default = 'DEFAULTS')
    
    defaults_tabs = bpy.props.EnumProperty(name="Main Tabs",
                                           items=[('CLOSETS',"Closets",'Setup the default closet settings'),
                                                  ('FRAMELESS',"Frameless",'Show the default Frameless cabinet settings'),
                                                  ('FACEFRAME',"Face Frame",'Show the default Face Frame cabinet settings'),
                                                  ('CARCASS',"Carcass",'Show the default carcass settings'),
                                                  ('EXTERIOR',"Exterior",'Show the default door and drawer settings')],
                                           default = 'CLOSETS')
    
    #ENUMERATORS
    base_moldings = bpy.props.EnumProperty(name="Base Molding",items=enum_base_molding)
    crown_moldings = bpy.props.EnumProperty(name="Crown Molding",items=enum_crown_molding)
    base_door_styles = bpy.props.EnumProperty(name="Base Door Styles",items=enum_door_styles)
    tall_door_styles = bpy.props.EnumProperty(name="Tall Door Styles",items=enum_door_styles)
    upper_door_styles = bpy.props.EnumProperty(name="Upper Door Styles",items=enum_door_styles)
    drawer_front_styles = bpy.props.EnumProperty(name="Drawer Front Styles",items=enum_door_styles)
    base_column_styles = bpy.props.EnumProperty(name="Base Column Styles",items=enum_column_styles)
    tall_column_styles = bpy.props.EnumProperty(name="Tall Column Styles",items=enum_column_styles)
    upper_column_styles = bpy.props.EnumProperty(name="Upper Column Styles",items=enum_column_styles)
    applied_panels = bpy.props.EnumProperty(name="Applied Panels",items=enum_door_styles)
    closet_accessory = bpy.props.EnumProperty(name="Closet Accessory",items=enum_closet_accessories)
    closet_wood_surface_materials = bpy.props.EnumProperty(name="Closet Wood Surface Materials",items=enum_closet_wood_materials)
    closet_wood_edge_materials = bpy.props.EnumProperty(name="Closet Wood Edge Materials",items=enum_closet_wood_materials)
    closet_solid_surface_materials = bpy.props.EnumProperty(name="Closet Solid Surface Materials",items=enum_closet_solid_materials)
    closet_solid_edge_materials = bpy.props.EnumProperty(name="Closet Solid Edge Materials",items=enum_closet_solid_materials)
    base_pull_name = bpy.props.EnumProperty(name="Base Pull Name",items=enum_pulls)
    tall_pull_name = bpy.props.EnumProperty(name="Tall Pull Name",items=enum_pulls)
    upper_pull_name = bpy.props.EnumProperty(name="Upper Pull Name",items=enum_pulls)
    drawer_pull_name = bpy.props.EnumProperty(name="Drawer Pull Name",items=enum_pulls)
    
    expand_crown_molding = bpy.props.BoolProperty(name="Expand Crown Molding")
    expand_base_molding = bpy.props.BoolProperty(name="Expand Base Molding")
    expand_surface_material = bpy.props.BoolProperty(name="Expand Surface Material")
    expand_edge_material = bpy.props.BoolProperty(name="Expand Edge Material")
    expand_base_pull = bpy.props.BoolProperty(name="Expand Base Pull")
    expand_tall_pull = bpy.props.BoolProperty(name="Expand Tall Pull")
    expand_upper_pull = bpy.props.BoolProperty(name="Expand Upper Pull")
    expand_drawer_pull = bpy.props.BoolProperty(name="Expand Drawer Pull")
    expand_base_door = bpy.props.BoolProperty(name="Expand Base Door")
    expand_tall_door = bpy.props.BoolProperty(name="Expand Tall Door")
    expand_upper_door = bpy.props.BoolProperty(name="Expand Upper Door")
    expand_drawer_front = bpy.props.BoolProperty(name="Expand Drawer Front")
    expand_base_column = bpy.props.BoolProperty(name="Expand Base Column")
    expand_tall_column = bpy.props.BoolProperty(name="Expand Tall Column")
    expand_upper_column = bpy.props.BoolProperty(name="Expand Upper Column")
    expand_applied_panel = bpy.props.BoolProperty(name="Expand Applied Panel")
    expand_closet_accessory = bpy.props.BoolProperty(name="Expand Closet Accessory")
    
    total_price = bpy.props.FloatProperty(name="Total Price",default=0)
    
    cam_qty = bpy.props.IntProperty(name="Cam Quantity")
    screw_qty = bpy.props.IntProperty(name="Screw Quantity")
    hinge_qty = bpy.props.IntProperty(name="Hinge Quantity")
    pull_qty = bpy.props.IntProperty(name="Pull Quantity")
    drawer_slide_qty = bpy.props.IntProperty(name="Drawer Slide Quantity")
    shelf_pin_qty = bpy.props.IntProperty(name="Shelf Pin Quantity")
    material_cost = bpy.props.FloatProperty(name="Material Cost")
    hardware_cost = bpy.props.FloatProperty(name="Hardware Cost")
    material_amount = bpy.props.FloatProperty(name="Material Sq Unit Amount")
    hanging_amount = bpy.props.FloatProperty(name="Hanging Amount")
    price_per_cam = bpy.props.FloatProperty(name="Price Per Cam",precision=2,default=.35)
    price_per_pull = bpy.props.FloatProperty(name="Price Per Pull",precision=2,default=6.25)
    price_per_hinge = bpy.props.FloatProperty(name="Price Per Hinge",precision=2,default=4.99)
    price_per_drawer_slide = bpy.props.FloatProperty(name="Price Per Drawer Slide",precision=2,default=18)
    price_per_shelf_pin = bpy.props.FloatProperty(name="Price Per Shelf Pin",precision=2,default=.2)
    price_per_ln_unit_of_rods = bpy.props.FloatProperty(name="Price Per linear Unit of Hanging Rods",precision=2,default=20)
    price_per_sq_unit_of_material = bpy.props.FloatProperty(name="Price Per Square Unit of Material",precision=2,default=1.5)
    
    surface_material_types = bpy.props.EnumProperty(name="Surface Material Type",
                                                    items=[('SOLID',"Solid",'Solid Materials'),
                                                           ('GRAIN',"Wood Grain",'Wood Grain Material')],
                                                    default = 'SOLID')
    
    edge_material_types = bpy.props.EnumProperty(name="Edge Material Type",
                                                 items=[('SOLID',"Solid",'Solid Materials'),
                                                        ('GRAIN',"Wood Grain",'Wood Grain Material')],
                                                 default = 'SOLID')
    
    def draw_molding_options(self,layout):
        molding_box = layout.box()
        row = molding_box.row(align=True)
        row = row.split(.6)
        row.label("Moldings Options:")
        row = molding_box.row(align=True)
        row.prop(self,'expand_crown_molding',text="",icon='TRIA_DOWN' if self.expand_crown_molding else 'TRIA_RIGHT',emboss=False)
        row.prop(self,'crown_moldings',text="Crown Molding")
        row.operator('moldings.auto_add_molding',text="",icon='ZOOMIN').molding_type = 'Crown'
        row.operator('moldings.delete_molding',text="",icon='X').molding_type = 'Crown'
        if self.expand_crown_molding:
            row = molding_box.row()
            row.label(text="",icon='BLANK1')
            row.template_icon_view(self,"crown_moldings",show_labels=True)
        row = molding_box.row(align=True)
        row.prop(self,'expand_base_molding',text="",icon='TRIA_DOWN' if self.expand_base_molding else 'TRIA_RIGHT',emboss=False)
        row.prop(self,'base_moldings',text="Base Molding")
        row.operator('moldings.auto_add_molding',text="",icon='ZOOMIN').molding_type = 'Base'
        row.operator('moldings.delete_molding',text="",icon='X').molding_type = 'Base'
        if self.expand_base_molding:
            row = molding_box.row()
            row.label(text="",icon='BLANK1')
            row.template_icon_view(self,"base_moldings",show_labels=True)
            
    def draw_hardware_options(self,layout):
        #IMPLEMENT CHANGING HINGES GLOBALLY
        #IMPLEMENT CHANGING DRAWER SLIDES GLOBALLY
        hardware_box = layout.box()
        hardware_box.label("Hardware Options:")
        
        row = hardware_box.row(align=True)
        row.prop(self,'expand_base_pull',text="",icon='TRIA_DOWN' if self.expand_base_pull else 'TRIA_RIGHT',emboss=False)
        row.prop(self,'base_pull_name',text="Base Pull")
        row.operator('lm_cabinet_closet_designer.update_pulls',text="",icon='FILE_REFRESH').cabinet_type = 'Base'
        if self.expand_base_pull:
            row = hardware_box.row()
            row.label(text="",icon='BLANK1')
            row.template_icon_view(self,"base_pull_name",show_labels=True)
            
        row = hardware_box.row(align=True)
        row.prop(self,'expand_tall_pull',text="",icon='TRIA_DOWN' if self.expand_tall_pull else 'TRIA_RIGHT',emboss=False)
        row.prop(self,'tall_pull_name',text="Tall Pull")
        row.operator('lm_cabinet_closet_designer.update_pulls',text="",icon='FILE_REFRESH').cabinet_type = 'Tall'
        if self.expand_tall_pull:
            row = hardware_box.row()
            row.label(text="",icon='BLANK1')
            row.template_icon_view(self,"tall_pull_name",show_labels=True)
            
        row = hardware_box.row(align=True)
        row.prop(self,'expand_upper_pull',text="",icon='TRIA_DOWN' if self.expand_upper_pull else 'TRIA_RIGHT',emboss=False)
        row.prop(self,'upper_pull_name',text="Upper Pull")
        row.operator('lm_cabinet_closet_designer.update_pulls',text="",icon='FILE_REFRESH').cabinet_type = 'Upper'
        if self.expand_upper_pull:
            row = hardware_box.row()
            row.label(text="",icon='BLANK1')
            row.template_icon_view(self,"upper_pull_name",show_labels=True)
            
        row = hardware_box.row(align=True)
        row.prop(self,'expand_drawer_pull',text="",icon='TRIA_DOWN' if self.expand_drawer_pull else 'TRIA_RIGHT',emboss=False)
        row.prop(self,'drawer_pull_name',text="Drawer Pull")
        row.operator('lm_cabinet_closet_designer.update_pulls',text="",icon='FILE_REFRESH').cabinet_type = 'Drawer'
        if self.expand_drawer_pull:
            row = hardware_box.row()
            row.label(text="",icon='BLANK1')
            row.template_icon_view(self,"drawer_pull_name",show_labels=True)
            
    def draw_material_options(self,layout):
        #IMPLEMENT CHANGING ROD MATERIAL
        #IMPLEMENT CHANGING BASKET MATERIAL
        #IMPLEMENT CHANGING DRAWER BOX MATERIAL
        material_box = layout.box()
        material_box.label("Material Selection:")
        
        row = material_box.row(align=True)
        row.prop(self,'expand_surface_material',text="",icon='TRIA_DOWN' if self.expand_surface_material else 'TRIA_RIGHT',emboss=False)
        row.label('Surface:')
        row.prop(self,'surface_material_types',text="",icon='FILE_FOLDER')
        if self.surface_material_types == 'GRAIN':
            row.prop(self,'closet_wood_surface_materials',text="")
        else:
            row.prop(self,'closet_solid_surface_materials',text="")
        row.operator('lm_cabinet_closet_designer.update_materials',text="",icon='FILE_REFRESH')
        if self.expand_surface_material:
            row = material_box.row()
            row.label(text="",icon='BLANK1')
            if self.surface_material_types == 'GRAIN':
                row.template_icon_view(self,"closet_wood_surface_materials",show_labels=True)
            else:
                row.template_icon_view(self,"closet_solid_surface_materials",show_labels=True)
            
        if self.expand_drawer_pull:
            row = material_box.row()
            row.label(text="",icon='BLANK1')
            row.template_icon_view(self,"drawer_pull_name",show_labels=True)
            
        row = material_box.row(align=True)
        row.prop(self,'expand_edge_material',text="",icon='TRIA_DOWN' if self.expand_edge_material else 'TRIA_RIGHT',emboss=False)
        row.label('Edge:')
        row.prop(self,'edge_material_types',text="",icon='FILE_FOLDER')
        if self.edge_material_types == 'GRAIN':
            row.prop(self,'closet_wood_edge_materials',text="")
        else:
            row.prop(self,'closet_solid_edge_materials',text="")
        row.operator('lm_cabinet_closet_designer.update_materials',text="",icon='FILE_REFRESH')   
        if self.expand_edge_material:
            row = material_box.row()
            row.label(text="",icon='BLANK1')
            if self.surface_material_types == 'GRAIN':
                row.template_icon_view(self,"closet_wood_edge_materials",show_labels=True)
            else:
                row.template_icon_view(self,"closet_solid_edge_materials",show_labels=True)
                
    def draw_door_style_options(self,layout):
        door_style_box = layout.box()
        door_style_box.label("Door Drawer Styles:")
        row = door_style_box.row(align=True)
        row.prop(self,'expand_base_door',text="",icon='TRIA_DOWN' if self.expand_base_door else 'TRIA_RIGHT',emboss=False)
        row.prop(self,'base_door_styles',text="Base Door Style")
        row.operator('lm_cabinet_closet_designer.update_all_doors',text="",icon='FILE_REFRESH').cabinet_type = "Base"
        row.operator('lm_cabinet_closet_designer.update_door_selection',text="",icon='MAN_TRANS').cabinet_type = "Base"
        if self.expand_base_door:
            row = door_style_box.row()
            row.label(text="",icon='BLANK1')
            row.template_icon_view(self,"base_door_styles",show_labels=True)
            
        row = door_style_box.row(align=True)
        row.prop(self,'expand_tall_door',text="",icon='TRIA_DOWN' if self.expand_tall_door else 'TRIA_RIGHT',emboss=False)
        row.prop(self,'tall_door_styles',text="Tall Door Style")
        row.operator('lm_cabinet_closet_designer.update_all_doors',text="",icon='FILE_REFRESH').cabinet_type = "Tall"
        row.operator('lm_cabinet_closet_designer.update_door_selection',text="",icon='MAN_TRANS').cabinet_type = "Tall"
        if self.expand_tall_door:
            row = door_style_box.row()
            row.label(text="",icon='BLANK1')
            row.template_icon_view(self,"tall_door_styles",show_labels=True)
            
        row = door_style_box.row(align=True)
        row.prop(self,'expand_upper_door',text="",icon='TRIA_DOWN' if self.expand_upper_door else 'TRIA_RIGHT',emboss=False)
        row.prop(self,'upper_door_styles',text="Upper Door Style")
        row.operator('lm_cabinet_closet_designer.update_all_doors',text="",icon='FILE_REFRESH').cabinet_type = "Upper"
        row.operator('lm_cabinet_closet_designer.update_door_selection',text="",icon='MAN_TRANS').cabinet_type = "Upper"
        if self.expand_upper_door:
            row = door_style_box.row()
            row.label(text="",icon='BLANK1')
            row.template_icon_view(self,"upper_door_styles",show_labels=True)
            
        row = door_style_box.row(align=True)
        row.prop(self,'expand_drawer_front',text="",icon='TRIA_DOWN' if self.expand_drawer_front else 'TRIA_RIGHT',emboss=False)
        row.prop(self,'drawer_front_styles',text="Drawer Front Style")
        row.operator('lm_cabinet_closet_designer.update_all_doors',text="",icon='FILE_REFRESH').cabinet_type = "Drawer"
        row.operator('lm_cabinet_closet_designer.update_door_selection',text="",icon='MAN_TRANS').cabinet_type = "Drawer"
        if self.expand_drawer_front:
            row = door_style_box.row()
            row.label(text="",icon='BLANK1')
            row.template_icon_view(self,"drawer_front_styles",show_labels=True)
            
    def draw_pricing(self,layout):
        total_box = layout.box()
        col = total_box.column(align=True)
        row = col.row()
        row.label("Total Price:")
        row.label("$" + str(round(self.total_price,2)))
        row.operator('lm_cabinet_closet_designer.update_pricing',text="",icon='FILE_REFRESH')
        col.separator()
        row = col.row()
        row.label('Square Unit of Material:')
        row.label(str(round(self.material_amount/144,1)))
        row = col.row()
        row.label('Linear Unit of Hanging Rods: ')
        row.label(str(round(fd.unit(self.hanging_amount),1)))
        row = col.row()
        row.label('Cam Quantity:')
        row.label(str(self.cam_qty))
        row = col.row()
        row.label('Shelf Pin Quantity:')
        row.label(str(self.shelf_pin_qty))
        row = col.row()
        row.label('Drawer Slide Quantity (Pairs):')
        row.label(str(self.drawer_slide_qty))
        row = col.row()
        row.label('Hinge Quantity:')
        row.label(str(self.hinge_qty))
        row = col.row()
        row.label('Pull Quantity:')
        row.label(str(self.pull_qty))
        
    def draw_pricing_setup(self,layout):
        setup_box = layout.box()
        col = setup_box.column(align=True)
        row = col.row()
        row.label('Material Cost:')
        row.prop(self,'price_per_sq_unit_of_material',text="Square Foot Cost")
        row = col.row()
        row.label('Hanging Rod Cost:')
        row.prop(self,'price_per_ln_unit_of_rods',text="Linear Foot Cost")
        row = col.row()
        row.label('Cam Cost:')
        row.prop(self,'price_per_cam',text='Each Cost')
        row = col.row()
        row.label('Hinge Cost:')
        row.prop(self,'price_per_hinge',text='Each Cost')
        row = col.row()
        row.label('Pull Cost:')
        row.prop(self,'price_per_pull',text='Each Cost')
        row = col.row()
        row.label('Drawer Slide Cost:')
        row.prop(self,'price_per_drawer_slide',text='Pair Cost')
        row = col.row()
        row.label('Shelf Pin Cost:')
        row.prop(self,'price_per_shelf_pin',text='Each Cost')
        
    def draw_column_style_options(self,layout):
        columns_panel_box = layout.box()
        columns_panel_box.label("Columns Styles:")
        
        row = columns_panel_box.row(align=True)
        row.prop(self,'expand_base_column',text="",icon='TRIA_DOWN' if self.expand_base_column else 'TRIA_RIGHT',emboss=False)
        row.prop(self,'base_column_styles',text="Base Column Style")
        row.operator('lm_cabinet_closet_designer.update_columns',text="",icon='FILE_REFRESH').column_type = "Base"
        row.operator('lm_cabinet_closet_designer.update_column_selection',text="",icon='MAN_TRANS').column_type = "Base"
        if self.expand_base_column:
            row = columns_panel_box.row()
            row.label(text="",icon='BLANK1')
            row.template_icon_view(self,"base_column_styles",show_labels=True)    
            
        row = columns_panel_box.row(align=True)    
        row.prop(self,'expand_tall_column',text="",icon='TRIA_DOWN' if self.expand_tall_column else 'TRIA_RIGHT',emboss=False)
        row.prop(self,'tall_column_styles',text="Tall Column Style")
        row.operator('lm_cabinet_closet_designer.update_columns',text="",icon='FILE_REFRESH').column_type = "Tall"
        row.operator('lm_cabinet_closet_designer.update_column_selection',text="",icon='MAN_TRANS').column_type = "Tall"
        if self.expand_tall_column:
            row = columns_panel_box.row()
            row.label(text="",icon='BLANK1')
            row.template_icon_view(self,"tall_column_styles",show_labels=True)
            
        row = columns_panel_box.row(align=True)    
        row.prop(self,'expand_upper_column',text="",icon='TRIA_DOWN' if self.expand_upper_column else 'TRIA_RIGHT',emboss=False)
        row.prop(self,'upper_column_styles',text="Upper Column Style")
        row.operator('lm_cabinet_closet_designer.update_columns',text="",icon='FILE_REFRESH').column_type = "Upper"
        row.operator('lm_cabinet_closet_designer.update_column_selection',text="",icon='MAN_TRANS').column_type = "Upper"
        if self.expand_upper_column:
            row = columns_panel_box.row()
            row.label(text="",icon='BLANK1')
            row.template_icon_view(self,"upper_column_styles",show_labels=True)                            
        
    def draw_applied_panels(self,layout):
        applied_panel_box = layout.box()
        applied_panel_box.label("Applied Panels:")
        row = applied_panel_box.row(align=True)
        row.prop(self,'expand_applied_panel',text="",icon='TRIA_DOWN' if self.expand_applied_panel else 'TRIA_RIGHT',emboss=False)
        row.prop(self,'applied_panels',text="Panel Style")
        row.operator('lm_cabinet_closet_designer.place_applied_panel',text="",icon='MAN_TRANS')
        if self.expand_applied_panel:
            row = applied_panel_box.row()
            row.label(text="",icon='BLANK1')
            row.template_icon_view(self,"applied_panels",show_labels=True)
        
    def draw_closet_accessories(self,layout):
        applied_panel_box = layout.box()
        applied_panel_box.label("Closet Accessories:")
        row = applied_panel_box.row(align=True)
        row.prop(self,'expand_closet_accessory',text="",icon='TRIA_DOWN' if self.expand_closet_accessory else 'TRIA_RIGHT',emboss=False)
        row.prop(self,'closet_accessory',text="Accessory")
        row.operator('lm_cabinet_closet_designer.place_accessory',text="",icon='MAN_TRANS')
        if self.expand_closet_accessory:
            row = applied_panel_box.row()
            row.label(text="",icon='BLANK1')
            row.template_icon_view(self,"closet_accessory",show_labels=True)
        
    def draw_default_sizes(self,layout):
        box = layout.box()
        row = box.row()
        row.prop(self,'defaults_tabs',expand=True)
        
        if self.defaults_tabs == 'CLOSETS':
            g = bpy.context.scene.lm_closets
            g.draw(box)
            
        if self.defaults_tabs == 'FRAMELESS':
            g = bpy.context.scene.lm_frameless_cabinets
            g.draw(box)
            
        if self.defaults_tabs == 'FACEFRAME':
            g = bpy.context.scene.lm_face_frame_cabients
            g.draw(box)
        
        if self.defaults_tabs == 'CARCASS':
            g = bpy.context.scene.lm_carcass
            g.draw(box)
        
        if self.defaults_tabs == 'EXTERIOR':
            g = bpy.context.scene.lm_exteriors
            g.draw(box)
    
    def draw(self,layout):
        box = layout.box()
        row = box.row()
        row.prop(self,'main_tabs',expand=True)
        
        if self.main_tabs == 'DEFAULTS':
            col = box.column(align=True)
            self.draw_default_sizes(col)

        if self.main_tabs == 'OPTIONS':
            self.draw_molding_options(box)
            self.draw_material_options(box)
            self.draw_hardware_options(box)
            self.draw_door_style_options(box)
            self.draw_column_style_options(box)
            self.draw_applied_panels(box)
            self.draw_closet_accessories(box)

        if self.main_tabs == 'PRICE':
            self.draw_pricing(box)
            self.draw_pricing_setup(box)

class PROPERTIES_Object_Properties(bpy.types.PropertyGroup):
    
    is_crown_molding = bpy.props.BoolProperty(name="Is Crown Molding",description="Used to Delete Molding When Using Auto Add Molding Operator",default=False)
    is_base_molding = bpy.props.BoolProperty(name="Is Base Molding",description="Used to Delete Molding When Using Auto Add Molding Operator",default=False)

def register():
    bpy.utils.register_class(PROPERTIES_Scene_Properties)
    bpy.utils.register_class(PROPERTIES_Object_Properties)
    bpy.types.Scene.lm_cabinet_closet_designer = bpy.props.PointerProperty(type = PROPERTIES_Scene_Properties)
    bpy.types.Object.lm_cabinet_closet_designer = bpy.props.PointerProperty(type = PROPERTIES_Object_Properties)
    bpy.utils.register_class(OPERATOR_Update_Door_Selection)
    bpy.utils.register_class(OPERATOR_Update_All_Doors)
    bpy.utils.register_class(OPERATOR_Update_Pulls)
    bpy.utils.register_class(OPERATOR_Update_Materials)
    bpy.utils.register_class(OPERATOR_Update_Columns)
    bpy.utils.register_class(OPERATOR_Update_Column_Selection)
    bpy.utils.register_class(OPERATOR_Place_Applied_Panel)
    bpy.utils.register_class(OPERATOR_Place_Accessory)
    bpy.utils.register_class(OPERATOR_Update_Pricing)
    
    base_molding_coll = bpy.utils.previews.new()
    base_molding_coll.my_previews_dir = ""
    base_molding_coll.my_previews = ()
    preview_collections["base_moldings"] = base_molding_coll
    
    crown_molding_coll = bpy.utils.previews.new()
    crown_molding_coll.my_previews_dir = ""
    crown_molding_coll.my_previews = ()
    preview_collections["crown_moldings"] = crown_molding_coll
    
    door_style_coll = bpy.utils.previews.new()
    door_style_coll.my_previews_dir = ""
    door_style_coll.my_previews = ()
    preview_collections["door_styles"] = door_style_coll
    
    column_style_coll = bpy.utils.previews.new()
    column_style_coll.my_previews_dir = ""
    column_style_coll.my_previews = ()
    preview_collections["column_styles"] = column_style_coll
    
    closet_wood_material_coll = bpy.utils.previews.new()
    closet_wood_material_coll.my_previews_dir = ""
    closet_wood_material_coll.my_previews = ()
    preview_collections["closet_wood_materials"] = closet_wood_material_coll
    
    closet_solid_material_coll = bpy.utils.previews.new()
    closet_solid_material_coll.my_previews_dir = ""
    closet_solid_material_coll.my_previews = ()
    preview_collections["closet_solid_materials"] = closet_solid_material_coll
    
    pull_coll = bpy.utils.previews.new()
    pull_coll.my_previews_dir = ""
    pull_coll.my_previews = ()
    preview_collections["pulls"] = pull_coll
    
    closet_accessory_coll = bpy.utils.previews.new()
    closet_accessory_coll.my_previews_dir = ""
    closet_accessory_coll.my_previews = ()
    preview_collections["closet_accessories"] = closet_accessory_coll
    
def unregister():
    bpy.utils.unregister_class(PROPERTIES_Scene_Properties)
    bpy.utils.unregister_class(PROPERTIES_Object_Properties)
    bpy.utils.unregister_class(OPERATOR_Update_Door_Selection)
    bpy.utils.unregister_class(OPERATOR_Update_All_Doors)
    bpy.utils.unregister_class(OPERATOR_Update_Pulls)
    bpy.utils.unregister_class(OPERATOR_Update_Materials)
    bpy.utils.unregister_class(OPERATOR_Update_Columns)
    bpy.utils.unregister_class(OPERATOR_Update_Column_Selection)
    bpy.utils.unregister_class(OPERATOR_Place_Applied_Panel)
    bpy.utils.unregister_class(OPERATOR_Place_Accessory)
    bpy.utils.unregister_class(OPERATOR_Update_Pricing)
    