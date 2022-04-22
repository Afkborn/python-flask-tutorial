
from http import HTTPStatus
from Python.OgrenciDatabase import Database
from Python.Model.Ogrenci import Ogrenci
from flask_restful import Resource
from flask import request



class OgrencilerRecipe(Resource):
    myDb = Database()
    def get(self):
        
        ogrenciList = self.myDb.getOgrenciler()
        dictOgrenciList = []
        for ogrenci in ogrenciList:
            dictOgrenciList.append(dict(ogrenci))
            
        if (len(dictOgrenciList) == 0):
            return {
                "status": HTTPStatus.NOT_FOUND,
                'message': 'Öğrenci bulunamadı'}
        
        return {
            "status": HTTPStatus.OK,
            'Ogrenciler': dictOgrenciList}


todos = {}              
class OgrenciRecipe(Resource):
    myDb = Database()
    def get(self, tc_kimlik_no):
        ogrenci = self.myDb.getOgrenci_TcKimlikNo(tc_kimlik_no)
        if ogrenci is None:
            return {
                "status": HTTPStatus.NOT_FOUND,
                'message': 'Öğrenci bulunamadı'}
        
        dictOgrenciList = []
        dictOgrenciList.append(dict(ogrenci))
        return {
            "status": HTTPStatus.OK,
            'Ogrenciler': dictOgrenciList}
        
    def post(self, tc_kimlik_no):
        data = request.args
        try:
            name = data['name']
            surname = data['surname']
            age = data['age']
        except:
            return {
                "status": HTTPStatus.BAD_REQUEST,
                'message': 'İsim, soyisim, yaş bilgisi gerekli'}
        
        myObj = Ogrenci(name=name,surname=surname,age=age,tc_kimlik_no=tc_kimlik_no)
        if (self.myDb.addOgrenciIfNotExists(myObj)) == False:
            return {
                "status": HTTPStatus.BAD_REQUEST,
                'message': 'Öğrenci zaten mevcut'}
        else:
            return {
                "status": HTTPStatus.OK}, HTTPStatus.OK
        

         
        
        
        