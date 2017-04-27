import os
from flask import Flask, request, render_template, url_for, json
app = Flask(__name__)


@app.route('/dashboard')
def hello():
    return render_template('main.html', server_name = "server1")

@app.route('/dashboard',methods=['POST'])
def post():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", "ip.json")
    data = json.load(open(json_url))
    s = request.form.get("server")
    return render_template('main.html', server_name = s)

if __name__ == '__main__':
    app.run(debug=True)
