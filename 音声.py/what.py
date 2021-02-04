"""
from poster.encode import multipart_encode, MultipartParam
from poster.streaminghttp import register_openers
import urllib2

url="https://api.webempath.net/v2/analyzeWav"
register_openers()
items = []
items.append(MultipartParam('apikey', "o2lvbxnxWBVkLBFrpfb6Tzwp2RRUxsy_bIMzFbsybVo"))
items.append(MultipartParam.from_file('wav', "./sample.wav"))
datagen, headers = multipart_encode(items)
request = urllib2.Request(url, datagen, headers)
response = urllib2.urlopen(request)
if response.getcode() == 200:
    print(response.read())
else:
    print("HTTP status %d" % (response.getcode()))
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([100, 200, 300, 400, 500])
plt.pie(x)
plt.show()