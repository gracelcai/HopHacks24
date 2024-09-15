from openai import OpenAI
from dotenv import load_dotenv
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

client.fine_tuning.jobs.create(
  training_file="file-Ekp1tFJpudXMaSqddBKpskND", 
  model="gpt-4o-mini-2024-07-18"
)