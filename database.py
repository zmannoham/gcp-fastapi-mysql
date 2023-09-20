from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#URL_DATABASE = 'mysql+pymysql://root:jimmy123@localhost:3306/CatSocial'
URL_DATABASE = 'mysql+pymysql://jimmy:jimmy123@10.7.0.3:3306/main'
## URL to correct corresponding server.
## 'mysql+pymysql://jimmy:jimmy123@10.7.0.3:3306/main' for use in GCP

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

