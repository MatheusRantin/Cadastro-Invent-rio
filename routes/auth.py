from flask import Flask, render_template, url_for, redirect, request, Blueprint, session
from serverDatabase import getUser

auth_bp = Blueprint('auth', __name__, template_folder='templates')
    
@auth_bp.route('/', methods=["POST","GET"])
def checkUser():
    if request.method == "POST":
        
        email = request.form.get('email')
        pwd = request.form.get('pwd')
        user_db = {'email':email, 'password':pwd}
        validation = getUser(user_db)
        if validation == False:
            return redirect('/auth')
        elif validation == True:
            print(validation)
            session['user']= email
            session['token']='0000'

            return redirect('/user')

    return render_template('login.html')

