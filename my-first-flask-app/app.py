from flask import Flask, request, jsonify, render_template
from froms import SignUpForm
app = Flask(__name__)

app.config['SECRET_KEY'] = "llave"

@app.route("/", methods = ["GET", "POST"])
def SignUp():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('user.html', result = result)

    return render_template('SignUp.html', form = form)

@app.route("/params", methods=["GET"])
def params():
    test = request.args.get("test", default = "Patriump", type=str)
    return f"Hello {test}"

@app.route("/name/<name>", methods=["GET"])
def name(name: str):
    return f"Hello {name}"

@app.route('/test', methods=['POST'])
def my_view_func():
    email = request.form.get('email')
    password = request.form.get('password')
    return f"Hello {email}"

@app.route('/json', methods=["POST"])
def json():
    data = request.get_json()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=3000)