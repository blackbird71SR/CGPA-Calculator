from wtforms import Form, StringField, IntegerField, DateField, PasswordField, SubmitField, BooleanField, SelectField, TextAreaField, RadioField, FieldList, FormField, DecimalField
from wtforms import validators, ValidationError

class SGPAForm(Form):
    s1 = DecimalField('Semester 1 SGPA', places=2, rounding=None, use_locale=False, number_format=None, validators=[validators.DataRequired()])
    s2 = DecimalField('Semester 2 SGPA', places=2, rounding=None, use_locale=False, number_format=None, validators=[validators.DataRequired()])
    s3 = DecimalField('Semester 3 SGPA', places=2, rounding=None, use_locale=False, number_format=None, validators=[validators.DataRequired()])
    s4 = DecimalField('Semester 4 SGPA', places=2, rounding=None, use_locale=False, number_format=None, validators=[validators.DataRequired()])
    s5 = DecimalField('Semester 5 SGPA', places=2, rounding=None, use_locale=False, number_format=None, validators=[validators.DataRequired()])
    submit = SubmitField('Submit')