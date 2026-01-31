from flask import Blueprint, render_template, request, redirect, url_for, flash

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def home():
    name = None
    if request.method == 'POST':
        name = request.form.get('name')

        # Basic validation
        if not name:
            flash('Name cannot be empty!', 'error')
            return redirect(url_for('main.home'))
        
        # You could save the name to a database or perform other actions here
        # for now, pass it via query parameters (simple way)
        return render_template('index.html', name=name)

    name = request.args.get('name')
    return render_template('index.html', name=name)

@main.route('/about', methods=['GET'])
def about():
    return render_template('about.html')
