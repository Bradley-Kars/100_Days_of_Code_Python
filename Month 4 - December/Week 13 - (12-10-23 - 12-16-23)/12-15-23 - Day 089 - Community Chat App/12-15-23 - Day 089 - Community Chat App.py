from flask import Flask, render_template, request, redirect, url_for
from replit import db

app = Flask(__name__)

ALLOWED_USER_NAME = "Bradley-Kars"

def is_admin():
    user_name = request.headers.get("X-Replit-User-Name")
    return user_name == ALLOWED_USER_NAME

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform Replit authentication or any other desired authentication logic
        username = request.form.get('username')
        if username:
            # Set session or perform login logic as needed
            return redirect(url_for('chat'))

    return render_template('login.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        if not is_admin():
            return redirect(url_for('login'))

        message = request.form['message']
        user_profile_image = request.headers.get("X-Replit-User-Profile-Image")

        if 'chat_messages' not in db:
            db['chat_messages'] = []

        db['chat_messages'].append({
            'username': request.headers.get("X-Replit-User-Name"),
            'message': message,
            'profile_image': user_profile_image
        })

    chat_messages = db.get('chat_messages', [])[-5:]

    return render_template('chat.html', chat_messages=chat_messages, is_admin=is_admin())

@app.route('/admin', methods=['GET'])
def admin():
    if is_admin():
        chat_messages = db.get('chat_messages', [])
        return render_template('admin.html', chat_messages=chat_messages)
    else:
        return redirect(url_for('login'))

@app.route('/delete_message/<int:message_index>', methods=['GET'])
def delete_message(message_index):
    if is_admin():
        chat_messages = db.get('chat_messages', [])
        if 0 <= message_index < len(chat_messages):
            del chat_messages[message_index]
            db['chat_messages'] = chat_messages
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
