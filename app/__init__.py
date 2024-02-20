from flask import Flask


def create_app():
    app = Flask(__name__)

    # Import and register blueprints
    from .main import main_bp
    from .about import about_bp
    from .contact import contact_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(contact_bp)

    return app
