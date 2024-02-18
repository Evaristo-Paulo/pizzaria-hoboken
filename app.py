from flask import Flask

app = Flask(__name__)

# HOMEPAGE
@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return 'home'


# HOMEPAGE
@app.route('/about-us')
def about():
    return 'about-us'


# HOMEPAGE
@app.route('/contact-us')
def contact():
    return 'contact-us'


if __name__ == '__main__':
    app.run(debug=True)