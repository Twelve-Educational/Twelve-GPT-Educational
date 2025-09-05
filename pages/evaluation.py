# Library imports
import streamlit as st
import pandas as pd
import argparse
import tiktoken
import os
import matplotlib.pyplot as plt
from utils.utils import normalize_text

from classes.data_source import PlayerStats
from classes.data_point import Player
import time
import numpy as np
from classes.visual import DistributionPlot

from utils.page_components import add_common_page_elements


# def show():
sidebar_container = add_common_page_elements()
page_container = st.sidebar.container()
sidebar_container = st.sidebar.container()

st.divider()

# --- Simulated data (replace with your own dataset / entity stats) ---
entity_name = "C_0"
metric = "Stamina"
entity_value = 7.3
cohort = np.random.normal(loc=6.0, scale=1.0, size=100)  # cohort distribution
cohort_median = np.median(cohort)

# --- LLM output (this would be generated under different arms) ---
llm_output = """The candidate is highly outgoing and energetic, exhibiting a strong tendency to engage socially, often taking the initiative to start conversations. While they are friendly and compassionate, they also display sensitivity and nervousness, leading them to experience more negative emotions and anxiety at times.
The candidate is very efficient and organized, demonstrating careful attention to detail and a diligent approach to their tasks. They are relatively consistent and cautious in their actions but tend to be less open to new ideas and experiences, favoring familiar routines over novelty."""

# --- Survey state ---
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

st.title("Output Evaluation Demo")



# 2. Show the ground truth plot for raters to compare
st.subheader(f"Ground Truth Reference for {entity_name}")
# embed picture
st.image("data/ressources/img/eval-demo.png", caption="Ground Truth Distribution (placeholder image)", use_column_width=True)



# 1. Show the generated text
st.subheader("LLM Generated Description")
st.write(llm_output)

# 3. Ask evaluation questions
st.subheader("Evaluation Questions")

faithfulness = st.slider("How faithful is the text to the ground truth?", 1, 7, 4)
clarity = st.slider("How clear/readable is the text?", 1, 7, 4)
trust = st.slider("How trustworthy/useful is the text?", 1, 7, 4)

hallucination = st.radio("Does the text contain hallucinations (unsupported claims)?", ["No", "Yes"])
comment = st.text_area("Optional comments:")

# 4. Save response + response time
if st.button("Submit and Continue"):
    response_time = time.time() - st.session_state.start_time
    st.session_state.start_time = time.time()

    st.success("Response submitted! ✅")
    st.write({
        "entity": entity_name,
        "metric": metric,
        "faithfulness": faithfulness,
        "clarity": clarity,
        "trust": trust,
        "hallucination": hallucination,
        "comment": comment,
        "response_time_sec": round(response_time, 2),
    })
