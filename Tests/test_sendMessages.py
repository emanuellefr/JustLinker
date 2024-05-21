import pytest
from unittest.mock import patch, mock_open
from Classes.sendMessages import sendEmail


@pytest.fixture
def mock_email():
    with patch('Classes.sendMessages.Email') as MockEmail:
        yield MockEmail()


@pytest.fixture
def mock_log():
    with patch('Classes.sendMessages.Log') as MockLog:
        yield MockLog()


@pytest.fixture
def mock_client_validator():
    with patch('Classes.sendMessages.ClientValidator') as MockClientValidator:
        yield MockClientValidator()


def test_assinaturaContrato(mock_email, mock_log, mock_client_validator):
    # Instancie a classe sendEmail
    email_instance = sendEmail()

    # Configure os mocks necessários
    email_service = mock_email.return_value
    log_instance = mock_log.return_value

    # Configura o retorno do método logs_exist_contrato
    mock_client_validator.return_value.logs_exist_contrato.return_value = {'success': True}

    # Configura o retorno do método sendEmailHTML
    email_service.sendEmailHTML.return_value = {'status': 'success'}

    # Chama o método que você quer testar
    result = email_instance.assinaturaContrato('destinatario@example.com', 'Assunto', 'Cliente', 'token123', 'contrato123')

    # Verifica se o resultado está correto
    assert result['success'] is True
