"""
Modify your except block in Exercise 10-8 to fail silently if either file is missing.
"""

from pathlib import Path

files = ["cat.txt", "dog.txt"]

for file in files:
    path = Path(file)
    try:
        content = path.read_text() 
    except FileNotFoundError:
        pass
    else:
        print(f"Showing contents in {file}.")
        print(content)