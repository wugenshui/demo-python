from openai import AzureOpenAI

# gets the API Key from environment variable AZURE_OPENAI_API_KEY
client = AzureOpenAI(
  api_key="",
  # https://learn.microsoft.com/en-us/azure/ai-services/openai/reference#rest-api-versioning
  api_version="2023-07-01-preview",
  # https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/create-resource?pivots=web-portal#create-a-resource
  azure_endpoint="",
)

response = client.chat.completions.create(
  model="gpt-35-turbo-16k",  # e.g. gpt-35-instant
  messages=[
    {
      "role": "user",
      "content": "我如何使用发布python服务?",
    },
  ],
  temperature=1
)
print(f"{response.choices[0].message.role}: {response.choices[0].message.content}")