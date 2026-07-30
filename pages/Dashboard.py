import streamlit as st

st.title("📊 Dashboard")

st.write("Welcome to the Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total SKU", "0")
col2.metric("Pending", "0")
col3.metric("Completed", "0")
col4.metric("Errors", "0")

st.divider()

st.subheader("Quick Actions")

if st.button("📂 Upload Excel"):
    st.write("Upload page will be added soon.")

if st.button("✅ Validate Data"):
    st.write("Validation page will be added soon.")

if st.button("📤 Generate Output"):
    st.write("Output page will be added soon.")
