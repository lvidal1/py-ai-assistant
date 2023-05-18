from flask import Blueprint, request
import os

from app.infrastructure.client.amazon_polly import amazon_polly

transcription_router = Blueprint('transcription',__name__)

@transcription_router.route('/speech-to-text', methods=["POST"])
def speech_to_text():
  bodyText = request.get_json()["text"];



  # Create a Polly client.
  polly_client = amazon_polly(
      region=os.environ.get('AWS_REGION'),
      access_key_id=os.environ.get('AWS_ACCESS_KEY'),
      secret_access_key=os.environ.get('AWS_SECRET_KEY')
  )

  response = polly_client.synthesize_speech(
    text=bodyText,
    voice_id="Mia",
    output_format="mp3"
  )

  audio_stream = response["AudioStream"]

  return audio_stream