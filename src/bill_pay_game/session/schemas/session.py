from pydantic import BaseModel
from datetime import datetime


class SessionResponse(BaseModel):
    id:str
    session_name: str
    created_at:datetime

