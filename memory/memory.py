import os
from dotenv import load_dotenv
from supabase_py import create_client, Client
from typing import List, Dict

# Load environment variables from .env file
load_dotenv()

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

class Memory:
    def __init__(self):
        self.short_term_memory = []

    def add_to_short_term(self, message: Dict[str, str]) -> None:
        self.short_term_memory.append(message)
        if len(self.short_term_memory) > 5:
            self.short_term_memory.pop(0)

    def recall(self, messages: List[Dict[str, str]]) -> List[Dict[str, str]]:
        return self.short_term_memory + messages

class LongTermMemory(Memory):
    def __init__(self):
        super().__init__()
        self.supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    def recall(self, messages: List[Dict[str, str]]) -> List[Dict[str, str]]:
        result = self.supabase.table('documents').select().execute()
        if result.get('error') is None and result.get('data') is not None:
            messages.extend(result.get('data'))
        return messages
