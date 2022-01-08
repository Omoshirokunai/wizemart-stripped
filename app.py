from flask import Flask, render_template, send_from_directory, request, redirect, jsonify
import os
from jumindex import jumia
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

@app.route("/", methods=['POST','GET'])
def home():
    if request.method =='POST':
        jum=jumia(request.form['sch'].replace(' ', '+'))
        return render_template('products.html',r=jum, title='Products')

    else:
        pass
    
    return render_template('index.html', title='Home')

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/product/", methods=['POST','GET'])
def product():
    
    if request.method =='POST':
        # print(request.form['sch'])
        jum=jumia(request.form['sch'].replace(' ', '+'))
        return render_template('products.html',r=jum, title='Products')
    else:
        lap=jumia("laptop")
        return render_template('products.html',r=lap, title='Products')

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("404.html"), 500

##? robots.txt
@app.route("/robots.txt")
def robots():
    return send_from_directory(app.static_folder, request.path[1:])



if __name__ == '__main__':
    app.run(debug=False)