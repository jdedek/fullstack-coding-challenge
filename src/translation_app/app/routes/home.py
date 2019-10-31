from app import app
import os

@app.route("/")
def index():
    app_name = os.environ["APP_NAME"]

    if app_name:
        return app_name

    return "Running with Flask"