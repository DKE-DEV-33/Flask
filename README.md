# Flask CRUD App (Blueprints + SQLAlchemy)

A clean, production-minded Flask application demonstrating best practices for routing, templating, database integration, and environment configuration.

This project implements a simple **CRUD workflow** (Create, Read, Update, Delete) using Flask Blueprints, SQLAlchemy, and Jinja templates, with an emphasis on maintainable structure and real-world patterns.

---

## ✨ Features

- Modular routing using Flask Blueprints
- SQLite database with SQLAlchemy ORM
- Create, edit, delete, and list records
- Flash messages for user feedback
- Environment-based configuration (`.env`)
- Template inheritance with `base.html`
- Static asset handling (CSS)
- Pagination-ready architecture
- Secure secret key handling for production

---

## 🛠 Tech Stack

- **Python**
- **Flask**
- **Flask-SQLAlchemy**
- **Jinja2**
- **SQLite**
- **python-dotenv**
- **HTML / CSS**

---

## 📁 Project Structure

**|── app.py** <br>
**|── extensions.py**<br>
**|── routes/**<br>
**│  └── main.py**<br>
**|── templates/**<br>
**| ├── base.html**<br>
**| ├── index.html**<br>
**| ├── about.html**<br>
**| ├── edit.html**<br>
**| └── delete.html**<br>
**|── static/**<br>
**| └── css/**<br>
**| └── style.css**<br>
**|── data.db**<br>
**|── .env**<br>
**|── .gitignore**<br>
**|── README.md**

---

## 🚀 Getting Started

### 1. Clone the Repository
**```bash**<br>
**git clone <repo-url>**<br>
**cd flask-project**<br>

### 2. Create & Activate a Virtual Environment
**python3 -m venv venv**<br>
**source venv/bin/activate**

### 3. Install Dependencies
**pip install -r requirements.txt**

### 4. Set Environment Variables

**Create a .env file in the project root:**<br>

**FLASK_ENV=development**<br>
**FLASK_SECRET_KEY=your-secret-key**<br>

---

## 🗄 Database Setup

### Initialize the SQLite database:

**python**

**from app import app**
**from extensions import db**

**with app.app_context():**<br>
**db.create_all()**

---

## ▶️ Running the Application

**python app.py**

**Then open your browser and navigate to:**

**http://127.0.0.1:5000**

---

## 🎯 What This Project Demonstrates

**Structuring a Flask app beyond a single file**

**Avoiding circular imports using an extensions module**

**Handling GET and POST requests correctly**

**Safe use of environment variables**

**Clean HTML templating with inheritance**

**Debugging common Flask issues (403 errors, static files, routing)**

---

## 🔮 Possible Enhancements

**User authentication & authorization**

**Server-side pagination**

**RESTful API endpoints**

**Form validation with WTForms**

**PostgreSQL migration**

**Production deployment (Gunicorn + Nginx / Render / Fly.io)**