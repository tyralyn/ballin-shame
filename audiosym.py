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


w = sunau.open("soundfiles/whatYouFeel.au", "r")

print (w.getsampwidth()*8 , "bits,")
print (w.getnframes(), "frames,")
print (w.getframerate() , "Hz sampling rate")
print (w.getcompname(), "compression")
nframes = math.floor(w.getnframes())

k = sunau.open("soundfiles/whatYouFeel2.au", "w")
k.setnchannels(w.getnchannels())
k.setframerate(w.getframerate())
k.setsampwidth(w.getsampwidth())
k.setnframes(w.getnframes())
k.setcomptype(w.getcomptype(),w.getcompname())

audiostring = w.readframes(nframes)
k.writeframes(audiostring)

list = []
for l in audiostring:
    list.append(l)
print ("list length:", len(list))
threshold = 2**16-1
list2 = []
for i in range (80000, 80050, 2):
    normalizedValue=(((audiostring[i]*256+audiostring[i+1])-(threshold/2))/(threshold/2))
    muValue = muOperation(normalizedValue)
    list2.append(muValue)
for item in list2:
    print(str(item).encode())
    




