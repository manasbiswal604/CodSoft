import re

def simple_chatbot(user_input):
    # Greeting responses
    if re.search(r'\b(hi|hello|hey)\b', user_input, re.IGNORECASE):
        return "Hello! How can I assist you today?"

    # Well-being responses
    if re.search(r'\b(how are you|how\'s it going)\b', user_input, re.IGNORECASE):
        return "I'm just a chatbot, but I'm here and ready to help!"

    # Weather responses
    if re.search(r'\b(weather|temperature)\b', user_input, re.IGNORECASE):
        return "I'm sorry, I don't have access to real-time weather information."

    # Joke responses
    if re.search(r'\b(joke|funny)\b', user_input, re.IGNORECASE):
        return "Sure, here's a joke for you: Why don't scientists trust atoms? Because they make up everything!"

    # Goodbye responses
    if re.search(r'\b(bye|goodbye)\b', user_input, re.IGNORECASE):
        return "Goodbye! Have a great day!"

    # Identity responses
    if re.search(r'\b(name|who are you)\b', user_input, re.IGNORECASE):
        return "I'm a simple chatbot designed to assist with basic queries."

    # Age responses
    if re.search(r'\b(age|old are you)\b', user_input, re.IGNORECASE):
        return "I don't have an age, as I'm just a computer program."

    # Thank you responses
    if re.search(r'\b(thank you|thanks)\b', user_input, re.IGNORECASE):
        return "You're welcome! Feel free to ask if you have more questions."

    # Time-related responses
    if re.search(r'\b(time|current time)\b', user_input, re.IGNORECASE):
        return "I don't have access to real-time data, including the current time."

    # General query responses
    if re.search(r'\b(who|what|where|when|why|how)\s', user_input, re.IGNORECASE):
        return "I'm just a simple chatbot and may not have the detailed information you're looking for."

    # Food-related responses
    if re.search(r'\b(food|eat)\b', user_input, re.IGNORECASE):
        return "I can't eat, but I can help you find recipes!"

    # Help-related responses
    if re.search(r'\b(help)\b', user_input, re.IGNORECASE):
        return "Of course! I'm here to help. What do you need assistance with?"

    # Movie recommendation responses
    if re.search(r'\b(movie|recommend)\b', user_input, re.IGNORECASE):
        return "Certainly! What genre are you in the mood for?"

    # Default response
    return "I'm sorry, I didn't quite understand your request. Could you please rephrase it?"

# Main loop
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)
