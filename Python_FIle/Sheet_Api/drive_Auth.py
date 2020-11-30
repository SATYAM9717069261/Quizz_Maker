"""
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

https://developers.google.com/drive/api/v3/quickstart/python 
 Go in website Click on Enable Drive Api and setup Api

 Down credentals  and Rename it Drive_Credentials.json
 Run this Python File 

 Open Browser and Allow all permission
"""
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class Drive_Setup:
    def check_cred(self,file_path,API_Name,scope,version):

         # The file token.pickle stores the user's access and refresh tokens, and is
         # created automatically when the authorization flow completes for the first
         # time.
        self.creds=None
        self.pickle_name=API_Name+'token.pickle'
        if os.path.exists(self.pickle_name):
            with open(self.pickle_name, 'rb') as self.token:
                self.creds = pickle.load(self.token)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                self.flow = InstalledAppFlow.from_client_secrets_file(file_path, scope)
                self.creds = self.flow.run_local_server(port=0)  # Browser OPen
                # Save the credentials for the next run
                with open(self.pickle_name, 'wb') as token:
                    pickle.dump(self.creds, token)
        self.service = build(API_Name, version, credentials=self.creds)
        # Call the Drive v3 API


    def call_API(self,num):  # num how many file you want show):
        results = self.service.files().list( pageSize=num, fields="nextPageToken, files(id, name)").execute()
        self.items = results.get('files')

"""d=Drive_Setup()
d.check_cred('Sheet_Credentials.json','sheets','https://www.googleapis.com/auth/spreadsheets','v4')
k=Drive_Setup()
k.check_cred('Drive_Credentials.json','drive','https://www.googleapis.com/auth/drive','v3')
print(dir(d))
print(dir(k))
"""
# for Drive and Sheet Authentiaction use different Name Objects 
# if ObjectName was same there are some confits occurs like program confuse which credentials load
