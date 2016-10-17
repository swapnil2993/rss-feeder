from flask import Flask, render_template, request, jsonify
from feedparser import parse

app = Flask(__name__)


@app.route('/feeds/',  methods=['POST'])
def hello_world():
    req = request.get_json(force=True)
    print req
    d = parse(req['url']).entries
    response = {"data": None}
    rlist = []
    for item in d:
        dictitem = {}
        dictitem['link'] = item['link']
        rlist.append(dictitem)
    response['data'] = rlist
    return jsonify(response)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
