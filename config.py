import os


class Config:
    # Use an environment variable or a default "dev" key
    SECRET_KEY = os.environ.get("SECRET_KEY") or "super-secret-change-me"

    # Define where the SQLite file lives
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "app.db")

    # Stop Flask-SQLAlchemy from tracking every modification (saves memory)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True
