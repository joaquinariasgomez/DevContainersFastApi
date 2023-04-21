from typing import Optional

from pydantic import BaseModel, Field, constr

class UserSchema(BaseModel):
    name: constr(strict=True) = Field(...)
    age: int = Field()

    class config:
        schema_extra = {
            "example": {
                "name": "Joaquín Arias",
                "age": "28"
            }
        }

class UpdateUserModel(BaseModel):
    name: Optional[constr(strict=True)]
    
    type: Optional[bool]

    class config:
        schema_extra = {
            "example": {
                "name": "Joaquín Arias",
                "age": "28"
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