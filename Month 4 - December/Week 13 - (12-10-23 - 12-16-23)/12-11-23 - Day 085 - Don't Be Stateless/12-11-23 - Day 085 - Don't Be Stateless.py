from flask import Flask, render_template, redirect, url_for, request, session
from replit import db

app = Flask(__name__)

app.secret_key = "your_secret_key"

@app.before_request
def before_request():
    if 'username' not in session and request.endpoint not in ['login', 'signup']:
        return redirect(url_for('login'))

@app.route('/')
def home():
    return redirect(url_for('dashboard'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in db and db[username] == password:
            session['username'] = username
            return redirect(url_for('dashboard'))

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username not in db:
            db[username] = password

            session['username'] = username
            return redirect(url_for('dashboard'))

    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)