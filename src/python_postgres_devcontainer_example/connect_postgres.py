import psycopg

def get_postgres_version() -> None:
    """Connect to PostgreSQL and get its version"""

    try:
        with psycopg.connect(
            dbname="postgres",
            user="postgres",
            password="postgres",
            host="db",
            port=5432
        ) as conn:
            
            print(conn)

            cur = conn.cursor()
            cur.execute("SELECT version();")
            version = cur.fetchone()

            print(f"Postgres Version: {version[0]}")

            cur.close()
            conn.close()

    except psycopg.OperationalError as err:
        print(f"Connection failed: {err}")
    
    return None

if __name__ == "__main__":
    get_postgres_version()