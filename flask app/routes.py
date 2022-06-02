from app import app 
from flask import render_template, redirect, url_for
import forms
from models import Task
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about', methods=['GET', 'POSt'])
def about():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        t = Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('about.html', form=form)