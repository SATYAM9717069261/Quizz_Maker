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
        __data__=self.window.option_text.displayText()
        if(__data__):
           # print(dir(self.window.Quizz_scroll.layout))
            # generate Options
            self.quizz_option.addWidget(QRadioButton(__data__))
            self.window.Quizz_scroll.setWidget(self.window.scrollAreaWidgetContents.setLayout(self.quizz_option))
            # end Generate Options
        else:
            print("Can't ADD ")


class Fillups(Setup_urls):
    def __init__(self,url,id):
        super(Fillups,self).__init__(url)
        self.save_fill=[]
        self.fill_up_id=id
        self.window.save_fill.clicked.connect(lambda: self.save_btn())            # save btn click event define

    def save_btn(self):
        print(self.window.Que.text())
        main.fill[self.window.Que.text()]=[self.window.Ans.text()]
        print(main.fill)
        pass

    


class Main_window(Setup_urls):
    def __init__(self,url):
        super(Main_window,self).__init__(url)
        self.fill_id=0
        self.fill={}             # Dictonary for Fillups

    def Button_Click(self):
        self.vbox=QVBoxLayout()
        self.window.Add_Quizz.clicked.connect(self.Quizz_UI_ADD) # quizz add in main frame
        self.window.Add_Fill.clicked.connect(self.Fillup_UI_ADD) # fillup add in main Frame
    
    def Fillup_UI_ADD(self):
        self.fill_id+=1
        self.fill[self.fill_id]=Fillups("Fillup.ui",self.fill_id)
        self.vbox.addWidget(self.fill[self.fill_id].window.Fillup)
        self.window.Scroll_Area.setWidget(self.window.Scroll_Area_Content.setLayout(self.vbox))


    def Quizz_UI_ADD(self):
        self.quizz_id+=1
        self.quizz[self.quizz_id]=Quizz("Quizz.ui")
        self.vbox.addWidget(self.quizz[self.quizz_id].window.final_quiz)
        self.window.Scroll_Area.setWidget(self.window.Scroll_Area_Content.setLayout(self.vbox))
        self.quizz[self.quizz_id].window.add_option.clicked.connect(lambda : quizz.option_add())  # directly can't call
        print(self.quizz)


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    main=Main_window("sheet_design.ui")
    main.Button_Click()
    main.window.show()
    sys.exit(app.exec_())

