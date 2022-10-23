from flask import Flask, render_template
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_ECHO'] = os.getenv('SQLALCHEMY_ECHO') == 'True'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') == 'False'

db = SQLAlchemy(app)

from main.views import main_blueprint
from users.views import users_blueprint
from blog.views import blog_blueprint

app.register_blueprint(main_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(blog_blueprint)


@app.errorhandler(403)
def forbidden_error(error):
    return render_template('403.html'), 403


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run()

