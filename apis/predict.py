from flask import request
from flask_restx import Namespace, Resource, fields
# from flask_cors import cross_origin
from resources.predictor import predTotal, perKalimat

api = Namespace(
    'predict', 
    description='prediksi sentimen', 
    # * kontrol akses dari domain lain.
    # ! rid of this decorator in production.
    # decorators=[cross_origin()]
    )
    
jsondata = api.model('data', {
    'data': fields.String
})

parser = api.parser()
parser.add_argument('data', type=str)
@api.route('/')
class predictKalimat(Resource):
    @api.expect(jsondata, parser)
    def post(self):
        x = {}
        data = request.get_json()
        ttl = predTotal(data['data'])
        txt = perKalimat(data['data'])
        x = {
            'total': ttl, 
            'perkalimat': txt, 
            }
        return x
