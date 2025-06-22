# Movie App

A full-stack Movie Application built with Django REST API backend and Vue.js frontend, containerized with Docker and managed via docker-compose.

---

## Project Structure

APIProject/
│
├── api/ # Django app
├── APIProject/ # Django project settings
├── frontend/ # Vue.js frontend app
├── db.sqlite3 # SQLite database file
├── docker-compose.yml # Docker Compose config
├── Dockerfile # Backend Dockerfile
├── vue.Dockerfile # Frontend Dockerfile
└── requirements.txt # Python dependencies


---

## Prerequisites

- Docker
- Docker Compose

---

## Running the Project

### 1. Build and start containers

```bash
cd APIProject
docker-compose build
docker-compose up

2. Access the apps

    Backend API: http://localhost:8000

    Frontend UI: http://localhost:8080 go directely to http://localhost:8080/movies

Database Persistence

    The project uses SQLite stored as db.sqlite3 in the project root.

    The entire project folder is mounted into the backend container (./:/app), so the database file persists between container restarts.

    Make sure db.sqlite3 exists in the project root, or Django will create a new empty database on first run.

Environment Variables

    Vue frontend connects to backend via VUE_APP_API_URL environment variable.

    Ensure it points to http://localhost:8000 in frontend/.env (or your local setup).

Development Without Docker (Optional)
Frontend

cd frontend
npm install
npm run serve

Backend

pip install -r requirements.txt
python manage.py runserver

Notes

    When deploying or sharing the project, include the db.sqlite3 file if you want to keep existing data.

    To reset data, simply delete db.sqlite3 and restart containers.

    The backend serves the API at port 8000, frontend at 8080.

Author

Charbel Al Nasr
