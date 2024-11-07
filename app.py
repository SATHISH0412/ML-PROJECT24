from flask import Flask, render_template, request
import pickle
import json
import random

app = Flask(__name__)

# Load the trained model and vectorizer
with open('intent_classifier.pkl', 'rb') as f:
    classifier = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Load the intents data
with open('intents.json', 'r') as f:
    intents = json.load(f)

def get_response(user_input):
    # Vectorize the user input
    user_input_vectorized = vectorizer.transform([user_input])

    # Predict the intent tag
    predicted_intent = classifier.predict(user_input_vectorized)[0]

    # Find responses for the predicted intent
    for intent in intents:
        if intent["tag"] == predicted_intent:
            # Choose a random response from the matched intent's responses
            return random.choice(intent["responses"])

    # Default response if no intent is matched
    return "I'm not sure I understand. Can you rephrase?"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = get_response(user_input)
    return response

if __name__ == '__main__':
    app.run(debug=True)