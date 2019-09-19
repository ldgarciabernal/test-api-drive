
class Folder(object):

    mimeType = 'application/vnd.google-apps.folder'
    name =''
    parent = 'root'
    service = None

    def __init__(self, name, service):
        self.name = name
        self.service = service

    @classmethod
    def create(cls, parent):
        folder_metadata = cls.__get_folder_metadata(parent)

        folder = cls.sservice.files().create(body=folder_metadata, fields='id').execute()
        return folder.get('id')

    @classmethod
    def __get_folder_metadata(cls, parent):
        return {
            'name': cls.name,
            'mimeType': cls.mimeType,
            'parent': parent,
        }