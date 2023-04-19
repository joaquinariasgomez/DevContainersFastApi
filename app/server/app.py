from fastapi import FastAPI

from server.routes.users import router as UserRouter

app = FastAPI()

app.include_router(UserRouter, tags=["User"], prefix="/user")

@app.get("/", tags=['root'])
async def read_root():
    return {"message": "Hello World!"}