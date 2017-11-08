#! /usr/bin/env python
# coding: utf-8
import logging    
import logging.config    
    
logging.config.fileConfig("logger.conf")    # 采用配置文件     
    
# create logger     
logger = logging.getLogger("wechatServer")