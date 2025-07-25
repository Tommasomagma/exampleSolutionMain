from PIL import Image
from io import BytesIO
import requests
from google import genai
from google.genai.types import GenerateContentConfig, ThinkingConfig
from prompts import *

def getNewProblem(problemImageUrl, prompt):

    input = [prompt]
    if problemImageUrl != 'missing':
        image_data = requests.get(problemImageUrl).content
        image = Image.open(BytesIO(image_data))
        input.append(image)

    client = genai.Client(api_key='AIzaSyCr_T8Zowta35sZ7b82XdycAERZvPosN7o')

    response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=input,
    config=GenerateContentConfig(
        thinking_config=ThinkingConfig(
            thinking_budget=200
        )
    )
    )

    # Extract the classification from the response
    output = response.candidates[0].content.parts[0].text

    return output