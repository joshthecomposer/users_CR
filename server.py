from flask_app import app
from flask_app.models.user import User
from flask import Flask, render_template, redirect, request

@app.route('/')
def index():
    return redirect('/users/new')

@app.route('/users/new')
def new_user_form():

    return render_template('create.html')

@app.route('/users')
def show_users():
    all_users = User.show_all()
    return render_template('read_all.html', all_users=all_users)

@app.route('/create_user', methods=['POST'])
def create_user():
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    User.save(data)
    return redirect('/users')

if __name__ == '__main__':
    app.run(debug=True)