import pandas as pd
import Classes.Connect as Connect
from loguru import logger
from datetime import datetime

conexao_BD = Connect.Conexao()
cnx_PG = conexao_BD.conexao_PGSQL()
cursor_PG = cnx_PG.connect()

class Log:
    def new_log(self, retorno):
        if retorno['success']:
            logger.success(retorno)
            self._save_to_db(retorno)

        else:
            logger.error(retorno)
            self._save_to_db(retorno)

    def _save_to_db(self, dados):
        dados['data_criacao'] = datetime.now()
        dados = pd.DataFrame([dados])
        dados.to_sql('logs_justlinker', schema='public', con=cnx_PG, if_exists='append', method='multi',
                     index=False)
