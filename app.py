from flask import Flask, render_template, request
from query_engine import process_query
from database import init_db

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    results = None
    if request.method == "POST":
        user_query = request.form["query"]
        results = process_query(user_query)
    return render_template("index.html", results=results)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)