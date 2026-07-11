# simple chatbot - rule based

while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello! How are you?")

    elif user_input in ["how are you", "how are you?"]:
        print("Bot: I'm good, thanks for asking!")

    elif user_input in ["what is your name", "what's your name"]:
        print("Bot: I'm a simple chatbot made in Python.")

    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Bye bye! Take care.")
        break

    else:
        print("Bot: Sorry, I didn't understand that.")