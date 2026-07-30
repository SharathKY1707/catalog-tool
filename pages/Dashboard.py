import streamlit as st

st.set_page_config(page_title="Dashboard", page_icon="📊")

st.title("📊 Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("📦 Total SKU", "15,250")
col2.metric("⏳ Pending", "320")
col3.metric("✅ Completed", "14,900")
col4.metric("❌ Errors", "30")

st.divider()

st.subheader("Progress")

st.progress(92)

st.write("92% of the catalog has been processed.")

st.divider()

st.subheader("Quick Actions")

c1, c2, c3 = st.columns(3)

with c1:
    st.button("📂 Upload File", use_container_width=True)

with c2:
    st.button("✅ Validate", use_container_width=True)

with c3:
    st.button("📤 Generate Output", use_container_width=True)

st.divider()

st.subheader("Validation Summary")

st.write("• Missing Images : 15")
st.write("• Missing Brand : 8")
st.write("• Duplicate SKU : 2")
st.write("• Price Errors : 5")
