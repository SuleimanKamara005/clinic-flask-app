from flask import Flask, render_template, request, redirect
from models import Patient
from datetime import datetime

app = Flask(__name__)

# Queue (FIFO)
queue = []

# Counter
patients_seen = 0
@app.route("/")
def home():
    return render_template("index.html", queue=queue, total=patients_seen)


@app.route("/add", methods=["GET", "POST"])
def add_patient():
    global patients_seen

    if request.method == "POST":
        name = request.form.get("name")

        patient = Patient(name)

        queue.append(patient)  # enqueue

        return redirect("/")

    return render_template("add.html")
if __name__ == "__main__":
    app.run(debug=True)