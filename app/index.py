from flask import render_template,request
import dao
from app import app


@app.route("/")
def index():
    cates = dao.load_categories()
    cate_id = request.args.get("category_id")
    product = dao.load_products(cate_id= cate_id)
    return render_template("index.html",categories = cates,products = product)

@app.route("/login", methods = ['post','get'])
def login_user():
    if(request.method.__eq__('POST')):
        print(request.form)
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)