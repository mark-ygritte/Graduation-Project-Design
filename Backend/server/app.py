# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify, request
from flask_restful import abort, Resource, marshal_with, reqparse
from flask_cors import CORS
from fields import risk_db_fields, risk_db_list_fields, risk_occur_db_fields
from extensions import app, db, api
from db_config import RiskDb, RiskOccurDb
import json

@app.route('/__health')
def health_check():
    return 'OK'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_risk', methods=['POST'])
def add_risk():
    try:
        type_id = request.form['type_id']
        module_id = request.form['module_id']
        r_id = request.form['r_id']
        desc = request.form['desc']
        effected_factor = request.form['effected_factor']
        effected_level = request.form['effected_level']
    except:
        return "Parameters missing"
    with app.app_context():
        new_risk = RiskDb(type_id=type_id, module_id=module_id, r_id=r_id, desc=desc, effected_factor=effected_factor, effected_level=effected_level)
        db.session.add(new_risk)
        db.session.commit()
    return "ok"

@app.route('/add_occur', methods=['POST'])
def add_risk_occur():
    try:
        type_id = request.form['type_id']
        module_id = request.form['module_id']
        r_id = request.form['r_id']
        result = request.form['result']
    except:
        return "Parameters missing"
    with app.app_context():
        new_risk_occur = RiskOccurDb(type_id=type_id, module_id=module_id, r_id=r_id, result=result)
        db.session.add(new_risk_occur)
        db.session.commit()
    return "ok"

class RiskDbApi(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('cve_id', type=int, help='cve should be an integer', required=False)
        self.parser.add_argument('desc', type=str, help='desc should be string', required=False)
        self.parser.add_argument('effected_factor', type=int, help='effected_factor should be an integer', required=True)
        self.parser.add_argument('effected_level', type=int, help='effected_level should be an integer', required=True)

    def abort_if_risk_doesnt_exist(self,type_id, module_id, r_id):
        res = RiskDb.query.filter_by(type_id=type_id, module_id=module_id, r_id=r_id).first()
        if res == None:
            abort(404, message="Risk doesn't exist")
        else:
            return res
        
    @marshal_with(risk_db_fields)
    def get(self, type_id, module_id, r_id):
        t = self.abort_if_risk_doesnt_exist(type_id, module_id, r_id)
        return t

    @marshal_with(risk_db_fields)
    def put(self, type_id, module_id, r_id):
        args = self.parser.parse_args()
        t = self.abort_if_risk_doesnt_exist(type_id, module_id, r_id)
        
        if args['cve_id'] != None:
            t.cve_id = args['cve_id']
        elif args['desc'] != None:
            t.desc = args['desc']
        
        t.effected_factor = args['effected_factor']
        t.effected_level = args['effected_level']

        with app.app_context():
            db.session.add(t)
            db.session.commit()
        
        return self.abort_if_risk_doesnt_exist(type_id, module_id, r_id)
    
    def delete(self, type_id, module_id, r_id):
        t = self.abort_if_risk_doesnt_exist(type_id, module_id, r_id)

        with app.app_context():
            db.session.delete(t)
            db.session.commit()
        
        return "ok"

class RiskDbListApi(Resource):
    
    def get(self):
        res = []
        for item in RiskDb.query.all():
            res.append({
                'id': item.id,
                'type_id': item.type_id,
                'module_id': item.module_id,
                'r_id': item.r_id,
                'desc': item.desc,
                'effected_factor': item.effected_factor,
                'effected_level': item.effected_level
            })
            
        return jsonify(res)


api.add_resource(RiskDbApi, '/riskDb/<int:type_id>/<int:module_id>/<int:r_id>')
api.add_resource(RiskDbListApi, '/riskDbs')

class RiskOccurApi(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('result', type=int, help='result should be an integer', required=True)
    
    def abort_if_risk_occur_doesnt_exist(self,type_id, module_id, r_id):
        res = RiskOccurDb.query.filter_by(type_id=type_id, module_id=module_id, r_id=r_id).first()
        if res == None:
            abort(404, message="Risk occur doesn't exist")
        else:
            return res

    @marshal_with(risk_occur_db_fields)
    def get(self, type_id, module_id, r_id):
        t = self.abort_if_risk_occur_doesnt_exist(type_id, module_id, r_id)
        return t
    
    @marshal_with(risk_occur_db_fields)
    def put(self, type_id, module_id, r_id):
        args = self.parser.parse_args()
        t = self.abort_if_risk_occur_doesnt_exist(type_id, module_id, r_id)
        
        t.result = args['result']

        with app.app_context():
            db.session.add(t)
            db.session.commit()
        
        return self.abort_if_risk_occur_doesnt_exist(type_id, module_id, r_id)
    
    def delete(self, type_id, module_id, r_id):
        t = self.abort_if_risk_occur_doesnt_exist(type_id, module_id, r_id)

        with app.app_context():
            db.session.delete(t)
            db.session.commit()
        
        return "ok"
    
class RiskOccurDbListApi(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('type_id', type=int, help='type id should be an integer', required=True)
        self.parser.add_argument('module_id', type=int, help='module id should be an integer', required=False)
        self.parser.add_argument('r_id', type=int, help='risk id should be an integer', required=False)

    def get(self):
        res = []
        for item in RiskOccurDb.query.all():
            res.append({
                'id': item.id,
                'type_id': item.type_id,
                'module_id': item.module_id,
                'r_id': item.r_id,
                'result': item.result
            })
            
        return jsonify(res)
    
    def post(self):
        args = self.parser.parse_args()
        res = []
        all = None
        app.logger.debug(args)
        if args['r_id'] == None and args['module_id'] == None:
            all = RiskOccurDb.query.filter_by(type_id=args['type_id']).all()
        elif args['module_id'] == None:
            all = RiskOccurDb.query.filter_by(type_id=args['type_id'], r_id=args['r_id']).all()
        elif args['r_id'] == None:
            all = RiskOccurDb.query.filter_by(type_id=args['type_id'], module_id=args['module_id']).all()
        else:
            all = RiskOccurDb.query.all()

        for item in all:
            res.append({
                'id': item.id,
                'type_id': item.type_id,
                'module_id': item.module_id,
                'r_id': item.r_id,
                'result': item.result
            })
            
        return jsonify(res)

api.add_resource(RiskOccurApi, '/riskOccurDb/<int:type_id>/<int:module_id>/<int:r_id>')
api.add_resource(RiskOccurDbListApi, '/riskOccurDbs')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.debug = True
    app.run(host="0.0.0.0", port="8000")