from flask import Flask
from .extensions import db, migrate, cors, bcrypt
from .routes import main_bp  # Importing your main blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Initialize extensions
    # db.init_app(app)
    # migrate.init_app(app, db)
    # cors.init_app(app)
    # bcrypt.init_app(app)

    # Register the blueprint
    app.register_blueprint(main_bp)

    # Ensure there is a base route to handle the root URL
    @app.route('/')
    def index():
        return "Welcome to the Event Management Platform API!", 200

    return app
