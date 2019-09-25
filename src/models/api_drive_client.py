import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class ApiDriveClient(object):
    
    scopes = ['https://www.googleapis.com/auth/drive']

    def __init__(self):
        self.__get_credentials()
        self.service = build('drive', 'v3', credentials=self.creds)

    @classmethod
    def __get_credentials(cls):
        if os.path.exists('../credentials/token.pickle'):
            with open('../credentials/token.pickle', 'rb') as token:
                cls.creds = pickle.load(token)

        if not cls.creds or not cls.creds.valid:
            if cls.creds and cls.creds.expired and cls.creds.refresh_token:
                cls.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    '../credentials/credentials_secret.json', cls.scopes)
                cls.creds = flow.run_local_server(port=0)

            with open('../credentials/token.pickle', 'wb') as token:
                pickle.dump(cls.creds, token)

    def set_scopes(self, scopes):
        self.scopes = scopes

    def get_service(self):
        return self.service
