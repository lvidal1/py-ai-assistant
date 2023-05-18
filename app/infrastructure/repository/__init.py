class TranscriptionRepository:
    def create(self, text: str) -> Transcription:
        transcription = Transcription(text=text)
        db.session.add(transcription)
        db.session.commit()
        return transcription