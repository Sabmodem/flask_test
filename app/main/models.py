from app.extensions import db


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, nullable=False)
    phone = db.Column(db.String(32), nullable=False)
    direction = db.Column(db.String(64), nullable=False)
    doctor = db.Column(db.String(64), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
