import os
from dotenv import load_dotenv
import pinecone

# Load environment variables from .env file
load_dotenv()

class PineconeStorage:
    def __init__(self, index_name):
        self.api_key = os.getenv("PINECONE_API_KEY")
        self.index_name = index_name
        pinecone.init(api_key=self.api_key)
        if index_name not in pinecone.list_indexes():
            pinecone.create_index(index_name=index_name, metric='cosine')

    def store(self, vectors):
        pinecone.upsert(index_name=self.index_name, items=vectors)

    def retrieve(self, ids):
        return pinecone.fetch(index_name=self.index_name, ids=ids)
