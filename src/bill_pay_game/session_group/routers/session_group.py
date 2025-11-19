from fastapi import APIRouter,status,HTTPException
from typing import List
from src.bill_pay_game.session_group.model.session_group import SessionGroupModel
from src.bill_pay_game.session_group.schemas.session_group import SessionGroupCreate, SessionGroupResponse
from src.bill_pay_game.session.model.session import SessionModel


router = APIRouter(prefix="/session_group", tags=["Session Group"])

@router.get("/", response_model=List[SessionGroupResponse],status_code=status.HTTP_200_OK)
async def session_group_list():
    session_groups = await SessionGroupModel.find_all().to_list()
    for sg in session_groups:
        sg.session = await sg.session.fetch()
    return session_groups


@router.post("/{session_id}", response_model=SessionGroupResponse,status_code=status.HTTP_201_CREATED)
async def session_group_create(session_id:str,session_group: SessionGroupCreate):
    db_session = await SessionModel.find_one(SessionModel.id == session_id)
    if not db_session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")
    new_session_group = SessionGroupModel(
        session=db_session.model_dump(),
        member_name=session_group.member_name,
    )
    await new_session_group.insert()
    return new_session_group
