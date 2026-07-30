import streamlit as st

st.title("📂 Upload Excel File")

uploaded_file = st.file_uploader(
    "Choose an Excel file",
    type=["xlsx", "xls"]
)

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")
