import sunau
import math
import audioop
import time
import random

nframes=0;
w = sunau.open("soundfiles/whatYouFeel.au", "r")
k = sunau.open("soundfiles/whatYouFeel2.au","w")
j= sunau.open("soundfiles/whatYouFeel3.au","w")
currentIndex = 0;

print (w.getsampwidth()*8 , "bits,")
print (w.getnframes(), "frames,")
print (w.getframerate() , "Hz sampling rate")
print (w.getcompname(), "compression")
print (w.getnchannels(), "channels")
print (w.getcomptype(),w.getcompname())

nframes = math.floor(w.getnframes())
audiostring = w.readframes(nframes)

uLawAudio = audioop.lin2ulaw(audiostring, 1)

'''k.setsampwidth(w.getsampwidth())
k.setframerate(w.getframerate())
k.setcomptype(w.getcomptype(),w.getcompname())
k.setnchannels(w.getnchannels())



k.writeframes(recodedaudio)'''

recodedaudio = audioop.ulaw2lin(uLawAudio, 1)

j.setsampwidth(w.getsampwidth())
j.setframerate(w.getframerate())
j.setcomptype(w.getcomptype(),w.getcompname())
j.setnchannels(w.getnchannels())

def sendPacket(packetsize, lossratio):
    previousend = 0;
    pos = j.tell()
    t0 = time.time()
    singleByte = b'\x00'
    replacement = singleByte
    for i in range (0, packetsize):
        replacement+=singleByte
        j.writeframes(replacement)
    for i in range (0, nframes, packetsize):
        randnum = random.random()
        if (randnum>lossratio):
            previousend = previousend+packetsize
            print("cont")
            continue
        else:
            newEnd = previousend+packetsize
            j.writeframes(recodedaudio[previousend:newEnd])
            previousend = previousend+packetsize
    print("time:",t0, time.time())
    

sendPacket(200, .75)
