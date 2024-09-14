# Python In-built packages
from pathlib import Path
import PIL

# External packages
import streamlit as st

# Local Modules
import settings
import helper
import table_maker

# Setting page layout
st.set_page_config(
    page_title="Object Detection using YOLOv8",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page heading
st.title("Surgical Tools Detector")
# Sidebar
st.sidebar.header("Video Selector")
confidence = 0.95

model_path = Path(settings.DETECTION_MODEL)

# Load Pre-trained ML Model
try:
    model = helper.load_model(model_path)
except Exception as ex:
    st.error(f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)


# st.sidebar.header("Image/Video Config")
# source_radio = st.sidebar.radio(
#     "Select Source", settings.SOURCES_LIST)

col1, col2 = st.columns([2,1])
with col1:
    helper.play_stored_video(confidence, model)

with col2:
    st.table(table_maker.create())