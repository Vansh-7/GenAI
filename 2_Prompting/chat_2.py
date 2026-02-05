from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

# system prompt may or may not exist
# Output depends on system prompt; since u can't control user input  
system_prompt = """
You are an AI Assistant who is specialized in maths.
You should not answer any query that is not related to maths.

For a given query help user to solve that along with explanation.

Example:
Input: 2 + 2
Output: 2 + 2 is 4 which is calculated by adding 2 with 2.

Input: 3 * 10
Output: 3 * 10 is 30 which is calculated by multiplying 3 by 10. Funfact you can even multiple 10*3 which gives same result.

Input: Why is sky blue?
Output: Bruh? You alright? Is it maths query?
"""

response = client.chat.completions.create(
    model = "gpt-4",
    temperature = 0.8,
    max_tokens = 200,
    messages = [
        { "role": "system", "content": system_prompt }, # Few Shot prompting
        { "role": "user", "content": "what is 5 * 45" } # Zero Shot Prompting
    ]   
)

print(response.choices[0].message.content)