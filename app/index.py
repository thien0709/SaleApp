from flask import Flask, render_template
import dao
app = Flask(__name__)

@app.route("/")
def index():
    cates = dao.load_categories()
    return render_template("index.html",categories = cates)


if __name__ == '__main__':
    app.run(debug=True)