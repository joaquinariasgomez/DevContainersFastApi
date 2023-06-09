import motor.motor_asyncio
from bson.objectid import ObjectId

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost")

database = client.users

user_collection = database.get_collection("users_collection")

# Helpers


def user_to_dict(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "dice": user["dice"],
    }


# Database operations


async def add_user(user_data: str) -> dict:
    user = await user_collection.insert_one(user_data)

    stored_user = await user_collection.find_one({"_id": user.inserted_id})
    return user_to_dict(stored_user)


async def retrieve_users():
    users = []
    async for user in user_collection.find():
        users.append(user_to_dict(user))
    return users


async def retrieve_user(id: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_to_dict(user)


async def db_update_user(id: str, new_user_data: dict) -> bool:
    if len(new_user_data) < 1:
        return False
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await user_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": new_user_data}
        )
        if updated_user:
            return True
    return False


async def db_delete_user(id: str) -> bool:
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(id)})
        return True
    return False
