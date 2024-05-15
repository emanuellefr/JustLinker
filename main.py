from Classes.sendMessages import sendEmail, sendWhats
from Classes.Validation import ClientValidator

send_email = sendEmail()
send_whats = sendWhats()
client_validator = ClientValidator()


# variaveis básicas para teste
destinatario = ['manu.frf2@gmail.com']
assunto = 'Teste de email envio html COM anexo'
anexo = "C:/Users/ThinkPad E490/Downloads/27b7591a770227556f1f23d376d98800878b665b70b0795cf5c211c6b4114885.pdf"
nome_arquivo = 'teste.png'
nome_cliente = 'Manu'
token_assinatura = '46fa4sd6f4asdfa'
telefone = 5531991105365
tipo_msg = 'instalacao'
periodo = 'manhã'
link_assinatura = f"https://teste.justweb.com/{token_assinatura}"

#
# email_assinatatura_contrato = send_email.assinaturaContrato(destinatario, assunto, nome_cliente, token_assinatura, 1123456)
#
# envio_contrato = send_email.envioContrato(destinatario, assunto, nome_cliente, anexo, nome_arquivo, 4651464)
#
# aviso_instalacao = send_whats.avisoInstalacao(telefone, nome_cliente, 'Manha', 651114621)
#
# assinatura_contrato = send_whats.assinaturaContrato(telefone, nome_cliente, link_assinatura, 465429317)

assinatura_contrato2 = send_whats.assinaturaContrato2(telefone, nome_cliente, link_assinatura, 78111945)
#
# pesquisa_suporte = send_whats.pesquisaSuporte(telefone, nome_cliente, 12356174)
#
# pesquisa_instalacao = send_whats.pesquisaInstalacao(telefone, nome_cliente, 741212)
#
# pesquisa_relacional = send_whats.pesquisaRelacional(telefone, nome_cliente, 4697197)
#
# avaliacao_negativa = send_whats.avaliacaoNegativa(telefone, nome_cliente, 65417987)
