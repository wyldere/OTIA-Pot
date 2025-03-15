from openai import OpenAI
import openai
openai.api_key = "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"
client = openai.OpenAI(api_key=openai.api_key)

response = client.responses.create(
    model="gpt-4o",
    input = "is this a piece of trash"
)

print(response.output_text)