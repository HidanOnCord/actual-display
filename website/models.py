from . import db
from sqlalchemy.sql import func


class singleRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    email = db.Column(db.String(20000))
    name = db.Column(db.String(20000))
    message = db.Column(db.String(20000))




#class emails(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    email = db.Column(db.String(20000))
#    date = db.Column(db.DateTime(timezone=True), default=func.now())
#    
#    
#class names(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(20000))
#    date = db.Column(db.DateTime(timezone=True), default=func.now())
#
#
#
#class messages(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    message = db.Column(db.String(20000))
#    date = db.Column(db.DateTime(timezone=True), default=func.now())