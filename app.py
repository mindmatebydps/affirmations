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

# Score counter
if "score" not in st.session_state:
    st.session_state.score = 0  # Initialize the score in session state

def recognize_affirmation(audio_data):
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Sorry, could you be a bit louder."
    except sr.RequestError:
        return "Sorry, the service is down."

# Display the current page content based on the session state
if "page" not in st.session_state:
    st.session_state.page = "Affirmation Recognition"  # Default to the recognition page

if st.session_state.page == "Affirmation Recognition":
    st.title("Affirmation Speech Recognition")

    # Process each affirmation
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
                st.session_state.score += 1  # Increment score if affirmation is correctly recognized
            else:
                st.warning(f"Detected: '{recognized_text}'. Please try again.")

elif st.session_state.page == "Score":
    st.title("Your Score")
    st.subheader(f"Total Affirmations Correct: {st.session_state.score}/{len(affirmations)}")

# Page selection box at the bottom
st.session_state.page = st.selectbox("Choose a page:", ["Affirmation Recognition", "Score"], index=["Affirmation Recognition", "Score"].index(st.session_state.page))
