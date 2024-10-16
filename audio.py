from pydub import AudioSegment

audio = AudioSegment.from_file("Nika.m4a", format="m4a")
audio.export("Nika.mp3", format="mp3")