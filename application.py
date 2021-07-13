from flask import Flask
from flask.templating import render_template

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html', name='home')


if __name__ == "__main__":
    app.run(debug=True)
