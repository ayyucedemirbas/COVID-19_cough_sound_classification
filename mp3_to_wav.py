from os import path
from pydub import AudioSegment

# files                                                                         
src = "pos-0422-096-cough-m-31.mp3"
dst = "pos-0422-096-cough-m-31.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")
