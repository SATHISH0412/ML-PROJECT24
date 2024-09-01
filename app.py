from flask import Flask, render_template, request, jsonify
from chat import get_response  
from flask_cors import CORS# Assuming you have this function for generating bot responses

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.get_json().get("message")
    print(text)  # Get the user's message from the request
    response = get_response(text)  # Generate the bot's response using your chatbot logic
    message = {"answer": response}  # Create a dictionary to hold the response
    return jsonify(message)  # Return the response as a JSON object

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask app in debug mode
