from flask_restful import Resource
from flask import request, Response
import database.database as db

class CategoriasResource(Resource):

    """
        GET
        /categorias
        /categorias/<name>
    """
    def get(self, name=None):
        if(name is None):
            return db.categorias
        else:
            try:
                games = [g for g in db.games if name in db.games[g]['categorias']]
            except KeyError:
                Response("Conteúdo não econtrado.", 404)

            return games