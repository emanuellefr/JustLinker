from Classes.Connect import Conexao
import pytest
from sqlalchemy.exc import OperationalError


@pytest.fixture
def db_engine():
    conn = Conexao()
    return conn.conexao_PGSQL()

def test_db_connection(db_engine):
    with db_engine.connect() as connection:
        result = connection.execute("SELECT 1")
        assert result.fetchone()[0] == 1
