from pydantic import BaseModel
from typing import Optional
from src.bill_pay_game.session.schemas.session import SessionResponse


class SessionGroupBase(BaseModel):
    member_name: str


class SessionGroupCreate(SessionGroupBase):
    pass


class SessionGroupResponse(SessionGroupBase):
    id: str
    session:Optional[SessionResponse]=None
