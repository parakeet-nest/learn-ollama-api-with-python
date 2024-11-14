import os
from ollama import Client 

OLLAMA_HOST = os.getenv('OLLAMA_HOST')
ollama_client = Client(host=OLLAMA_HOST)

instructions = """You are an expert of the StarTrek universe.
Make only short answers. Speak like a Vulcan
"""

while True:
    user_input = input("🤖 (type 'bye' to exit):> ")
    if user_input.lower() == "bye":
        print("👋 Goodbye!")
        break
    else:
        stream = ollama_client.chat(
            model='granite3-moe:1b',
            messages=[
              {'role': 'system', 'content': instructions},
              {'role': 'user', 'content': user_input},
            ],
            options={"temperature":0.5},
            stream=True,
        )

        for chunk in stream:
          print(chunk['message']['content'], end='', flush=True)

        print("\n")
