import openai
from typing import List, Dict, Optional
from memory.memory import Memory, LongTermMemory

class LLM:
    def __init__(self, model: str):
        self.model = model

    def chat(self, messages: List[Dict[str, str]], memory: Optional[Memory] = None, long_term_memory: Optional[LongTermMemory] = None):
        if memory is not None:
            messages = memory.recall(messages)
        if long_term_memory is not None:
            messages = long_term_memory.recall(messages)

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            max_tokens=150
        )

        if memory is not None:
            memory.remember(messages, response)
        if long_term_memory is not None:
            long_term_memory.remember(messages, response)

        return response.choices[0].message['content']
