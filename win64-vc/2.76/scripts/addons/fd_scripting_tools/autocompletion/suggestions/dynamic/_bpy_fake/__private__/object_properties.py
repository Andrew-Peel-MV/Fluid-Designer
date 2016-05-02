from . machine_point import Machine_Point
from . material_slot import Material_Slot
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class OBJECT_PROPERTIES(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def cutpart_name(self):
        '''(String)'''
        return str()
    @property
    def mirror_z(self):
        '''(Boolean) Used in an product assembly to determine if the z dim is
        mirrored'''
        return bool()
    @property
    def product_shape(self):
        '''(String) Shape of the product. 'RECTANGLE','INSIDE_NOTCH','''''
        return str()
    @property
    def type_mesh(self):
        '''(Enum) Select the Mesh Type.
        
        [NONE, CUTPART, EDGEBANDING, SOLIDSTOCK, HARDWARE, BUYOUT, MACHINING]'''
        return str()
    @property
    def mirror_y(self):
        '''(Boolean) Used in an product assembly to determine if the y dim is
        mirrored'''
        return bool()
    @property
    def is_custom(self):
        '''(Boolean) If the product is custom then Solid Analyzer will read the
        geometry otherwise a product match will be used.'''
        return bool()
    @property
    def spec_group_name(self):
        '''(String) Current name of the specification group that is assigned to
        the group.'''
        return str()
    @property
    def edge_w2(self):
        '''(String)'''
        return str()
    @property
    def item_number(self):
        '''(Integer)'''
        return int()
    @property
    def mp(self):
        '''(Machine_Point) Machining Point'''
        return Machine_Point()
    @property
    def product_sub_category(self):
        '''(String)'''
        return str()
    @property
    def library_name(self):
        '''(String) Name of the library that this product is assigned.'''
        return str()
    @property
    def exterior_open(self):
        '''(Boolean)'''
        return bool()
    @property
    def spec_group_index(self):
        '''(Integer)'''
        return int()
    @property
    def type_group(self):
        '''(Enum) Select the Group Type.
        
        [NONE, PRODUCT, INSERT, SPLITTER, OPENING]'''
        return str()
    @property
    def product_category(self):
        '''(String)'''
        return str()
    @property
    def comment(self):
        '''(String) Comment to store information for reporting purposes.'''
        return str()
    @property
    def edge_l1(self):
        '''(String)'''
        return str()
    @property
    def edge_l2(self):
        '''(String)'''
        return str()
    @property
    def edgepart_name(self):
        '''(String)'''
        return str()
    @property
    def placement_type(self):
        '''(String) Type of placement for products. 'STANDARD','CORNER''''
        return str()
    @property
    def interior_open(self):
        '''(Boolean)'''
        return bool()
    @property
    def edge_w1(self):
        '''(String)'''
        return str()
    @property
    def material_slots(self):
        '''(Sequence of Material_Slot) Collection of material slots used'''
        return (Material_Slot(),)