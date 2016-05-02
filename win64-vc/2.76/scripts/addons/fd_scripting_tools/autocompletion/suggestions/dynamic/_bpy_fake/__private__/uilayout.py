from . movieclipuser import MovieClipUser
from . textureslot import TextureSlot
from . imageuser import ImageUser
from . stereo3dformat import Stereo3dFormat
from . movietrackingtrack import MovieTrackingTrack
from . nodetree import NodeTree
from . operatorproperties import OperatorProperties
from . node import Node
from . uilayout import UILayout
from . id import ID
from . struct import Struct
from . imageformatsettings import ImageFormatSettings
from . image import Image
from . anytype import AnyType
from . nodesocket import NodeSocket
from . keymapitem import KeyMapItem
from . constraint import Constraint
from . modifier import Modifier
from . bpy_struct import bpy_struct
import mathutils

class UILayout(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(Boolean)'''
        return bool()
    @property
    def operator_context(self):
        '''(Enum)
        
        [INVOKE_DEFAULT, INVOKE_REGION_WIN, INVOKE_REGION_CHANNELS,
        INVOKE_REGION_PREVIEW, INVOKE_AREA, INVOKE_SCREEN, EXEC_DEFAULT,
        EXEC_REGION_WIN, EXEC_REGION_CHANNELS, EXEC_REGION_PREVIEW, EXEC_AREA,
        EXEC_SCREEN]'''
        return str()
    @property
    def enabled(self):
        '''(Boolean) When false, this (sub)layout is grayed out'''
        return bool()
    @property
    def alert(self):
        '''(Boolean)'''
        return bool()
    @property
    def alignment(self):
        '''(Enum)
        
        [EXPAND, LEFT, CENTER, RIGHT]'''
        return str()
    @property
    def scale_x(self):
        '''(Float) Scale factor along the X for items in this (sub)layout'''
        return float()
    @property
    def scale_y(self):
        '''(Float) Scale factor along the Y for items in this (sub)layout'''
        return float()
    def row(self, align):
        '''Sub-layout. Items placed in this sublayout are placed next to each
        other in a row
        
        Parameter:
          align: (Boolean) Align buttons to each other
        
        Returns:
          layout: (UILayout) Sub-layout to put items in'''
        return UILayout()
    def column(self, align):
        '''Sub-layout. Items placed in this sublayout are placed under each other
        in a column
        
        Parameter:
          align: (Boolean) Align buttons to each other
        
        Returns:
          layout: (UILayout) Sub-layout to put items in'''
        return UILayout()
    def column_flow(self, columns, align):
        '''column_flow
        
        Parameter:
          columns: (Integer) Number of columns, 0 is automatic
          align: (Boolean) Align buttons to each other
        
        Returns:
          layout: (UILayout) Sub-layout to put items in'''
        return UILayout()
    def box(self):
        '''Sublayout (items placed in this sublayout are placed under each other
        in a column and are surrounded by a box)
        
        Returns:
          layout: (UILayout) Sub-layout to put items in'''
        return UILayout()
    def split(self, percentage, align):
        '''split
        
        Parameter:
          percentage: (Float) Percentage of width to split at
          align: (Boolean) Align buttons to each other
        
        Returns:
          layout: (UILayout) Sub-layout to put items in'''
        return UILayout()
    def menu_pie(self):
        '''Sublayout. Items placed in this sublayout are placed in a radial
        fashion around the menu center)
        
        Returns:
          layout: (UILayout) Sub-layout to put items in'''
        return UILayout()
    def icon(self, data):
        '''Return the custom icon for this data, use it e.g. to get materials or
        texture icons
        
        Parameter:
          data: (AnyType) Data from which to take the icon
        
        Returns:
          icon_value: (Integer) Icon identifier'''
        return int()
    def enum_item_name(self, data, property, identifier):
        '''Return the UI name for this enum item
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data
          identifier: (String) Identifier of the enum item
        
        Returns:
          name: (String) UI name of the enum item'''
        return str()
    def enum_item_description(self, data, property, identifier):
        '''Return the UI description for this enum item
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data
          identifier: (String) Identifier of the enum item
        
        Returns:
          description: (String) UI description of the enum item'''
        return str()
    def enum_item_icon(self, data, property, identifier):
        '''Return the icon for this enum item
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data
          identifier: (String) Identifier of the enum item
        
        Returns:
          icon_value: (Integer) Icon identifier'''
        return int()
    def prop(self, data, property, text, text_ctxt, translate, icon, expand, slider, toggle, icon_only, event, full_event, emboss, index, icon_value):
        '''Item. Exposes an RNA item and places it into the layout
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data
          text: (String) Override automatic text of the item
          text_ctxt: (String) Override automatic translation context of the given text
          translate: (Boolean) Translate the given text, when UI translation is enabled
          icon: (Enum) Override automatic icon of the item
          expand: (Boolean) Expand button to show more detail
          slider: (Boolean) Use slider widget for numeric values
          toggle: (Boolean) Use toggle widget for boolean values
          icon_only: (Boolean) Draw only icons in buttons, no text
          event: (Boolean) Use button to input key events
          full_event: (Boolean) Use button to input full events including modifiers
          emboss: (Boolean) Draw the button itself, just the icon/text
          index:
            (Integer) The index of this button, when set a single member of an
            array can be accessed, when set to -1 all array members are used
          icon_value: (Integer) Override automatic icon of the item'''
        return 
    def props_enum(self, data, property):
        '''props_enum
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data'''
        return 
    def prop_menu_enum(self, data, property, text, text_ctxt, translate, icon):
        '''prop_menu_enum
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data
          text: (String) Override automatic text of the item
          text_ctxt: (String) Override automatic translation context of the given text
          translate: (Boolean) Translate the given text, when UI translation is enabled
          icon: (Enum) Override automatic icon of the item'''
        return 
    def prop_enum(self, data, property, value, text, text_ctxt, translate, icon):
        '''prop_enum
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data
          value: (String) Enum property value
          text: (String) Override automatic text of the item
          text_ctxt: (String) Override automatic translation context of the given text
          translate: (Boolean) Translate the given text, when UI translation is enabled
          icon: (Enum) Override automatic icon of the item'''
        return 
    def prop_search(self, data, property, search_data, search_property, text, text_ctxt, translate, icon):
        '''prop_search
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data
          search_data: (AnyType) Data from which to take collection to search in
          search_property: (String) Identifier of search collection property
          text: (String) Override automatic text of the item
          text_ctxt: (String) Override automatic translation context of the given text
          translate: (Boolean) Translate the given text, when UI translation is enabled
          icon: (Enum) Override automatic icon of the item'''
        return 
    def operator(self, operator, text, text_ctxt, translate, icon, emboss, icon_value):
        '''Item. Places a button into the layout to call an Operator
        
        Parameter:
          operator: (String) Identifier of the operator
          text: (String) Override automatic text of the item
          text_ctxt: (String) Override automatic translation context of the given text
          translate: (Boolean) Translate the given text, when UI translation is enabled
          icon: (Enum) Override automatic icon of the item
          emboss: (Boolean) Draw the button itself, just the icon/text
          icon_value: (Integer) Override automatic icon of the item
        
        Returns:
          properties:
            (OperatorProperties) Operator properties to fill in, return when
            'properties' is set to true'''
        return OperatorProperties()
    def operator_enum(self, operator, property):
        '''operator_enum
        
        Parameter:
          operator: (String) Identifier of the operator
          property: (String) Identifier of property in operator'''
        return 
    def operator_menu_enum(self, operator, property, text, text_ctxt, translate, icon):
        '''operator_menu_enum
        
        Parameter:
          operator: (String) Identifier of the operator
          property: (String) Identifier of property in operator
          text: (String) Override automatic text of the item
          text_ctxt: (String) Override automatic translation context of the given text
          translate: (Boolean) Translate the given text, when UI translation is enabled
          icon: (Enum) Override automatic icon of the item'''
        return 
    def label(self, text, text_ctxt, translate, icon, icon_value):
        '''Item. Display text and/or icon in the layout
        
        Parameter:
          text: (String) Override automatic text of the item
          text_ctxt: (String) Override automatic translation context of the given text
          translate: (Boolean) Translate the given text, when UI translation is enabled
          icon: (Enum) Override automatic icon of the item
          icon_value: (Integer) Override automatic icon of the item'''
        return 
    def menu(self, menu, text, text_ctxt, translate, icon, icon_value):
        '''menu
        
        Parameter:
          menu: (String) Identifier of the menu
          text: (String) Override automatic text of the item
          text_ctxt: (String) Override automatic translation context of the given text
          translate: (Boolean) Translate the given text, when UI translation is enabled
          icon: (Enum) Override automatic icon of the item
          icon_value: (Integer) Override automatic icon of the item'''
        return 
    def separator(self):
        '''Item. Inserts empty space into the layout between items'''
        return 
    def context_pointer_set(self, name, data):
        '''context_pointer_set
        
        Parameter:
          name: (String) Name of entry in the context
          data: (AnyType) Pointer to put in context'''
        return 
    def template_header(self):
        '''template_header'''
        return 
    def template_ID(self, data, property, new, open, unlink):
        '''template_ID
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data
          new: (String) Operator identifier to create a new ID block
          open:
            (String) Operator identifier to open a file for creating a new ID
            block
          unlink: (String) Operator identifier to unlink the ID block'''
        return 
    def template_ID_preview(self, data, property, new, open, unlink, rows, cols):
        '''template_ID_preview
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data
          new: (String) Operator identifier to create a new ID block
          open:
            (String) Operator identifier to open a file for creating a new ID
            block
          unlink: (String) Operator identifier to unlink the ID block
          rows: (Integer)
          cols: (Integer)'''
        return 
    def template_any_ID(self, data, property, type_property, text, text_ctxt, translate):
        '''template_any_ID
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data
          type_property:
            (String) Identifier of property in data giving the type of the ID-
            blocks to use
          text: (String) Override automatic text of the item
          text_ctxt: (String) Override automatic translation context of the given text
          translate: (Boolean) Translate the given text, when UI translation is enabled'''
        return 
    def template_path_builder(self, data, property, root, text, text_ctxt, translate):
        '''template_path_builder
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data
          root: (ID) ID-block from which path is evaluated from
          text: (String) Override automatic text of the item
          text_ctxt: (String) Override automatic translation context of the given text
          translate: (Boolean) Translate the given text, when UI translation is enabled'''
        return 
    def template_modifier(self, data):
        '''Generates the UI layout for modifiers
        
        Parameter:
          data: (Modifier) Modifier data
        
        Returns:
          layout: (UILayout) Sub-layout to put items in'''
        return UILayout()
    def template_constraint(self, data):
        '''Generates the UI layout for constraints
        
        Parameter:
          data: (Constraint) Constraint data
        
        Returns:
          layout: (UILayout) Sub-layout to put items in'''
        return UILayout()
    def template_preview(self, id, show_buttons, parent, slot, preview_id):
        '''Item. A preview window for materials, textures, lamps or worlds
        
        Parameter:
          id: (ID) ID datablock
          show_buttons: (Boolean) Show preview buttons?
          parent: (ID) ID datablock
          slot: (TextureSlot) Texture slot
          preview_id:
            (String) Identifier of this preview widget, if not set the ID type
            will be used (i.e. all previews of materials without explicit ID will
            have the same size...)'''
        return 
    def template_curve_mapping(self, data, property, type, levels, brush, use_negative_slope):
        '''Item. A curve mapping widget used for e.g falloff curves for lamps
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data
          type: (Enum) Type of curves to display
          levels: (Boolean) Show black/white levels
          brush: (Boolean) Show brush options
          use_negative_slope: (Boolean) Use a negative slope by default'''
        return 
    def template_color_ramp(self, data, property, expand):
        '''Item. A color ramp widget
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data
          expand: (Boolean) Expand button to show more detail'''
        return 
    def template_icon_view(self, data, property, show_labels, scale):
        '''Enum. Large widget showing Icon previews
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data
          show_labels: (Boolean) Show enum label in preview buttons
          scale: (Float) Scale the icon size (by the button size)'''
        return 
    def template_histogram(self, data, property):
        '''Item. A histogramm widget to analyze imaga data
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data'''
        return 
    def template_waveform(self, data, property):
        '''Item. A waveform widget to analyze imaga data
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data'''
        return 
    def template_vectorscope(self, data, property):
        '''Item. A vectorscope widget to analyze imaga data
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data'''
        return 
    def template_layers(self, data, property, used_layers_data, used_layers_property, active_layer):
        '''template_layers
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data
          used_layers_data: (AnyType) Data from which to take property
          used_layers_property: (String) Identifier of property in data
          active_layer: (Integer)'''
        return 
    def template_color_picker(self, data, property, value_slider, lock, lock_luminosity, cubic):
        '''Item. A color wheel widget to pick colors
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data
          value_slider: (Boolean) Display the value slider to the right of the color wheel
          lock:
            (Boolean) Lock the color wheel display to value 1.0 regardless of
            actual color
          lock_luminosity: (Boolean) Keep the color at its original vector length
          cubic: (Boolean) Cubic saturation for picking values close to white'''
        return 
    def template_palette(self, data, property, color):
        '''Item. A palette used to pick colors
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data
          color: (Boolean) Display the colors as colors or values'''
        return 
    def template_image_layers(self, image, image_user):
        '''template_image_layers
        
        Parameter:
          image: (Image)
          image_user: (ImageUser)'''
        return 
    def template_image(self, data, property, image_user, compact, multiview):
        '''Item(s). User interface for selecting images and their source paths
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data
          image_user: (ImageUser)
          compact: (Boolean) Use more compact layout
          multiview: (Boolean) Expose Multi-View options'''
        return 
    def template_image_settings(self, image_settings, color_management):
        '''User interface for setting image format options
        
        Parameter:
          image_settings: (ImageFormatSettings)
          color_management: (Boolean) Show color management settings'''
        return 
    def template_image_stereo_3d(self, stereo_3d_format):
        '''User interface for setting image stereo 3d options
        
        Parameter:
          stereo_3d_format: (Stereo3dFormat)'''
        return 
    def template_image_views(self, image_settings):
        '''User interface for setting image views output options
        
        Parameter:
          image_settings: (ImageFormatSettings)'''
        return 
    def template_movieclip(self, data, property, compact):
        '''Item(s). User interface for selecting movie clips and their source
        paths
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data
          compact: (Boolean) Use more compact layout'''
        return 
    def template_track(self, data, property):
        '''Item. A movie-track widget to preview tracking image.
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data'''
        return 
    def template_marker(self, data, property, clip_user, track, compact):
        '''Item. A widget to control single marker settings.
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data
          clip_user: (MovieClipUser)
          track: (MovieTrackingTrack)
          compact: (Boolean) Use more compact layout'''
        return 
    def template_movieclip_information(self, data, property, clip_user):
        '''Item. Movie clip information data.
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data
          clip_user: (MovieClipUser)'''
        return 
    def template_list(self, listtype_name, list_id, dataptr, propname, active_dataptr, active_propname, item_dyntip_propname, rows, maxrows, type, columns):
        '''Item. A list widget to display data, e.g. vertexgroups.
        
        Parameter:
          listtype_name: (String) Identifier of the list type to use
          list_id:
            (String) Identifier of this list widget (mandatory when using default
            "UI_UL_list" class). If this is set, the uilist gets a custom ID,
            otherwise it takes the name of the class used to define the uilist
            (for example, if the class name is "OBJECT_UL_vgroups", and list_id is
            not set by the script, then bl_idname = "OBJECT_UL_vgroups")
          dataptr: (AnyType) Data from which to take the Collection property
          propname: (String) Identifier of the Collection property in data
          active_dataptr:
            (AnyType) Data from which to take the integer property, index of the
            active item
          active_propname:
            (String) Identifier of the integer property in active_data, index of
            the active item
          item_dyntip_propname:
            (String) Identifier of a string property in items, to use as tooltip
            content
          rows: (Integer) Default and minimum number of rows to display
          maxrows: (Integer) Default maximum number of rows to display
          type: (Enum) Type of layout to use
          columns: (Integer) Number of items to display per row, for GRID layout'''
        return 
    def template_running_jobs(self):
        '''template_running_jobs'''
        return 
    def template_operator_search(self):
        '''template_operator_search'''
        return 
    def template_header_3D(self):
        '''template_header_3D'''
        return 
    def template_edit_mode_selection(self):
        '''template_edit_mode_selection'''
        return 
    def template_reports_banner(self):
        '''template_reports_banner'''
        return 
    def template_node_link(self, ntree, node, socket):
        '''template_node_link
        
        Parameter:
          ntree: (NodeTree)
          node: (Node)
          socket: (NodeSocket)'''
        return 
    def template_node_view(self, ntree, node, socket):
        '''template_node_view
        
        Parameter:
          ntree: (NodeTree)
          node: (Node)
          socket: (NodeSocket)'''
        return 
    def template_texture_user(self):
        '''template_texture_user'''
        return 
    def template_keymap_item_properties(self, item):
        '''template_keymap_item_properties
        
        Parameter:
          item: (KeyMapItem)'''
        return 
    def template_component_menu(self, data, property, name):
        '''Item. Display expanded property in a popup menu
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data
          name: (String)'''
        return 
    def introspect(self):
        '''introspect
        
        Returns:
          string: (String) DESCR'''
        return str()
    def template_colorspace_settings(self, data, property):
        '''Item. A widget to control input color space settings.
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data'''
        return 
    def template_colormanaged_view_settings(self, data, property):
        '''Item. A widget to control color managed view settings settings.
        
        Parameter:
          data: (AnyType) Data from which to take property
          property: (String) Identifier of property in data'''
        return 
    def template_node_socket(self, color):
        '''Node Socket Icon
        
        Parameter:
          color: (Float[4])'''
        return 