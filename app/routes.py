from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import AnalyzeForm
from scrape import read_time

@app.route('/', methods=['GET', 'POST'])
def root():
    form = AnalyzeForm()
    if form.validate_on_submit():
        url = request.form.get("url")

        try: time = read_time(url, 230)
        except: time = 'Error occured!'

        return render_template('form.html', form=form, data=time)
    return render_template('form.html', form=form)