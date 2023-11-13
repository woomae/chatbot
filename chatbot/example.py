import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],
)
response = client.completions.create(
    model="text-davinci-003",
    prompt="안녕. 내 이름은 조형근이야. \n\nQ: 이름이 뭘까?\nA:",
    temperature=0.1,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n"]
)

print(response)

print(response.choices[0].text.strip())