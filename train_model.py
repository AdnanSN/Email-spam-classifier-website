import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_20newsgroups

# Load a dataset
data = fetch_20newsgroups(subset='train', categories=['rec.autos', 'sci.space', 'talk.politics.misc', 'comp.graphics', 'rec.sport.hockey', 'rec.sport.baseball'], shuffle=True, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3, random_state=42)

# Create a pipeline that combines a CountVectorizer with a Naive Bayes classifier
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(X_train, y_train)

# Save the model to disk
with open("spam_classifier.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

print("Model training completed and saved as spam_classifier.pkl.")
