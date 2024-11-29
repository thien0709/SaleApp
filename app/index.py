import math

from flask import render_template, request, redirect
import dao
from app import app, admin, login
from flask_login import login_user

@app.route("/")
def index():
    cate_id = request.args.get("category_id")
    kw = request.args.get("kw")
    page = request.args.get("page",1)
    product = dao.load_products(cate_id= cate_id,kw=kw,page= page)
    total = dao.count_products()
    return render_template("index.html",products = product, page = math.ceil(total/app.config['PAGE_SIZE']))

@app.route("/login", methods = ['post','get'])
def login_user():
    msg = None
    if(request.method.__eq__('POST')):
        username = request.form.get('username')
        password = request.form.get('pwd')
        user = dao.auth_user(username=username, password=password)
        if(user):
            login_user(user)
            return redirect('/')
        else:
            msg = "Login failed"
    return render_template('login.html',msg = msg)

@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)

if __name__ == '__main__':
    app.run(debug=True)