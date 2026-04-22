from datetime import datetime, timezone
from uuid import uuid4

from app.config import Settings
from app.repositories.users import UserRepository
from app.security import hash_password


def initialize_data(user_repository: UserRepository, settings: Settings) -> None:
    user_repository.ensure_indexes()

    seed_users = [
        {
            "email": settings.manager_email,
            "password": settings.manager_password,
            "role": "manager",
        },
        {
            "email": settings.user_email,
            "password": settings.user_password,
            "role": "user",
        },
    ]

    for seed_user in seed_users:
        existing = user_repository.get_by_email(seed_user["email"])
        if existing is not None:
            continue

        user_repository.create(
            {
                "id": str(uuid4()),
                "email": seed_user["email"],
                "password_hash": hash_password(seed_user["password"]),
                "role": seed_user["role"],
                "created_at": datetime.now(timezone.utc),
            }
        )

