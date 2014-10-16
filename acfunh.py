#!/usr/bin/python2
# coding=utf8

import httplib
import urllib
import urllib2
import json

req = urllib2.Request('http://h.acfun.tv/综合版1.json')
res = urllib2.urlopen(req)
json_str = res.read()
json_dic = json.loads(json_str)
print json.dumps(json_dic, indent=4,encoding='utf-8')
# print json.dumps(json_dic['data']['replys'].items()[0], indent=4)
