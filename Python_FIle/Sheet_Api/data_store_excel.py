# Question Append ? 
# Student Append OK !

import xml.etree.ElementTree as ET 
from drive_Auth import Drive_Setup

class data_save(Drive_Setup):
    def __init__(self):
        self.head_strt_value=97 # use for Aplhabets 
        self.check_cred('Sheet_Credentials.json','sheets','https://www.googleapis.com/auth/spreadsheets','v4')


    def student_list(self):
        self.St_list=['Satyam','Vasant Govind Patil','Debjyoti Roy','Mandal','Harsh']
        """
        here add Student list using Excel or Mainual
        """
        self.head_strt_value+=len(self.St_list)


    def sheet_head(self):
        head=["Sno.","Question","Option","Answer"]
        self.head_strt_value+=len(head)
        for i in self.St_list:
            head.append(i)

        values=[ head  ]
        body={'values':values}

        result = self.service.spreadsheets().values().update(spreadsheetId="1NfAi49UWTh7FQPfibrE91MgN-AWCD4YIA8EA_lzna5s", 
                range="A1:"+ chr(self.head_strt_value)+ "1",valueInputOption="USER_ENTERED", body=body).execute()

    def Question_add(self):
        mytree =ET.parse("../Project_dec.xml")
        myroot =mytree.getroot()
        values=[]
        S_no=0
        for i,q_num in zip(myroot,range(len(myroot))):       # Only for Quizz
            value=[]
            opt=""
            value.append(q_num+1)
            if(str(i.tag)=="quizz"):
                value.append(str(i[0].text))
                for j,ans_num in zip(i[1],range(len(i[1]))):
                    opt+=str(j.text)
                    opt+="\n"
                value.append(opt)
                value.append(str(i[2].text))
                
            if(str(i.tag)=="Fullips"):
                value.append(str(i[0].text))
                value.append(" ")
                value.append(str(i[1].text))
                
            values.append(value)
        body={'values':values}
        result = self.service.spreadsheets().values().update(spreadsheetId="1NfAi49UWTh7FQPfibrE91MgN-AWCD4YIA8EA_lzna5s",
                range="A2:D"+str(len(values)+1),valueInputOption="USER_ENTERED", body=body).execute()

  
    def append_Student(self,*name):           #Extract Header then add name and Update header 
        
        #data Extract from excel file
        values=[]
        header=self.service.spreadsheets().values().get(spreadsheetId="1NfAi49UWTh7FQPfibrE91MgN-AWCD4YIA8EA_lzna5s",
                range="A1:Z1",majorDimension='COLUMNS').execute() # Z1 fix if number of student greater then 26 then Z1 is change first increase Column then change ite scaning Size

        value=[i[0] for i in header['values'] ]     # add Previous name
        value+=[i for i in name]            # add New Name
        #print(value)
        values.append(value)
        body={'values':values}
        #self.head_strt_value
        result =self.service.spreadsheets().values().update(spreadsheetId="1NfAi49UWTh7FQPfibrE91MgN-AWCD4YIA8EA_lzna5s",
                range="A1",valueInputOption="USER_ENTERED", body=body).execute()





obj1=data_save()
obj1.student_list()
obj1.sheet_head()
obj1.Question_add()
obj1.append_Student('SAM','Killer')
