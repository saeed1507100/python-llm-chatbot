import requests
import os

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_TOKEN')}"}


def ask_llm(input_text: str):
	payload = {
		"inputs": input_text,
		"parameters": {
			"temperature": 1,
			"return_full_text": False,
        },
		"options": {
			"wait_for_model": True
        }
	}
	response = requests.post(API_URL, headers=headers, json=payload)
	try:
		return response.json()[0]["generated_text"]
	except:
		return response.json()
	

# print(ask_llm("can you give me a one line definition of LLM?"))
