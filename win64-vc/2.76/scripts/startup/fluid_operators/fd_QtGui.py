'''
Created on Feb 25, 2016

@author: montes
'''

import bpy
from bpy.types import Header, Menu, Operator, PropertyGroup
import math
from PyQt4 import QtGui
from . import myQMainWindow
import sys
import os

from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       BoolVectorProperty,
                       PointerProperty,
                       EnumProperty,
                       CollectionProperty)

import fd

class ExampleApp(QtGui.QMainWindow, myQMainWindow.Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        
        self.btnBrowse.clicked.connect(self.browse_folder)
        
    def browse_folder(self):
        self.listWidget.clear()
        dir = QtGui.QFileDialog.getExistingDirectory(self,"Fluid")
        
        if dir:
            for file_name in os.listdir(dir):
                self.listWidget.addItem(file_name)
                
class OPS_call_qt_gui(Operator):
    bl_idname = "fd_qtgui.call_gui"
    bl_label = "Call QtGui"

    def execute(self, context):
        app = QtGui.QApplication(sys.argv)
        form = ExampleApp()
        form.show()
        app.exec_()        

#------REGISTER
classes = [
           OPS_call_qt_gui,
           ]

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

if __name__ == "__main__":
    register()