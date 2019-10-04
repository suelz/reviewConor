from datetime import datetime
from . import db

class Review(db.Model):
    #__tablename__ = "Review"

    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime, default = datetime.utcnow)
    review = db.Column(db.String(256), nullable = False,)

    def __repr__(self):
        return "<Review : {}>".format(self.review)
