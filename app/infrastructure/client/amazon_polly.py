import boto3

class amazon_polly:

    def __init__(self, region, access_key_id, secret_access_key, language_code="es-MX"):
        self.region = region
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key
        self.language_code = language_code

        self.client = boto3.client("polly",
                                    region_name=self.region,
                                    aws_access_key_id=self.access_key_id,
                                    aws_secret_access_key=self.secret_access_key)

    def synthesize_speech(self, text, voice_id, output_format):
        response = self.client.synthesize_speech(
            Text=text,
            VoiceId=voice_id,
            OutputFormat=output_format,
            TextType="text",
            LanguageCode=self.language_code
        )

        return response
