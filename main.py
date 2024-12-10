import streamlit as st
from langchain_helper import  generate_resturant_name_and_menu_items

st.title("restuarant name generator")

cuisine = st.sidebar.selectbox("pick a cuisine",("Indian","American","Mexican","Chinese","Italian"))


if cuisine :
    response = generate_resturant_name_and_menu_items(cuisine)

    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].split(",")

    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-",item)