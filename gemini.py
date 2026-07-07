from google import genai

def gemini_prompt(prompt, api_key):
    client = genai.Client(api_key=api_key)

    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input=prompt
    )

    return interaction.output_text

