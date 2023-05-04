from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
import random

from db.database import (
    add_user,
    db_delete_user,
    retrieve_user,
    retrieve_users,
    db_update_user,
)
from server.models.user import (
    CreatedResponseModel,
    OKResponseModel,
    ErrorResponseModel,
    UserModel,
    UpdateUserModel,
)

router = APIRouter()


@router.post("/", response_description="User data added to the database")
async def create_user(user: UserModel = Body(...)):
    user = jsonable_encoder(user)

    # Create a random dice number for the user
    generated_dice = random.randint(1, 6)
    user["dice"] = generated_dice

    new_user = await add_user(user)
    return CreatedResponseModel(new_user, "User added")


@router.get("/", response_description="All the users data have been retrieved")
async def get_users():
    users = await retrieve_users()
    if users:
        return OKResponseModel(users, "All users data retrieved OK")
    return OKResponseModel(users, "There are no users in the database")


@router.get(
    "/{id}",
    response_description="It returns the information from an user, through its id",
)
async def get_user(id):
    user = await retrieve_user(id)
    if user:
        return OKResponseModel(user, "User data retrieved OK")
    return OKResponseModel(user, f"There are no users in the database with id {id}")


@router.put(
    "/{id}",
    response_description="User with given id's information is updated, including dice number (cheating here is allowed :P)",
)
async def update_user(id: str, updated_user: UpdateUserModel = Body(...)):
    updated_user = jsonable_encoder(updated_user)

    is_user_updated = await db_update_user(id, updated_user)
    if is_user_updated:
        return OKResponseModel(
            updated_user, f"User with id {id} has been correclty updated"
        )
    return ErrorResponseModel(
        f"There was an error updating user with id {id}",
        404,
        f"We didn't find the user with id {id}",
    )


@router.delete(
    "/{id}", response_description="The user information is deleted from the database"
)
async def delete_user(id: str):
    is_user_deleted = await db_delete_user(id)
    if is_user_deleted:
        return OKResponseModel(is_user_deleted, f"User with id {id} correctly deleted")
    return ErrorResponseModel(
        f"There was an error deleting user with id {id}",
        404,
        f"We didn't find the user with id {id}",
    )
