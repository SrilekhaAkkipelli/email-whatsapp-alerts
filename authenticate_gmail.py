import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Gmail API scope - read-only access
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail(credentials_file='credentials.json'):
    """
    Authenticate with Gmail API using OAuth 2.0.
    Stores token in token.pickle for future use.
    Returns Gmail API service object.
    """
    creds = None

    # Load existing token if available
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # Refresh or re-authenticate if needed
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_file, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save token for next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('gmail', 'v1', credentials=creds)


def get_unread_emails(service):
    """Fetch all unread emails from inbox."""
    results = service.users().messages().list(userId='me', q='is:unread').execute()
    return results.get('messages', [])


def extract_subject_sender(service, msg_id):
    """Extract subject and sender from a Gmail message."""
    msg = service.users().messages().get(
        userId='me',
        id=msg_id,
        format='metadata',
        metadataHeaders=['Subject', 'From']
    ).execute()

    headers = msg['payload']['headers']
    subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
    sender  = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown')

    return sender, subject


if __name__ == '__main__':
    service = authenticate_gmail()
    messages = get_unread_emails(service)
    print(f"Found {len(messages)} unread emails.")
    for msg in messages[:5]:
        sender, subject = extract_subject_sender(service, msg['id'])
        print(f"From: {sender} | Subject: {subject}")

# update 5 - 2025-01-13
# update 7 - 2025-01-15
# update 18 - 2025-01-21
# update 19 - 2025-01-21
# update 27 - 2025-01-26
# update 43 - 2025-02-04
# update 45 - 2025-02-06
# update 53 - 2025-02-09
# update 65 - 2025-02-16