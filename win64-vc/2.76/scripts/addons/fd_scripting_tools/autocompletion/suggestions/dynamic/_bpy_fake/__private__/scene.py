from . imagepreview import ImagePreview
from . sceneobjects import SceneObjects
from . greasepencil import GreasePencil
from . id import ID
from . iconprops import IconProps
from . displaysafeareas import DisplaySafeAreas
from . scene import Scene
from . keyingsets import KeyingSets
from . animdata import AnimData
from . scenebases import SceneBases
from . scene_props import Scene_Props
from . rigidbodyworld import RigidBodyWorld
from . nodetree import NodeTree
from . sequenceeditor import SequenceEditor
from . rendersettings import RenderSettings
from . colormanageddisplaysettings import ColorManagedDisplaySettings
from . properties_scene_variables import PROPERTIES_Scene_Variables
from . depsgraph import Depsgraph
from . object import Object
from . cyclesrendersettings import CyclesRenderSettings
from . properties_scene_properties import PROPERTIES_Scene_Properties
from . fd_scene import fd_scene
from . scene_variables import Scene_Variables
from . unitsettings import UnitSettings
from . scene_properties import SCENE_PROPERTIES
from . toolsettings import ToolSettings
from . scenegamedata import SceneGameData
from . cyclescurverendersettings import CyclesCurveRenderSettings
from . library import Library
from . colormanagedviewsettings import ColorManagedViewSettings
from . timelinemarkers import TimelineMarkers
from . movieclip import MovieClip
from . keyingsetsall import KeyingSetsAll
from . struct import Struct
from . transformorientation import TransformOrientation
from . colormanagedsequencercolorspacesettings import ColorManagedSequencerColorspaceSettings
from . world import World
from . bpy_struct import bpy_struct
import mathutils

