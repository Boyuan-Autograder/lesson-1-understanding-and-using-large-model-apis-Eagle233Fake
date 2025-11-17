import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()
TOKEN = os.getenv("TOKEN")

def chat_stream(user_text):
    # 如果你是用的是硅基流动，可以直接使用下面的URL
    # url = "https://api.siliconflow.cn/v1/chat/completions"
    url = FILLED
    payload = {
        "model": "FILLED",
        "messages": [{"role": "user", FILLED}],
        "stream": FILLED
    }
    headers = {
        "Authorization": FILLED,
        "Content-Type": FILLED
    }

    with requests.FILLED(url, headers=headers, json=payload, stream=FILLED) as r:
        for line in r.iter_lines():
            if not line:
                continue
            decoded = line.decode("utf-8").strip()
            if decoded == FILLED:
                break
            if decoded.startswith(FILLED):
                try:
                    data_json = json.loads(decoded[len(FILLED):])
                    choices = data_json.get(FILLED, [])
                    for choice in choices:
                        delta = choice.get(FILLED, {})
                        text = delta.get(FILLED)
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
