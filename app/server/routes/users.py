from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from db.database import (
    add_user,
    delete_user,
    retrieve_user,
    retrieve_users,
    update_user
)
from server.models.user import (
    ErrorResponseModel,
    ResponseModel,
    UserSchema,
    UpdateUserModel
)

router = APIRouter()

@router.post("/", response_description="Datos del user agregados a la base de datos")
async def add_user_data(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    return ResponseModel(new_user, "User agregado")

@router.get("/", response_description="Devuelve los usuarios")
async def get_users():
    users = await retrieve_users()
    if users:
        return ResponseModel(users, "Se consiguieron los datos de los usuarios")
    return ResponseModel(users, "No hay usuarios en la base de datos")

@router.get("/{id}", response_description="Devuelve la información de un usuario, a través de su id")
async def get_user(id):
    user = await retrieve_user(id)
    if user:
        return ResponseModel(user, "Se consiguieron los datos del usuario")
    return ResponseModel(user, f"No hay usuarios en la base de datos para el usuario con id {id}")

@router.put("/{id}", response_description="Se actualiza la información de un usuario")
async def update_user_data(id: str, req: UpdateUserModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    print(f"Request es como sigue: {req}")
    updated_user = await update_user(id, req)
    if updated_user:
        return ResponseModel(updated_user, f"User con id {id} actualizado correctamente")
    return ErrorResponseModel(f"Ocurrió un error actualizando el usuario {id}", 404, f"No se encontró el usuario {id}")

@router.delete("/{id}", response_description="Se elimina la información de un usuario")
async def delete_user_data(id: str):
    deleted_user = await delete_user(id)
    if deleted_user:
        return ResponseModel(deleted_user, f"Usuario con id {id} borrado satisfactoriamente")
    return ErrorResponseModel(f"Ocurrió un error borrando el usuario {id}", 404, f"No se encontró el usuario {id}")