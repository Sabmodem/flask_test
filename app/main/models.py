from app.extensions import db
import json

class ModelsEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Appointment):
      return {
          'id': obj.id, 
          'name': obj.name, 
          'direction': obj.direction, 
          'doctor': obj.doctor, 
          'date': obj.date, 
          'time': obj.time, 
          'phone': obj.phone 
          }
    return json.JSONEncoder.default(self, obj)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, nullable=False)
    phone = db.Column(db.String(32), nullable=False)
    direction = db.Column(db.String(64), nullable=False)
    doctor = db.Column(db.String(64), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
