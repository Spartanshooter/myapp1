from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    
@app.route('/hello')
def hello():
    return 'Hello again!'
    
@app.route('/formulari')
def formulari_get():
    # mostrem el formulari
    return """
<form method='post'>
    Introdueix el teu nom:
    <input name='nom' type='text' />
    <br>
    <input type='submit'>
</form>
"""
 
@app.route('/formulari', methods=['POST'])
def formulari_post():
    # processem les dades del formulari
    nom = request.form["nom"]
    return "Salut, {}".format(nom)
