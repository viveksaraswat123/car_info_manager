from flask import Flask, render_template, request, redirect
from main import add_car, view_all_cars

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        car = request.form["car_number"]
        owner = request.form["owner_name"]
        year = request.form["model_year"]
        km = request.form["service_km"]

        if car and owner and year and km:
            add_car(car, owner, int(year), int(km))
            return redirect("/")

    cars = view_all_cars()
    return render_template("index.html", cars=cars)

if __name__ == "__main__":
    app.run(debug=True)
