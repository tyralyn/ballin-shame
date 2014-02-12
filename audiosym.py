import sunau
import math
import audioop

def muOperation (x):
    if x<0:
        sign = -1
    else:
        sign = 1
    muValue = sign * math.log(1+255*abs(x)) / math.log(1+255)
    return muValue

def muOperation2 (x):
    return audioop.lin2ulaw(x, 1)



w = sunau.open("soundfiles/whatYouFeel.au", "r")
print (w.getsampwidth()*8 , "bits,")
print (w.getnframes(), "frames,")
print (w.getframerate() , "Hz sampling rate")
print (w.getcompname(), "compression")
print (w.getnchannels(), "channels")
print (w.getcomptype(),w.getcompname())

nframes = math.floor(w.getnframes())

k = sunau.open("soundfiles/whatYouFeel2.au", "w")
k.setnchannels(w.getnchannels())
k.setframerate(w.getframerate())
k.setsampwidth(w.getsampwidth())
k.setnframes(w.getnframes())
k.setcomptype(w.getcomptype(),w.getcompname())

audiostring = w.readframes(nframes)
#k.writeframes(audiostring)

list3 = audioop.lin2lin(audiostring, 2, 1)

m = sunau.open("soundfiles/whatYouFeel3.au", "w")
m.setnchannels(w.getnchannels())
m.setframerate(w.getframerate())
m.setsampwidth(1)
m.setcomptype('ULAW', w.getcompname())
m.writeframes(list3)

list4 = audioop.lin2lin(list3, 1, 2)
k.writeframes(list4)





