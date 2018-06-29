'''
@author Alexandre F. Rosa
Data base Models
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class BreakLength(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    auto_break_length = db.Column(db.Integer)
    threshold = db.Column(db.Integer)

class AutoBreakRules(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    break_length_id = db.Column(db.Integer, db.ForeingKey('BreanLength.id'), nullable=False)

class LabourSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    auto_break = db.Column(db.Boolean)
    auto_break_rules_id = db.Column(db.Integer, db.ForeingKey('AutoBreakRules.id'), nullable=False)

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(80), nullable=False)
    city = db.Column(db.Text, nullable=False)
    country = db.Column(db.Text, nullable=False)
    state = db.Column(db.Text, nullable=False)
    timeZone = db.Column(db.Text)
    latitude = db.Column(db.Integer)
    longitude = db.Column(db.Integer)

    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    labour_settings_id = db.Column(db.Integer, db.ForeingKey('LabourSettings.id'), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeingKey('Location.id'), nullable=False)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    hourly_wage = db.Column(db.Text)
    photo = db.Column(db.Text)
    email = db.Column(db.Text)





