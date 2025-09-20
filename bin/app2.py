from flask import Flask, request,redirect, url_for, render_template, session, Response

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html') 

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']

    """if username == 'mohan123' and password == 'pass':
        return render_template('welcome.html', name=username)"""
    
    valid_users = {
        'admin': '123',
        'mohan123': 'pass',
        'mohan': '456'
    }

    if username in valid_users and valid_users[username]:
        return render_template('welcome.html', name=username)
    else:
        return "Invalid credentials. Please try again.`"
   