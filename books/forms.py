
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired, Length


class BookForm(FlaskForm):
    title = StringField('Book Title', validators=[DataRequired(), Length(min=4, max=40)])
    description = StringField('Description')
    image = StringField('Book Cover')
    num_pages = IntegerField('Number of pages')
    submit = SubmitField('Add New Book')

class EditForm(FlaskForm):
    title = StringField('Book Title', validators=[DataRequired(), Length(min=4, max=40)])
    description = StringField('Description')
    image = StringField('Book Cover')
    num_pages = IntegerField('Number of Pages')
    submit = SubmitField('Save Changes')