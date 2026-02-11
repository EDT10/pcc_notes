from pathlib import Path

def word_count(filename):
    """Count the number of words in a given file"""
    try:
        content = filename.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
    # count the approximate number of words in the file:
        words = content.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ["alice.txt", "siddhartha.txt", "moby_dick.txt", "little_women.txt"]

for filename in filenames:
    path = Path(filename)
    word_count(path)
