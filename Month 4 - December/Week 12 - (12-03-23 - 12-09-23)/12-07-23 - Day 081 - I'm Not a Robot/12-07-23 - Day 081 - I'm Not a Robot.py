from flask import Flask, request, redirect, url_for

app = Flask(__name__)

foods = ["Nuts", "Pizza", "Bacon-wrapped donuts", "Human food"]

def get_base_html(content):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="/static/style.css" rel="stylesheet" type="text/css" />
        <title>Your Flask App</title>
    </head>
    <body style="background-color: #1a1a1a; color: #ffffff;">
        {content}
    </body>
    </html>
    """

@app.route('/')
def index():
    food_options = "".join(f"<option value='{food}'>{food}</option>" for food in foods)
    page = f"""
    <div class="card">
        <form method="post" action="/welcome">
            <p class="center">Are you secretly a robot? <input type="radio" name="robot" value="yes">Yes <input type="radio" name="robot" value="no">No</p>
            <p class="center">What is the meaning of life? <input type="text" name="meaning_of_life"></p>
            <p class="center">Choose your favorite food:
            <select name="food">
                {food_options}
            </select>
            </p>
            <button class="center" type="submit">Prove You're Not a Robot</button>
        </form>
    </div>
    """
    return get_base_html(page)

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    form = request.form

    if request.method == "POST":
        if form["robot"] == "no" and form["meaning_of_life"] == "42" and form["food"] != "Human food":
            page = "<p class='center large-text'>Congratulations, you've passed the human verification test!</p>"
        else:
            page = "<p class='center large-text'>Error 404: Human Not Found. Are you sure you're not a robot?</p>"
    else:
        return redirect(url_for("index"))

    return get_base_html(page)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)