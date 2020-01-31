import time, audioop
import pyaudio
SAMPLErate = 48000
TIMEdivlx = [0.2, 0.5, 1.0,2.0,5.0,10.0]
TIMEdiv = 0

CHUNK = int( float(SAMPLErate) * TIMEdivlx[TIMEdiv])
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 88200

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, rate=RATE,input=True, frames_per_buffer = CHUNK, channels = CHANNELS)

while True:
    data = stream.read(CHUNK)
    reading = audioop.max(data, 2)
    print(reading)

    time.sleep(.0001)
