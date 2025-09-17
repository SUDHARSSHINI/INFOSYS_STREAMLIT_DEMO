# app.py

import streamlit as st
import pandas as pd
import numpy as np

# -------------------------------
# 1. Title and Description
# -------------------------------
st.set_page_config(page_title="Streamlit Demo", layout="wide")

st.title("🚀 Streamlit Demo App")
st.subheader("A quick showcase of what Streamlit can do")
st.write("Streamlit lets you build interactive web apps in pure Python!")

# -------------------------------
# 2. Sidebar for inputs
# -------------------------------
st.sidebar.header("🔧 Controls")
user_name = st.sidebar.text_input("Enter your name:", "Friend")
number = st.sidebar.slider("Pick a number:", 1, 100, 42)

st.sidebar.write("✅ You picked:", number)

# -------------------------------
# 3. Main content
# -------------------------------
st.write(f"👋 Hello **{user_name}**! Welcome to the Streamlit demo.")

# Example DataFrame
st.subheader("📊 Random Data Table")
data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=["Column A", "Column B", "Column C"]
)
st.dataframe(data)

# -------------------------------
# 4. Charts
# -------------------------------
st.subheader("📈 Line Chart")
st.line_chart(data)

st.subheader("📉 Area Chart")
st.area_chart(data)

# -------------------------------
# 5. Layout example (columns)
# -------------------------------
st.subheader("🖼️ Layout with Columns")
col1, col2 = st.columns(2)

with col1:
    st.write("This is the left column")
    st.bar_chart(data)

with col2:
    st.write("This is the right column (map)")
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [12.97, 77.59],  # random points near Bangalore
        columns=["lat", "lon"]  # ✅ must name columns lat/lon
    )
    st.map(map_data)

# -------------------------------
# 6. Button example
# -------------------------------
if st.button("Click Me!"):
    st.success("🎉 You clicked the button!")

# -------------------------------
# 7. Footer
# -------------------------------
st.write("---")
st.caption("Made with ❤️ using Streamlit")
