from typing import Any

from pymongo import ASCENDING
from pymongo.database import Database


class UserRepository:
    def __init__(self, database: Database) -> None:
        self.collection = database["users"]

    def ensure_indexes(self) -> None:
        self.collection.create_index([("id", ASCENDING)], unique=True)
        self.collection.create_index([("email", ASCENDING)], unique=True)

    def create(self, user_data: dict[str, Any]) -> dict[str, Any]:
        self.collection.insert_one(user_data)
        return user_data

    def get_by_email(self, email: str) -> dict[str, Any] | None:
        return self.collection.find_one({"email": email})

    def get_by_id(self, user_id: str) -> dict[str, Any] | None:
        return self.collection.find_one({"id": user_id})

    def list_users(self) -> list[dict[str, Any]]:
        return list(self.collection.find({}, {"_id": 0, "password_hash": 0}).sort("created_at", ASCENDING))

