from __future__ import print_function

import os.path
from decouple import config
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


class ScrapingMail():
    
  def service(self):
      """Shows basic usage of the Gmail API.
      Lists the user's Gmail labels.
      """

      creds = None
      # The file token.json stores the user's access and refresh tokens, and is
      # created automatically when the authorization flow completes for the first
      # time.
      if os.path.exists('token.json'):
          creds = Credentials.from_authorized_user_file('token.json', self.SCOPES)
      # If there are no (valid) credentials available, let the user log in.
      if not creds or not creds.valid:
          if creds and creds.expired and creds.refresh_token:
              creds.refresh(Request())
          else:
              flow = InstalledAppFlow.from_client_secrets_file(
                  config('CREDENTIAL_GCP'), self.SCOPES)
              creds = flow.run_local_server(port=0)
          # Save the credentials for the next run
          with open('token.json', 'w') as token:
              token.write(creds.to_json())

      service = build('gmail', 'v1', credentials=creds)
      return service

  def search_messages(self,service, query):
      result = service.users().messages().list(userId='me',q=query).execute()
      messages = []
      if 'messages' in result:
          messages.extend(result['messages'])

      while 'nextPageToken' in result:
          page_token = result['nextPageToken']
          result = service.users().messages().list(userId='me',q=query,pageToken=page_token).execute()
          if 'messages' in result:
              messages.extend(result['messages'])
      return messages

  def mark_as_read(self,service,messages_to_mark, query):
      #messages_to_mark = ScrapingMail.search_messages(self,service, query)
      # add the label UNREAD to each of the search results
      return service.users().messages().batchModify(
          userId='me',
          body={
              'ids': [msg['id'] for msg in messages_to_mark],
              'removeLabelIds': ['UNREAD']
          }
      ).execute()
  
  def read_message(self, service, message):
    msg = service.users().messages().get(userId='me', id=message['id'], format='full').execute()
    payload = msg['payload']
    parts = payload.get("parts")
    headers = payload.get("headers")

    return parts, headers
  
  def get_message_detail(self,service,message_id, msg_format='metadata',metadata_headers: list=None):
    message_detail = service.users().messages().get(
        userId='me',
        id=message_id,
        format=msg_format,
        metadataHeaders=metadata_headers
    ).execute()
    return message_detail

  def get_file_data(self,service,message_id,attachment_id,file_name,save_location):
      response = service.users().messages().attachments().get(
          userId='me',
          messageId=message_id,
          id=attachment_id,
      ).execute()
      file_data = base64.urlsafe_b64decode(response.get('data').encode('UTF-8'))
      with open(os.path.join(save_location,file_name),'wb') as f:
          f.write(file_data)
      #return file_data