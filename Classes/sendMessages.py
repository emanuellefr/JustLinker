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
    def assinaturaContrato(self, destinatario, assunto, cliente, token):
        caminho_template = os.path.abspath('Templates/assinatura_contrato.html')
        with open(caminho_template, 'r', encoding='utf-8') as file:
            body = file.read()
            body = body.replace('{cliente}', cliente)
            body = body.replace('{token_assinatura}', token)
        # Envio de email HTML SEM anexo
        assina_contrato = email.sendEmailHTML(destinatario, assunto, body)
        assina_contrato['metodo'] = inspect.currentframe().f_code.co_name
        log.new_log(assina_contrato)
        return assina_contrato

    def envioContrato(self, destinatario, assunto, cliente, anexo, nome_arquivo):
        # CONFIGURA TEMPLATE + CORPO EMAIL
        caminho_template = os.path.abspath('Templates/doc_contrato.html')
        with open(caminho_template, 'r', encoding='utf-8') as file:
            body = file.read()
            body = body.replace('{cliente}', cliente)
        # Envio de email HTML COM anexo
        envio_contrato = email.sendEmailAnexo(destinatario, assunto, body, [(anexo, nome_arquivo)])
        envio_contrato['metodo'] = inspect.currentframe().f_code.co_name
        log.new_log(envio_contrato)
        return envio_contrato


class sendWhats:
    def __init__(self):
        self.client_validator = ClientValidator()

    def avisoInstalacao(self, contato, cliente, periodo):
        aviso_instalacao = szChat.startSending(contato, 'avisoInstalacao', cliente, periodo)
        log.new_log(aviso_instalacao)
        return aviso_instalacao

    def assinaturaContrato(self, contato, cliente, link_contrato):
        assinatura_contrato = szChat.startSending(contato, 'assinaturaContrato', cliente, link_contrato)
        log.new_log(assinatura_contrato)
        return assinatura_contrato

    def assinaturaContrato2(self, contato, cliente, link_contrato):
        assinatura_contrato2 = szChat.startSending(contato, 'assinaturaContrato2', cliente, link_contrato)
        log.new_log(assinatura_contrato2)
        return assinatura_contrato2

    def pesquisaSuporte(self, contato, cliente, id_os):
        validator = self.client_validator.logs_exist_os(id_os, 'pesquisaSuporte')
        if validator['success']:
            pesquisa_suporte = szChat.startSending(contato, 'pesquisaSuporte', cliente)
            pesquisa_suporte['os'] = id_os
            log.new_log(pesquisa_suporte)
            return pesquisa_suporte
        else:
            log.new_log(validator)
            return False


    def pesquisaInstalacao(self, contato, cliente):
        pesquisa_instalacao = szChat.startSending(contato, 'pesquisaInstalacao', cliente)
        log.new_log(pesquisa_instalacao)
        return pesquisa_instalacao

    def pesquisaRelacional(self, contato, cliente):
        pesquisa_relacional = szChat.startSending(contato, 'pesquisaRelacional', cliente)
        log.new_log(pesquisa_relacional)
        return pesquisa_relacional

    def avaliacaoNegativa(self, contato, cliente):
        avaliacao_negativa = szChat.startSending(contato, 'avaliacaoNegativa', cliente)
        log.new_log(avaliacao_negativa)
        return avaliacao_negativa
