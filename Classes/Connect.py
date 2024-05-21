from sqlalchemy import create_engine
from .utils import USER_PGSQL, HOST_PGSQL, PASSWORD_PGSQL, DATABASE_PGSQL


class Conexao:
    """ Classe que realiza conexao com os bancos de dados MYSQL e PGSQL utilixando o sqlalchmy
        Link da documentação SQLAlchemy: https://docs.sqlalchemy.org/en/14/core/engines.html"""

    def __init__(self):
        self.__USER_PGSQL = USER_PGSQL
        self.__HOST_PGSQL = HOST_PGSQL
        self.__PASSWORD_PGSQL = PASSWORD_PGSQL
        self.__DATABASE_PGSQL = DATABASE_PGSQL


    def conexao_PGSQL(self):
        url = "postgresql+psycopg2://"+str(self.__USER_PGSQL)+":"+str(self.__PASSWORD_PGSQL)+"@"+str(self.__HOST_PGSQL)+"/"+str(self.__DATABASE_PGSQL)
        return create_engine(url)

