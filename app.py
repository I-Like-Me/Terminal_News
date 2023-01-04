from flask import Flask, render_template
import terminal_api

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", template_articles=terminal_api.Players("Characters_Players", '"name"').get()['name'])

@app.route("/articles/<int:id>")
def articles(id):
  return render_template("article.html", template_articles=terminal_api.Players("Characters_Players", '"name"').get()['name'][id])

if __name__ == "__main__":
    app.run(debug=True)