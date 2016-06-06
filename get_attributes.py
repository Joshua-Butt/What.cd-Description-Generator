"""
Get Attributes Modules for the Python What.CD Album Bio generator,

(c) 2016 Joshua Butt.
Made for twitter user @Mabbupuku
"""

# Import required modules
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.easyid3 import EasyID3
import time

class Song_Attributes:
	def __init__(self, file, type):
		if type == "MP3":
			check_if_mp3 = ", ID3=EasyID3"
		else:
			check_if_mp3 = ""
		exec "media_file = {type}(file{check})".format(type=type, check=check_if_mp3)
		
		# Generate Object Information
		self.file = file
		self.length = media_file.info.length
		self.title = media_file['title']
		self.artist = media_file['artist']
		self.album = media_file['album']
		self.track = media_file['tracknumber']
		self.year = media_file['date']

def time_str(seconds):
	return time.strftime("%M:%S", time.gmtime(seconds))