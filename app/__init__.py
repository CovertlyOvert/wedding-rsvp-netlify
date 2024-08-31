from flask import Flask
from app.routes import main
from app.database import init_db

def create_app():
    app = Flask(__name__, template_folder='templates')
    # app = Flask(__name__)
    
    # Initialize the database
    init_db()
    
    # Register Blueprints
    app.register_blueprint(main)

    return app
