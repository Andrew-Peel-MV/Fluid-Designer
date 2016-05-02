from . struct import Struct
from . material import Material
from . particlesystem import ParticleSystem
from . colorramp import ColorRamp
from . bpy_struct import bpy_struct
import mathutils

class DynamicPaintBrushSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def paint_color(self):
        '''(Vector 3D) Color of the paint'''
        return mathutils.Vector()
    @property
    def paint_alpha(self):
        '''(Float) Paint alpha'''
        return float()
    @property
    def use_material(self):
        '''(Boolean) Use object material to define color and influence'''
        return bool()
    @property
    def material(self):
        '''(Material) Material to use (if not defined, material linked to the
        mesh is used)'''
        return Material()
    @property
    def use_absolute_alpha(self):
        '''(Boolean) Only increase alpha value if paint alpha is higher than
        existing'''
        return bool()
    @property
    def paint_wetness(self):
        '''(Float) Paint wetness, visible in wetmap (some effects only affect wet
        paint)'''
        return float()
    @property
    def use_paint_erase(self):
        '''(Boolean) Erase / remove paint instead of adding it'''
        return bool()
    @property
    def wave_type(self):
        '''(Enum)
        
        [CHANGE, DEPTH, FORCE, REFLECT]'''
        return str()
    @property
    def wave_factor(self):
        '''(Float) Multiplier for wave influence of this brush'''
        return float()
    @property
    def wave_clamp(self):
        '''(Float) Maximum level of surface intersection used to influence waves
        (use 0.0 to disable)'''
        return float()
    @property
    def use_smudge(self):
        '''(Boolean) Make this brush to smudge existing paint as it moves'''
        return bool()
    @property
    def smudge_strength(self):
        '''(Float) Smudge effect strength'''
        return float()
    @property
    def velocity_max(self):
        '''(Float) Velocity considered as maximum influence (Blender units per
        frame)'''
        return float()
    @property
    def use_velocity_alpha(self):
        '''(Boolean) Multiply brush influence by velocity color ramp alpha'''
        return bool()
    @property
    def use_velocity_depth(self):
        '''(Boolean) Multiply brush intersection depth (displace, waves) by
        velocity ramp alpha'''
        return bool()
    @property
    def use_velocity_color(self):
        '''(Boolean) Replace brush color by velocity color ramp'''
        return bool()
    @property
    def paint_source(self):
        '''(Enum)
        
        [PARTICLE_SYSTEM, POINT, DISTANCE, VOLUME_DISTANCE, VOLUME]'''
        return str()
    @property
    def paint_distance(self):
        '''(Float) Maximum distance from brush to mesh surface to affect paint'''
        return float()
    @property
    def use_proximity_ramp_alpha(self):
        '''(Boolean) Only read color ramp alpha'''
        return bool()
    @property
    def proximity_falloff(self):
        '''(Enum) Proximity falloff type
        
        [SMOOTH, CONSTANT, RAMP]'''
        return str()
    @property
    def use_proximity_project(self):
        '''(Boolean) Brush is projected to canvas from defined direction within
        brush proximity'''
        return bool()
    @property
    def ray_direction(self):
        '''(Enum) Ray direction to use for projection (if brush object is located
        in that direction it's painted)
        
        [CANVAS, BRUSH, Z_AXIS]'''
        return str()
    @property
    def invert_proximity(self):
        '''(Boolean) Proximity falloff is applied inside the volume'''
        return bool()
    @property
    def use_negative_volume(self):
        '''(Boolean) Negate influence inside the volume'''
        return bool()
    @property
    def particle_system(self):
        '''(ParticleSystem) The particle system to paint with'''
        return ParticleSystem()
    @property
    def use_particle_radius(self):
        '''(Boolean) Use radius from particle settings'''
        return bool()
    @property
    def solid_radius(self):
        '''(Float) Radius that will be painted solid'''
        return float()
    @property
    def smooth_radius(self):
        '''(Float) Smooth falloff added after solid radius'''
        return float()
    @property
    def paint_ramp(self):
        '''(ColorRamp) Color ramp used to define proximity falloff'''
        return ColorRamp()
    @property
    def velocity_ramp(self):
        '''(ColorRamp) Color ramp used to define brush velocity effect'''
        return ColorRamp()