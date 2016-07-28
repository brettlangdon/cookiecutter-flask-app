from flask import render_template
from flask_security import login_required


@login_required
def index():
    return render_template('root.jinja')
