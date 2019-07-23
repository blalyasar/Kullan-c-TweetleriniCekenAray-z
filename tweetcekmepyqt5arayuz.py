"""
BİLAL YAŞAR 
TWİTTER: bilalyasar07
githup:  bilalyasar07
Medium: 

"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from twitter_scraper import get_tweets
import sys

class Pencere(QWidget):
	def __init__(self):
		super().__init__()
		self.setUI()
	def setUI(self):

		baslik = QLabel("")
		aciklamaLabel = QLabel("@'TEN SONRA TWİTTER ADRESİNİ GİRİNİZ....... @")

		self.giris = QLineEdit()
		gonder = QPushButton("TWEET + Retweet")
		gonder1 = QPushButton("SADECE TWEET")
		self.alinantweet = QTextEdit()


		#baslik
		baslik.setText("""
			<h1><font color =\"black\"> TWEET CEKME UYGULAMASI <\font></h1>
			""")
		baslik.setFont(QFont("Times New Roman",15,QFont.Bold))
		baslik.setAlignment(Qt.AlignCenter)

	
		h_box = QHBoxLayout()
		h_box.addWidget(aciklamaLabel)
		h_box.addWidget(self.giris)
		h_box.addWidget(gonder)
		h_box.addWidget(gonder1)

		#v_box
		v_box = QVBoxLayout()
		v_box.addWidget(baslik)
		v_box.addWidget(self.alinantweet)
		v_box.addLayout(h_box)

		gonder.clicked.connect(self.tweetvert)
		gonder1.clicked.connect(self.sadecetweet)

		self.setLayout(v_box)
		self.show()
		self.setWindowTitle("TWEET-RETWEET ÇEKME UYGULAMASI")

	def tweetvert(self):#tweet + rt
		adres = str(self.giris.text())

		liste = list()
		try:
			for tweet in get_tweets(adres): # kullanicinin tum tweetlerini cek ve liste halinde donguye sokar		
			#print(tweet['text'])
				liste.append(tweet['text'])
		
			toplamyazi = ""
			for i in liste:
				toplamyazi = toplamyazi + i + "\n"*3
				self.alinantweet.setText(toplamyazi)			
		except:
			pass

	def sadecetweet(self): #sadecetweet 
		adres = str(self.giris.text())

		liste = list()
		try:
				for tweet in get_tweets(adres): # kullanicinin tum tweetlerini cek ve liste halinde donguye sokar		
				#print(tweet['text'])
					if not tweet['isRetweet']:
						liste.append(tweet['text'])	
							
				toplamyazi = ""
				for i in liste:
					toplamyazi = toplamyazi + i + "\n"*3
					self.alinantweet.setText(toplamyazi)
		except:
			pass

if __name__ == "__main__":
    app=QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())