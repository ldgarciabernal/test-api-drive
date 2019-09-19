from googleapiclient.http import MediaFileUpload
import magic
from api_drive_client import ApiDriveClient


class File(object):
    
    file_path = ''
    mimetype = None
    name = ''
    service = None

    def __init__(self, name, file_path, service)
        self.file_path = file_path 
        mimetype = __get_mime_type()
        self.name = name
        self.service = service

    @classmethod
    def create(cls, folder_id)
        file_metadata = __get_file_metadata(folder_id)

        media = MediaFileUpload(cls.file_path, mimetype=cls.mimetype, resumable=True)
        file = cls.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        return file.get('id')

    @classmethod
    def __get_file_metadata(cls, folder_id):
        return {
            'name': cls.name,
            'parent': [folder_id],
        }

    @classmethod
    def __get_mime_type(cls):
        mime = magic.Magic(mime=True)
        return mime.from_file(cls.file_path)