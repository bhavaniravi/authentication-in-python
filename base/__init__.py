import logging

USER_NAME = "username"
PASSWORD = "password"


def authorize_user(username, password):
    logging.info(username, password)
    return USER_NAME == username and password == PASSWORD