import psycopg2


def edit_db():
    conn = psycopg2.connect(
        host="postgresql",
        port=5432,
        dbname="postgres",
        user="postgres",
        password="postgres",
    )
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS users (id serial PRIMARY KEY, name VARCHAR(50), password VARCHAR(50));"
    )
    conn.commit()
    cur.close()
    conn.close()
    return "OK"
