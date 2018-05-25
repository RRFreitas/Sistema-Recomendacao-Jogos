from flask import Flask, Blueprint
from flask_restful import Api
from flask_cors import CORS
from database.database import lerArquivos
from resources.GamesResource import GamesResource
from resources.SimilarityResource import SimilarityResource
from resources.CategoriasResource import CategoriasResource

app = Flask(__name__)

app.config['DEBUG'] = True

api_bp = Blueprint('api', __name__)
api = Api(api_bp, prefix='/sisrec/api')

api.add_resource(GamesResource, '/games', '/games/<name>')
api.add_resource(SimilarityResource, '/similarity/<game1>','/similarity/<game1>/<game2>')
api.add_resource(CategoriasResource, '/categorias', '/categorias/<name>')

app.register_blueprint(api_bp)

cors = CORS(app, resources={r"/sisrec/api/*": {"origins": "*"}})

lerArquivos()

if __name__ == '__main__':
    app.run(host='0.0.0.0')