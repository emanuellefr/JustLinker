import Classes.Connect as Connect


class ClientValidator:
    def __init__(self):
        self.conexao_BD = Connect.Conexao()
        self.cnx_PG = self.conexao_BD.conexao_PGSQL()
        self.cursor_PG = self.cnx_PG.connect()

    def logs_exist_contrato(self, id_contrato, metodo):
        query = (f"SELECT COUNT(*) FROM logs_justlinker "
                 f"WHERE contrato = {id_contrato} and metodo='{metodo}' AND data_criacao > CURRENT_DATE;")

        result = self.cursor_PG.execute(query).fetchone()[0]

        if result == 0:
            return {'success': True}
        else:
            return {'success': False, 'msg': 'Duplicidade de requisição!', 'contrato': id_contrato, 'metodo': metodo}

    def logs_exist_os(self, id_os, metodo):
        query = (f"SELECT COUNT(*) FROM logs_justlinker "
                 f"WHERE os = {id_os} and metodo='{metodo}' AND data_criacao > CURRENT_DATE;")

        result = self.cursor_PG.execute(query).fetchone()[0]

        if result == 0:
            return {'success': True}
        else:
            return {'success': False, 'msg': 'Duplicidade de requisição!', 'os': id_os, 'metodo': metodo}

