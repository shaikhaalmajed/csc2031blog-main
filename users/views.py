from flask import Blueprint, render_template, request, redirect, url_for
from users.forms import RegisterForm


users_blueprint = Blueprint('users', __name__, template_folder='templates')


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        print(request.form.get('username'))
        print(request.form.get('password'))
        print(request.form.get('confirm_password'))
        return redirect(url_for('users.login'))

    return render_template('users/register.html', form=form)

@users_blueprint.route('/login')
def login():
    return render_template('users/login.html')