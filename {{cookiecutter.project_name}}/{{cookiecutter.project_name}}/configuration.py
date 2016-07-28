import json
import os

HERE = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
NODE_MODULES = os.path.abspath(os.path.join(ROOT, 'node_modules'))


class MetaEnvConfig(type):
    def __init__(cls, name, bases, dict):
        super(MetaEnvConfig, cls).__init__(name, bases, dict)

        # Override default configuration from environment variables
        for key, value in os.environ.items():
            try:
                value = json.loads(value)
            except Exception:
                pass
            setattr(cls, key, value)


class EnvConfig(metaclass=MetaEnvConfig):
    # Assets
    BROWSERIFY_BIN = os.path.abspath(os.path.join(NODE_MODULES, '.bin', 'browserify'))
    LIBSASS_INCLUDES = [os.path.abspath(os.path.join(NODE_MODULES, 'bulma'))]
    LIBSASS_STYLE = 'compressed'

    # User sessions
    SECRET_KEY = 'super secret key'
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_PASSWORD_SALT = 'super secret salt'

    # User session templates
    SECURITY_LOGIN_USER_TEMPLATE = 'security/login_user.jinja'

    # Database
    SQLALCHEMY_DATABASE_URI = '{{cookiecutter.database_uri}}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
