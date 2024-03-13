import nltk
import random
from nltk.chat.util import Chat, reflections
import json

# open the json file and read it
with open('intents.json', 'r') as f:
    # Load the JSON data
    data = json.load(f)

# Extract patterns and responses from loaded data
patterns = []
for intent in data['intents']:
    for pattern in intent['patterns']:
        patterns.append((pattern, intent['responses']))

# Define reflections for certain pronouns
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# Create a chatbot instance
chatbot = Chat(patterns, reflections)

# Function to start and run the chatbot
def start_chat():
    print("Hi! I'm Chatbot. Let's chat. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
        if user_input.lower() in ['quit', 'goodbye', 'bye']:
            break

# Run the chatbot
if __name__ == "__main__":
    start_chat()

# print(patterns)