from flask_wtf import FlaskForm
from wtforms_alchemy import model_form_factory
from my_project import db
from my_project.models import Project
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

BaseModelForm = model_form_factory(FlaskForm)
class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ["imgfile", "index"]
        field_name=("title", "github_url","website","description","long_desc")


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])

    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')