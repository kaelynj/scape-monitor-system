from __future__ import print_function

import os.path
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload


# If modifying these scopes, delete the file token.json.
#SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
SCOPES = ['https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive.metadata.readonly']

def get_credentials():
    ''' Obtain user credentials.  First by checking if the auth token file
    exists, ask the user to login and validate the credentials if it doesn't
    '''
    creds = None
    if os.path.exists('token.json'):
        with open('token.json', 'r') as tokenFile:
            tokenData = json.load(tokenFile)
        #Check to make sure scopes of token match
        scopeCheck = [scope in tokenData['scopes'] for scope in SCOPES]
        if all(scopeCheck):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        else:
            creds = None
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


def upload_file(folderName, fileName):
    """Upload test image to a specified folder
    """
    creds = get_credentials()
    try:
        service = build('drive', 'v3', credentials=creds)

        #Call the drive v3 API
        query = "name = '{}'".format(folderName)
        gdriveFolder = service.files().list(q=query,     # will query (look) for folderName
                                        spaces='drive',
                                        fields='nextPageToken, '
                                                'files(id, name)').execute()

        # Will use the first folder the query finds as the location to upload
        folders = gdriveFolder.get('files', [])
        if not folders:
            print("Folder wasn't found, uploading into home directory...")
            fileMetadata = {'name':fileName}
        else:
            folderID = folders[0]['id']
            fileMetadata = {'name':fileName,
                            'parents': [folderID]}

        media = MediaFileUpload(fileName,
                                        mimetype='image/jpeg',
                                        resumable=True)
        file = service.files().create(body=fileMetadata, media_body=media,
                                        fields='id').execute()
        print("File ID: {} ".format(file.get("id")))
        return file.get('id')


    except HttpError as error:
        #You should handle errors here in case of no connection
        print('An error occured: {}'.format(error))
