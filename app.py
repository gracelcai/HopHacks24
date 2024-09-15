import pymongo.mongo_client
import streamlit as st
from textblob import TextBlob
import analyzer
import json
import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["trainingdb"]
mycol = mydb["responses"]

def concat_bs(input, msg_json, agree):
  # return f'{{"messages": [{{"role": "user", "content": "{input}"}}, {{"role": "assistant", "content": {{"urgency": {msg_json["urgency"]}, "necessity": {msg_json["necessity"]}, "want": {msg_json["want"]}, "informational": {msg_json["informational"]}, "planning": {msg_json["planning"]}, "career-related": {msg_json["career-related"]}, "notify": {agree == msg_json["notify"]}, "confidence": {msg_json["confidence"]}}}]}}'
  document = {
        "messages": [
            {
                "role": "user",
                "content": input
            },
            {
                "role": "assistant",
                "content": {
                    "urgency": msg_json["urgency"],
                    "necessity": msg_json["necessity"],
                    "want": msg_json["want"],
                    "informational": msg_json["informational"],
                    "planning": msg_json["planning"],
                    "career-related": msg_json["career-related"],
                    "notify": agree == msg_json["notify"],
                    "confidence": msg_json["confidence"]
                }
            }
        ]
    }
  return document
def get_input(option):
  text = st.text_area("Please enter your text")
  st.session_state.text = text

  analyze_button = st.button("Analyze the Sentiment")
  if analyze_button: 
    blob = TextBlob(text)
        
    result = analyzer.get_results(blob, option, data)
      
    message_content = result.choices[0].message.content
    content_trimmed = message_content[7:-3]
    message_json = json.loads(content_trimmed)
    st.session_state.message_json = message_json
    
    st.write(f"Notify: {message_json['notify']}, Confidence: {message_json['confidence']}%")

    for category, definition in data["categories"].items():
      percentage = message_json[f"{category}"]
      st.progress(percentage, text=f"{category}: {percentage}%")
    
    st.session_state.analyzed = True
    
if 'analyzed' not in st.session_state:
  st.session_state.analyzed = False

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
      data = get_input(custom_mode)
else:
  data = get_input(option) 
  
if st.session_state.analyzed:  
  if st.button("Agree"):
    ins_data = concat_bs(st.session_state.text, st.session_state.message_json, True)
    mycol.insert_one(ins_data)
    st.session_state.analyzed = False
    st.rerun()
  
  if st.button("Disagree"):
    ins_data = concat_bs(st.session_state.text,st.session_state.message_json, False)
    mycol.insert_one(ins_data)
    st.session_state.analyzed = False
    st.rerun()