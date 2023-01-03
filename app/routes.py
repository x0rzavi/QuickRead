from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import AnalyzeForm
from scrape import words

@app.route('/', methods=['GET', 'POST'])
def root():
    form = AnalyzeForm()
    if form.validate_on_submit():
        data = request.form.get("data")

        try: num_words = words(data)
        except: num_words='Error occured!'

        return render_template('form.html', form=form, data=num_words)
    return render_template('form.html', form=form)