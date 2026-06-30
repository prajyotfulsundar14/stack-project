import os
import redis
import psycopg2
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Environment variables
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "db")
POSTGRES_DB = os.getenv("POSTGRES_DB", "Prajyot_db")
POSTGRES_USER = os.getenv("POSTGRES_USER", "Prajyot_user")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "Prajyot_pass")
REDIS_HOST = os.getenv("REDIS_HOST", "redis")

# Redis connection
redis_client = redis.Redis(host=REDIS_HOST, port=6379)

# Postgres connection
def get_db_connection():
    print("HOST:", POSTGRES_HOST)
    print("DB:", POSTGRES_DB)
    print("USER:", POSTGRES_USER)
    print("PASS:", POSTGRES_PASSWORD)
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        database=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD
    )
    return conn


def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS visits (
            id SERIAL PRIMARY KEY,
            visit_time TIMESTAMP NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()


@app.route("/")
def index():
    # Redis counter
    visits = redis_client.incr("visit_count")

    # Store visit in Postgres
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO visits (visit_time) VALUES (%s)",
        (datetime.now(),)
    )
    conn.commit()
    cur.close()
    conn.close()

    return render_template("index.html", visits=visits)


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)