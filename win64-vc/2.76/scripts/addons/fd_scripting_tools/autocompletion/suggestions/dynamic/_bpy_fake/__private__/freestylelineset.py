from . struct import Struct
from . group import Group
from . freestylelinestyle import FreestyleLineStyle
from . bpy_struct import bpy_struct
import mathutils

class FreestyleLineSet(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def linestyle(self):
        '''(FreestyleLineStyle) Line style settings'''
        return FreestyleLineStyle()
    @property
    def name(self):
        '''(String) Line set name'''
        return str()
    @property
    def show_render(self):
        '''(Boolean) Enable or disable this line set during stroke rendering'''
        return bool()
    @property
    def select_by_visibility(self):
        '''(Boolean) Select feature edges based on visibility'''
        return bool()
    @property
    def select_by_edge_types(self):
        '''(Boolean) Select feature edges based on edge types'''
        return bool()
    @property
    def select_by_group(self):
        '''(Boolean) Select feature edges based on a group of objects'''
        return bool()
    @property
    def select_by_image_border(self):
        '''(Boolean) Select feature edges by image border (less memory
        consumption)'''
        return bool()
    @property
    def select_by_face_marks(self):
        '''(Boolean) Select feature edges by face marks'''
        return bool()
    @property
    def edge_type_negation(self):
        '''(Enum) Specify either inclusion or exclusion of feature edges selected
        by edge types
        
        [INCLUSIVE, EXCLUSIVE]'''
        return str()
    @property
    def edge_type_combination(self):
        '''(Enum) Specify a logical combination of selection conditions on
        feature edge types
        
        [OR, AND]'''
        return str()
    @property
    def group(self):
        '''(Group) A group of objects based on which feature edges are selected'''
        return Group()
    @property
    def group_negation(self):
        '''(Enum) Specify either inclusion or exclusion of feature edges
        belonging to a group of objects
        
        [INCLUSIVE, EXCLUSIVE]'''
        return str()
    @property
    def face_mark_negation(self):
        '''(Enum) Specify either inclusion or exclusion of feature edges selected
        by face marks
        
        [INCLUSIVE, EXCLUSIVE]'''
        return str()
    @property
    def face_mark_condition(self):
        '''(Enum) Specify a feature edge selection condition based on face marks
        
        [ONE, BOTH]'''
        return str()
    @property
    def select_silhouette(self):
        '''(Boolean) Select silhouettes (edges at the boundary of visible and
        hidden faces)'''
        return bool()
    @property
    def select_border(self):
        '''(Boolean) Select border edges (open mesh edges)'''
        return bool()
    @property
    def select_crease(self):
        '''(Boolean) Select crease edges (those between two faces making an angle
        smaller than the Crease Angle)'''
        return bool()
    @property
    def select_ridge_valley(self):
        '''(Boolean) Select ridges and valleys (boundary lines between convex and
        concave areas of surface)'''
        return bool()
    @property
    def select_suggestive_contour(self):
        '''(Boolean) Select suggestive contours (almost silhouette/contour edges)'''
        return bool()
    @property
    def select_material_boundary(self):
        '''(Boolean) Select edges at material boundaries'''
        return bool()
    @property
    def select_contour(self):
        '''(Boolean) Select contours (outer silhouettes of each object)'''
        return bool()
    @property
    def select_external_contour(self):
        '''(Boolean) Select external contours (outer silhouettes of occluding and
        occluded objects)'''
        return bool()
    @property
    def select_edge_mark(self):
        '''(Boolean) Select edge marks (edges annotated by Freestyle edge marks)'''
        return bool()
    @property
    def exclude_silhouette(self):
        '''(Boolean) Exclude silhouette edges'''
        return bool()
    @property
    def exclude_border(self):
        '''(Boolean) Exclude border edges'''
        return bool()
    @property
    def exclude_crease(self):
        '''(Boolean) Exclude crease edges'''
        return bool()
    @property
    def exclude_ridge_valley(self):
        '''(Boolean) Exclude ridges and valleys'''
        return bool()
    @property
    def exclude_suggestive_contour(self):
        '''(Boolean) Exclude suggestive contours'''
        return bool()
    @property
    def exclude_material_boundary(self):
        '''(Boolean) Exclude edges at material boundaries'''
        return bool()
    @property
    def exclude_contour(self):
        '''(Boolean) Exclude contours'''
        return bool()
    @property
    def exclude_external_contour(self):
        '''(Boolean) Exclude external contours'''
        return bool()
    @property
    def exclude_edge_mark(self):
        '''(Boolean) Exclude edge marks'''
        return bool()
    @property
    def visibility(self):
        '''(Enum) Determine how to use visibility for feature edge selection
        
        [VISIBLE, HIDDEN, RANGE]'''
        return str()
    @property
    def qi_start(self):
        '''(Integer) First QI value of the QI range'''
        return int()
    @property
    def qi_end(self):
        '''(Integer) Last QI value of the QI range'''
        return int()