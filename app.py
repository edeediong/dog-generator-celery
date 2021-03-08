#!/usr/bin/python

import os
from dotenv import load_dotenv
from celery import Celery
from flask import Flask, render_template
import requests
import json

load_dotenv()


# used to load our env variables

# used to setup celery with flask as per the official documentation


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config["CELERY_BACKEND_URL"],
        broker=app.config["CELERY_BROKER_URL"],
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


# We use the Flask framework to create an instance of the flask app
# We then update our broker and backend urls with the env variables

flask_app = Flask(__name__)
flask_app.config.update(
    CELERY_BROKER_URL=os.environ.get("CELERY_BROKER_URL"),
    CELERY_BACKEND_URL=os.environ.get("CELERY_BACKEND_URL"),
)

# create an instance of celery using the function created earlier

celery = make_celery(flask_app)


# This fetches the links and return an array of what's consumed


@celery.task()
def get_dog_pics(breed_type, limit):
    url = "<https://dog.ceo/api/breed/>" + breed_type + "/images/random/" + limit
    r = requests.get(url)
    files = r.json()

    for file in files["message"]:
        with open("url.txt", "a") as myfile:
            myfile.write(" " + file)
    return files["message"]


# import routes as this is the client-side

import routes
