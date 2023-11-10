import maya.cmds as cmds
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui

class SearchAndReplaceTool(MainWindow):
    def __init__(self, *args, **kwargs):
        super(SearchAndReplaceTool, self).__init__(*args, **kwargs)
        self.resize(300,100)
        self.setWindowTitle('Search And Replace Tool')
        
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
            
        self.Search_label = LabelStyle('Search : ')
        self.Search_LineEdit = TextBoxStyle()
        self.Search_LineEdit.setMinimumHeight(30)
        self.Search_LineEdit.setText('Find what?')
        self.Search_LineEdit.selectAll()
                
        self.Replace_label = LabelStyle('Replace : ')
        self.Replace_LineEdit = TextBoxStyle()
        self.Replace_LineEdit.setMinimumHeight(30)
        self.Replace_LineEdit.setText('Replace with')
              
        self.main_input_layout.addWidget(self.Search_label,0,0)
        self.main_input_layout.addWidget(self.Search_LineEdit,0,1)
        
        self.main_input_layout.addWidget(self.Replace_label,1,0)
        self.main_input_layout.addWidget(self.Replace_LineEdit,1,1)
        
    def init_opt_widget(self):
        self.main_opt_widget = QWidget()
        self.main_opt_layout = QHBoxLayout()
        self.main_opt_widget.setLayout(self.main_opt_layout)
        
        self.rename_button = ButtonStyle("replace")
        self.rename_button.setMinimumHeight(40)
        self.main_opt_layout.addWidget(self.rename_button)
        self.rename_button.clicked.connect(self.SearchAndReplace)
        
        self.no_button = ButtonStyle("Cancel")
        self.no_button.setMinimumHeight(40)
        self.main_opt_layout.addWidget(self.no_button)
        self.no_button.clicked.connect(self.closeUI)
        
        self.setWindowOpacity(1)
        
        
    def SearchAndReplace(self):
        search = self.Search_LineEdit.text()
        replace = self.Replace_LineEdit.text()
        sels = cmds.ls(sl=True)
        for each in sels:
            new_name = each.replace(search, replace)
            cmds.rename(each, new_name)   

    def closeUI(self):
        self.close()
        
class LabelStyle(QLabel):
    def __init__(self, *args, **kwargs):
        super( LabelStyle, self).__init__(*args, **kwargs)
        
        self.setStyleSheet("""
            QLabel {
                color: black;
                font-family: verdana;
            }
        """)
                    
class TextBoxStyle(QLineEdit):
    def __init__(self, *args, **kwargs):
        super(TextBoxStyle, self).__init__(*args, **kwargs)
        
        self.setStyleSheet("""
            QLineEdit {
                background-color: white;
                color: gray;
                font-family: verdana;
                border-style: solid;
                border-width: 2px;
                border-radius: 10px;
                border-color: black;
                padding: 5px;
            }
            QPushButton:hover:!pressed {
                background-color: Gainsboro;
                font-weight: bold;
                border-width: 5px;
            }
            QPushButton:pressed {
                background-color: forestgreen;
                font-weight: bold;
                border-width: 5px;
            }
        """)
        
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setStyleSheet("""
            background-color: #FFF8DC;
        """)
        
class ButtonStyle(QPushButton):
    def __init__(self, *args, **kwargs):
        super(ButtonStyle, self).__init__(*args, **kwargs)

        self.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: black;
                font-family: verdana;
                border-style: solid;
                border-width: 2px;
                border-radius: 10px;
                border-color: black;
                padding: 5px;
            }
            QPushButton:hover:!pressed {
                background-color: Gainsboro;
                font-weight: bold;
                border-width: 5px;
            }
            QPushButton:pressed {
                background-color: forestgreen;
                font-weight: bold;
                border-width: 5px;
            }
        """)
        
global ui
try:
    ui.close()
except:
    pass
        
maya_ptr = omui.MQtUtil.mainWindow()
ptr = wrapInstance(int(maya_ptr), QWidget)

ui = SearchAndReplaceTool(parent = ptr)
ui.show()