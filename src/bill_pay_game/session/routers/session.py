from fastapi import APIRouter,status
from typing import List
from src.bill_pay_game.session.model.session import SessionModel
from src.bill_pay_game.session.schemas.session import SessionResponse

router = APIRouter(prefix="/session", tags=["Session"])
@router.post("/", response_model=SessionResponse, status_code=status.HTTP_201_CREATED)
async def create_session():
    new_session= SessionModel()
    await new_session.insert()
    return new_session


@router.get("/", response_model=List[SessionResponse], status_code=status.HTTP_200_OK)
async def read_session():
    db_sessions = await SessionModel.find_all().to_list()
    return db_sessions





