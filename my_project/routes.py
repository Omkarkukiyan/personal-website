import os
from my_project import app
from flask import render_template,Blueprint,abort, request,flash,redirect, render_template,url_for
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash
from my_project.models import User
from urllib.parse import urlparse, urljoin
from my_project.forms import LoginForm
from werkzeug.urls import url_parse
from urllib.parse import unquote

contact_info = {
    "email":"omkarkukiyan1234@gmail.com",
    "linkedin":"https://www.linkedin.com/in/omkarkukiyan/",
    "github":"https://github.com/Omkarkukiyan",
    "twitter":"https://twitter.com/omkar_kukiyan"
}


main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
#URL for homepage
@main.route('/index')
def index():
    user = {'username':'Omkar'}
    return render_template('home.html', title='Welcome', user=user)

#URL for project page
@main.route('/portfolio')
def _project():
    from my_project.models import Project
    projects = Project.query.all()
    projects.sort(key=lambda p:p.index)
    paths = {
        "detail": "projects",
        "edit": "edit",
        "delete": "delete",
        "moveup": "moveup"
    }

    return render_template('items.html', title='Project', heading="OMKAR'S PROJECT", items= projects, paths=paths)



#URL for about page
@main.route('/about', methods=["GET", "POST"])
def about():
    return render_template('about.html', title='About Me',contact=contact_info)


@main.route('/login', methods=['GET','POST'])
def handle_login():
    error=None
    form=LoginForm()
    if request.method=='POST':
        if request.form['username'] != 'omkarkukiyan' or request.form['password']!='9819945388omkar':
            flash('Invalid Credentials')
            return redirect(url_for('handle_login'))
        else:
            flash('Successful Login')
            return redirect(url_for('portfolio.new_project'))
    return render_template('log.html',form=form)




portfolio = Blueprint("portfolio", __name__, template_folder="templates")

@portfolio.route("/projects/<string:title>" ,methods=["GET","POST"])
def project_view(title):
    from my_project.models import Project
    if request.method == "POST":
        return handle_login()
    project = Project.query.filter_by(title=title).first()
    if not project:
        abort(404)
    return render_template('project.html', title=project.title, project=project)


def _is_safe_url(target):
    # http://flask.pocoo.org/snippets/62/
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ("http", "https") and \
        ref_url.netloc == test_url.netloc


