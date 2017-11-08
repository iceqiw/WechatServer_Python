#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   qiwei
#   E-mail  :   qqwei1123@163.com
from model.tplModels import *
from config import logger
import time

def parse(data):
    appid = data.find('ToUserName').text
    openid = data.find('FromUserName').text
    msgType = data.find('MsgType').text
    if msgType == 'event':
        event = data.find('Event').text
        return processMsg(openid, appid, event)
    else:
        msg = data.find('Content').text
        return processMsg(openid, appid, msg)


def processMsg(openid, appid, msg):
    try:
        t = Tpl.get(Tpl.tpl_key == msg)
    except Exception as err:
        t = Tpl.get(Tpl.tpl_key == 'msg')
    return reply(openid, appid, t.message, msg)


def reply(openid, appid, tpl, msg):
    if not tpl.strip():
        return None
    real_msg = getMsg(msg)
    CreateTime = int(time.time())
    out = tpl % (openid, appid, CreateTime, real_msg)
    return out


def getMsg(msg):
    try:
        return Msg.get(Msg.keyword == msg).content
    except Exception as err:
        logger.info(err)
        return msg