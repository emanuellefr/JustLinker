import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from utils import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS


class Email:
    def __init__(self):
        # Constructor com configs e credenciais de login
        self.HOST = SMTP_HOST
        self.PORT = SMTP_PORT
        self.USER = SMTP_USER
        self.PASS = SMTP_PASS
        self.FROM = 'relatorio@justweb.com.br'

    def _configura_servidor_smtp(self):
        server = smtplib.SMTP(self.HOST, self.PORT)
        server.starttls()
        server.login(self.USER, self.PASS)
        return server

    def _send_email(self, to_list, subject, body, attachments=None, simple=None):
        try:
            server = self._configura_servidor_smtp()
            msg = MIMEMultipart()
            msg['From'] = self.FROM
            msg['To'] = ", ".join(to_list)
            msg['Subject'] = subject
            if simple:
                msg.attach(MIMEText(body, 'text'))
            else:
                msg.attach(MIMEText(body, 'html'))
            if attachments:
                for caminho, filename in attachments:
                    with open(caminho, 'rb') as attachment:
                        att = MIMEBase('application', 'octet-stream')
                        att.set_payload(attachment.read())
                        encoders.encode_base64(att)
                        att.add_header('Content-Disposition', f'attachment; filename = {filename}')
                        msg.attach(att)

            server.sendmail(self.FROM, to_list, msg.as_string())
            server.quit()
            return True, None
        except Exception as e:
            return False, f"Erro ao enviar e-mail: {str(e)}"

    def sendEmail(self, to_list, subject, body):
        return self._send_email(to_list, subject, body, simple=True)
    def sendEmailHTML(self, to_list, subject, body):
        return self._send_email(to_list, subject, body)

    def sendEmailAnexo(self, to_list, subject, body, attachments):
        return self._send_email(to_list, subject, body, attachments)

