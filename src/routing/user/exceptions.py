"""Exceptions for user routing."""
from fastapi import status

from src.app.exceptions import CustomException


class UserNotFound(CustomException):
    """Exception raised when a user is not found."""

    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = "User was not found."
