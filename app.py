# Ao abrir o GitPod, execute:
# pip intall -r requirements.txt

from flask import Flask, render_template

app = Flask(__name__)




@app.route('/')
def hello():
    return render_template('index.html', nomes=['Calvo', 'Deizy', 'Igor'])

app.run(debug=True)