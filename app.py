from flask import Flask, render_template, url_for

app = Flask(__name__)

# HOMEPAGE
@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return render_template('site/home.html')


# HOMEPAGE
@app.route('/about-us')
def about():
    title = 'About us'
    return render_template('site/about.html', title=title)


# HOMEPAGE
@app.route('/contact-us')
def contact():
    title = 'Contact us'
    return render_template('site/contact.html', title=title)


if __name__ == '__main__':
    app.run(debug=True)