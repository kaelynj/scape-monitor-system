from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from googleapiclient.http import MediaFileUpload


# If modifying these scopes, delete the file token.json.
#SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
SCOPES = ['https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive.metadata']

def get_credentials():
    ''' Obtain user credentials.  First by checking if the auth token file
    exists, ask the user to login and validate the credentials if it doesn't
    '''
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, have the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            cred_secrets_file = input("Filename of client_secret: ")
            flow = InstalledAppFlow.from_client_secrets_file(cred_secrets_file, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save teh credentials for the next run
        with open('token.json', 'w') as tokenFile:
            tokenFile.write(creds.to_json())
    return creds

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = get_credentials()
    try:
        service = build('drive', 'v3', credentials=creds)

        # Call the Drive v3 API
        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
            return
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')


def uploadTest():
    """Upload test image to a specified folder
    """
    creds = get_credentials()
    try:
        service = build('drive', 'v3', credentials=creds)

        #Call the drive v3 API
        scapeFolder = service.files().list(q="name = 'ScapePhotos'", #q="mimeType = 'application/vnd.google-apps.folder'", # will query all folders q="name = 'ScapePhotos'"
                                        spaces='drive',
                                        fields='nextPageToken, '
                                                'files(id, name)').execute()

        # Make this a less bespoke approach, add in modularity
        folders = scapeFolder.get('files', [])
        folder_id = folders[0]['id']
        file_metadata = {'name':'test-scape-image.jpg',
                        'parents': [folder_id]}
        media = MediaFileUpload('test-scape-image.jpg',
                                        mimetype='image/jpeg',
                                        resumable=True)
        file = service.files().create(body=file_metadata, media_body=media,
                                        fields='id').execute()
        print("File ID: {} ".format(file.get("id")))
        return file.get('id')

        if not results:
            print('Nothing found...')
            return
        #folders = results.get('files', [])
        #print(folders)
        for item in folders:
            print('{} ({})'.format(item['name'], item['id']))
        print("############################################################")
    except HttpError as error:
        #You should handle errors here in case of no connection
        print('An error occured: {}'.format(error))

if __name__ == '__main__':
    #main()
    uploadTest()
