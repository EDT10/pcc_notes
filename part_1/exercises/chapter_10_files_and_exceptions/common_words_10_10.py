"""
Write a program that reads the files you found at Project Gutenberg and determines 
how many times the word 'the' appears in each text. This will be an approximation 
because it will also count words such as 'then' and 'there'. Try counting 'the ', 
with a space in the string, and see how much lower your count is.
"""

from pathlib import Path

path = Path("alice.txt")
content = path.read_text().strip()
word_count = content.lower().count("the ")

print(word_count)
