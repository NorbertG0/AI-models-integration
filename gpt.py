from openai import OpenAI

def openai_prompt(prompt, api_key):
    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model="gpt-5.5",
        input=prompt
    )

    return response.text
