import speech_recognition as sr
import os
import subprocess

# Initialize recognizer
recognizer = sr.Recognizer()

# The correct passphrases for authentication
AUTHORIZED_USER_PASSPHRASE = "open system"
AUTHORIZED_ADMIN_PASSPHRASE = "hi system"

def add_user_to_group(username, group_name):
    try:
        # Use subprocess to add user to the specified group
        subprocess.run(["sudo", "usermod", "-aG", group_name, username], check=True)
        print(f"User '{username}' added to the group '{group_name}'.")
    except subprocess.CalledProcessError:
        print(f"Failed to add user '{username}' to the group '{group_name}'.")

def authenticate_voice():
    with sr.Microphone() as source:
        print("Please say the passphrase to authenticate:")

        # Adjust for ambient noise before listening
        recognizer.adjust_for_ambient_noise(source)

        try:
            # Capture the audio from the microphone
            audio = recognizer.listen(source, timeout=5)  # timeout :5 sec
            print("Audio captured successfully!")

        except sr.WaitTimeoutError:
            print("No speech detected within the timeout period.")
            return None
        except sr.RequestError:
            print("Could not connect to the Google Speech Recognition service.")
            return None
        except sr.UnknownValueError:
            print("Speech was not recognized.")
            return None

        # Try recognizing the speech and check for the passphrase
        try:
            recognized_text = recognizer.recognize_google(audio).lower()
            print("You said: " + recognized_text)

            if recognized_text == AUTHORIZED_USER_PASSPHRASE:
                print("Limited access granted.")
                return "user"
            elif recognized_text == AUTHORIZED_ADMIN_PASSPHRASE:
                print("Full access granted.")
                return "admin"
            else:
                print("Authentication failed! Incorrect passphrase.")
                return None

        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return None
        except sr.RequestError:
            print("Could not request results from the Google Speech Recognition service.")
            return None

# Authentication step
user_role = authenticate_voice()

if user_role == "user":
    # Authorization step for limited access user
    username = os.getlogin()  # Get the current system username
    add_user_to_group(username, "user_group")
    print("User added to 'user_group'. Limited access granted.")

elif user_role == "admin":
    # Authorization step for admin
    username = os.getlogin()  # Get the current system username
    add_user_to_group(username, "admin_group")
    print("User added to 'admin_group'. Full access granted.")

else:
    print("Access denied.")