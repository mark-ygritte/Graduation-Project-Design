# -*- encoding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask import current_app
from extensions import db
import datetime

class RiskDb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, nullable=False)
    module_id = db.Column(db.Integer, nullable=False)
    r_id = db.Column(db.Integer, nullable=False)
    cve_id = db.Column(db.String(8), nullable=True)
    desc = db.Column(db.String(200), nullable=True)
    effected_factor = db.Column(db.Integer, nullable=False)
    effected_level = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Risk %r-%r-%r>' % (self.type_id, self.module_id, self.r_id)

class RiskOccurDb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, nullable=False)
    module_id = db.Column(db.Integer, nullable=False)
    r_id = db.Column(db.Integer, nullable=False)
    occur_time = db.Column(db.DateTime, default=datetime.datetime.now)
    result = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<RiskOccur %r-%r-%r-%r-%r>' % (self.type_id, self.module_id, self.r_id, self.occur_time, self.result)

def drop_all():
    db.drop_all()
