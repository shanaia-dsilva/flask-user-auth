from flask import Flask
from app.auth.routes import auth
from app.api.routes import api
from app.views import views

def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(api, url_prefix="/api")
    app.register_blueprint(views, url_prefix="/")

    return app
