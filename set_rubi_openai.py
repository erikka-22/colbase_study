from openai import OpenAI
from openai.types.file_object import FileObject
from dotenv import load_dotenv
load_dotenv()

import time
import pathlib
import os

api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(
  api_key=api_key
)

file = client.files.create(
  file=open("colbase_20240603_test_small.csv", "rb"),
  purpose="assistants"
)

# print(file.model_dump_json(indent=2))

assistant = client.beta.assistants.create(
  name="colbase-rubi-assistant-2024-06-10",
  tools=[{"type": "code_interpreter"}],
  model="gpt-3.5-turbo-16k",
  tool_resources={
    "code_interpreter": {
      "file_ids": [file.id]
    }
  }
)

# print(assistant.model_dump_json(indent=2))

thread = client.beta.threads.create()

# print(thread.model_dump_json(indent=2))

client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content="colbase_20240603_test_small.csvから、「作品名」列の値の読み仮名を「作品名かな」列に入力して、それをcolbase_20240603_test_small_output.csvとして返してください。"
)

messages = client.beta.threads.messages.list(thread_id=thread.id)

# print(messages.model_dump_json(indent=2))

run = client
