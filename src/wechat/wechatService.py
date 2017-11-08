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


def processMsg(openid, appid, m):
    try:
        msgCfg=Msg.get(Msg.keyword == m)
        t = Tpl.get(Tpl.tpl_key == msgCfg.tpl_key)
    except Exception as err:
        logger.debug(err)
        t = Tpl.get(Tpl.tpl_key == 'msg')
        return reply(openid, appid, t.message, m)

    return reply(openid, appid, t.message, msgCfg.content)


def reply(openid, appid, tpl, msg):
    if not tpl.strip():
        return None
    CreateTime = int(time.time())
    out = tpl % (openid, appid, CreateTime, msg)
    return out