from . struct import Struct
from . material import Material
from . freestylesettings import FreestyleSettings
from . group import Group
from . bpy_struct import bpy_struct
import mathutils

class SceneRenderLayer(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Render layer name'''
        return str()
    @property
    def material_override(self):
        '''(Material) Material to override all other materials in this render
        layer'''
        return Material()
    @property
    def light_override(self):
        '''(Group) Group to override all other lights in this render layer'''
        return Group()
    @property
    def layers(self):
        '''(Boolean[20]) Scene layers included in this render layer'''
        return bool()
    @property
    def layers_zmask(self):
        '''(Boolean[20]) Zmask scene layers for solid faces'''
        return bool()
    @property
    def layers_exclude(self):
        '''(Boolean[20]) Exclude scene layers from having any influence'''
        return bool()
    @property
    def samples(self):
        '''(Integer) Override number of render samples for this render layer, 0
        will use the scene setting'''
        return int()
    @property
    def pass_alpha_threshold(self):
        '''(Float) Z, Index, normal, UV and vector passes are only affected by
        surfaces with alpha transparency equal to or higher than this
        threshold'''
        return float()
    @property
    def use(self):
        '''(Boolean) Disable or enable the render layer'''
        return bool()
    @property
    def use_zmask(self):
        '''(Boolean) Only render what's in front of the solid z values'''
        return bool()
    @property
    def invert_zmask(self):
        '''(Boolean) For Zmask, only render what is behind solid z values instead
        of in front'''
        return bool()
    @property
    def use_all_z(self):
        '''(Boolean) Fill in Z values for solid faces in invisible layers, for
        masking'''
        return bool()
    @property
    def use_solid(self):
        '''(Boolean) Render Solid faces in this Layer'''
        return bool()
    @property
    def use_halo(self):
        '''(Boolean) Render Halos in this Layer (on top of Solid)'''
        return bool()
    @property
    def use_ztransp(self):
        '''(Boolean) Render Z-Transparent faces in this Layer (on top of Solid
        and Halos)'''
        return bool()
    @property
    def use_sky(self):
        '''(Boolean) Render Sky in this Layer'''
        return bool()
    @property
    def use_edge_enhance(self):
        '''(Boolean) Render Edge-enhance in this Layer (only works for Solid
        faces)'''
        return bool()
    @property
    def use_strand(self):
        '''(Boolean) Render Strands in this Layer'''
        return bool()
    @property
    def use_freestyle(self):
        '''(Boolean) Render stylized strokes in this Layer'''
        return bool()
    @property
    def use_pass_combined(self):
        '''(Boolean) Deliver full combined RGBA buffer'''
        return bool()
    @property
    def use_pass_z(self):
        '''(Boolean) Deliver Z values pass'''
        return bool()
    @property
    def use_pass_vector(self):
        '''(Boolean) Deliver speed vector pass'''
        return bool()
    @property
    def use_pass_normal(self):
        '''(Boolean) Deliver normal pass'''
        return bool()
    @property
    def use_pass_uv(self):
        '''(Boolean) Deliver texture UV pass'''
        return bool()
    @property
    def use_pass_mist(self):
        '''(Boolean) Deliver mist factor pass (0.0-1.0)'''
        return bool()
    @property
    def use_pass_object_index(self):
        '''(Boolean) Deliver object index pass'''
        return bool()
    @property
    def use_pass_material_index(self):
        '''(Boolean) Deliver material index pass'''
        return bool()
    @property
    def use_pass_color(self):
        '''(Boolean) Deliver shade-less color pass'''
        return bool()
    @property
    def use_pass_diffuse(self):
        '''(Boolean) Deliver diffuse pass'''
        return bool()
    @property
    def use_pass_specular(self):
        '''(Boolean) Deliver specular pass'''
        return bool()
    @property
    def use_pass_shadow(self):
        '''(Boolean) Deliver shadow pass'''
        return bool()
    @property
    def use_pass_ambient_occlusion(self):
        '''(Boolean) Deliver AO pass'''
        return bool()
    @property
    def use_pass_reflection(self):
        '''(Boolean) Deliver raytraced reflection pass'''
        return bool()
    @property
    def use_pass_refraction(self):
        '''(Boolean) Deliver raytraced refraction pass'''
        return bool()
    @property
    def use_pass_emit(self):
        '''(Boolean) Deliver emission pass'''
        return bool()
    @property
    def use_pass_environment(self):
        '''(Boolean) Deliver environment lighting pass'''
        return bool()
    @property
    def use_pass_indirect(self):
        '''(Boolean) Deliver indirect lighting pass'''
        return bool()
    @property
    def exclude_specular(self):
        '''(Boolean) Exclude specular pass from combined'''
        return bool()
    @property
    def exclude_shadow(self):
        '''(Boolean) Exclude shadow pass from combined'''
        return bool()
    @property
    def exclude_ambient_occlusion(self):
        '''(Boolean) Exclude AO pass from combined'''
        return bool()
    @property
    def exclude_reflection(self):
        '''(Boolean) Exclude raytraced reflection pass from combined'''
        return bool()
    @property
    def exclude_refraction(self):
        '''(Boolean) Exclude raytraced refraction pass from combined'''
        return bool()
    @property
    def exclude_emit(self):
        '''(Boolean) Exclude emission pass from combined'''
        return bool()
    @property
    def exclude_environment(self):
        '''(Boolean) Exclude environment pass from combined'''
        return bool()
    @property
    def exclude_indirect(self):
        '''(Boolean) Exclude indirect pass from combined'''
        return bool()
    @property
    def use_pass_diffuse_direct(self):
        '''(Boolean) Deliver diffuse direct pass'''
        return bool()
    @property
    def use_pass_diffuse_indirect(self):
        '''(Boolean) Deliver diffuse indirect pass'''
        return bool()
    @property
    def use_pass_diffuse_color(self):
        '''(Boolean) Deliver diffuse color pass'''
        return bool()
    @property
    def use_pass_glossy_direct(self):
        '''(Boolean) Deliver glossy direct pass'''
        return bool()
    @property
    def use_pass_glossy_indirect(self):
        '''(Boolean) Deliver glossy indirect pass'''
        return bool()
    @property
    def use_pass_glossy_color(self):
        '''(Boolean) Deliver glossy color pass'''
        return bool()
    @property
    def use_pass_transmission_direct(self):
        '''(Boolean) Deliver transmission direct pass'''
        return bool()
    @property
    def use_pass_transmission_indirect(self):
        '''(Boolean) Deliver transmission indirect pass'''
        return bool()
    @property
    def use_pass_transmission_color(self):
        '''(Boolean) Deliver transmission color pass'''
        return bool()
    @property
    def use_pass_subsurface_direct(self):
        '''(Boolean) Deliver subsurface direct pass'''
        return bool()
    @property
    def use_pass_subsurface_indirect(self):
        '''(Boolean) Deliver subsurface indirect pass'''
        return bool()
    @property
    def use_pass_subsurface_color(self):
        '''(Boolean) Deliver subsurface color pass'''
        return bool()
    @property
    def freestyle_settings(self):
        '''(FreestyleSettings)'''
        return FreestyleSettings()