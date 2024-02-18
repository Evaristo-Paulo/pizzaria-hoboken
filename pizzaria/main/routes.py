from flask import render_template, url_for, Blueprint

main = Blueprint('main', __name__)


# HOME PAGE
@main.route('/')
@main.route('/index')
@main.route('/home')
def home():
    return render_template('site/home.html')


# ABOUT-US PAGE
@main.route('/about-us')
def about():
    title = 'About us'
    return render_template('site/about.html', title=title)


# CONTACT-US PAGE
@main.route('/contact-us')
def contact():
    title = 'Contact us'
    return render_template('site/contact.html', title=title)