from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class ClothSolverResult(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def status(self):
        '''(Enum) Status of the solver iteration
        
        [SUCCESS, NUMERICAL_ISSUE, NO_CONVERGENCE, INVALID_INPUT]'''
        return str()
    @property
    def max_error(self):
        '''(Float) Maximum error during substeps'''
        return float()
    @property
    def min_error(self):
        '''(Float) Minimum error during substeps'''
        return float()
    @property
    def avg_error(self):
        '''(Float) Average error during substeps'''
        return float()
    @property
    def max_iterations(self):
        '''(Integer) Maximum iterations during substeps'''
        return int()
    @property
    def min_iterations(self):
        '''(Integer) Minimum iterations during substeps'''
        return int()
    @property
    def avg_iterations(self):
        '''(Float) Average iterations during substeps'''
        return float()