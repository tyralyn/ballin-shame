import sunau
import math
import audioop
import time
import random

#initializing global variables
nframes=0;
w = sunau.open("soundfiles/whatYouFeel.au", "r")
j= sunau.open("soundfiles/whatYouFeel0.au","w")
k= sunau.open("soundfiles/whatYouFeel1.au","w")
currentIndex = 0;
replacement = b'\x00'
packetsize = 100
prev=0
lossratio = 0.50
zeroes = False;

nframes = math.floor(w.getnframes())
audiostring = w.readframes(nframes)
encodedaudio = audioop.lin2ulaw(audiostring, 1)

recodedaudio = audioop.ulaw2lin(encodedaudio, 1)

j.setsampwidth(w.getsampwidth())
j.setframerate(w.getframerate())
j.setcomptype(w.getcomptype(),w.getcompname())
j.setnchannels(w.getnchannels())

k.setsampwidth(w.getsampwidth())
k.setframerate(w.getframerate())
k.setcomptype(w.getcomptype(),w.getcompname())
k.setnchannels(w.getnchannels())

'''for i in range (0, packetsize):
    replacement+=b'\x00'


for i in range (0, nframes, packetsize):
    makePacket(prev)'''

def sendPacket(packetsize, lossratio):
    previousend = 0;
    pos = j.tell()
    t0 = time.time()
    singleByte = b'\x00'
    replacement = singleByte
    newEnd = 0
    for i in range (1, packetsize):
        replacement+=singleByte
    for i in range (0, 2*nframes, packetsize):
        randnum = random.random()
        if (randnum<lossratio):
            j.writeframes(recodedaudio[previousend-packetsize:newEnd])
            k.writeframes(replacement)
            previousend = previousend+packetsize
        else:
            newEnd = previousend+packetsize
            j.writeframes(recodedaudio[previousend:newEnd])
            k.writeframes(recodedaudio[previousend:newEnd])
            previousend = previousend+packetsize
    print("time:",t0, time.time())
    

sendPacket(packetsize, lossratio)
