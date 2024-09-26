from flask import Flask, render_template, request, send_from_directory
import generator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_no = int(request.form["user_no"])
        file = generator.make(user_no)
        return send_from_directory(filename='file.csv')
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
