import psycopg 
from pipeline.config import DbSettings
from pathlib import Path
from pipeline.extract import get_moedas

SQL_FILE = Path(__file__).parent.parent / "sql" / "01_moedas_tb.sql"


def get_connection(settings: DbSettings) -> psycopg.Connection:
    return psycopg.connect(settings.url)

def criar_tabela_moedas(conn) -> None:
    sql = SQL_FILE.read_text(encoding="utf-8")
    with conn.cursor() as cur:
        cur.execute(sql)
    conn.commit()
    print("Tabela 'moedas' criada com sucesso!")

def insert_moedas(conn, moedas: list[dict]) -> None:
    sql = """
    INSERT INTO moedas (simbolo, nome_moeda, tipo_moeda)
    VALUES (%(simbolo)s, %(nomeFormatado)s, %(tipoMoeda)s)
    """

    with conn.cursor() as cur:
        cur.executemany(sql, moedas)
    conn.commit()
    print("Moedas inseridas com sucesso!")

if __name__ == "__main__":
    settings = DbSettings()
    with get_connection(settings) as conn:
        criar_tabela_moedas(conn)
        
        moedas = get_moedas()
        insert_moedas(conn, moedas)