from flask import Blueprint, render_template, request 

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def home():
    name = ""
    if request.method == 'POST':
        name = request.form.get('name')
    return render_template('index.html', name=name)

@main.route('/about', methods=['GET', 'POST'])
def about():
    return render_template("about.html")
