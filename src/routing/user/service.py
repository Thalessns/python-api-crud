"""Module for handling user-related operations."""
from pydantic import EmailStr

from src.database.database import Database
from src.routing.user.tables import user_table
from src.routing.user.exceptions import (
    UserNotFound
)
from src.routing.user.schemas import UserCreate, User


class UserService:
    """Service for user-related database operations."""

    async def create_user(cls, data: UserCreate) -> None:
        """Create a new user in the database.
        
        Args:
            data (UserCreate): The data of the user to create.
        """
        query = user_table.insert().values(**data.model_dump())
        await Database.execute(query)

    @classmethod
    async def get_user_by_id(cls, email: EmailStr) -> User:
        """Fetch a user by email.
        
        Args:
            email (EmailStr): The email of the user to fetch.

        Returns:

        Raises:
            UserNotFound: If the user with the given email does not exist.
        """
        user = await cls.get_user(email)
        if user is None:
            raise UserNotFound
        return User(**user)

    @classmethod
    async def get_user(cls, email: EmailStr) -> dict | None:
        """Fetch a user by email.
        
        Args:
            email (EmailStr): The email of the user to fetch.

        Returns:
            dict | None: The user data if found, otherwise None.
        """
        query = user_table.select().where(user_table.c.email == email)
        return await Database.fetch_one(query)


user_service = UserService()