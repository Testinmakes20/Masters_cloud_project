from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

# Database connection settings
DB_HOST = os.getenv("DB_HOST", "postgres")
DB_NAME = os.getenv("DB_NAME", "ecommerce")
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")

def get_conn():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

@app.get("/products")
def list_products():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name, price, stock FROM products")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [
        {"id": r[0], "name": r[1], "price": float(r[2]), "stock": r[3]}
        for r in rows
    ]

@app.get("/products/{product_id}")
def get_product(product_id: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name, price, stock FROM products WHERE id = %s", (product_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row:
        return {"id": row[0], "name": row[1], "price": float(row[2]), "stock": row[3]}
    return {"error": "Product not found"}
