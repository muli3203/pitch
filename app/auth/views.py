from flask import render_template,url_for,redirect
from ..models import User
from . form import UserForm,Required
from .. import db 

@auth.route('/login',methods=['GET','POST'])
def login():
    form = UserForm()
    if form.validate_on_submit:
        user = User.query.filter_by(username =form.username.data).first()
        if user != None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username and password')
    return render_template('auth/login.html',loginform=form)