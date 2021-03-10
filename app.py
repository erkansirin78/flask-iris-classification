from flask import Flask, request, jsonify, session, url_for, redirect, render_template
import joblib

from flower_form import FlowerForm

classifier_loaded = joblib.load("saved_models/01.knn_with_iris_dataset.pkl")
encoder_loaded = joblib.load("saved_models/02.iris_label_encoder.pkl")


# prediction function
def make_prediction(model, encoder, sample_json):
    # parse input from request
    SepalLengthCm = sample_json['SepalLengthCm']
    SepalWidthCm = sample_json['SepalWidthCm']
    PetalLengthCm = sample_json['PetalLengthCm']
    PetalWidthCm = sample_json['PetalWidthCm']

    # Make an input vector
    flower = [[SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]]

    # Predict
    prediction_raw = model.predict(flower)

    # Convert Species index to Species name
    prediction_real = encoder.inverse_transform(prediction_raw)

    return prediction_real[0]


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


@app.route("/", methods=['GET','POST'])
def index():
    form = FlowerForm()

    if form.validate_on_submit():
        session['SepalLengthCm'] = form.SepalLengthCm.data
        session['SepalWidthCm'] = form.SepalWidthCm.data
        session['PetalLengthCm'] = form.PetalLengthCm.data
        session['PetalWidthCm'] = form.PetalWidthCm.data

        return redirect(url_for("prediction"))
    return render_template("home.html", form=form)


# Read models
classifier_loaded = joblib.load("saved_models/01.knn_with_iris_dataset.pkl")
encoder_loaded = joblib.load("saved_models/02.iris_label_encoder.pkl")


@app.route('/prediction')
def prediction():
    content = {'SepalLengthCm': float(session['SepalLengthCm']), 'SepalWidthCm': float(session['SepalWidthCm']),
               'PetalLengthCm': float(session['PetalLengthCm']), 'PetalWidthCm': float(session['PetalWidthCm'])}

    results = make_prediction(classifier_loaded, encoder_loaded, content)

    return render_template('prediction.html', results=results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
