from flask_assets import ManageAssets
from flask_script import Manager
from flask_security.script import (CreateUserCommand, CreateRoleCommand, AddRoleCommand,
                                   RemoveRoleCommand, DeactivateUserCommand, ActivateUserCommand)
from flask_migrate import Migrate, MigrateCommand

from . import app, assets, db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('assets', ManageAssets(assets))
manager.add_command('db', MigrateCommand)

manager.add_command('create', CreateUserCommand, namespace='user')
manager.add_command('activate', ActivateUserCommand, namespace='user')
manager.add_command('deactivate', DeactivateUserCommand, namespace='user')
manager.add_command('add_role', AddRoleCommand, namespace='user')
manager.add_command('remove_role', RemoveRoleCommand, namespace='user')

manager.add_command('create', CreateRoleCommand, namespace='role')
