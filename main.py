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

    def do_greet(self, line):
        print("Hello, welcome to Langchain!")

    def do_quit(self, line):
        return True

if __name__ == '__main__':
    LangchainCLI().cmdloop()
