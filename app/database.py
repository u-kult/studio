from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .settings import settings

engine = create_engine(
    settings.sqlalchemy_database_url,
    # connect_args={"check_same_thread": False},
)

Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db():
    with Session() as session:
        yield session
