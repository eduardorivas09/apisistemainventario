from app.app import app
from Conexion.base import Base
from Conexion.db_session import engine

def main():
    
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    app.run()

if __name__ == '__main__':
    main()