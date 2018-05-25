from flask_restful import Resource
from flask import request, Response
import database.database as db
from operator import itemgetter

class SimilarityResource(Resource):

    """
        GET
        /similarity/<game1>
        /similarity/<game1>/<game2>
    """
    def get(self, game1, game2=None):
        if(not game2 is None):
            try:
                similares = db.similaridades[game1]['outros_jogos'][game2]
            except KeyError:
                return Response("Não encontrado.", 404)
            return similares
        else:
            try:
                similares = sorted(db.similaridades[game1]["outros_jogos"].items(), key=itemgetter(1), reverse=True)
            except KeyError:
                return Response("Não encontrado.", 404)
            return similares