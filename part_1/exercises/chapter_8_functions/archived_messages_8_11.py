"""
Start with your work from Exercise 8-10. Call the function send_messages() with 
a copy of the list of messages. After calling the function, print both of your 
lists to show that the original list has retained its messages.
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

#using the copy of the list of messages.
send_messages(messages[:], sent_messages)

print(f"Original messages: {messages}")