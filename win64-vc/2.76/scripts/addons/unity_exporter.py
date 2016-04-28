'''
Created on Jan 15, 2016

@author: Ryan Montes
'''

bl_info = {
    "name": "Unity Exporter",
    "category": "Import-Export",
    "description": "Exports Blend Files to Unity 5",
    "author": "Ryan Montes"
}

import bpy
from bpy.types import Header, Menu, Panel, Operator, PropertyGroup
from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       BoolVectorProperty,
                       PointerProperty,
                       CollectionProperty,
                       EnumProperty)
import fd

class PANEL_Unity_Exporter(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_label = "Export to Unity"
    bl_category = "Unity Exporter"

    def draw_header(self, context):
        layout = self.layout
        layout.label("",icon='IMAGE_COL')

    @classmethod
    def poll(cls, context):
        return True   

    def draw(self, context):
        layout = self.layout 
        scene = bpy.context.scene.unity_export   
        box = layout.box()
        col = box.column()
        col.prop(scene, "unity_project_path")
        col.operator("unity_export.join_meshes_by_material",text="Join Meshes by Material",icon='MATERIAL')

class OPS_create_unity_build(Operator): 
    bl_idname = "unity_export.create_unity_build"
    bl_label = "Build for Unity 3D"
    bl_options = {'UNDO'}
    
    save_name = StringProperty(name="Name")
    
    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        subprocess.call("\"C:\\Program Files (x86)\\Unity\\Editor\\Unity.exe\"" + \
                         "-batchmode -executeMethod PerformBuild.build", shell=False)
        return {'FINISHED'}     

class OPS_join_meshes_by_material(Operator):
    bl_idname = "unity_export.join_meshes_by_material"
    bl_label = "Join Meshes by Material"
    bl_options = {'UNDO'}
    
    obj_join = []

    def gather_objects_by_material(self, mat):
        for obj in bpy.context.scene.objects:
            if obj.type == 'MESH':
                if obj.material_slots:
                    if obj.material_slots[0].material == mat:
                        self.obj_join.append(obj)        

    def execute(self, context):                 
        objects = bpy.context.scene.objects
        materials = bpy.data.materials
        
        bpy.ops.object.select_all(action='SELECT')    
        bpy.ops.mesh.separate(type='MATERIAL')
        bpy.ops.object.select_all(action='DESELECT')            
        
        for mat in materials:
            for obj in bpy.context.scene.objects:
                if obj.type == 'MESH':
                    if obj.material_slots:
                        if obj.material_slots[0].material == mat:
                            self.obj_join.append(obj)            

            if self.obj_join:
                bpy.context.scene.objects.active = self.obj_join[0]
                for obj in self.obj_join:
                    obj.select = True 
                
                if bpy.context.active_object != 'NONE':    
                    bpy.ops.object.join()              
                    bpy.ops.object.select_all(action='DESELECT')
                    bpy.context.scene.objects.active = None
                
            self.obj_join.clear()
            
        return {'FINISHED'}

class ue_scene(PropertyGroup):
    unity_project_path = StringProperty(name="Unity Project Path",
                                        subtype='DIR_PATH')
    
bpy.utils.register_class(ue_scene)

#------REGISTER
classes = [
           PANEL_Unity_Exporter,
           OPS_create_unity_build,
           OPS_join_meshes_by_material
           ]

class extend_blender_data():
    bpy.types.Scene.unity_export = PointerProperty(type = ue_scene)

def register():
    extend_blender_data()

    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

if __name__ == "__main__":
    register()