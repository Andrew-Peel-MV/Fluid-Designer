from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class PROPERTIES_Scene_Properties(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def crown_moldings(self):
        '''(Enum)'''
        return str()
    @property
    def drawer_front_styles(self):
        '''(Enum)'''
        return str()
    @property
    def closet_solid_edge_materials(self):
        '''(Enum)'''
        return str()
    @property
    def closet_solid_surface_materials(self):
        '''(Enum)'''
        return str()
    @property
    def drawer_slide_qty(self):
        '''(Integer)'''
        return int()
    @property
    def upper_column_styles(self):
        '''(Enum)'''
        return str()
    @property
    def price_per_hinge(self):
        '''(Float)'''
        return float()
    @property
    def upper_pull_name(self):
        '''(Enum)'''
        return str()
    @property
    def hardware_cost(self):
        '''(Float)'''
        return float()
    @property
    def price_per_sq_unit_of_material(self):
        '''(Float)'''
        return float()
    @property
    def expand_base_door(self):
        '''(Boolean)'''
        return bool()
    @property
    def defaults_tabs(self):
        '''(Enum)
        
        [CLOSETS, FRAMELESS, FACEFRAME, CARCASS, EXTERIOR]'''
        return str()
    @property
    def closet_accessory(self):
        '''(Enum)'''
        return str()
    @property
    def base_moldings(self):
        '''(Enum)'''
        return str()
    @property
    def edge_material_types(self):
        '''(Enum)
        
        [SOLID, GRAIN]'''
        return str()
    @property
    def base_column_styles(self):
        '''(Enum)'''
        return str()
    @property
    def expand_closet_accessory(self):
        '''(Boolean)'''
        return bool()
    @property
    def upper_door_styles(self):
        '''(Enum)'''
        return str()
    @property
    def expand_upper_pull(self):
        '''(Boolean)'''
        return bool()
    @property
    def material_cost(self):
        '''(Float)'''
        return float()
    @property
    def tall_column_styles(self):
        '''(Enum)'''
        return str()
    @property
    def material_amount(self):
        '''(Float)'''
        return float()
    @property
    def closet_wood_edge_materials(self):
        '''(Enum)'''
        return str()
    @property
    def main_tabs(self):
        '''(Enum)
        
        [DEFAULTS, OPTIONS, PRICE]'''
        return str()
    @property
    def expand_crown_molding(self):
        '''(Boolean)'''
        return bool()
    @property
    def cam_qty(self):
        '''(Integer)'''
        return int()
    @property
    def shelf_pin_qty(self):
        '''(Integer)'''
        return int()
    @property
    def expand_edge_material(self):
        '''(Boolean)'''
        return bool()
    @property
    def expand_upper_door(self):
        '''(Boolean)'''
        return bool()
    @property
    def screw_qty(self):
        '''(Integer)'''
        return int()
    @property
    def expand_drawer_pull(self):
        '''(Boolean)'''
        return bool()
    @property
    def surface_material_types(self):
        '''(Enum)
        
        [SOLID, GRAIN]'''
        return str()
    @property
    def expand_surface_material(self):
        '''(Boolean)'''
        return bool()
    @property
    def base_pull_name(self):
        '''(Enum)'''
        return str()
    @property
    def pull_qty(self):
        '''(Integer)'''
        return int()
    @property
    def base_door_styles(self):
        '''(Enum)'''
        return str()
    @property
    def price_per_shelf_pin(self):
        '''(Float)'''
        return float()
    @property
    def price_per_pull(self):
        '''(Float)'''
        return float()
    @property
    def expand_tall_door(self):
        '''(Boolean)'''
        return bool()
    @property
    def expand_tall_column(self):
        '''(Boolean)'''
        return bool()
    @property
    def expand_tall_pull(self):
        '''(Boolean)'''
        return bool()
    @property
    def applied_panels(self):
        '''(Enum)'''
        return str()
    @property
    def expand_base_pull(self):
        '''(Boolean)'''
        return bool()
    @property
    def expand_drawer_front(self):
        '''(Boolean)'''
        return bool()
    @property
    def price_per_cam(self):
        '''(Float)'''
        return float()
    @property
    def total_price(self):
        '''(Float)'''
        return float()
    @property
    def tall_pull_name(self):
        '''(Enum)'''
        return str()
    @property
    def closet_wood_surface_materials(self):
        '''(Enum)'''
        return str()
    @property
    def expand_base_molding(self):
        '''(Boolean)'''
        return bool()
    @property
    def tall_door_styles(self):
        '''(Enum)'''
        return str()
    @property
    def hanging_amount(self):
        '''(Float)'''
        return float()
    @property
    def expand_base_column(self):
        '''(Boolean)'''
        return bool()
    @property
    def price_per_ln_unit_of_rods(self):
        '''(Float)'''
        return float()
    @property
    def price_per_drawer_slide(self):
        '''(Float)'''
        return float()
    @property
    def expand_applied_panel(self):
        '''(Boolean)'''
        return bool()
    @property
    def hinge_qty(self):
        '''(Integer)'''
        return int()
    @property
    def expand_upper_column(self):
        '''(Boolean)'''
        return bool()
    @property
    def drawer_pull_name(self):
        '''(Enum)'''
        return str()