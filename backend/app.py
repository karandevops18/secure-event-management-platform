import time
from flask import Flask
from flask_cors import CORS

from config import (
    SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS
)

from models.db import db

from models.user import User

from routes.auth import auth_bp
from routes.events import events_bp
from routes.bookings import bookings_bp

app = Flask(__name__)

CORS(app)

# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)

# Health Check
@app.route("/health")
def health():
    return {"status": "healthy"}, 200

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix="/api")
app.register_blueprint(events_bp, url_prefix="/api")
app.register_blueprint(bookings_bp, url_prefix="/api")

if __name__ == "__main__":
    max_retries = 10
    retry_delay = 5

    for attempt in range(max_retries):
        try:
            print(
                f"Attempt {attempt + 1}: Connecting to database...",
                flush=True
            )

            with app.app_context():
                db.create_all()

            print("Database connection successful!", flush=True)
            break

        except Exception as e:
            print(f"Database not ready: {e}", flush=True)

            if attempt < max_retries - 1:
                time.sleep(retry_delay)
            else:
                raise

    app.run(host="0.0.0.0", port=5000)