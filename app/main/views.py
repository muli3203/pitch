from flask import render_template, flash, redirect
from . import main


#Views
@main.route('/')
def index():
    '''
    View the root page function that returns the index page and its data.
    '''
    title = 'A Pitcher App'
    return render_template('index.html', title = title)

# @main.route('/pitcher/<int:pitcher_id>')
# def pitcher(pitcher_id):

#     '''
#     View the pitcher page function that returns the pitcher page details and its data
#     '''
#     return render_template('pitcher.html', id = pitcher_id)

# @main.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         flash('  form.username.data, form.remember_me.data))
#         return redirect(url_for('index'))
#     return render_template('login.html', title='Sign In', form=formLogin requested for user {}, remember_me={}'.format(
          