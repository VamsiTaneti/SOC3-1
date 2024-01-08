import streamlit as st
st.set_page_config(page_title='Cats')
st.header("Types of Cats")
col1, col2 = st.columns(2)
with col1:
  st.subheader("First pic")
  st.image("./_G0A8343.JPG", caption="FIRST", width=300,use_column_width=True)
  st.write("First pic")
with col2:
  st.subheader("Second pic")
  st.image("._G0A8347.JPG", caption="SECOND", width=300,use_column_width=True)
  st.write("Second pic")
