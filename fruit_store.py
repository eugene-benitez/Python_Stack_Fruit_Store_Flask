from flask import Flask, render_template, request, redirect

from datetime import datetime


app = Flask(__name__)

now = datetime.now()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=["POST"])
def result():
    strawberry_from_form = request.form['Strawberry']
    raspberry_from_form = request.form['Raspberry']
    apple_from_form = request.form['Apple']
    name_from_form = request.form['name']
    student_from_form = request.form['student_id']
    return render_template("checkout.html", strawberry_on_template=strawberry_from_form, raspberry_on_template=raspberry_from_form,
                           apple_on_template=apple_from_form,
                           name_on_template=name_from_form,
                           student_on_template=student_from_form, total=int(strawberry_from_form)+int(raspberry_from_form)+int(raspberry_from_form), time=datetime.now())


if __name__ == "__main__":
    app.run(debug=True)
