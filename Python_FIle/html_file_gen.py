import xml.etree.ElementTree as ET 

def html_file_data():
    mytree =ET.parse("Project_dec.xml")
    myroot =mytree.getroot()
    value=[]
    S_no=0
    for i,q_num in zip(myroot,range(len(myroot))):       # Only for Quizz
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
    print(value)


def base():


html_file_data()
