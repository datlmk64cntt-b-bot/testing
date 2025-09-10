
# app.py
import streamlit as st
import my_backend as be   # đổi import sang my_backend

st.title("Demo kết nối Frontend - Backend bằng Streamlit")

name = st.text_input("Nhập tên của bạn:")
a = st.number_input("Số thứ nhất:", step=1, value=0)
b = st.number_input("Số thứ hai:", step=1, value=0)

if st.button("Chạy backend"):
    if name:
        st.success(be.greetuser(name))
    result = be.addnumbers(a, b)
    st.info(f"Tổng của {a} + {b} = {result}")
