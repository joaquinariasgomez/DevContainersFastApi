from typing import Optional

from pydantic import BaseModel, EmailStr, Field, constr


class UserModel(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)

    class config:
        schema_extra = {
            "example": {
                "name": "Joaquín Arias",
                "email": "joaquin.42.is.the.answer@gmail.com",
            }
        }


class UpdateUserModel(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    dice: Optional[int] = Field(None, ge=1, le=6)

    class config:
        schema_extra = {
            "example": {
                "name": "Joaquín Arias",
                "email": "joaquin.42.is.the.answer@gmail.com",
                "dice": 6,
            }
        }


def CreatedResponseModel(data, message):
    return {"data": [data], "code": 201, "message": message}


def OKResponseModel(data, message):
    return {"data": [data], "code": 200, "message": message}


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
