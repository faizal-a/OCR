# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ocr_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(842, 881)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1371, 811))
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.tabWidget = QtGui.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1351, 791))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_main = QtGui.QWidget()
        self.tab_main.setObjectName(_fromUtf8("tab_main"))
        self.label_img = QtGui.QLabel(self.tab_main)
        self.label_img.setGeometry(QtCore.QRect(200, 10, 601, 561))
        self.label_img.setStyleSheet(_fromUtf8("border: 2px solid gray;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
""))
        self.label_img.setText(_fromUtf8(""))
        self.label_img.setScaledContents(True)
        self.label_img.setObjectName(_fromUtf8("label_img"))
        self.frame_3 = QtGui.QFrame(self.tab_main)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 181, 741))
        self.frame_3.setStyleSheet(_fromUtf8("border: 2px solid gray;\n"
"border-radius: 10px;\n"
"padding: 0 8px;"))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.pb_openFile = QtGui.QPushButton(self.frame_3)
        self.pb_openFile.setGeometry(QtCore.QRect(20, 10, 141, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pb_openFile.setFont(font)
        self.pb_openFile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pb_openFile.setStyleSheet(_fromUtf8("border: 2px solid gray;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"background-color: rgb(184, 233, 255);"))
        self.pb_openFile.setObjectName(_fromUtf8("pb_openFile"))
        self.pb_run = QtGui.QPushButton(self.frame_3)
        self.pb_run.setGeometry(QtCore.QRect(20, 90, 141, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pb_run.setFont(font)
        self.pb_run.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pb_run.setStyleSheet(_fromUtf8("border: 2px solid gray;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"background-color: rgb(166, 255, 215);"))
        self.pb_run.setObjectName(_fromUtf8("pb_run"))
        self.label_status = QtGui.QLabel(self.tab_main)
        self.label_status.setGeometry(QtCore.QRect(890, 730, 451, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_status.setFont(font)
        self.label_status.setText(_fromUtf8(""))
        self.label_status.setObjectName(_fromUtf8("label_status"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.tab_main)
        self.textBrowser_2.setGeometry(QtCore.QRect(200, 580, 601, 171))
        self.textBrowser_2.setStyleSheet(_fromUtf8("border: 2px solid gray;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
""))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.tabWidget.addTab(self.tab_main, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 842, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setShortcut(_fromUtf8(""))
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionOpen_Directory = QtGui.QAction(MainWindow)
        self.actionOpen_Directory.setObjectName(_fromUtf8("actionOpen_Directory"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionOpen_Directory)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "OCR Tracking", None))
        self.pb_openFile.setText(_translate("MainWindow", "Open File", None))
        self.pb_run.setText(_translate("MainWindow", "Run", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_main), _translate("MainWindow", "Home", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionOpen.setText(_translate("MainWindow", "Open      Ctrl-O", None))
        self.actionOpen_Directory.setText(_translate("MainWindow", "Open Directory", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

