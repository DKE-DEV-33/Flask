from dotenv import load_dotenv
import os
from flask import Flask
from routes.main import main

load_dotenv()  # Load environment variables from a .env file if present 

app = Flask(__name__)

# Use environment variable for secret key if available (fallback to a default for development)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'fallback-secret')

app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)


# Make sure venv (environment) is active: 
# source venv/bin/activate
# run Flask: 
# python3 app.py 