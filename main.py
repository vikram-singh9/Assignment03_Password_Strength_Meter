import string  # Importing string module for character sets
import random  # Importing random module to generate passwords
import re  # Importing re (regex) for password validation
import streamlit as st  # Importing Streamlit for UI

# Function to generate a random password of given length
def password_generator(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))

# Function to check password strength
def password_strength_checker(password):
    score = 0  # Strength score initialization
    common_passwords = ["12345678", "password123", "vikram123", "infinity999", "abcdefghij"]

    # Check if password is too common
    if password in common_passwords:
        return "❌ This is too common! Try another one...", "weak"

    feedback = []  # List to store improvement suggestions

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters! Try again 😪")

    # Check for uppercase and lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters 🙄")

    # Check for numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers between 0-9 🤨")

    # Check for special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Use special characters 🥱")

    # Determine password strength based on score
    if score == 4:
        return "💪🏽 Strong Password", "strong"
    if score == 3:
        return "🧐 Moderate Password", "moderate"
    if score == 2:
        return "\n".join(feedback), "weak"
    
    # If password is very weak (score 0 or 1)
    return "Password is extremely weak! Try making it stronger. 😵", "weak"

# Streamlit UI
st.title("Password Strength Checker 🔏")

# Input field for password checking
check_password = st.text_input("Enter Password to check **Strength**", type="password")

# Button to check password strength
if st.button("Check Strength"):
    if check_password:
        result, strength = password_strength_checker(check_password)
        
        if strength == "strong":
            st.success(result)  # Show success message for strong passwords
            st.balloons()  # Display balloons animation 🎈
        elif strength == "moderate":
            st.warning(result)  # Show warning for moderate passwords
        else:
            st.error("Weak Password! Improve it with these tips:")  # Show error message
            st.write(result)  # Display feedback for improvement

# Input for password length selection
password_length = st.number_input("Enter the password length", min_value=8, max_value=25, value=12)

# Button to generate a strong random password
if st.button("Generate Password"):
    password = password_generator(password_length)
    st.info(f"Generated Password: `{password}`")  # Display generated password
