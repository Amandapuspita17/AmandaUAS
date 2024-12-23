import os

class Config:
    # Ganti 'DATABASE_URI' dengan path yang sesuai ke database 'karyawaan'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/rumputpanjangamanda'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'kontolbelang')  # Ganti dengan kunci rahasia yang sesuai