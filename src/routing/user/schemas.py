"""Schemas for user-related operations."""
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    """Schema for creating a new user."""

    name: str
    email: EmailStr


class UserUpdate(BaseModel):
    """Schema for updating a user."""

    email: EmailStr
    name:  str


class User(BaseModel):
    """Schema for user data."""

    email: EmailStr
    name: str
    date_created: str
    date_updated: str | None = None
