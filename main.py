import string
import random
import streamlit as st

def password_generator(length):
    charactors = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(charactors) for x in range(length))

st.title("Password Stength Checker🔏")

password_length = st.number_input("Enter the password length",min_value=8, max_value=25, value=12)

if st.button("Generate Password"):
    password = password_generator(password_length)
    st.info(password)
