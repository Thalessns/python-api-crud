"""Endpoints for user operations."""
from fastapi import APIRouter, status
from pydantic import EmailStr

from src.routing.user.service import user_service
from src.routing.user.schemas import UserCreate, User


user_router = APIRouter()
prefix = "/user"


@user_router.post(prefix, status_code=status.HTTP_201_CREATED)
async def create_user(data: UserCreate) -> str:
    """Endpoint to create a new user.

    Returns:
        str: Success message.
    """
    await user_service.create_user(data)
    return "User created successfully!"


@user_router.get(prefix, status_code=status.HTTP_200_OK)
async def get_user(email: EmailStr) -> User:
    """Endpoint to fetch a user by ID.

    Args:
        id (EmailStr): The ID of the user to fetch.

    Returns:
        User: The user data.
    """
    return await user_service.get_user_by_id(email)