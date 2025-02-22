from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
from modes import PeopleForseUser

app = FastAPI()

@app.get("/")
async def root():
    pf = PeopleForseUser()

    return {"Nginx": "I'm alive"}