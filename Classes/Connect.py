from urllib.parse import quote_plus
from sqlalchemy import create_engine
from utils import (USER_PGSQL, HOST_PGSQL, PASSWORD_PGSQL, DATABASE_PGSQL, USER_MYSQL, HOST_MYSQL, PASSWORD_MYSQL,
                   DATABASE_MYSQL, USER_PGSQL_DOCKER, HOST_PGSQL_DOCKER, PASSWORD_PGSQL_DOCKER, DATABASE_PGSQL_DOCKER)

class Conexao:
    """ Classe que realiza conexao com os bancos de dados MYSQL e PGSQL utilixando o sqlalchmy
        Link da documentação SQLAlchemy: https://docs.sqlalchemy.org/en/14/core/engines.html"""

    def __init__(self):
        self.__USER_PGSQL = USER_PGSQL
        self.__HOST_PGSQL = HOST_PGSQL
        self.__PASSWORD_PGSQL = PASSWORD_PGSQL
        self.__DATABASE_PGSQL = DATABASE_PGSQL
        self.__USER_MYSQL = USER_MYSQL
        self.__HOST_MYSQL = HOST_MYSQL
        self.__PASSWORD_MYSQL = PASSWORD_MYSQL
        self.__DATABASE_MYSQL = DATABASE_MYSQL
        self.__USER_PGSQL_DOCKER = USER_PGSQL_DOCKER
        self.__HOST_PGSQL_DOCKER = HOST_PGSQL_DOCKER
        self.__PASSWORD_PGSQL_DOCKER = PASSWORD_PGSQL_DOCKER
        self.__DATABASE_PGSQL_DOCKER = DATABASE_PGSQL_DOCKER

    def conexao_MySQL(self):
        url = "mysql+pymysql://"+str(self.__USER_MYSQL)+":"+'%s@' % quote_plus(str(self.__PASSWORD_MYSQL)) +str(self.__HOST_MYSQL)+"/"+str(self.__DATABASE_MYSQL)+"?charset=utf8mb4"
        return create_engine(url)

    def conexao_PGSQL(self):
        url = "postgresql+psycopg2://"+str(self.__USER_PGSQL)+":"+str(self.__PASSWORD_PGSQL)+"@"+str(self.__HOST_PGSQL)+"/"+str(self.__DATABASE_PGSQL)
        return create_engine(url)

    def conexao_PGSQL_DOCKER(self):
        url = "postgresql+psycopg2://"+str(self.__USER_PGSQL_DOCKER)+":"+str(self.__PASSWORD_PGSQL_DOCKER)+"@"+str(self.__HOST_PGSQL_DOCKER)+"/"+str(self.__DATABASE_PGSQL_DOCKER)
        return create_engine(url)

