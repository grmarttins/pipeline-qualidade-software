import psycopg 
from pipeline.config import DbSettings


def get_connection(settings: DbSettings) -> psycopg.Connection:
    return psycopg.connect(settings.url)

def get_postgres_version(conn: psycopg.Connection) -> str:
    with conn.cursor() as cur:
        cur.execute("SELECT version();") 
        row = cur.fetchone()
    if row is None:
        raise RuntimeError(f"Versao nao encontrada")
    return row[0]

if __name__ == "__main__":
    settings = DbSettings()
    with get_connection(settings) as conn:
        version = get_postgres_version(conn)
        print(f"PostgreSQL Version: {version}")