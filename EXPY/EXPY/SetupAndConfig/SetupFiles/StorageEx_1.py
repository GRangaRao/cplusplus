# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StorageEx.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QObject, pyqtSlot

import globals
import TextCn
import ctypes

sys.path.insert(0, '../../TestEngine/TestInterface/SATA')

from SATA_wrapper import *
from loggin import LogginClass
from FromJsonFiles import *
import globals

#<chandu> all the reference to other files should be moved under one class so that, creating multiple objects is reduced


b = LogginClass()
device_node = JsonFile.read_json('details',0,'drive_name' )
device_node = ctypes.c_char_p(device_node)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

def p(x):
    print x

class Ui_Dialog(object):
    def setupUi(self, myDialog):
        myDialog.setObjectName(_fromUtf8("Dialog"))
        myDialog.setWindowTitle("PyTAF Text Console")
        myDialog.resize(1333, 500)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(myDialog.sizePolicy().hasHeightForWidth())
        myDialog.setSizePolicy(sizePolicy)
        self.label = QtGui.QLabel(myDialog)
        self.label.setGeometry(QtCore.QRect(25, 110, 141, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(myDialog)
        self.label_2.setGeometry(QtCore.QRect(25, 170, 141, 41))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(myDialog)
        self.label_3.setGeometry(QtCore.QRect(25, 230, 141, 41))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.checkBox = QtGui.QCheckBox(myDialog)
        self.checkBox.setGeometry(QtCore.QRect(135, 120, 16, 21))
        self.checkBox.setIconSize(QtCore.QSize(40, 40))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(myDialog)
        self.checkBox_2.setGeometry(QtCore.QRect(135, 180, 16, 21))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(myDialog)
        self.checkBox_3.setGeometry(QtCore.QRect(135, 240, 16, 21))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.label_4 = QtGui.QLabel(myDialog)
        self.label_4.setGeometry(QtCore.QRect(195, 110, 91, 41))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(myDialog)
        self.label_5.setGeometry(QtCore.QRect(195, 170, 91, 41))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(myDialog)
        self.label_6.setGeometry(QtCore.QRect(195, 230, 101, 41))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.textEdit = QtGui.QTextEdit(myDialog)
        self.textEdit.setGeometry(QtCore.QRect(305, 110, 191, 41))
        self.textEdit.setReadOnly(False)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.textEdit.setObjectName(_fromUtf8("param1"))
        self.textEdit_2 = QtGui.QTextEdit(myDialog)
        self.textEdit_2.setGeometry(QtCore.QRect(305, 170, 191, 41))
        self.textEdit.setPlainText("LBA Value")
        self.textEdit_2.setObjectName(_fromUtf8("param2"))
        self.textEdit_3 = QtGui.QTextEdit(myDialog)
        self.textEdit_3.setGeometry(QtCore.QRect(305, 230, 191, 41))
        self.textEdit_3.setObjectName(_fromUtf8("param3"))
        self.textEdit_4 = QtGui.QTextEdit(myDialog)
        self.textEdit_4.setGeometry(QtCore.QRect(555, 170, 191, 41))
        self.textEdit_4.setObjectName(_fromUtf8("param4"))
        self.textEdit_5 = QtGui.QTextEdit(myDialog)
        self.textEdit_5.setGeometry(QtCore.QRect(555, 230, 191, 41))
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.textEdit_6 = QtGui.QTextEdit(myDialog)
        self.textEdit_6.setGeometry(QtCore.QRect(555, 110, 191, 41))
        self.textEdit_6.setObjectName(_fromUtf8("textEdit_6"))
        self.textEdit_6.setPlainText("Count")
        self.textEdit_7 = QtGui.QTextEdit(myDialog)
        self.textEdit_7.setGeometry(QtCore.QRect(785, 230, 191, 41))
        self.textEdit_7.setObjectName(_fromUtf8("textEdit_7"))
        self.textEdit_8 = QtGui.QTextEdit(myDialog)
        self.textEdit_8.setGeometry(QtCore.QRect(785, 170, 191, 41))
        self.textEdit_8.setObjectName(_fromUtf8("textEdit_8"))
        self.textEdit_9 = QtGui.QTextEdit(myDialog)
        self.textEdit_9.setGeometry(QtCore.QRect(785, 110, 191, 41))
        self.textEdit_9.setObjectName(_fromUtf8("textEdit_9"))
        self.textEdit_10 = QtGui.QTextEdit(myDialog)
        self.textEdit_10.setGeometry(QtCore.QRect(1005, 170, 191, 41))
        self.textEdit_10.setObjectName(_fromUtf8("textEdit_10"))
        self.textEdit_11 = QtGui.QTextEdit(myDialog)
        self.textEdit_11.setGeometry(QtCore.QRect(1005, 230, 191, 41))
        self.textEdit_11.setObjectName(_fromUtf8("textEdit_11"))
        self.textEdit_12 = QtGui.QTextEdit(myDialog)
        self.textEdit_12.setGeometry(QtCore.QRect(1005, 110, 191, 41))
        self.textEdit_12.setObjectName(_fromUtf8("textEdit_12"))
        self.label_7 = QtGui.QLabel(myDialog)
        self.label_7.setGeometry(QtCore.QRect(305, 70, 141, 41))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(myDialog)
        self.label_8.setGeometry(QtCore.QRect(555, 70, 141, 41))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(myDialog)
        self.label_9.setGeometry(QtCore.QRect(785, 70, 141, 41))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(myDialog)
        self.label_10.setGeometry(QtCore.QRect(1005, 70, 141, 41))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.pushButton_4 = QtGui.QPushButton(myDialog)
        self.pushButton_4.setGeometry(QtCore.QRect(725, 310, 141, 51))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(myDialog)



        self.pushButton_5.setGeometry(QtCore.QRect(885, 310, 141, 51))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.progressBar = QtGui.QProgressBar(myDialog)
        self.progressBar.setGeometry(QtCore.QRect(615, 390, 411, 21))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label_11 = QtGui.QLabel(myDialog)
        self.label_11.setGeometry(QtCore.QRect(480, 390, 101, 21))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.pushButton_6 = QtGui.QPushButton(myDialog)
        '''
        self.pushButton_6.setGeometry(QtCore.QRect(555, 310, 111, 51))
        '''

        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))

        '''
        self.pushButton_6.setGeometry(QtCore.QRect(0, 0, 200, 200))

        self.pushButton_6.setStyleSheet('background-color:#00FF00;color:#000000;')

        self.pushButton_6.setFixedHeight(100)
        self.pushButton_6.setFixedWidth(100)


        self.region = QtGui.QRegion(QtCore.QRect(self.pushButton_6.x() + 5, self.pushButton_6.y() + 5, 190, 190),
                                    QtGui.QRegion.Ellipse)
        self.pushButton_6.setMask(self.region)
        '''
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL("clicked()"), self.c1_clicked)

        '''
        self.frame = QtGui.QFrame(myDialog)
        self.frame.setGeometry(QtCore.QRect(10, 10, 121, 81))
        self.frame.setStyleSheet(_fromUtf8("image: url(:/images/Elogo.png);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.actionLogo1 = QtGui.QAction(myDialog)
        '''

        '''
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/Eximius design logo.bmp")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLogo1.setIcon(icon)
        self.actionLogo1.setObjectName(_fromUtf8("actionLogo1"))
        self.actionLogo1_2 = QtGui.QAction(myDialog)
        self.actionLogo1_2.setIcon(icon)
        self.actionLogo1_2.setObjectName(_fromUtf8("actionLogo1_2"))
        '''
        
        self.retranslateUi(myDialog)
        QtCore.QMetaObject.connectSlotsByName(myDialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Read", None))
        self.label_2.setText(_translate("Dialog", "Write", None))
        self.label_3.setText(_translate("Dialog", "Identify", None))
        self.checkBox.setText(_translate("Dialog", "CheckBox", None))
        self.checkBox_2.setText(_translate("Dialog", "CheckBox", None))
        self.checkBox_3.setText(_translate("Dialog", "CheckBox", None))
        self.label_4.setText(_translate("Dialog", "Drive Read", None))
        self.label_5.setText(_translate("Dialog", "Drive Write", None))
        self.label_6.setText(_translate("Dialog", "Drive Inquiry", None))
        self.label_7.setText(_translate("Dialog", "Param1", None))
        self.label_8.setText(_translate("Dialog", "Param2", None))
        self.label_9.setText(_translate("Dialog", "Param3", None))
        self.label_10.setText(_translate("Dialog", "Param4", None))
        self.pushButton_4.setText(_translate("Dialog", "Select All", None))
        self.pushButton_5.setText(_translate("Dialog", "Deselect All", None))
        self.label_11.setText(_translate("Dialog", "Test Progress", None))
        self.pushButton_6.setText(_translate("Dialog", "Run", None))


    def c1_clicked(self):
        val = int(self.textEdit.toPlainText())
        r = Storage(device_node.value).ReadSector(val)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))

        MainWindow.resize(1056, 814)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        '''
        self.tabWidget.setGeometry(QtCore.QRect(499, 9, 661, 541))
        '''

        self.tabWidget.setGeometry(QtCore.QRect(499, 9, 761, 641))

        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.textEdit = QtGui.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 621, 581))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.textEdit_2 = QtGui.QTextEdit(self.tab_2)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 0, 661, 521))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.executionpanel = QtGui.QFrame(self.centralwidget)
        self.executionpanel.setGeometry(QtCore.QRect(0, 10, 389, 479))
        self.executionpanel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.executionpanel.setFrameShadow(QtGui.QFrame.Raised)
        self.executionpanel.setObjectName(_fromUtf8("executionpanel"))
        self.verticalLayout = QtGui.QVBoxLayout(self.executionpanel)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.executionpanel)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtGui.QComboBox(self.executionpanel)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.comboBox)
        self.label_2 = QtGui.QLabel(self.executionpanel)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.comboBox_3 = QtGui.QComboBox(self.executionpanel)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.comboBox_3)
        self.tabWidget_2 = QtGui.QTabWidget(self.executionpanel)
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.frame = QtGui.QFrame(self.tab_3)
        self.frame.setGeometry(QtCore.QRect(0, 10, 361, 421))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 71, 31))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(140, 10, 121, 31))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 61, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.checkBox = QtGui.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(90, 40, 16, 16))
        self.checkBox.setText(_fromUtf8(""))
        self.checkBox.setObjectName(_fromUtf8("Read"))


        self.checkBox.setStyleSheet("QCheckBox:checked {color:green;}")

        self.label_10 = QtGui.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(140, 40, 161, 21))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.checkBox_2 = QtGui.QCheckBox(self.frame)
        self.checkBox_2.setGeometry(QtCore.QRect(90, 70, 16, 16))
        self.checkBox_2.setText(_fromUtf8(""))
        self.checkBox_2.setObjectName(_fromUtf8("Write"))



        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 61, 41))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_11 = QtGui.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(140, 70, 161, 21))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(140, 100, 161, 21))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.checkBox_3 = QtGui.QCheckBox(self.frame)
        self.checkBox_3.setGeometry(QtCore.QRect(90, 100, 16, 16))
        self.checkBox_3.setText(_fromUtf8(""))
        self.checkBox_3.setObjectName(_fromUtf8("Identify"))


        '''
        self.palette= QtGui.QPalette(self.checkBox_3.palette())
        self.palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.WindowText,QtCore.Qt.darkGreen)
        self.brush=QtGui.QBrush(QtGui.QColor(0,255,0))
        self.palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Background,self.brush)
        self.checkBox_3.setPalette(self.palette)
        '''

        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 61, 41))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton_5 = QtGui.QPushButton(self.frame)
        '''
        self.pushButton_5.setGeometry(QtCore.QRect(90+10, 230+10, 61+10, 31+10))
        '''

        self.pushButton_5.setGeometry(QtCore.QRect(90, 200, 81, 31))




        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.frame)
        '''
        self.pushButton_6.setGeometry(QtCore.QRect(170+10, 230+10, 71+10, 31+10))
        '''


        self.pushButton_6.setGeometry(QtCore.QRect(190, 200, 91, 31))

        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.progressBar = QtGui.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(90, 260, 171, 16))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label_9 = QtGui.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(110, 340, 81, 31))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.WriteCache = QtGui.QCheckBox(self.frame)
        self.WriteCache.setGeometry(QtCore.QRect(90, 130, 16, 16))
        self.WriteCache.setText(_fromUtf8(""))
        self.WriteCache.setCheckable(True)
        self.WriteCache.setChecked(False)
        self.WriteCache.setObjectName(_fromUtf8("WriteCache"))
        self.label_31 = QtGui.QLabel(self.frame)
        self.label_31.setGeometry(QtCore.QRect(140, 130, 161, 21))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.label_32 = QtGui.QLabel(self.frame)
        self.label_32.setGeometry(QtCore.QRect(10, 120, 61, 41))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.frame.raise_()
        self.label_8.raise_()
        self.label_8.raise_()
        self.tabWidget_2.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.frame_4 = QtGui.QFrame(self.tab_4)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 361, 431))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.label_22 = QtGui.QLabel(self.frame_4)
        self.label_22.setGeometry(QtCore.QRect(10, 10, 71, 31))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_23 = QtGui.QLabel(self.frame_4)
        self.label_23.setGeometry(QtCore.QRect(140, 10, 121, 31))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_24 = QtGui.QLabel(self.frame_4)
        self.label_24.setGeometry(QtCore.QRect(10, 30, 61, 31))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.checkBox_7 = QtGui.QCheckBox(self.frame_4)
        self.checkBox_7.setGeometry(QtCore.QRect(80, 40, 16, 16))
        self.checkBox_7.setText(_fromUtf8(""))
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.label_25 = QtGui.QLabel(self.frame_4)
        self.label_25.setGeometry(QtCore.QRect(140, 40, 161, 21))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.checkBox_8 = QtGui.QCheckBox(self.frame_4)
        self.checkBox_8.setGeometry(QtCore.QRect(80, 70, 16, 16))
        self.checkBox_8.setText(_fromUtf8(""))
        self.checkBox_8.setObjectName(_fromUtf8("checkBox_8"))
        self.label_26 = QtGui.QLabel(self.frame_4)
        self.label_26.setGeometry(QtCore.QRect(10, 60, 61, 41))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.label_27 = QtGui.QLabel(self.frame_4)
        self.label_27.setGeometry(QtCore.QRect(140, 70, 161, 21))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.label_28 = QtGui.QLabel(self.frame_4)
        self.label_28.setGeometry(QtCore.QRect(140, 100, 161, 21))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        '''
        self.checkBox_9 = QtGui.QCheckBox(self.frame_4)
        self.checkBox_9.setGeometry(QtCore.QRect(80, 100, 16, 16))
        self.checkBox_9.setText(_fromUtf8(""))
        self.checkBox_9.setCheckable(True)
        self.checkBox_9.setChecked(False)
        self.checkBox_9.setObjectName(_fromUtf8("checkBox_9"))
        '''

        self.label_29 = QtGui.QLabel(self.frame_4)
        self.label_29.setGeometry(QtCore.QRect(10, 90, 61, 41))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.pushButton_9 = QtGui.QPushButton(self.frame_4)
        self.pushButton_9.setGeometry(QtCore.QRect(90, 200, 81, 31))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_10 = QtGui.QPushButton(self.frame_4)
        self.pushButton_10.setGeometry(QtCore.QRect(190, 200, 91, 31))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.progressBar_3 = QtGui.QProgressBar(self.frame_4)
        self.progressBar_3.setGeometry(QtCore.QRect(90, 260, 171, 16))
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName(_fromUtf8("progressBar_3"))
        self.label_30 = QtGui.QLabel(self.frame_4)
        self.label_30.setGeometry(QtCore.QRect(110, 290, 81, 31))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.tabWidget_2.addTab(self.tab_4, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget_2)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 500, 381, 21))
        self.pushButton.setCheckable(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 10, 391, 481))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget.raise_()
        self.tabWidget_2.raise_()
        self.executionpanel.raise_()
        self.frame_4.raise_()
        self.textEdit.raise_()
        self.pushButton.raise_()
        self.executionpanel.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 856, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(100, 40))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionLogo = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/Elogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLogo.setIcon(icon)
        self.actionLogo.setObjectName(_fromUtf8("actionLogo"))
        self.actionSettings = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("images/settings.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon1)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionTextConsole = QtGui.QAction(MainWindow)
        self.actionTextConsole.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/TextConsole.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTextConsole.setIcon(icon2)
        self.actionTextConsole.setObjectName(_fromUtf8("actionTextConsole"))
        self.toolBar.addAction(self.actionLogo)
        self.toolBar.addAction(self.actionTextConsole)
        self.toolBar.addAction(self.actionSettings)

        '''
	QtCore.QObject.connect(self.actionExit_2, QtCore.SIGNAL("triggered()"), self.ExitClick)
	'''

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        '''
        QtCore.QObject.connect(self.pushButton_9, QtCore.SIGNAL(_fromUtf8("clicked()")), self.checkBox_9.toggle)
        '''
        QtCore.QObject.connect(self.pushButton_9, QtCore.SIGNAL(_fromUtf8("clicked()")), self.checkBox_8.toggle)
        QtCore.QObject.connect(self.pushButton_9, QtCore.SIGNAL(_fromUtf8("clicked()")), self.checkBox_7.toggle)
        '''
        QtCore.QObject.connect(self.pushButton_10, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.checkBox_9.setChecked)
        '''
        QtCore.QObject.connect(self.pushButton_10, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.checkBox_8.setChecked)
        QtCore.QObject.connect(self.pushButton_10, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.checkBox_7.setChecked)

        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.checkBox_3.toggle)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.checkBox_2.toggle)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.checkBox.toggle)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.WriteCache.toggle)

        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.checkBox_3.setChecked)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.checkBox_2.setChecked)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.checkBox.setChecked)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.WriteCache.setChecked)

        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.c1_clicked)
        QtCore.QObject.connect(self.checkBox_2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.c1_clicked)
        QtCore.QObject.connect(self.checkBox_3, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.c1_clicked)
        QtCore.QObject.connect(self.WriteCache, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.c1_clicked)
		
        QtCore.QObject.connect(self.pushButton_9, QtCore.SIGNAL("clicked()"), self.c1_clicked)
	QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.b1_clicked)

	QtCore.QObject.connect(self.pushButton_9, QtCore.SIGNAL("clicked()"), self.b2_clicked)

        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL("clicked()"), self.b2_clicked)

        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL("clicked()"), self.b3_clicked)

        QtCore.QObject.connect(self.pushButton_10, QtCore.SIGNAL("clicked()"), self.b3_clicked)

        QtCore.QObject.connect(self.actionTextConsole, QtCore.SIGNAL("triggered()"), self.TextConsoleClick)

        QtCore.QObject.connect(self.progressBar, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_6.setNum)
        QtCore.QObject.connect(self.progressBar, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_4.setNum)
        QtCore.QObject.connect(self.progressBar, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_5.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        if globals.SATA == 0:
            self.tabWidget_2.setTabEnabled(0, 1)
            self.tabWidget_2.setTabEnabled(1, 0)
        else:
            self.tabWidget_2.setTabEnabled(1, 1)
            self.tabWidget_2.setTabEnabled(0, 0)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("ExTAF Storage", "ExTAF Storage", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Test Log", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Command Log", None))
        self.label.setText(_translate("MainWindow", "Select Test Suite", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "SATA", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "NVMe", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "SCSi", None))

        self.comboBox.currentIndexChanged.connect(self.selectionchange)

        '''
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL("currentIndexChanged(int)"),
                              self.comboBox,QtCore.SLOT("onIndexChange(int)"))
        '''

        self.label_2.setText(_translate("MainWindow", "Test Execution Method", None))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "CLI", None))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "GUI", None))
        self.label_7.setText(_translate("MainWindow", "Test ID\'s", None))
        self.label_8.setText(_translate("MainWindow", "Description", None))
        self.label_4.setText(_translate("MainWindow", "Read", None))
        self.label_10.setText(_translate("MainWindow", "Drive Read Command", None))
        self.label_5.setText(_translate("MainWindow", "Write", None))
        self.label_11.setText(_translate("MainWindow", "Drive Write Command", None))
        self.label_12.setText(_translate("MainWindow", "Drive Inquiry Data", None))
        self.label_6.setText(_translate("MainWindow", "Identify", None))
        self.pushButton_5.setText(_translate("MainWindow", "Select All", None))
        self.pushButton_6.setText(_translate("MainWindow", "Deselect All", None))
        self.label_9.setText(_translate("MainWindow", "Test progress", None))
        self.label_31.setText(_translate("MainWindow", "Drive Write Cache Enable", None))
        self.label_32.setText(_translate("MainWindow", "Write Cache", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "SATA", None))
        self.label_22.setText(_translate("MainWindow", "Test Type", None))
        self.label_23.setText(_translate("MainWindow", "Description", None))
        self.label_24.setText(_translate("MainWindow", "Ctrl", None))
        self.label_25.setText(_translate("MainWindow", "Nvme Ctrl Command", None))
        self.label_26.setText(_translate("MainWindow", "List", None))
        self.label_27.setText(_translate("MainWindow", "Nvme List Command", None))
        '''
        self.label_28.setText(_translate("MainWindow", "Drive Inquiry Data", None))
        self.label_29.setText(_translate("MainWindow", "Identify", None))
        '''
        self.pushButton_9.setText(_translate("MainWindow", "Select All", None))
        self.pushButton_10.setText(_translate("MainWindow", "Deselect All", None))
        self.label_30.setText(_translate("MainWindow", "Test progress", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "NVME", None))
        self.pushButton.setText(_translate("MainWindow", "Run", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionLogo.setText(_translate("MainWindow", "Logo", None))
        self.actionLogo.setToolTip(_translate("MainWindow", "Company", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings", None))
        self.actionSettings.setToolTip(_translate("MainWindow", "Settings", None))
        self.actionTextConsole.setText(_translate("MainWindow", "TextConsole", None))
        self.actionTextConsole.setToolTip(_translate("MainWindow", "Tests Individual Command", None))

        self.progressBar.setValue(0)
        self.progressBar_3.setValue(0)


    def a1_clicked(self):
        sys.exit(0)

    def c1_clicked(self, val):
        self.pushButton.setDisabled(not val)


    def b2_clicked(self):
        self.pushButton.setDisabled(0)


    def b3_clicked(self):
        self.pushButton.setDisabled(1)
        self.textEdit_2.setText("")
        self.textEdit.setText("")

        self.progressBar.setValue(0)
        self.progressBar_3.setValue(0)
        self.checkBox_3.setStyleSheet("QCheckBox:checked {color:white;background-color:white}")
        self.checkBox_2.setStyleSheet("QCheckBox:checked {color:white;background-color:white}")
        self.checkBox.setStyleSheet("QCheckBox:checked {color:white;background-color:white}")
        self.WriteCache.setStyleSheet("QCheckBox:checked {color:white;background-color:white}")
        self.label_4.setText(_translate("MainWindow", "Read", None))

        self.label_5.setText(_translate("MainWindow", "Write", None))
        self.label_6.setText(_translate("MainWindow", "Identify", None))

    def ExitClick(self):
        sys.exit()

    def TextConsoleClick(self):

        self.Dialog = QtGui.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()

    '''
    @pyqtSlot(int)
    def onIndexChange(self, i):
        print i
    '''

    def selectionchange(self, i):
        globals.SATA=i
        if globals.SATA == 0:
            self.tabWidget_2.setTabEnabled(0, 1)
            self.tabWidget_2.setTabEnabled(1, 0)
        else:
            self.tabWidget_2.setTabEnabled(1, 1)
            self.tabWidget_2.setTabEnabled(0, 0)

        print globals.SATA

    def b1_clicked(self):
        self.textEdit_2.setText("")
        self.textEdit.setText("")

        globals.retval = 0
        print 'Connecting process'
        self.process = QtCore.QProcess(parent=None)

        self.process.readyReadStandardOutput.connect(self.stdoutReady)
        self.process.readyReadStandardError.connect(self.stderrReady)
        self.process.started.connect(lambda: p('Started!'))
        self.process.finished.connect(lambda: p('Finished!'))
        print 'Starting process'



        '''
        self.process.start('python', ['main.py', 'tsuite2.json', '> ../../Logging/SATA/One.txt'])
        '''

        if globals.SATA == 0:
            self.process.start('python', ['main.py', 'tsuite2.json'])
            path = "../../Logging/SATA/SATACmdLog.txt"

            path1 = "../../Logging/SATA/runLog.log"


        else:
            self.process.start('python', ['main.py', 'tsuite3.json'])
            path = "../../Logging/NVMe/NVMECmdLog.txt"

            path1 = "../../Logging/NVMe/runLog.log"



        if globals.retval != 0:
            self.checkBox_3.setStyleSheet("QCheckBox:checked {color:red;background-color:red}")
        else:
            self.checkBox_3.setStyleSheet("QCheckBox:checked {color:red;background-color:green}")

        if globals.retvalCache != 0:
            self.checkBox_2.setStyleSheet("QCheckBox:checked {color:white;background-color:red}")
        else:
            self.checkBox_2.setStyleSheet("QCheckBox:checked {color:red;background-color:green}")

        if globals.retvalCacheE != 0:
            self.checkBox.setStyleSheet("QCheckBox:checked {color:white;background-color:red}")
        else:
            self.checkBox.setStyleSheet("QCheckBox:checked {color:red;background-color:green}")

        if globals.retvalCacheE != 0:
            self.WriteCache.setStyleSheet("QCheckBox:checked {color:white;background-color:red}")
        else:
            self.WriteCache.setStyleSheet("QCheckBox:checked {color:red;background-color:green}")

        if globals.NvmeIdCtrl != 0:
            self.checkBox_7.setStyleSheet("QCheckBox:checked {color:white;background-color:red}")
        else:
            self.checkBox_7.setStyleSheet("QCheckBox:checked {color:red;background-color:green}")

        if globals.NvmeIdList != 0:
            self.checkBox_8.setStyleSheet("QCheckBox:checked {color:white;background-color:red}")
        else:
            self.checkBox_8.setStyleSheet("QCheckBox:checked {color:red;background-color:green}")

        text = open(path).read()
        self.textEdit_2.setText("")
        self.textEdit_2.setPlainText(text)
        '''
        text1 = open(path1).read()
        '''


        text = open(path).read()
        self.textEdit_2.setText("")
        self.textEdit_2.setPlainText(text)
        text1 = open(path1).read()
        self.textEdit.setPlainText(text1)

        if globals.SATA == 0:
            self.progressBar.setValue(100)
        else:
            self.progressBar_3.setValue(100)

        self.label_4.setText(_translate("MainWindow", "Read", None))

        self.label_5.setText(_translate("MainWindow", "Write", None))
        self.label_6.setText(_translate("MainWindow", "Identify", None))

    def append(self, text):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(text)
        # self.output.ensureCursorVisible()


    def stdoutReady(self):
        text = str(self.process.readAllStandardOutput())
        print text.strip()
        self.append(text)


    def stderrReady(self):
        text = str(self.process.readAllStandardError())
        print text.strip()
        self.append(text)


import Storage_rc
import sys

class MyApp(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    exit=app
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
