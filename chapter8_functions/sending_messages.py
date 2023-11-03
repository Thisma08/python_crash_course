def show_messages(messages):
    print("Tous les messages:")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    print("\nEnvoi des messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["message1", "message2", "message3"]
show_messages(messages)

sent_messages = []
send_messages(messages, sent_messages)

print("\nResultat:")
print(messages)
print(sent_messages)