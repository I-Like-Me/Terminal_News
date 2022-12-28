from flask import Flask
import assets

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '''<h1>Hello, World!</h1>
    <a href="/articles/kevin">Go to kevin</a>
    <a href="/articles/steve">Go to steve</a>
    <a href="/articles/cindy">Go to Cindy</a>
    '''

@app.route('/articles/<article_name>')
def article(article_name):
    return f'''
    <h2>{article_name.replace('-', ' ').title()}</h2>
    <a href="/">Return to home page</a>
    '''