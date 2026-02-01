from dotenv import load_dotenv
import os
from flask import Flask
from routes.main import main
from extensions import db

load_dotenv()  # Load environment variables from a .env file if present 

app = Flask(__name__)

# Use environment variable for secret key if available (fallback to a default for development)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'fallback-secret')

# Database configuration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')

# Initialize database with app
db.init_app(app)

# Register Blueprints
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(
        debug=os.getenv('FLASK_ENV') == 'development',
        port=5000
    )


# Make sure venv (environment) is active: 
# source venv/bin/activate
# run Flask: 
# python3 app.py 