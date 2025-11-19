from http.client import responses
from typing import List

from fastapi import APIRouter,HTTPException,status
from src.bill_pay_game.wining_record.model.wining_record import WiningRecordModel
from src.bill_pay_game.wining_record.schemas.wining_record import WiningRecordCreate,WiningRecordResponse
from src.bill_pay_game.session.model.session import SessionModel


router = APIRouter(
    prefix="/wining_record",
    tags=["Wining Record"]
)



@router.post("/",status_code=status.HTTP_201_CREATED)
async def create_wining_record(wining_record:WiningRecordCreate):
    db_session = await SessionModel.find_one(SessionModel.id == wining_record.session_id)
    if not db_session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")
    new_wining_record = WiningRecordModel(
        session=db_session.model_dump(),
        wining_player= wining_record.wining_player,
        emoji = wining_record.emoji,
        description = wining_record.description,
    )
    await new_wining_record.insert()
    return new_wining_record



@router.get("/", status_code=status.HTTP_200_OK)
async def read_all_wining_records():
    wining_records = await WiningRecordModel.find_all().to_list()
    response = []
    for record in wining_records:
        session = await record.session.fetch()   # <-- fetch linked session
        data = record.model_dump()
        data["session"] = session.model_dump()
        response.append(WiningRecordResponse(**data))
    return response




@router.get("/{session_id}", status_code=status.HTTP_200_OK)
async def read_one_wining_record(session_id: str):
    db_session = await SessionModel.find_one(SessionModel.id == session_id)
    if not db_session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")
    db_wining_player = await WiningRecordModel.find_one(
        WiningRecordModel.session.id == session_id
    )
    if not db_wining_player:
        raise HTTPException(status_code=404, detail="Wining record not found")
    session = await db_wining_player.session.fetch()
    data = db_wining_player.model_dump()
    data["session"] = session.model_dump()
    return WiningRecordResponse(**data)
