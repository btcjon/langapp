from supabase_py import create_client, Client
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class SupabaseMemory:
    def __init__(self):
        self.url = os.getenv("SUPABASE_URL")
        self.key = os.getenv("SUPABASE_KEY")
        self.client: Client = create_client(self.url, self.key)

    def store(self, table, data):
        self.client.from_(table).insert(data)

    def retrieve(self, table, query):
        return self.client.from_(table).select().match(query)
