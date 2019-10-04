"""
Routes and views for the flask application.
"""

from datetime import datetime
from reviewConor.models import Review
from flask import render_template
from flask import request
from reviewConor import *


@app.route('/', methods= ["GET", "POST"])
@app.route('/home')
def home():
    reviews = None
    if request.form:
        try:
            review = Review(review = request.form.get("review"))
            db.session.add(review)
            db.session.commit()
        except Exception as e:
            print("You goofed")
            print(e)

        reviews = Review.query.all()
        return render_template('index.html', reviews = reviews)
    else:
        reviews = Review.query.all()
        return render_template(
        'index.html',
        title='Review Conor', reviews = reviews)

    '''
    reviews = session.query(Review).all()
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Review Conor',
        reviews = reviews
    )
    '''