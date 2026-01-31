from flask import Blueprint, render_template, request, redirect, url_for, flash
from extensions import db

# Blueprint setup
main = Blueprint('main', __name__)

# Model for storing submitted names
class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    
    def __repr__(self):
        return f'<Name {self.name}>'

# Home route handling both GET and POST requests
@main.route('/', methods=['GET', 'POST'])
def home():
    name = None
    if request.method == 'POST':
        submitted_name = request.form.get('name', '').strip()

        # Basic validation
        if not submitted_name:
            flash('Name cannot be empty!', 'error')
            return redirect(url_for('main.home'))
        
        new_name = Name(name=submitted_name)
        db.session.add(new_name)
        db.session.commit()

        flash('Name submitted successfully!', 'success')
        return redirect(url_for('main.home'))

    all_names = Name.query.all()
    return render_template('index.html', names=all_names)

# About route
@main.route('/about', methods=['GET'])
def about():
    return render_template('about.html')
