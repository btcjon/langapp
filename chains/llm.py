import openai

class LLM:
    def __init__(self, model_name):
        self.model_name = model_name

    def execute(self):
        pass

    def chat(self, messages):
        self.memory.store(messages[0]["role"], messages[0]["content"])
        messages = self.memory.retrieve()
        messages.insert(0, {"role": "system", "content": "You are a helpful assistant."})
        response = openai.ChatCompletion.create(
          model=self.model_name,
          messages=messages
        )
        self.memory.store("ai", response.choices[0].message['content'])
        return response.choices[0].message['content']
