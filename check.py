#! python3

"""check.py - Launches google.com with words from the command line or using clipboard."""

# Import essential modules.
import sys
import pyperclip
import webbrowser

# Set searched_words variable using command line or clipboard.
if len(sys.argv) > 1:
    searched_words = ' '.join(sys.argv[1:])
else:
    searched_words = pyperclip.paste()

# Open browser with provided words.
webbrowser.open('https://www.google.com/search?client=firefox-b-d&q=' + searched_words)
