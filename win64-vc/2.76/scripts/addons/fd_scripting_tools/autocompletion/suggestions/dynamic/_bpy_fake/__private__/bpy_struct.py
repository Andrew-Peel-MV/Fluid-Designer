
from . fcurve import FCurve

class bpy_struct:
    id_data = ID()
    def as_pointer():
        return int()
    def driver_add(path, index):
        return FCurve()
    def driver_remove(path, index):
        return bool()
    def keyframe_delete(data_path, index, frame, group):
        return bool()
    def keyframe_insert(data_path, index, frame, group):
        return bool()
    def path_from_id(property):
        return str()
    def path_resolve(path, coerce):
        return
    def property_unsert(property):
        return
