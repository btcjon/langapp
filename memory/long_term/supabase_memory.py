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

    def store(self, user_id, session_id, user_message, ai_response):
        data = {
            "user_id": user_id,
            "session_id": session_id,
            "timestamp": datetime.now(),
            "user_message": user_message,
            "ai_response": ai_response
        }
        self.client.from_("conversations").insert(data)

    def retrieve(self, user_id, session_id):
        query = {"user_id": user_id, "session_id": session_id}
        return self.client.from_("conversations").select().match(query)
