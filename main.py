from flask import Flask, render_template
app = Flask(__name__)
menu = [
    {"dishes": "Пепероні", "price": 100},
    {"dishes": "Капрічоза ", "price": 78},
    {"dishes": "Маргарита ", "price": 100},
    {"dishes": "Баварська ", "price": 93},
    {"dishes": "Диявола", "price": 99}
]


@app.route("/")
@app.route("/index/")
def index():
    return render_template("index.html")


app.run(host="0.0.0.0", port=64000, debug=True)
