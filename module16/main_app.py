import streamlit as st

if st.button("Click me"):
    st.write("Button clicked")

if st.checkbox("Check me to show some text"):
    st.write("You're seeing this text because you checked the checkbox")

user_input = st.text_input("Enter text", "Sample text")

st.write("You entered", user_input)

age = st.number_input("Enter your age", min_value=0, max_value=100)

st.write(f"Your age is {age}")

message = st.text_area("Enter a message")

st.write(f"Your message is {message}")

choice = st.radio("Pick one", ["Choice 1", "Choice 2", "Choice 3"])

st.write(f"Your choice is {choice}")

if st.button("Success"):
    st.success("Operation was successful")

try:
    1 / 0
except Exception as e:
    st.exception(e)

if st.button("Click me"):
    st.write("Button clicked!")

if st.checkbox("Check me to show some text")