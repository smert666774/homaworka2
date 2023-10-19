from flask import Flask, render_template
app = Flask(__name__)
menus = [
    {"dishes": "Пепероні", "price": 100},
    {"dishes": "Капрічоза ", "price": 78},
    {"dishes": "Маргарита ", "price": 100},
    {"dishes": "Баварська ", "price": 93},
    {"dishes": "Диявола", "price": 99}
]


@app.route("/")
@app.route("/index/")
def index():
    contex = {"pizzas " : menus
    }
    return render_template("index.html",**context )

context = {"pizzas ": menus
          }


app.run(host="0.0.0.0", port=64000, debug=True)
