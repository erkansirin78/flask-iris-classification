from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class FlowerForm(FlaskForm):
    SepalLengthCm = StringField("Sepal Length")
    SepalWidthCm = StringField("Sepal Width")
    PetalLengthCm = StringField("Petal Length")
    PetalWidthCm = StringField("Petal With")

    submit = SubmitField("Predict")
