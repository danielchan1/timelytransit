# [START gae_python37_app]
from flask import Flask, render_template
from datetime import datetime, date, time

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def main():
    MINUTES_TO_BUS_STOP= 10
    estimate = 0 #+/- minutes from now until bus arrives
    accuracy = 0
    dt = datetime.now()
    return render_template('index.html',MINUTES_TO_BUS_STOP = MINUTES_TO_BUS_STOP, dt = dt)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
