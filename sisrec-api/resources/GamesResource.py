from flask_restful import Resource
from flask import request, Response
import database.database as db

class GamesResource(Resource):

    """
        GET
        /games
        /games/<name>
    """
    def get(self, name=None):
        if(name is None):
            return db.games
        else:
            try:
                return db.games[name]
            except KeyError:
                return Response("Não encontrado.",status=404)