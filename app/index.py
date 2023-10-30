from flask import Flask, render_template, request
import dao

app = Flask(__name__)


@app.route("/")
def index():
    kw = request.args.get("kw")
    cates = dao.get_categories()
    prods = dao.get_products(kw)
    return render_template('index.html', categories=cates, products=prods)


if __name__ == '__main__':
    app.run(debug=True)
