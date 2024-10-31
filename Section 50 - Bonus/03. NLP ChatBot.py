# https://chat.openai.com/share/9e9a4668-fb2f-4498-ab4b-9125b7a6fc7e

import nltk
from nltk.chat.util import Chat, reflections
from textblob import TextBlob

nltk.download('punkt')

# Define a simple reflection dictionary for responses
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
}

# Define initial conversation pairs
pairs = [
    [
        r"my name is (.*)",
        ["Hello, %1! How can I assist you today?", "Hi there, %1. What can I do for you?"],
    ],
    [
        r"what is your name?",
        ["I'm just a simple chatbot. You can call me ChatGPT.", "I'm ChatGPT, your virtual assistant."],
    ],
    [
        r"how are you?",
        ["I'm just a computer program, so I don't have feelings, but thanks for asking. How can I help you?",],
    ],
    [
        r"(.*) (weather|temperature) in (.*)",
        ["I'm not able to check the weather at the moment. You can try a weather website or app for that.",],
    ],
    [
        r"(.*)",
        [
            "I'm sorry, but I don't understand. Can you please rephrase your question?",
            "I'm not sure I follow. Could you please provide more context?",
        ],
    ],
]

# Create a Chat instance
chatbot = Chat(pairs, reflections)

# Start the conversation
print("ChatGPT: Hello! How can I assist you today? (type 'quit' to exit)")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("ChatGPT: Goodbye! Have a great day.")
        break
    else:
        response = chatbot.respond(user_input)
        print("ChatGPT:", response)

# End of the script