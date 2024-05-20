import pandas as pd
import Classes.Connect as Connect
from loguru import logger
from datetime import datetime

class Log:
    def __init__(self):
        self.conexao_BD = Connect.Conexao()
        self.cnx_PG = self.conexao_BD.conexao_PGSQL()

    def new_log(self, retorno, os=None, contrato=None):
        if retorno['success']:
            retorno['os'] = os
            retorno['contrato'] = contrato
            logger.success(retorno)
            self._save_to_db(retorno)

        else:
            logger.error(retorno)
            self._save_to_db(retorno)

    def _save_to_db(self, dados):
        dados['data_criacao'] = datetime.now()
        dados = pd.DataFrame([dados])
        dados.to_sql('logs_justlinker', schema='public', con=self.cnx_PG, if_exists='append', method='multi',
                     index=False)
