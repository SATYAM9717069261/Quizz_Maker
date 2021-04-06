class BaseOperation:
    def __init__(self):
         self.__switcher={
                  'Html':['<html>','</html>'],
                  'style':['<style>','</style>'],
                  'body':['<body>','</body>'],
                  'div':['<div>','</div>'],
                  'Project':['<table>','</table>'],
                  'Question':['<tr><th> Question : </th> <td>','</td></tr>'],
                  'Options':['<tr>','</tr>'],
                  'Option':['<td>','</td>'],
                  'Answer':['<tr><th> Answer : </th> <td>','</td></tr>'],
                  'Script':['<script>','</script>']
                }
    def create_html_element(self,data):
        opentag,closetag=self.__switcher.get(data,["",""])
        return opentag,closetag;

    def chk_tag(self,tag):
        __tag=self.__switcher.get(tag,"")
        if(__tag!=""):
            return True;
        else:
            return False;

    def add_attribute(self,tag_name,atr,val):
        if(self.chk_tag(tag_name)==False):
            return None
        self.__switcher[tag_name]=[ self.__switcher[tag_name][0][0:-1],self.__switcher[tag_name][1] ];
        self.__switcher[tag_name]=[ self.__switcher[tag_name][0]+" {0}='{1}'>".format(atr,val) ,self.__switcher[tag_name][1] ];
        print(self.__switcher[tag_name])
    
    def template(self,html_filename,script_filename,stylesheet_filename):
        


"""
obj1=BaseOperation()
obj1.add_attribute("Html","class","demo")
obj1.add_attribute("Html","style","'padding:10px'")
obj1.add_attribute("Html","click","function()")
"""


class HTML_FILE(BaseOperation):
    def __init__(self,xml_filename,html_filename,tag):
        with open(xml_filename,'r')as xml_file:
            self.file_data=xml_file.read()
        self.html_file=open(html_filename,tag)
        super().__init__();
        
    def search_tag_html(self,tag): # trim '<,> from tag (for dictonary)'
        tag_nam=''
        for i in tag[1:]:
            if(i=='>' or i==' ' or i=='/'):
                break;
            else:
                tag_nam+=i;
        return self.create_html_element(tag_nam)

    def data_extract(self,rawdata):  # extract data from tag (dfdfdfj</Project>))
        data=""
        tag=""
        if(rawdata[0]=='<'):
            return ("",rawdata)
        else:
            for i in rawdata:
                if(tag=="" and i!='<'):
                    data+=i
                else:
                    tag+=i
        return(data,tag)
    
    def html_file_creator(self,strt_scan=0):   # find tages only not data
        tag_name=""
        for i in self.file_data[strt_scan:]:
            if(i=='>'):
                tag_name+=i
                data,tag=self.data_extract(tag_name)
                start_tag,end_tag=self.search_tag_html(tag)
                data_found=data
                self.html_file.write(start_tag+data)
                self.html_file_creator(strt_scan+1)
                self.html_file.write(end_tag)
                return "HTml file is Ready"
            else:
                tag_name+=i
                strt_scan+=1


obj1=HTML_FILE('Project_dec.xml','index.html','w') # extend-a , new-'w'
obj1.html_file_creator(0)
obj1.html_file.close()

#print(search_tag('</Project id="dfkjdfslflsfdjl">'));
#html_page(1,2,3)
#print(data) 
