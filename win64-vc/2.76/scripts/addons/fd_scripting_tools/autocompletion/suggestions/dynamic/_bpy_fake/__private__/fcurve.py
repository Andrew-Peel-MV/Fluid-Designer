from . driver import Driver
from . struct import Struct
from . fcurvekeyframepoints import FCurveKeyframePoints
from . fcurvemodifiers import FCurveModifiers
from . anytype import AnyType
from . actiongroup import ActionGroup
from . fcurvesample import FCurveSample
from . bpy_struct import bpy_struct
import mathutils

class FCurve(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def extrapolation(self):
        '''(Enum) Method used for evaluating value of F-Curve outside first and
        last keyframes
        
        [CONSTANT, LINEAR]'''
        return str()
    @property
    def driver(self):
        '''(Driver) Channel Driver (only set for Driver F-Curves)'''
        return Driver()
    @property
    def group(self):
        '''(ActionGroup) Action Group that this F-Curve belongs to'''
        return ActionGroup()
    @property
    def data_path(self):
        '''(String) RNA Path to property affected by F-Curve'''
        return str()
    @property
    def array_index(self):
        '''(Integer) Index to the specific property affected by F-Curve if
        applicable'''
        return int()
    @property
    def color_mode(self):
        '''(Enum) Method used to determine color of F-Curve in Graph Editor
        
        [AUTO_RAINBOW, AUTO_RGB, CUSTOM]'''
        return str()
    @property
    def color(self):
        '''(Vector 3D) Color of the F-Curve in the Graph Editor'''
        return mathutils.Vector()
    @property
    def select(self):
        '''(Boolean) F-Curve is selected for editing'''
        return bool()
    @property
    def lock(self):
        '''(Boolean) F-Curve's settings cannot be edited'''
        return bool()
    @property
    def mute(self):
        '''(Boolean) F-Curve is not evaluated'''
        return bool()
    @property
    def hide(self):
        '''(Boolean) F-Curve and its keyframes are hidden in the Graph Editor
        graphs'''
        return bool()
    @property
    def is_valid(self):
        '''(Boolean) False when F-Curve could not be evaluated in past, so should
        be skipped when evaluating'''
        return bool()
    @property
    def sampled_points(self):
        '''(Sequence of FCurveSample) Sampled animation data'''
        return (FCurveSample(),)
    @property
    def keyframe_points(self):
        '''(Sequence of Keyframe) User-editable keyframes'''
        return FCurveKeyframePoints()
    @property
    def modifiers(self):
        '''(Sequence of FModifier) Modifiers affecting the shape of the F-Curve'''
        return FCurveModifiers()
    def evaluate(self, frame):
        '''Evaluate F-Curve
        
        Parameter:
          frame: (Float) Evaluate F-Curve at given frame
        
        Returns:
          value: (Float) Value of F-Curve specific frame'''
        return float()
    def update(self):
        '''Ensure keyframes are sorted in chronological order and handles are set
        correctly'''
        return 
    def range(self):
        '''Get the time extents for F-Curve
        
        Returns:
          range: (Vector 2D) Min/Max values'''
        return mathutils.Vector()
    def update_autoflags(self, data):
        '''Update FCurve flags set automatically from affected property
        (currently, integer/discrete flags set when the property is not a
        float)
        
        Parameter:
          data: (AnyType) Data containing the property controlled by given FCurve'''
        return 
    def convert_to_samples(self, start, end):
        '''Convert current FCurve from keyframes to sample points, if necessary
        
        Parameter:
          start: (Integer)
          end: (Integer)'''
        return 
    def convert_to_keyframes(self, start, end):
        '''Convert current FCurve from sample points to keyframes (linear
        interpolation), if necessary
        
        Parameter:
          start: (Integer)
          end: (Integer)'''
        return 