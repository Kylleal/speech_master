import requests
import numpy as np
import matplotlib.pyplot as plt
import json
"""
url = 'https://api.webempath.net/v2/analyzeWav'

apikey = 'o2lvbxnxWBVkLBFrpfb6Tzwp2RRUxsy_bIMzFbsybVo'
payload = {'apikey' : apikey}

wav = "./sample.wav"

data = open(wav, 'rb')
file = {'wav' : data}

res = requests.post(url, params=payload, files=file)
print(res.json)
"""
with open('./sample.wav', 'rb') as f:
    files = {
        'apikey': (None, 'o2lvbxnxWBVkLBFrpfb6Tzwp2RRUxsy_bIMzFbsybVo'),
        'wav': ('./sample.wav', open('./sample.wav', 'rb'))
        }

response = requests.post('https://api.webempath.net/v2/analyzeWav', files=files)
r= response.text
print(r)
res = json.loads(r)
print(type(res))
print(res)
dik = []
div = []
res.pop("error")
for k,v in res.items():
  dik.append(k)
  div.append(v)
x = np.array(div)
plt.pie(x, labels=dik, counterclock=False, startangle=90, autopct="%.1f%%",pctdistance=0.7)
plt.show()