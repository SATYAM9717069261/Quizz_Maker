import xml.etree.cElementTree as Et
import os
class dic_to_Xml:
    def __init__(self,name):
        self.project_Name=name
        self.fill={}
        self.quizz={}

    def fill_data(self):
        for i in range(10):
            self.fill[i]="Answer"
        #print(self.fill)

    def quizz_data(self):
        for i in range(10):
            self.quizz[i]=[j for j in range(4)]
        #print(self.quizz)

    def write_file(self):
        root = Et.Element('Project',id=self.project_Name)
        sub_quiz=Et.SubElement(root,'quizz')
        


        for i in self.quizz:
            que=Et.SubElement(sub_quiz,'Question').text=str(i)
            options=Et.SubElement(sub_quiz,'options')
            for j in self.quizz[i]:
                opt=Et.SubElement(options,'Option').text=str(j)

        data=Et.ElementTree(root)
        data.write('Project_dec.xml')






obj1=dic_to_Xml("Project2")
obj1.fill_data()
obj1.quizz_data()
obj1.write_file()
