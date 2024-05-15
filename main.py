from Classes.sendMessages import sendEmail, sendWhats
from Classes.Validation import ClientValidator

send_email = sendEmail()
send_whats = sendWhats()
client_validator = ClientValidator()


# variaveis básicas para teste
destinatario = ['manu.frf2@gmail.com']
assunto = 'Teste de email envio html COM anexo'
anexo = "C:/Users/ThinkPad E490/Pictures/Screenshots/teste.png"
nome_arquivo = 'teste.png'
nome_cliente = 'Manu Ferreira'
token_assinatura = '46fa4sd6f4asdfa'
telefone = 5531991105365
tipo_msg = 'instalacao'
periodo = 'manhã'
link_assinatura = f'http:justweb.teste.linkassinatura/{token_assinatura}'


#Email assinatura de contrato
email_assinatatura_contrato = send_email.assinaturaContrato(destinatario, assunto, nome_cliente, token_assinatura, 123456)

# #Email envio de contrato
# envio_contrato = send_email.envioContrato(destinatario, assunto, nome_cliente, anexo, nome_arquivo, 465464)

# #SZChat aviso instalacao
# pesquisa_suporte = send_whats.pesquisaSuporte(telefone, nome_cliente)

# #SZChat assinatura contrato
# assinatura_contrato = send_whats.assinaturaContrato(telefone, nome_cliente, link_assinatura)

#SZChat assinatura contrato2
# assinatura_contrato2 = send_whats.assinaturaContrato2(telefone, nome_cliente, link_assinatura)



# #SZChat pesquisa suporte
pesquisa_suporte = send_whats.pesquisaSuporte(telefone, nome_cliente, 12356)


# #SZChat pesquisa instalacao
# pesquisa_instalacao = send_whats.pesquisaInstalacao(telefone, nome_cliente)

# #SZChat pesquisa relacional
# pesquisa_relacional = send_whats.pesquisaRelacional(telefone, nome_cliente)

# #SZChat pesquisa negativa
# avaliacao_negativa = send_whats.avaliacaoNegativa(telefone, nome_cliente)
