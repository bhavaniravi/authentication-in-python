from flask import Flask, make_response, session
from flask import request
import base

app = Flask("authorization")


@app.route('/auth/basic')
def basic_authorize():
    is_authorized = False
    if request.authorization:
        is_authorized = base.authorize_user(request.authorization.get("username"),
                                            request.authorization.get("password"))
    status = "Authorized" if is_authorized else "Not Authorized"
    return {"Status": status}


@app.route('/auth/form')
def form_authorize():
    is_authorized = base.authorize_user(request.form.get("username"),
                                        request.form.get("password"))
    status = "Authorized" if is_authorized else "Not Authorized"
    return {"Status": status}


@app.route('/auth/cookie')
def cookie_authorize():
    if request.cookies.get("is_authorized") == "Authorized":
        return {"Status": "Authorized"}

    if not base.authorize_user(request.args.get("username"),
                               request.args.get("password")):
        return {"Status": "Not Authorized"}

    res = make_response({"Status": "Authorized"})
    res.set_cookie("is_authorized", "Authorized")
    return res


@app.route('/auth/session')
def session_authorize():
    if session.get("is_authorized") == "Authorized":
        return {"Status": "Authorized"}

    if not base.authorize_user(request.args.get("username"),
                               request.args.get("password")):
        return {"Status": "Not Authorized"}

    res = make_response({"Status": "Authorized"})
    session["is_authorized"] =  "Authorized"
    return res


@app.route('/auth/token')
def token_authorize():
    ACTUAL_TOKEN = "ARandomToken"
    auth_headers = request.headers.get('Authorization')
    if auth_headers:
        token = auth_headers.split(" ")[1]
        if token == ACTUAL_TOKEN:
            return {"status": "Authorized"}
    if base.authorize_user(request.form.get("username"), request.form.get("password")):
        return {"token": ACTUAL_TOKEN}
    return {"status": "UnAuthorized"}



if __name__ == "__main__":
    app.secret_key = "Demo123"
    app.run(debug=True)
