from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
import random

from db.database import (
    add_user,
    delete_user,
    retrieve_user,
    retrieve_users,
    update_user,
)
from server.models.user import (
    CreatedResponseModel,
    OKResponseModel,
    ErrorResponseModel,
    UserSchema,
    UpdateUserModel,
)

router = APIRouter()


@router.post("/", response_description="User data added to the database")
async def create_user(user: UserSchema = Body(...)):
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
async def update_user(id: str, req: UpdateUserModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await update_user(id, req)
    if updated_user:
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
    deleted_user = await delete_user(id)
    if deleted_user:
        return OKResponseModel(deleted_user, f"User with id {id} correctly deleted")
    return ErrorResponseModel(
        f"There was an error deleting user with id {id}",
        404,
        f"We didn't find the user with id {id}",
    )
