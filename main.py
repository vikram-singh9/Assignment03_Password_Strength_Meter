import string
import random
import re
import streamlit as st

def password_generator(length):
    charactors = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(charactors) for x in range(length))


def password_strength_checker(password):
    score = 0
    common_passwords = ["12345678", "password123", "vikram123", "infinity999", "abcdefghij"]
    if password in common_passwords:
        return "❌ This is too common ! try with another one..."
    feedback = []

    if len(password) >= 8:
        score +=1
    else:
        feedback.append("Password should be atleast 8 charactors! try again😪")
    
    if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
        score += 1
    else:
        feedback.append("Include Uppercase and Lowercase🙄")
    
    if re.search(r"\d",password):
        score += 1
    else:
        feedback.append("Add numbers btw 0-9🤨")

    if re.search(r"[!@#$%^&*]",password):
        score += 1
    else:
        feedback.append("Use special charactors🥱")

    if score == 4:
        return "💪🏽 Strong Password","strong"
    if score == 3:
        return "🧐 Weak password","moderate"
    if score == 2:
        return "\n".join(feedback),"weak"
    



st.title("Password Stength Checker🔏")

check_password = st.text_input("Enter Password to check **Strength**" ,type="password")
if st.button("Check Strength"):
   result, strength=  password_strength_checker(check_password)
   if result == "strong":
       st.success(result)
       st.balloons()

password_length = st.number_input("Enter the password length",min_value=8, max_value=25, value=12)

if st.button("Generate Password"):
    password = password_generator(password_length)
    st.info(password)
