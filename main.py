import flask
from flask import Flask,request,redirect, render_template, session
from oauth import Oauth
app = Flask(__name__)
app.config["SECRET_KEY"] = "soski"

@app.route("/")
def home():
    return render_template("/var/www/html/index.html",discord_url=Oauth.discord_login_url)

@app.route("/login",methods=["get"])
def login():
    code = request.args.get("code")
    at=Oauth.get_access_token(code)
    session["token"] = at
    user = Oauth.get_user_json(at)
    user_name = user.get("username")
    user_id = user.get("discriminator")
    

if __name__ == "__main__":
    app.run(debug = True)