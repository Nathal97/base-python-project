def init_routes(app):
    from app.routes.home_routes import example_route 
    from app.routes.login_routes import login_route 
    from app.routes.register_routes import register_route 
     # Importe la route spécifique ici
    app.register_blueprint(example_route)
    app.register_blueprint(login_route)
    app.register_blueprint(register_route)
