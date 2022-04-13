from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

Base = automap_base()


SQLALCHEMY_DATABASE_URL = "postgresql://fsmuser:HelpMe@db/database"

engine = create_engine(SQLALCHEMY_DATABASE_URL, encoding="latin1", echo=True,)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
