#start from import fast api class
from fastapi import FastAPI

from mongoengine import connect

from starlette.testclient import TestClient

from app.routers import users, todos

#inisiasi
app = FastAPI()

#connect to db
mongodb = connect('mongodb', host='mongodb://localhost/test_db')
client = TestClient(app)

app.include_router(users.router, prefix="/users", tags=["User Docs"], )
app.include_router(todos.router, prefix="/todo", tags=["Todo Docs!"], )