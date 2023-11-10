import maya.cmds as cmds
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui

class RenameTool(QDialog):
    def __init__(self, *args, **kwargs):
        super(RenameTool, self).__init__(*args, **kwargs)
  
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.resize(300,150)
        self.setWindowTitle('Rename Tool')
        
        self.init_input_widget()
        self.init_opt_widget()
        
        self.main_layout.addWidget(self.main_opt_widget)
        self.main_layout.addWidget(self.name_widget)
        
    def init_input_widget(self):
        self.name_widget = QWidget()
        self.name_layout = QGridLayout()
        self.name_widget.setLayout(self.name_layout)
        self.main_layout.addWidget(self.name_widget)
            
        self.name_label = QLabel('Name :')
        self.name_LineEdit = QLineEdit()
        
        self.prefix_label = QLabel('Prefix :')
        
        self.Side_label = QLabel('Side :')
        self.Side_combobox = QComboBox()
        self.Side_combobox.addItems(['None','MID', 'L', 'R'])
        
        self.Suffix_label = QLabel('Suffix :')
        self.Suffix_combobox = QComboBox()
        self.Suffix_combobox.addItems(['None','grp','geo','jnt','Ik'])
            
        self.name_layout.addWidget(self.name_label,0,0)
        self.name_layout.addWidget(self.name_LineEdit,0,1)
        
        self.name_layout.addWidget(self.Side_label,1 ,0)
        self.name_layout.addWidget(self.Side_combobox,1,1)
        
        self.name_layout.addWidget(self.Suffix_label, 2, 0)
        self.name_layout.addWidget(self.Suffix_combobox, 2, 1)
       
    def init_opt_widget(self):
        self.main_opt_widget = QWidget()
        self.main_opt_layout = QHBoxLayout()
        self.main_opt_widget.setLayout(self.main_opt_layout)
        
        self.ok_button = QPushButton("Rename")
        self.ok_button.setMinimumHeight(30)
        self.main_opt_layout.addWidget(self.ok_button)
        self.ok_button.clicked.connect(self.nameFn)
        
        self.no_button = QPushButton("Cancel")
        self.no_button.setMinimumHeight(30)
        self.main_opt_layout.addWidget(self.no_button)
        self.no_button.clicked.connect(self.closeUI)
        
        self.setWindowOpacity(1)      
        
    def nameFn(self):
        name = self.name_LineEdit.text()
        side = self.Side_combobox.currentText()
        suffix = self.Suffix_combobox.currentText()
        sels = cmds.ls(sl = True)
        for i,each in enumerate(sels):
            if side == 'None':
                New_name = '{}_{}'.format(name, suffix)
            if suffix == 'None':
                New_name = '{}_{}'.format(side, name)
            if side == 'None' and suffix == 'None':
                New_name = '{}'.format(name)
            if not side == 'None' and not suffix == 'None':
                New_name = '{}_{}_{}'.format(side, name, suffix)
                
            cmds.rename(each, New_name)
        
    def closeUI(self):
        self.close() 
            

global ui
try:
    ui.close()
except:
    pass
        
maya_ptr = omui.MQtUtil.mainWindow()
ptr = wrapInstance(int(maya_ptr), QWidget)

ui = RenameTool(parent = ptr)
ui.show()