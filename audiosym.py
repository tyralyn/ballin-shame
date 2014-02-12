import sunau
import math
import audioop
import time
import random

#initializing global variables
nframes=0;
w = sunau.open("soundfiles/whatYouFeel.au", "r")

J = []
J.append(sunau.open("soundfiles/whatYouFeel0a.au","w"))
J.append(sunau.open("soundfiles/whatYouFeel0b.au","w"))
J.append(sunau.open("soundfiles/whatYouFeel0c.au","w"))
J.append(sunau.open("soundfiles/whatYouFeel0d.au","w"))
J.append(sunau.open("soundfiles/whatYouFeel0e.au","w"))
J.append(sunau.open("soundfiles/whatYouFeel0f.au","w"))
J.append(sunau.open("soundfiles/whatYouFeel0g.au","w"))

K = []
K.append(sunau.open("soundfiles/whatYouFeel1a.au","w"))
K.append(sunau.open("soundfiles/whatYouFeel1b.au","w"))
K.append(sunau.open("soundfiles/whatYouFeel1c.au","w"))
K.append(sunau.open("soundfiles/whatYouFeel1d.au","w"))
K.append(sunau.open("soundfiles/whatYouFeel1e.au","w"))
K.append(sunau.open("soundfiles/whatYouFeel1f.au","w"))
K.append(sunau.open("soundfiles/whatYouFeel1g.au","w"))


k= sunau.open("soundfiles/whatYouFeel1.au","w")
currentIndex = 0;
replacement = b'\x00'
packetsize = 256
prev=0
lossratio = [.1,.2,.35,.5,.7,100]
zeroes = False;

nframes = math.floor(w.getnframes())
audiostring = w.readframes(nframes)
encodedaudio = audioop.lin2ulaw(audiostring, 1)

recodedaudio = audioop.ulaw2lin(encodedaudio, 1)

for item in J:
    item.setsampwidth(w.getsampwidth())
    item.setframerate(w.getframerate())
    item.setcomptype(w.getcomptype(),w.getcompname())
    item.setnchannels(w.getnchannels())

for item in K:
    item.setsampwidth(w.getsampwidth())
    item.setframerate(w.getframerate())
    item.setcomptype(w.getcomptype(),w.getcompname())
    item.setnchannels(w.getnchannels())

'''for i in range (0, packetsize):
    replacement+=b'\x00'


for i in range (0, nframes, packetsize):
    makePacket(prev)'''

def sendPacket(packetsize):
    previousend = 0;
    singleByte = b'\x00'
    replacement = singleByte
    newEnd = 0
    for i in range (1, packetsize):
        replacement+=singleByte
    for i in range (0, nframes, packetsize):
        randnum = random.random()
        for i in range(0,6):
            if (randnum<lossratio[i]):
                J[i].writeframes(audioop.ulaw2lin(encodedaudio[previousend-packetsize:newEnd],1))
                K[i].writeframes(replacement)
                previousend = previousend+packetsize
            else:
                newEnd = previousend+packetsize
                J[i].writeframes(audioop.ulaw2lin(encodedaudio[previousend:newEnd],1))
                K[i].writeframes(audioop.ulaw2lin(encodedaudio[previousend:newEnd],1))
                previousend = previousend+packetsize

sendPacket(packetsize)
print("finished!")
