#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   qiwei
#   E-mail  :   qqwei1123@163.com
#   Date    :   17/7/15 下午3:54
#   Desc    :   首页控制器

from core import BaseModel
from peewee import *
import datetime

class Tpl(BaseModel):
    tpl_key = CharField(unique=True)
    message = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)

class Msg(BaseModel):
    keyword = CharField(unique=True)
    tpl_key = CharField()
    content = CharField()