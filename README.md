# python-llm-chatbot
A simple chatbot web-app in Python using LLM

# Deploy locally

## 1. Add Environment variable
Add a .env file with hugging face api key like:
```
HUGGINGFACEHUB_API_TOKEN = "hf_...."
```
to get your own hugging face hub api key, follow the instructions at: [get-your-api-token](https://huggingface.co/docs/api-inference/en/quicktour#get-your-api-token)

## 2. Install requirements
```
pip install -r requirements.txt
```

## 3. Run the app with streamlit
```
streamlit run app.py
```

# Demo of the app

[python-llm-chatbot](https://python-llm-chatbot.streamlit.app/)
