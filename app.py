"""
pip install pipenv
pipenv shell
pip install flask

pip freeze > requirements.txt
"""


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)