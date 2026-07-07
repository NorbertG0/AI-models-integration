from xai_sdk import Client
from xai_sdk.chat import user

def grok_prompt(prompt, api_key):

    client = Client(api_key=api_key)
    chat = client.chat.create(model="grok-4.3")
    chat.append(user(prompt))

    return chat.sample().content
