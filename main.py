import os
from dotenv import load_dotenv
import openai
import cmd
from chains.llm import LLM
from memory.memory import Memory, LongTermMemory
from document_loaders import (
    csv_documents,
    file_directory_documents,
    html_documents,
    markdown_documents,
    pdf_documents,
    xml_documents,
    youtube_transcript_documents,
    youtube_audio_documents,
    web_base_documents,
    url_documents,
    twitter_documents,
    sitemap_documents,
    recursive_url_documents,
)
from text_processing import split_by_token  # Import our text splitting function

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI API with your key
openai.api_key = os.getenv("OPENAI_API_KEY")

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

class LangchainCLI(cmd.Cmd):
    prompt = 'You: '

    def __init__(self):
        self.memory = Memory()
        self.long_term_memory = LongTermMemory()
        super().__init__()
        self.llm_gpt4 = LLM("gpt-4")
        self.llm_gpt35turbo16k = LLM("gpt-3.5-turbo-16k")
        self.llm_gpt35turbo = LLM("gpt-3.5-turbo")
        self.current_llm = self.llm_gpt35turbo
        print("Hello, welcome to Langchain!")
        print("The default language model is gpt-3.5-turbo.")
        print("You can change the language model using the 'select_model' command.")
        print("You can start chatting with the language model using the 'chat' command.")
        print("Type 'help' for more information on commands.")

    def do_chat(self, args):
        if args:
            message = {"role": "user", "content": args}
            self.memory.add_to_short_term(message)
            messages = self.memory.recall()
            if not messages:
                messages = [{"role": "system", "content": "You are a helpful assistant."}]
            response = self.current_llm.chat(messages, long_term_memory=self.long_term_memory)
            self.memory.add_to_short_term({"role": "assistant", "content": response})
        else:
            message = {"role": "system", "content": "You are a helpful assistant."}
            self.memory.add_to_short_term(message)
            messages = self.memory.recall()
            if not messages:
                messages = [{"role": "system", "content": "You are a helpful assistant."}]
            response = self.current_llm.chat(messages, long_term_memory=self.long_term_memory)
            self.memory.add_to_short_term({"role": "assistant", "content": response})
        print(response)

    def do_greet(self, line):
        print("Hello, welcome to Langchain!")

    def do_quit(self, line):
        return True

    def do_select_model(self, line):
        if line == "gpt-4":
            self.current_llm = self.llm_gpt4
        elif line == "gpt-3.5-turbo-16k":
            self.current_llm = self.llm_gpt35turbo16k
        elif line == "gpt-3.5-turbo":
            self.current_llm = self.llm_gpt35turbo
        else:
            print("Invalid model name")

    def do_split_text(self, line):
        args = line.split()
        if len(args) != 2:
            print("Usage: split_text <text> <max_tokens>")
            return
        text, max_tokens = args
        max_tokens = int(max_tokens)
        chunks = split_by_token(text, max_tokens)
        for chunk in chunks:
            print(chunk)

    def default(self, line):
        self.do_chat(line)

if __name__ == '__main__':
    LangchainCLI().cmdloop()
