from fastapi import APIRouter,status,HTTPException
from typing import List
from src.bill_pay_game.session.model.session import SessionModel
from src.bill_pay_game.session.schemas.session import SessionResponse
from src.bill_pay_game.session_group.model.session_group import SessionGroupModel

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


@router.get("/{session_id}", status_code=status.HTTP_200_OK)
async def read_session(session_id: str):
    try:
        db_session = await SessionModel.get(session_id)

        if not db_session:
            raise HTTPException(status_code=404, detail="Session not found")

        db_session_members = await SessionGroupModel.find(
            SessionGroupModel.session.id == session_id
        ).to_list()

        response_members = []
        for member in db_session_members:
            member_dict = member.model_dump(exclude={"session"})
            response_members.append(member_dict)

        return {
            "session": db_session.model_dump(),
            "members": response_members
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching session: {str(e)}")