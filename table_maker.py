import streamlit as st
import pandas as pd
import numpy as np


def create():
    df = pd.DataFrame(
    np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))
    return df

