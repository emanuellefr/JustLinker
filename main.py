from Classes.sendMessages import sendEmail, sendWhats
from Classes.Validation import ClientValidator

send_email = sendEmail()
send_whats = sendWhats()
client_validator = ClientValidator()


# variaveis básicas para teste
destinatario = ['manu.frf2@gmail.com']
assunto = 'Confirmamos o recebimento do aceite digital - JustWeb'
nome_arquivo = 'teste.png'
nome_cliente = 'Cliente Teste'
token_assinatura = 'a78756dc87cdc6ec3ceb81b9b25bae974c54efb09d144c7c45150b6a5122513d'
telefone = 5531991105365
tipo_msg = 'instalacao'
periodo = 'manhã'
link_assinatura = f"https://teste.justweb.com/{token_assinatura}"


#email_assinatatura_contrato = send_email.assinaturaContrato(destinatario, assunto, nome_cliente, token_assinatura, 4654)

#envio_contrato = send_email.envioContrato(destinatario, assunto, nome_cliente, token_assinatura, 98765)

#aviso_instalacao = send_whats.avisoInstalacao(telefone, nome_cliente, 'Manha', 16546)

#assinatura_contrato2 = send_whats.assinaturaContrato2(telefone, nome_cliente, link_assinatura, 165494)

# pesquisa_suporte = send_whats.pesquisaSuporte(telefone, nome_cliente, 95464)
#
# pesquisa_instalacao = send_whats.pesquisaInstalacao(telefone, nome_cliente, 684654)
#
#pesquisa_relacional = send_whats.pesquisaRelacional(telefone, nome_cliente, 974197)

#avaliacao_negativa = send_whats.avaliacaoNegativa(telefone, nome_cliente, 123456)

envia_boleto_sem_bloq = send_whats.enviaBoletoSemBloqueio(telefone, nome_cliente, 6546)
