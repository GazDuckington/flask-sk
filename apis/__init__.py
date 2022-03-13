from flask_restx import Api
from .training import api as training
from .predict import api as predict

api = Api(
        #* alamat halaman dokumentasi
        doc='/docs/', 
        #* dokumentasi untuk halaman dokumentasi
        title='API docs', 
        description='Dokumentasi untuk endpoints API', 
        #* url prefix untuk endpoint
        prefix='/api/1'
        )

#* add routes here :)
api.add_namespace(training)
api.add_namespace(predict)