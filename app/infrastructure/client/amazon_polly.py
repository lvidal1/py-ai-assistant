import boto3

class amazon_polly:

    def __init__(self, region, access_key_id, secret_access_key):
        self.region = region
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key

        self.client = boto3.client("polly",
                                    region_name=self.region,
                                    aws_access_key_id=self.access_key_id,
                                    aws_secret_access_key=self.secret_access_key)

    def synthesize_speech(self, text, voice_id, output_format):
        """
        Synthesizes speech from the given text.

        Args:
            text (str): The text to be converted to speech.
            voice_id (str): The ID of the voice to use for speech synthesis.
            output_format (str): The format of the output audio.

        Returns:
            A dict containing the audio stream and other information about the response.
        """

        response = self.client.synthesize_speech(
            Text=text,
            VoiceId=voice_id,
            OutputFormat=output_format,
            TextType="text",
            LanguageCode="es-MX"
        )

        return response
