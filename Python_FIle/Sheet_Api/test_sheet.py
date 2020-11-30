# first create sheet then move that sheet in directory 
# there is noway to direct create sheet in perticular directory
# Never use driveobj veriable 
from drive_Auth import Drive_Setup
__dirname__="Quizz_Application"  # fix Folder Name where all Excel File Stored
class sheet_opr(Drive_Setup):
    def __init__(self,api_name):
        if(api_name=='sheet'):
            self.check_cred('Sheet_Credentials.json','sheets','https://www.googleapis.com/auth/spreadsheets','v4')
        if(api_name=='drive'):
            self.check_cred('Drive_Credentials.json','drive','https://www.googleapis.com/auth/drive','v3')

    def create_sheet(self,name): # return Sheet id
        find=self.find_sheet(name)
        if(find is  None):
            print("File not Existed")
            sheet_body = {
                'properties': {
                    'title': name,
                    'locale': 'en_US',
                    'autoRecalc': 'ON_CHANGE', 
                    'timeZone': 'America/Los_Angeles'
                    },
                'sheets': [
                    {
                        'properties': {
                            'title': 'Sales South'
                            }
                        },{
                            'properties': {
                                'title': 'Sales North'
                                }
                            }
                        ]
                }
            self.__data__=self.service.spreadsheets().create(body=sheet_body).execute()
            self.sheet_move(self.__data__['spreadsheetId'] )
            return self.__data__['spreadsheetId']
        else:
            print("Sheet Already Existed")
            return find


    def sheet_move(self,sheet_id):
        __driveobj__=sheet_opr('drive')
        dir_id=[i['id'] for i in  __driveobj__.service.files().list().execute().get('files',[]) if(i['name']=="Quizz_Application" )] # geting file id for moving
         
        # moving excel file in Directory
        # Only change file id and folder id cann't change anything 
        file_id = sheet_id
        folder_id = dir_id[0]
        # Retrieve the existing parents to remove
        file = __driveobj__.service.files().get(fileId=file_id,
                                 fields='parents').execute();
        previous_parents = ",".join(file.get('parents'))
        # Move the file to the new folder
        file = __driveobj__.service.files().update(fileId=file_id,
                                    addParents=folder_id,
                                    removeParents=previous_parents,
                                    fields='id, parents').execute()
        del __driveobj__
        # End moving Excel end


    def find_sheet(self,sheet_name):
        __driveobj__=sheet_opr('drive')
        for i in  __driveobj__.service.files().list().execute().get('files',[]):
            if(i['name']==sheet_name):
                return i['id']
        del __driveobj__
        return None


obj1=sheet_opr('sheet')
id=obj1.create_sheet("DemoSheet")  # return Sheet id
