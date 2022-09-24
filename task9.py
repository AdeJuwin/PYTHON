from flask import Flask, render_template, json, request
app = Flask(__name__, template_folder='template')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/message")
def message():
    username = request.form['username']
    massage = request.form['message']
    if username and massage:
        return json.dumps({'number of words': counter(massage)})

def counter(message):
    words = message.split()
    length = len(words)
    return int(length)


if __name__ == '__main__':
    app.run(debug=True)