from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
tudu = []

@app.route("/")
def home():
    return render_template("home.html", tudu=tudu)

@app.route("/add", methods=['POST'])
def add():
    tudu_name = request.form.get("tudu")
    if tudu_name:
        tudu.append({"id": len(tudu), "name": tudu_name, "completed": False})
    return redirect(url_for("home"))

@app.route("/edit/<int:tudu_id>", methods=['POST'])
def edit_tudu(tudu_id):
    edited_name = request.form.get("edit")
    for tudus in tudu:
        if tudus["id"] == tudu_id and edited_name:
            tudus["name"] = edited_name
    return redirect(url_for("home"))

@app.route("/delete/<int:tudu_id>")
def delete_tudu(tudu_id):
    global tudu
    tudu = [tudus for tudus in tudu if tudus["id"] != tudu_id]
    return redirect(url_for("home"))

@app.route("/toggle/<int:tudu_id>")
def toggle_tudu(tudu_id):
    for tudus in tudu:
        if tudus["id"] == tudu_id:
            tudus["completed"] = not tudus["completed"]
            return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
