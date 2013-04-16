#!/usr/bin/python
-*-coding:utf-8-*-


import MySQLdb


class Model:
    @staticmethod
    def initilize(settings):
        if not hasattr(Model, "_db_settings"):
            Model._db_settings = settings
  
    def __init__(self):
        self._db = None
        self._max_idle_sec = 
        self.host = Model._db_settings['host']
        self._data = {}
        

        pass
    
    def __del__(self):
        self.close()
        
    def autocommit(switch):
        pass
    
    def close(self):
        if self._db:
            self._db.close()
        self._db = None
    
    def __getitem__(self, row):
        return self._data[row]

    def _connect(self):
        self._db = MySQLdb.connect()
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
    

    



