"""
Start with a copy of your program from Exercise 8-9. Write a function called send_messages() 
that prints each text message and moves each message to a new list called 
sent_messages as it’s printed. After calling the function, print both of your 
lists to make sure the messages were moved correctly.
"""

messages = ["hell world", "text me back", "i am in a meeting", "i love you"]
sent_messages = []

def show_messages(text_messages):
    """show all messages in the list"""
    for message in text_messages:
        print(message.title())


def send_messages(messages, sent_messages):
    """display messages and move them to a new list called sent_messages"""
    print("\nsending messages")
    while messages:
        pending_message = messages.pop()
        print(pending_message.title())
        sent_messages.append(pending_message)



show_messages(messages)

send_messages(messages, sent_messages)