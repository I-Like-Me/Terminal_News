from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '''<h1>Hello, World!</h1>
    <=input name="text">
    <a href="/articles/<entry>">Return to home page</a>
    '''
    #<input type="submit">

@app.route('/articles/<article_name>')
def article(article_name):
    return f'''
    <h2>{article_name.replace('-', ' ').title()}</h2>
    <a href="/">Return to home page</a>
    '''