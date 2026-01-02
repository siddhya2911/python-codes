def chatbot():
    print("Bot: hello! type by for exit")
    while True:
        user=input("You :")
        if user=='hello'or user=="hi":
            print("Bot: what can i help you")
        elif user=='how are you':
            print("Bot: i m find. Thank you")
        elif user=='what is your name':
            print("Bot: my name is chatbot ")
        elif user=="who is your creator":
            print("Bot: My creator is Siddharth ")
        elif user=='by':
            print("Bot: 'Good by', Have a nice day")
            break
        else:
            print("Bot: I can't understand ")
    return 0
chatbot()

