from Classes.Email import Email
from Classes.SZChat import SZChat
import os

email = Email()
szChat = SZChat()
class sendEmail:
    def assinaturaContrato(self, destinatario, assunto, cliente, token):
        caminho_template = os.path.abspath('Templates/assinatura_contrato.html')
        with open(caminho_template, 'r', encoding='utf-8') as file:
            body = file.read()
            body = body.replace('{cliente}', cliente)
            body = body.replace('{token_assinatura}', token)

        # Envio de email HTML SEM anexo
        return email.sendEmailHTML(destinatario, assunto, body)

    def envioContrato(self, destinatario, assunto, cliente, anexo, nome_arquivo):
        # CONFIGURA TEMPLATE + CORPO EMAIL
        caminho_template = os.path.abspath('Templates/doc_contrato.html')
        with open(caminho_template, 'r', encoding='utf-8') as file:
            body = file.read()
            body = body.replace('{cliente}', cliente)

        # Envio de email HTML COM anexo
        return email.sendEmailAnexo(destinatario, assunto, body, [(anexo, nome_arquivo)])

class sendWhats:
    def avisoInstalacao(self, contato, cliente, periodo):
        return szChat.startSending(contato, 'instalacao', cliente, periodo)

    def assinaturaContrato(self, contato, cliente, link_contrato):
        return szChat.startSending(contato, 'assinatura', cliente, link_contrato)

    def assinaturaContrato2(self, contato, cliente, link_contrato):
        return szChat.startSending(contato, 'assinatura2', cliente, link_contrato)

    def pesquisaSuporte(self, contato, cliente):
        return szChat.startSending(contato, 'nps_suporte', cliente)

    def pesquisaInstalacao(self, contato, cliente):
        return szChat.startSending(contato, 'nps_suporte', cliente)

    def pesquisaRelacional(self, contato, cliente):
        return szChat.startSending(contato, 'nps_pes', cliente)

    def avaliacaoNegativa(self, contato, cliente):
        return szChat.startSending(contato, 'nps_pos', cliente)
