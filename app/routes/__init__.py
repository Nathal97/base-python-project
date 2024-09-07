def init_routes(app):
    from app.routes.routes1 import example_route  # Importe la route spécifique ici
    app.register_blueprint(example_route)
