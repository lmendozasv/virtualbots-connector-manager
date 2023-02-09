from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://deltasist_credify:Credify$100@mysql.us.cloudlogin.co/deltasist_credify')
Session = sessionmaker(bind=engine)

Base = declarative_base()