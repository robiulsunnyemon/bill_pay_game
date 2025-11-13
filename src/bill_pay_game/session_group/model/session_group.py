from beanie import Document,Link
from pydantic import Field
import uuid
from src.bill_pay_game.session.model.session import SessionModel


class SessionGroupModel(Document):
    id:str=Field(default_factory=lambda: str(uuid.uuid4()),alias="_id")
    session:Link[SessionModel]
    member_name:str

    class Settings:
        name = "session_group"