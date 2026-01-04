from openai import AzureOpenAI
import os

from dotenv import load_dotenv
load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# def ask_mobility_ai(prompt: str):
#     response = client.chat.completions.create(
#         model="gpt-35-turbo",
#         messages=[
#             {"role": "system", "content": "You are a global mobility expert."},
#             {"role": "user", "content": prompt}
#         ]
#     )
#     return response.choices[0].message.content


def ask_mobility_ai(prompt: str, temperature: float = 0.7):
    response = client.chat.completions.create(
        model="gpt-35-turbo",
        temperature=temperature,
        messages=[
            {"role": "system", "content": "You are a global mobility expert."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
