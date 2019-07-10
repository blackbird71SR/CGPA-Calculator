from flask import Flask, render_template, request, redirect, url_for, jsonify, session, escape, Response, flash, send_from_directory, Markup
from forms import SGPAForm
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    form = SGPAForm(request.form) 
    if request.method == 'POST' and form.validate():
        s1 = float(request.form['s1'])
        s2 = float(request.form['s2'])
        s3 = float(request.form['s3'])
        s4 = float(request.form['s4'])
        s5 = float(request.form['s5'])
        s6 = float(request.form['s6'])
        cgpa = (32 * s1 + 35 * s2 + 25 * s3 + 21 * s4 + 25 * s5 + 25 * s6)/163
        return render_template('score.html', cgpa = cgpa)
    return render_template('index.html', form = form)