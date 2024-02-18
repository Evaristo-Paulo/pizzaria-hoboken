from flask import Flask

app = Flask(__name__)

# HOMEPAGE
@app.route('/')
def home():
    return 'home'


if __name__ == '__main__':
    app.run(debug=True)