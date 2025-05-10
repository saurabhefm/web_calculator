from flask import Flask, render_template, request, jsonify

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
    app.run(debug=True)
