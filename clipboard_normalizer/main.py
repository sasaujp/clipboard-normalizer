import click
import pyperclip
import re

@click.command()
def cmd():

    while True:
        new_text = text = pyperclip.waitForNewPaste()
        new_text = re.sub(r'[\r\n]', '', new_text)
        new_text = re.sub(r'([^a-zA-Z]) ([^a-zA-Z])', r'\1\2', new_text)
        new_text = re.sub(r'([a-zA-Z]) ([^a-zA-Z])', r'\1\2', new_text)
        new_text = re.sub(r'([^a-zA-Z]) ([a-zA-Z])', r'\1\2', new_text)
        pyperclip.copy(new_text)
        print(text, '->', new_text)
