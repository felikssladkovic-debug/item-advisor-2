from pymongo import MongoClient
from pymongo.database import Database

from app.config import Settings


def build_database(settings: Settings) -> Database:
    client = MongoClient(settings.mongodb_uri)
    return client[settings.mongodb_db]

