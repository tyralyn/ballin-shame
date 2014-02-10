import sunau

w = sunau.open("soundfiles/syringe.au", "r")

if w.getnchannels() == 1: print ("mono," , w.getnchannels())
else:
    print ("stereo," , w.getnchannels())

print (w.getsampwidth()*8 , "bits,")
print (w.getframerate() , "Hz sampling rate")
