from openai import OpenAI
from dotenv import load_dotenv
import json
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

# Use for updating fine-tuning data
# client.files.create(
#   file=open("file-data.jsonl", "rb"),
#   purpose="fine-tune"
# )

client.fine_tuning.jobs.create(
  training_file="file-NKZnnY5PgxPONSOt1NSFjcnY", 
  model="gpt-4o-mini-2024-07-18"
)

def get_results(text, option):
    messages = [{"role": "system", "content": f"You are a helpful assistant that evaluates text messages based on categories to decide whether the receiver should be notified. "}]
    messages.append({"role": "user", "content": f"Given the following text message: \"{text}\", give percentages for each of the following grading categories below:"})
    
    file = open('defs.json', 'r')
    data = json.load(file)
    for category, definition in data["categories"].items():
        messages.append({"role": "user", "content": f"{category}: {definition}"})
    
    defn = data["modes"][option]
    messages.append({"role": "user", "content": f"With those percentages, should a user in mode: \"{option}\" ({defn}) be notified? return only a json file with each grading category and their respective percentages and also yes or no and its confidence"})
        
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    print(completion)
    return completion
