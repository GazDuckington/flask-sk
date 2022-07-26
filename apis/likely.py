from typing import List
from flask_restx import Namespace, Resource
from flask_cors import cross_origin
from database.query import readLoglikelihood
from .wrapper import secure
from typing import List

api = Namespace(
    'likelihoods',
    description='daftar kata dan nilai likelihoods-nya',
    decorators=[cross_origin()]
)

@api.route('/')
class readLikelihood(Resource):
    method_decorators = [secure]
    def get(self) -> List:
        lh = readLoglikelihood()
        return [{"kata": lh[x], "likelihood": x} for x in lh]