from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length
from flask_babel import lazy_gettext as _l


class MessageForm(FlaskForm):
    item_id = IntegerField('Item id', validators=[DataRequired()])
    message = TextAreaField(_l('Message'), validators=[DataRequired(), Length(min=0, max=140)])
    submit = SubmitField(_l('Submit'))
