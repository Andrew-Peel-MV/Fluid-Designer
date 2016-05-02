from . struct import Struct
from . actuator import Actuator
from . sensor import Sensor
from . bpy_struct import bpy_struct
import mathutils

class Controller(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String)'''
        return str()
    @property
    def type(self):
        '''(Enum)
        
        [LOGIC_AND, LOGIC_OR, LOGIC_NAND, LOGIC_NOR, LOGIC_XOR, LOGIC_XNOR,
        EXPRESSION, PYTHON]'''
        return str()
    @property
    def show_expanded(self):
        '''(Boolean) Set controller expanded in the user interface'''
        return bool()
    @property
    def active(self):
        '''(Boolean) Set the active state of the controller'''
        return bool()
    @property
    def use_priority(self):
        '''(Boolean) Mark controller for execution before all non-marked
        controllers (good for startup scripts)'''
        return bool()
    @property
    def actuators(self):
        '''(Sequence of Actuator) The list containing the actuators connected to
        the controller'''
        return (Actuator(),)
    @property
    def states(self):
        '''(Integer) Set Controller state index (1 to 30)'''
        return int()
    def link(self, sensor, actuator):
        '''Link the controller with a sensor/actuator
        
        Parameter:
          sensor: (Sensor) Sensor to link the controller to
          actuator: (Actuator) Actuator to link the controller to'''
        return 
    def unlink(self, sensor, actuator):
        '''Unlink the controller from a sensor/actuator
        
        Parameter:
          sensor: (Sensor) Sensor to unlink the controller from
          actuator: (Actuator) Actuator to unlink the controller from'''
        return 