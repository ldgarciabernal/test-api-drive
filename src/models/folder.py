
from googleapiclient.http import MediaFileUpload
import magic
from src.models.api_drive_client import ApiDriveClient


class Files(ApiDriveClient):

    mimeType = 'application/vnd.google-apps.folder'

    def __init__(self):
        super(Files, self).__init__()

    def create_folder(self, name, parent='root'):
        folder_metadata = self.__get_metadata(name, self.mimeType, parent)

        folder = self.service.files().create(body=folder_metadata, fields='id').execute()
        return folder.get('id')

    def create_file(self, name, file_path, folder_id):
        mimetype = self.__get_mime_type(file_path)
        file_metadata = self.__get_metadata(name, mimetype, folder_id)

        media = MediaFileUpload(file_path, mimetype=mimetype, resumable=True)
        file = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        return file.get('id')

    def get_first_ten_files(self):
        results = self.service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            return None
        else:
            return items

    def set_folder_permissions(self):
        pass

    @staticmethod
    def __get_mime_type(file_path):
        mime = magic.Magic(mime=True)
        return mime.from_file(file_path)

    @staticmethod
    def __get_metadata(name, mimetype, parent):
        return {
            'name': name,
            'mimeType': mimetype,
            'parents': [parent],
        }