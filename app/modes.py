from pydantic import BaseModel

class PeopleForseUser(BaseModel):
    id : int
    first_name : str
    last_name : str


