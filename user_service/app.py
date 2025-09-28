from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

DB_HOST = os.getenv("DB_HOST", "postgres")
DB_NAME = os.getenv("DB_NAME", "ecommerce")
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")

def get_conn():
    return psycopg2.connect(host=DB_HOST, database=DB_NAME,
                            user=DB_USER, password=DB_PASSWORD)

@app.post("/products")
def create_product(product: dict):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO products (name, price, stock) VALUES (%s, %s, %s) RETURNING id",
        (product["name"], product["price"], product["stock"])
    )
    product_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return {"id": product_id, **product}

@app.get("/products")
def list_products():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name, price, stock FROM products")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": r[0], "name": r[1], "price": r[2], "stock": r[3]} for r in rows]
