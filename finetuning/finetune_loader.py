from openai import OpenAI
from dotenv import load_dotenv
import json
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

# Use for updating fine-tuning data
client.files.create(
  file=open("finetuning/finetuning-data.jsonl", "rb"),
  purpose="fine-tune"
)