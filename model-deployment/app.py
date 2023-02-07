from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open("sentiment_analysis_model.pkl", "rb"))


@app.route("/predict", methods=["POST"])
def predict():
    # Get the data from the request
    data = request.get_json(force=True)

    # Make a prediction using the model
    prediction = model.predict(data)

    # Return the prediction result
    return jsonify(prediction)


if __name__ == "__main__":
    app.run(debug=True)
