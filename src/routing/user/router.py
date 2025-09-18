"""Endpoints for user operations."""
from fastapi import APIRouter, status
from pydantic import EmailStr

from src.routing.user.service import user_service
from src.routing.user.schemas import (
    User,
    UserCreate,
    UserUpdate
)

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
    return await user_service.get_user_by_email(email)


@user_router.put(prefix, status_code=status.HTTP_202_ACCEPTED)
async def update_user(data: UserUpdate) -> str:
    """Endpoint to update a user.
    
    Returns:
        str: "Success message."
    """
    await user_service.update_user(data)
    return "User updated successfully!"


@user_router.delete(prefix, status_code=status.HTTP_200_OK)
async def delete_user(email: EmailStr) -> str:
    """Endpoint to dele an user by the email.
    
    Args:
        email (EmailStr): The user email.
    """
    await user_service.delete_user(email)
    return "User deleted successfully!"
