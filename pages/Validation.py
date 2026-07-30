import streamlit as st
import pandas as pd

from utils.validator import validate

st.title("Validation")

uploaded = st.file_uploader("Upload Excel")

if uploaded:

    df = pd.read_excel(uploaded)

    error_df = validate(df)

    st.metric("Total Errors", len(error_df))

    st.dataframe(error_df, use_container_width=True)
