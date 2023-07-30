import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker


class Orm:
    engine = None
    factory = None
    session = None
    connection = None
    load_dotenv()

    def __init__(self):
        if not self.engine:
            self.url_object = URL.create(
                drivername=os.getenv('DATABASE_DRIVER'),
                username=os.getenv('DATABASE_USERNAME'),
                password=os.getenv('DATABASE_PASSWORD'),  # plain (unescaped) text
                host=os.getenv('DATABASE_HOST'),
                port=os.getenv('DATABASE_PORT'),
                database=os.getenv('DATABASE_NAME'),
            )
            self.engine = create_engine(self.url_object)
        super().__init__()

    def get_session(self):
        if not self.session:
            self.factory = sessionmaker(bind=self.engine)
            self.session = self.factory()
        else:
            self.session.close()
            self.factory = sessionmaker(bind=self.engine)
            self.session = self.factory()
        return self.session

    def get_connection(self):
        if not self.engine:
            self.engine = create_engine(self.url_object)
        self.connection = self.engine.connect()
        return self.connection
