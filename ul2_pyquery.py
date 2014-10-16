__author__ = 'tianchi.ltc'

import urllib2
from pyquery import PyQuery as _

Q_HOST = 'baidu.com'
QUERY = 'ip=' + Q_HOST
HOST_N_METHOD = 'http://ip.cn/index.php'

req = urllib2.Request(HOST_N_METHOD)
res = urllib2.urlopen(req, QUERY)
str = res.read()
# print str

# doc=pq(url=HOST_N_METHOD)  # encoding issue
doc = _(str)  # encoding issue
# print doc

print doc('.well')
