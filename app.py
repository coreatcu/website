from flask import Flask, redirect, render_template, request, url_for
from flask_mail import Mail
from flask.ext.mail import Message
import simplejson
import os
from flask_sslify import SSLify

app = Flask(__name__)
app.config.from_pyfile('config.py')
mail = Mail(app)
data = {}
sslify = SSLify(app)

from config import SECRET_KEY
from forms import ContactForm

# import data from relevant JSON
def load_data():
    global data
    for name, path in app.config['DATA_FILENAMES'].iteritems():
        path = os.path.join(os.path.dirname(__file__), path)
        with open(path, 'r') as file:
            data[name] = simplejson.load(file)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/initiatives')
def initiatives():
    return render_template('initiatives.html', **data['initiatives'])

@app.route('/jade')
def jade():
    return render_template('jade.html')

@app.route('/cvc')
def cvc():
    return render_template('cvc.html')

@app.route('/womenatcore')
def womenatcore():
    return render_template('womenatcore.html')

@app.route('/corecircles')
def corecircles():
    return render_template('corecircles.html')

@app.route('/housing-lotto-16-17')
def housing_16_17():
    return redirect("https:\/\/docs.google.com/spreadsheets/d/1Mn6v5vvHK5pr1A_EWYtr9HfRU3tB7fmvUCwETlDHhW8/edit?usp=sharing")

@app.route('/infographic/<infographic_item>')
def infographic_path(infographic_item):
    return render_template('infographic.html', infographic=infographic_item)

@app.route('/team')
def team():
    return render_template('team.html', **data['team'])

@app.route('/alumni')
def alumni():
    return render_template('alumni.html', **data['alumni'])

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        print form.email.data
        msg = Message(form.subject.data,
                    recipients=[(form.name.data, form.email.data),
                                ('CORE Board', 'coreboard@columbia.edu')])
        msg.body = form.message.data
        mail.send(msg)
        return redirect(url_for('index'))
    return render_template('contact.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

load_data()

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=5000)

application = app
