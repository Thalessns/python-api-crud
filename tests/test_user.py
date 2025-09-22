"""Module for user-related tests."""

import pytest

from httpx import AsyncClient
from fastapi import status


@pytest.mark.asyncio
@pytest.mark.vcr
async def test_create_user(client: AsyncClient) -> None:
    """Test user creation endpoint.

    Args:
        client (AsyncClient): The AsyncClient fixture for making requests.
    """
    data = {"email": "example@f1rst.com", "name": "example"}
    response = await client.post(
        "user",
        json=data
    )
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.asyncio
@pytest.mark.vcr
async def test_get_user(client: AsyncClient) -> None:
    """Test user retrieval endpoint.

    Args:
        client (AsyncClient): The AsyncClient fixture for making requests.
    """
    param = {"email": "example@f1rst.com"}
    response = await client.get(
        "user",
        params=param
    )
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.asyncio
@pytest.mark.vcr
async def test_update(client: AsyncClient) -> None:
    """Test user update endpoint.

    Args:
        client (AsyncClient): The AsyncClient fixture for making requests.
    """
    data = {"email": "example@f1rst.com", "name": "updated example"}
    response = await client.put(
        "user",
        json=data
    )
    assert response.status_code == status.HTTP_202_ACCEPTED


@pytest.mark.asyncio
@pytest.mark.vcr
async def test_delete_user(client: AsyncClient) -> None:
    """Test user deletion endpoint.

    Args:
        client (AsyncClient): The AsyncClient fixture for making requests.
    """
    param = {"email": "example@f1rst.com"}
    response = await client.delete(
        "user",
        params=param
    )
    assert response.status_code == status.HTTP_200_OK
