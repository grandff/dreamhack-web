#!/usr/bin/python3
from flask import Flask, request, render_template, make_response, redirect, url_for
from selenium.common.exceptions import TimeoutException
from urllib.parse import urlparse
from selenium import webdriver
from hashlib import md5
import urllib
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

try:
    FLAG = open("./flag.txt", "r").read()
except:
    FLAG = "[**FLAG**]"

notes = {
    (FLAG, True), 
    ("Hello World", False), 
    ("DreamHack", False), 
    ("carpe diem, quam minimum credula postero", False)
}

def read_url(url, cookie={"name": "name", "value": "value"}):
    cookie.update({"domain": "127.0.0.1"})
    try:
        options = webdriver.ChromeOptions()
        for _ in [
            "headless",
            "window-size=1920x1080",
            "disable-gpu",
            "no-sandbox",
            "disable-dev-shm-usage",
        ]:
            options.add_argument(_)
        driver = webdriver.Chrome("/chromedriver", options=options)
        driver.implicitly_wait(3)
        driver.set_page_load_timeout(3)
        driver.get(url)
    except TimeoutException as e:
        driver.quit()
        return True
    except Exception as e:
        driver.quit()
        # return str(e)
        return False
    driver.quit()
    return True


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    query = request.args.get('query', None)
    if query == None:
        return render_template("search.html", query=None, result=None)
    for note, private in notes:
        if private == True and request.remote_addr != "127.0.0.1" and request.headers.get("HOST") != "127.0.0.1:8000":
            continue
        if query != "" and query in note:
            return render_template("search.html", query=query, result=note)
    return render_template("search.html", query=query, result=None)


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "GET":
        return render_template("submit.html")
    elif request.method == "POST":
        url = request.form.get("url", "")
        if not urlparse(url).scheme.startswith("http"):
            return '<script>alert("wrong url");history.go(-1);</script>'
        if not read_url(url):
            return '<script>alert("wrong??");history.go(-1);</script>'

        return '<script>alert("good");history.go(-1);</script>'


app.run(host="0.0.0.0", port=8000)
