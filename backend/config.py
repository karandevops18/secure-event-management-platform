import os

DB_USER = os.getenv("DB_USER", "eventadmin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "CHANGE_ME")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "eventdb")

SQLALCHEMY_DATABASE_URI = (
    f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

SQLALCHEMY_TRACK_MODIFICATIONS = False