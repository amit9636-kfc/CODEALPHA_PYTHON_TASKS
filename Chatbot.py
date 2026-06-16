def chatbot():
    print("--- Chatbot se baat karein (khatam karne ke liye 'bye' likhein) ---")
    
    while True:
        # User input
        user_input = input("Aap: ").lower().strip()
        
        # Rule-based response logic
        if user_input == "hello":
            print("Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Sorry, mujhe samajh nahi aaya.")

# Chatbot start karein
if __name__ == "__main__":
    chatbot()