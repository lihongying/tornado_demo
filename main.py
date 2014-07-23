#!/usr/bin/env python
#coding:utf-8

import tornado.ioloop
import tornado.web

import urls
import sys

settings = dict(
  debug=True,
  static_path="static",
  template_path="templates"
)

application = tornado.web.Application(urls.urls,**settings)

if __name__ == "__main__":
    application.listen(3000)
    tornado.ioloop.IOLoop.instance().start()
