
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import databases
import sqlalchemy

#SQLALCHEMY_DATABASE_URL = os.getenv("DB_CONN")
SQLALCHEMY_DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
print(SQLALCHEMY_DATABASE_URL)

database = databases.Database(SQLALCHEMY_DATABASE_URL)

metadata = sqlalchemy.MetaData()

table = sqlalchemy.Table(
    "srealitky",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column("title", sqlalchemy.Text()),
    sqlalchemy.Column("image_url", sqlalchemy.Text())
)
engine = sqlalchemy.create_engine(
    SQLALCHEMY_DATABASE_URL
)
metadata.create_all(engine)

