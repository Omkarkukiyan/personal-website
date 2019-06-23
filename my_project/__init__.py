import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_images import Images
from flask_login import LoginManager



app=Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
images = Images()
migrate=Migrate(app,db)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'

from my_project import routes, models

from my_project.models import Project

admin = Admin(app)
app.config['FLASK_ADMIN_SWATCH'] = 'Cyborg'
admin.add_view(ModelView(Project,db.session))



def create_app(config_class=Config):
    # ...
    if not app.debug and not app.testing:
        # ...

        if app.config['LOG_TO_STDOUT']:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            app.logger.addHandler(stream_handler)
        else:
            if not os.path.exists('logs'):
                os.mkdir('logs')
            file_handler = RotatingFileHandler('logs/microblog.log',
                                               maxBytes=10240, backupCount=10)
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s '
                '[in %(pathname)s:%(lineno)d]'))
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Personal startup')

    return app

from my_project.routes import main,portfolio
app.register_blueprint(main)
app.register_blueprint(portfolio)

if __name__ == '__main__':
    app.run(debug=True)


