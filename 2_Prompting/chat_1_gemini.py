from google import genai
from google.genai import types

client = genai.Client(api_key="AIzaSyAgIL6rmVOGM9gM-nQlFcLehMb7IlyHaFc")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="How does AI work?",
)

print(response.text)