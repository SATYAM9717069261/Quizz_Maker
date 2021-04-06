import sys
from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication,QVBoxLayout,QRadioButton,QHBoxLayout
from PySide2.QtCore import QFile, QCoreApplication, QIODevice
from Setup import Setup_urls
import xml.etree.cElementTree as Et
import os

class Quizz(Setup_urls):
    def __init__(self,url):
        super(Quizz,self).__init__(url) 
        self.quizz_option=QHBoxLayout()    # for vertcal use QVBoxLayout for horizontal QHBoxLayout
        self.window.quizz_save_btn.clicked.connect(lambda: self.quizz_save_btn())   # save btn Click
        self.window.add_option.clicked.connect(lambda : self.option_add())          # add Options click
        self.window.quizz_edit_btn.clicked.connect(lambda: self.editable())         #edit btn event
        self.window.quizz_edit_btn.setEnabled(False)
        self.option=[]                                                              # store all options add in questions
        

    def option_add(self):
        __data__=self.window.option_text.displayText()
        if(__data__):
            # generate Options
            self.option.append(__data__)
            self.quizz_option.addWidget(QRadioButton(__data__))
            self.window.Quizz_scroll.setWidget(self.window.scrollAreaWidgetContents.setLayout(self.quizz_option))
            # end Generate Options
        else:
            print("Can't ADD ")

    def quizz_save_btn(self):
        main.quizz_data[self.window.quizz_Que.text()]=[i for i in self.option]
        #main.quizz_data[self.window.quizz_Que.text()].append(self.window.quizz_Ans.text())
        self.window.quizz_Que.setEnabled(False)
        self.window.quizz_Ans.setEnabled(False)
        self.window.option_text.setEnabled(False)
        self.window.add_option.setEnabled(False)
        self.window.quizz_save_btn.setEnabled(False)
        self.window.quizz_edit_btn.setEnabled(True)
        #print(main.quizz_data)

    def editable(self):
        self.window.quizz_Que.setEnabled(True)
        self.window.quizz_Ans.setEnabled(True)
        self.window.option_text.setEnabled(True)
        self.window.add_option.setEnabled(True)
        self.window.quizz_save_btn.setEnabled(True)
        self.window.quizz_edit_btn.setEnabled(False)
        main.quizz_data.pop(self.window.quizz_Que.text())


class Fillups(Setup_urls):
    def __init__(self,url):
        super(Fillups,self).__init__(url)
        self.save_fill=[]
        self.window.save_fill.clicked.connect(lambda: self.save_btn())            # save btn click event define
        self.window.Disable_Fill.clicked.connect(lambda: self.editable())         #edit btn event
        self.window.Disable_Fill.setEnabled(False)

    def save_btn(self):
        #print(self.window.Que.text())
        main.fill_data[self.window.Que.text()]=[self.window.Ans.text()]         # store question and Answer
        self.window.Que.setEnabled(False)
        self.window.Ans.setEnabled(False)
        self.window.save_fill.setEnabled(False)
        self.window.Disable_Fill.setEnabled(True)
       # print(main.fill_data)

    def editable(self):
        self.window.Que.setEnabled(True)
        self.window.Ans.setEnabled(True)
        self.window.save_fill.setEnabled(True)
        main.fill_data.pop(self.window.Que.text())


class Main_window(Setup_urls):
    def __init__(self,url):
        super(Main_window,self).__init__(url)
        self.fill_id=0
        self.fill_object={}  # fillups object store Dictonary?=> if multiple time same save button click then dictonary can't Replicate multiple time
        self.fill_data={}    # fillups Data Store questions are keys 
        self.quizz_id=0
        self.quizz_object={}  # Quizz object store Dictonary?=> if multiple time same save button click then dictonary can't Replicate multiple time
        self.quizz_data={}     # Quizz data Store , Options  are store in Array and Answer of Quizz Store in last of array

    def Button_Click(self):
        self.vbox=QVBoxLayout()
        self.window.Add_Quizz.clicked.connect(self.Quizz_UI_ADD) # quizz add in main frame
        self.window.Add_Fill.clicked.connect(self.Fillup_UI_ADD) # fillup add in main Frame
        self.window.save_Quizz.clicked.connect(self.Xml_generator)
    
    def Fillup_UI_ADD(self):
        self.fill_id+=1
        self.fill_object[self.fill_id]=Fillups("Fillup.ui")
        self.vbox.addWidget(self.fill_object[self.fill_id].window.Fillup)
        self.window.Scroll_Area.setWidget(self.window.Scroll_Area_Content.setLayout(self.vbox))

    def Quizz_UI_ADD(self):
        self.quizz_id+=1
        self.quizz_object[self.quizz_id]=Quizz("Quizz.ui")
        self.vbox.addWidget(self.quizz_object[self.quizz_id].window.final_quiz)
        self.window.Scroll_Area.setWidget(self.window.Scroll_Area_Content.setLayout(self.vbox))
       # self.quizz_object[self.quizz_id].window.add_option.clicked.connect(lambda : self.quizz_object[self.quizz_id].option_add())  # directly can't call

    def Xml_generator(self):
        if(self.window.sheet_name.text() ):
            root = Et.Element('Project',id=self.window.sheet_name.text())
            #add Quizz 
            for i in self.quizz_data:
                sub_quiz=Et.SubElement(root,'Quizz')
                mcq_que=Et.SubElement(sub_quiz,'Question').text=str(i)
                options=Et.SubElement(sub_quiz,'Options')
                for j in self.quizz_data[i]:
                    opt=Et.SubElement(options,'Option').text=str(j)
                ans=Et.SubElement(sub_quiz,'Answer').text=str(self.quizz_data[i][-1])
            # add Fillups
            for i in self.fill_data:
                sub_fill=Et.SubElement(root,'Fullips')
                fill_que=Et.SubElement(sub_fill,'Question').text=str(i)
                answ=Et.SubElement(sub_fill,'Answer').text=str(self.fill_data[i][0])
                
            data=Et.ElementTree(root)
            data.write('Project_dec.xml')
            print("Data Saved")
        else:
            print("Title Is Empty")

QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
app = QApplication(sys.argv)
main=Main_window("sheet_design.ui")
main.Button_Click()
main.window.show()
sys.exit(app.exec_())
