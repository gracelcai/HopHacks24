import streamlit as st
import pandas as pd
import numpy as np

def create(res):
    res = pd.read_json("example.json")
    classes = []
    for prediction in res["predictions"]:
        classes.append(prediction["class"])
    df = pd.DataFrame(classes)
    return df

# print(create(pd.read_json("example.json")))