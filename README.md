**Greetings people!!!**

This is my web application that leverages machine learning to classify emails as spam or not spam. Here's a detailed breakdown of the machine learning aspects used in this application:

**Model Training:**

The heart of this application is a pre-trained Naive Bayes classifier, which is widely used for text classification tasks like spam detection.

The model was trained using a dataset containing labeled examples of spam and non-spam emails. The training process involved learning the patterns and features that distinguish spam emails from non-spam emails.

The Naive Bayes algorithm is particularly effective for this task because it assumes independence between features, making it well-suited for high-dimensional text data.

**Text Preprocessing:**

Before training, the email text data was preprocessed to convert it into a format suitable for the model. This preprocessing typically involves:
**Tokenization**: Splitting the email content into individual words or tokens.

**Lowercasing**: Converting all words to lowercase to ensure consistency.

**Removing stop words**: Eliminating common words (e.g., "the," "and," "is") that do not contribute to spam detection.

**Vectorization**: Transforming the processed text into numerical feature vectors using techniques like TF-IDF (Term Frequency-Inverse Document Frequency) or Bag-of-Words.

**Model Integration:**

The trained model is saved as spam_classifier.pkl and loaded by the Flask backend during runtime.

When a user submits an email for classification, the backend applies the same preprocessing steps to the input text before feeding it to the model.

**Prediction:**

The model predicts the likelihood that the email belongs to the "spam" or "not spam" class based on the patterns it learned during training.

This prediction is then sent back to the frontend, where it is displayed to the user.

**Model Accuracy:**

The Naive Bayes model offers high accuracy for email spam classification due to its effectiveness with text data and its ability to handle the presence of numerous features.

By using a machine learning model, this application demonstrates how data-driven techniques can accurately distinguish between spam and non-spam emails, providing real-time predictions based on learned patterns. This makes my application a practical example of applying machine learning to a common problem in email filtering.


**Here's how you can run my email spam classifer in your own machine and get accurate classifications.**

Step 1: Clone my repository in your machine or download the zip file of my repository by clicking on the "Code" button.

Step 2: Run the "Train_model.py" file. What this program does is it trains the model and then produces a "spam_classifier.pkl" file.

Step 3: Now run the "app.py". What this does is it utilises the "spam_classifier.pkl" file to essentially perform the classification.

Step 4: After succesfully running the "app.py" file, your website should be running on your local host, to view the website go to "http://127.0.0.1:5000" in your browser to use the application.

**Thank you!!!**
