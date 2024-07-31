from .utils import BASE_URL_SZCHAT, LOGIN_SZCHAT, SENHA_SZCHAT
import requests
import traceback



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
        padrao_mensagens = {'avisoInstalacao': ['aviso_instalacao', '62e339084aa3e700160970bb'],
                            'assinaturaContrato': ['contrato_assinatura_modelo1', '62e338b331519200178d6d2b'],
                            'assinaturaContrato2': ['contrato_assinatura_modelo2', '62e338b331519200178d6d2b'],
                            'pesquisaSuporte': ['v3_nps_suporte', '62e339084aa3e700160970bb'],
                            'pesquisaInstalacao': ['v3_nps_instalacao', '62e339084aa3e700160970bb'],
                            'pesquisaRelacional': ['v3_pes_nps', '62e339084aa3e700160970bb'],
                            'avaliacaoNegativa': ['v4_pos_nps', '62e338b331519200178d6d2b'],
                            'enviaBoletoSemBloqueio': ['en_boleto_sem_bloqueio', '62e338b331519200178d6d2b']
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
                  'channel_id': template[1],
                  'attendance_id': '665f181a1be2c44bbc0c6770',
                  'is_hsm': '1',
                  'hsm_template_name': template[0],
                  'platform_id': contato,
                  'type': 'text',
                  'close_session': 3,
                  'hsm_placeholders[]': variaveis}
        response = requests.get(url, params=params)
        if response.ok:
            data = response.json()
            return {'success': True, 'msg': f"{data['message']}", 'tipo': 'whatsapp', 'metodo': tipo_msg}
        else:
            return {'success': False, 'msg': f'Erro ao enviar whatsapp: {response.text}',
                    'tipo': 'whatsapp', 'metodo': tipo_msg}

    def startSending(self, contato, tipo_msg, variavel1, variavel2=None):
        try:
            if not self.session_token:
                self._login()
            if not self.auth_token:
                self._get_auth_token()
            return self._send_message(contato, tipo_msg, variavel1, variavel2)

        except Exception as err:
            erro = (
                f"Tipo de exceção: {type(err).__name__}\n"
                f"Mensagem de erro: {str(err)}\n"
                f"Traceback completo:\n{traceback.format_exc()}"
            )
            return erro

