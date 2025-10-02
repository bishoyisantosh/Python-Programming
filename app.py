from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# simple in-memory notes list
notes = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note_text = request.form.get("note")
        if note_text:
            notes.append(note_text)
        return redirect(url_for("index"))
    return render_template("index.html", notes=notes)

@app.route("/delete/<int:note_id>")
def delete(note_id):
    if 0 <= note_id < len(notes):
        notes.pop(note_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
