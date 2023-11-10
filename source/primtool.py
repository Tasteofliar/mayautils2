import maya.cmds as cmds
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui

class polygonTool(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(polygonTool, self).__init__(*args, **kwargs)
        self.resize(300,100)
        self.setWindowTitle('Primitive Tool')
        
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        
        self.init_input_widget()
        self.init_opt_widget()

        self.main_layout.addWidget(self.main_input_widget)
        self.main_layout.addWidget(self.main_opt_widget)
        
    def init_input_widget(self):
        self.main_input_widget = QWidget()
        self.main_input_layout = QGridLayout()
        self.main_input_widget.setLayout(self.main_input_layout)

        self.name_label = QLabel('Name : ')
        self.name_LineEdit = QLineEdit()
        self.name_LineEdit.setMinimumHeight(30)
        self.name_LineEdit.setFixedWidth(150)
        
        self.amount_label = QLabel('Amount : ')
        self.amount_spinbox = QSpinBox()
        self.amount_spinbox.setMinimumHeight(30)
        
        self.suffix_label = QLabel('Suffix : ')
        self.suffix_LineEdit = QLineEdit()
        self.suffix_LineEdit.setMinimumHeight(30)
        
        self.Or = QLabel('or')
        
        self.suffix_comboBox = QComboBox()
        self.suffix_comboBox.addItems(['please select','grp','geo','jnt'])
        
        self.main_input_layout.addWidget(self.name_label,0,0)
        self.main_input_layout.addWidget(self.name_LineEdit,0,1)
        self.main_input_layout.addWidget(self.amount_label,0,2)
        self.main_input_layout.addWidget(self.amount_spinbox,0,3)
        self.main_input_layout.addWidget(self.suffix_label,1,0)
        self.main_input_layout.addWidget(self.suffix_LineEdit,1,1)
        self.main_input_layout.addWidget(self.Or,1,2)
        self.main_input_layout.addWidget(self.suffix_comboBox,1,3)
         
    def init_opt_widget(self):
        self.main_opt_widget = QWidget()
        self.main_opt_layout = QHBoxLayout()
        self.main_opt_widget.setLayout(self.main_opt_layout)
        
        self.create_button = QPushButton("Create")
        self.create_button.setMinimumHeight(30)
        self.main_opt_layout.addWidget(self.create_button)
        self.create_button.clicked.connect(self.closeUI)
        
        self.no_button = QPushButton("Cancel")
        self.no_button.setMinimumHeight(30)
        self.main_opt_layout.addWidget(self.no_button)
        self.no_button.clicked.connect(self.closeUI)
        
        self.setWindowOpacity(1)      
        
    def generatePrim(self):
        Objname = self.name_LineEdit.text()
        suffixText = self.suffix_LineEdit.text()
        suffixChoose = self.suffix_comboBox.currentText()
        num = self.amount_spinbox.value()
        amp = 3
        for i in range(num):
            if suffixText == '' and suffixChoose == 'please select':
                objfullname = '{}{}'.format(Objname, '%04d' % (i+1))
            if suffixChoose != 'please select':
                objfullname = '{}{}_{}'.format(Objname, '%04d' % (i+1), suffixChoose)
            if suffixText != '':
                objfullname = '{}{}_{}'.format(Objname, '%04d' % (i+1), suffixText)   
            prim = cmds.polyTorus(name = objfullname)[0]
            cmds.setAttr(f'{prim}.translateX', (i*amp))

    def closeUI(self):
        cmds.quit(force=True)
        

global ui
try:
    ui.close()
except:
    pass
        
maya_ptr = omui.MQtUtil.mainWindow()
ptr = wrapInstance(int(maya_ptr), QWidget)

ui = polygonTool(parent = ptr)
ui.show()