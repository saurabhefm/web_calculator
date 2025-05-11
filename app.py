from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def calculator():
    return render_template("index.html")

@app.route("/evaluate", methods=["POST"])
def evaluate():
    data = request.get_json()
    expression = data.get("expression", "")
    try:
        # Safely evaluate the expression
        result = str(eval(expression))
    except Exception:
        result = "Error"
    return jsonify({"result": result})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
