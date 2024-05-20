import os
from dotenv import load_dotenv


env_path = os.path.abspath('.env')
print(env_path)
load_dotenv(env_path)

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

#Credenciais do banco PostgreSQL DOCKER
USER_PGSQL_DOCKER=os.getenv("USER_PGSQL_DOCKER")
HOST_PGSQL_DOCKER=os.getenv("HOST_PGSQL_DOCKER")
PASSWORD_PGSQL_DOCKER=os.getenv("PASSWORD_PGSQL_DOCKER")
DATABASE_PGSQL_DOCKER=os.getenv("DATABASE_PGSQL_DOCKER")

#Configuração SMTP para envio de email
SMTP_HOST = os.getenv("HOST_SMTP")
SMTP_PORT = os.getenv("PORT_SMTP")
SMTP_USER = os.getenv("USER_SMTP")
SMTP_PASS = os.getenv("PASS_SMTP")

#url, login e senha da API do SZChat
BASE_URL_SZCHAT = os.getenv("BASE_URL_SZCHAT")
LOGIN_SZCHAT = os.getenv("LOGIN_SZCHAT")
SENHA_SZCHAT = os.getenv("PASSWORD_SZCHAT")
