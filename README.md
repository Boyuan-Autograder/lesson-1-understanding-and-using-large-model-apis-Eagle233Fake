# Lesson 1: Understanding and Using Large Model APIs

- 邀请链接：https://classroom.github.com/a/A-tj83T9

## 要求

- 获得一个 API Key，并且在`.env`文件中将 API Key 添加进去。（推荐使用[硅基流动](https://www.siliconflow.cn/)）

- 补充未完成的`app.py`程序，并且试着运行，看看能否实现流式响应。

- 一切完成之后，使用 Git 提交你的`app.py`。**请不要提交你的`.env`文件！！！**

## 提示

### 提交作业

当你通过邀请链接加入课程后，你会获得一个仓库的链接：

![image.png](https://s2.loli.net/2025/11/17/MRd8ITG9nmrkVEP.png)

进入仓库后，你需要把这个仓库 clone 到本地，并且使用 Git 提交你的代码。

![image.png](https://s2.loli.net/2025/11/17/ahqGguj8le1fHbT.png)

### 配置环境

你需要创建虚拟环境以安装对应的库。

```bash
python -m venv .venv   
source ./.venv/bin/activate  
pip install requests python-dotenv
```

### 参考的 OpenAI API 响应

```json
data: {
  "id": "019a8fdafd091c809cf14705cced6e75",
  "object": "chat.completion.chunk",
  "created": 1763350084,
  "model": "Qwen/Qwen2.5-7B-Instruct",
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "",
        "reasoning_content": null,
        "role": "assistant"
      },
      "finish_reason": null
    }
  ],
  "system_fingerprint": "",
  "usage": {
    "prompt_tokens": 30,
    "completion_tokens": 0,
    "total_tokens": 30
  }
}

data: {
  "id": "019a8fdafd091c809cf14705cced6e75",
  "object": "chat.completion.chunk",
  "created": 1763350084,
  "model": "Qwen/Qwen2.5-7B-Instruct",
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "你好",
        "reasoning_content": null
      },
      "finish_reason": null
    }
  ],
  "system_fingerprint": "",
  "usage": {
    "prompt_tokens": 30,
    "completion_tokens": 1,
    "total_tokens": 31
  }
}

data: {
  "id": "019a8fdafd091c809cf14705cced6e75",
  "object": "chat.completion.chunk",
  "created": 1763350084,
  "model": "Qwen/Qwen2.5-7B-Instruct",
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "！",
        "reasoning_content": null
      },
      "finish_reason": null
    }
  ],
  "system_fingerprint": "",
  "usage": {
    "prompt_tokens": 30,
    "completion_tokens": 2,
    "total_tokens": 32
  }
}

data: {
  "id": "019a8fdafd091c809cf14705cced6e75",
  "object": "chat.completion.chunk",
  "created": 1763350084,
  "model": "Qwen/Qwen2.5-7B-Instruct",
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "有什么",
        "reasoning_content": null
      },
      "finish_reason": null
    }
  ],
  "system_fingerprint": "",
  "usage": {
    "prompt_tokens": 30,
    "completion_tokens": 3,
    "total_tokens": 33
  }
}

data: {
  "id": "019a8fdafd091c809cf14705cced6e75",
  "object": "chat.completion.chunk",
  "created": 1763350084,
  "model": "Qwen/Qwen2.5-7B-Instruct",
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "问题",
        "reasoning_content": null
      },
      "finish_reason": null
    }
  ],
  "system_fingerprint": "",
  "usage": {
    "prompt_tokens": 30,
    "completion_tokens": 4,
    "total_tokens": 34
  }
}

data: {
  "id": "019a8fdafd091c809cf14705cced6e75",
  "object": "chat.completion.chunk",
  "created": 1763350084,
  "model": "Qwen/Qwen2.5-7B-Instruct",
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "或者",
        "reasoning_content": null
      },
      "finish_reason": null
    }
  ],
  "system_fingerprint": "",
  "usage": {
    "prompt_tokens": 30,
    "completion_tokens": 5,
    "total_tokens": 35
  }
}

data: {
  "id": "019a8fdafd091c809cf14705cced6e75",
  "object": "chat.completion.chunk",
  "created": 1763350084,
  "model": "Qwen/Qwen2.5-7B-Instruct",
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "需要",
        "reasoning_content": null
      },
      "finish_reason": null
    }
  ],
  "system_fingerprint": "",
  "usage": {
    "prompt_tokens": 30,
    "completion_tokens": 6,
    "total_tokens": 36
  }
}

data: {
  "id": "019a8fdafd091c809cf14705cced6e75",
  "object": "chat.completion.chunk",
  "created": 1763350084,
  "model": "Qwen/Qwen2.5-7B-Instruct",
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "帮助",
        "reasoning_content": null
      },
      "finish_reason": null
    }
  ],
  "system_fingerprint": "",
  "usage": {
    "prompt_tokens": 30,
    "completion_tokens": 7,
    "total_tokens": 37
  }
}

data: {
  "id": "019a8fdafd091c809cf14705cced6e75",
  "object": "chat.completion.chunk",
  "created": 1763350084,
  "model": "Qwen/Qwen2.5-7B-Instruct",
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "的",
        "reasoning_content": null
      },
      "finish_reason": null
    }
  ],
  "system_fingerprint": "",
  "usage": {
    "prompt_tokens": 30,
    "completion_tokens": 8,
    "total_tokens": 38
  }
}

data: {
  "id": "019a8fdafd091c809cf14705cced6e75",
  "object": "chat.completion.chunk",
  "created": 1763350084,
  "model": "Qwen/Qwen2.5-7B-Instruct",
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "吗",
        "reasoning_content": null
      },
      "finish_reason": null
    }
  ],
  "system_fingerprint": "",
  "usage": {
    "prompt_tokens": 30,
    "completion_tokens": 9,
    "total_tokens": 39
  }
}

data: {
  "id": "019a8fdafd091c809cf14705cced6e75",
  "object": "chat.completion.chunk",
  "created": 1763350084,
  "model": "Qwen/Qwen2.5-7B-Instruct",
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "？",
        "reasoning_content": null
      },
      "finish_reason": null
    }
  ],
  "system_fingerprint": "",
  "usage": {
    "prompt_tokens": 30,
    "completion_tokens": 10,
    "total_tokens": 40
  }
}

data: {
  "id": "019a8fdafd091c809cf14705cced6e75",
  "object": "chat.completion.chunk",
  "created": 1763350084,
  "model": "Qwen/Qwen2.5-7B-Instruct",
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "",
        "reasoning_content": null
      },
      "finish_reason": "stop"
    }
  ],
  "system_fingerprint": "",
  "usage": {
    "prompt_tokens": 30,
    "completion_tokens": 10,
    "total_tokens": 40
  }
}

data: [DONE]

```
