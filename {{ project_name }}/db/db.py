import json
from sqlalchemy import create_engine, event, orm, and_
from sqlalchemy.orm import sessionmaker, scoped_session, Session, ORMExecuteState, with_loader_criteria
from sqlalchemy.engine import URL

class Database:
    def __init__(self, path: str):
        self._engine = None
        self._session = None
        self._db_setting_path = path

    def _load_db_setting(self) -> dict:
        with open(self._db_setting_path, "r") as f:
            return json.load(f)

    def build(self) -> None:
        db_setting = self._load_db_setting()
        url = URL.create(
            drivername=db_setting.get("driver"),
            username=db_setting.get("user"),
            password=db_setting.get("password"),
            host=db_setting.get("host"),
            port=db_setting.get("port"),
            database=db_setting.get("database"),
        )

        self._engine = create_engine(
            url=url,
            echo=False
        )

        self._session = scoped_session(
            session_factory=sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            )
        )

    def get_session(self) -> any:
        db = self._session
        try:
            yield db
        finally:
            db.close()
