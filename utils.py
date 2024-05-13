import os
from dotenv import load_dotenv

load_dotenv('./.env')

#Credenciais do banco MYSQL
USER_MYSQL = os.getenv("USER_MYSQL")
HOST_MYSQL = os.getenv("HOST_MYSQL")
PASSWORD_MYSQL = os.getenv("PASSWORD_MYSQL")
DATABASE_MYSQL = os.getenv("DATABASE_MYSQL")

#Credenciais do banco PostgreSQL
USER_PGSQL = os.getenv("USER_PGSQL")
HOST_PGSQL = os.getenv("HOST_PGSQL")
PASSWORD_PGSQL = os.getenv("PASSWORD_PGSQL")
DATABASE_PGSQL = os.getenv("DATABASE_PGSQL")

#Configuração SMTP para envio de email
SMTP_HOST = os.getenv("HOST_SMTP")
SMTP_PORT = os.getenv("PORT_SMTP")
SMTP_USER = os.getenv("USER_SMTP")
SMTP_PASS = os.getenv("PASS_SMTP")

#url, login e senha da API do SZChat
BASE_URL_SZCHAT = os.getenv("BASE_URL_SZCHAT")
LOGIN_SZCHAT = os.getenv("LOGIN_SZCHAT")
SENHA_SZCHAT = os.getenv("PASSWORD_SZCHAT")
