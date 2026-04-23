from datetime import datetime

from pymongo import ASCENDING, MongoClient

from .config import settings
from .security import hash_password


client = MongoClient(settings.itemadvisor_mongodb_uri)
db = client[settings.itemadvisor_mongodb_db]
users_collection = db["users"]
sessions_collection = db["sessions"]


def ensure_indexes() -> None:
    users_collection.create_index([("email", ASCENDING)], unique=True)
    sessions_collection.create_index([("id", ASCENDING)], unique=True)


def ensure_seed_users() -> None:
    seed_users = [
        {
            "email": settings.itemadvisor_manager_email,
            "password": settings.itemadvisor_manager_password,
            "role": "manager",
        },
        {
            "email": settings.itemadvisor_user_email,
            "password": settings.itemadvisor_user_password,
            "role": "user",
        },
    ]

    for seed_user in seed_users:
        existing = users_collection.find_one({"email": seed_user["email"]})
        if existing:
            continue

        users_collection.insert_one(
            {
                "email": seed_user["email"],
                "password_hash": hash_password(seed_user["password"]),
                "role": seed_user["role"],
                "created_at": datetime.utcnow().isoformat() + "Z",
            }
        )
