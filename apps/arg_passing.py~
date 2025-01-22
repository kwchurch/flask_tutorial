from flask import Flask

app = Flask(__name__)

def my_parse_args():
    if request.method == 'GET':
        return request.args
    elif request.method == 'POST':
        return request.form
    else: assert False, 'request.method should be GET or POST; it was ' + str(request.method)

@app.route("/api/my_json_example", methods = ['GET', 'POST'])
def my_json_example():
    j = my_parse_args()
    r = app.make_response(jsonify(j))
    r.mimetype='application/json'
    return render_template("output_json.html", json=r)


@app.route("/my_html_example", methods = ['GET', 'POST'])
def my_html_example():
    j = my_parse_args()
    r = app.make_response(jsonify(j))
    return render_template("output_html.html", json=r)

@app.route("/", methods = ['GET', 'POST'])
def my_help_example():
    return render_template("doc.html", json=r)


