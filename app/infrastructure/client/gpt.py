from app.infrastructure.service.openai import OpenAI


class gpt:
    def __init__(self):
        self.service = OpenAI()

    def prompt(self, text):
        try:
            chat_completion = self.service.client().ChatCompletion.create(
                model="gpt-3.5-turbo", messages=[{"role": "user", "content": text}]
            )

            return chat_completion.choices[0].message.content

        except Exception as e:
            print(e)
            return "Error"
