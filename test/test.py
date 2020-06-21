import os
import traceback
import requests
import hashlib
from pyquery import PyQuery as pq

testStr = '000.wav'
print(testStr.split('.')[0])

testStr2 = 'word = %s = %d' % ('sky',1)
print(testStr2)


# md5 sha1
m = hashlib.md5()
testStr = 'asdfasdfsadfasdfdas'.encode(encoding='utf8')
m.update(testStr)
print(m.hexdigest())
print(hashlib.sha1(testStr).hexdigest())