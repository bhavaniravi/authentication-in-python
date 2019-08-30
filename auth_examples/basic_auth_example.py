from flask import Flask
from flask import request
import base

app = Flask("basic_auth")


@app.route('/auth')
def authorize():
    is_authorized = False
    if request.authorization:
        is_authorized = base.authorize_user(request.authorization.get("username"),
                                            request.authorization.get("password"))
    status = "Authorized" if is_authorized else "Not Authorized"
    return {"Status": status}




if __name__ == "__main__":
    app.run(debug=True)
