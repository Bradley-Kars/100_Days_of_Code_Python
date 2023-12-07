from flask import Flask, request, render_template
from replit import db
import hashlib

app = Flask(__name__)

if "users" not in db:
    db["users"] = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/login", methods=["POST"])
def login():
    form = request.form
    username = form["username"]
    email = form["email"]
    password = form["password"]

    # Validate email format
    if "@" not in email or "." not in email:
        return "Invalid email format"

    users = db["users"]

    if username not in users:
        # Hash the password before storing it
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        users[username] = {"email": email, "password": hashed_password}
        return "Account created!"
    else:
        # Verify hashed password
        stored_password = users[username]["password"]
        if hashlib.sha256(password.encode()).hexdigest() == stored_password:
            return f"Welcome {username}, you are logged in"
        else:
            return "Email or password incorrect"

@app.route("/login", methods=["GET"])
def login_page():
    username = request.args.get("username")
    if username:
        return f"Username {username} not found. Please check your credentials."
    else:
        return "This is the login page. Use the form to submit a login request."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)