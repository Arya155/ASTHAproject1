def chatbot():
                        #base 
    responses= {

        "hello":   "Hi there! Welcome to DecoBot.",
        "hi":      "Hey! How can I assist you today?",
        "bye":     "Goodbye! Have a wonderful day!",
        "help":    "Sure! You can ask me about greetings, my name, or the time.",
        "name":    "I am DecoBot, your rule-based AI assistant.",
        "thanks":  "You're welcome! Anything else?",
        "how are you": "I am just code, but I'm running great!",
        "can u help me":  "yes sure , tell me !"

    }

    print("DecoBot: Hello! I am DecoBot. Type 'exit' to quit.\n")

    while True :
        #input and snaitization 
        raw_input_text = input("you :")
        clean_input = raw_input_text.lower().strip()
        
        if clean_input =="exit" :
            print("DecoBot : Shutting down. Goodbye!")
            break

        #process
        reply = responses.get(clean_input, "I do not understand that.Can u rephrases?")

       #output 
        print(f"DecoBot: {reply}\n")


chatbot()