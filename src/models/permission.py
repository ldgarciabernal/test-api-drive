
class Permission(object):

    service = None

    def __init__(self, service):
        self.service = service

    def set_folder_permission(self, type_, role, email, file_id):
        permission_metadata = self.__get_body(type_, role, email)

        self.service.permissions().create(
            fileId=file_id,
            body=permission_metadata,
            fields='id',
        )

    def get_folder_permission(self, folder_id):
        folder = self.service.files().get(fileId=folder_id)

        return folder.get('permissions')

    @staticmethod
    def __get_body(type_, role, email):
        return {
            'type': type_,
            'role': role,
            'emailAddress': email,
        }
