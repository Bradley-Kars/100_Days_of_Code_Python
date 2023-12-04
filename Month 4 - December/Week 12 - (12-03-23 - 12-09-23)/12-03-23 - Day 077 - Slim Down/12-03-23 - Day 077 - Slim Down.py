from flask import Flask, redirect

app = Flask(__name__, static_url_path="/static")

@app.route('/')
@app.route('/blog')
def index():
  page = ""
  with open("static/home.html", "r") as f:
      page = f.read()

  return page

@app.route("/blog/introduction")
@app.route("/introduction")
def introduction():
    title = "Introduction to My Blog"
    date = "January 10th"
    text = "Welcome to my blog! This is the beginning of my blogging journey."
    return render_blog_template(title, date, text)

@app.route("/blog/tech-trends")
@app.route("/tech-trends")
def tech_trends():
    title = "Current Tech Trends"
    date = "January 15th"
    text = "Exploring the latest trends in technology and its impact on various industries."
    return render_blog_template(title, date, text)

@app.route("/blog/coding-tips")
@app.route("/coding-tips")
def coding_tips():
    title = "Essential Coding Tips"
    date = "January 20th"
    text = "Sharing valuable coding tips to enhance your programming skills and productivity."
    return render_blog_template(title, date, text)

@app.route('/blog/game-dev')
@app.route('/game-dev')
def game_dev():
    title = "Journey into Game Development"
    date = "January 25th"
    text = "Documenting my experiences and challenges in the exciting world of game development."
    return render_blog_template(title, date, text)

@app.route('/blog/farewell')
@app.route('/farewell')
def farewell():
    title = "Farewell to My Blog"
    date = "January 30th"
    text = "Saying goodbye to this blog with gratitude and reflections on the journey."
    return render_blog_template(title, date, text)

def render_blog_template(title, date, text):
    page = ""
    with open("template/blog.html", "r") as f:
        page = f.read()

    page = page.replace("{title}", title)
    page = page.replace("{date}", date)
    page = page.replace("{text}", text)

    return page

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
