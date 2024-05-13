from Classes.sendMessages import sendEmail, sendWhats

send_email = sendEmail()
send_whats = sendWhats()

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


#Email assinatura de contrato
email_assinatatura_contrato = send_email.assinaturaContrato(destinatario, assunto, nome_cliente, token_assinatura)
print(email_assinatatura_contrato)

#Email envio de contrato
envio_contrato = send_email.envioContrato(destinatario, assunto, nome_cliente, anexo, nome_arquivo)
print(envio_contrato)

#SZChat aviso instalacao
aviso_instalacao = send_whats.avisoInstalacao(telefone, nome_cliente, periodo)
print(aviso_instalacao)


