import openai
from typing import List, Dict, Optional
from memory.memory import Memory, LongTermMemory

class LLM:
    def __init__(self, model: str):
        self.model = model

    def chat(self, messages: List[Dict[str, str]], long_term_memory: LongTermMemory = None) -> str:
        if not messages:
            messages = [{"role": "system", "content": "You are a helpful assistant."}]
        if long_term_memory is not None:
            long_term_memory_messages = long_term_memory.recall()
            if long_term_memory_messages:
                messages.extend(long_term_memory_messages)
        print(f"Messages before API call: {messages}")
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            max_tokens=150
        )
        print(f"Response from API: {response}")
        return response.choices[0].message['content']


