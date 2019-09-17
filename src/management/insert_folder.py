class InsertFolder(object):

    mimeType = 'application/vnd.google-apps.folder'
    file_metadata = None

    def __init__(self, name, parent):
        self.file_metadata = {
            'name': name,
            'mimeType': self.mimeType,
            'parent': parent,
        }

    @classmethod
    def add_new_folder(cls, service):
        file = service.files().create(body=cls.file_metadata, fields='id').execute()
        print('Folder ID: %s' % file.get('id'))
