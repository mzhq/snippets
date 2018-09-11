import pyperclip
text = pyperclip.paste()

text_one_line = ' '.join(text.split())
pyperclip.copy(text_one_line)
print(text_one_line)
