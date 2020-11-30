import os
from gtts import gTTS
import PyPDF2
lan="en"
play=gTTS(text="ENTER PDF FILE NAME FOR AUDIO BOOK",lang=lan,slow=False)
play.save("p.mp3")
os.system("mpg123 p.mp3")
PdfFileName=input("ENTER PDF FILE NAME FOR AUDIO BOOK:-")
pdfReader = PyPDF2.PdfFileReader(open(PdfFileName, 'rb'))

for page_num in range(pdfReader.numPages):
	textt =  pdfReader.getPage(page_num).extractText()
	play=gTTS(text=textt,lang=lan,slow=False)
	play.save("p.mp3")
	print(textt)
	os.system("mpg123 p.mp3")

