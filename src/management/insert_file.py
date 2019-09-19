from googleapiclient.http import MediaFileUpload
import magic


class insertFileIntoSpecificFolder(object):
    """
        https://github.com/ahupp/python-magic
        https://developers.google.com/drive/api/v3/folder?authuser=1
        https://developers.google.com/drive/api/v3/reference/files/create?authuser=1
    """
    folder_id = '1g6qh8K7rq5G2IbtGyTaHGjymIupaNnhY'
    file_metadata = None

    def __init__(self, name, folder_id):
        self.file_metadata = {
            'name': name,
            'parent': [folder_id],
        }

    @classmethod
    def add_file(cls, service, file_path):
        media = MediaFileUpload(file_path, mimetype=cls.__get_mime_type(file_path), resumable=True)
        file = service.files().create(body=cls.file_metadata, media_body=media, fields='id').execute()
        return file.get('id')

    @staticmethod
    def __get_mime_type(file_path):
        mime = magic.Magic(mime=True)
        return mime.from_file(file_path)
