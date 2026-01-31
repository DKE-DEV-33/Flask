from flask import Flask
from routes.main import main

app = Flask(__name__)
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)


# To run app.py, ensure you have an 'index.html' file in a 'templates' and 
# run command: python3 app.py for now.