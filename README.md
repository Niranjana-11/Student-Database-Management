# 🎓 Student Management System

A full-stack student record manager built with **FastAPI**, **SQLAlchemy** and **SQLite**, with a clean web interface and an optional AI assistant that answers questions about your student data using a local LLM (Ollama).

🌐 **Live demo:** https://student-database-management-upsn.onrender.com

> ⚠️ The demo runs on a free server, so it sleeps after 15 minutes without visits (the first load can take about a minute) and the data resets on restart. The AI assistant needs Ollama, so it works when you run the project locally and shows a message on the live demo.

## ✨ Features

- ➕ Add, ✏️ edit, 🗑️ delete and 📋 list students
- 🔍 Instant filtering by name, class or subject
- ✅ Input validation (a student name is mandatory and cannot be blank)
- 🤖 Ask questions in plain English, answered by a local `llama3.2:3b` model
- 📘 Interactive API docs at `/docs` (Swagger UI)
- 🌗 Responsive interface with automatic light and dark mode
- ☁️ Deployed on Render, with ready-to-use systemd and nginx files for a Linux server

## 🧰 Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI, Pydantic v2 |
| Database | SQLite via SQLAlchemy ORM |
| AI | LangChain + Ollama (`llama3.2:3b`) |
| Frontend | HTML, CSS and vanilla JavaScript |
| Deployment | Render (live demo), systemd + nginx (Linux server) |

## 📁 Project Structure

```
Student-Database-Management/
├── app/
│   ├── routes/
│   │   ├── ai_query.py
│   │   ├── base.py
│   │   ├── create_student.py
│   │   ├── delete_student.py
│   │   ├── get_student.py
│   │   └── update_student.py
│   ├── config.py
│   ├── database.py
│   ├── model.py
│   └── schema.py
├── Frontend/
│   └── index.html
├── deploy/
│   ├── nginx.conf
│   └── student-app.service
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Niranjana-11/Student-Database-Management.git
cd Student-Database-Management
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv

# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. (Optional) Configure the environment

Create a `.env` file in the project root:

```env
DATABASE_URL=sqlite:///./students.db
```

If you skip this, the app uses `sqlite:///./students.db` by default.

### 5. Run the app

```bash
uvicorn main:app --reload
```

| Page | URL |
|---|---|
| Web interface | http://127.0.0.1:8000/ui/ |
| API docs | http://127.0.0.1:8000/docs |

On first start, three sample students are added automatically when the database is empty.

## 🤖 AI Assistant (optional)

The "Ask about your students" box uses a local model, so no API key is needed.

1. Install [Ollama](https://ollama.com)
2. Pull the model: `ollama pull llama3.2:3b`
3. Keep Ollama running while you use the app

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/students/` | Create a student |
| GET | `/students/` | List students (`skip`, `limit`) |
| GET | `/students/{id}` | Get one student |
| PUT | `/students/{id}` | Update a student |
| DELETE | `/students/{id}` | Delete a student |
| POST | `/ai/query-student` | Ask a question about the data |

**Example request body**

```json
{
  "student_name": "Asha Nair",
  "student_class": "10",
  "student_section": "A",
  "student_dob": "2009-05-14",
  "student_sub": "Mathematics"
}
```

## ☁️ Deployment

### Render (used for the live demo)

| Setting | Value |
|---|---|
| Build command | `pip install -r requirements.txt` |
| Start command | `uvicorn main:app --host 0.0.0.0 --port $PORT` |
| Instance type | Free |

Every push to `main` can redeploy the service. Free instances use temporary storage, so the SQLite data resets on restart.

### Linux server (systemd + nginx)

The `deploy/` folder contains two ready-made files:

- `student-app.service`: runs the app as a background service with systemd
- `nginx.conf`: nginx reverse proxy that forwards port 80 to the app

```bash
# Run the app as a service
sudo cp deploy/student-app.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now student-app

# Put nginx in front of it
sudo cp deploy/nginx.conf /etc/nginx/sites-available/student-app
sudo ln -s /etc/nginx/sites-available/student-app /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```

Before using them, edit the user name and folder paths in `student-app.service` to match your server, and create a Linux virtual environment (the Windows `.venv` will not work).

## 🛣️ Future Improvements

- Authentication and user roles
- Persistent database (PostgreSQL) for the hosted version
- Hosted LLM option so the AI assistant also works online
- Database migrations with Alembic
- Unit tests with pytest

## 👩‍💻 Author

**Niranjana** · [GitHub](https://github.com/Niranjana-11) · [LinkedIn](https://linkedin.com/in/niranjanarajesh)
