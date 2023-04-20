from typing import Optional

from pydantic import BaseModel, EmailStr, Field, constr

class UserSchema(BaseModel):
    name: constr(strict=True) = Field(...)  # ... means ellipsis, aka required field
    email: EmailStr = Field(...)
    type: bool = Field()

    class config:
        schema_extra = {
            "example": {
                "name": "Joaquín Arias",
                "email": "joaquin.42.is.the.answer@gmail.com",
                "type": True
            }
        }

class UpdateUserModel(BaseModel):
    name: Optional[constr(strict=True)]
    email: Optional[EmailStr]
    type: Optional[bool]

    class config:
        schema_extra = {
            "example": {
                "name": "Joaquín Arias",
                "email": "joaquin.42.is.the.answer@gmail.com",
                "type": True
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message
    }

def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }