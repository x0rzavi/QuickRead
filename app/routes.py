from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import AnalyzeForm
from helper.scrape import read_time
from helper.tips import get_tips

@app.route('/', methods=['GET', 'POST'])
def home():
    form = AnalyzeForm()
    tip = get_tips()
    wpm = 230
    if form.validate_on_submit():
        try:
            url = request.form.get("url")
            time = read_time(url, wpm)
        except: 
            time = 'Error occured!'

        return render_template('form.html', form=form, data=time, tips=tip)
    return render_template('form.html', form=form, tips=tip)

@app.route("/health")
def health():
    return "Success", 200