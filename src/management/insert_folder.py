class InsertFolder(object):

    mimeType = 'application/vnd.google-apps.folder'
    folder_metadata = None

    def __init__(self, name, parent):
        self.folder_metadata = {
            'name': name,
            'mimeType': self.mimeType,
            'parent': parent,
        }

    @classmethod
    def add_new_folder(cls, service):
        folder = service.files().create(body=cls.file_metadata, fields='id').execute()
        return folder.get('id')
