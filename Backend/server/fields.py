from flask_restful import fields, marshal_with

risk_db_fields = {
    'id': fields.Integer,
    'type_id': fields.Integer,
    'module_id': fields.Integer,
    'r_id': fields.Integer,
    'cve_id': fields.Integer,
    'desc': fields.String,
    'effected_factor': fields.Integer,
    'effected_level': fields.Integer
}

risk_db_list_fields = {
    fields.List(fields.Nested(risk_db_fields)),
}

risk_occur_db_fields = {
    'id': fields.Integer,
    'type_id': fields.Integer,
    'module_id': fields.Integer,
    'r_id': fields.Integer,
    'occur_time': fields.DateTime,
    'result': fields.Integer
}

