"""
The flask application package.
"""

from flask import Flask
from flask import request
app = Flask(__name__)


from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

from .models import *

db.create_all()

import reviewConor.views


#review = Review(review= "Bilbo bagins was here")
#db.session.add(review)
#db.session.commit()
