#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: python_study
@file: main
@time: 2020/12/28 17:32
@IDE: PyCharm
@desc:

"""
from scrapy import cmdline

cmdline.execute('scrapy crawl china_weather'.split())