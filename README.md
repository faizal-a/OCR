# OCR for text extraction

A simple OCR application built in Python, PyQt and Tesseract OCR engine to perform text extraction from PDF or image file.
You will need to install the OCR engine separetely in C drive and configure the environment variable before run the application.
It was tested and worked on Windows machine by executing it as window application.
If you want to make it as a executable file, simply convert it using pyinstaller then you are ready to go. Good luck!

Here some of the guidelines ;

1. Download and install Tesseract OCR engine from this link https://github.com/UB-Mannheim/tesseract/wiki.
2. Install all libraries and dependencies via pip. (pytesseract, openCV, etc)
3. Download the source code (ocrNet.py & ocr_window.py) and save it under same directory.
4. Test the code.
5. Once statistied, run the ocrNet.py with a command "pyinstaller --onefile ocrNet.py" and you will get an executable file as output (try look it from 'dist' folder).
