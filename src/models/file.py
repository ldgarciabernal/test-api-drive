from googleapiclient.http import MediaFileUpload
import magic


class File(object):

    def __init__(self, name, file_path, service):
        self.file_path = file_path 
        self.mimetype = self.__get_mime_type()
        self.name = name
        self.service = service

    def create(self, folder_id):
        file_metadata = self.__get_file_metadata(folder_id)

        media = MediaFileUpload(self.file_path, mimetype=self.mimetype, resumable=True)
        file = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        return file.get('id')

    def __get_file_metadata(self, folder_id):
        return {
            'name': self.name,
            'parent': [folder_id],
        }

    def __get_mime_type(self):
        mime = magic.Magic(mime=True)
        return mime.from_file(self.file_path)
