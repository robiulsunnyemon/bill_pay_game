from beanie import Document,Link
from pydantic import Field
import uuid
from datetime import datetime,timezone
from src.bill_pay_game.session.model.session import SessionModel


class WiningRecordModel(Document):
    id:str=Field(default_factory=lambda: str(uuid.uuid4()),alias="_id")
    session:Link[SessionModel]
    wining_player:str
    emoji:str
    description:str
    created_at:datetime=Field(default_factory=lambda: datetime.now(timezone.utc))

    class Settings:
        name = "wining_record"
