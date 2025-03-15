import string
import random
import streamlit as st

def password_generator(length):
    charactors = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(charactors) for x in range(length))

st.title("Password Stength Checker🔏")
