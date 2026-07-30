import streamlit as st

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")

st.title("📊 Catalog Dashboard")

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("📦 Total SKU", "0")
col2.metric("✅ Completed", "0")
col3.metric("⏳ Pending", "0")
col4.metric("❌ Errors", "0")

st.divider()

left, right = st.columns([2,1])

with left:
    st.subheader("📈 Processing Progress")
    st.progress(0)

    st.subheader("📂 Recent Uploads")

    st.info("No files uploaded yet.")

with right:
    st.subheader("⚠ Validation Summary")

    st.write("Missing Images : 0")
    st.write("Missing Brand : 0")
    st.write("Duplicate SKU : 0")
    st.write("Price Errors : 0")

st.divider()

st.subheader("🚀 Quick Actions")

c1,c2,c3,c4 = st.columns(4)

c1.button("📂 Upload")
c2.button("✅ Validate")
c3.button("🔄 Mapping")
c4.button("📤 Output")
