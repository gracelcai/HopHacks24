import streamlit as st
from textblob import TextBlob
import analyzer
import json
import pymongo

def get_opinion_data(input, msg_json):
  col1, col2, col3, col4 = st.columns([0.65, 1, 1, 3])

  with col1:
    if st.button('Agree'):
      print("TEST SFJLSDFKSF")
      st.write("poop")
      print(concat_bs(input, msg_json, True))
  with col2:
    if st.button('Disagree'):
      print(concat_bs(input, msg_json, False))

def does_a_brotha_agree(agree, notify):
  if agree:
    notify
  else:
    not notify

def concat_bs(input, msg_json, agree):
  return f'{{"messages": [{{"role": "user", "content": "{input}"}}, {{"role": "assistant", "content": {{"urgency": {msg_json["urgency"]}, "necessity": {msg_json["necessity"]}, "want": {msg_json["want"]}, "informational": {msg_json["informational"]}, "planning": {msg_json["planning"]}, "career-related": {msg_json["career-related"]}, "notify": {does_a_brotha_agree(agree, msg_json["notify"])}, "confidence": {msg_json["confidence"]}}}]}}'

def get_input(option):
  text = st.text_area("Please enter your text")

  if st.button("Analyze the Sentiment"): 
    blob = TextBlob(text) 
      
    result = analyzer.get_results(blob, option, data)
      
    message_content = result.choices[0].message.content
    content_trimmed = message_content[7:-3]
    message_json = json.loads(content_trimmed)
    st.write(message_json)
    st.write(f"Notify: {message_json['notify']}, Confidence: {message_json['confidence']}%")

    for category, definition in data["categories"].items():
      percentage = message_json[f"{category}"]
      st.progress(percentage, text=f"{category}: {percentage}%")
      
    get_opinion_data(blob, message_json)

file = open('defs.json', 'r')
data = json.load(file)

st.title("Text Message Sentiment Analysis") 
st.text("This webapp evaluates whether the receiver of a text message should be notified\nbased on the urgency of the message and their conditions.")

option = st.selectbox(
     'Select Notification Mode',
     ('Meeting', 'Work', 'Social', 'Available', 'Custom'))

if (option == 'Custom'):
  custom_mode = st.text_input("Enter custom mode name")
  if (custom_mode != ''):
    custom_mode_def = st.text_input(f"Enter {custom_mode} mode guidlines")
    if (custom_mode_def != ''):
      new = {custom_mode: custom_mode_def}
      data["modes"].update(new)
      get_input(custom_mode)
else:
  get_input(option)