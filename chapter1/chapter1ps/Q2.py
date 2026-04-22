import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say(" hi Aniket welcome to python programming language and this is your first program in python good luck for your python journey")
engine.runAndWait()