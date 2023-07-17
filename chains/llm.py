import openai

class LLM:
    def __init__(self, model_name):
        self.model_name = model_name

    def execute(self):
        pass

    def chat(self, messages):
        messages.insert(0, {"role": "system", "content": "You are a helpful assistant."})
        response = openai.ChatCompletion.create(
          model=self.model_name,
          messages=messages
        )
        return response.choices[0].message['content']
