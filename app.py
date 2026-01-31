from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    name = ""
    if request.method == 'POST':
        name = request.form.get('name')
    return render_template('index.html', name=name)
    
if __name__ == '__main__':
    app.run(debug=True)


# To run app.py, ensure you have an 'index.html' file in a 'templates' and 
# run command: python3 app.py