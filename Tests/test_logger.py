import pytest
from unittest.mock import MagicMock, patch
from Classes.Logger import Log

@pytest.fixture
def mock_db_connection():
    mock_engine = MagicMock()
    return mock_engine

@pytest.fixture
def log_instance(mock_db_connection):
    with patch('Classes.Connect.Conexao.conexao_PGSQL', return_value=mock_db_connection):
        return Log()

def test_new_log_success(log_instance, mock_db_connection):
    retorno = {'success': True, 'message': 'Test success'}
    os = 12345
    contrato = 'ABC-123'

    with patch('Classes.Logger.logger.success') as mock_logger_success, patch.object(log_instance, '_save_to_db', wraps=log_instance._save_to_db) as mock_save_to_db:
        log_instance.new_log(retorno, os, contrato)
        mock_logger_success.assert_called_once_with(retorno)
        mock_save_to_db.assert_called_once_with(retorno)
        dados_salvos = mock_save_to_db.call_args[0][0]

        assert dados_salvos['os'] == os
        assert dados_salvos['contrato'] == contrato

def test_new_log_failure(log_instance, mock_db_connection):
    retorno = {'success': False, 'message': 'Test failure'}
    with patch('Classes.Logger.logger.error') as mock_logger_error, patch.object(log_instance, '_save_to_db', wraps=log_instance._save_to_db) as mock_save_to_db:
        log_instance.new_log(retorno)
        mock_logger_error.assert_called_once_with(retorno)
        mock_save_to_db.assert_called_once_with(retorno)
        dados_salvos = mock_save_to_db.call_args[0][0]
        
        assert dados_salvos['message'] == 'Test failure'
