from PIL import Image
from io import BytesIO
import requests
from google import genai
from google.genai.types import GenerateContentConfig, ThinkingConfig
from prompts import *

def fixSolutionString(solutionString):

    # Initialize empty result string
    opsLs = ['+', '-', '*', '=', '/']
    varsLs = ['x','(',')']
    result = ""
    i = 0

    # Replace multiplication asterisk with dot
    solutionString = solutionString.replace('*', '·')
    
    while i < len(solutionString):
        result += solutionString[i]
        
        # Check if current char is digit and not last char
        if i < len(solutionString)-1 and solutionString[i].isdigit():
            next_char = solutionString[i+1]
            # If next char is not digit or decimal point, add space
            if not next_char.isdigit() and next_char != '.':
                # Remove * between digit and non-digit
                if next_char == '·':
                    i += 1
                    continue
                # Add space if not operator or variable
                if next_char not in opsLs and next_char not in varsLs:
                    result += ' '
        i += 1

    # Replace underscores with spaces
    result = result.replace('_', ' ')
    # Replace double spaces with single space until no more double spaces exist
    while '  ' in result:
        result = result.replace('  ', ' ')
        
    return result

def getSolutionString(problemImageUrl, prompt):

    input = [prompt]
    if problemImageUrl != 'missing':
            image_data = requests.get(problemImageUrl).content
            image = Image.open(BytesIO(image_data))
            input.append(image)

    client = genai.Client(api_key='X')

    response = client.models.generate_content(
    model='gemini-2.5-pro',
    contents=input,
    config=GenerateContentConfig(
        thinking_config=ThinkingConfig(
            thinking_budget=200
        )
    )
    )

    # Extract the classification from the response
    output = response.candidates[0].content.parts[0].text
    output = fixSolutionString(output)

    return output