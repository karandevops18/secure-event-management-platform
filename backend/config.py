DB_USER = "eventadmin"
DB_PASSWORD = "StrongPassword123!"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "eventdb"

SQLALCHEMY_DATABASE_URI = (
    f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

SQLALCHEMY_TRACK_MODIFICATIONS = False
