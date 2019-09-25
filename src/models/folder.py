from googleapiclient.http import MediaFileUpload
import magic


class Files(object):

    mimeType = 'application/vnd.google-apps.folder'

    def __init__(self, service):
        self.service = service

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

    @staticmethod
    def __get_mime_type(file_path):
        mime = magic.Magic(mime=True)
        return mime.from_file(file_path)

    @staticmethod
    def __get_metadata(name, mimetype, parent):
        return {
            'name': name,
            'mimeType': mimetype,
            'parent': [parent],
        }