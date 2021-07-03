from flask_wtf import Form
from wtforms import FloatField
from wtforms.validators import DataRequired


class GetId(Form):
    Id = FloatField("Id", validators=[DataRequired()])
