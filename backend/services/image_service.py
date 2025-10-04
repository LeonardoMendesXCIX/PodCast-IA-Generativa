import openai
from config import settings

openai.api_key = settings.openai_api_key

def generate_image(prompt: str) -> str:
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    return response['data'][0]['url']
