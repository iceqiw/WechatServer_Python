#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   qiwei
#   E-mail  :   qqwei1123@163.com
#   Date    :   17/7/15 下午3:54
#   Desc    :   启动入口
import os
import tornado.web
import tornado.httpserver
from tornado.options import define, options
from config.router import web_handlers

settings = {'cookie_secret': 'e440769943b4e8442f09de341f3fea28462d2341f483a0ed9a3d5d3859f==78d',
            'session_secret': "3cdcb1f07693b6e75ab50b466a40b9977db123440c28307f428b25e2231f1bcc",
            'session_timeout': 3600,
            'port': 8080,
            }

define("port", default=settings['port'], help="run on the given port", type=int)

if __name__ == "__main__":
    app = tornado.web.Application(web_handlers, **settings)
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print("start：port",options.port)
    tornado.ioloop.IOLoop.instance().start()
