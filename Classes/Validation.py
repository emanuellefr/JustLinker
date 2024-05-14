import Classes.Connect as Connect


class ClientValidator:
    def __init__(self):
        self.conexao_BD = Connect.Conexao()
        self.cnx_PG = self.conexao_BD.conexao_PGSQL()
        self.cursor_PG = self.cnx_PG.connect()

    def logs_exist_contrato(self, id_contrato):
        query = f"SELECT COUNT(*) FROM client_table WHERE client = '{id_contrato}'"

        with self.cnx_PG.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()[0]

        return result == 0

    def logs_exist_os(self, id_os, metodo):
        query = (f"SELECT COUNT(*) FROM logs_justlinker "
                 f"WHERE os = {id_os} and metodo='{metodo}' AND data_criacao > CURRENT_DATE;")

        result = self.cursor_PG.execute(query).fetchone()[0]

        if result == 0:
            return {'success': True}
        else:
            return {'success': False, 'msg': 'Duplicidade de requisição!', 'os': id_os, 'metodo': metodo}

