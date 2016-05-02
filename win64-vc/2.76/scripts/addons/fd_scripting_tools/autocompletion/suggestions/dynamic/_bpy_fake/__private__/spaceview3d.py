from . spaceview3d import SpaceView3D
from . struct import Struct
from . transformorientation import TransformOrientation
from . backgroundimages import BackgroundImages
from . gpufxsettings import GPUFXSettings
from . object import Object
from . regionview3d import RegionView3D
from . bpy_struct import bpy_struct
import mathutils

class SpaceView3D(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def type(self):
        '''(Enum) Space data type
        
        [EMPTY, VIEW_3D, TIMELINE, GRAPH_EDITOR, DOPESHEET_EDITOR, NLA_EDITOR,
        IMAGE_EDITOR, SEQUENCE_EDITOR, CLIP_EDITOR, TEXT_EDITOR, NODE_EDITOR,
        LOGIC_EDITOR, PROPERTIES, OUTLINER, USER_PREFERENCES, INFO,
        FILE_BROWSER, CONSOLE]'''
        return str()
    @property
    def show_locked_time(self):
        '''(Boolean)'''
        return bool()
    @property
    def camera(self):
        '''(Object) Active camera used in this view (when unlocked from the
        scene's active camera)'''
        return Object()
    @property
    def use_render_border(self):
        '''(Boolean) Use a region within the frame size for rendered viewport
        (when not viewing through the camera)'''
        return bool()
    @property
    def render_border_min_x(self):
        '''(Float) Minimum X value for the render border'''
        return float()
    @property
    def render_border_min_y(self):
        '''(Float) Minimum Y value for the render border'''
        return float()
    @property
    def render_border_max_x(self):
        '''(Float) Maximum X value for the render border'''
        return float()
    @property
    def render_border_max_y(self):
        '''(Float) Maximum Y value for the render border'''
        return float()
    @property
    def lock_object(self):
        '''(Object) 3D View center is locked to this object's position'''
        return Object()
    @property
    def lock_bone(self):
        '''(String) 3D View center is locked to this bone's position'''
        return str()
    @property
    def lock_cursor(self):
        '''(Boolean) 3D View center is locked to the cursor's position'''
        return bool()
    @property
    def viewport_shade(self):
        '''(Enum) Method to display/shade objects in the 3D View
        
        [BOUNDBOX, WIREFRAME, SOLID, TEXTURED, MATERIAL, RENDERED]'''
        return str()
    @property
    def local_view(self):
        '''(SpaceView3D) Display an isolated sub-set of objects, apart from the
        scene visibility'''
        return SpaceView3D()
    @property
    def cursor_location(self):
        '''(Vector 3D) 3D cursor location for this view (dependent on local view
        setting)'''
        return mathutils.Vector()
    @property
    def lens(self):
        '''(Float) Viewport lens angle'''
        return float()
    @property
    def clip_start(self):
        '''(Float) 3D View near clipping distance (perspective view only)'''
        return float()
    @property
    def clip_end(self):
        '''(Float) 3D View far clipping distance'''
        return float()
    @property
    def grid_scale(self):
        '''(Float) Distance between 3D View grid lines'''
        return float()
    @property
    def grid_lines(self):
        '''(Integer) Number of grid lines to display in perspective view'''
        return int()
    @property
    def grid_subdivisions(self):
        '''(Integer) Number of subdivisions between grid lines'''
        return int()
    @property
    def grid_scale_unit(self):
        '''(Float) Grid cell size scaled by scene unit system settings'''
        return float()
    @property
    def show_floor(self):
        '''(Boolean) Show the ground plane grid in perspective view'''
        return bool()
    @property
    def show_axis_x(self):
        '''(Boolean) Show the X axis line in perspective view'''
        return bool()
    @property
    def show_axis_y(self):
        '''(Boolean) Show the Y axis line in perspective view'''
        return bool()
    @property
    def show_axis_z(self):
        '''(Boolean) Show the Z axis line in perspective view'''
        return bool()
    @property
    def show_outline_selected(self):
        '''(Boolean) Show an outline highlight around selected objects in non-
        wireframe views'''
        return bool()
    @property
    def show_all_objects_origin(self):
        '''(Boolean) Show the object origin center dot for all (selected and
        unselected) objects'''
        return bool()
    @property
    def show_relationship_lines(self):
        '''(Boolean) Show dashed lines indicating parent or constraint
        relationships'''
        return bool()
    @property
    def show_grease_pencil(self):
        '''(Boolean) Show grease pencil for this view'''
        return bool()
    @property
    def show_textured_solid(self):
        '''(Boolean) Display face-assigned textures in solid view'''
        return bool()
    @property
    def show_backface_culling(self):
        '''(Boolean) Use back face culling to hide the back side of faces'''
        return bool()
    @property
    def show_textured_shadeless(self):
        '''(Boolean) Show shadeless texture without lighting in textured draw
        mode'''
        return bool()
    @property
    def show_occlude_wire(self):
        '''(Boolean) Use hidden wireframe display'''
        return bool()
    @property
    def lock_camera(self):
        '''(Boolean) Enable view navigation within the camera view'''
        return bool()
    @property
    def show_only_render(self):
        '''(Boolean) Display only objects which will be rendered'''
        return bool()
    @property
    def show_world(self):
        '''(Boolean) Display world colors in the background'''
        return bool()
    @property
    def use_occlude_geometry(self):
        '''(Boolean) Limit selection to visible (clipped with depth buffer)'''
        return bool()
    @property
    def background_images(self):
        '''(Sequence of BackgroundImage) List of background images'''
        return BackgroundImages()
    @property
    def show_background_images(self):
        '''(Boolean) Display reference images behind objects in the 3D View'''
        return bool()
    @property
    def pivot_point(self):
        '''(Enum) Pivot center for rotation/scaling
        
        [BOUNDING_BOX_CENTER, CURSOR, INDIVIDUAL_ORIGINS, MEDIAN_POINT,
        ACTIVE_ELEMENT]'''
        return str()
    @property
    def use_pivot_point_align(self):
        '''(Boolean) Manipulate center points (object and pose mode only)'''
        return bool()
    @property
    def show_manipulator(self):
        '''(Boolean) Use a 3D manipulator widget for controlling transforms'''
        return bool()
    @property
    def transform_manipulators(self):
        '''(Enum) Transformation manipulators
        
        [TRANSLATE, ROTATE, SCALE]'''
        return str()
    @property
    def transform_orientation(self):
        '''(Enum) Transformation orientation
        
        [GLOBAL, LOCAL, NORMAL, GIMBAL, VIEW]'''
        return str()
    @property
    def current_orientation(self):
        '''(TransformOrientation) Current transformation orientation'''
        return TransformOrientation()
    @property
    def lock_camera_and_layers(self):
        '''(Boolean) Use the scene's active camera and layers in this view,
        rather than local layers'''
        return bool()
    @property
    def layers(self):
        '''(Boolean[20]) Layers visible in this 3D View'''
        return bool()
    @property
    def layers_local_view(self):
        '''(Boolean[8]) Local view layers visible in this 3D View'''
        return bool()
    @property
    def layers_used(self):
        '''(Boolean[20]) Layers that contain something'''
        return bool()
    @property
    def region_3d(self):
        '''(RegionView3D) 3D region in this space, in case of quad view the
        camera region'''
        return RegionView3D()
    @property
    def region_quadviews(self):
        '''(Sequence of RegionView3D) 3D regions (the third one defines quad view
        settings, the forth one is same as 'region_3d')'''
        return (RegionView3D(),)
    @property
    def show_reconstruction(self):
        '''(Boolean) Display reconstruction data from active movie clip'''
        return bool()
    @property
    def tracks_draw_size(self):
        '''(Float) Display size of tracks from reconstructed data'''
        return float()
    @property
    def tracks_draw_type(self):
        '''(Enum) Viewport display style for tracks
        
        [PLAIN_AXES, ARROWS, SINGLE_ARROW, CIRCLE, CUBE, SPHERE, CONE]'''
        return str()
    @property
    def show_camera_path(self):
        '''(Boolean) Show reconstructed camera path'''
        return bool()
    @property
    def show_bundle_names(self):
        '''(Boolean) Show names for reconstructed tracks objects'''
        return bool()
    @property
    def use_matcap(self):
        '''(Boolean) Active Objects draw images mapped on normals, enhancing
        Solid Draw Mode'''
        return bool()
    @property
    def matcap_icon(self):
        '''(Enum) Image to use for Material Capture, active objects only
        
        [01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17,
        18, 19, 20, 21, 22, 23, 24]'''
        return str()
    @property
    def fx_settings(self):
        '''(GPUFXSettings) Options used for real time compositing'''
        return GPUFXSettings()
    @property
    def stereo_3d_eye(self):
        '''(Enum) Current stereo eye being drawn
        
        [LEFT_EYE, RIGHT_EYE]'''
        return str()
    @property
    def stereo_3d_camera(self):
        '''(Enum)
        
        [LEFT, RIGHT, S3D]'''
        return str()
    @property
    def show_stereo_3d_cameras(self):
        '''(Boolean) Show the left and right cameras'''
        return bool()
    @property
    def show_stereo_3d_convergence_plane(self):
        '''(Boolean) Show the stereo 3d convergence plane'''
        return bool()
    @property
    def stereo_3d_convergence_plane_alpha(self):
        '''(Float) Opacity (alpha) of the convergence plane'''
        return float()
    @property
    def show_stereo_3d_volume(self):
        '''(Boolean) Show the stereo 3d frustum volume'''
        return bool()
    @property
    def stereo_3d_volume_alpha(self):
        '''(Float) Opacity (alpha) of the cameras' frustum volume'''
        return float()