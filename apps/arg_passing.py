from flask import Flask
from flask import request,Response,jsonify,render_template,send_from_directory
import numpy as np
import os, json, requests, time

app = Flask(__name__)

# get the arguments
# and return them as a json object
# supports both GET and POST

def my_parse_args():
    if request.method == 'GET':
        return request.args
    elif request.method == 'POST':
        return request.form
    else: assert False, 'request.method should be GET or POST; it was ' + str(request.method)

# return the args as a json object
@app.route("/api/my_json_example", methods = ['GET', 'POST'])
def my_json_example():
    j = my_parse_args()
    r = app.make_response(jsonify(j))
    r.mimetype='application/json'
    return render_template("output_json.html", json=r.get_json())

# return the args as an html page
@app.route("/my_html_example", methods = ['GET', 'POST'])
def my_html_example():
    t0 = time.time()
    j = my_parse_args()
    r = app.make_response(jsonify(j))
    return render_template("output_html.html", json=r.get_json(), time=np.round(time.time()-t0,6))

# calls http://recommendpapers.xyz/api/paper_search with the arguments
# outputs an html page with the results
@app.route("/my_paper_search_with_get", methods = ['GET', 'POST'])
def my_paper_search_with_get():
    t0 = time.time()
    j = my_parse_args()
    cmd='http://recommendpapers.xyz/api/paper_search?' + '&'.join(['%s=%s' % (k,j[k]) for k in j])
    jj = requests.get(cmd).json()
    if 'papers' in jj:
        return render_template("output_search_results.html", papers=jj['papers'], time=np.round(time.time()-t0,6))
    else:
        return render_template("debug.html", json=jj, time=np.round(time.time()-t0,6))

# Same as above, but uses POST to do the call
@app.route("/my_paper_search_with_post", methods = ['GET', 'POST'])
def my_paper_search_with_post():
    t0 = time.time()
    j = my_parse_args()
    cmd='http://recommendpapers.xyz/api/paper_search'
    jj = requests.post(cmd, j).json()
    # return render_template("debug.html", json=jj, time=np.round(time.time()-t0,6))
    if 'papers' in jj:
        return render_template("output_search_results.html", papers=jj['papers'], time=np.round(time.time()-t0,6))
    else:
        return render_template("debug.html", json=jj, time=np.round(time.time()-t0,6))

@app.route("/<name>", methods = ['GET', 'POST'])
def my_help_example(name):
    return render_template("help.html", name=name, supported_names=['help'])



