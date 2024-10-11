from flask import Flask, render_template, redirect, url_for, request, session
from routes.user_route import user_bp
from routes.auth import auth_bp
from serverDatabase import getUser
app = Flask(__name__)
app.secret_key = 'mathias1732'

#Rotas

app.register_blueprint(auth_bp, url_prefix='/auth')    
app.register_blueprint(user_bp, url_prefix='/user')


if __name__ == ("__main__"):
    app.run(debug=True, host='192.168.10.25')