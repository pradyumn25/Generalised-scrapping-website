from flask import Flask, request, render_template
from imageScraper import getImageUrls
import xml.dom.minidom

app = Flask(__name__)


@app.route('/', methods = ['POST', 'GET'])
def data():

    l = []

    if request.method == "POST":
        search = request.form.get("search")
        val = request.form.get("choice")

        l = []
        if val == "images":
            print("True")
            l = list(getImageUrls(search, 5))
        
    return render_template("index.html",list = l)

if __name__  ==  '__main__':
    app.run(debug=True)