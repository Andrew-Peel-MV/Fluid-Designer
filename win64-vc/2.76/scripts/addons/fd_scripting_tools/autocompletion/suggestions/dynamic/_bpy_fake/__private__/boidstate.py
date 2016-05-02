from . struct import Struct
from . boidrule import BoidRule
from . bpy_struct import bpy_struct
import mathutils

class BoidState(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Boid state name'''
        return str()
    @property
    def ruleset_type(self):
        '''(Enum) How the rules in the list are evaluated
        
        [FUZZY, RANDOM, AVERAGE]'''
        return str()
    @property
    def rules(self):
        '''(Sequence of BoidRule)'''
        return (BoidRule(),)
    @property
    def active_boid_rule(self):
        '''(BoidRule)'''
        return BoidRule()
    @property
    def active_boid_rule_index(self):
        '''(Integer)'''
        return int()
    @property
    def rule_fuzzy(self):
        '''(Float)'''
        return float()
    @property
    def volume(self):
        '''(Float)'''
        return float()
    @property
    def falloff(self):
        '''(Float)'''
        return float()