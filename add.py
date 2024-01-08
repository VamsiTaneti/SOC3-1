import streamlit as st
st.set_page_config(page_title='Pics')
st.header("My pictures")
col1, col2 = st.columns(2)
with col1:
  st.subheader("First pic")
  st.image("./_G0A8343.JPG", caption="1", width=300,use_column_width=True)
with col2:
  st.subheader("Second pic")
  st.image("./_G0A8347.JPG", caption="2", width=300,use_column_width=True)
st.header("Favourate pics")
