from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import config
from hash_passwords import make_hash


engine = create_engine(config.DB_URI, convert_unicode=True)
#db_session = scoped_session(sessionmaker(autocommit=True, autoflush=True, bind=engine))
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=True, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models
    # Initialize database schema (create tables)
    Base.metadata.create_all(bind=engine)
    admin_password = make_hash('dedefault')
    admin_user = models.User(username='admin', password = admin_password, active=True)
    db_session.add(admin_user)
    db_session.commit()
    
def clear_db():
    Base.metadata.drop_all(bind=engine)

