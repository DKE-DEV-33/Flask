Flask CRUD App (Blueprints + SQLAlchemy)

A clean, beginner-to-intermediate Flask application demonstrating best practices for routing, templates, database integration, and environment configuration. Built with scalability and clarity in mind.

This project implements a simple CRUD workflow (create, read, update, delete) using Flask Blueprints, SQLAlchemy, and Jinja templates.

Features

Flask Blueprints for clean route separation

SQLite database with SQLAlchemy ORM

Create, edit, delete, and list entries

Flash messages for user feedback

Environment-based configuration (.env)

Base layout with reusable templates

Static asset handling (CSS)

Pagination-ready structure

Production-safe secret key handling

Tech Stack

Python

Flask

Flask-SQLAlchemy

Jinja2

SQLite

dotenv

HTML / CSS

Project Structure
.
├── app.py
├── extensions.py
├── routes/
│   └── main.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── edit.html
│   └── delete.html
├── static/
│   └── css/
│       └── style.css
├── data.db
├── .env
├── .gitignore
└── README.md

Setup & Installation
1. Clone the repo
git clone <repo-url>
cd flask-project

2. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Create .env file
FLASK_ENV=development
FLASK_SECRET_KEY=your-secret-key


.env should not be committed to GitHub.

Initialize the Database
python
>>> from app import app
>>> from extensions import db
>>> with app.app_context():
...     db.create_all()


This will create data.db.

Run the App
python app.py


Then visit:

http://127.0.0.1:5000

What This Project Demonstrates

How to structure a Flask app beyond a single file

Avoiding circular imports with extensions

Proper handling of POST/GET requests

Safe environment variable usage

Clean HTML templating with inheritance

Debugging common Flask issues (403s, routing, static files)

Possible Next Improvements

User authentication

Full pagination support

REST API endpoints

Form validation with WTForms

Production deployment (Gunicorn + Nginx)

PostgreSQL swap for SQLite

![License](https://img.shields.io/badge/license-MIT-green)