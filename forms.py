from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class EnterRoom(FlaskForm):
	roomcode = StringField('Room Code', validators=[DataRequired()])
	enterroom = SubmitField('Enter Room')

