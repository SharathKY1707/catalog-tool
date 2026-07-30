import streamlit as st

st.set_page_config(
    page_title="Catalog Tool",
    page_icon="📦",
    layout="wide"
)

st.title("📦 Catalog Management Tool")

st.write("Welcome to your first Streamlit application!")

st.header("Features")
st.checkbox("Upload Excel File")
st.checkbox("Validate Data")
st.checkbox("Generate Marketplace Output")
st.checkbox("Download Final File")

st.success("Your app is running successfully!")
