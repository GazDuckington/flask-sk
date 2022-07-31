from typing import List

from flask import request
from flask_cors import cross_origin
from flask_restx import Namespace, Resource, fields

from resources.predictor import perKalimat, predTotal

from .wrapper import secure

api = Namespace(
    'predict', 
    description='prediksi sentimen', 
    # ** kontrol akses dari domain lain.
    # !! rid of this decorator in production.
    decorators=[cross_origin()]
    )
    
jsondata = api.model('data', {
    'data': fields.String
})


parser = api.parser()
parser.add_argument('data', type=str)

@api.route('/')
class predictKalimat(Resource):
    method_decorators = [secure]
    @api.expect(jsondata, parser)
    def post(self) -> List:
        data = request.get_json()
        ttl = predTotal(data['data']) # type: ignore
        txt = perKalimat(data['data']) # type: ignore
        return [{"total": ttl, "detail": txt}]
