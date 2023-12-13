from flask import Flask, render_template, request, redirect, session, url_for
from replit import db
import os

app = Flask(__name__)
app.secret_key = os.environ['app_key']

@app.route('/')
def blog():
    if request.method == 'POST' and not session.get('logged_in'):
        return redirect(url_for('login'))

    if request.method == 'POST' and session.get('logged_in'):
        title = request.form['title']
        body = request.form['body']

        if 'blog_posts' not in db:
            db['blog_posts'] = []

        db['blog_posts'].append({'title': title, 'body': body})

    blog_posts = db.get('blog_posts', [])

    return render_template('blog.html', blog_posts=blog_posts, can_post=session.get('logged_in'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'nimda':
            session['logged_in'] = True
            return redirect(url_for('blog'))
        else:
            return render_template('login.html', error='Invalid credentials')

    return render_template('login.html', error=None)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('blog'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)