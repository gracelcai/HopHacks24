import streamlit as st
from textblob import TextBlob
import analyzer
import json

file = open('defs.json', 'r')
data = json.load(file)

st.title("Text Message Sentiment Analysis") 
st.text("This webapp evaluates whether the receiver of a text message should be notified based on the urgency of the message.")

option = st.selectbox(
     'Select Notification Mode',
     ('Meeting', 'Work', 'Social', 'Available'))

text = st.text_area("Please Enter your text")

if st.button("Analyze the Sentiment"): 
  blob = TextBlob(text) 
  result = analyzer.get_results(blob, option)
  message_content = result.choices[0].message['content']
  # dic = result.choices[0].message.content

  jsonresult = json.loads(message_content)
  st.write(type(jsonresult))
  # for category, definition in data["categories"].items():
    # st.progress(result.choices[0].message.content[0], text=f"{category}")