class Scene(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique datablock ID name'''
        return str()
    @property
    def users(self):
        '''(Integer) Number of times this datablock is referenced'''
        return int()
    @property
    def use_fake_user(self):
        '''(Boolean) Save this datablock even if it has no users'''
        return bool()
    @property
    def tag(self):
        '''(Boolean) Tools can use this to tag data for their own purposes
        (initial state is undefined)'''
        return bool()
    @property
    def is_updated(self):
        '''(Boolean) Datablock is tagged for recalculation'''
        return bool()
    @property
    def is_updated_data(self):
        '''(Boolean) Datablock data is tagged for recalculation'''
        return bool()
    @property
    def is_library_indirect(self):
        '''(Boolean) Is this ID block linked indirectly'''
        return bool()
    @property
    def library(self):
        '''(Library) Library file the datablock is linked from'''
        return Library()
    @property
    def preview(self):
        '''(ImagePreview) Preview image and icon of this datablock (None if not
        supported for this type of data)'''
        return ImagePreview()
    @property
    def camera(self):
        '''(Object) Active camera, used for rendering the scene'''
        return Object()
    @property
    def background_set(self):
        '''(Scene) Background set scene'''
        return Scene()
    @property
    def world(self):
        '''(World) World used for rendering the scene'''
        return World()
    @property
    def cursor_location(self):
        '''(Vector 3D) 3D cursor location'''
        return mathutils.Vector()
    @property
    def object_bases(self):
        '''(Sequence of ObjectBase)'''
        return SceneBases()
    @property
    def objects(self):
        '''(Sequence of Object)'''
        return SceneObjects()
    @property
    def layers(self):
        '''(Boolean[20]) Visible layers - Shift-Click/Drag to select multiple
        layers'''
        return bool()
    @property
    def active_layer(self):
        '''(Integer) Active scene layer index'''
        return int()
    @property
    def frame_current(self):
        '''(Integer) Current Frame, to update animation data from python
        frame_set() instead'''
        return int()
    @property
    def frame_subframe(self):
        '''(Float)'''
        return float()
    @property
    def frame_start(self):
        '''(Integer) First frame of the playback/rendering range'''
        return int()
    @property
    def frame_end(self):
        '''(Integer) Final frame of the playback/rendering range'''
        return int()
    @property
    def frame_step(self):
        '''(Integer) Number of frames to skip forward while rendering/playing
        back each frame'''
        return int()
    @property
    def frame_current_final(self):
        '''(Float) Current frame with subframe and time remapping applied'''
        return float()
    @property
    def lock_frame_selection_to_range(self):
        '''(Boolean) Don't allow frame to be selected with mouse outside of frame
        range'''
        return bool()
    @property
    def use_preview_range(self):
        '''(Boolean) Use an alternative start/end frame range for animation
        playback and OpenGL renders instead of the Render properties start/end
        frame range'''
        return bool()
    @property
    def frame_preview_start(self):
        '''(Integer) Alternative start frame for UI playback'''
        return int()
    @property
    def frame_preview_end(self):
        '''(Integer) Alternative end frame for UI playback'''
        return int()
    @property
    def show_keys_from_selected_only(self):
        '''(Boolean) Consider keyframes for active Object and/or its selected
        bones only (in timeline and when jumping between keyframes)'''
        return bool()
    @property
    def use_stamp_note(self):
        '''(String) User defined note for the render stamping'''
        return str()
    @property
    def animation_data(self):
        '''(AnimData) Animation data for this datablock'''
        return AnimData()
    @property
    def is_nla_tweakmode(self):
        '''(Boolean) Whether there is any action referenced by NLA being edited
        (strictly read-only)'''
        return bool()
    @property
    def use_frame_drop(self):
        '''(Boolean) Play back dropping frames if frame display is too slow'''
        return bool()
    @property
    def sync_mode(self):
        '''(Enum) How to sync playback
        
        [NONE, FRAME_DROP, AUDIO_SYNC]'''
        return str()
    @property
    def node_tree(self):
        '''(NodeTree) Compositing node tree'''
        return NodeTree()
    @property
    def use_nodes(self):
        '''(Boolean) Enable the compositing node tree'''
        return bool()
    @property
    def sequence_editor(self):
        '''(SequenceEditor)'''
        return SequenceEditor()
    @property
    def keying_sets(self):
        '''(Sequence of KeyingSet) Absolute Keying Sets for this Scene'''
        return KeyingSets()
    @property
    def keying_sets_all(self):
        '''(Sequence of KeyingSet) All Keying Sets available for use (Builtins
        and Absolute Keying Sets for this Scene)'''
        return KeyingSetsAll()
    @property
    def rigidbody_world(self):
        '''(RigidBodyWorld)'''
        return RigidBodyWorld()
    @property
    def tool_settings(self):
        '''(ToolSettings)'''
        return ToolSettings()
    @property
    def unit_settings(self):
        '''(UnitSettings) Unit editing settings'''
        return UnitSettings()
    @property
    def gravity(self):
        '''(Vector 3D) Constant acceleration in a given direction'''
        return mathutils.Vector()
    @property
    def use_gravity(self):
        '''(Boolean) Use global gravity for all dynamics'''
        return bool()
    @property
    def render(self):
        '''(RenderSettings)'''
        return RenderSettings()
    @property
    def safe_areas(self):
        '''(DisplaySafeAreas)'''
        return DisplaySafeAreas()
    @property
    def timeline_markers(self):
        '''(Sequence of TimelineMarker) Markers used in all timelines for the
        current scene'''
        return TimelineMarkers()
    @property
    def use_audio(self):
        '''(Boolean) Play back of audio from Sequence Editor will be muted'''
        return bool()
    @property
    def use_audio_sync(self):
        '''(Boolean) Play back and sync with audio clock, dropping frames if
        frame display is too slow'''
        return bool()
    @property
    def use_audio_scrub(self):
        '''(Boolean) Play audio from Sequence Editor while scrubbing'''
        return bool()
    @property
    def audio_doppler_speed(self):
        '''(Float) Speed of sound for Doppler effect calculation'''
        return float()
    @property
    def audio_doppler_factor(self):
        '''(Float) Pitch factor for Doppler effect calculation'''
        return float()
    @property
    def audio_distance_model(self):
        '''(Enum) Distance model for distance attenuation calculation
        
        [NONE, INVERSE, INVERSE_CLAMPED, LINEAR, LINEAR_CLAMPED, EXPONENT,
        EXPONENT_CLAMPED]'''
        return str()
    @property
    def audio_volume(self):
        '''(Float) Audio volume'''
        return float()
    @property
    def game_settings(self):
        '''(SceneGameData)'''
        return SceneGameData()
    @property
    def grease_pencil(self):
        '''(GreasePencil) Grease Pencil datablock'''
        return GreasePencil()
    @property
    def orientations(self):
        '''(Sequence of TransformOrientation)'''
        return (TransformOrientation(),)
    @property
    def active_clip(self):
        '''(MovieClip) Active movie clip used for constraints and viewport
        drawing'''
        return MovieClip()
    @property
    def view_settings(self):
        '''(ColorManagedViewSettings) Color management settings applied on image
        before saving'''
        return ColorManagedViewSettings()
    @property
    def display_settings(self):
        '''(ColorManagedDisplaySettings) Settings of device saved image would be
        displayed on'''
        return ColorManagedDisplaySettings()
    @property
    def sequencer_colorspace_settings(self):
        '''(ColorManagedSequencerColorspaceSettings) Settings of color space
        sequencer is working in'''
        return ColorManagedSequencerColorspaceSettings()
    @property
    def depsgraph(self):
        '''(Depsgraph) Dependencies in the scene data'''
        return Depsgraph()
    @property
    def mv(self):
        '''(fd_scene)'''
        return fd_scene()
    @property
    def cabinetlib(self):
        '''(SCENE_PROPERTIES)'''
        return SCENE_PROPERTIES()
    @property
    def lm_face_frame_cabients(self):
        '''(PROPERTIES_Scene_Variables)'''
        return PROPERTIES_Scene_Variables()
    @property
    def lm_frameless_cabinets(self):
        '''(PROPERTIES_Scene_Variables)'''
        return PROPERTIES_Scene_Variables()
    @property
    def lm_cabinet_closet_designer(self):
        '''(PROPERTIES_Scene_Properties)'''
        return PROPERTIES_Scene_Properties()
    @property
    def lm_cabinet_doors(self):
        '''(Scene_Variables)'''
        return Scene_Variables()
    @property
    def lm_carcass(self):
        '''(PROPERTIES_Scene_Variables)'''
        return PROPERTIES_Scene_Variables()
    @property
    def lm_closets(self):
        '''(PROPERTIES_Scene_Properties)'''
        return PROPERTIES_Scene_Properties()
    @property
    def lm_columns(self):
        '''(PROPERTIES_Scene_Variables)'''
        return PROPERTIES_Scene_Variables()
    @property
    def lm_exteriors(self):
        '''(PROPERTIES_Scene_Variables)'''
        return PROPERTIES_Scene_Variables()
    @property
    def lm_interiors(self):
        '''(PROPERTIES_Scene_Variables)'''
        return PROPERTIES_Scene_Variables()
    @property
    def lm_moldings(self):
        '''(PROPERTIES_Scene_Variables)'''
        return PROPERTIES_Scene_Variables()
    @property
    def lm_pulls(self):
        '''(PROPERTIES_Scene_Variables)'''
        return PROPERTIES_Scene_Variables()
    @property
    def cycles(self):
        '''(CyclesRenderSettings) Cycles render settings'''
        return CyclesRenderSettings()
    @property
    def cycles_curves(self):
        '''(CyclesCurveRenderSettings) Cycles hair rendering settings'''
        return CyclesCurveRenderSettings()
    @property
    def icon_props(self):
        '''(IconProps)'''
        return IconProps()
    @property
    def fd_roombuilder(self):
        '''(Scene_Props)'''
        return Scene_Props()
    def copy(self):
        '''Create a copy of this datablock (not supported for all datablocks)
        
        Returns:
          id: (ID) New copy of the ID'''
        return ID()
    def user_clear(self):
        '''Clear the user count of a datablock so its not saved, on reload the
        data will be removed'''
        return 
    def animation_data_create(self):
        '''Create animation data to this ID, note that not all ID types support
        this
        
        Returns:
          anim_data: (AnimData) New animation data or NULL'''
        return AnimData()
    def animation_data_clear(self):
        '''Clear animation on this this ID'''
        return 
    def update_tag(self, refresh):
        '''Tag the ID to update its display data, e.g. when calling
        :class:`bpy.types.Scene.update`
        
        Parameter:
          refresh: (Enum) Type of updates to perform'''
        return 
    def sequence_editor_create(self):
        '''Ensure sequence editor is valid in this scene
        
        Returns:
          sequence_editor: (SequenceEditor) New sequence editor data or NULL'''
        return SequenceEditor()
    def sequence_editor_clear(self):
        '''Clear sequence editor in this scene'''
        return 
    def statistics(self):
        '''statistics
        
        Returns:
          statistics: (String)'''
        return str()
    def frame_set(self, frame, subframe):
        '''Set scene frame updating all objects immediately
        
        Parameter:
          frame: (Integer) Frame number to set
          subframe: (Float) Sub-frame time, between 0.0 and 1.0'''
        return 
    def update(self):
        '''Update data tagged to be updated from previous access to data or
        operators'''
        return 
    def uvedit_aspect(self, object):
        '''Get uv aspect for current object
        
        Parameter:
          object: (Object) Object
        
        Returns:
          result: (Vector 2D) aspect'''
        return mathutils.Vector()
    def ray_cast(self, start, end):
        '''Cast a ray onto in object space
        
        Parameter:
          start: (Vector 3D)
          end: (Vector 3D)
        
        Returns:
          result: (Boolean)
          object: (Object) Ray cast object
          matrix: (Matrix) Matrix
          location: (Vector 3D) The hit location of this ray cast
          normal: (Vector 3D) The face normal at the ray cast hit location'''
        return bool(), Object(), mathutils.Matrix(), mathutils.Vector(), mathutils.Vector()