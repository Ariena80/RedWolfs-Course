import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://arien:12345678@fizorger?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24).hex()
