from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:Tomorrowland@localhost:5432/Panaderia")
db_session = scoped_session(sessionmaker(bind=engine))

#autocommit=False, autoflush=False, 