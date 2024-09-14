from openai import OpenAI
import os
import json
from trying_random_bs import *

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def load_messages():
    messages = [{"role": "system", "content": "You are a helpful assistant that evaluates text messages based on several categories to decide whether the receiver should be notified about it or not."}]
    with open('defs.json', 'r') as file:
        data = json.load(file)
        for word, definition in data["categories"].items():
            messages.append({"role": "user", "content": "Here is the definition for texts that fall under the category of {word}: {definition}"})
        for word, definition in data["modes"].items():
            messages.append({"role": "user", "content": "Here is the definition for the mode {word}: {definition}"})
    return messages

def get_results(text, option):
    messages = load_messages()
    data = json.load(open('defs.json', 'r'))
    definition = data["modes"][option]
    messages.append({"role": "user", "content": "Here is the text message to be analyzed: {text}. The user is currently in mode {option}, which means {definition}"})
    messages.append({"role": "user", "content": prompt})
    print(messages)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    return completion
