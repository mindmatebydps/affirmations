# Initialize the recognizer
recognizer = speech_recognition.Recognizer()

# Define the listreamlit of affirmations
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
    "I love my body justreamlit the way it is",
    "I am ready for what comes next.",
    "No one can make me feel inferior without my consent",
    "I deserve happiness and fulfillment"
]

streamlit.title("Affirmation Speech Recognition")

def recognize_affirmation(audio_data):
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except speech_recognition.UnknownValueError:
        return "Sorry, could you be a bit louder."
    except speech_recognition.RequestreamlitError:
        return "Sorry, the service is down."

for affirmation in affirmations:
    streamlit.subheader(f"Please say: '{affirmation}'")

    if streamlit.button(f"Listreamliten for '{affirmation}'"):
        with speech_recognition.Microphone() as source:
            recognizer.adjustreamlit_for_ambient_noise(source, duration=1)
            streamlit.write("Listreamlitening...")
            audio = recognizer.listreamliten(source)

        recognized_text = recognize_affirmation(audio)

        if recognized_text.lower() == affirmation.lower():
            streamlit.success(f"Affirmation detected: '{affirmation}'")
        else:
            streamlit.warning(f"Detected: '{recognized_text}'. Please try again.")


