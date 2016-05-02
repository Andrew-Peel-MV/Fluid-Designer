from . struct import Struct
from . controller import Controller
from . bpy_struct import bpy_struct
import mathutils

class Sensor(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Sensor name'''
        return str()
    @property
    def type(self):
        '''(Enum)
        
        [ACTUATOR, ALWAYS, ARMATURE, COLLISION, DELAY, JOYSTICK, KEYBOARD,
        MESSAGE, MOUSE, NEAR, PROPERTY, RADAR, RANDOM, RAY]'''
        return str()
    @property
    def pin(self):
        '''(Boolean) Display when not linked to a visible states controller'''
        return bool()
    @property
    def active(self):
        '''(Boolean) Set active state of the sensor'''
        return bool()
    @property
    def show_expanded(self):
        '''(Boolean) Set sensor expanded in the user interface'''
        return bool()
    @property
    def invert(self):
        '''(Boolean) Invert the level(output) of this sensor'''
        return bool()
    @property
    def use_level(self):
        '''(Boolean) Level detector, trigger controllers of new states (only
        applicable upon logic state transition)'''
        return bool()
    @property
    def use_pulse_true_level(self):
        '''(Boolean) Activate TRUE level triggering (pulse mode)'''
        return bool()
    @property
    def use_pulse_false_level(self):
        '''(Boolean) Activate FALSE level triggering (pulse mode)'''
        return bool()
    @property
    def tick_skip(self):
        '''(Integer) Number of logic ticks skipped between 2 active pulses (0 =
        pulse every logic tick, 1 = skip 1 logic tick between pulses, etc.)'''
        return int()
    @property
    def use_tap(self):
        '''(Boolean) Trigger controllers only for an instant, even while the
        sensor remains true'''
        return bool()
    @property
    def controllers(self):
        '''(Sequence of Controller) The list containing the controllers connected
        to the sensor'''
        return (Controller(),)
    def link(self, controller):
        '''Link the sensor to a controller
        
        Parameter:
          controller: (Controller) Controller to link to'''
        return 
    def unlink(self, controller):
        '''Unlink the sensor from a controller
        
        Parameter:
          controller: (Controller) Controller to unlink from'''
        return 