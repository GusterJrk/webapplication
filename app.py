# Ao abrir o GitPod, execute:
# pip intall -r requirements.txt

from flask import Flask

app = Flask(_name_)

@app.route('/')
def hello():
    return 'Hello World'

app.run()

print('Olá mundo')