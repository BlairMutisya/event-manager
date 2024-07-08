from flask import Flask
from .extensions import db, migrate, cors, bcrypt
from .routes import main_bp, event_bp, contact_bp, auth_bp, user_bp
from .config import Config  # Import Config from your config module

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Use Config from your config module

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    cors.init_app(app)
    bcrypt.init_app(app)

    # Register blueprints
    app.register_blueprint(main_bp, url_prefix='/api')
    app.register_blueprint(event_bp, url_prefix='/api')
    app.register_blueprint(contact_bp, url_prefix='/api')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(user_bp, url_prefix='/api')

    # Define the base route
    @app.route('/')
    def index():
        return "Welcome to the Event Management Platform API!", 200

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
