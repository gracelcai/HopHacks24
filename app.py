import streamlit as st
from textblob import TextBlob
import analyzer
import json

file = open('defs.json', 'r')
data = json.load(file)

st.title("Text Message Sentiment Analysis") 
st.text("This webapp evaluates whether the receiver of a text message should be notified\nbased on the urgency of the message and their conditions.")

option = st.selectbox(
     'Select Notification Mode',
     ('Meeting', 'Work', 'Social', 'Available'))

text = st.text_area("Please enter your text")

if st.button("Analyze the Sentiment"): 
  blob = TextBlob(text) 
  result = analyzer.get_results(blob, option)
    
  message_content = result.choices[0].message.content
  message_json = json.loads(message_content)
  
  st.write(f"Notify: {message_json['notify']}, Confidence: {message_json['confidence']}%")

  for category, definition in data["categories"].items():
    percentage = message_json[f"{category}"]
    st.progress(percentage, text=f"{category}: {percentage}%")