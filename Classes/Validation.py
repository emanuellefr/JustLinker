from .Connect import Conexao


class ClientValidator:
    def __init__(self):
        self.conexao_BD = Conexao()
        self.cnx_PG = self.conexao_BD.conexao_PGSQL()
        self.cursor_PG = self.cnx_PG.connect()

    def logs_exist_contrato(self, id_contrato, metodo, tipo):
        query = (f'''
        SELECT COUNT(*) FROM logs_justlinker
        WHERE contrato = {id_contrato}  
            and success is TRUE 
            and metodo='{metodo}' 
            and tipo='{tipo}' 
            AND data_criacao > CURRENT_DATE;''')

        result = self.cursor_PG.execute(query).fetchone()[0]

        if result == 0:
            return {'success': True}
        else:
            if metodo == 'assinaturaContrato':
                return {'success': True}
            else:
                return {'success': False, 'msg': 'Duplicidade de requisição!', 'contrato': id_contrato, 'metodo': metodo}

    def logs_exist_os(self, id_os, metodo, tipo):
        query = (f'''
        SELECT COUNT(*) 
        FROM logs_justlinker 
        WHERE os = {id_os}   
             and success is TRUE 
             and metodo='{metodo}' 
             and tipo='{tipo}' 
             AND data_criacao > CURRENT_DATE;''')

        result = self.cursor_PG.execute(query).fetchone()[0]

        if result == 0:
            return {'success': True}
        else:
            return {'success': False, 'msg': 'Duplicidade de requisição!', 'os': id_os, 'metodo': metodo}

