import streamlit as st
from textblob import TextBlob
import analyzer
import json

def get_input(option):
  text = st.text_area("Please enter your text")

  if st.button("Analyze the Sentiment"): 
    blob = TextBlob(text) 
      
    result = analyzer.get_results(blob, option, data)
      
    message_content = result.choices[0].message.content
    content_trimmed = message_content[7:-3]
    message_json = json.loads(content_trimmed)
    
    st.write(f"Notify: {message_json['notify']}, Confidence: {message_json['confidence']}%")

    for category, definition in data["categories"].items():
      percentage = message_json[f"{category}"]
      st.progress(percentage, text=f"{category}: {percentage}%")

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