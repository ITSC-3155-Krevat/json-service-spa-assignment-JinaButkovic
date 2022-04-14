from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

from src.config import cfg
from src.models import db
from src.routes.book_router import book_router

# Load local environment variables before anything else
load_dotenv()

# Initialize flask WSGI app
app = Flask(__name__)

# Configure and initialize database
app.config['SQLALCHEMY_DATABASE_URI'] = cfg.DB.URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Apply CORS header middleware for cross-origin requests
CORS(app)

# Register router
app.register_blueprint(book_router)
