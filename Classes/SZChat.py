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

    def _send_message(self, contato, tipo_msg, var1, var2=None):
        padrao_mensagens = {'avisoInstalacao': 'aviso_instalacao',
                            'assinaturaContrato': 'contrato_assinatura_modelo1',
                            'assinaturaContrato2': 'contrato_assinatura_modelo2',
                            'pesquisaSuporte': 'v3_nps_suporte',
                            'pesquisaInstalacao': 'v3_nps_instalacao',
                            'pesquisaRelacional': 'v3_pes_nps',
                            'avaliacaoNegativa': 'v4_pos_nps'
                            }
        template = padrao_mensagens.get(tipo_msg)
        if not template:
            raise ValueError("Tipo de mensagem inválido")
        if var2:
            variaveis = [var1, var2]
        else:
            variaveis = [var1]

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
                  'hsm_placeholders[]': [var1, var2]}
        response = requests.get(url, params=params)
        if response.ok:
            data = response.json()
            return {'success': True, 'msg': f"{data['message']}", 'tipo': 'whatsapp', 'metodo': tipo_msg}
        else:
            return {'success': False, 'msg': f'Erro ao enviar whatsapp: {response.raise_for_status()}',
                    'tipo': 'whatsapp', 'metodo': tipo_msg}

    def startSending(self, contato, tipo_msg, variavel1, variavel2=None):
        try:
            if not self.session_token:
                self._login()
            if not self.auth_token:
                self._get_auth_token()
            return self._send_message(contato, tipo_msg, variavel1, variavel2)

        finally:
            self._logout()

