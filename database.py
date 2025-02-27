from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATA_BASE_URL

Base = declarative_base()

_engine = create_engine(DATA_BASE_URL,pool_size=10, max_overflow=20, pool_timeout=30, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)


def init_db():
    Base.metadata.create_all(bind=_engine)