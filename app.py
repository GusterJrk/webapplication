# Ao abrir o GitPod, execute:
# pip intall -r requirements.txt

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

app.run()

print('Olá mundo')