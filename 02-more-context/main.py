import os
from ollama import Client 

OLLAMA_HOST = os.getenv('OLLAMA_HOST')
ollama_client = Client(host=OLLAMA_HOST)

instructions = """You are an expert of the StarTrek universe.
Make only short answers. Speak like a Vulcan
"""

context="""
James Tiberius Kirk is a fictional character in the Star Trek media franchise. 
Kirk was first played by William Shatner as the captain of the USS Enterprise in the Star Trek: The Original Series.

The best friends of James T. Kirk are:
- Spock: The Vulcan science officer of the USS Enterprise.
- Leonard McCoy: The ship's chief medical officer.

Here are some of main adversaries/enemies of James T. Kirk:
- Klingons: The warrior race was often at odds with the Federation and Kirk personally.
- Khan Noonien Singh: A genetically engineered superhuman and Kirk's most famous nemesis.
- Romulans: Another major alien race often in conflict with the Federation.
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
              {'role': 'system', 'content': context},
              {'role': 'user', 'content': user_input},
            ],
            options={"temperature":0.5},
            stream=True,
        )

        for chunk in stream:
          print(chunk['message']['content'], end='', flush=True)

        print("\n")
