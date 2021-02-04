import pyaudio
import wave
import numpy as pd
import matplotlib.pyplot as plt
import requests


chunk = 1024
FORMAT = pyaudio.paInt16

CHANNELS = 1 #モノラル（2にするとステレオ）
RATE = 11025
RECORD_SECONDS = 3 #時間

p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = chunk)

print("Now Recording...")
all = []
for i in range(0, int(RATE / chunk * RECORD_SECONDS)):
    data = stream.read(chunk) #音声を読み取って、
    all.append(data) #データを追加

#レコード終了
print("Finished Recording.")

stream.close()
p.terminate()

data = b"".join(all)

result = pd.frombuffer(data,dtype="int16") / float(2**15)

plt.plot(result)
plt.show()

