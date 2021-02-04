import requests
import pyaudio
import wave
import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import json

RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "sample.wav"
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1 
RATE = 11025

audio = pyaudio.PyAudio()

stream = audio.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = chunk)

print("Now loading...")
all = []
for i in range(0, int(RATE / chunk * RECORD_SECONDS)):
    data = stream.read(chunk) #音声を読み取って、
    all.append(data) 
print("Finished!!")

stream.stop_stream()
stream.close()
audio.terminate()
 
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(all))
waveFile.close()

with open('./sample.wav', 'rb') as f:
    files = {
        'apikey': (None, 'API key'), #ENTER YOU APIKEY 
        'wav': ('./sample.wav', open('./sample.wav', 'rb'))
        }

response = requests.post('https://api.webempath.net/v2/analyzeWav', files=files)
print(response.text)

AUDIO_FILE = "./sample.wav"

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

result=r.recognize_google(audio, language='ja-JP')

print(result)

r1 = response.text
print(r1)
res = json.loads(r1)
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
