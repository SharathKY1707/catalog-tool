import streamlit as st
import pandas as pd

st.set_page_config(page_title="Upload", page_icon="📂", layout="wide")

st.title("📂 Upload Excel")

uploaded_file = st.file_uploader(
    "Choose an Excel file",
    type=["xlsx", "xls"]
)

if uploaded_file:

    df = pd.read_excel(uploaded_file)

    st.success("File uploaded successfully!")

    col1,col2,col3 = st.columns(3)

    col1.metric("Rows", len(df))
    col2.metric("Columns", len(df.columns))
    col3.metric("Missing Values", int(df.isna().sum().sum()))

    st.divider()

    st.subheader("Column Names")

    st.write(df.columns.tolist())

    st.divider()

    st.subheader("Preview")

    st.dataframe(df, use_container_width=True)
