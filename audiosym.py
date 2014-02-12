import sunau
import math
import audioop
import time
import random

def makePacket(prev):
    randnum = random.random()
    if (randnum<lossratio):
        #print("<")
        j.writeframes(replacement)
    else:
        newEnd = prev+packetsize
        j.writeframes(recodedaudio[prev:newEnd])
        #print(">")
    prev = prev+packetsize

#initializing global variables
nframes=0;
w = sunau.open("soundfiles/whatYouFeel.au", "r")
j= sunau.open("soundfiles/whatYouFeel3.au","w")
currentIndex = 0;
replacement = b'\x00'
packetsize = 200
prev=0
lossratio = 0.0

nframes = math.floor(w.getnframes())
audiostring = w.readframes(nframes)
uLawAudio = audioop.lin2ulaw(audiostring, 1)
recodedaudio = audioop.ulaw2lin(uLawAudio, 1)

j.setsampwidth(w.getsampwidth())
j.setframerate(w.getframerate())
j.setcomptype(w.getcomptype(),w.getcompname())
j.setnchannels(w.getnchannels())

for i in range (0, packetsize):
    replacement+=b'\x00'


for i in range (0, nframes, packetsize):
    makePacket(prev)


print("finished!")
