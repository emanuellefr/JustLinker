from utils import BASE_URL_SZCHAT, LOGIN_SZCHAT, SENHA_SZCHAT
import requests


class SZChat:
    def __init__(self):
        self.BASE_URL_SZCHAT = BASE_URL_SZCHAT
        self.LOGIN_SZCHAT = LOGIN_SZCHAT
        self.SENHA_SZCHAT = SENHA_SZCHAT
        self.session_token = None
        self.auth_token = None

    def _login(self):
        url = self.BASE_URL_SZCHAT + '/auth/login'
        params = {'email': self.LOGIN_SZCHAT, 'password': self.SENHA_SZCHAT}
        response = requests.post(url, params=params)
        if response.ok:
            data = response.json()
            self.token = data['token']
            self.params_token_login = {'token': self.token}
            self.session_token = data['user']['session_token']
            return True
        else:
            response.raise_for_status()

    def _logout(self):
        url = self.BASE_URL_SZCHAT + '/auth/logout'
        response = requests.get(url, params=self.params_token_login)
        if response.ok:
            return True
        else:
            response.raise_for_status()

    def _get_auth_token(self):
        url = self.BASE_URL_SZCHAT + '/auth/me'
        response = requests.get(url, params=self.params_token_login)
        if response.ok:
            data = response.json()
            self.auth_token = data['auth_token']
            return True
        else:
            response.raise_for_status()

    def _send_message(self, contato, tipo_msg, nome_cliente, periodo):
        padrao_mensagens = {'instalacao': 'aviso_instalacao', 'reparo': 'aviso_reparo'}
        template = padrao_mensagens.get(tipo_msg)
        if not template:
            raise ValueError("Tipo de mensagem inválido")

        url = self.BASE_URL_SZCHAT + '/message/send'
        params = {'token': self.auth_token,
                  'agent': 'conexaoapi@justweb.com.br',
                  'channel_id': '62e339084aa3e700160970bb',
                  'attendance_id': '62dfda9f6dddfe2294453b13',
                  'is_hsm': '1',
                  'hsm_template_name': template,
                  'platform_id': contato,
                  'type': 'text',
                  'close_session': '0',
                  'hsm_placeholders[]': [nome_cliente, periodo]}
        response = requests.get(url, params=params)
        if response.ok:
            data = response.json()
            return data['message']
        else:
            response.raise_for_status()

    def startSending(self, contato, tipo_msg, nome_cliente, periodo):
        try:
            if not self.session_token:
                self._login()
            if not self.auth_token:
                self._get_auth_token()
            return self._send_message(contato, tipo_msg, nome_cliente, periodo)
        finally:
            self._logout()
