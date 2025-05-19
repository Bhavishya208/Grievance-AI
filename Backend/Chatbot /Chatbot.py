import json

def get_response(intent):
    with open('chatbot/intents.json') as f:
        intents = json.load(f)
    return intents.get(intent, "I'm sorry, I didn't understand that.")
