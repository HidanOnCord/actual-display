
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    
    
    if request.method == 'POST':
        a = request.form
        print(a['name'])
        return render_template('base.html', a=a)
    else:
        return render_template('base.html', a=None)

    


