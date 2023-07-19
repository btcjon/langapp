import os
from dotenv import load_dotenv
import openai
import cmd
from chains.llm import LLM
from memory.memory import Memory, LongTermMemory

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
        #self.do_chat('')

    def do_chat(self, args):
        if args:
            message = {"role": "user", "content": args}
            self.memory.add_to_short_term(message)
            messages = self.memory.recall()
            response = self.current_llm.chat(messages, long_term_memory=self.long_term_memory)
            self.memory.add_to_short_term({"role": "assistant", "content": response})
        else:
            message = {"role": "system", "content": "You are a helpful assistant."}
            self.memory.add_to_short_term(message)
            messages = self.memory.recall()
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

    def default(self, line):
        self.do_chat(line)

if __name__ == '__main__':
    LangchainCLI().cmdloop()
