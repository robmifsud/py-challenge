import base64
import wave

data = open('./indian.txt', 'r').read()

wav = open('./indian.wav', 'wb')

dec = base64.b64decode(data)
print(dec)

wav.write(dec) # ans: sorry

inp = wave.open('./indian.wav', 'rb')
out = wave.open('./19_ans.wav', 'wb')

out.setnchannels(inp.getnchannels())
out.setsampwidth(inp.getsampwidth()//2)
out.setframerate(inp.getframerate()*2)

frames = inp.readframes(inp.getnframes())
wave.big_endiana = 1
out.writeframes(frames)

out.close()#ans: idiot
