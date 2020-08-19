# import necessary library

import numpy as np
import sys
import os
import cv2
import fitz
import pytesseract
import pyodbc
import datetime
import PIL
from PIL import Image
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QMessageBox, QFileDialog, QImageReader, QTableWidgetItem, QLabel, QPixmap, QWidget, QLineEdit, QGridLayout, QPushButton, QPainter, QPen, QSizePolicy
from ocr_window import Ui_MainWindow
from libs.ustr import ustr

__appname__ = 'OCR'

refPt = []
cropping = False

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, defaultFilename=None):
        super(MainWindow, self).__init__()
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        QtGui.QWidget.__init__(self)
        self.setupUi(self)


        # Application state
        self.filePath = ustr(defaultFilename)

        # Event assignment
        self.pb_openFile.clicked.connect(self.openFile)
        self.pb_run.clicked.connect(self.extractImage)


    # display image on the canvas
    def openFile(self, _value=False):
        global fileImg, output, i, pdffile

        path = os.path.dirname(ustr(self.filePath)) if self.filePath else '.'
        fileImg = QFileDialog.getOpenFileName(self, '%s - Choose file' % __appname__, path)

        i = 0

        # convert PDF to image file
        pdffile = fileImg
        doc = fitz.open(pdffile)
        page = doc.loadPage(i)
        pix = page.getPixmap(matrix=fitz.Matrix(100 / 72, 100 / 72))
        output = "output.png"
        pix.writePNG(output)

        # display converted file as an image
        self.label_img.setPixmap(QtGui.QPixmap(output))


    def loadFile(self, filePath=None):
        """Load the specified file, or the last opened file if None."""
        self.resetState()
        self.canvas.setEnabled(False)
        if filePath is None:
            filePath = self.settings.get(SETTING_FILENAME)


    def extractImage(self, event):

            image = cv2.imread("Output.png")
            text = pytesseract.image_to_string(image)
            self.textBrowser_2.setText(str("Output :" + text))
            #print(text)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())
    sys.stdout()
