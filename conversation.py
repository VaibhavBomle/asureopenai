import os
from openai import AzureOpenAI
import json


# Define AzureOpenAI Client
client = AzureOpenAI(
    api_version="2024-02-01",
    azure_endpoint="https://practiceazure.openai.azure.com/", # Mention End point of aure openai
    api_key="Mention_API_KEY"
)

completion = client.chat.completions.create(
    model="chat",
    messages=[
        {
            "role": "user",
            "content": "Biggest AI Company in World?",  # Enter question
        }
    ]
)
      
print(completion.to_json())