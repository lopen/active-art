import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

def queryGPT(model, msgs):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=msgs
    )
    return completion.choices[0].message.content