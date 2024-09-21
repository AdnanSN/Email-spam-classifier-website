from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load the pre-trained model
with open("spam_classifier.pkl", "rb") as model_file:
    model = pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    email_content = data['email_content']

    # Predict whether the email is spam or not
    prediction = model.predict([email_content])
    result = 'SPAM' if prediction[0] == 1 else 'NOT SPAM'

    return jsonify({'classification': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
