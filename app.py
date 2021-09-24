from flask import Flask, request, render_template
from imageScraper import getImageUrls
import xml.dom.minidom

app = Flask(__name__)


@app.route('/', methods = ['POST', 'GET'])
def data():
    if request.method == "POST":
        search = request.form.get("search")
        val = request.form.get("choice")

        l = []
        if val == "images":
            print("True")
            l = list(getImageUrls(search, 50))

            impl = xml.dom.minidom.getDOMImplementation()
            dom = impl.createDocument(None, 'div', None)
            # div = dom.documentElement

            l=["a","b","c"]

            div = dom.createElement('div')
            div.setAttribute('id', 'new')

            for i in l:
                a = dom.createElement('a')
                a.setAttribute('href', 'www.google.com')
                div.appendChild(a)

        # return "you searched"+ search+"and choice = "+val

    return render_template("index.html")

if __name__  ==  '__main__':
    app.run(debug=True)