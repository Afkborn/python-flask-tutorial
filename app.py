

from Python.Resources.recipe import OgrencilerRecipe,OgrenciRecipe
from flask import Flask
from flask_restful import Api




app = Flask(__name__)
api =  Api(app)

api.add_resource(OgrencilerRecipe,'/api/v1/resources/ogrenciler')
api.add_resource(OgrenciRecipe,'/api/v1/resources/ogrenciler/<int:tc_kimlik_no>')