from flask import Flask, render_template, url_for

app = Flask(__name__)


# HOME PAGE
@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return render_template('site/home.html')


# ABOUT US PAGE
@app.route('/about-us')
def about():
    title = 'About us'
    return render_template('site/about.html', title=title)


# CONTACT US PAGE
@app.route('/contact-us')
def contact():
    title = 'Contact us'
    return render_template('site/contact.html', title=title)


if __name__ == '__main__':
    app.run(debug=True)