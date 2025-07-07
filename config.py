import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MYSQL_HOST = '121.43.233.12:3408'
    MYSQL_PASS = '1qaz%40WSX'
    MYSQL_USER = 'root'

    SQLALCHEMY_DATABASE_URI = os.getenv(
        MYSQL_HOST,
        "mysql+pymysql://{0}:{1}@{2}/audit-pioneer?charset=utf8mb4".format(MYSQL_USER, MYSQL_PASS, MYSQL_HOST)
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


MYSQL_HOST = '121.43.233.12:3408'
MYSQL_PASS = '1qaz%40WSX'
MYSQL_USER = 'root'

SQLALCHEMY_DATABASE_URI = os.getenv(
    MYSQL_HOST,
    "mysql+pymysql://{0}:{1}@{2}/audit-pioneer?charset=utf8mb4".format(MYSQL_USER, MYSQL_PASS, MYSQL_HOST)
)
SQLALCHEMY_TRACK_MODIFICATIONS = False

