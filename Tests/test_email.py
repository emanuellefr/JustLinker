import smtplib
import pytest
from unittest.mock import patch, MagicMock, mock_open
from Classes.Email import Email


@pytest.fixture
def email_instance():
    return Email()

def test_send_email_success(email_instance):
    to_list = ['test@example.com']
    subject = 'Test Subject'
    body = 'Test Body'

    with patch.object(email_instance, '_configura_servidor_smtp', return_value=MagicMock()) as mock_config_smtp, \
            patch.object(smtplib.SMTP, 'sendmail', return_value=None) as mock_sendmail, \
            patch.object(smtplib.SMTP, 'quit', return_value=None) as mock_quit:
        result = email_instance.sendEmail(to_list, subject, body)

        mock_config_smtp.assert_called_once()
        assert result['success'] is True
        assert result['msg'] == 'Email enviado com sucesso!'


def test_send_email_failure(email_instance):
    to_list = ['test@example.com']
    subject = 'Test Subject'
    body = 'Test Body'

    with patch.object(email_instance, '_configura_servidor_smtp',
                      side_effect=Exception('SMTP error')) as mock_config_smtp:
        result = email_instance.sendEmail(to_list, subject, body)
        mock_config_smtp.assert_called_once()
        assert result['success'] is False
        assert 'Erro ao enviar e-mail' in result['msg']


def test_send_email_with_attachment(email_instance):
    to_list = ['test@example.com']
    subject = 'Test Subject'
    body = 'Test Body'
    attachments = [('/path/to/file', 'file.txt')]

    # Mock open to simulate opening a file
    with patch.object(email_instance, '_configura_servidor_smtp', return_value=MagicMock()) as mock_config_smtp, \
            patch.object(smtplib.SMTP, 'sendmail', return_value=None) as mock_sendmail, \
            patch.object(smtplib.SMTP, 'quit', return_value=None) as mock_quit, \
            patch('builtins.open', mock_open(read_data=b'attachment_content')) as mock_open_file:
        result = email_instance.sendEmailAnexo(to_list, subject, body, attachments)

        mock_config_smtp.assert_called_once()

        assert result['success'] is True