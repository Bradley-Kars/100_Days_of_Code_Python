from flask import Flask, render_template, request, redirect, url_for
from replit import db

app = Flask(__name__)

ALLOWED_USER_ID = "Bradley-Kars"

def is_valid_user():
    user_id = request.headers["X-Replit-User-Id"]
    return user_id == ALLOWED_USER_ID

@app.route('/')
def blog():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        if 'blog_posts' not in db:
            db['blog_posts'] = []

        db['blog_posts'].append({'title': title, 'body': body})

    blog_posts = db.get('blog_posts', [])

    return render_template('blog.html', blog_posts=blog_posts)

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        if is_valid_user():
            title = request.form['post_title']
            body = request.form['post_body']

            if 'blog_posts' not in db:
                db['blog_posts'] = []

            db['blog_posts'].append({'title': title, 'body': body})

            return redirect(url_for('blog'))
        else:
            return "Unauthorized", 401

    if is_valid_user():
        return render_template('post.html')
    else:
        return "Unauthorized", 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)