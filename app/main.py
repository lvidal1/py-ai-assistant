from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

from app.infrastructure.database import db
from app.config import get_config

from app.routes.home import home_router
from app.routes.transcription import transcription_router

def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())

    # Initialize the database
    with app.app_context():
        db.init_app(app)
        db.create_all()

    CORS(app, resources=r"/transcript/*" )

    # Routes
    app.register_blueprint(home_router, url_prefix='/home')
    app.register_blueprint(transcription_router, url_prefix='/transcript')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()

