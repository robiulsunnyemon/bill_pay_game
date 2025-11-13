from beanie import Document
from pydantic import Field
import uuid
from datetime import datetime,timezone

class SessionModel(Document):
    id:str=Field(default_factory=lambda: str(uuid.uuid4()),alias="_id")
    session_name: str = Field(default_factory=lambda: f"session_{uuid.uuid4().hex[:8]}")
    created_at:datetime=Field(default_factory=lambda: datetime.now(timezone.utc))

    class Settings:
        name = "session"
