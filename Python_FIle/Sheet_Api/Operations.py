from drive_Auth import Drive_Setup

__dirname__="Quizz_Application"  # fix Folder Name where all Excel File Stored
class Drive_opr(Drive_Setup):
    def __init__(self):
        super(Drive_opr,self).__init__()
        super(Drive_opr,self).check_cred('Drive_Credentials.json','drive','https://www.googleapis.com/auth/drive','v3')
        
    def find(self,path=__dirname__):          # use for both dir and file search
        self.response=self.service.files().list().execute()
        for i in self.response.get('files', []):
            if(i['name']==path):
                return i['id']
        return False

    def create_dir(self):
        file_metadata = {
                'name':__dirname__,
                'mimeType': 'application/vnd.google-apps.folder'
                }
        file = self.service.files().create(body=file_metadata).execute()
        return file.get('id')

        

class sheet_opr(Drive_Setup):
    def __init__(self):
        super(Drive_opr,self).__init__()
        super(Drive_opr,self).check_cred('Sheet_Credentials.json','Sheets','https://www.googleapis.com/auth/spreadsheets','v4')


    def create_file(name):
        file_metadata={'name':name+'. xlsx',
                file_metadata={'name':name+'. xlsx',
                    'minmeType':'application/vnd.google-apps.spreadsheet',
                    'parents': [dir_id]
                    }


    def main(self,name):
        dir_id=self.find()   # check main directory

        if(dir_id is False):
            #directory is missing So Create it
            dir_id=direct.create_dir()

        sheet_id=self.find(name)  #cheack spreed sheet
        if(sheet_id is False):
            # create file
            create_file(name) # return id

obj1=sheet_opri()
