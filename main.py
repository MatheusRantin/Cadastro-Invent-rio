from flask import Flask, render_template, redirect, url_for, request
from models import Usuario
from serverDatabase import getUser
app = Flask(__name__)

#Rotas
@app.route('/')
def login():
    return render_template('login.html')
    
@app.route('/check-user', methods=["POST","GET"])
def checkUser():
    email = request.form.get('email')
    pwd = request.form.get('pwd')
    response_login = {'email':email, 'password':pwd}
    validationUser = getUser(response_login)
    if validationUser == True:
        return redirect('/home')
    elif validationUser == False:
        
        return redirect('/')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == ("__main__"):
    app.run(debug=True)