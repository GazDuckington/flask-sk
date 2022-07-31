from typing import List

from flask_cors import cross_origin
from flask_restx import Namespace, Resource

from database.query import readLoglikelihood, readLogprior

from .wrapper import secure

api = Namespace(
    'logs',
    description='nilai prior dan daftar nilai likelihood setiap kata',
    decorators=[cross_origin()]
)

@api.route('/likelihoods')
class readLikelihood(Resource):
    method_decorators = [secure]
    def get(self) -> List:
        lh = readLoglikelihood()
        return [{"kata": lh[x], "likelihood": x} for x in lh]

@api.route('/prior')
class readPrior(Resource):
    method_decorators = [secure]
    def get(self) -> float:
        return readLogprior()
