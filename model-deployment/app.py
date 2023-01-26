from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from nltk.sentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

# Load the model and vectorizer
clf = MultinomialNB()
cv = CountVectorizer()
sia = SentimentIntensityAnalyzer()

# Train the model with the training data
X_train_vect = cv.fit_transform(X_train)
clf.fit(X_train_vect, y_train)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    review = request.form['review']
    review_vect = cv.transform([review])
    sentiment = clf.predict(review_vect)
    sentiment_proba = clf
