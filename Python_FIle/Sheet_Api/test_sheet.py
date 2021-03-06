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
        return self.__data__['spreadsheetId']


    def sheet_move(self,sheet_id):
        __driveobj__=sheet_opr('drive')
        file_id=[i['id'] for i in  __driveobj__.service.files().list().execute().get('files',[]) if(i['name']=="Quizz_Application" )] # geting file id for moving
        
        # moving excel file in Directory


        source_folder_id=''
        target_folder_id=''
        query=f"parents = '{source_folder_id}' "
        response=service.files().list(q=query).execute()
        file=response.get('files')
        nextPageToken=response.get('nextPageToken')
        
        while nextPageToken:
            respose=service.file().list(q=query,pageToken=nextPageToken).execute()
            files.extend(response.get('files'))
            nextPageToken=response.get('nextPageToken')
            
        for f in files:
            if f['mineType'] != 'application/vnd.google-apps.folder':
                service.files().update(
                        fileId=f.get('id'),
                        addParents=target_folder_id,
                        removeParents=source_folder_is
                        ).execute()


        # moving Excel end





obj1=sheet_opr('sheet')
#id=obj1.create_sheet("DemoSheet")
obj1.sheet_move(id)

