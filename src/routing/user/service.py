"""Module for handling user-related operations."""
from pydantic import EmailStr

from src.database.database import Database
from src.routing.user.tables import user_table
from src.routing.user.exceptions import (
    UserNotFound
)
from src.routing.user.schemas import (
    User,
    UserCreate,
    UserUpdate
)


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
    async def get_user_by_email(cls, email: EmailStr) -> User:
        """Fetch a user by email.
        
        Args:
            email (EmailStr): The email of the user to fetch.

        Returns:
            User: The user with the specified email.

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

    @classmethod
    async def update_user(cls, data: UserUpdate) -> None:
        """Update a user data in the database.

        Args:
            data (UserUpdate): The user data to be updated.
        """
        _ = await cls.get_user_by_email(data.email)
        update_query = user_table.update().values(
            name = data.name).where(user_table.c.email == data.email)
        await Database.execute(update_query)

    @classmethod
    async def delete_user(cls, email: EmailStr) -> None:
        """Delete a user by the email.

        Args:
            email (EmailStr): The user email.
        """
        _ = await cls.get_user_by_email(email)
        delete_query = user_table.delete().where(user_table.c.email == email)
        await Database.execute(delete_query)


user_service = UserService()
