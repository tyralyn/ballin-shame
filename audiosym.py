import sunau
import math
import audioop


muValueList =[0,0,1,1,2,2,2,2,3,3,3,3,3,3,3,3, 
     4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,
     5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,
     5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,
     6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,
     6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,
     6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,
     6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,
     7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,
     7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,
     7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,
     7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,
     7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,
     7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,
     7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,
     7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]


def normalize(x):
    threshold = 2*16-1
    normalizedValue = (x-(threshold/2))/(threshold/2)
    return normalizedValue
    



w = sunau.open("soundfiles/whatYouFeel.au", "r")
print (w.getsampwidth()*8 , "bits,")
print (w.getnframes(), "frames,")
print (w.getframerate() , "Hz sampling rate")
print (w.getcompname(), "compression")
print (w.getnchannels(), "channels")
print (w.getcomptype(),w.getcompname())

nframes = math.floor(w.getnframes())
audiostring = w.readframes(nframes)

audiolist = []
for l in audiostring:
    audiolist.append(l)

uLawAudio = audioop.lin2ulaw(audiostring, 1)

ulist = []
for i in uLawAudio:
    ulist.append(i)

for i in range(60060, 60100):
    print(ulist[i], audiolist[i])

k = sunau.open("soundfiles/whatYouFeel2.au","w")

k.setsampwidth(w.getsampwidth())
k.setframerate(w.getframerate())
k.setcomptype(w.getcomptype(),w.getcompname())
k.setnchannels(w.getnchannels())

recodedaudio = audioop.ulaw2lin(uLawAudio, 1)

k.writeframes(recodedaudio)

j= sunau.open("soundfiles/whatYouFeel3.au","w")




