from flask import Flask
from flask_assets import Bundle, Environment
from flask_security import Security, SQLAlchemyUserDatastore
from flask_sqlalchemy import SQLAlchemy
from webassets.filter import register_filter
from webassets_browserify import Browserify

app = Flask(__name__)
app.config.from_object('{{cookiecutter.project_name}}.configuration.EnvConfig')

db = SQLAlchemy(app)

# Configure static assets
assets = Environment(app)

css = Bundle('scss/app.scss', filters='libsass', output='dist/app.css', depends=['scss/**/*.scss'])
assets.register('css_all', css)

register_filter(Browserify)
js = Bundle('js/app.js', filters='browserify', output='dist/app.js', depends=['js/**/*.js'])
assets.register('js_all', js)

# Import models down here to ensure circular import works as expected
from .models.role import Role
from .models.user import User
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

from .views import bind_routes
bind_routes(app)
