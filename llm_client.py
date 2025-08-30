from google import genai
from google.genai import types
import os

API_KEY = os.getenv("API_KEY", "")
client = genai.Client(api_key= API_KEY)

def get_response(contents, response_schema):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contents,
        config={
            "response_mime_type": "application/json",
            "response_json_schema": response_schema
        },
    )
    print(response.parsed)
    return response.parsed