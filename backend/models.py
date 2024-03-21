from config import db

class Contact(db.Model):
    id = db.Coloumn(db.Integer, primary_key=True)
    first_name = db.Cloumn(db.String(80), unique=False, nullable=False)