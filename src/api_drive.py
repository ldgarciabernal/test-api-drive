from googleapiclient.discovery import build
from src.management.insert_folder import InsertFolder
from src.management.insert_file import insertFileIntoSpecificFolder
from src.auth import Auth


class ApiDriveClient(object):

    scopes = ['https://www.googleapis.com/auth/drive']
    service = None

    def __init__(self):
        authentication = Auth(self.scopes)
        creds = authentication.get_credentials()
        service = build('drive', 'v3', credentials=creds)

    @classmethod
    def set_scopes(cls, scopes):
        cls.scopes = scopes

    @classmethod
    def create_folder(cls, name, parent):
        folder = InsertFolder(name, parent)
        folder_id = folder.add_new_folder(cls.service)
        return folder_id

    @classmethod
    def create_file(cls, name, folder_id, file_path):
        file = insertFileIntoSpecificFolder(name, folder_id)
        file_id = file.add_file(cls.service, file_path)
        return file_id

    
    @classmethod
    def set_permission_folder(cls, file_id, emails):
        pass