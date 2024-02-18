from flask import Flask, render_template, url_for

app = Flask(__name__)

# HOMEPAGE
@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return render_template('site/home.html')


# HOMEPAGE
@app.route('/about-us')
def about():
    return render_template('about.html')


# HOMEPAGE
@app.route('/contact-us')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)