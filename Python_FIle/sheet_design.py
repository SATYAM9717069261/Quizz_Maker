import sys
from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication,QVBoxLayout,QRadioButton,QHBoxLayout
from PySide2.QtCore import QFile, QCoreApplication, QIODevice
from Setup import Setup_urls

class Quizz(Setup_urls):
    def __init__(self,url):
        super(Quizz,self).__init__(url) 
        self.quizz_option=QHBoxLayout()    # for vertcal use QVBoxLayout for horizontal QHBoxLayout
        

    def option_add(self):
        #print(self.window.option_text.displayText())
        __data__=self.window.option_text.displayText()
        if(__data__):
           # print(dir(self.window.Quizz_scroll.layout))
            # generate Options
            self.quizz_option.addWidget(QRadioButton(__data__))
            self.window.Quizz_scroll.setWidget(self.window.scrollAreaWidgetContents.setLayout(self.quizz_option))
            #self.window.Quizz_Option_frame.layout.addItem( QRadioButton(__data__)  )
            # end Generate Options
        else:
            print("Can't ADD ")



class Main_window(Setup_urls):
    def __init__(self,url):
        super(Main_window,self).__init__(url)
        
    def Button_Click(self):
        self.vbox=QVBoxLayout() 
        self.window.Add_Quizz.clicked.connect(self.Quizz_UI_ADD)
        self.window.Add_Fill.clicked.connect(self.Fillup_UI_ADD) 
    
    def Fillup_UI_ADD(self):
        Fillup=Setup_urls("../UI/Fillup.ui")
        self.vbox.addWidget(Fillup.window.Fillup)
        self.window.Scroll_Area.setWidget(self.window.Scroll_Area_Content.setLayout(self.vbox))

    def Quizz_UI_ADD(self):
        quizz=Quizz("../UI/Quizz.ui")
        self.vbox.addWidget(quizz.window.final_quiz)
        self.window.Scroll_Area.setWidget(self.window.Scroll_Area_Content.setLayout(self.vbox))
        quizz.window.add_option.clicked.connect(lambda : quizz.option_add())  # directly can't call



if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    main=Main_window("../UI/sheet_design.ui")
    main.Button_Click()
    main.window.show()
    sys.exit(app.exec_())

