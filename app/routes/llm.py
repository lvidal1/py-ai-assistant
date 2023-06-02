from flask import Blueprint, request
from app.infrastructure.client.bard import bard
from app.infrastructure.client.amazon_polly import amazon_polly
import os

llm_router = Blueprint("llm", __name__)


@llm_router.route("/bard", methods=["POST"])
def bard_llm():
    try:
        body = request.get_json()

        text = body["text"]

        speak = body.get("speak", False)

        bard_client = bard(api_key=os.environ.get("BARD_API_KEY"))

        response = bard_client.prompt(f"""Max 10 words: '{text}' """)

        if response == "Error":
            return "Error connecting to Bard service", 500

        if speak:
            polly_client = amazon_polly(
                region=os.environ.get("AWS_REGION"),
                access_key_id=os.environ.get("AWS_ACCESS_KEY"),
                secret_access_key=os.environ.get("AWS_SECRET_KEY"),
                language_code="en-US",
            )

            response = polly_client.synthesize_speech(
                text=response, voice_id="Salli", output_format="mp3"
            )

            return response["AudioStream"]

        else:
            return response

    except Exception:
        return "Error connecting to service", 500
