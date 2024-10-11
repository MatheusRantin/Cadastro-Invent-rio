from flask import Flask, render_template, redirect, url_for, request, session, Blueprint
from serverDatabase import getUser

user_bp = Blueprint('user', __name__ , template_folder='templates')

@user_bp.route('/')
def home():
    name = session.get('user')
    return render_template('home.html', name= name)


@user_bp.before_request
def check_validation():
    if 'token' not in session:
        return redirect('/auth')