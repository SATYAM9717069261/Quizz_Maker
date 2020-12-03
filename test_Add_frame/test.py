import sys
from PySide2 import QtCore
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication,QFileDialog,QStackedWidget
from PySide2.QtCore import QFile, QIODevice,QCoreApplication,Qt

class Setup_urls:
    def __init__(self,fileURL):
        self.ui_file_name = fileURL
        self.ui_file = QFile(self.ui_file_name)

        if not self.ui_file.open(QIODevice.ReadOnly):                                                         # Error Occure if file not open
            print("Cannot open {}: {}".format(self.ui_file_name, ui_file.errorString()))
            sys.exit(-1)

        self.window=QUiLoader().load(self.ui_file)
        self.ui_file.close()

# customisation if any changes in Design level like lable text then use self.window

    def Button_clicks(self):                                                                         # all Button click define here And call Further function
        self.window.Add.clicked.connect(self.add)
        self.vbox=QVBoxLayout()

    def add(self):
        label1 =QLabel('1. This is a Label.')
        Quizz=Setup_urls("quizz.ui")
        self.vbox.addWidget(Quizz.window.final_quizz)
        self.window.scrollArea.setWidget(self.window.scrollAreaWidgetContents.setLayout(self.vbox))


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)



    app = QApplication(sys.argv)
    Object1 = Setup_urls("main.ui")
    #Quizz=Setup_urls("quizz.ui")
    #print(dir(Quizz.window.final_quizz))
    Object1.Button_clicks()   # all Click event define here

    Object1.window.show()
    sys.exit(app.exec_())


