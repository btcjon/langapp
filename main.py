import os
from dotenv import load_dotenv
import openai
import cmd

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI API with your key
openai.api_key = os.getenv("OPENAI_KEY")

class LangchainCLI(cmd.Cmd):
    prompt = 'langchain> '

    def __init__(self):
        super().__init__()
        self.llm_gpt4 = LLM("gpt-4")
        self.llm_gpt35turbo16k = LLM("gpt-3.5-turbo-16k")
        self.llm_gpt35turbo = LLM("gpt-3.5-turbo")
        self.current_llm = self.llm_gpt4

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

if __name__ == '__main__':
    LangchainCLI().cmdloop()
