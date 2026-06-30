# Stack Project - Python Flask Web App

A simple and aesthetic web app built with *Python Flask, connected to **PostgreSQL* as the database and *Redis* as a cache.  
The app displays a “Hello Prajyot Fulsundar” message and interacts with the database.

---

## 1️⃣ Project Description

This project demonstrates:

- A Python Flask web application (app.py)
- Connection to a PostgreSQL database (Prajyot_db)  
- Connection to a Redis cache for fast data retrieval  
- Modular structure for easy Dockerization and CI/CD deployment  

This project is perfect for learning *Docker, Docker Compose, and DevOps pipelines*.

---

## 2️⃣ Prerequisites

Before running the app locally, make sure you have:

- Python 3.11+ installed  
- pip installed  
- PostgreSQL installed or running in a container  
- Redis installed or running in a container  
- Git (optional, for version control)  

---

## 3️⃣ Setup Python Environment

1. Create a virtual environment:
python -m venv venv

---

Configure Environment Variables
```
POSTGRES_HOST=localhost   # Change to 'db' when using Docker Compose
POSTGRES_DB=Prajyot_db
POSTGRES_USER=Prajyot_user
POSTGRES_PASSWORD=Prajyot_pass
REDIS_HOST=localhost      # Change to 'redis' when using Docker Compose
REDIS_PORT=6379
```
⚡ Tip: When using Docker Compose, POSTGRES_HOST should be the service name of the database (db) and REDIS_HOST should be the service name of Redis (redis).

✅ After this, your project will be on GitHub, excluding venv/ and other ignored files.
## 4️⃣ Running the App Locally
Make sure PostgreSQL and Redis are running locally (or in containers).
- Activate your virtual environment:
- .\venv\Scripts\Activate    # Windows

- source venv/bin/activate    # Linux/Mac
- Run the Flask app:

- python app.py
### Open your browser and go to:
```
http://127.0.0.1:5000
You should see the “Hello Prajyot Fulsundar” message
```
