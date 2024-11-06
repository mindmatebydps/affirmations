import streamlit as st
import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Define the list of affirmations
affirmations = [
    "I am confident",
    "I am worthy",
    "I am loved",
    "I am happy",
    "I am grateful",
    "I am enough",
    "I deserve to be happy",
    "I am enough because I am me",
    "I love myself for who I am",
    "My feelings matter",
    "I am worthy of respect",
    "I love my body just the way it is",
    "I am ready for what comes next.",
    "No one can make me feel inferior without my consent",
    "I deserve happiness and fulfillment"
]

st.title("Affirmation Speech Recognition")

def recognize_affirmation(audio_data):
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Sorry, could you be a bit louder."
    except sr.RequestError:
        return "Sorry, the service is down."

for affirmation in affirmations:
    st.subheader(f"Please say: '{affirmation}'")

    if st.button(f"Listen for '{affirmation}'"):
        with sr.Microphone() as source:
            status_placeholder = st.empty()  # Create a placeholder for status messages
            status_placeholder.write("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)
            status_placeholder.empty()  # Clear the placeholder after recording is done

        recognized_text = recognize_affirmation(audio)

        if recognized_text.lower() == affirmation.lower():
            st.success(f"Affirmation detected: '{affirmation}'")
        else:
            st.warning(f"Detected: '{recognized_text}'. Please try again.")
