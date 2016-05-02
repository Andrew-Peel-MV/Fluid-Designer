from . nodetreeoutputs import NodeTreeOutputs
from . nodetree import NodeTree
from . context import Context
from . imagepreview import ImagePreview
from . nodelinks import NodeLinks
from . id import ID
from . greasepencil import GreasePencil
from . struct import Struct
from . library import Library
from . animdata import AnimData
from . nodes import Nodes
from . nodetreeinputs import NodeTreeInputs
from . bpy_struct import bpy_struct
import mathutils

class NodeTree(bpy_struct):
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
    def view_center(self):
        '''(Vector 2D)'''
        return mathutils.Vector()
    @property
    def animation_data(self):
        '''(AnimData) Animation data for this datablock'''
        return AnimData()
    @property
    def nodes(self):
        '''(Sequence of Node)'''
        return Nodes()
    @property
    def links(self):
        '''(Sequence of NodeLink)'''
        return NodeLinks()
    @property
    def grease_pencil(self):
        '''(GreasePencil) Grease Pencil datablock'''
        return GreasePencil()
    @property
    def type(self):
        '''(Enum) Node Tree type (deprecated, bl_idname is the actual node tree
        type identifier)
        
        [SHADER, TEXTURE, COMPOSITING]'''
        return str()
    @property
    def inputs(self):
        '''(Sequence of NodeSocketInterface) Node tree inputs'''
        return NodeTreeInputs()
    @property
    def active_input(self):
        '''(Integer) Index of the active input'''
        return int()
    @property
    def outputs(self):
        '''(Sequence of NodeSocketInterface) Node tree outputs'''
        return NodeTreeOutputs()
    @property
    def active_output(self):
        '''(Integer) Index of the active output'''
        return int()
    @property
    def bl_idname(self):
        '''(String)'''
        return str()
    @property
    def bl_label(self):
        '''(String) The node tree label'''
        return str()
    @property
    def bl_description(self):
        '''(String)'''
        return str()
    @property
    def bl_icon(self):
        '''(Enum) The node tree icon
        
        [NONE, QUESTION, ERROR, CANCEL, TRIA_RIGHT, TRIA_DOWN, TRIA_LEFT,
        TRIA_UP, ARROW_LEFTRIGHT, PLUS, DISCLOSURE_TRI_DOWN,
        DISCLOSURE_TRI_RIGHT, RADIOBUT_OFF, RADIOBUT_ON, MENU_PANEL, BLENDER,
        GRIP, DOT, COLLAPSEMENU, X, GO_LEFT, PLUG, UI, NODE, NODE_SEL,
        FULLSCREEN, SPLITSCREEN, RIGHTARROW_THIN, BORDERMOVE, VIEWZOOM,
        ZOOMIN, ZOOMOUT, PANEL_CLOSE, COPY_ID, EYEDROPPER, LINK_AREA, AUTO,
        CHECKBOX_DEHLT, CHECKBOX_HLT, UNLOCKED, LOCKED, UNPINNED, PINNED,
        SCREEN_BACK, RIGHTARROW, DOWNARROW_HLT, DOTSUP, DOTSDOWN, LINK,
        INLINK, PLUGIN, HELP, GHOST_ENABLED, COLOR, LINKED, UNLINKED, HAND,
        ZOOM_ALL, ZOOM_SELECTED, ZOOM_PREVIOUS, ZOOM_IN, ZOOM_OUT,
        RENDER_REGION, BORDER_RECT, BORDER_LASSO, FREEZE, STYLUS_PRESSURE,
        GHOST_DISABLED, NEW, FILE_TICK, QUIT, URL, RECOVER_LAST,
        FULLSCREEN_ENTER, FULLSCREEN_EXIT, BLANK1, LAMP, MATERIAL, TEXTURE,
        ANIM, WORLD, SCENE, EDIT, GAME, RADIO, SCRIPT, PARTICLES, PHYSICS,
        SPEAKER, TEXTURE_SHADED, VIEW3D, IPO, OOPS, BUTS, FILESEL, IMAGE_COL,
        INFO, SEQUENCE, TEXT, IMASEL, SOUND, ACTION, NLA, SCRIPTWIN, TIME,
        NODETREE, LOGIC, CONSOLE, PREFERENCES, CLIP, ASSET_MANAGER,
        OBJECT_DATAMODE, EDITMODE_HLT, FACESEL_HLT, VPAINT_HLT, TPAINT_HLT,
        WPAINT_HLT, SCULPTMODE_HLT, POSE_HLT, PARTICLEMODE, LIGHTPAINT,
        SCENE_DATA, RENDERLAYERS, WORLD_DATA, OBJECT_DATA, MESH_DATA,
        CURVE_DATA, META_DATA, LATTICE_DATA, LAMP_DATA, MATERIAL_DATA,
        TEXTURE_DATA, ANIM_DATA, CAMERA_DATA, PARTICLE_DATA,
        LIBRARY_DATA_DIRECT, GROUP, ARMATURE_DATA, POSE_DATA, BONE_DATA,
        CONSTRAINT, SHAPEKEY_DATA, CONSTRAINT_BONE, CAMERA_STEREO, PACKAGE,
        UGLYPACKAGE, BRUSH_DATA, IMAGE_DATA, FILE, FCURVE, FONT_DATA,
        RENDER_RESULT, SURFACE_DATA, EMPTY_DATA, SETTINGS, RENDER_ANIMATION,
        RENDER_STILL, LIBRARY_DATA_BROKEN, BOIDS, STRANDS,
        LIBRARY_DATA_INDIRECT, GREASEPENCIL, LINE_DATA, GROUP_BONE,
        GROUP_VERTEX, GROUP_VCOL, GROUP_UVS, RNA, RNA_ADD, OUTLINER_OB_EMPTY,
        OUTLINER_OB_MESH, OUTLINER_OB_CURVE, OUTLINER_OB_LATTICE,
        OUTLINER_OB_META, OUTLINER_OB_LAMP, OUTLINER_OB_CAMERA,
        OUTLINER_OB_ARMATURE, OUTLINER_OB_FONT, OUTLINER_OB_SURFACE,
        OUTLINER_OB_SPEAKER, RESTRICT_VIEW_OFF, RESTRICT_VIEW_ON,
        RESTRICT_SELECT_OFF, RESTRICT_SELECT_ON, RESTRICT_RENDER_OFF,
        RESTRICT_RENDER_ON, OUTLINER_DATA_EMPTY, OUTLINER_DATA_MESH,
        OUTLINER_DATA_CURVE, OUTLINER_DATA_LATTICE, OUTLINER_DATA_META,
        OUTLINER_DATA_LAMP, OUTLINER_DATA_CAMERA, OUTLINER_DATA_ARMATURE,
        OUTLINER_DATA_FONT, OUTLINER_DATA_SURFACE, OUTLINER_DATA_SPEAKER,
        OUTLINER_DATA_POSE, MESH_PLANE, MESH_CUBE, MESH_CIRCLE, MESH_UVSPHERE,
        MESH_ICOSPHERE, MESH_GRID, MESH_MONKEY, MESH_CYLINDER, MESH_TORUS,
        MESH_CONE, LAMP_POINT, LAMP_SUN, LAMP_SPOT, LAMP_HEMI, LAMP_AREA,
        META_EMPTY, META_PLANE, META_CUBE, META_BALL, META_ELLIPSOID,
        META_CAPSULE, SURFACE_NCURVE, SURFACE_NCIRCLE, SURFACE_NSURFACE,
        SURFACE_NCYLINDER, SURFACE_NSPHERE, SURFACE_NTORUS, CURVE_BEZCURVE,
        CURVE_BEZCIRCLE, CURVE_NCURVE, CURVE_NCIRCLE, CURVE_PATH, COLOR_RED,
        COLOR_GREEN, COLOR_BLUE, TRIA_RIGHT_BAR, TRIA_DOWN_BAR, TRIA_LEFT_BAR,
        TRIA_UP_BAR, FORCE_FORCE, FORCE_WIND, FORCE_VORTEX, FORCE_MAGNETIC,
        FORCE_HARMONIC, FORCE_CHARGE, FORCE_LENNARDJONES, FORCE_TEXTURE,
        FORCE_CURVE, FORCE_BOID, FORCE_TURBULENCE, FORCE_DRAG,
        FORCE_SMOKEFLOW, NODE_INSERT_ON, NODE_INSERT_OFF, MODIFIER, MOD_WAVE,
        MOD_BUILD, MOD_DECIM, MOD_MIRROR, MOD_SOFT, MOD_SUBSURF, HOOK,
        MOD_PHYSICS, MOD_PARTICLES, MOD_BOOLEAN, MOD_EDGESPLIT, MOD_ARRAY,
        MOD_UVPROJECT, MOD_DISPLACE, MOD_CURVE, MOD_LATTICE, CONSTRAINT_DATA,
        MOD_ARMATURE, MOD_SHRINKWRAP, MOD_CAST, MOD_MESHDEFORM, MOD_BEVEL,
        MOD_SMOOTH, MOD_SIMPLEDEFORM, MOD_MASK, MOD_CLOTH, MOD_EXPLODE,
        MOD_FLUIDSIM, MOD_MULTIRES, MOD_SMOKE, MOD_SOLIDIFY, MOD_SCREW,
        MOD_VERTEX_WEIGHT, MOD_DYNAMICPAINT, MOD_REMESH, MOD_OCEAN, MOD_WARP,
        MOD_SKIN, MOD_TRIANGULATE, MOD_WIREFRAME, MOD_DATA_TRANSFER,
        MOD_NORMALEDIT, REC, PLAY, FF, REW, PAUSE, PREV_KEYFRAME,
        NEXT_KEYFRAME, PLAY_AUDIO, PLAY_REVERSE, PREVIEW_RANGE, ACTION_TWEAK,
        PMARKER_ACT, PMARKER_SEL, PMARKER, MARKER_HLT, MARKER, SPACE2, SPACE3,
        KEYINGSET, KEY_DEHLT, KEY_HLT, MUTE_IPO_OFF, MUTE_IPO_ON,
        VISIBLE_IPO_OFF, VISIBLE_IPO_ON, DRIVER, SOLO_OFF, SOLO_ON,
        FRAME_PREV, FRAME_NEXT, NLA_PUSHDOWN, IPO_CONSTANT, IPO_LINEAR,
        IPO_BEZIER, IPO_SINE, IPO_QUAD, IPO_CUBIC, IPO_QUART, IPO_QUINT,
        IPO_EXPO, IPO_CIRC, IPO_BOUNCE, IPO_ELASTIC, IPO_BACK, IPO_EASE_IN,
        IPO_EASE_OUT, IPO_EASE_IN_OUT, VERTEXSEL, EDGESEL, FACESEL, LOOPSEL,
        ROTATE, CURSOR, ROTATECOLLECTION, ROTATECENTER, ROTACTIVE, ALIGN,
        SMOOTHCURVE, SPHERECURVE, ROOTCURVE, SHARPCURVE, LINCURVE, NOCURVE,
        RNDCURVE, PROP_OFF, PROP_ON, PROP_CON, SCULPT_DYNTOPO, PARTICLE_POINT,
        PARTICLE_TIP, PARTICLE_PATH, MAN_TRANS, MAN_ROT, MAN_SCALE, MANIPUL,
        SNAP_OFF, SNAP_ON, SNAP_NORMAL, SNAP_GRID, SNAP_VERTEX, SNAP_EDGE,
        SNAP_FACE, SNAP_VOLUME, SNAP_INCREMENT, STICKY_UVS_LOC,
        STICKY_UVS_DISABLE, STICKY_UVS_VERT, CLIPUV_DEHLT, CLIPUV_HLT,
        SNAP_PEEL_OBJECT, GRID, PASTEDOWN, COPYDOWN, PASTEFLIPUP,
        PASTEFLIPDOWN, SNAP_SURFACE, AUTOMERGE_ON, AUTOMERGE_OFF, RETOPO,
        UV_VERTEXSEL, UV_EDGESEL, UV_FACESEL, UV_ISLANDSEL, UV_SYNC_SELECT,
        BBOX, WIRE, SOLID, SMOOTH, POTATO, ORTHO, LOCKVIEW_OFF, LOCKVIEW_ON,
        AXIS_SIDE, AXIS_FRONT, AXIS_TOP, NDOF_DOM, NDOF_TURN, NDOF_FLY,
        NDOF_TRANS, LAYER_USED, LAYER_ACTIVE, SORTALPHA, SORTBYEXT, SORTTIME,
        SORTSIZE, LONGDISPLAY, SHORTDISPLAY, GHOST, IMGDISPLAY, SAVE_AS,
        SAVE_COPY, BOOKMARKS, FONTPREVIEW, FILTER, NEWFOLDER, OPEN_RECENT,
        FILE_PARENT, FILE_REFRESH, FILE_FOLDER, FILE_BLANK, FILE_BLEND,
        FILE_IMAGE, FILE_MOVIE, FILE_SCRIPT, FILE_SOUND, FILE_FONT, FILE_TEXT,
        RECOVER_AUTO, SAVE_PREFS, LINK_BLEND, APPEND_BLEND, IMPORT, EXPORT,
        EXTERNAL_DATA, LOAD_FACTORY, LOOP_BACK, LOOP_FORWARDS, BACK, FORWARD,
        FILE_HIDDEN, FILE_BACKUP, DISK_DRIVE, MATPLANE, MATSPHERE, MATCUBE,
        MONKEY, HAIR, ALIASED, ANTIALIASED, MAT_SPHERE_SKY, WORDWRAP_OFF,
        WORDWRAP_ON, SYNTAX_OFF, SYNTAX_ON, LINENUMBERS_OFF, LINENUMBERS_ON,
        SCRIPTPLUGINS, SEQ_SEQUENCER, SEQ_PREVIEW, SEQ_LUMA_WAVEFORM,
        SEQ_CHROMA_SCOPE, SEQ_HISTOGRAM, SEQ_SPLITVIEW, IMAGE_RGB,
        IMAGE_RGB_ALPHA, IMAGE_ALPHA, IMAGE_ZDEPTH, IMAGEFILE, BRUSH_ADD,
        BRUSH_BLOB, BRUSH_BLUR, BRUSH_CLAY, BRUSH_CLAY_STRIPS, BRUSH_CLONE,
        BRUSH_CREASE, BRUSH_DARKEN, BRUSH_FILL, BRUSH_FLATTEN, BRUSH_GRAB,
        BRUSH_INFLATE, BRUSH_LAYER, BRUSH_LIGHTEN, BRUSH_MASK, BRUSH_MIX,
        BRUSH_MULTIPLY, BRUSH_NUDGE, BRUSH_PINCH, BRUSH_SCRAPE,
        BRUSH_SCULPT_DRAW, BRUSH_SMEAR, BRUSH_SMOOTH, BRUSH_SNAKE_HOOK,
        BRUSH_SOFTEN, BRUSH_SUBTRACT, BRUSH_TEXDRAW, BRUSH_TEXFILL,
        BRUSH_TEXMASK, BRUSH_THUMB, BRUSH_ROTATE, BRUSH_VERTEXDRAW, MATCAP_01,
        MATCAP_02, MATCAP_03, MATCAP_04, MATCAP_05, MATCAP_06, MATCAP_07,
        MATCAP_08, MATCAP_09, MATCAP_10, MATCAP_11, MATCAP_12, MATCAP_13,
        MATCAP_14, MATCAP_15, MATCAP_16, MATCAP_17, MATCAP_18, MATCAP_19,
        MATCAP_20, MATCAP_21, MATCAP_22, MATCAP_23, MATCAP_24]'''
        return str()
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
    def interface_update(self, context):
        '''Updated node group interface
        
        Parameter:
          context: (Context)'''
        return 
    def poll(self, context):
        '''Check visibility in the editor
        
        Parameter:
          context: (Context)
        
        Returns:
          visible: (Boolean)'''
        return bool()
    def update(self):
        '''Update on editor changes'''
        return 
    def get_from_context(self, context):
        '''Get a node tree from the context
        
        Parameter:
          context: (Context)
        
        Returns:
          result_1: (NodeTree) Active node tree from context
          result_2: (ID) ID data block that owns the node tree
          result_3: (ID) Original ID data block selected from the context'''
        return NodeTree(), ID(), ID()