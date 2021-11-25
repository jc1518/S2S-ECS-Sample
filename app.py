# from flask import Flask, escape, request, render_template
import flask
import datetime
import platform
import os

app = flask.Flask(__name__)


@app.route("/")
def hello():
    name = flask.request.args.get("name", "ECS-service-demo")
    time = datetime.datetime.now()
    python_version = platform.python_version()
    aws_platform = os.environ.get("PLATFORM", "Amazon Web Services")
    return flask.render_template(
        "hello.html",
        platform=aws_platform,
        flask_version=flask.__version__,
        python_version=python_version,
        flask_url="https://palletsprojects.com/p/flask/",
        s2s_url="https://github.com/jc1518/S2S",
        time=time,
        name=name,
    )


if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG", False), host="0.0.0.0", port=5000)
