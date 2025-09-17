# streamlit_demo.py

import streamlit as st
import pandas as pd
import numpy as np

# -------------------------------
# 1. Page Configuration
# -------------------------------
st.set_page_config(page_title="Streamlit Demo", layout="wide")

# -------------------------------
# 2. Title and Description
# -------------------------------
st.title("🚀 Streamlit Demo App")
st.subheader("A quick showcase of what Streamlit can do")
st.write("Streamlit lets you build interactive web apps in pure Python!")

# -------------------------------
# 3. Sidebar for Inputs
# -------------------------------
st.sidebar.header("🔧 Controls")
user_name = st.sidebar.text_input("Enter your name:", "Friend")
number = st.sidebar.slider("Pick a number:", 1, 100, 42)

st.sidebar.write("✅ You picked:", number)

# -------------------------------
# 4. Main Content
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
# 5. Charts
# -------------------------------
st.subheader("📈 Line Chart")
st.line_chart(data)

st.subheader("📉 Area Chart")
st.area_chart(data)

# -------------------------------
# 6. Layout Example (Columns)
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
        columns=["lat", "lon"]  # ✅ required column names
    )
    st.map(map_data)

# -------------------------------
# 7. Button Example
# -------------------------------
if st.button("Click Me!"):
    st.success("🎉 You clicked the button!")

# -------------------------------
# 8. Footer
# -------------------------------
st.write("---")
st.caption("Made with ❤️ using Streamlit")
