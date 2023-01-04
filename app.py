from flask import Flask, render_template
import terminal_api

app = Flask(__name__)
kevin= terminal_api.Players("Characters_Players", '"name"')

@app.route('/')
def index():
    return render_template("index.html", template_articles=kevin.get())

#@app.route("/recipe/<int:id>")
#def recipe(id):
  #return render_template("article.html", template_recipe=recipes[id], template_description=descriptions[id], template_ingredients=ingredients[id], template_instructions=instructions[id])

if __name__ == "__main__":
    app.run(debug=True)