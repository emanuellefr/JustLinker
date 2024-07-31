import base64
import msal
import os
from .utils import TENANT_ID, CLIENT_ID, CLIENT_SECRET, CLIENT_SECRET_ID
import requests


class Email:
    def __init__(self):
        # APP MICROSOFT GRAPH
        self.TENANT_ID = TENANT_ID
        self.CLIENT_ID = CLIENT_ID
        self.CLIENT_SECRET = CLIENT_SECRET
        self.CLIENT_SECRET_ID = CLIENT_SECRET_ID

    def _get_token(self):
        tenant_id = self.TENANT_ID
        url = f'https://login.microsoftonline.com/{tenant_id}'
        client_id = self.CLIENT_ID
        client_secret = self.CLIENT_SECRET_ID
        scope = ['https://graph.microsoft.com/.default']

        app = msal.ConfidentialClientApplication(
            client_id,
            authority=url,
            client_credential=client_secret
        )
        token = app.acquire_token_silent(scopes=scope, account=None)
        if not token:
            token = app.acquire_token_for_client(scopes=scope)

        if 'access_token' in token:
            return token['access_token']
        else:
            return token.get('error_description')

    def create_attachment(self, file_path):
        if not os.path.exists(file_path):
            return False

        with open(file_path, "rb") as file:
            content_bytes = file.read()
            content_base64 = base64.b64encode(content_bytes).decode('utf-8')
            attachment = {
                "@odata.type": "#microsoft.graph.fileAttachment",
                "name": file_path.split("/")[-1],
                "contentBytes": content_base64,
                "contentType": "application/octet-stream"
            }
            return attachment

    def _send_email(self, email_id, destino, subject, body, contentType, attachments=None):
        token = self._get_token()
        if not token:
            return False

        url = f'https://graph.microsoft.com/v1.0/users/{email_id}/sendMail'
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        message = {
            "subject": subject,
            "body": {
                "contentType": contentType,
                "content": body
            },
            "toRecipients": [{"emailAddress": {"address": destino}}]
        }
        if attachments:
            attachments = self.create_attachment(attachments)
            message["attachments"] = [attachments]

        payload = {
            "message": message,
            "saveToSentItems": "true"
        }
        try:
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code == 202:
                return {'success': True, 'msg': f'Email enviado com sucesso!', 'tipo': 'email'}
            else:
                return {'success': False, 'msg': f'Falha ao enviar o email: {response.status_code} - {response.text}',
                        'tipo': 'email'}
        except Exception as e:
            return {'success': False, 'msg': f'Exceção ao enviar o email: {str(e)}', 'tipo': 'email'}

    def sendEmail(self, email_id, destino, subject, body, contentType='HTML', attachments=None):
        return self._send_email(email_id, destino, subject, body, contentType, attachments)


