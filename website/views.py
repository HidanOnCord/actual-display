from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import singleRequest
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template("base.html", query=singleRequest.query.all())
    else:
        
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        information = [name, email, message]
        for info in information:
            if info == None:
                return render_template("error.html")
            else:
                continue
        
        theRequest = singleRequest(name=name, email=email, message=message)
        db.session.add(theRequest)
        db.session.commit()
        return render_template("base.html", query=singleRequest.query.all())
        
        
        
            
            
    

            