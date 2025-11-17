import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()
TOKEN = os.getenv("TOKEN")

def chat_stream(user_text):
    # 如果你是用的是硅基流动，可以直接使用下面的URL
    # url = "https://api.siliconflow.cn/v1/chat/completions"
    url = ____TO BE FILLED____
    payload = {
        "model": "____TO BE FILLED____",
        "messages": [{"role": "user", ____TO BE FILLED____}],
        "stream": ____TO BE FILLED____
    }
    headers = {
        "Authorization": ____TO BE FILLED____,
        "Content-Type": ____TO BE FILLED____
    }

    with requests.____TO BE FILLED____(url, headers=headers, json=payload, stream=____TO BE FILLED____) as r:
        for line in r.iter_lines():
            if not line:
                continue
            decoded = line.decode("utf-8").strip()
            if decoded == ____TO BE FILLED____:
                break
            if decoded.startswith(____TO BE FILLED____):
                try:
                    data_json = json.loads(decoded[len(____TO BE FILLED____):])
                    choices = data_json.get(____TO BE FILLED____, [])
                    for choice in choices:
                        delta = choice.get(____TO BE FILLED____, {})
                        text = delta.get(____TO BE FILLED____)
                        if text:
                            print(text, end="", flush=True)
                except json.JSONDecodeError:
                    continue

if __name__ == "__main__":
    print("SiliconFlow ChatBot")
    while True:
        user_input = input("\n你: ")
        print("AI: ", end="", flush=True)
        chat_stream(user_input)
        print()
