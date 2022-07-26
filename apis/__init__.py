from flask_restx import Api
from .predict import api as predict
from .likely import api as likeli

api = Api(
        #* alamat halaman dokumentasi
        doc='/docs/', 
        #* dokumentasi untuk halaman dokumentasi
        title='API docs', 
        description='Dokumentasi untuk endpoints API', 
        #* url prefix untuk endpoint
        prefix='/api'
        )

#* add routes here :)
api.add_namespace(predict)
api.add_namespace(likeli)