 from flask_wtf import Form
 from wtforms import TextField, SubmitField
 from wtforms.validators import Required
 from flask_wtf import FlaskForm

class LoginForm(Form):
    username=TextField('login', validators=[Required()])
    submit=SubmitField('Sign In')
# class Categories(db.Document):
#     categ_id = db.SequenceField()
#     name = db.StringField()
#     count = db.StringField()
#
# class AddItem(Form):
#     name = TextField('name', validators = [Required()])
#     category = TextField('category', validators = [Required()])
#     cost = TextField('cost', validators = [Required()])
#     photo_hash = TextField('photo')
#     description = TextField('descr')
#   submit = SubmitField('add')
