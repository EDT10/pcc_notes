glossary = {
    "variable": "They are labels that you can assign to values.",
    "strings": "A series of characters.",
    "methods": "A method is an action that Python can perform on a piece of data.",
    "integers": "These are whole numbers.",
    "list": "A collection of items in a particular order",
    "sets": "This is collection in which each item must be unique.",
    "dictionary": "In Python a dictionary is a collection of key-value pairs.",
    "tuple": "This is a list of items that cannot change.",
    "logical errors": "Valid python code but the code does not produce the desired"
    "result because the problem occurs in its logic",
}


for word, meaning in glossary.items():
    print(f"{word.title()}: {meaning}")

