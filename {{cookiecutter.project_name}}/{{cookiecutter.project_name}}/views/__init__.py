from . import root


def bind_routes(app):
    app.add_url_rule('/', 'root_index', root.index)
