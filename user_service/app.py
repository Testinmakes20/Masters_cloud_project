from fastapi import FastAPI, HTTPException
import psycopg2
import os

app = FastAPI()

DB_HOST = os.getenv("DB_HOST", "postgres-service")
DB_NAME = os.getenv("DB_NAME", "ecommerce")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "admin123")

def get_conn():
    return psycopg2.connect(host=DB_HOST, database=DB_NAME,
                            user=DB_USER, password=DB_PASSWORD)

@app.post("/users")
def create_user(user: dict):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id",
            (user["name"], user["email"])
        )
        user_id = cur.fetchone()[0]
        conn.commit()
        return {"id": user_id, **user}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()

@app.get("/users")
def list_users():
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id, name, email FROM users")
        rows = cur.fetchall()
        return [{"id": r[0], "name": r[1], "email": r[2]} for r in rows]
    finally:
        cur.close()
        conn.close()
