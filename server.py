import os
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Usercreds

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    user = ""
    if request.method == 'POST':
        user_data=Usercreds.query.filter_by(name = request.form['username']).first()
        if not Usercreds.query.filter_by(name = request.form['username']).first():
             error = 'Invalid user. Please try again.'
        elif request.form['password'] == user_data.password:
             return redirect(url_for('home', user_name = request.form['username']))
        else:
            error = 'Invalid Password. Please try again.'
    return render_template('login.html', error=error)
@app.route('/home')
def home():
    return "<h3>Login: <span style='color:green'>Success<span></h3><h3>User: <span style='color:green'>"+request.args.get('user_name')+"<span></h3><br><a href='/'>Back</a>"
if __name__ == '__main__':
    app.run()
