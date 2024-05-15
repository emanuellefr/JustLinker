from Classes.Email import Email
from Classes.SZChat import SZChat
from Classes.Logger import Log
from Classes.Validation import ClientValidator
import inspect
import os

email = Email()
szChat = SZChat()
log = Log()


class sendEmail:
    def __init__(self):
        self.client_validator = ClientValidator()

    def assinaturaContrato(self, destinatario, assunto, cliente, token, contrato_id):
        validator = self.client_validator.logs_exist_contrato(contrato_id, 'assinaturaContrato')
        if validator['success']:
            caminho_template = os.path.abspath('Templates/assinatura_contrato.html')
            with open(caminho_template, 'r', encoding='utf-8') as file:
                body = file.read()
                body = body.replace('{cliente}', cliente)
                body = body.replace('{token_assinatura}', token)
            # Envio de email HTML SEM anexo
            assina_contrato = email.sendEmailHTML(destinatario, assunto, body)
            assina_contrato['metodo'] = inspect.currentframe().f_code.co_name
            log.new_log(assina_contrato, contrato=contrato_id)
            return assina_contrato
        else:
            validator['tipo'] = 'email'
            log.new_log(validator)
            return False


    def envioContrato(self, destinatario, assunto, cliente, anexo, nome_arquivo, contrato_id):
        validator = self.client_validator.logs_exist_contrato(contrato_id, 'envioContrato')
        if validator['success']:
            # CONFIGURA TEMPLATE + CORPO EMAIL
            caminho_template = os.path.abspath('Templates/doc_contrato.html')
            with open(caminho_template, 'r', encoding='utf-8') as file:
                body = file.read()
                body = body.replace('{cliente}', cliente)
            # Envio de email HTML COM anexo
            envio_contrato = email.sendEmailAnexo(destinatario, assunto, body, [(anexo, nome_arquivo)])
            envio_contrato['metodo'] = inspect.currentframe().f_code.co_name
            log.new_log(envio_contrato, contrato=contrato_id)
            return envio_contrato
        else:
            validator['tipo'] = 'email'
            log.new_log(validator)
            return False


class sendWhats:
    def __init__(self):
        self.client_validator = ClientValidator()

    def avisoInstalacao(self, contato, cliente, periodo, id_os):
        validator = self.client_validator.logs_exist_os(id_os, 'avisoInstalacao')
        if validator['success']:
            aviso_instalacao = szChat.startSending(contato, 'avisoInstalacao', cliente, periodo)
            log.new_log(aviso_instalacao, os=id_os)
            return aviso_instalacao
        else:
            validator['tipo'] = 'whatsapp'
            log.new_log(validator)
            return False

    def assinaturaContrato(self, contato, cliente, link_contrato, contrato_id):
        validator = self.client_validator.logs_exist_contrato(contrato_id, 'assinaturaContrato')
        if validator['success']:
            assinatura_contrato = szChat.startSending(contato, 'assinaturaContrato', cliente, link_contrato)
            log.new_log(assinatura_contrato, contrato=contrato_id)
            return assinatura_contrato
        else:
            validator['tipo'] = 'whatsapp'
            log.new_log(validator)
            return False

    def assinaturaContrato2(self, contato, cliente, link_contrato, contrato_id):
        validator = self.client_validator.logs_exist_contrato(contrato_id, 'assinaturaContrato2')
        if validator['success']:
            assinatura_contrato2 = szChat.startSending(contato, 'assinaturaContrato2', cliente, link_contrato)
            log.new_log(assinatura_contrato2, contrato=contrato_id)
            return assinatura_contrato2
        else:
            validator['tipo'] = 'whatsapp'
            log.new_log(validator)
            return False

    def pesquisaSuporte(self, contato, cliente, id_os):
        validator = self.client_validator.logs_exist_os(id_os, 'pesquisaSuporte')
        if validator['success']:
            pesquisa_suporte = szChat.startSending(contato, 'pesquisaSuporte', cliente)
            pesquisa_suporte['tipo'] = 'whatsapp'
            log.new_log(pesquisa_suporte, os=id_os)
            return pesquisa_suporte
        else:
            validator['tipo'] = 'whatsapp'
            log.new_log(validator)
            return False


    def pesquisaInstalacao(self, contato, cliente, id_os):
        validator = self.client_validator.logs_exist_os(id_os, 'pesquisaInstalacao')
        if validator['success']:
            pesquisa_instalacao = szChat.startSending(contato, 'pesquisaInstalacao', cliente)
            log.new_log(pesquisa_instalacao, os=id_os)
            return pesquisa_instalacao
        else:
            validator['tipo'] = 'whatsapp'
            log.new_log(validator)
            return False

    def pesquisaRelacional(self, contato, cliente, id_contrato):
        validator = self.client_validator.logs_exist_contrato(id_contrato, 'pesquisaRelacional')
        if validator['success']:
            pesquisa_relacional = szChat.startSending(contato, 'pesquisaRelacional', cliente)
            log.new_log(pesquisa_relacional, contrato=id_contrato)
            return pesquisa_relacional
        else:
            validator['tipo'] = 'whatsapp'
            log.new_log(validator)
            return False

    def avaliacaoNegativa(self, contato, cliente, id_contrato):
        validator = self.client_validator.logs_exist_contrato(id_contrato, 'avaliacaoNegativa')
        if validator['success']:
            avaliacao_negativa = szChat.startSending(contato, 'avaliacaoNegativa', cliente)
            log.new_log(avaliacao_negativa, contrato=id_contrato)
            return avaliacao_negativa
        else:
            validator['tipo'] = 'whatsapp'
            log.new_log(validator)
            return False
