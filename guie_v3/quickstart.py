from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

#from src.management.insert_folder import InsertFolder
# good structure: https://docs.python-guide.org/writing/structure/
# If modifying these scopes, delete the file token.pickle.


SCOPES = ['https://www.googleapis.com/auth/drive'] # especie de permisos/ acceso del usuario

def callback(request_id, response, exception):
    if exception:
        # Handle error
        print(exception)
    else:
        print("Permission Id: %s" % response.get('id'))

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('credentials/token.pickle'):
        with open('credentials/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials/client_secret_855707331349-pdgs54ha5lfmfioj3j3o513g9odo9heb.apps.googleusercontent.com', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('credentials/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)
    """
    file_id = '1g6qh8K7rq5G2IbtGyTaHGjymIupaNnhY'

    batch = service.new_batch_http_request(callback=callback)
    user_permission = {
        'type': 'user',
        'role': 'reader',
        'emailAddress': 'luis.garcia@opinno.com'
    }
    perId = '07579917493837771955'
    batch.add(service.permissions().delete(
            fileId=file_id,
            permissionId=perId,
            fields='id',
    ))

    
    'reader', 'commenter', 'writer', 'fileOrganizer', 'organizer', and 'owner'
    Permission Id: 07579917493837771955
    domain_permission = {
        'type': 'domain',
        'role': 'reader',
        'domain': 'opinno.com'
    }
    batch.add(service.permissions().create(
            fileId=file_id,
            body=domain_permission,
            fields='id',
    ))
    
    batch.execute()
    # Call the Drive v3 API
    """
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))
    """
    folder = InsertFolder("TEST CLASS", 'root')
    folder.add_new_folder(service)
    

    folder_id = '1g6qh8K7rq5G2IbtGyTaHGjymIupaNnhY'
    file_metadata = {
        'name': 'photo.jpg',
        'parents': [folder_id]
    }
    media = MediaFileUpload('media/photo.jpg', mimetype='image/jpeg', resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print('File ID: %s' % file.get('id'))
    """


if __name__ == '__main__':
    main()