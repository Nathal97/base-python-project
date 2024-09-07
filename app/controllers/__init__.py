def init_routes(app):
    from app.controllers.home_contoller import example_route 
    from app.controllers.user_controller import login_route 
    from app.controllers.user_controller import register_route 
     # Importe la route spécifique ici
    app.register_blueprint(example_route)
    app.register_blueprint(login_route)
    app.register_blueprint(register_route)
