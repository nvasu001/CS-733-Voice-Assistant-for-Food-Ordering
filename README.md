# CS-733-Voice-Assistant-for-Food-Ordering
NLP project

//to do this we need python version 3.8 - following instructions are for windows machine
1. Go to this page to get Python 3.8.6. ""https://www.python.org/downloads/release/python-386/""
Scroll Down to Files Section and install file with the name "Windows x86-64 executable installer" 
2. From within VS Code, you can create non-global environments, using virtual environments or Anaconda, by opening the Command Palette (Ctrl+Shift+P), start typing the Python: Create Environment command to search, and then select the command.
https://code.visualstudio.com/docs/python/environments
3. Choose Python 3.8 version
4. (Ctrl+Shift+P) Python: Select Interpreter (Choose Python 3.8.x ('.venv': venv))
5. (Ctrl+Shift+P) Terminal: Create New Terminal in Active Workspace
6. Check which version of Pythons you have "py -0". you should (venv) * and 3.8.*. Wait until "Creating environment(Show Logs): Installing packages) popup is done and gone
7. You can proceed with this to avoid steps below and be done with steps 7 through 14 "pip install -r requirements.txt"
{
    7. "python -m pip install requests"
    
    8. "python -m pip install --upgrade pip"
    9. "pip3 install nltk"
    10. "pip3 install speechrecognition"
    11. "pip3 install pyttsx3"
    12. "pip3 install pyaudio"
    13. "pip3 install tensorflow"
    14. "pip3 install neuralintents"
    15. "pip3 install flask"
    16. "pip3 install beautifulsoup4"
    17. "pip3 install selenium"
    18. "pip3 install --upgrade autopep8"
}

Execution:
To run right click on main.py and "Run Python File in Terminal"

Note: This step is not requiredCreate requirements.txt - "pip freeze > requirements.txt"

References:
https://www.youtube.com/watch?v=F62wb_jfUUw
https://www.tensorflow.org/install/pip#windows-native_1
https://www.youtube.com/watch?v=GHvj1ivQ7ms