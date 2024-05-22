import pandas as pd
from .Connect import Conexao
from loguru import logger
from datetime import datetime

class Log:
    def __init__(self):
        self.conexao_BD = Conexao()
        self.cnx_PG = self.conexao_BD.conexao_PGSQL()

    def new_log(self, retorno, os=None, contrato=None):
        if retorno['success']:
            retorno['os'] = os
            retorno['contrato'] = contrato
            retorno['id_log'] = self._save_to_db(retorno)
            logger.success(retorno)

        else:
            retorno['id_log'] = self._save_to_db(retorno)
            logger.error(retorno)

    def _save_to_db(self, dados):
        dados['data_criacao'] = datetime.now()

        if 'contrato' in dados and dados['contrato'] is not None:
            query = f'''SELECT id FROM logs_justlinker where contrato={dados['contrato']} and data_criacao='{dados['data_criacao']}' limit 1 '''
        elif 'os' in dados and dados['os'] is not None:
            query = f'''SELECT id FROM logs_justlinker where contrato={dados['os']} and data_criacao='{dados['data_criacao']}' limit 1 '''
        else:
            query = f'''SELECT id FROM logs_justlinker where data_criacao='{dados['data_criacao']}' and contrato is null and os is null limit 1 '''


        dados = pd.DataFrame([dados])
        dados.to_sql('logs_justlinker', schema='public', con=self.cnx_PG, if_exists='append', method='multi',
                     index=False)

        #BUSCA ID_LOG
        return pd.read_sql(query, self.cnx_PG).iloc[0][0]

