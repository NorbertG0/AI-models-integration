import anthropic

def claude_prompt(prompt, api_key):
    client = anthropic.Anthropic(api_key=api_key)

    message = client.messages.create(
      model="claude-opus-4-8",
      max_tokens=1024,
      messages=[{
        "role": "user",
        "content": prompt
      }]
    )

    return message.content[0].text