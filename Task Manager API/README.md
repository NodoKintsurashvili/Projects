# Task Manager — Fullstack REST API

A fullstack task manager built with **FastAPI**, **PostgreSQL**, and **JavaScript**. Supports full CRUD operations with a clean, responsive frontend.

---

## Features

- Add, edit, and delete tasks
- Mark tasks as complete / incomplete
- Filter tasks by status — All / Active / Completed
- Double-click to edit a task inline
- Data is stored in a PostgreSQL database

---

## Tech Stack

| Layer     | Technology                        |
|-----------|-----------------------------------|
| Backend   | Python, FastAPI, SQLAlchemy       |
| Database  | PostgreSQL                        |
| Frontend  | HTML, CSS, JavaScript     |
| Other     | Pydantic, python-dotenv           |

---

## Project Structure

```
task-manager/
│   ├── main.py        # FastAPI routes (CRUD endpoints)
│   ├── models.py      # SQLAlchemy Task model
│   ├── database.py    # DB connection, SessionLocal, get_db()
│   ├── .env           # Environment variables (not committed)
│   |── .env.example   # Example env file
│   ├── index.html
│   ├── style.css
│   └── script.js
└── requirements.txt
└── README.md
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/NodoKintsurashvili/Projects.git
cd task
```

### 2. Set up the backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv
```

### 3. Configure environment variables

Create a `.env` file in the `backend/` folder based on `.env.example`:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/taskdb
```

### 4. Run the backend

```bash
uvicorn main:app --reload
```

API will be available at `http://127.0.0.1:8000`

### 5. Open the frontend

Open `frontend/index.html` directly in your browser — no build step needed.

---

## API Endpoints

| Method | Endpoint        | Description        |
|--------|-----------------|--------------------|
| GET    | `/tasks`        | Get all tasks      |
| GET    | `/tasks/{id}`   | Get task by ID     |
| POST   | `/tasks`        | Create a new task  |
| PUT    | `/tasks/{id}`   | Update a task      |
| DELETE | `/tasks/{id}`   | Delete a task      |

---

## Screenshots

> _Add a screenshot of the UI here_

---

## Author

Made by **Nodo** — Junior Backend Developer
