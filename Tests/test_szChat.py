import pytest
from unittest.mock import patch, MagicMock
from Classes.SZChat import SZChat


@pytest.fixture
def szchat_instance():
    return SZChat()


@patch('Classes.SZChat.requests.post')
def test_login_success(mock_post, szchat_instance):
    mock_response = MagicMock()
    mock_response.ok = True
    mock_response.json.return_value = {'token': 'dummy_token', 'user': {'session_token': 'dummy_session_token'}}
    mock_post.return_value = mock_response

    szchat_instance._login()

    assert szchat_instance.session_token is not None
    assert szchat_instance.token is not None


@patch('Classes.SZChat.requests.post')
def test_login_failure(mock_post, szchat_instance):
    mock_response = MagicMock()
    mock_response.ok = False
    mock_response.raise_for_status.side_effect = Exception('Error')
    mock_post.return_value = mock_response

    with pytest.raises(Exception):
        szchat_instance._login()


@patch('Classes.SZChat.requests.get')
def test_logout_success(mock_get, szchat_instance):
    mock_response = MagicMock()
    mock_response.ok = True
    mock_get.return_value = mock_response

    szchat_instance.session_token = 'dummy_session_token'
    szchat_instance.params_token_login = {'token': 'dummy_token'}

    assert szchat_instance._logout() == True


@patch('Classes.SZChat.requests.get')
def test_get_auth_token(mock_get, szchat_instance):
    mock_response = MagicMock()
    mock_response.ok = True
    mock_get.return_value = mock_response

    szchat_instance.session_token = 'dummy_session_token'
    szchat_instance.params_token_login = {'token': 'dummy_token'}
    szchat_instance.auth_token = {'token': 'dummy_token'}

    assert szchat_instance._get_auth_token() is True


@patch('Classes.SZChat.requests.get')
def test_send_message_success(mock_get, szchat_instance):
    mock_response = MagicMock()
    mock_response.ok = True
    mock_response.json.return_value = {'message': 'Test message'}
    mock_get.return_value = mock_response

    szchat_instance.auth_token = 'dummy_auth_token'

    result = szchat_instance._send_message('dummy_contato', 'avisoInstalacao', 'dummy_var1', 'dummy_var2')

    assert result['success'] is True
    assert result['msg'] == 'Test message'
    assert result['tipo'] == 'whatsapp'
    assert result['metodo'] == 'avisoInstalacao'


@patch('Classes.SZChat.SZChat._login')
@patch('Classes.SZChat.SZChat._get_auth_token')
@patch('Classes.SZChat.SZChat._send_message')
def test_start_sending_success(mock_send_message, mock_get_auth_token, mock_login, szchat_instance):
    mock_send_message.return_value = {'success': True, 'msg': 'Test message', 'tipo': 'whatsapp', 'metodo': 'avisoInstalacao'}
    szchat_instance.session_token = 'dummy_session_token'
    szchat_instance.auth_token = 'dummy_auth_token'

    result = szchat_instance.startSending('dummy_contato', 'avisoInstalacao', 'dummy_var1', 'dummy_var2')

    mock_login.assert_not_called()
    mock_get_auth_token.assert_not_called()
    mock_send_message.assert_called_once_with('dummy_contato', 'avisoInstalacao', 'dummy_var1', 'dummy_var2')

    assert result == {'success': True, 'msg': 'Test message', 'tipo': 'whatsapp', 'metodo': 'avisoInstalacao'}


