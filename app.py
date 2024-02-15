from flask import Flask, request
from urllib.parse import unquote_plus

app = Flask(__name__)

# Déclaration globale du tableau de messages
messages = ["Bonjour le jour"]

def gen_html(messages):
    html = "<ul>"
    for message in messages:
        html += f"<li>{message}</li>"
    html += "</ul>"
    return html

def add_message(messages, text):
    messages.append(text)

def remove_message(messages, index):
    if 0 <= index < len(messages):
        del messages[index]

@app.route('/', methods=['GET', 'POST', 'DELETE'])
def discussion():
    global messages
    if request.method == 'GET':
        return gen_html(messages)
    elif request.method == 'POST':
        text = unquote_plus(request.path[1:])  # récupérer le message de l'URL
        add_message(messages, text)
        return gen_html(messages)
    elif request.method == 'DELETE':
        index = int(request.path[1:])  # récupérer l'indice de l'URL
        remove_message(messages, index)
        return gen_html(messages)

if __name__ == '__main__':
    app.run()
