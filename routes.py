#!/usr/bin/python
from app import flask_app, get_dog_pics
from flask import render_template, request, redirect, url_for, jsonify


@flask_app.route("/", methods=["GET", "POST"])
def index():
    # we define dog breeds so the user chooses from this list
    dog_breeds = [
        "affenpinscher",
        "dalmatian",
        "germanshepherd",
        "kelpie",
        "labrador",
        "husky",
        "otterhound",
        "pitbull",
        "pug",
        "rottweiler",
    ]

    # we store links in this list
    pictures = []

    open_file = open("url.txt", "r")

    for images in open_file:
        image = images.replace(",", " ")
        image = image.replace('"', "")
        pictures.extend(image.split())

    # on form submission, the task is ran
    if request.method == "POST":
        if request.form["submit"] == "getDogPics":
            breed_type = request.form.get("breed")
            limit = request.form.get("limit")
            get_dog_pics.delay(breed_type, limit)
            return redirect(url_for("index"))

        # an option for clearing all the links
        elif request.form["submit"] == "clearDogPics":
            f = open("url.txt", "w")
            f.close()
            return redirect(url_for("index"))

    # Results
    return render_template("template.html", breeds=dog_breeds, link=pictures)
