# CS-733-Voice-Assistant-for-Food-Ordering
NLP project

//to do this we need python version 3.8 - following instructions are for windows machine
1. From within VS Code, you can create non-global environments, using virtual environments or Anaconda, by opening the Command Palette (Ctrl+Shift+P), start typing the Python: Create Environment command to search, and then select the command.
https://code.visualstudio.com/docs/python/environments
2. Choose Python 3.8 version
3. (Ctrl+Shift+P) Python: Select Interpreter (Choose Python 3.8.x ('.venv': venv))
4. (Ctrl+Shift+P) Terminal: Create New Terminal in Active Workspace
5. Check which version of Pythons you have "py -0". you should (venv) * and 3.8.*. Wait until "Creating environment(Show Logs): Installing packages) popup is done and gone
6. You can proceed with this to avoid steps below and be done with steps 7 through 14 "pip install -r requirements.txt"
{
    7. "python -m pip install requests"
    8. "python -m pip install --upgrade pip"
    9. "pip3 install nltk"
    10. "pip3 install speechrecognition"
    11. "pip3 install pyttsx3"
    12. "pip3 install pyaudio"
    13. "pip3 install tensorflow"
    14. "pip3 install neuralintents"
}

Execution:
To run right click on main.py and "Run Python File in Terminal"

Note: This step is not requiredCreate requirements.txt - "pip freeze > requirements.txt"

References:
https://www.youtube.com/watch?v=F62wb_jfUUw
https://www.tensorflow.org/install/pip#windows-native_1