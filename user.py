#!/usr/bin/python


-*-coding:utf-8-*-

import Model
import time
import hashlib

class User(Model):

    def __init__(self):
        self.id  = None
        self.encrypt_password = None
        self.encrypt_salt = None
        self.user_name
        self.user_email
        self.create_at
        self.login_at
        self.auth_type
   def _encrypt_password(self, submmited_password):
        
        if not hasattr(self, "_salt"):
            self._salt = self._make_salt(submmited_password)
        
        return self._encrypt(submmited_password)
    
    def _encrypt(self, text):
        return self._secure_hash("%s--%s" %(self._salt, text))
    
    def _secure_hash(self, text):
        
        return hashlib.sha224(text).hexdigest()
    
    def _make_salt(self, text):
        
        return self._secure_hash(strftime('%Y-%m-%d %H:%M:%S UTC', gmtime()) + "--" + text)
    
