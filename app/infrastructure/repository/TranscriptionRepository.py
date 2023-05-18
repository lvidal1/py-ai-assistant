from app.infrastructure.entity import Transcription
from app.infrastructure.database import db

class TranscriptionRepository:
    def create(self, text: str) -> Transcription:
        transcription = Transcription(text=text)
        db.session.add(transcription)
        db.session.commit()
        return transcription