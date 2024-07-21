import pyperclip

# Get text from the clipboard and remove trailing whitespace
clipboard_text = pyperclip.paste().rstrip()

# Print the cleaned text
print(clipboard_text)
