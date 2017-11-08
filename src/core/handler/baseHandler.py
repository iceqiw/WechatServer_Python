#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   qiwei
#   E-mail  :   qqwei1123@163.com
#   Date    :   17/7/15 下午3:54
#   Desc    :   首页控制器

from tornado.web import RequestHandler
import tornado.escape
from ..model.baseModel import db
from config import logger



class BaseHandler(RequestHandler):

    def prepare(self):
        if db.is_closed():
            db.connect()
            logger.info('>>>>>>>>>>>>>>>>>>>>>>>>>> db open')

    def on_finish(self):
        if not db.is_closed():
            db.close()
            logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>> db close")

