import openai
from config import settings

openai.api_key = settings.openai_api_key

def generate_script(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a podcast script writer."},
            {"role": "user", "content": f"Generate a podcast script based on: {prompt}"}
        ]
    )
    return response.choices[0].message.content
