import base64
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

# Gmail API 스코프
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# Google OAuth 인증
def authenticate():
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json',  # 다운로드한 JSON 파일의 경로
        SCOPES
    )
    # 인증 후 리디렉션할 URL 설정
    flow.redirect_uri = 'http://localhost:8501'
    
    credentials = flow.run_local_server(port=0)
    return credentials

# Gmail에서 모든 이메일 추출
def extract_emails(credentials):
    service = build('gmail', 'v1', credentials=credentials)
    results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
    messages = results.get('messages', [])

    extracted_emails = []

    if not messages:
        print('No emails found.')
    else:
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            headers = msg['payload'].get('headers', [])

            # 이메일에서 원하는 내용 추출
            text = ''
            From = ''
            Subject = ''
            Date = ''

            parts = msg['payload'].get('parts', [])
            for part in parts:
                mimeType = part.get('mimeType')
                body = part.get('body', {})
                data = body.get('data')
                if part['mimeType'] == 'text/plain' and data:
                    text = base64.urlsafe_b64decode(data).decode('utf-8')
                    print('Email Content:')
                    print(text)
                    print('-------------------')

            for header in headers:
                name = header.get('name', '').lower()
                if name == 'from':
                    From = header.get('value')
                elif name == 'subject':
                    Subject = header.get('value')
                elif name == 'date':
                    Date = header.get('value')

            # 추출한 내용 저장
            extracted_emails.append({
                'Date': Date,
                'From': From,
                'Subject': Subject,
                'Body': text
            })
            print("BODY", extracted_emails[0]["Body"])
    return extracted_emails
