#coding=utf8
__author__ = 'snowonion'

import urllib2
import json

req=urllib2.Request('http://h.acfun.tv/综合版1.json')
res=urllib2.urlopen(req)
json_str=res.read()
print json_str