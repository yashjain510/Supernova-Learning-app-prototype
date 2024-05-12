import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from textblob import TextBlob
import speech_recognition as sr
import pyttsx3

# Initialize NLTK
nltk.download('punkt')

# Initialize the speech recognizer and synthesizer
recognizer = sr.Recognizer()
synthesizer = pyttsx3.init()

def get_word_meaning(word):
    synsets = wordnet.synsets(word)
    if synsets:
        meaning = synsets[0].definition()
    else:
        meaning = "Meaning not found for the word: " + word
    speak(meaning)
    return meaning

def correct_spelling(sentence):
    corrected_sentence = str(TextBlob(sentence).correct())
    speak(corrected_sentence)
    return corrected_sentence

def correct_sentence(sentence):
    corrected_sentence = str(TextBlob(sentence).correct())
    speak(corrected_sentence)
    return corrected_sentence

def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        spoken_text = recognizer.recognize_google(audio)
        print("You said:", spoken_text)
        return spoken_text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError:
        print("Sorry, the speech recognition service is unavailable.")
        return ""

def speak(text):
    synthesizer.say(text)
    synthesizer.runAndWait()

def main():
    while True:
        print("\n!!!Welcome to SpeaksEasyEdu!!!")
        print("Choose an option:")
        print("1. Get meaning of a word")
        print("2. Correct spelling in a sentence")
        print("3. Correct sentence")
        print("4. Speak a word and get its meaning")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            word = input("Enter a word: ")
            meaning = get_word_meaning(word)
            print("Meaning:", meaning)
        elif choice == "2":
            sentence = input("Enter a sentence: ")
            corrected_sentence = correct_spelling(sentence)
            print("Corrected sentence:", corrected_sentence)
        elif choice == "3":
            sentence = input("Enter a sentence: ")
            corrected_sentence = correct_sentence(sentence)
            print("Corrected sentence:", corrected_sentence)
        elif choice == "4":
            print("Speak a word...")
            spoken_word = recognize_speech()
            if spoken_word:
                meaning = get_word_meaning(spoken_word)
                print("Meaning:", meaning)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
