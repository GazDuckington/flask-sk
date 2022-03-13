from flask_restx import Namespace, Resource, fields
from database.query import readAllTraining

api = Namespace('training', description='Training dataset')

@api.route('/')
class Training(Resource):
    def get(self):
        return readAllTraining()