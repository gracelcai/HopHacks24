import streamlit as st
from textblob import TextBlob
import analyzer
import json

def get_opinion_data():
  col1, col2, col3, col4 = st.columns([0.65, 1, 1, 3])

  with col1:
    if st.button('Agree'):
      pass
  with col2:
    if st.button('Disagree'):
      pass
  
def get_input(option):
  text = st.text_area("Please enter your text")

  if st.button("Analyze the Sentiment"): 
    blob = TextBlob(text) 
      
    result = analyzer.get_results(blob, option, data)
      
    message_content = result.choices[0].message.content
    message_json = json.loads(message_content)
    
    st.write(f"Notify: {message_json['notify']}, Confidence: {message_json['confidence']}%")

    for category, definition in data["categories"].items():
      percentage = message_json[f"{category}"]
      st.progress(percentage, text=f"{category}: {percentage}%")
      
    get_opinion_data()

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