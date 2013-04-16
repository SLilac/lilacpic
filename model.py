#!/usr/bin/python
-*-coding:utf-8-*-


import MySQLdb


class Model:
    @staticmethod
    def initilize(settings):
        if Model.hasattr("_db_settings", None) == None:
            Model._db_settings = settings
  
    def __init__(self):
        self._db = None
        self._data = {}

        pass
    
    def __getitem__(self, row):
        return self._data[row]

    def _connect(self):
        pass

    def _reconnect(self):
        pass

    def query(self, args):

        pass

    def executemany(self):
        pass

    def getone(self, query_stmt):
        pass
    def update(self, data):
    
    def update_remote(self):
    
    @staticmethod
    def getlists()
        pass
    

    



