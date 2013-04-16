#!/usr/bin/python
-*-coding:utf-8-*-

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options

import os.path



class LilacPicApp(tornado.web.Application): 
  
  def __init(self, **kargs):
    
    self.settings = { 
                    static_path = os.path.join(os.path.dirname(__file__), "static"),
                    template_path = os.path.join(os.path.dirname(__file__), "templates"),
                    debug = True,
                    cookie_secret = "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
                    }
    sefl.db_seetings = {
      }
                    
    self.handlers = [(r'/', IndexRequest),
                   (r'/about', AboutRequest),
                   (r'/sitemap', SiteMapRequest),
      
                   ]
    tornado.web.Application.__init__(self, self.handlers, self.settings)
    
  
if __name__ == "__main__":
    
    tornado.options.parse_command_line()
    
    server = tornado.httpserver.HTTPServer(LilacPicApp())
    
    server.listen(options.port)
    
    tornado.ioloop.IOLoop.instance().start()
    
