from pymongo import MongoClient
from config import MONGO_URI, DB_NAME
from threading import Lock


class MongoDB:

    _instance = None
    _lock = Lock()

    def __new__(cls):

        # First check (without lock)
        if cls._instance is None:

            with cls._lock:

                # Second check (inside lock)
                if cls._instance is None:

                    cls._instance = super().__new__(cls)

                    cls._instance.client = MongoClient(
                        MONGO_URI
                    )

                    cls._instance.db = cls._instance.client[
                        DB_NAME
                    ]

        return cls._instance

    def get_db(self):
        return self.db