import xml.etree.ElementTree as ET

mytree =ET.parse("Project_dec.xml")

myroot =mytree.getroot()

#myroot.attrib # return attribute
"""
for i in myroot:
    print("Root tag=> "+str(i.tag))
    for j in i:
        print(j.tag)

    print("\n")

    """

for i,q_num in zip(myroot,range(len(myroot))):       # Only for Quizz
    if(str(i.tag)=="quizz"):
        print("Q"+str(q_num+1)+" "+str(i[0].text))
        

        for j,ans_num in zip(i[1],range(len(i[1]))):
            print("Option"+str(ans_num+1)+ " "+str(j.text))

        print("Answer: "+str(i[2].text))


    if(str(i.tag)=="Fullips"):
        print("Q"+str(q_num+1)+" "+str(i[0].text))
        print("Answer: "+str(i[1].text))
        
