from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import base64
import email
import json

SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'

# Setup the Gmail API
def create_gmail_service():
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))
    return service

def get_message_snippet(service, message_id, user_id = 'me', format = 'raw'):
    message = service.users().messages().get(userId=user_id, id=message_id,
                                             format=format).execute()
    return message['snippet']

def confirm_snippet(snippet):
    sender = "sender_id" in snippet
    lat = "lat" in snippet
    log = "long" in snippet
    return sender and lat and log

def parse_snippet(snippet):
    snippet = snippet.replace('&quot;','"')
    try:
        obj = json.loads(snippet)
        return obj
    except:
        return None

def get_user_data(service, user_id = 'me'):
    msgs = service.users().messages().list(userId=user_id,labelIds=['INBOX']).execute()
    if 'messages' not in msgs:
        return None
    msgs = msgs['messages']
    user_data = []
    for m in msgs:
        message_snippet = get_message_snippet(service, message_id = m['id'], user_id = user_id)
        if confirm_snippet(message_snippet):
            data = parse_snippet(message_snippet)
            if data is not None:
                user_data.append(data)
    return user_data



if __name__ == "__main__":
    gmail = create_gmail_service()
    user_data = get_user_data(gmail)
    print(user_data)
