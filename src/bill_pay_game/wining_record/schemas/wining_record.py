from pydantic import BaseModel
from datetime import datetime,timezone

from bill_pay_game.session.schemas.session import SessionResponse
from typing import Optional

class WiningRecordBase(BaseModel):
    wining_player:str
    emoji:str
    description:str


class WiningRecordCreate(WiningRecordBase):
    session_id:str


class WiningRecordResponse(WiningRecordBase):
    id: str
    session:Optional[SessionResponse]=None
    created_at:datetime