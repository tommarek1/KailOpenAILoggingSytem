import requests
import openai
import os

# Set the API endpoint URL
url = "http://89.203.251.114/KOLS/post-data"

openai.api_key = os.getenv("OPENAI_API_KEY")

def Makerequest(KolsAPIkey, Input, Output, MaxTokens, Model, Temp, TopP, N, Service):
    payload = {
        "token": KolsAPIkey,
        "input": Input,
        "output": Output,
        "max_tokens": MaxTokens,
        "model": Model,
        "temperature": Temp,
        "top_p": TopP,
        "n": N,
        "service": Service,
    }

    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        print(response.text)
    else:
        print("Something went wrong.")

promptAI = "Hello" ##If you want change this with text fiel input
max_tokensAI = "0.6"
temperatureAI = "0.5"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=promptAI,
  max_tokens=max_tokensAI,
  temperature=temperatureAI
)

## 1. Our API token (http://89.203.251.114/get-key) 2. Input (What you put to generate) 3. Output (OpenAI Respond) 4. Max Tokens (How many letter can generate) 5. Model (What model you use to generate) 6. Temperature (How creative will the Response generate) 7. top_p (Don't Required / Leave Black) 8. n (Don't Required / Leave Black) 9. Your service (Discord bot .ec (If you dont want provide your service name type "Unknow"))
Makerequest('Place Our Token Here (http://89.203.251.114/get-key)', promptAI, response.choices[0].text, max_tokensAI, response.model, temperatureAI, "", "", "Discord Bot")