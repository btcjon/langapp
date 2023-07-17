import openai

class LLM:
    def __init__(self, model_name):
        self.model_name = model_name

    def execute(self):
        pass

    def chat(self, line):
        response = openai.ChatCompletion.create(
          model=self.model_name,
          messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": line}
            ]
        )
        return response.choices[0].message['content']
