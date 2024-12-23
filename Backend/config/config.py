import os

# Define the base directory of the application
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Base configuration with default settings."""
    DEBUG = False
    TESTING = False
    SQLITE_DB_DIR = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authorization"
    WTF_CSRF_ENABLED = False  # Disable CSRF for API requests

class LocalDevelopmentConfig(Config):
    """Configuration for local development."""
    DEBUG = True
    SQLITE_DB_DIR = os.path.join(BASE_DIR, '../database')
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(SQLITE_DB_DIR, 'database.sqlite3')
    SECRET_KEY = 'EventManagement@123' 
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_PASSWORD_SALT = 'event-management123'  # Strong unique key
    JWT_SECRET_KEY = 'EventManagement@123'  # Strong unique random key
