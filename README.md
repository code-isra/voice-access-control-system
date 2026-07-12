# voice-access-control-system
Voice-based authentication and authorization system using Python Speech Recognition and Linux group access control



##  Features 
* **Voice Passphrase Authentication:** Utilizes the microphone to capture audio and processes it using the Google Speech Recognition API.
* **Role-Based Access Control (RBAC):** Dynamically assigns users to specific Linux security groups based on the recognized passphrase.
* **Automated Group Mapping:** Uses Python's `subprocess` and `os` modules to execute system-level commands for permission management.

---

##  Tools and Technologies
* **Language:** Python 3
* **OS Target:** Linux Ubuntu
* **Primary Libraries:** `SpeechRecognition`, `pyaudio`
* **API Integration:** Google Speech Recognition API
* **System Core Modules:** `os`, `subprocess`

---

##  Initial Requirements & Setup

**To get this system running locally on an Ubuntu environment, follow these preparation steps:**
1. Download VirtualBox and Ubuntu ISO file to set up the virtual machine.
2. Install Ubuntu inside VirtualBox then create an account on your Linux 
     Ubuntu virtual machine.
3. Make sure that you have python3.x installed on your system.
4. Install SpeechReconition and puaudio libraries using the command:
     **pip install SpeechReconition pyaudio.**
5. To use Google Speech Recognition API, ensure that your system is connected to 
    the internet.
6. Form the settings > Audio, enable audio input to allow the microphone to capture the 
    voice.
7. The user running the script must have sudo privileges since the code uses system- 
    level commands.
8. Create two groups one for the administrators and the other for the regular users using 
    the following commands:
    **sudo groupadd 
      admin_group sudo 
      groupadd user_group**
9. Change the permission for admin_group to allow admins have full access to home 
directory:
    **sudo chown -R :admin_group /home/client1 
      sudo chmod -R 770 /home/client1**
10. Change the permission for user_group to prevent users from having access to home 
directory and only have access to /home/client1/Sys directory:
**sudo chown -R :user_group /home/client1/Users 
  sudo chmod -R 770 /home/client1/Users
  sudo chmod -R 700 /home/client1 
  sudo chmod -R 700 /home/**

##  Running the code!
1. To run the code, download the file “voice_authentication.py”. Then run it using the
command: python3 voice_authentication.py.
2.  The program will prompt the user to say the passphrase, the user must be close to 
 the microphone while speaking for better passphrase recognition.
3.The script checks if the recognized speech matches one of the passphrases and grant 
access based on that.
