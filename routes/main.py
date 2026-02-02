from flask import Blueprint, render_template, request, redirect, url_for, flash
from extensions import db
from routes.models import Name

# Blueprint setup
main = Blueprint('main', __name__)

# Home route handling both GET and POST requests
@main.route('/', methods=['GET', 'POST'])
def home():
    
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

    # Pagination logic
    page = request.args.get('page', 1, type=int)

    pagination = Name.query.order_by(
        Name.created_at.desc()
    ).paginate(
        page=page, 
        per_page=5, 
        error_out=False
    )

    # Render the template with names and pagination info
    return render_template(
        'index.html',
        names=pagination.items,
        pagination=pagination
    )

# About route
@main.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

# Delete route 
@main.route('/delete/<int:name_id>', methods=['GET', 'POST'])
def delete_name(name_id):
    name_entry = Name.query.get_or_404(name_id)

    if request.method == 'POST':
        db.session.delete(name_entry)
        db.session.commit()
        flash(' Name deleted successfully.', 'success')
        return redirect(url_for('main.home'))
    
    return render_template('delete.html', name_entry=name_entry)

# edit route
@main.route('/edit/<int:name_id>', methods=['GET', 'POST'])
def edit_name(name_id):
    name_entry = Name.query.get_or_404(name_id)
    # For the flash message to show the old name vs the new name
    old_name = name_entry.name
    if request.method == 'POST':
        new_name = request.form.get('name', '').strip()

        # Basic validation
        if not new_name:
            flash('Name cannot be empty!', 'error')
            return redirect(url_for('main.edit_name', name_id=name_id))

        name_entry.name = new_name
        db.session.commit()
        flash(f'Updated {old_name} to {new_name}', 'success')
        return redirect(url_for('main.home'))

    return render_template('edit.html', name_entry=name_entry)