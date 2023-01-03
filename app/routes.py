from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import AnalyzeForm

'''
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Avishek'},
            'body': 'Hi Introducing myself'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
'''

@app.route('/', methods=['GET', 'POST'])
def root():
    form = AnalyzeForm()
    if form.validate_on_submit():
        data = request.form.get("data")
        return render_template('form.html', form=form, data=data)
    return render_template('form.html', form=form)