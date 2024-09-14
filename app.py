import streamlit as st
from textblob import TextBlob
import analyzer

st.title("Text Message Sentiment Analysis") 
st.text("This webapp evaluates whether the receiver of a text message should be notified based on the urgency of the message.")

option = st.selectbox(
     'Select Notification Mode',
     ('Meeting', 'Work', 'Social', 'Available'))

text = st.text_area("Please Enter your text")

if st.button("Analyze the Sentiment"): 
  blob = TextBlob(text) 
  result = analyzer.get_results(blob, option)
  st.write(result)